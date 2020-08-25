# Event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of event | [optional] 
**event_type** | **str** | Type of event - drift, remediation, or compliance. | [optional] 
**created_at** | **int** | Time the event occurred. | [optional] 
**error** | **str** | Error message. | [optional] 
**resource_diff** | [**ResourceDiff**](ResourceDiff.md) | Difference between the old and new state of the resource. | [optional] 
**compliance_diff** | [**ComplianceDiff**](ComplianceDiff.md) | Difference between the old and new compliance state of the resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


