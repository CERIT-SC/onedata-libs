# onepanel_client.StoragesApi

All URIs are relative to */api/v3/onepanel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_storage**](StoragesApi.md#add_storage) | **POST** /provider/storages | Add storage
[**get_storage_details**](StoragesApi.md#get_storage_details) | **GET** /provider/storages/{id} | Get storage details
[**get_storages**](StoragesApi.md#get_storages) | **GET** /provider/storages | Get storages
[**modify_storage**](StoragesApi.md#modify_storage) | **PATCH** /provider/storages/{id} | Modify storage config
[**remove_storage**](StoragesApi.md#remove_storage) | **DELETE** /provider/storages/{id} | Remove storage

# **add_storage**
> StorageCreateResponse add_storage(body)

Add storage

Adds additional storage resources to the provider.  ***Example cURL requests***  **Add storage** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST https://$OP_PANEL_HOST/api/v3/onepanel/provider/storages \\ -H \"Content-Type: application/json\" -d '{     \"My S3 Storage\": {         \"type\": \"s3\",         \"hostname\": \"https://iam.example.com:443\",         \"bucketName\": \"bucket1.iam.example.com\",         \"skipStorageDetection\": true     },     \"My Posix Storage\": {         \"type\": \"posix\",         \"mountPoint\": \"/volumes/inexistent/path\"     } }'  {   \"My S3 Storage\": {       \"id\": \"f891d1ddf693232bbf0c11fe3cd9f7e7cheda9\"   },   \"My Posix Storage\": {       \"error\": {           \"id\": \"storageTestFailed\",           \"description\": \"Failed to write test file on storage.\",           \"details\": {               \"operation\": \"write\"           }       }   } } ``` 

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
api_instance = onepanel_client.StoragesApi(onepanel_client.ApiClient(configuration))
body = NULL # dict(str, StorageCreateDetails) | The configuration details of storage resources to be added to the provider deployment. Must be an object with unique names for the storages as keys and their corresponding configuration (objects) as values - see the request body example.


try:
    # Add storage
    api_response = api_instance.add_storage(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesApi->add_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, StorageCreateDetails)**](dict.md)| The configuration details of storage resources to be added to the provider deployment. Must be an object with unique names for the storages as keys and their corresponding configuration (objects) as values - see the request body example.
 | 

### Return type

[**StorageCreateResponse**](StorageCreateResponse.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_details**
> StorageGetDetails get_storage_details(id)

Get storage details

Returns the details of the selected storage.  ***Example cURL requests***  **Get Storage Details** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET https:/$OP_PANEL_HOST/api/v3/onepanel/provider/storages/$STORAGE_ID  {     \"type\": \"s3\",     \"storagePathType\": \"flat\",     \"skipStorageDetection\": true,     \"signatureVersion\": 4,     \"scheme\": \"http\",     \"readonly\": false,     \"qosParameters\":{         \"storageId\": \"05b6c0a9b72e475c9d5061b0b7e16947chbcdc\",         \"providerId\": \"03c7e42a793912307b01b1bbb72a3a6bch4c1c\"     },     \"name\": \"My S3 Storage\",     \"maximumCanonicalObjectSize\": 67108864,     \"lumaFeed\": \"auto\",     \"importedStorage\": false,     \"id\": \"05b6c0a9b72e475c9d5061b0b7e16947chbcdc\",     \"hostname\": \"https://iam.exampele.com:443/\",     \"fileMode\": \"0664\",     \"dirMode\": \"0775\",     \"bucketName\": \"bucket1.iam.examplee.com\",     \"blockSize\": 10485760,     \"accessKey\": \"\" } ``` 

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
api_instance = onepanel_client.StoragesApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage resource, which details should be returned. 

try:
    # Get storage details
    api_response = api_instance.get_storage_details(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesApi->get_storage_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a storage resource, which details should be returned.  | 

### Return type

[**StorageGetDetails**](StorageGetDetails.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storages**
> ProviderStorages get_storages()

Get storages

Returns the list of provider storage resources and their details.  ***Example cURL requests***  **Get provider storage ids** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET https://$OP_PANEL_HOST/api/v3/onepanel/provider/storages  {     \"ids\": [         \"18a42a43b1b2d92455ffa09e9a15df7fch4f82\",         \"0a26877440f6ce457106c6958dfe7ecbch0ac6\",         \"b3d7d10504393556d9b1631a74c34520ch8359\"     ] } ``` 

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
api_instance = onepanel_client.StoragesApi(onepanel_client.ApiClient(configuration))

try:
    # Get storages
    api_response = api_instance.get_storages()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesApi->get_storages: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProviderStorages**](ProviderStorages.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_storage**
> StorageModifyDetails modify_storage(body, id)

Modify storage config

Modifies storage configuration.  ***Example cURL requests***  **Modify storage name. Notice, that current storage name is the map key.** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X PATCH https://$OP_PANEL_HOST/api/v3/onepanel/provider/storages/$STORAGE_ID \\ -H \"Content-Type: application/json\" -d '{     \"My S3 Storage\": {         \"type\":\"s3\",         \"name\": \"My S3 Storage Updated\"     } }'  {     \"type\": \"s3\",     \"storagePathType\": \"flat\",     \"skipStorageDetection\": \"true\",     \"signatureVersion\": \"4\",     \"scheme\": \"http\",     \"readonly\": false,     \"qosParameters\": {         \"storageId\": \"2456aa013af797dbef27743790a5f12cche680\",         \"providerId\": \"03c7e42a793912307b01b1bbb72a3a6bch4c1c\"     },     \"name\": \"My S3 Storage Updated\",     \"maximumCanonicalObjectSize\": \"67108864\",     \"lumaFeed\": \"auto\",     \"importedStorage\": false,     \"id\": \"2456aa013af797dbef27743790a5f12cche680\",     \"hostname\": \"https://iam.exampele.com:443/\",     \"fileMode\": \"0664\",     \"dirMode\": \"0775\",     \"bucketName\": \"bucket1.iam.examplee.com\",     \"blockSize\": \"10485760\",     \"accessKey\": \"\" } ``` 

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
api_instance = onepanel_client.StoragesApi(onepanel_client.ApiClient(configuration))
body = NULL # dict(str, StorageModifyDetails) | An object with one key - the current name of the storage that is being modified - and its value set to an object with updated parameters.

id = 'id_example' # str | The Id of the storage resource which details should be modified. 

try:
    # Modify storage config
    api_response = api_instance.modify_storage(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesApi->modify_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, StorageModifyDetails)**](dict.md)| An object with one key - the current name of the storage that is being modified - and its value set to an object with updated parameters.
 | 
 **id** | **str**| The Id of the storage resource which details should be modified.  | 

### Return type

[**StorageModifyDetails**](StorageModifyDetails.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_storage**
> remove_storage(id)

Remove storage

Removes storage from the cluster. Only storage not supporting any spaces can be removed.  ***Example cURL requests***  **Remove storage** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X DELETE https://$OP_PANEL_HOST/api/v3/onepanel/provider/storages/$STORAGE_ID ``` 

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
api_instance = onepanel_client.StoragesApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of the storage to remove.

try:
    # Remove storage
    api_instance.remove_storage(id)
except ApiException as e:
    print("Exception when calling StoragesApi->remove_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the storage to remove. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

