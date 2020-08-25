# swagger_client.EventsApi

All URIs are relative to *https://api.riskmanager.fugue.co/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_events**](EventsApi.md#list_events) | **GET** /events | Lists drift, remediation, and compliance events for an environment.


# **list_events**
> Events list_events(environment_id, offset=offset, max_items=max_items, range_from=range_from, range_to=range_to, event_type=event_type, change=change, remediated=remediated, resource_type=resource_type)

Lists drift, remediation, and compliance events for an environment.

Lists drift, remediation, and compliance events for an environment.

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
api_instance = swagger_client.EventsApi(swagger_client.ApiClient(configuration))
environment_id = 'environment_id_example' # str | Environment ID.
offset = 0 # int | Number of items to skip before returning. This parameter is used when the number of items spans multiple pages. (optional) (default to 0)
max_items = 100 # int | Maximum number of items to return. (optional) (default to 100)
range_from = 56 # int | Earliest created_at time to return events from. (optional)
range_to = 56 # int | Latest created_at time to return events from. (optional)
event_type = ['event_type_example'] # list[str] | Event type to filter by. When not specified, all event types will be returned. (optional)
change = ['change_example'] # list[str] | Type of change made in the event to filter by. When not specified, all change types will be returned. (optional)
remediated = ['remediated_example'] # list[str] | Filter remediation results for an event by success or failure. When not specified, all remediation results will be returned. (optional)
resource_type = ['resource_type_example'] # list[str] | Resource types in the event to filter by. When not specified, all resource types will be returned. (optional)

try:
    # Lists drift, remediation, and compliance events for an environment.
    api_response = api_instance.list_events(environment_id, offset=offset, max_items=max_items, range_from=range_from, range_to=range_to, event_type=event_type, change=change, remediated=remediated, resource_type=resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->list_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID. | 
 **offset** | **int**| Number of items to skip before returning. This parameter is used when the number of items spans multiple pages. | [optional] [default to 0]
 **max_items** | **int**| Maximum number of items to return. | [optional] [default to 100]
 **range_from** | **int**| Earliest created_at time to return events from. | [optional] 
 **range_to** | **int**| Latest created_at time to return events from. | [optional] 
 **event_type** | [**list[str]**](str.md)| Event type to filter by. When not specified, all event types will be returned. | [optional] 
 **change** | [**list[str]**](str.md)| Type of change made in the event to filter by. When not specified, all change types will be returned. | [optional] 
 **remediated** | [**list[str]**](str.md)| Filter remediation results for an event by success or failure. When not specified, all remediation results will be returned. | [optional] 
 **resource_type** | [**list[str]**](str.md)| Resource types in the event to filter by. When not specified, all resource types will be returned. | [optional] 

### Return type

[**Events**](Events.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

