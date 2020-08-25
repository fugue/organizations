# swagger_client.NotificationsApi

All URIs are relative to *https://api.riskmanager.fugue.co/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification**](NotificationsApi.md#create_notification) | **POST** /notifications | Creates a new notification.
[**delete_notification**](NotificationsApi.md#delete_notification) | **DELETE** /notifications/{notification_id} | Deletes a notification.
[**list_notifications**](NotificationsApi.md#list_notifications) | **GET** /notifications | Lists details for all notifications.
[**update_notification**](NotificationsApi.md#update_notification) | **PUT** /notifications/{notification_id} | Updates an existing notification.


# **create_notification**
> Notification create_notification(notification)

Creates a new notification.

Creates a new notification.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.NotificationsApi(swagger_client.ApiClient(configuration))
notification = swagger_client.CreateNotificationInput() # CreateNotificationInput | Configuration options for the new notification.

try:
    # Creates a new notification.
    api_response = api_instance.create_notification(notification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->create_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification** | [**CreateNotificationInput**](CreateNotificationInput.md)| Configuration options for the new notification. | 

### Return type

[**Notification**](Notification.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification**
> delete_notification(notification_id)

Deletes a notification.

Deletes a notification.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.NotificationsApi(swagger_client.ApiClient(configuration))
notification_id = 'notification_id_example' # str | Notification ID.

try:
    # Deletes a notification.
    api_instance.delete_notification(notification_id)
except ApiException as e:
    print("Exception when calling NotificationsApi->delete_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| Notification ID. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notifications**
> Notifications list_notifications(offset=offset, max_items=max_items)

Lists details for all notifications.

Lists details for all notifications.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.NotificationsApi(swagger_client.ApiClient(configuration))
offset = 0 # int | Number of items to skip before returning. This parameter is used when the number of items spans multiple pages. (optional) (default to 0)
max_items = 100 # int | Maximum number of items to return. (optional) (default to 100)

try:
    # Lists details for all notifications.
    api_response = api_instance.list_notifications(offset=offset, max_items=max_items)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->list_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Number of items to skip before returning. This parameter is used when the number of items spans multiple pages. | [optional] [default to 0]
 **max_items** | **int**| Maximum number of items to return. | [optional] [default to 100]

### Return type

[**Notifications**](Notifications.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification**
> Notification update_notification(notification_id, notification)

Updates an existing notification.

Updates an existing notification.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.NotificationsApi(swagger_client.ApiClient(configuration))
notification_id = 'notification_id_example' # str | Notification ID.
notification = swagger_client.UpdateNotificationInput() # UpdateNotificationInput | New configuration options for the notification.

try:
    # Updates an existing notification.
    api_response = api_instance.update_notification(notification_id, notification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->update_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| Notification ID. | 
 **notification** | [**UpdateNotificationInput**](UpdateNotificationInput.md)| New configuration options for the notification. | 

### Return type

[**Notification**](Notification.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

