"""
Creates a stackset in an AWS organization master account and provision stack
instances across any number of organizational units (OUs) in the organization.

Reference:
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-enable-trusted-access.html

Requirements:
 * Installed botocore via `pip install botocore` or equivalent
 * Python 3.6+
 * Active AWS credentials belonging to your organization's master account
 * The credentials must include:
    * AWSOrganizationsReadOnlyAccess
    * AWSCloudFormationFullAccess
"""
# pylint: disable=broad-except
import argparse
import sys
import botocore
import botocore.session
from botocore.exceptions import ClientError


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def fail(message, err=None):
    eprint(f'ERROR: {message}')
    if err:
        eprint(err)
    sys.exit(1)


def read_file(path):
    with open(path, 'r') as f:
        return f.read()


def create_stack_set(cfn_client, stackset_name, description, tmpl, parameters):
    params = [dict(ParameterKey=p[0], ParameterValue=p[1]) for p in parameters]
    auto_deployment = {'Enabled': True,
                       'RetainStacksOnAccountRemoval': False}
    return cfn_client.create_stack_set(
        StackSetName=stackset_name,
        Description=description,
        TemplateBody=tmpl,
        Capabilities=['CAPABILITY_NAMED_IAM'],
        Tags=[],
        PermissionModel='SERVICE_MANAGED',
        AutoDeployment=auto_deployment,
        Parameters=params)


def create_stack_instances(cfn_client, stackset_name, region, ous):
    print('create instances', ous)
    return cfn_client.create_stack_instances(
        StackSetName=stackset_name,
        Regions=[region],
        DeploymentTargets={'OrganizationalUnitIds': ous},
        OperationPreferences={
            'FailureToleranceCount': 20,
            'MaxConcurrentCount': 20,
        }
    )['OperationId']


def list_children(orgs_client, parent_id, child_type):
    children = []
    next_token = None
    while True:
        kwargs = {'ParentId': parent_id, 'ChildType': child_type}
        if next_token:
            kwargs['NextToken'] = next_token
        resp = orgs_client.list_children(**kwargs)
        children.extend(resp['Children'])
        next_token = resp.get('NextToken')
        if not next_token:
            return children


def get_root(orgs_client):
    roots = orgs_client.list_roots()['Roots']
    if len(roots) != 1:
        raise ValueError('Expected exactly one root; got %d' % len(roots))
    return roots[0]['Id']


def list_organizational_units(orgs_client, parent_id=None):
    # If no parent was specified, automatically choose the root OU
    if parent_id is None:
        parent_id = get_root(orgs_client)
    # Find immediate children and then recurse
    ous = list_children(orgs_client, parent_id, 'ORGANIZATIONAL_UNIT')
    for ou in ous:
        ous.extend(list_organizational_units(orgs_client, ou['Id']))
    return ous


def validate_ous(requested_ous, existing_ous):
    """
    Confirms that the specified organizational unit IDs exist. Also converts
    an asterisk to all known OUs. Raises an error on an unknown OU.
    """
    if not requested_ous:
        raise ValueError('No organizational units specified')
    requested = set(requested_ous)
    existing = set(existing_ous)
    if '*' in requested:
        return sorted(list(existing))
    missing_ous = requested - existing
    if missing_ous:
        raise ValueError(f'Unknown OUs: {missing_ous}')
    return sorted(list(requested))


def main():
    parser = argparse.ArgumentParser(
        description='Create a stackset in an AWS master account')
    parser.add_argument('-t', '--template',
                        default='./cloudformation/account.yaml',
                        help='Cloudformation template for stacks')
    parser.add_argument('-n', '--name', required=True, help='Stackset name')
    parser.add_argument('-d', '--description', required=True,
                        help='Stackset description')
    parser.add_argument('--ous', default=['*'], nargs='+',
                        help='Organizational units (default: all OUs)')
    parser.add_argument('--parameters', default=[], nargs='+',
                        help='Stack template parameters in k=v format')
    parser.add_argument('-r', '--region', default='us-east-1',
                        help='AWS region (default: us-east-1)')
    args = parser.parse_args()

    try:
        session = botocore.session.get_session()
        sts_client = session.create_client('sts')
        org_client = session.create_client('organizations')
        cfn_client = session.create_client('cloudformation')
    except Exception as exc:
        fail('Failed to create AWS clients', exc)

    try:
        ident = sts_client.get_caller_identity()
    except ClientError as exc:
        fail('Failed to get AWS identity', exc)

    try:
        org = org_client.describe_organization()['Organization']
    except Exception as exc:
        fail('Failed to describe AWS organization', exc)

    print(f'Identity ARN: {ident["Arn"]}')
    print(f'Identity account: {ident["Account"]}')
    print(f'Master account: {org["MasterAccountId"]}')
    print(f'Organization ID: {org["Id"]}')

    if ident['Account'] != org['MasterAccountId']:
        fail('This script must be run with credentials for the '
             'organization master account')

    try:
        template = read_file(args.template)
    except Exception as exc:
        fail('Failed to read cloudformation template', exc)

    try:
        params = [p.split('=') for p in args.parameters]
        create_stack_set(cfn_client, args.name,
                         args.description, template, params)
        print(f'Stackset {args.name} created')
    except Exception as exc:
        fail('Failed to create stackset', exc)

    if not args.ous:
        print('No organizational units specified')
        sys.exit(0)

    existing_ous = [ou['Id'] for ou in list_organizational_units(org_client)]
    ous = validate_ous(args.ous, existing_ous)
    create_stack_instances(cfn_client, args.name, args.region, ous)
    print(f'Creating stacks instances in {len(ous)} ous')
    print(" ".join(ous))


if __name__ == '__main__':
    main()
