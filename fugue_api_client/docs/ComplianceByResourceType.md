# ComplianceByResourceType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** | Name of the resource type. | [optional] 
**total** | **int** | Count of all resources evaluated for this resource type. | [optional] 
**compliant** | **int** | Count of resources found to be fully compliant with all rules it has been evaulated against. | [optional] 
**noncompliant** | [**list[NonCompliantResource]**](NonCompliantResource.md) | List of non-compliant resources and the rules they have violated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


