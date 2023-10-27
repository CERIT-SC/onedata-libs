# onepanel_client.SecurityApi

All URIs are relative to */api/v3/onepanel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_emergency_passphrase_status**](SecurityApi.md#get_emergency_passphrase_status) | **GET** /emergency_passphrase | Get emergency passphrase status
[**get_web_cert**](SecurityApi.md#get_web_cert) | **GET** /web_cert | Get information about SSL certificates configuration and status
[**modify_web_cert**](SecurityApi.md#modify_web_cert) | **PATCH** /web_cert | Modify SSL certificate configuration
[**set_emergency_passphrase**](SecurityApi.md#set_emergency_passphrase) | **PUT** /emergency_passphrase | Set emergency passphrase

# **get_emergency_passphrase_status**
> EmergencyPassphraseStatus get_emergency_passphrase_status()

Get emergency passphrase status

Returns information whether emergency passphrase is set.

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
api_instance = onepanel_client.SecurityApi(onepanel_client.ApiClient(configuration))

try:
    # Get emergency passphrase status
    api_response = api_instance.get_emergency_passphrase_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_emergency_passphrase_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EmergencyPassphraseStatus**](EmergencyPassphraseStatus.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_cert**
> WebCert get_web_cert()

Get information about SSL certificates configuration and status

Returns information about SSL certificate status and renewal configuration. 

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
api_instance = onepanel_client.SecurityApi(onepanel_client.ApiClient(configuration))

try:
    # Get information about SSL certificates configuration and status
    api_response = api_instance.get_web_cert()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_web_cert: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WebCert**](WebCert.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_web_cert**
> modify_web_cert(body)

Modify SSL certificate configuration

Modifies configuration regarding certificate management. Allows enabling or disabling certificate autorenewal using Let's Encrypt service. 

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
api_instance = onepanel_client.SecurityApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.WebCertModifyRequest() # WebCertModifyRequest | New values for certificate management configuration.


try:
    # Modify SSL certificate configuration
    api_instance.modify_web_cert(body)
except ApiException as e:
    print("Exception when calling SecurityApi->modify_web_cert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebCertModifyRequest**](WebCertModifyRequest.md)| New values for certificate management configuration.
 | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_emergency_passphrase**
> set_emergency_passphrase(body)

Set emergency passphrase

Sets passphrase which can be used to access the Onepanel REST API and emergency Onepanel GUI. May be invoked without credentials when no passphrase is set. 

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
api_instance = onepanel_client.SecurityApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.EmergencyPassphraseChangeRequest() # EmergencyPassphraseChangeRequest | 

try:
    # Set emergency passphrase
    api_instance.set_emergency_passphrase(body)
except ApiException as e:
    print("Exception when calling SecurityApi->set_emergency_passphrase: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmergencyPassphraseChangeRequest**](EmergencyPassphraseChangeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

