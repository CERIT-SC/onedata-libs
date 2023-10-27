# oneprovider_client.FilePathResolutionApi

All URIs are relative to */api/v3/oneprovider*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lookup_file_id**](FilePathResolutionApi.md#lookup_file_id) | **POST** /lookup-file-id/{path} | Lookup file id

# **lookup_file_id**
> InlineResponse2001 lookup_file_id(path)

Lookup file id

Returns Id of file or directory specified by path.  ***Example cURL requests***  **Lookup file id** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/lookup-file-id/MySpace/dir/readme.txt\"  {   \"fileId\": \"094576776E667431723230677767776C6B497031394E445F6E3868677873...\" } ``` 

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
api_instance = oneprovider_client.FilePathResolutionApi(oneprovider_client.ApiClient(configuration))
path = 'path_example' # str | File path (e.g. '/MySpace/dir/readme.txt')

try:
    # Lookup file id
    api_response = api_instance.lookup_file_id(path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilePathResolutionApi->lookup_file_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path (e.g. &#x27;/MySpace/dir/readme.txt&#x27;) | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

