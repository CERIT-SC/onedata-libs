# oneprovider_client.DatasetApi

All URIs are relative to */api/v3/oneprovider*

Method | HTTP request | Description
------------- | ------------- | -------------
[**establish_dataset**](DatasetApi.md#establish_dataset) | **POST** /datasets | Establish dataset
[**get_dataset**](DatasetApi.md#get_dataset) | **GET** /datasets/{did} | Get dataset information
[**get_file_dataset_summary**](DatasetApi.md#get_file_dataset_summary) | **GET** /data/{id}/dataset/summary | Get dataset summary for file or directory
[**list_dataset_children**](DatasetApi.md#list_dataset_children) | **GET** /datasets/{did}/children | List child datasets of a dataset
[**list_space_top_datasets**](DatasetApi.md#list_space_top_datasets) | **GET** /spaces/{sid}/datasets | List space top datasets
[**remove_dataset**](DatasetApi.md#remove_dataset) | **DELETE** /datasets/{did} | Remove dataset
[**update_dataset**](DatasetApi.md#update_dataset) | **PATCH** /datasets/{did} | Update dataset

# **establish_dataset**
> InlineResponse2016 establish_dataset(body)

Establish dataset

Establishes a dataset with the specified file/directory as the dataset's root. For each file/directory, only one dataset can be established.  This operation requires `space_manage_datasets` privilege.  ***Example cURL requests***  **Establish dataset** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/datasets\" \\ -H \"Content-Type: application/json\" -d '{     \"rootFileId\": \"'$FILE_ID'\",     \"protectionFlags\": [\"data_protection\"] }' ``` 

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
api_instance = oneprovider_client.DatasetApi(oneprovider_client.ApiClient(configuration))
body = oneprovider_client.DatasetEstablishRequest() # DatasetEstablishRequest | Dataset properties.

try:
    # Establish dataset
    api_response = api_instance.establish_dataset(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->establish_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DatasetEstablishRequest**](DatasetEstablishRequest.md)| Dataset properties. | 

### Return type

[**InlineResponse2016**](InlineResponse2016.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset**
> Dataset get_dataset(did)

Get dataset information

Returns the basic information about a dataset.  ***Example cURL requests***  **Get the basic information about dataset** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/datasets/$DATASET_ID\"  {     \"state\": \"attached\",     \"datasetId\": \"1f4b762b1380946e73aeca574c77f14c\",     \"parentId\": null,     \"rootFileId\": \"00000000006CB663736861726547756964233339643236366165646365...\",     \"rootFileType\": \"DIR\",     \"rootFilePath\": \"/MySpace/dir\",     \"rootFileDeleted\": false,     \"protectionFlags\": [\"data_protection\"],     \"effectiveProtectionFlags\": [\"data_protection\", \"metadata_protection\"],     \"creationTime\": 1576152793,     \"archiveCount\": 5 } ``` 

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
api_instance = oneprovider_client.DatasetApi(oneprovider_client.ApiClient(configuration))
did = 'did_example' # str | Dataset Id

try:
    # Get dataset information
    api_response = api_instance.get_dataset(did)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->get_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| Dataset Id | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_dataset_summary**
> DatasetSummary get_file_dataset_summary(id)

Get dataset summary for file or directory

Returns dataset summary for a file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Get file's dataset summary** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/dataset/summary\"  {     \"directDataset\": null,     \"effectiveAncestorDatasets\": [\"1f4b762b1380946e73aeca574c77f14c\", \"64233339643236366165646365626666\"],     \"effectiveProtectionFlags\": [\"data_protection\", \"metadata_protection\"] } ``` 

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
api_instance = oneprovider_client.DatasetApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | Id of the file or directory.

try:
    # Get dataset summary for file or directory
    api_response = api_instance.get_file_dataset_summary(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->get_file_dataset_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the file or directory. | 

### Return type

[**DatasetSummary**](DatasetSummary.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dataset_children**
> Datasets list_dataset_children(did, limit=limit, offset=offset, index=index, token=token)

List child datasets of a dataset

Returns the list of child datasets of a specific dataset. The list of top datasets in a space can be acquired using [this endpoint](#operation/list_space_top_datasets).  ***Example cURL requests***  **List child datasets** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/datasets/$DATASET_ID/children\"  {     \"datasets\": [         {             \"datasetId\": \"1f4b762b1380946e73aeca574c77f14c\",             \"name\": \"File1.txt\"         },         {             \"datasetId\": \"64233339643236366165646365626666\",             \"name\": \"Dir2\"         }     ],     \"nextPageToken\": \"RGlyMjY0MjMzMzM5NjQzMjM2MzY2MTY1NjQ2MzY1NjI2NjY2\" } ``` 

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
api_instance = oneprovider_client.DatasetApi(oneprovider_client.ApiClient(configuration))
did = 'did_example' # str | Dataset Id
limit = 1000 # int | Allows specifying maximum number of entries that should be returned. If there are more child datasets, they can be retrieved using `offset` or `token` query parameters.  (optional) (default to 1000)
offset = 0 # int | Offset determining beginning of the list of datasets returned in the response. Expressed in number of entries, further adjusts the starting point of listing indicated by `index` or `token` parameters. The value can be negative, in such case entries preceding the starting point will be returned.  (optional) (default to 0)
index = 'null' # str | Determines the starting point for listing. The listing will (inclusively) start from the first dataset whose name is lexicographically greater or equal to the specified index. Since the index may include characters that are not URL-safe, it should always be urlencoded.  (optional) (default to null)
token = 'null' # str | Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding `nextPageToken`. If both `token` and `index` are passed, the `token` prevails.  (optional) (default to null)

try:
    # List child datasets of a dataset
    api_response = api_instance.list_dataset_children(did, limit=limit, offset=offset, index=index, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->list_dataset_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| Dataset Id | 
 **limit** | **int**| Allows specifying maximum number of entries that should be returned. If there are more child datasets, they can be retrieved using &#x60;offset&#x60; or &#x60;token&#x60; query parameters.  | [optional] [default to 1000]
 **offset** | **int**| Offset determining beginning of the list of datasets returned in the response. Expressed in number of entries, further adjusts the starting point of listing indicated by &#x60;index&#x60; or &#x60;token&#x60; parameters. The value can be negative, in such case entries preceding the starting point will be returned.  | [optional] [default to 0]
 **index** | **str**| Determines the starting point for listing. The listing will (inclusively) start from the first dataset whose name is lexicographically greater or equal to the specified index. Since the index may include characters that are not URL-safe, it should always be urlencoded.  | [optional] [default to null]
 **token** | **str**| Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding &#x60;nextPageToken&#x60;. If both &#x60;token&#x60; and &#x60;index&#x60; are passed, the &#x60;token&#x60; prevails.  | [optional] [default to null]

### Return type

[**Datasets**](Datasets.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_space_top_datasets**
> Datasets list_space_top_datasets(sid, state, limit=limit, offset=offset, index=index, token=token)

List space top datasets

Returns the list of space's top datasets - ones that do not have any parent dataset. In special case when dataset has been established for space root directory, there is only one top dataset.  Datasets in each space are divided into two separate trees based on their states: * `attached` - this tree represents the hierarchy of datasets, which corresponds   to the hierarchy of files in the space. It can be perceived as a \"compressed\"   file tree, containing only the nodes corresponding to files/directories marked   as a dataset. For example, dataset A is child of dataset B because   B's root directory is ancestor to A's root file and no directory between   them is a root of any attached dataset. Consequently, moving dataset's root file   to other location may change the dataset location in the tree.  * `detached` - this tree represents the hierarchy of datasets for the moment   of detachment and does not change when root files are moved. Individual   datasets from this tree can be reattached, causing the tree to be   restructured in specific cases.  ***Example cURL requests***  **List space top datasets** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/datasets?state=attached\"  {     \"datasets\": [         {             \"datasetId\": \"1f4b762b1380946e73aeca574c77f14c\",             \"name\": \"File1.txt\"         },         {             \"datasetId\": \"64233339643236366165646365626666\",             \"name\": \"Dir2\"         }     ],     \"nextPageToken\": \"RGlyMjY0MjMzMzM5NjQzMjM2MzY2MTY1NjQ2MzY1NjI2NjY2\" } ``` 

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
api_instance = oneprovider_client.DatasetApi(oneprovider_client.ApiClient(configuration))
sid = 'sid_example' # str | Space Id
state = 'attached' # str | The dataset tree to list from. (default to attached)
limit = 100 # int | Allows specifying maximum number of entries that should be returned. If there are more datasets, they can be retrieved using `offset` or `token` query parameters.  (optional) (default to 100)
offset = 0 # int | Offset determining beginning of the list of datasets returned in the response. Expressed in number of entries, further adjusts the starting point of listing indicated by `index` or `token` parameters. The value can be negative, in such case entries preceding the starting point will be returned.  (optional) (default to 0)
index = 'null' # str | Determines the starting point for listing. The listing will (inclusively) start from the first dataset whose name is lexicographically greater or equal to the specified index. Since the index may include characters that are not URL-safe, it should always be urlencoded.  (optional) (default to null)
token = 'null' # str | Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding `nextPageToken`. If both `token` and `index` are passed, the `token` prevails.  (optional) (default to null)

try:
    # List space top datasets
    api_response = api_instance.list_space_top_datasets(sid, state, limit=limit, offset=offset, index=index, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->list_space_top_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Space Id | 
 **state** | **str**| The dataset tree to list from. | [default to attached]
 **limit** | **int**| Allows specifying maximum number of entries that should be returned. If there are more datasets, they can be retrieved using &#x60;offset&#x60; or &#x60;token&#x60; query parameters.  | [optional] [default to 100]
 **offset** | **int**| Offset determining beginning of the list of datasets returned in the response. Expressed in number of entries, further adjusts the starting point of listing indicated by &#x60;index&#x60; or &#x60;token&#x60; parameters. The value can be negative, in such case entries preceding the starting point will be returned.  | [optional] [default to 0]
 **index** | **str**| Determines the starting point for listing. The listing will (inclusively) start from the first dataset whose name is lexicographically greater or equal to the specified index. Since the index may include characters that are not URL-safe, it should always be urlencoded.  | [optional] [default to null]
 **token** | **str**| Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding &#x60;nextPageToken&#x60;. If both &#x60;token&#x60; and &#x60;index&#x60; are passed, the &#x60;token&#x60; prevails.  | [optional] [default to null]

### Return type

[**Datasets**](Datasets.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_dataset**
> remove_dataset(did)

Remove dataset

Removes a specific dataset. This procedure does not modify any files or directories that were a part of the dataset. <!--- TODO VFS-7304 Add information that datasets can be deleted only if they have no archives -->  This operation requires `space_manage_datasets` privilege.  ***Example cURL requests***  **Remove dataset** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/datasets/$DATASET_ID\" ``` 

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
api_instance = oneprovider_client.DatasetApi(oneprovider_client.ApiClient(configuration))
did = 'did_example' # str | Dataset Id

try:
    # Remove dataset
    api_instance.remove_dataset(did)
except ApiException as e:
    print("Exception when calling DatasetApi->remove_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| Dataset Id | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset**
> update_dataset(body, did)

Update dataset

Changes dataset properties.  This operation requires `space_manage_datasets` privilege.  ***Example cURL requests***  **Change dataset protection flags** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X PATCH \"https://$PROVIDER_HOST/api/v3/oneprovider/datasets/$DATASET_ID\" \\ -H \"Content-Type: application/json\" -d '{     \"setProtectionFlags\": [\"metadata_protection\"],     \"unsetProtectionFlags\": [\"data_protection\"] }' ``` 

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
api_instance = oneprovider_client.DatasetApi(oneprovider_client.ApiClient(configuration))
body = oneprovider_client.DatasetUpdateRequest() # DatasetUpdateRequest | Dataset properties
did = 'did_example' # str | Dataset Id

try:
    # Update dataset
    api_instance.update_dataset(body, did)
except ApiException as e:
    print("Exception when calling DatasetApi->update_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DatasetUpdateRequest**](DatasetUpdateRequest.md)| Dataset properties | 
 **did** | **str**| Dataset Id | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

