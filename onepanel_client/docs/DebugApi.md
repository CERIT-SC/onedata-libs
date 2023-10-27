# onepanel_client.DebugApi

All URIs are relative to */api/v3/onepanel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transfers_mock**](DebugApi.md#get_transfers_mock) | **GET** /provider/debug/transfers_mock | Get transfers mock status
[**modify_transfers_mock**](DebugApi.md#modify_transfers_mock) | **PATCH** /provider/debug/transfers_mock | Modify transfers mock

# **get_transfers_mock**
> TransfersMock get_transfers_mock()

Get transfers mock status

Returns information whether transfers mocking is enabled. 

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.DebugApi(onepanel_client.ApiClient(configuration))

try:
    # Get transfers mock status
    api_response = api_instance.get_transfers_mock()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->get_transfers_mock: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TransfersMock**](TransfersMock.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_transfers_mock**
> modify_transfers_mock(body)

Modify transfers mock

Toggle transfers mock. When enabled, all transfers finish successfully without actually transferring data. WARNING: this is a debugging feature disrupting normal Oneprovider operation. 

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.DebugApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.TransfersMock() # TransfersMock | New value for the mock setting.

try:
    # Modify transfers mock
    api_instance.modify_transfers_mock(body)
except ApiException as e:
    print("Exception when calling DebugApi->modify_transfers_mock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransfersMock**](TransfersMock.md)| New value for the mock setting. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

