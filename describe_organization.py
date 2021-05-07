"""
Describes your AWS organization.

This script uses the AWS Organizations API to discover all active
organizational units (OUs) and accounts within your AWS organization.

The accounts are output to stdout in a table and to a file in JSON format.

Requirements:
 * Installed botocore via `pip install botocore` or equivalent
 * Python 3.6+
 * Active AWS credentials belonging to your organization's master account
 * The credentials must include AWSOrganizationsReadOnlyAccess permissions
   or equivalent: "organizations:Describe*", "organizations:List*"
"""
# pylint: disable=broad-except
import argparse
import json
import sys
import botocore
import botocore.session
from botocore.exceptions import ClientError


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def list_roots(client):
    return map(ou_json, client.list_roots()["Roots"])


def find_children(client, root, child_type):
    children = []
    next_token = None
    while True:
        kwargs = {"ParentId": root["ou_id"], "ChildType": child_type}
        if next_token:
            kwargs["NextToken"] = next_token
        resp = client.list_children(**kwargs)
        children.extend(resp["Children"])
        next_token = resp.get("NextToken")
        if not next_token:
            break
    return children


def find_child_accounts(client, root):
    children = find_children(client, root, "ACCOUNT")
    children_accounts = describe_accounts(client, map(account_json, children))
    return list(filter(lambda c: c["status"] == "ACTIVE", children_accounts))


def find_child_org_units(client, root):
    children = find_children(client, root, "ORGANIZATIONAL_UNIT")
    return describe_org_units(client, map(ou_json, children))


def describe_accounts(orgs_client, accounts):
    result = []
    for account in accounts:
        acc = orgs_client.describe_account(AccountId=account["account_id"])["Account"]
        result.append(account_json(acc))
    return result


def describe_org_units(orgs_client, ous):
    result = []
    for ou in ous:
        desc = orgs_client.describe_organizational_unit(
            OrganizationalUnitId=ou["ou_id"]
        )["OrganizationalUnit"]
        result.append(ou_json(desc))
    return result


def account_json(acc):
    return dict(
        account_id=acc["Id"],
        account_name=acc.get("Name", ""),
        arn=acc.get("Arn", ""),
        email=acc.get("Email", ""),
        status=acc.get("Status", ""),
        ou_id="",
        ou_name="",
    )


def ou_json(ou):
    return dict(
        ou_id=ou["Id"],
        ou_name=ou.get("Name", ""),
        arn=ou.get("Arn", ""),
        parent_id="",
        parent_name="",
    )


def discover_children(orgs_client, root):
    # Find immediate children accounts and organizational units
    accounts = find_child_accounts(orgs_client, root)
    ous = find_child_org_units(orgs_client, root)
    # Set the parent on these children
    for acc in accounts:
        acc["ou_id"] = root["ou_id"]
        acc["ou_name"] = root["ou_name"]
    for ou in ous:
        ou["parent_id"] = root["ou_id"]
        ou["parent_name"] = root["ou_name"]
    # Recurse down the tree of organizational units
    for ou in ous:
        child_accounts, child_ous = discover_children(orgs_client, ou)
        accounts.extend(child_accounts)
        ous.extend(child_ous)
    return accounts, ous


def longest(rows, column):
    """
    Returns the width required for the given column
    """
    col_max = max([len(str(row[column])) for row in rows])
    return max(len(column), col_max)


def show_table(rows, columns, separator=" | ", header=True):
    """
    Prints a table with the given rows and column names to stdout
    """
    # Calculate column widths
    column_widths = [longest(rows, column) for column in columns]
    column_formats = ["%%-%ds" % width for width in column_widths]
    horiz_line = "=" * (sum(column_widths) + len(separator) * (len(columns) - 1))
    # Print table header
    if header:
        print(horiz_line)
        column_headers = [
            column_formats[i] % columns[i].upper() for i, _ in enumerate(columns)
        ]
        print(separator.join(column_headers))
        print(horiz_line)
    # Print table rows
    for row in rows:
        column_values = [column_formats[i] % row[col] for i, col in enumerate(columns)]
        print(separator.join(column_values))


def get_caller_identity(sts_client):
    return sts_client.get_caller_identity()


def describe_organization(org_client):
    return org_client.describe_organization()["Organization"]


def discover_organization(org_client):
    ous, accounts = [], []
    for root in list_roots(org_client):
        root_accounts, root_ous = discover_children(org_client, root)
        accounts.extend(root_accounts)
        ous.extend(root_ous)
    return accounts, ous


def fail(message, err=None):
    eprint(f"ERROR: {message}")
    if err:
        eprint(err)
    sys.exit(1)


def write_json(path, data):
    text = json.dumps(data, sort_keys=True, indent="\t")
    with open(path, "w") as f:
        f.write(text)


def main():
    parser = argparse.ArgumentParser(description="Describes your AWS organization")
    parser.add_argument(
        "-o", "--output", default="organization.json", help="Path to save JSON output"
    )
    args = parser.parse_args()

    try:
        session = botocore.session.get_session()
        sts_client = session.create_client("sts")
        org_client = session.create_client("organizations")
    except Exception as exc:
        fail("Failed to create AWS clients", exc)

    try:
        ident = get_caller_identity(sts_client)
    except ClientError as exc:
        fail("Failed to get AWS identity", exc)

    try:
        org = describe_organization(org_client)
    except ClientError as exc:
        fail("Failed to describe AWS organization", exc)

    print(f'Identity ARN: {ident["Arn"]}')
    print(f'Identity account: {ident["Account"]}')
    print(f'Master account: {org["MasterAccountId"]}')
    print(f'Organization ID: {org["Id"]}')

    if ident["Account"] != org["MasterAccountId"]:
        fail(
            "This script must be run with credentials for the "
            "organization master account"
        )

    try:
        accounts, ous = discover_organization(org_client)
    except ClientError as exc:
        fail("Failed to discover organization accounts")

    accounts.sort(key=lambda acc: acc["ou_name"] + "_" + acc["account_name"])
    ous.sort(key=lambda ou: ou["ou_name"])

    print()
    print(f"Found {len(ous)} OUs")
    print(f"Found {len(accounts)} accounts")
    print()

    # Human readable output showing all discovered accounts
    columns = ["ou_id", "ou_name", "account_id", "account_name", "email"]
    show_table(accounts, columns)

    # Structured output saved to disk
    if args.output:
        write_json(
            args.output,
            {
                "master_account_id": org["MasterAccountId"],
                "organization_id": org["Id"],
                "accounts": accounts,
                "organizational_units": ous,
            },
        )
        print(f"\nSaved accounts as JSON to {args.output}")


if __name__ == "__main__":
    main()
