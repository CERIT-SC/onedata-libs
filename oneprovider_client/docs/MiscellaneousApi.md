# oneprovider_client.MiscellaneousApi

All URIs are relative to */api/v3/oneprovider*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_directory_size_stats**](MiscellaneousApi.md#get_directory_size_stats) | **GET** /data/{id}/dir_size_stats | Get directory size statistics
[**register_file**](MiscellaneousApi.md#register_file) | **POST** /data/register | Register file

# **get_directory_size_stats**
> DirSizeStatsResponse get_directory_size_stats(body, id)

Get directory size statistics

Retrieves historical size statistics over time for a directory. The response includes only the information pertaining to the queried provider; in order to collect globally-complete statistics, all providers supporting the space must be queried. There may be discrepancies in statistics such as logical size of data, which stem from synchronization delays between providers.  Size statistics over time are available only for directories. They are collected hierarchically i.e. for a  certain directory, its statistics are a sum of statistics for the directory (regarding its direct children), and the statistics from all its subdirectories. Additionally, size statistics for the space directory encompass relevant information from archives.  **This endpoint requires the size statistics to be enabled for the containing space on the queried provider.** Otherwise, an adequate error will be returned.  Two request modes are supported:    * `layout` - returns information about the structure of stats collection,  i.e. the names of the available time series and metrics within them   * `slice` - returns a slice of statistics as a collection of slices of  requested time series and metrics  The following time series are available for each directory:   * `total_size` - the total logical size of file data contained in the directory,  i.e. the sum of logical byte sizes of all regular files.   * `storage_use_$STORAGE_ID` - storage size used to store the physical data of the contained files for given `$STORAGE_ID`. Only the storage backends owned by the queried providers are returned.   * `reg_file_and_link_count` - the count of regular files, hardlinks,  and symbolic links contained in the directory.   * `dir_count` - the count of directories contained in the directory.   * `file_errors_count` - the count of error occurrences when the statistics  mechanisms were not able to gather size information about a certain file.   * `dir_errors_count` - like above, for directories.  If the values of `file_errors_count` or `dir_errors_count` are not zero, the statistics may not be accurate.  The following metrics are available for each time series: `day`, `hour`, `minute`, `month`.  ***Example cURL requests***  **Get the layout of directory size statistics**     ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$DIR_ID/dir_size_stats\" \\ -H \"Content-Type: application/json\" -d '{     \"mode\": \"layout\"   }'  {     \"layout\": {         \"total_size\": [             \"day\",             \"hour\",             \"minute\",             \"month\"         ],         \"storage_use_7ab46e96fdb27a2694493c2c5bd7491dch8f55\": [...],         \"reg_file_and_link_count\": [...],         \"file_errors_count\": [...],         \"dir_errors_count\": [...],         \"dir_count\": [...]     } } ```  **Get a slice of directory size statistics**     ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$DIR_ID/dir_size_stats\" \\ -H \"Content-Type: application/json\" -d '{     \"mode\": \"slice\",     \"extendedInfo\": true,     \"layout\": {         \"total_size\": [             \"minute\"         ],         \"storage_use_7ab46e96fdb27a2694493c2c5bd7491dch8f55\": [             \"minute\"         ]     },     \"startTimestamp\": 1687513285,     \"stopTimestamp\": 1687499802,     \"windowLimit\": 31 }'  {     \"slice\": {         \"total_size\": {             \"minute\": [                 {                     \"value\": 883365,                     \"timestamp\": 1687513260,                     \"lastMeasurementTimestamp\": 1687513287,                     \"firstMeasurementTimestamp\": 1687513287                 },                 ...             ]         },         \"storage_use_7ab46e96fdb27a2694493c2c5bd7491dch8f55\": {             \"minute\": [                 {                     \"value\": 56280,                     \"timestamp\": 1687513260,                     \"lastMeasurementTimestamp\": 1687513287,                     \"firstMeasurementTimestamp\": 1687513287                 },                 ...             ]         }     } }' ``` 

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
api_instance = oneprovider_client.MiscellaneousApi(oneprovider_client.ApiClient(configuration))
body = oneprovider_client.DirSizeStatsQuery() # DirSizeStatsQuery | Query body.
id = 'id_example' # str | Directory Id 

try:
    # Get directory size statistics
    api_response = api_instance.get_directory_size_stats(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->get_directory_size_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DirSizeStatsQuery**](DirSizeStatsQuery.md)| Query body. | 
 **id** | **str**| Directory Id  | 

### Return type

[**DirSizeStatsResponse**](DirSizeStatsResponse.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_file**
> InlineResponse2011 register_file(body)

Register file

Registers a file located on an `imported storage`. This operation is available only in spaces supported with `imported storages` with `manual import mode` enabled. In such setup, the files existing on the storage are not automatically visible in the space and must be registered manually by the space users - [learn more](https://onedata.org/#/home/documentation/stable/doc/using_onedata/file-registration.html).  The operation creates the necessary metadata for the file and registers its physical location on the storage in Onedata, which makes the file visible and accessible within the space. The metadata can be provided explicitly by the registering user, or an automatic detection will be performed (although not all storage backends support the required `stat` operation or equivalent - in such case some metadata must be provided for the operation to succeed).  The registration of the same file can be repeated, which updates the previous metadata with the new information. In most cases, the metadata is overwritten with new values, with exception of xattrs - previous values are merged with new ones.  This operation requires:   * space_register_file privilege  ***Example cURL requests***  **Register file** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/data/register\" \\ -H 'Content-Type: application/json' -d \"@./file_spec.json\" ``` 

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
api_instance = oneprovider_client.MiscellaneousApi(oneprovider_client.ApiClient(configuration))
body = oneprovider_client.FileRegistrationRequest() # FileRegistrationRequest | Specification of a file to be registered.

try:
    # Register file
    api_response = api_instance.register_file(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->register_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileRegistrationRequest**](FileRegistrationRequest.md)| Specification of a file to be registered. | 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

