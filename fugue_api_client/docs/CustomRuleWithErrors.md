# CustomRuleWithErrors

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the custom rule. | [optional] 
**name** | **str** | Human readable name of the custom rule. | [optional] 
**source** | **str** | The origin of this rule. | [optional] 
**description** | **str** | Description of the custom rule. | [optional] 
**provider** | **str** | Provider of the custom rule. | [optional] 
**resource_type** | **str** | Resource type to which the custom rule applies. | [optional] 
**compliance_controls** | **list[str]** | Compliance controls to which the custom rule belongs. | [optional] 
**status** | **str** | The current status of the rule. | [optional] 
**rule_text** | **str** | The rego source code for the rule. | [optional] 
**created_by** | **str** | Principal that created the rule. | [optional] 
**created_by_display_name** | **str** | Display name of the user that created the rule | [optional] 
**created_at** | **int** | The date and time the rule was created. | [optional] 
**updated_by** | **str** | Principal that last updated the rule. | [optional] 
**updated_by_display_name** | **str** | Display name of the user that last updated the rule | [optional] 
**updated_at** | **int** | The date and time the rule was last updated. | [optional] 
**errors** | [**list[CustomRuleError]**](CustomRuleError.md) | Syntax errors in the rego source code. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


