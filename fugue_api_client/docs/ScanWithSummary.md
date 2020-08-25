# ScanWithSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the scan. | [optional] 
**environment_id** | **str** | ID of the environment the scan belongs to. | [optional] 
**created_at** | **int** | Time the scan was created. | [optional] 
**updated_at** | **int** | Time the scan was last updated. | [optional] 
**finished_at** | **int** | Time the scan was finished. | [optional] 
**status** | **str** | Status of the scan. | [optional] 
**message** | **str** | Message related to the scan. | [optional] 
**remediation_error** | **bool** | Indicates whether there were any remediation errors on the scan. | [optional] 
**resource_summary** | [**ResourceSummary**](ResourceSummary.md) |  | [optional] 
**resource_type_errors** | [**list[ScanWithSummaryResourceTypeErrors]**](ScanWithSummaryResourceTypeErrors.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


