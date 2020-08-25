# swagger_client.CustomRulesApi

All URIs are relative to *https://api.riskmanager.fugue.co/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_rule**](CustomRulesApi.md#create_custom_rule) | **POST** /rules | Create a new custom rule.
[**delete_custom_rule**](CustomRulesApi.md#delete_custom_rule) | **DELETE** /rules/{rule_id} | Delete a custom rule.
[**get_custom_rule**](CustomRulesApi.md#get_custom_rule) | **GET** /rules/{rule_id} | Get details on a single custom rule.
[**list_custom_rules**](CustomRulesApi.md#list_custom_rules) | **GET** /rules | List custom rules.
[**test_custom_rule**](CustomRulesApi.md#test_custom_rule) | **POST** /rules/test | Test a custom rule.
[**test_custom_rule_input**](CustomRulesApi.md#test_custom_rule_input) | **GET** /rules/test/input | Get the input for a custom rule test.
[**update_custom_rule**](CustomRulesApi.md#update_custom_rule) | **PATCH** /rules/{rule_id} | Update custom rule.


# **create_custom_rule**
> CustomRuleWithErrors create_custom_rule(rule)

Create a new custom rule.

Create a new custom rule. 

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
api_instance = swagger_client.CustomRulesApi(swagger_client.ApiClient(configuration))
rule = swagger_client.CreateCustomRuleInput() # CreateCustomRuleInput | Configuration options for the new custom rule.

try:
    # Create a new custom rule.
    api_response = api_instance.create_custom_rule(rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomRulesApi->create_custom_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | [**CreateCustomRuleInput**](CreateCustomRuleInput.md)| Configuration options for the new custom rule. | 

### Return type

[**CustomRuleWithErrors**](CustomRuleWithErrors.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_rule**
> delete_custom_rule(rule_id)

Delete a custom rule.

Delete a specified custom rule. 

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
api_instance = swagger_client.CustomRulesApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | The id of the rule to delete.

try:
    # Delete a custom rule.
    api_instance.delete_custom_rule(rule_id)
except ApiException as e:
    print("Exception when calling CustomRulesApi->delete_custom_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| The id of the rule to delete. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_rule**
> CustomRule get_custom_rule(rule_id)

Get details on a single custom rule.

Get details on a single custom rule. 

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
api_instance = swagger_client.CustomRulesApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | The ID of the Rule to get.

try:
    # Get details on a single custom rule.
    api_response = api_instance.get_custom_rule(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomRulesApi->get_custom_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| The ID of the Rule to get. | 

### Return type

[**CustomRule**](CustomRule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_rules**
> CustomRules list_custom_rules(offset=offset, max_items=max_items)

List custom rules.

Return a list of custom rules. 

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
api_instance = swagger_client.CustomRulesApi(swagger_client.ApiClient(configuration))
offset = 0 # int | Number of items to skip before returning. This parameter is used when the number of items spans multiple pages. (optional) (default to 0)
max_items = 100 # int | Maximum number of items to return. (optional) (default to 100)

try:
    # List custom rules.
    api_response = api_instance.list_custom_rules(offset=offset, max_items=max_items)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomRulesApi->list_custom_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Number of items to skip before returning. This parameter is used when the number of items spans multiple pages. | [optional] [default to 0]
 **max_items** | **int**| Maximum number of items to return. | [optional] [default to 100]

### Return type

[**CustomRules**](CustomRules.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_custom_rule**
> TestCustomRuleOutput test_custom_rule(rule)

Test a custom rule.

Test a custom rule using state from an scan. 

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
api_instance = swagger_client.CustomRulesApi(swagger_client.ApiClient(configuration))
rule = swagger_client.TestCustomRuleInput() # TestCustomRuleInput | Information about custom rule to be tested.

try:
    # Test a custom rule.
    api_response = api_instance.test_custom_rule(rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomRulesApi->test_custom_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | [**TestCustomRuleInput**](TestCustomRuleInput.md)| Information about custom rule to be tested. | 

### Return type

[**TestCustomRuleOutput**](TestCustomRuleOutput.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_custom_rule_input**
> TestCustomRuleInputScan test_custom_rule_input(scan_id)

Get the input for a custom rule test.

Get the input against which a custom rule would be tested. 

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
api_instance = swagger_client.CustomRulesApi(swagger_client.ApiClient(configuration))
scan_id = 'scan_id_example' # str | Scan of which we should get the custom rule test input.

try:
    # Get the input for a custom rule test.
    api_response = api_instance.test_custom_rule_input(scan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomRulesApi->test_custom_rule_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **str**| Scan of which we should get the custom rule test input. | 

### Return type

[**TestCustomRuleInputScan**](TestCustomRuleInputScan.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_rule**
> CustomRuleWithErrors update_custom_rule(rule_id, rule)

Update custom rule.

Update configuration of a custom rule. 

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
api_instance = swagger_client.CustomRulesApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | The id of the rule to update.
rule = swagger_client.UpdateCustomRuleInput() # UpdateCustomRuleInput | New configuration options for the custom rule.

try:
    # Update custom rule.
    api_response = api_instance.update_custom_rule(rule_id, rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomRulesApi->update_custom_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| The id of the rule to update. | 
 **rule** | [**UpdateCustomRuleInput**](UpdateCustomRuleInput.md)| New configuration options for the custom rule. | 

### Return type

[**CustomRuleWithErrors**](CustomRuleWithErrors.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

