# swagger_client.EnvironmentsApi

All URIs are relative to *https://api.riskmanager.fugue.co/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_environment**](EnvironmentsApi.md#create_environment) | **POST** /environments | Creates a new environment.
[**delete_environment**](EnvironmentsApi.md#delete_environment) | **DELETE** /environments/{environment_id} | Deletes an environment.
[**get_environment**](EnvironmentsApi.md#get_environment) | **GET** /environments/{environment_id} | Retrieves details and resource summary for an environment.
[**list_environments**](EnvironmentsApi.md#list_environments) | **GET** /environments | Lists details for all environments.
[**update_environment**](EnvironmentsApi.md#update_environment) | **PATCH** /environments/{environment_id} | Updates an environment.


# **create_environment**
> Environment create_environment(environment)

Creates a new environment.

Creates a new environment.

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
api_instance = swagger_client.EnvironmentsApi(swagger_client.ApiClient(configuration))
environment = swagger_client.CreateEnvironmentInput() # CreateEnvironmentInput | Configuration options for the new environment.

try:
    # Creates a new environment.
    api_response = api_instance.create_environment(environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->create_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | [**CreateEnvironmentInput**](CreateEnvironmentInput.md)| Configuration options for the new environment. | 

### Return type

[**Environment**](Environment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_environment**
> delete_environment(environment_id)

Deletes an environment.

Deletes an environment.

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
api_instance = swagger_client.EnvironmentsApi(swagger_client.ApiClient(configuration))
environment_id = 'environment_id_example' # str | Environment ID.

try:
    # Deletes an environment.
    api_instance.delete_environment(environment_id)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->delete_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment**
> EnvironmentWithSummary get_environment(environment_id)

Retrieves details and resource summary for an environment.

Retrieves details and resource summary for an environment.

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
api_instance = swagger_client.EnvironmentsApi(swagger_client.ApiClient(configuration))
environment_id = 'environment_id_example' # str | Environment ID.

try:
    # Retrieves details and resource summary for an environment.
    api_response = api_instance.get_environment(environment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->get_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID. | 

### Return type

[**EnvironmentWithSummary**](EnvironmentWithSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_environments**
> Environments list_environments(offset=offset, max_items=max_items, order_by=order_by, order_direction=order_direction)

Lists details for all environments.

Lists details for all environments.

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
api_instance = swagger_client.EnvironmentsApi(swagger_client.ApiClient(configuration))
offset = 0 # int | Number of items to skip before returning. This parameter is used when the number of items spans multiple pages. (optional) (default to 0)
max_items = 100 # int | Maximum number of items to return. (optional) (default to 100)
order_by = 'created_at' # str | Field to sort the items by. (optional) (default to created_at)
order_direction = 'desc' # str | Direction to sort the items in. (optional) (default to desc)

try:
    # Lists details for all environments.
    api_response = api_instance.list_environments(offset=offset, max_items=max_items, order_by=order_by, order_direction=order_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->list_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Number of items to skip before returning. This parameter is used when the number of items spans multiple pages. | [optional] [default to 0]
 **max_items** | **int**| Maximum number of items to return. | [optional] [default to 100]
 **order_by** | **str**| Field to sort the items by. | [optional] [default to created_at]
 **order_direction** | **str**| Direction to sort the items in. | [optional] [default to desc]

### Return type

[**Environments**](Environments.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_environment**
> Environment update_environment(environment_id, environment=environment)

Updates an environment.

Updates an environment.

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
api_instance = swagger_client.EnvironmentsApi(swagger_client.ApiClient(configuration))
environment_id = 'environment_id_example' # str | Environment ID.
environment = swagger_client.UpdateEnvironmentInput() # UpdateEnvironmentInput | Environment details to update. (optional)

try:
    # Updates an environment.
    api_response = api_instance.update_environment(environment_id, environment=environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->update_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID. | 
 **environment** | [**UpdateEnvironmentInput**](UpdateEnvironmentInput.md)| Environment details to update. | [optional] 

### Return type

[**Environment**](Environment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

