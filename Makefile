
VENV_NAME = .orgvenv
VENV = source $(VENV_NAME)/bin/activate
AWS = $(VENV) && aws
STACKSET_MARKER = .stackset

TRUSTED_ACCOUNT_ID ?= 370134896156 # Fugue
TRUSTED_PRINCIPAL ?= role/generate-credentials # Fugue's Role
STACKSET_NAME ?= Fugue
ROLE_NAME ?= $(shell cat role_name)
OU ?= "*"
EVENT_BUS_ARN ?= arn:aws:events:us-east-1:$(TRUSTED_ACCOUNT_ID):event-bus/fugue-events

# Create the Fugue stackset which provisions secured roles in each AWS account
.PHONY: stackset
stackset: role_name.txt organization.json
ifeq ($(EXTERNAL_ID),)
	$(error EXTERNAL_ID is not set. Specify the value with "EXTERNAL_ID=VALUE" on the make command)
endif
	python create_stackset.py \
		--name $(STACKSET_NAME) \
		--template template.yaml \
		--description "Provides read-only scan access to Fugue" \
		--ous $(OU) \
		--parameters \
			RoleName=$(ROLE_NAME) \
			TrustedPrincipal=$(TRUSTED_PRINCIPAL) \
			TrustedAccountID=$(TRUSTED_ACCOUNT_ID) \
			ExternalID=$(EXTERNAL_ID) \
			EventBusArn=$(EVENT_BUS_ARN)
	@echo "The stackset is being created. This may take approximately 15 minutes."
	@echo "Please monitor the process in the AWS console."

# Helps track whether the stackset has been provisioned
$(STACKSET_MARKER): stackset
	@touch $@

# Describe your AWS organization and save information to organization.json in
# this directory
organization.json: $(VENV_NAME)
	$(VENV) && python describe_organization.py

# Create a Python virtual environment to use for scripting in this Makefile
$(VENV_NAME):
	python -m venv $(VENV_NAME)
	source $(VENV_NAME)/bin/activate && pip install -q awscli

# Create a "random" role name to make the role name less guessable. The role
# access would already be secured via the role trust policy, but this is just
# added for good measure.
role_name.txt: $(VENV_NAME)
	@$(VENV) && python -c "import time; print('Fugue-%d' % int(time.time()))" > $@

.PHONY: print_role_name
print_role_name: role_name
	@echo "Role name: $(ROLE_NAME)"

# Shortcut for the AWS command to list all stacksets in your account
.PHONY: list_stacksets
list_stacksets:
	$(AWS) cloudformation list-stack-sets

.PHONY: clean
clean:
	rm -f role_name organization.json $(STACKSET_MARKER)
