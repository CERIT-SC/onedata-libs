# oneprovider_client.OneproviderApi

All URIs are relative to */api/v3/oneprovider*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_configuration**](OneproviderApi.md#get_configuration) | **GET** /configuration | Get public information
[**health**](OneproviderApi.md#health) | **GET** /health | Check cluster health
[**test_image**](OneproviderApi.md#test_image) | **GET** /test_image | Get test image

# **get_configuration**
> Configuration get_configuration()

Get public information

Returns public information about the Oneprovider service.  This endpoint does not require authentication.  ***Example cURL requests***  **Get public information about the Oneprovider service** ```bash curl -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/configuration\"  {     \"providerId\": \"c4798eb2dbd2486fae940e6fa0a5071d\",     \"name\": \"ProviderName\",     \"domain\": \"zone.domain.org\",     \"onezoneDomain\": \"example.domain.org\",     \"version\": \"R14B04\",     \"build\": \"14-g0d0fd5b\",     \"compatibleOnezoneVersions\": [\"R13B04, R14B04\"],     \"compatibleOneproviderVersions\": [\"R14B04\"],     \"compatibleOneclientVersions\": [\"R14B04\"] } ``` 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.OneproviderApi(oneprovider_client.ApiClient(configuration))

try:
    # Get public information
    api_response = api_instance.get_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OneproviderApi->get_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Configuration**](Configuration.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health**
> health()

Check cluster health

Returns status code indicating oneprovider service health status. This endpoint does not require authentication. 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.OneproviderApi(oneprovider_client.ApiClient(configuration))

try:
    # Check cluster health
    api_instance.health()
except ApiException as e:
    print("Exception when calling OneproviderApi->health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_image**
> test_image()

Get test image

This endpoint returns a dummy image in `.png` format. It is used internally by web applications across Onedata to check connectivity with certain services. This endpoint does not require authentication. 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.OneproviderApi(oneprovider_client.ApiClient(configuration))

try:
    # Get test image
    api_instance.test_image()
except ApiException as e:
    print("Exception when calling OneproviderApi->test_image: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

