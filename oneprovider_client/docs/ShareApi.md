# oneprovider_client.ShareApi

All URIs are relative to */api/v3/oneprovider*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_share**](ShareApi.md#create_share) | **POST** /shares | Create share
[**get_share**](ShareApi.md#get_share) | **GET** /shares/{shid} | Get share info
[**remove_share**](ShareApi.md#remove_share) | **DELETE** /shares/{shid} | Remove share
[**update_share**](ShareApi.md#update_share) | **PATCH** /shares/{shid} | Update share

# **create_share**
> InlineResponse2015 create_share(body)

Create share

Shares a file or a directory. Shared files can be viewed by everyone through public URL. This operation assigns a share Id that can be used to manage share, see:   * [Get basic information about share](#operation/get_share)   * [List shares associated with file or directory](#operation/list_file_shares_by_id)   * [Change name of the share](#operation/update_share)   * [Remove share](#operation/remove_share)  Any number of shares can be associated with each file or directory.  This operation requires `space_manage_share` privilege.  ***Example cURL requests***  **Create share** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/shares\" \\ -H \"Content-Type: application/json\" -d '{\"name\": \"MyShare\", \"rootFileId\": \"'$FILE_ID'\"}' ``` 

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
api_instance = oneprovider_client.ShareApi(oneprovider_client.ApiClient(configuration))
body = oneprovider_client.ShareCreateRequest() # ShareCreateRequest | Share properties.

try:
    # Create share
    api_response = api_instance.create_share(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShareApi->create_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShareCreateRequest**](ShareCreateRequest.md)| Share properties. | 

### Return type

[**InlineResponse2015**](InlineResponse2015.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_share**
> Share get_share(shid)

Get share info

Returns the basic information about share.  ***Example cURL requests***  **Get the basic information about share** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/shares/$SHARE_ID\"  {     \"shareId\": \"1f4b762b1380946e73aeca574c77f14c\",     \"name\": \"Experiment XYZ\",     \"description\": \"# Experiment XYZ\\nThis collection contains results from Experiment XYZ.\",     \"publicUrl\": \"https://onedata.org/shares/1f4b762b1380946e73aeca574c77f14c\",     \"rootFileType\": \"DIR\",     \"rootFileId\": \"00000000006CB663736861726547756964233339643236366165646365...\",     \"spaceId\": \"6ec1a5413b6f4e2b01a5c85a8fd797e2\",     \"handleId\" \"doi:10.15911/MyShares.726855\" } ``` 

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
api_instance = oneprovider_client.ShareApi(oneprovider_client.ApiClient(configuration))
shid = 'shid_example' # str | Share Id

try:
    # Get share info
    api_response = api_instance.get_share(shid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShareApi->get_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shid** | **str**| Share Id | 

### Return type

[**Share**](Share.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_share**
> remove_share(shid)

Remove share

Removes a specific share. This operation will not remove data from shared file or directory but it will not be accessible through public url anymore.  This operation requires `space_manage_share` privilege.  ***Example cURL requests***  **Remove share** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/shares/$SHARE_ID\" ``` 

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
api_instance = oneprovider_client.ShareApi(oneprovider_client.ApiClient(configuration))
shid = 'shid_example' # str | Share Id

try:
    # Remove share
    api_instance.remove_share(shid)
except ApiException as e:
    print("Exception when calling ShareApi->remove_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shid** | **str**| Share Id | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_share**
> update_share(body, shid)

Update share

Changes name and/or description of the share.  This operation requires `space_manage_share` privilege.  ***Example cURL requests***  **Change name of the share** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X PATCH \"https://$PROVIDER_HOST/api/v3/oneprovider/shares/$SHARE_ID\" \\ -H \"Content-Type: application/json\" -d '{     \"name\": \"NewShareName\",     \"description\": \"# New description\" }' ``` 

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
api_instance = oneprovider_client.ShareApi(oneprovider_client.ApiClient(configuration))
body = oneprovider_client.SharesShidBody() # SharesShidBody | New share details
shid = 'shid_example' # str | Share Id

try:
    # Update share
    api_instance.update_share(body, shid)
except ApiException as e:
    print("Exception when calling ShareApi->update_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SharesShidBody**](SharesShidBody.md)| New share details | 
 **shid** | **str**| Share Id | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

