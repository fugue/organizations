# UpdateEnvironmentInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the environment. | [optional] 
**provider** | **str** | Name of the cloud service provider for the environment. | [optional] 
**provider_options** | [**ProviderOptionsUpdateInput**](ProviderOptionsUpdateInput.md) |  | [optional] 
**compliance_families** | **list[str]** | List of compliance families validated against the environment. | [optional] 
**baseline_id** | **str** | Scan ID of the baseline if baseline is enabled. | [optional] 
**remediation** | **bool** | Indicates whether remediation is enabled for the environment. | [optional] 
**survey_resource_types** | **list[str]** | List of resource types surveyed for the environment. | [optional] 
**remediate_resource_types** | **list[str]** | List of resource types remediated for the environment if remediation is enabled. | [optional] 
**scan_schedule_enabled** | **bool** | Indicates whether an environment is scanned on a schedule. | [optional] 
**scan_interval** | **int** | Time in seconds between the end of one scan to the start of the next. Must also set scan_schedule_enabled to true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


