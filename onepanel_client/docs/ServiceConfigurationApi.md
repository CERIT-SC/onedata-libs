# onepanel_client.ServiceConfigurationApi

All URIs are relative to */api/v3/onepanel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_gui_message**](ServiceConfigurationApi.md#get_gui_message) | **GET** /zone/gui_messages/{id} | Get settings of a Onezone GUI message
[**get_zone_policies**](ServiceConfigurationApi.md#get_zone_policies) | **GET** /zone/policies | Get Onezone policies
[**modify_gui_message**](ServiceConfigurationApi.md#modify_gui_message) | **PATCH** /zone/gui_messages/{id} | Modify settings of a Onezone GUI message
[**modify_zone_policies**](ServiceConfigurationApi.md#modify_zone_policies) | **PATCH** /zone/policies | Modify current Onezone policies

# **get_gui_message**
> GuiMessage get_gui_message(id)

Get settings of a Onezone GUI message

Returns settings of a message displayed in Onezone GUI.

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
api_instance = onepanel_client.ServiceConfigurationApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | Possible values are:   - cookie_consent_notification - for the contents of cookie consent popup   - privacy_policy - for the contents of the privacy policy document   - terms_of_use - for the contents of the Terms of Use document   - signin_notification - for the message displayed on the Onezone sign in screen 

try:
    # Get settings of a Onezone GUI message
    api_response = api_instance.get_gui_message(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceConfigurationApi->get_gui_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Possible values are:   - cookie_consent_notification - for the contents of cookie consent popup   - privacy_policy - for the contents of the privacy policy document   - terms_of_use - for the contents of the Terms of Use document   - signin_notification - for the message displayed on the Onezone sign in screen  | 

### Return type

[**GuiMessage**](GuiMessage.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_policies**
> ZonePolicies get_zone_policies()

Get Onezone policies

Returns restrictions placed on Onezone operations such as registering Oneproviders. 

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
api_instance = onepanel_client.ServiceConfigurationApi(onepanel_client.ApiClient(configuration))

try:
    # Get Onezone policies
    api_response = api_instance.get_zone_policies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceConfigurationApi->get_zone_policies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ZonePolicies**](ZonePolicies.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_gui_message**
> modify_gui_message(body, id)

Modify settings of a Onezone GUI message

Enables, disables or modifies a message displayed in Onezone GUI.

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
api_instance = onepanel_client.ServiceConfigurationApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.GuiMessage() # GuiMessage | 
id = 'id_example' # str | Possible values are:   - cookie_consent_notification - for the contents of cookie consent popup   - privacy_policy - for the contents of the privacy policy document   - terms_of_use - for the contents of the Terms of Use document   - signin_notification - for the message displayed on the Onezone sign in screen 

try:
    # Modify settings of a Onezone GUI message
    api_instance.modify_gui_message(body, id)
except ApiException as e:
    print("Exception when calling ServiceConfigurationApi->modify_gui_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GuiMessage**](GuiMessage.md)|  | 
 **id** | **str**| Possible values are:   - cookie_consent_notification - for the contents of cookie consent popup   - privacy_policy - for the contents of the privacy policy document   - terms_of_use - for the contents of the Terms of Use document   - signin_notification - for the message displayed on the Onezone sign in screen  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_zone_policies**
> modify_zone_policies(body)

Modify current Onezone policies

Modifies restrictions placed on Onezone operations such as registering providers. 

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
api_instance = onepanel_client.ServiceConfigurationApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.ZonePolicies() # ZonePolicies | New values for Onezone policies.

try:
    # Modify current Onezone policies
    api_instance.modify_zone_policies(body)
except ApiException as e:
    print("Exception when calling ServiceConfigurationApi->modify_zone_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ZonePolicies**](ZonePolicies.md)| New values for Onezone policies. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

