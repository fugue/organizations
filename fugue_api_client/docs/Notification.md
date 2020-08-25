# Notification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_id** | **str** | ID of the notification. | [optional] 
**name** | **str** | Human readable name of the notification. | [optional] 
**events** | **list[str]** | List of events the notification is triggered on. | [optional] 
**environments** | **list[dict(str, str)]** | List of maps from environment id to name the notification is attached to. | [optional] 
**emails** | **list[str]** | List of email address the notification is delivered to. | [optional] 
**topic_arn** | **str** | AWS SNS topic arn the notification is delivered to. | [optional] 
**last_error** | **str** | Last error recorded while processing notification. If the last notification processed had no error this field will be empty. | [optional] 
**created_by** | **str** | Principal the created the notification. | [optional] 
**created_at** | **int** | The date and time the notification was created. | [optional] 
**updated_by** | **str** | Principal that last updated the notification. | [optional] 
**updated_at** | **int** | AWS The date and time the notification was last updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


