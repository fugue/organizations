# Organizations

This repository contains utilities used to create IAM roles that provide Fugue
secure access to multiple AWS accounts within an AWS organization.

After setting up the dependencies, as listed below, there are four steps to
follow to set up Fugue with all your AWS accounts. This approach leverages
AWS [Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html)
and CloudFormation [Stacksets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html)
to provision an IAM role in each account.

## Dependenices

These scripts were developed and tested primarily on MacOS. They should work
with no changes on Linux as well. In Windows running in WSL in probably your
best bet.

Using these scripts requires the following:

 * Python 3.6+
 * AWS credentials for your AWS root account
 * GNU Make

By running Make commands as described below, the required Python dependencies
will automatically be installed for you.

## Step 1: Create a Fugue Account

[Register to create a Fugue account](https://riskmanager.fugue.co/register)
if you don't already have one. The secure cross-account access we set up in
subsequent steps will be restricted to this account, with its associated
[External ID](https://aws.amazon.com/blogs/security/how-to-use-external-id-when-granting-access-to-your-aws-resources/).

Once your account is created you can move on to the next step.

## Step 2: Gather information about your AWS organization

**Prerequisite**: You must have AWS credentials **for your root account** active, with
the `AWSOrganizationsReadOnlyAccess` policy attached to your user or role, or
equivalent permissions via another policy.

Run the following to gather account and organizational unit (OU) information
from your AWS organization and write it to a JSON-formatted output file:

```bash
$ make organization.json
```

## Step 3: Create a Cloudformation Stackset to provision IAM roles

We will need the **External ID** associated with your Fugue account for this step.
Reach out to `support@fugue.co` or your solutions architect to get this value.
Alternatively, follow the [steps in the Fugue Docs](https://docs.fugue.co/setup.html#step-2b-create-iam-role)
to create one IAM role from our parameterized template and then retrieve the
value from that.

With the External ID in hand, we can now create the Stackset.

You will still need AWS credentials for your root account active, with the
`AWSCloudFormationFullAccess` and `AWSOrganizationsReadOnlyAccess` or equivalent
policies attached.

```bash
$ make stackset EXTERNAL_ID=<extid>
```

Replace `<extid>` with the actual external ID from Fugue. You may optionally
also specify `OU=<ou_id>` to deploy roles within one OU only, rather than all.

See [account.yaml](cloudformation/account.yaml) for the CloudFormation template
used to create the role in each account.

It may take about 15 minutes for the Stackset to create the corresponding
Stacks and Roles in each AWS account. Monitor this progress via the AWS console.
Once the Stackset has is ready, move go to the next step.

## Step 4: Creating Fugue Environments for each AWS account

You must have [Fugue API credentials](https://docs.fugue.co/api.html#getting-started-create-client-id-and-secret)
set in your environment which correspond to an active API client in Fugue:

* `FUGUE_API_ID` - your Fugue API client ID
* `FUGUE_API_SECRET` - your Fugue API client secret

Run the following to create Fugue environments for AWS accounts
where the Fugue IAM role has already been provisioned.

```bash
$ make environments
```

By default this will use `CIS` and `FBP` for compliance families and create
environments for every AWS account in your organization.

To override those defaults, you may run the following instead:

```bash
$ make environments OU=<ou_id> COMPLIANCE_FAMILIES="SOC2"
```

Now visit the Fugue webpage to see the environments that were created.
