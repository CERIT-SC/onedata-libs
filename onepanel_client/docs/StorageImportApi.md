# onepanel_client.StorageImportApi

All URIs are relative to */api/v3/onepanel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**force_start_auto_storage_import_scan**](StorageImportApi.md#force_start_auto_storage_import_scan) | **POST** /provider/spaces/{id}/storage-import/auto/force-start | Force start auto storage import scan
[**force_stop_auto_storage_import_scan**](StorageImportApi.md#force_stop_auto_storage_import_scan) | **POST** /provider/spaces/{id}/storage-import/auto/force-stop | Force stop auto storage import scan
[**get_auto_storage_import_info**](StorageImportApi.md#get_auto_storage_import_info) | **GET** /provider/spaces/{id}/storage-import/auto/info | Get information about auto storage import scan
[**get_auto_storage_import_stats**](StorageImportApi.md#get_auto_storage_import_stats) | **GET** /provider/spaces/{id}/storage-import/auto/stats | Get statistics of auto storage import mechanism
[**get_manual_storage_import_example**](StorageImportApi.md#get_manual_storage_import_example) | **GET** /provider/spaces/{id}/storage-import/manual/example | Get manual storage import example

# **force_start_auto_storage_import_scan**
> force_start_auto_storage_import_scan(id)

Force start auto storage import scan

Forcefully starts scan of auto storage import mechanism in given space.

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
api_instance = onepanel_client.StorageImportApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a space.

try:
    # Force start auto storage import scan
    api_instance.force_start_auto_storage_import_scan(id)
except ApiException as e:
    print("Exception when calling StorageImportApi->force_start_auto_storage_import_scan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a space. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **force_stop_auto_storage_import_scan**
> force_stop_auto_storage_import_scan(id)

Force stop auto storage import scan

Forcefully stops current scan of auto storage import mechanism in given space.

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
api_instance = onepanel_client.StorageImportApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a space.

try:
    # Force stop auto storage import scan
    api_instance.force_stop_auto_storage_import_scan(id)
except ApiException as e:
    print("Exception when calling StorageImportApi->force_stop_auto_storage_import_scan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a space. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_storage_import_info**
> AutoStorageImportInfo get_auto_storage_import_info(id)

Get information about auto storage import scan

Returns information about current or last finished auto storage import scan.

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
api_instance = onepanel_client.StorageImportApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a space for which storage import stats should be returned.

try:
    # Get information about auto storage import scan
    api_response = api_instance.get_auto_storage_import_info(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageImportApi->get_auto_storage_import_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a space for which storage import stats should be returned. | 

### Return type

[**AutoStorageImportInfo**](AutoStorageImportInfo.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_storage_import_stats**
> AutoStorageImportStats get_auto_storage_import_stats(id, period, metrics)

Get statistics of auto storage import mechanism

Returns requested statistics of auto storage import mechanism for given space on this provider. 

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
api_instance = onepanel_client.StorageImportApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a space for which storage import stats should be returned.
period = 'period_example' # str | Predefined time period for which the statistics should be fetched.
metrics = 'metrics_example' # str | Specify which statistic metrics should be returned - strings delimited with comma. Accepted values are: `queueLength`, `createdFiles`, `modifiedFiles`, `deletedFiles` 

try:
    # Get statistics of auto storage import mechanism
    api_response = api_instance.get_auto_storage_import_stats(id, period, metrics)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageImportApi->get_auto_storage_import_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a space for which storage import stats should be returned. | 
 **period** | **str**| Predefined time period for which the statistics should be fetched. | 
 **metrics** | **str**| Specify which statistic metrics should be returned - strings delimited with comma. Accepted values are: &#x60;queueLength&#x60;, &#x60;createdFiles&#x60;, &#x60;modifiedFiles&#x60;, &#x60;deletedFiles&#x60;  | 

### Return type

[**AutoStorageImportStats**](AutoStorageImportStats.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manual_storage_import_example**
> ManualStorageImportExample get_manual_storage_import_example(id)

Get manual storage import example

Returns example `curl` command that can be executed to manually import (register) file from storage.  The command is filled with correct host of the Oneprovider, space and storage ids. In order to execute the command, user must set 3 variables:  * `TOKEN` - Onedata access token.  * `STORAGE_FILE_ID` - Identifier of the file on storage, relevant for given storage backend:    * path on POSIX-compatible or canonical object storages, e.g. /dir/file.txt,    * URL on HTTP based storages, e.g. https://www.example.org/data/21/run123.tar.  * `DESTINATION_PATH` - An absolute path in space where file should be created.  For more info please read: https://onedata.org/#/home/api/stable/oneprovider?anchor=tag/File-registration 

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
api_instance = onepanel_client.StorageImportApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a space for which the example command should be generated.

try:
    # Get manual storage import example
    api_response = api_instance.get_manual_storage_import_example(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageImportApi->get_manual_storage_import_example: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a space for which the example command should be generated. | 

### Return type

[**ManualStorageImportExample**](ManualStorageImportExample.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

