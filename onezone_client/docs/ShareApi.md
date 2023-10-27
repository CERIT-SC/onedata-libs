# onezone_client.ShareApi

All URIs are relative to */api/v3/onezone*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_public_share_details**](ShareApi.md#get_public_share_details) | **GET** /shares/{id}/public | Get public share details
[**get_share**](ShareApi.md#get_share) | **GET** /shares/{id} | Get share details
[**get_shared_data**](ShareApi.md#get_shared_data) | **GET** /shares/data/{file_id}/{subpath} | Get shared file or directory data
[**list_shares**](ShareApi.md#list_shares) | **GET** /shares | List all shares
[**modify_share**](ShareApi.md#modify_share) | **PATCH** /shares/{id} | Modify share details

# **get_public_share_details**
> Share get_public_share_details(id)

Get public share details

Returns the publicly available details of a specific share. This endpoint is available for anyone knowing the share Id, without authentication.  ***Example cURL requests***  **Get public share details** ```bash curl -X GET https://$ZONE_HOST/api/v3/onezone/shares/$SHARE_ID/public  {   \"shareId\": \"1f4b762b1380946e73aeca574c77f14c\",   \"name\": \"Experiment XYZ\",   \"description\": \"# Experiment XYZ\\nThis collection contains results from Experiment XYZ.\",   \"publicUrl\": \"https://example.com/shares/1f4b762b1380946e73aeca574c77f14c\",   \"publicRestUrl\": \"https://example.com/api/v3/onezone/shares/1f4b762b1380946e73aeca574c77f14c/public\",   \"fileType\": \"dir\",   \"rootFileId\": \"00000000006CB663736861726547756964233339643236366165646365\\   6266666164353939663761373734313235363166342336656331613534313362366634653\\   2623031613563383561386664373937653223316634623736326231333830393436653733\\   6165636135373463373766313463\",   \"handleId\" \"70570c0ebcd081835ca29560708fd98f\",   \"creationTime\": 1576152793 } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ShareApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Share Id.

try:
    # Get public share details
    api_response = api_instance.get_public_share_details(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShareApi->get_public_share_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Share Id. | 

### Return type

[**Share**](Share.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_share**
> Share get_share(id)

Get share details

Returns the private details about a specific share.  NOTE: Only Oneprovider API supports creating / deleting shares and is preferred for all share operations. Onezone API is limited to retrieving and modifying share details.  This operation requires `space_view` privilege in space where share is created or `oz_shares_view` admin privilege.  ***Example cURL requests***  **Get share details** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/shares/$SHARE_ID  {   \"shareId\": \"1f4b762b1380946e73aeca574c77f14c\",   \"name\": \"Experiment XYZ\",   \"description\": \"# Experiment XYZ\\nThis collection contains results from Experiment XYZ.\",   \"publicUrl\": \"https://example.com/shares/1f4b762b1380946e73aeca574c77f14c\",   \"publicRestUrl\": \"https://example.com/api/v3/onezone/shares/1f4b762b1380946e73aeca574c77f14c/public\",   \"fileType\": \"dir\",   \"rootFileId\": \"00000000006CB663736861726547756964233339643236366165646365\\   6266666164353939663761373734313235363166342336656331613534313362366634653\\   2623031613563383561386664373937653223316634623736326231333830393436653733\\   6165636135373463373766313463\",   \"spaceId\": \"6ec1a5413b6f4e2b01a5c85a8fd797e2\",   \"handleId\" \"70570c0ebcd081835ca29560708fd98f\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ShareApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Share Id.

try:
    # Get share details
    api_response = api_instance.get_share(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShareApi->get_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Share Id. | 

### Return type

[**Share**](Share.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_data**
> get_shared_data(file_id, subpath)

Get shared file or directory data

This endpoint can be used to fetch publicly available information and content of a shared file or directory knowing its Id, without any authentication. It redirects to the corresponding REST endpoint in one of the supporting Oneproviders. The Oneprovider is chosen dynamically and may change in time, so the redirection URL should not be cached.  The endpoint accepts only identifiers of shared files/directories and will reject requests if a containing share is deleted. The shared file/directory Id can be acquired either by fetching public share details or by listing a shared directory.  The provided query string (if any) is preserved during redirection - consult corresponding Oneprovider REST endpoints for possible options.  Currently, publicly available operations are: * `{...}/$FILE_ID/content` - download file or directory content   (see Oneprovider [REST endpoint](https://onedata.org/#/home/api/latest/oneprovider?anchor=operation/download_file_content))  * `{...}/$FILE_ID/children` - list directory files and subdirectories   (see Oneprovider [REST endpoint](https://onedata.org/#/home/api/latest/oneprovider?anchor=operation/list_children))  * `{...}/$FILE_ID` - get basic attributes of a file or directory   (see Oneprovider [REST endpoint](https://onedata.org/#/home/api/latest/oneprovider?anchor=operation/get_attrs))  * `{...}/$FILE_ID/metadata/xattrs` - get custom extended attributes (xattrs) associated with a file or directory   (see Oneprovider [REST endpoint](https://onedata.org/#/home/api/latest/oneprovider?anchor=operation/get_xattrs))  * `{...}/$FILE_ID/metadata/json` - get custom JSON metadata associated with a file or directory   (see Oneprovider [REST endpoint](https://onedata.org/#/home/api/latest/oneprovider?anchor=operation/get_json_metadata))  * `{...}/$FILE_ID/metadata/rdf` - get custom RDF metadata associated with a file or directory   (see Oneprovider [REST endpoint](https://onedata.org/#/home/api/latest/oneprovider?anchor=operation/get_rdf_metadata))  The endpoint will return `503 Service Unavailable` when there is no suitable Oneprovider to handle the request and `501 Not Implemented` when all available Oneproviders are in versions older than `20.02.*`. If an invalid subpath is requested, the target Oneprovider will respond with a proper error.  ***Example cURL requests***  **Get shared file or directory data** ```bash curl -v -X GET https://$ZONE_HOST/api/v3/onezone/shares/data/$FILE_ID/content  < HTTP/1.1 307 Temporary Redirect < location: https://provider.example.com/api/v3/oneprovider/data/$FILE_ID/content  # -------------------------------------------------------------------------------  curl -v -X GET https://$ZONE_HOST/api/v3/onezone/shares/data/$FILE_ID/children?limit=3  < HTTP/1.1 307 Temporary Redirect < location: https://provider.example.com/api/v3/oneprovider/data/$FILE_ID/children?limit=3  # -------------------------------------------------------------------------------  # automatically follow redirects with -L option, request a byte range curl -L -X GET https://$ZONE_HOST/api/v3/onezone/shares/data/$FILE_ID/content \\ -H \"Range: bytes=5-8\"  fghi ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ShareApi(onezone_client.ApiClient(configuration))
file_id = 'file_id_example' # str | Shared file/directory Id.
subpath = 'subpath_example' # str | Subpath corresponding to desired [Oneprovider REST API](https://onedata.org/#/home/api/latest/oneprovider?anchor=tag/Basic-File-Operations) operation. 

try:
    # Get shared file or directory data
    api_instance.get_shared_data(file_id, subpath)
except ApiException as e:
    print("Exception when calling ShareApi->get_shared_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Shared file/directory Id. | 
 **subpath** | **str**| Subpath corresponding to desired [Oneprovider REST API](https://onedata.org/#/home/api/latest/oneprovider?anchor&#x3D;tag/Basic-File-Operations) operation.  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shares**
> Shares list_shares()

List all shares

Returns the list of all shares managed by the Onezone service.  NOTE: Only Oneprovider API supports creating / deleting shares and is preferred for all share operations. Onezone API is limited to retrieving and modifying share details.  This operation requires admin privilege `oz_shares_list`.  ***Example cURL requests***  **Get shares** ```bash curl -u admin:password -X GET https://$ZONE_HOST/api/v3/onezone/shares  {   \"shares\": [     \"303884afb761d91a7362b2841647bc08\",     \"32919d6a51bac9b040c7cb7961fdccf3\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ShareApi(onezone_client.ApiClient(configuration))

try:
    # List all shares
    api_response = api_instance.list_shares()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShareApi->list_shares: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Shares**](Shares.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_share**
> modify_share(body, id)

Modify share details

Updates the share details - name or description.  NOTE: Only Oneprovider API supports creating / deleting shares and is preferred for all share operations. Onezone API is limited to retrieving and modifying share details.  This operation requires privilege `space_manage_shares` in space in which the share was created or `oz_shares_update` admin privilege.  ***Example cURL requests***  **Modify share details** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"name\": \"NewShareName\", \"description\": \"# New description\"}' \\ https://$ZONE_HOST/api/v3/onezone/shares/$SHARE_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ShareApi(onezone_client.ApiClient(configuration))
body = onezone_client.SharesIdBody() # SharesIdBody | New share details
id = 'id_example' # str | Space Id.

try:
    # Modify share details
    api_instance.modify_share(body, id)
except ApiException as e:
    print("Exception when calling ShareApi->modify_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SharesIdBody**](SharesIdBody.md)| New share details | 
 **id** | **str**| Space Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

