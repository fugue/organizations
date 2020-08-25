# Environment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the environment. | [optional] 
**tenant_id** | **str** | ID of the tenant that owns the environment. | [optional] 
**name** | **str** | Name of the environment. | [optional] 
**provider** | **str** | Name of the cloud service provider for the environment. | [optional] 
**provider_options** | [**ProviderOptions**](ProviderOptions.md) |  | [optional] 
**compliance_families** | **list[str]** | List of compliance families validated against the environment. | [optional] 
**baseline_id** | **str** | Scan ID of the baseline if baseline is enabled. | [optional] 
**drift** | **bool** | Indicates whether drift detection is enabled for the environment. | [optional] 
**remediation** | **bool** | Indicates whether remediation is enabled for the environment. | [optional] 
**scan_status** | **str** | Status of the current or most recently completed scan for the environment. | [optional] 
**scan_interval** | **int** | Time in seconds between the end of one scan to the start of the next. | [optional] 
**last_scan_at** | **int** | Time the current or most recently completed scan for the environment started. | [optional] 
**next_scan_at** | **int** | Time the next scan will start. | [optional] 
**survey_resource_types** | **list[str]** | List of resource types surveyed for the environment. | [optional] 
**remediate_resource_types** | **list[str]** | List of resource types remediated for the environment if remediation is enabled. | [optional] 
**scan_schedule_enabled** | **bool** | Indicates whether the environment should have scans run on a schedule. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


