# CreateEnvironmentInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the environment. | [optional] 
**provider** | **str** | Name of the cloud service provider for the environment. | [optional] 
**provider_options** | [**ProviderOptions**](ProviderOptions.md) | A dictionary of options for the provider. | [optional] 
**compliance_families** | **list[str]** | List of compliance families validated against the environment. | [optional] 
**survey_resource_types** | **list[str]** | List of resource types to be surveyed. | [optional] 
**remediate_resource_types** | **list[str]** | List of resource types to be remediated if remediation is enabled. | [optional] 
**scan_schedule_enabled** | **bool** | Indicates if the new environment should have scans run on a schedule upon creation. | [optional] 
**scan_interval** | **int** | Time in seconds between the end of one scan to the start of the next. Must also set scan_schedule_enabled to true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


