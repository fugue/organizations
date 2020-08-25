
VENV_NAME = .orgvenv
VENV = source $(VENV_NAME)/bin/activate
AWS = $(VENV) && aws
STACKSET_MARKER = .stackset

FUGUE_ACCOUNT_ID ?= 370134896156
STACKSET_NAME ?= Fugue
ROLE_NAME ?= $(shell cat role_name)
OU ?= "*"
COMPLIANCE_FAMILIES ?= "CIS FBP"

# Create a Python virtual environment to use for scripting in this Makefile
$(VENV_NAME):
	python -m venv $(VENV_NAME)
	source $(VENV_NAME)/bin/activate && pip install -q awscli

# Describe your AWS organization and save information to organization.json in
# this directory
organization.json: $(VENV_NAME)
	$(VENV) && python describe_organization.py

# Create a "random" role name to make the role name less guessable. The role
# access would already be secured via the role trust policy, but this is just
# added for good measure.
role_name:
	@$(VENV) && python -c "import time; print('Fugue-%d' % int(time.time()))" > $@

.PHONY: print_role_name
print_role_name: role_name
	@echo "Role name: $(ROLE_NAME)"

# Create the Fugue stackset which provisions secured roles in each AWS account
.PHONY: stackset
stackset: role_name
ifeq ($(EXTERNAL_ID),)
	$(error EXTERNAL_ID not set)
endif
	$(VENV) && python create_stackset.py \
		--name $(STACKSET_NAME) \
		--template cloudformation/account.yaml \
		--description "Provides read-only scan access to Fugue" \
		--ous $(OU) \
		--parameters \
			RoleName=$(ROLE_NAME) \
			FugueAccountId=$(FUGUE_ACCOUNT_ID) \
			FugueExternalId=$(EXTERNAL_ID)
	@echo "The Fugue Stackset is being created. This may take approximately 15 minutes."
	@echo "Please monitor the process in the AWS console."

# Helps track whether the stackset has been provisioned
$(STACKSET_MARKER): stackset
	@touch $@

# Create Fugue environments for AWS accounts in your AWS organization
.PHONY: environments
environments: $(VENV_NAME) organization.json role_name $(STACKSET_MARKER)
	$(VENV) && pip install -q ./fugue_api_client
	$(VENV) && python create_environments.py \
		--role-name $(ROLE_NAME) \
		--ous $(OU) \
		--compliance-families $(COMPLIANCE_FAMILIES)

# This file is committed in the repo so this target is only needed to refresh
# the swagger file to get any updates
swagger.yaml:
	wget -q https://api.riskmanager.fugue.co/v0/swagger -O swagger.yaml

# Similarly, the fugue_api_client directory is committed in the repository but
# this rule can be used to regenerate it as needed
fugue_api_client: swagger.yaml
	swagger-codegen generate -i ./swagger.yaml -l python -o fugue_api_client

# Shortcut for the AWS command to list all stacksets in your account
.PHONY: list_stacksets
list_stacksets:
	$(AWS) cloudformation list-stack-sets

.PHONY: clean
clean:
	rm -f role_name organization.json $(STACKSET_MARKER)
