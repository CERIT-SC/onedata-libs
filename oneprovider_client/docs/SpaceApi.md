# oneprovider_client.SpaceApi

All URIs are relative to */api/v3/oneprovider*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_spaces**](SpaceApi.md#get_all_spaces) | **GET** /spaces | Get all user spaces
[**get_space**](SpaceApi.md#get_space) | **GET** /spaces/{sid} | Get basic space information

# **get_all_spaces**
> list[InlineResponse200] get_all_spaces()

Get all user spaces

Returns the list of all user spaces.  ***Example cURL requests***  **List all user spaces** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces\"  [     {         \"spaceId\": \"fb519d81146bcc635b890ff03a5da0fdch34fe\",         \"fileId\": \"094576776E667431723230677767776C6B497031394E445F6E3868677873...\",         \"name\": \"Space1\"     },     {         \"spaceId\": \"e14039c53235c44f2f25dce4c90b1f0acha61c\",         \"fileId\": \"000000184465677569642373706163655F73706163653123737061636531...\",         \"name\": \"Space2\"     } ] ``` 

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
api_instance = oneprovider_client.SpaceApi(oneprovider_client.ApiClient(configuration))

try:
    # Get all user spaces
    api_response = api_instance.get_all_spaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->get_all_spaces: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space**
> Space get_space(sid)

Get basic space information

Returns the basic information about space with given Id.  ***Example cURL requests***  **Get information about a specific space** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID\"  {     \"name\": \"My Space 1\",     \"providers\": [         {             \"providerId\": \"a0b1d2e6ad583ba1b14caf3b71bc6129ch4f74\",             \"providerName\": \"MyPrivateCloud\"         },         {             \"providerId\": \"b107606a22f006b82f6f665a9e6f116cch0500\",             \"providerName\": \"PublicCloud1\"         }     ],     \"spaceId\": \"fb519d81146bcc635b890ff03a5da0fdch34fe\",     \"fileId\": \"094576776E667431723230677767776C6B497031394E445F6E3868677873...\" } ``` 

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
api_instance = oneprovider_client.SpaceApi(oneprovider_client.ApiClient(configuration))
sid = 'sid_example' # str | Space Id.

try:
    # Get basic space information
    api_response = api_instance.get_space(sid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->get_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Space Id. | 

### Return type

[**Space**](Space.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

