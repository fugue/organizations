# ComplianceByRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family** | **str** | Name of the compliance family. | [optional] 
**rule** | **str** | Name of the compliance rule. | [optional] 
**result** | **str** | Result of the rule. | [optional] 
**unsurveyed_resource_types** | **list[str]** | List of resource types that were not surveyed and caused the result to be unknown. | [optional] 
**failed_resource_types** | [**list[ComplianceByRuleFailedResourceTypes]**](ComplianceByRuleFailedResourceTypes.md) | List of resource types that failed to satisfy the rule due to a required resource being omitted and associated error messages. | [optional] 
**failed_resources** | [**list[ComplianceByRuleFailedResources]**](ComplianceByRuleFailedResources.md) | List of resources that failed to satisfy the rule due to a misconfiguration in the resource and associated error messages. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


