# AWS Organizations and Fugue

Scripts in this repository help create AWS IAM roles for secure cross-account
scan access (read-only) to accounts within an AWS organization.

We will use [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html)
and [CloudFormation Stacksets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html)
to provision an IAM role in multiple accounts in one operation.

## Dependenices

Using these scripts requires the following:

- Python 3.6+
- AWS credentials for your **AWS organization root account**
- GNU Make
- AWS CLI and Botocore (these are automatically installed in a virtualenv)

This was tested on MacOS, but should also work on Linux and WSL on Windows.
By running Make commands as described below, the required Python dependencies
will automatically be installed for you.

## Step 1: Your Fugue Account and IAM Role External ID

Your Fugue account will have an associated [External ID](https://aws.amazon.com/blogs/security/how-to-use-external-id-when-granting-access-to-your-aws-resources/)
associated with it. You should [sign up](https://riskmanager.fugue.co/register)
for Fugue now if you haven't yet. Once you have a Fugue account, you can retreive your external ID as follows:

- Sign into the AWS console of one of your accounts
- In another tab, sign into the Fugue console
- Click _Create New Environment_
- Choose the AWS cloud provider and provide a name
- Use defaults for regions and resource types
- Click _Review Stack in AWS Console_
- Click _View in Designer_ in the AWS console webpage
- Copy the external ID from the YAML file. The line starts with `"sts:ExternalId"`.

Alternatively, you can reach out to `support@fugue.co` for help retrieving this
value.

## Step 2: Gather information about your AWS organization

**Prerequisite**: You must have AWS credentials **for your organization root account** active, with
the `AWSOrganizationsReadOnlyAccess` policy or equivalent permissions attached to your user or role.

Run the following to gather account and organizational unit (OU) information
from your AWS organization and write it to a JSON-formatted output file:

```bash
make organization.json
```

This creates `organization.json` in the current directory.

## Step 3: Create a Cloudformation Stackset to provision IAM roles

With the External ID from Step 1 in hand, we can now create the Stackset. You
will still need AWS credentials for your root account active, with the
`AWSCloudFormationFullAccess` and `AWSOrganizationsReadOnlyAccess` or equivalent
policies attached. See [template.yaml](template.yaml) for the CloudFormation template
used to create the role in each AWS account.

Run the following command, replacing `<extid>` with your value:

```bash
make stackset EXTERNAL_ID=<extid>
```

You may also _optionally_ override the following variables:

- `ROLE_NAME=<name>` to customize the role name in each account (default: `Fugue-[timestamp]`)
- `OU=<ou_id>` to deploy the roles to accounts in one OU only (default: all OUs)
- `STACKSET_NAME=<name>` to customize the Stackset name (default: `Fugue`)
- `TRUSTED_ACCOUNT_ID=<aws_account_id>` to override the account to grant access to (default: Fugue's AWS account)
- `TRUSTED_PRINCIPAL=<principal>` to grant access to a specific role
- `EVENT_BUS_ARN=<arn>` destination for CloudTrail events

It may take about 15 minutes for the Stackset to create the corresponding
Stacks and Roles in each AWS account. Monitor this progress via the
[Stacksets](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacksets)
webpage in the AWS console.

## Step 4: Determine the Role Name in each Account

You can now find the name of the role that was provisioned in each AWS account
in a couple different ways. The name should look like `Fugue-[timestamp]`.

Option 1: read the local file that was written automatically:

```
cat role_name.txt
```

Option 2: navigate to the IAM roles page in the AWS console and search for a
role name starting with `Fugue-`.

These roles may now be used to grant Fugue read-only access to your AWS accounts.
