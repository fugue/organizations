# swagger_client.CORSApi

All URIs are relative to *https://api.riskmanager.fugue.co/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rules_options**](CORSApi.md#rules_options) | **OPTIONS** /rules | CORS support.
[**rules_rule_id_options**](CORSApi.md#rules_rule_id_options) | **OPTIONS** /rules/{rule_id} | CORS support.
[**rules_test_input_options**](CORSApi.md#rules_test_input_options) | **OPTIONS** /rules/test/input | CORS support.
[**rules_test_options**](CORSApi.md#rules_test_options) | **OPTIONS** /rules/test | CORS support.


# **rules_options**
> rules_options()

CORS support.

Enable CORS by returning correct headers. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CORSApi()

try:
    # CORS support.
    api_instance.rules_options()
except ApiException as e:
    print("Exception when calling CORSApi->rules_options: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_rule_id_options**
> rules_rule_id_options(rule_id)

CORS support.

Enable CORS by returning correct headers. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CORSApi()
rule_id = 'rule_id_example' # str | ID of the rule

try:
    # CORS support.
    api_instance.rules_rule_id_options(rule_id)
except ApiException as e:
    print("Exception when calling CORSApi->rules_rule_id_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| ID of the rule | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_test_input_options**
> rules_test_input_options()

CORS support.

Enable CORS by returning correct headers. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CORSApi()

try:
    # CORS support.
    api_instance.rules_test_input_options()
except ApiException as e:
    print("Exception when calling CORSApi->rules_test_input_options: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_test_options**
> rules_test_options()

CORS support.

Enable CORS by returning correct headers. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CORSApi()

try:
    # CORS support.
    api_instance.rules_test_options()
except ApiException as e:
    print("Exception when calling CORSApi->rules_test_options: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

