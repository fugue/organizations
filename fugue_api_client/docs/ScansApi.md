# swagger_client.ScansApi

All URIs are relative to *https://api.riskmanager.fugue.co/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scan**](ScansApi.md#create_scan) | **POST** /scans | Creates and triggers a new environment scan.
[**get_compliance_by_resource_types**](ScansApi.md#get_compliance_by_resource_types) | **GET** /scans/{scan_id}/compliance_by_resource_types | Lists compliance results by resource type for a scan.
[**get_compliance_by_rules**](ScansApi.md#get_compliance_by_rules) | **GET** /scans/{scan_id}/compliance_by_rules | Lists compliance results by rule for a scan.
[**get_scan**](ScansApi.md#get_scan) | **GET** /scans/{scan_id} | Retrieves details for a scan.
[**list_scans**](ScansApi.md#list_scans) | **GET** /scans | Lists scans for an environment.


# **create_scan**
> Scan create_scan(environment_id)

Creates and triggers a new environment scan.

Creates and triggers a new environment scan.

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
api_instance = swagger_client.ScansApi(swagger_client.ApiClient(configuration))
environment_id = 'environment_id_example' # str | ID of the environment to scan.

try:
    # Creates and triggers a new environment scan.
    api_response = api_instance.create_scan(environment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScansApi->create_scan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| ID of the environment to scan. | 

### Return type

[**Scan**](Scan.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compliance_by_resource_types**
> ComplianceByResourceTypeOutput get_compliance_by_resource_types(scan_id, offset=offset, max_items=max_items, resource_type=resource_type, family=family)

Lists compliance results by resource type for a scan.

Lists compliance results by resource type for a scan.

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
api_instance = swagger_client.ScansApi(swagger_client.ApiClient(configuration))
scan_id = 'scan_id_example' # str | Scan ID.
offset = 0 # int | Number of items to skip before returning. This parameter is used when the number of items spans multiple pages. (optional) (default to 0)
max_items = 100 # int | Maximum number of items to return. (optional) (default to 100)
resource_type = ['resource_type_example'] # list[str] | Resource types to filter by. When not specified, all resource types will be returned. (optional)
family = ['family_example'] # list[str] | Compliance family to filter by. When not specified, all compliance families will be returned. (optional)

try:
    # Lists compliance results by resource type for a scan.
    api_response = api_instance.get_compliance_by_resource_types(scan_id, offset=offset, max_items=max_items, resource_type=resource_type, family=family)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScansApi->get_compliance_by_resource_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **str**| Scan ID. | 
 **offset** | **int**| Number of items to skip before returning. This parameter is used when the number of items spans multiple pages. | [optional] [default to 0]
 **max_items** | **int**| Maximum number of items to return. | [optional] [default to 100]
 **resource_type** | [**list[str]**](str.md)| Resource types to filter by. When not specified, all resource types will be returned. | [optional] 
 **family** | [**list[str]**](str.md)| Compliance family to filter by. When not specified, all compliance families will be returned. | [optional] 

### Return type

[**ComplianceByResourceTypeOutput**](ComplianceByResourceTypeOutput.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compliance_by_rules**
> ComplianceByRules get_compliance_by_rules(scan_id, offset=offset, max_items=max_items, family=family, result=result)

Lists compliance results by rule for a scan.

Lists compliance results by rule for a scan.

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
api_instance = swagger_client.ScansApi(swagger_client.ApiClient(configuration))
scan_id = 'scan_id_example' # str | Scan ID.
offset = 0 # int | Number of items to skip before returning. This parameter is used when the number of items spans multiple pages. (optional) (default to 0)
max_items = 100 # int | Maximum number of items to return. (optional) (default to 100)
family = ['family_example'] # list[str] | Compliance family to filter by. When not specified, all compliance families will be returned. (optional)
result = ['result_example'] # list[str] | Rule result to filter by. When not specified, all results will be returned. (optional)

try:
    # Lists compliance results by rule for a scan.
    api_response = api_instance.get_compliance_by_rules(scan_id, offset=offset, max_items=max_items, family=family, result=result)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScansApi->get_compliance_by_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **str**| Scan ID. | 
 **offset** | **int**| Number of items to skip before returning. This parameter is used when the number of items spans multiple pages. | [optional] [default to 0]
 **max_items** | **int**| Maximum number of items to return. | [optional] [default to 100]
 **family** | [**list[str]**](str.md)| Compliance family to filter by. When not specified, all compliance families will be returned. | [optional] 
 **result** | [**list[str]**](str.md)| Rule result to filter by. When not specified, all results will be returned. | [optional] 

### Return type

[**ComplianceByRules**](ComplianceByRules.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scan**
> ScanWithSummary get_scan(scan_id)

Retrieves details for a scan.

Retrieves details for a scan.

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
api_instance = swagger_client.ScansApi(swagger_client.ApiClient(configuration))
scan_id = 'scan_id_example' # str | Scan ID.

try:
    # Retrieves details for a scan.
    api_response = api_instance.get_scan(scan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScansApi->get_scan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **str**| Scan ID. | 

### Return type

[**ScanWithSummary**](ScanWithSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scans**
> Scans list_scans(environment_id, offset=offset, max_items=max_items, order_by=order_by, order_direction=order_direction, status=status, range_from=range_from, range_to=range_to)

Lists scans for an environment.

Lists scans for an environment.

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
api_instance = swagger_client.ScansApi(swagger_client.ApiClient(configuration))
environment_id = 'environment_id_example' # str | ID of the environment to retrieve scans for.
offset = 0 # int | Number of items to skip before returning. This parameter is used when the number of items spans multiple pages. (optional) (default to 0)
max_items = 100 # int | Maximum number of items to return. (optional) (default to 100)
order_by = 'created_at' # str | Field to sort the items by. (optional) (default to created_at)
order_direction = 'desc' # str | Direction to sort the items in. (optional) (default to desc)
status = ['status_example'] # list[str] | Status to filter by. When not specified, all statuses will be returned. (optional)
range_from = 56 # int | Earliest created_at time to return scans from. (optional)
range_to = 56 # int | Latest created_at time to return scans from. (optional)

try:
    # Lists scans for an environment.
    api_response = api_instance.list_scans(environment_id, offset=offset, max_items=max_items, order_by=order_by, order_direction=order_direction, status=status, range_from=range_from, range_to=range_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScansApi->list_scans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| ID of the environment to retrieve scans for. | 
 **offset** | **int**| Number of items to skip before returning. This parameter is used when the number of items spans multiple pages. | [optional] [default to 0]
 **max_items** | **int**| Maximum number of items to return. | [optional] [default to 100]
 **order_by** | **str**| Field to sort the items by. | [optional] [default to created_at]
 **order_direction** | **str**| Direction to sort the items in. | [optional] [default to desc]
 **status** | [**list[str]**](str.md)| Status to filter by. When not specified, all statuses will be returned. | [optional] 
 **range_from** | **int**| Earliest created_at time to return scans from. | [optional] 
 **range_to** | **int**| Latest created_at time to return scans from. | [optional] 

### Return type

[**Scans**](Scans.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

