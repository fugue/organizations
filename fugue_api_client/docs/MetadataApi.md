# swagger_client.MetadataApi

All URIs are relative to *https://api.riskmanager.fugue.co/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy**](MetadataApi.md#create_policy) | **POST** /metadata/{provider}/permissions | Returns the permissions required to survey and remediate resources.
[**get_resource_types**](MetadataApi.md#get_resource_types) | **GET** /metadata/{provider}/resource_types | Lists the resource types supported by Fugue.
[**get_swagger**](MetadataApi.md#get_swagger) | **GET** /swagger | Returns the OpenAPI 2.0 specification for this API.
[**get_swagger_ui**](MetadataApi.md#get_swagger_ui) | **GET** /swagger/ui | Returns a friendly user interface for the OpenAPI 2.0 specification for this API.


# **create_policy**
> Permissions create_policy(provider, input)

Returns the permissions required to survey and remediate resources.

Returns the permissions required to survey and remediate resources.

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
api_instance = swagger_client.MetadataApi(swagger_client.ApiClient(configuration))
provider = 'provider_example' # str | Name of the cloud provider.
input = swagger_client.CreatePolicyInput() # CreatePolicyInput | List of resource types to be able to survey and remediate.

try:
    # Returns the permissions required to survey and remediate resources.
    api_response = api_instance.create_policy(provider, input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->create_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| Name of the cloud provider. | 
 **input** | [**CreatePolicyInput**](CreatePolicyInput.md)| List of resource types to be able to survey and remediate. | 

### Return type

[**Permissions**](Permissions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_types**
> ResourceTypeMetadata get_resource_types(provider, region=region, beta_resources=beta_resources)

Lists the resource types supported by Fugue.

Lists the resource types supported by Fugue.

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
api_instance = swagger_client.MetadataApi(swagger_client.ApiClient(configuration))
provider = 'provider_example' # str | Name of the cloud provider.
region = 'region_example' # str | The AWS region for which to return resource types.  Required if provider is aws or aws_govcloud. (optional)
beta_resources = true # bool | Indicates whether resource types in beta will be returned. (optional)

try:
    # Lists the resource types supported by Fugue.
    api_response = api_instance.get_resource_types(provider, region=region, beta_resources=beta_resources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_resource_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| Name of the cloud provider. | 
 **region** | **str**| The AWS region for which to return resource types.  Required if provider is aws or aws_govcloud. | [optional] 
 **beta_resources** | **bool**| Indicates whether resource types in beta will be returned. | [optional] 

### Return type

[**ResourceTypeMetadata**](ResourceTypeMetadata.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_swagger**
> object get_swagger()

Returns the OpenAPI 2.0 specification for this API.

Returns the OpenAPI 2.0 specification for this API.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()

try:
    # Returns the OpenAPI 2.0 specification for this API.
    api_response = api_instance.get_swagger()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_swagger: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_swagger_ui**
> get_swagger_ui()

Returns a friendly user interface for the OpenAPI 2.0 specification for this API.

Returns a friendly user interface for the OpenAPI 2.0 specification for this API.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()

try:
    # Returns a friendly user interface for the OpenAPI 2.0 specification for this API.
    api_instance.get_swagger_ui()
except ApiException as e:
    print("Exception when calling MetadataApi->get_swagger_ui: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

