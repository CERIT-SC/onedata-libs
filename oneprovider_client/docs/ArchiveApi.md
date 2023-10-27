# oneprovider_client.ArchiveApi

All URIs are relative to */api/v3/oneprovider*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_archive_recall**](ArchiveApi.md#cancel_archive_recall) | **POST** /data/{id}/recall/cancel | Cancel an archive recall
[**create_archive**](ArchiveApi.md#create_archive) | **POST** /archives | Create archive from a dataset
[**delete_archive**](ArchiveApi.md#delete_archive) | **POST** /archives/{aid}/delete | Delete archive
[**get_archive**](ArchiveApi.md#get_archive) | **GET** /archives/{aid} | Get archive information
[**get_archive_recall_details**](ArchiveApi.md#get_archive_recall_details) | **GET** /data/{id}/recall/details | Get details of an archive recall
[**get_archive_recall_progress**](ArchiveApi.md#get_archive_recall_progress) | **GET** /data/{id}/recall/progress | Get progress of an archive recall
[**list_dataset_archives**](ArchiveApi.md#list_dataset_archives) | **GET** /datasets/{did}/archives | List archives of a dataset
[**recall_archive**](ArchiveApi.md#recall_archive) | **POST** /archives/{aid}/recall | Recall archive
[**update_archive**](ArchiveApi.md#update_archive) | **PATCH** /archives/{aid} | Update archive

# **cancel_archive_recall**
> cancel_archive_recall(id)

Cancel an archive recall

Cancels an ongoing archive recall, identified by the root [FILE_ID] to which the archive  is being recalled.  **Cancel archive recall** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/recall/cancel\" ``` 

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
api_instance = oneprovider_client.ArchiveApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | File Id.

try:
    # Cancel an archive recall
    api_instance.cancel_archive_recall(id)
except ApiException as e:
    print("Exception when calling ArchiveApi->cancel_archive_recall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_archive**
> InlineResponse2017 create_archive(body)

Create archive from a dataset

Creates an archive of a dataset - a snapshot of its data and metadata.  This operation requires `space_manage_datasets` and `space_create_archives` privileges.  ***Example cURL requests***  **Create archive from a dataset** <!--- TODO VFS-7616 add metadata structure to the example-->  ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/archives\" \\ -H \"Content-Type: application/json\" -d '{     \"datasetId\": \"'$DATASET_ID'\",     \"config\": {         \"incremental\": {\"enabled\": true},         \"includeDip\": false,         \"layout\": \"bagit\",         \"createNestedArchives\": true,         \"followSymlinks\": true     },     \"preservedCallback\": \"https://example.org/preserved_archives\",     \"deletedCallback\": \"https://example.org/deleted_archives\",     \"description\": \"Archived dataset with experiment data from 2021.\" }' ``` 

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
api_instance = oneprovider_client.ArchiveApi(oneprovider_client.ApiClient(configuration))
body = oneprovider_client.ArchiveCreateRequest() # ArchiveCreateRequest | Dataset properties.

try:
    # Create archive from a dataset
    api_response = api_instance.create_archive(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->create_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArchiveCreateRequest**](ArchiveCreateRequest.md)| Dataset properties. | 

### Return type

[**InlineResponse2017**](InlineResponse2017.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_archive**
> delete_archive(aid, body=body)

Delete archive

Initializes process of purging an archive. First, the archived data is deleted from the storage, then all the information concerning the archive is deleted. The process may be time consuming therefore it is possible to pass callback URL on which the POST request will be performed to notify that the process has finished. The callback request will include JSON `{\"archiveId\": $ARCHIVE_ID}` as a body to determine which archive has been deleted.  This operation requires `space_manage_datasets` and `space_remove_archives` privileges.  ***Example cURL requests***  **Delete archive** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/archives/$ARCHIVE_ID/delete\" \\ -H \"Content-Type: application/json\" -d '{     \"deletedCallback\": \"https://example.org/deleted_archives\" }' ``` 

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
api_instance = oneprovider_client.ArchiveApi(oneprovider_client.ApiClient(configuration))
aid = 'aid_example' # str | Id of a specific archive to be deleted.
body = oneprovider_client.ArchiveDeleteRequest() # ArchiveDeleteRequest | Parameters for initializing purging of an archive. (optional)

try:
    # Delete archive
    api_instance.delete_archive(aid, body=body)
except ApiException as e:
    print("Exception when calling ArchiveApi->delete_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| Id of a specific archive to be deleted. | 
 **body** | [**ArchiveDeleteRequest**](ArchiveDeleteRequest.md)| Parameters for initializing purging of an archive. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_archive**
> Archive get_archive(aid)

Get archive information

Returns the basic information about an archive.  This operation requires `space_view_archives` privilege.  ***Example cURL requests***  **Get the basic information about archive** <!--- TODO VFS-7616 add metadata structure to the example-->  ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/archives/$ARCHIVE_ID\"  {     \"archiveId\": \"ae6f78c89a97c9e78e891105f703bcb8\",     \"state\": \"preserved\",     \"datasetId\": \"1f4b762b1380946e73aeca574c77f14c\",     \"rootDirectoryId\": \"00000000006CB663736861726547756964233339643236366165646365\",     \"creationTime\": 1576152793,     \"config\": {       \"incremental\": {\"enabled\": true},       \"includeDip\": false,       \"layout\": \"bagit\",     },     \"preservedCallback\": \"https://example.org/preserved_archives\",     \"deletedCallback\": null,     \"description\": \"Archived dataset with experiment data from 2021.\",     \"stats\": {         \"filesArchived\": 7940,         \"filesFailed\": 3,         \"bytesArchived\": 879245378924537     },     \"baseArchiveId\": \"ae6f78c89a97c9e78e891105f703bcb8\",     \"relatedAipId\": \"e891105f703bcb8ae6f78c89a97c9e78\",     \"relatedDipId\": \"78e891105f703bcb8ae6f78c89a97c9e\" } ``` 

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
api_instance = oneprovider_client.ArchiveApi(oneprovider_client.ApiClient(configuration))
aid = 'aid_example' # str | Archive Id

try:
    # Get archive information
    api_response = api_instance.get_archive(aid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->get_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| Archive Id | 

### Return type

[**Archive**](Archive.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_archive_recall_details**
> ArchiveRecallDetails get_archive_recall_details(id)

Get details of an archive recall

If this file is a root of a past or ongoing archive recall, returns its details. Otherwise,  returns `404 NOT FOUND` error.  **Get archive recall details** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/recall/details\"  {     \"archiveId\": \"$ARCHIVE_ID\",     \"datasetId\": \"$DATASET_ID\",     \"startTime\": 1643103923417,     \"finishTime\": 1643103933417,     \"totalFileCount\" : 1,     \"totalByteSize\": 65536,     \"lastError\": {         \"fileId\": \"$FILE_ID\",         \"reason\": {           \"description\": \"The resource could not be found.\",           \"id\": \"notFound\"         }     } } ``` 

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
api_instance = oneprovider_client.ArchiveApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | File Id.

try:
    # Get details of an archive recall
    api_response = api_instance.get_archive_recall_details(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->get_archive_recall_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File Id. | 

### Return type

[**ArchiveRecallDetails**](ArchiveRecallDetails.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_archive_recall_progress**
> ArchiveRecallProgress get_archive_recall_progress(id)

Get progress of an archive recall

If this file is a root of a past or ongoing archive recall, returns its progress. Otherwise,  returns `404 NOT FOUND` error. This resource is only available on the Oneprovider performing the recall.  **Get archive recall progress** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/recall/progress\"  {     \"filesCopied\": 8,     \"bytesCopied\": 16384,     \"filesFailed\": 1 } ``` 

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
api_instance = oneprovider_client.ArchiveApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | File Id.

try:
    # Get progress of an archive recall
    api_response = api_instance.get_archive_recall_progress(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->get_archive_recall_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File Id. | 

### Return type

[**ArchiveRecallProgress**](ArchiveRecallProgress.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dataset_archives**
> Archives list_dataset_archives(did, limit=limit, offset=offset, token=token)

List archives of a dataset

Returns the list of archives created from a specific dataset.  This operation requires `space_view_archives` privilege.  ***Example cURL requests***  **List dataset archives** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/datasets/$DATASET_ID/archives\"  {     \"archives\": [\"d0f08b098804da5504609b2c54b507b3\", \"5a1e63f7cf5282a206144f77822c3f10\"],     \"nextPageToken\": \"UkdseU1qWTBNak16TXpNNU5qUXpNak0yTXpZMk1UWTFOalEyTXpZMU5qSTJOalky\" } ``` 

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
api_instance = oneprovider_client.ArchiveApi(oneprovider_client.ApiClient(configuration))
did = 'did_example' # str | Dataset Id
limit = 1000 # int | Allows specifying maximum number of entries that should be returned. If there are more archives, they can be retrieved using `offset` or `token` query parameters.  (optional) (default to 1000)
offset = 0 # int | Offset determining beginning of the list of archives returned in the response. Expressed in number of entries, further adjusts the starting point of listing indicated by `token` parameter. The value can be negative, in such case entries preceding the starting point will be returned.  (optional) (default to 0)
token = 'null' # str | Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding `nextPageToken`.  (optional) (default to null)

try:
    # List archives of a dataset
    api_response = api_instance.list_dataset_archives(did, limit=limit, offset=offset, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->list_dataset_archives: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| Dataset Id | 
 **limit** | **int**| Allows specifying maximum number of entries that should be returned. If there are more archives, they can be retrieved using &#x60;offset&#x60; or &#x60;token&#x60; query parameters.  | [optional] [default to 1000]
 **offset** | **int**| Offset determining beginning of the list of archives returned in the response. Expressed in number of entries, further adjusts the starting point of listing indicated by &#x60;token&#x60; parameter. The value can be negative, in such case entries preceding the starting point will be returned.  | [optional] [default to 0]
 **token** | **str**| Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding &#x60;nextPageToken&#x60;.  | [optional] [default to null]

### Return type

[**Archives**](Archives.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recall_archive**
> ArchiveRecallResponse recall_archive(body, aid)

Recall archive

Initializes process of recalling an archive. The recall creates a copy of the archive content in specified destination.  This operation requires `space_recall_archives` privilege.  ***Example cURL requests***  **Recall archive** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/archives/$ARCHIVE_ID/recall\" \\ -H \"Content-Type: application/json\" -d '{     \"parentDirectoryId\": \"$PARENT_DIRECTORY_ID\",     \"targetFileName\": \"example_name\" }'  {     \"rootFileId\": \"$ROOT_FILE_ID\" } ``` 

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
api_instance = oneprovider_client.ArchiveApi(oneprovider_client.ApiClient(configuration))
body = oneprovider_client.ArchiveRecallRequest() # ArchiveRecallRequest | Parameters for initializing recall of an archive.
aid = 'aid_example' # str | Id of a specific archive to be recalled.

try:
    # Recall archive
    api_response = api_instance.recall_archive(body, aid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->recall_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArchiveRecallRequest**](ArchiveRecallRequest.md)| Parameters for initializing recall of an archive. | 
 **aid** | **str**| Id of a specific archive to be recalled. | 

### Return type

[**ArchiveRecallResponse**](ArchiveRecallResponse.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_archive**
> update_archive(body, aid)

Update archive

Changes archive properties.  This operation requires `space_manage_datasets` and `space_create_archives` privileges.  ***Example cURL requests***  **Change archive description and callbacks** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X PATCH \"https://$PROVIDER_HOST/api/v3/oneprovider/archives/$ARCHIVE_ID\" \\ -H \"Content-Type: application/json\" -d '{     \"description\": \"New archive description\",     \"preservedCallback\": \"https://archives.org/preserved_archives\",     \"deletedCallback\": \"https://archives.org/deleted_archives\" }' ``` 

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
api_instance = oneprovider_client.ArchiveApi(oneprovider_client.ApiClient(configuration))
body = oneprovider_client.ArchiveUpdateRequest() # ArchiveUpdateRequest | Archive properties
aid = 'aid_example' # str | Archive Id

try:
    # Update archive
    api_instance.update_archive(body, aid)
except ApiException as e:
    print("Exception when calling ArchiveApi->update_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArchiveUpdateRequest**](ArchiveUpdateRequest.md)| Archive properties | 
 **aid** | **str**| Archive Id | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

