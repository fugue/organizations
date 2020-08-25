# pylint: disable=bad-continuation
# pylint: disable=bare-except
import argparse
import json
import os
import sys
import time
from typing import List, Set, Dict
from fugue_api_client.swagger_client import (
    Configuration,
    ApiClient,
    EnvironmentsApi,
    MetadataApi,
    Environment,
    CreateEnvironmentInput,
    ProviderOptions,
    ProviderOptionsAws,
)

FUGUE_API_HOST = os.environ.get('FUGUE_API_HOST', 'api.riskmanager.fugue.co')
FUGUE_API_VERSION = os.environ.get('FUGUE_API_VERSION', 'v0')
FUGUE_API_ID = os.environ.get('FUGUE_API_ID')
FUGUE_API_SECRET = os.environ.get('FUGUE_API_SECRET')

# One day in seconds
ONE_DAY = 86400


def initialize_client() -> ApiClient:
    """
    Creates a swagger client for the Fugue API using credentials passed via
    environment variables.
    """
    c = Configuration()
    c.host = f'https://{FUGUE_API_HOST}/{FUGUE_API_VERSION}'
    c.username = FUGUE_API_ID
    c.password = FUGUE_API_SECRET
    client = ApiClient(configuration=c)
    return client


def create_aws_environment(
    environments_api: EnvironmentsApi,
    name: str,
    role_arn: str,
    compliance_families: List[str] = None,
    survey_resource_types: List[str] = None,
) -> Environment:
    """
    Create an AWS environment in Fugue with the given settings.
    """
    aws_provider_opts = ProviderOptionsAws(regions=["*"], role_arn=role_arn)
    environment: Environment = environments_api.create_environment(
        CreateEnvironmentInput(
            name=name,
            provider='aws',
            provider_options=ProviderOptions(aws=aws_provider_opts),
            survey_resource_types=survey_resource_types,
            compliance_families=compliance_families,
            scan_schedule_enabled=True,
            scan_interval=ONE_DAY,
        ))
    assert len(environment.id) > 0
    print(f"environment {environment.id} created")
    return environment


def read_json(path):
    with open(path, 'r') as f:
        return json.loads(f.read())


def filter_accounts(org, chosen_ous: List[str]) -> List[Dict[str, str]]:
    """
    Returns a list of account objects that match the specified list of OUs.
    The OUs list may contain '*' (ALL), OU IDs, or OU names.
    """
    ous: Set[str] = set(chosen_ous)
    if '*' in ous:
        return org['accounts']
    result = []
    for acc in org['accounts']:
        if acc['ou_name'] in ous:
            result.append(acc)
        elif acc['ou_id'] in ous:
            result.append(acc)
    return result


def main():
    parser = argparse.ArgumentParser(
        description='Create environments in Fugue')
    parser.add_argument('--ous', default=['*'], nargs='+',
                        help='Organizational units (default: all OUs)')
    parser.add_argument('--role-name', default='FugueRole',
                        help='Name of the Fugue role in the AWS accounts')
    parser.add_argument('--sleep', default=3, type=int,
                        help='Seconds to sleep between create calls')
    parser.add_argument('--compliance-families',
                        default=['CIS', 'FBP'], nargs='+',
                        help='Compliance families to enable')
    args = parser.parse_args()

    if not FUGUE_API_ID:
        print('FUGUE_API_ID is not set')
        sys.exit(1)

    if not FUGUE_API_SECRET:
        print('FUGUE_API_SECRET is not set')
        sys.exit(1)

    sleep_time = args.sleep if args.sleep >= 1 else 1
    api_client: ApiClient = initialize_client()
    metadata_client: MetadataApi = MetadataApi(api_client)
    resource_types = metadata_client.get_resource_types('aws').resource_types
    env_api: EnvironmentsApi = EnvironmentsApi(api_client)

    # Account ID will be filled into the ARN later for each account
    role_fmt = f'arn:aws:iam::%s:role/{args.role_name}'

    try:
        org = read_json('organization.json')
    except:
        print('File organizations.json not found. Refer to the README.')
        sys.exit(1)

    accounts = filter_accounts(org, args.ous)
    if not accounts:
        print('No matching accounts found.')
        sys.exit(1)

    print('Creating environments for', len(accounts), 'accounts')

    for i, account in enumerate(accounts):
        print(i + 1, account['account_id'], account['account_name'])
        role_arn = role_fmt % account['account_id']
        create_aws_environment(
            env_api,
            account['account_name'],
            role_arn,
            args.compliance_families,
            survey_resource_types=resource_types)
        time.sleep(sleep_time)


if __name__ == '__main__':
    main()
