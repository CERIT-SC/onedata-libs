# oneprovider_client.TransferApi

All URIs are relative to */api/v3/oneprovider*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_transfer**](TransferApi.md#cancel_transfer) | **DELETE** /transfers/{tid} | Cancel specific transfer
[**create_transfer**](TransferApi.md#create_transfer) | **POST** /transfers | Create transfer
[**get_all_transfers**](TransferApi.md#get_all_transfers) | **GET** /spaces/{sid}/transfers | Get all space transfers
[**get_transfer_status**](TransferApi.md#get_transfer_status) | **GET** /transfers/{tid} | Get transfer status
[**rerun_transfer**](TransferApi.md#rerun_transfer) | **POST** /transfers/{tid}/rerun | Rerun ended transfer

# **cancel_transfer**
> cancel_transfer(tid)

Cancel specific transfer

Cancels a scheduled or active transfer. Returns 400 in case the transfer is already completed, canceled or failed.  This operation requires `space_cancel_replication` privilege in case of canceling replication, `space_cancel_eviction` privilege in case of canceling eviction and both of them when canceling migration.  However, canceling your own transfers does not require any privileges.  ***Example cURL requests***  **Cancel specific transfer** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/transfers/$TRANSFER_ID\" ``` 

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
api_instance = oneprovider_client.TransferApi(oneprovider_client.ApiClient(configuration))
tid = 'tid_example' # str | Transfer Id.

try:
    # Cancel specific transfer
    api_instance.cancel_transfer(tid)
except ApiException as e:
    print("Exception when calling TransferApi->cancel_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tid** | **str**| Transfer Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_transfer**
> InlineResponse2012 create_transfer(body)

Create transfer

Creates transfer, which is a process of data movement between providers. This operation is asynchronous and it can take a long time depending on the size of the data to move.  The following types of transfer are supported: - `replication` - process of copying data to achieve a complete replica in provider   specified as `replicatingProviderId`. The data will be copied   from one or more providers in the space that hold replicas   or some fragments. This operation requires   `space_schedule_replication` privilege. - `eviction` - process of removing replica(s) from provider specified in `evictingProviderId`.   Eviction is safe - will succeed only if there is at least one   complete replica (accumulated) on other providers in the space.   This operation requires `space_schedule_eviction` privilege. - `migration` - `replication` followed by `eviction`. This operation requires both   `space_schedule_replication` and `space_schedule_eviction` privileges.  Each transfer applies to one or more files/directories, depending on chosen `dataSourceType`:   - file - a single chosen file or directory   - view - all files that are returned as a result of querying chosen view  In case of a directory, the transfer applies to all its subfiles and subdirectories (recursively).  ***Example cURL requests***  **Create file replication** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/transfers\" \\ -H \"Content-Type: application/json\" -d '{     \"type\": \"replication\",     \"replicatingProviderId\": \"'$PROVIDER_ID'\",     \"dataSourceType\": \"file\",     \"fileId\": \"'$FILE_ID'\" }' ``` 

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
api_instance = oneprovider_client.TransferApi(oneprovider_client.ApiClient(configuration))
body = oneprovider_client.TransferCreateRequest() # TransferCreateRequest | Transfer properties.

try:
    # Create transfer
    api_response = api_instance.create_transfer(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferApi->create_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransferCreateRequest**](TransferCreateRequest.md)| Transfer properties. | 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_transfers**
> InlineResponse2002 get_all_transfers(sid, state=state, limit=limit, page_token=page_token)

Get all space transfers

Returns the list of all transfer IDs in a space with given state. The list is broken down into pages, each with length less or equal to the limit parameter. If the nextPageToken in the response has non-null value, there are more transfers to list - provide the token in the page_token parameter in the following request.  This operation requires `space_view_transfers` privilege.  ***Example cURL requests***  **List at most 3 ongoing transfers starting from page id 757136151113c2f** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/transfers?state=ongoing&limit=3&page_token=757136151113c2f\"  {     \"transfers\": [         \"2727a9fe5f5df6b43a8033386d2990e8ch5df6\",         \"4bd9b58f6387622bf07f7388945e4fc4ch8762\",         \"579a785181331e618b26980166b6ba2fch331e\"     ],     \"nextPageToken\": \"8471726779817b3a\" } ``` 

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
api_instance = oneprovider_client.TransferApi(oneprovider_client.ApiClient(configuration))
sid = 'sid_example' # str | Space Id in which to list transfers. 
state = 'state_example' # str | Specifies the state of transfers to list. The default is \"ongoing\".  (optional)
limit = 100 # int | Allows to limit the number of returned transfers.  (optional) (default to 100)
page_token = 'page_token_example' # str | Allows to start the listing from a certain point, identified by the page token.  (optional)

try:
    # Get all space transfers
    api_response = api_instance.get_all_transfers(sid, state=state, limit=limit, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferApi->get_all_transfers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Space Id in which to list transfers.  | 
 **state** | **str**| Specifies the state of transfers to list. The default is \&quot;ongoing\&quot;.  | [optional] 
 **limit** | **int**| Allows to limit the number of returned transfers.  | [optional] [default to 100]
 **page_token** | **str**| Allows to start the listing from a certain point, identified by the page token.  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transfer_status**
> TransferStatus get_transfer_status(tid)

Get transfer status

Returns status of specific transfer.  This operation requires `space_view_transfers` privilege.  ***Example cURL requests***  **Get status of specific transfer** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/transfers/$TRANSFER_ID\"  {     \"type\": \"replication\",     \"userId\": \"admin\",     \"rerunId\": null,     \"effectiveJobTransferId\": $TRANSFER_ID,     \"spaceId\": \"6ec1a5413b6f4e2b01a5c85a8fd797e2\",     \"dataSourceType\": \"file\",     \"fileId\": \"00000000005CF4706775696423745F772D67686431633765446F4D76546D6F2D67575F3361737A7670486B477A7936587734507265584A7723394A4F355F5F396E4C31623031594576776E667431723230677767776C6B497031394E445F6E3868677873\",     \"filePath\": \"/space/tmp\",     \"transferStatus\": \"completed\",     \"effectiveJobStatus\": \"completed\",     \"replicationStatus\": \"completed\",     \"evictionStatus\": \"skipped\",     \"replicatingProviderId\": \"HICATChd8wzbFmB6qfGby9VN7MfdXgI1qC4pULGVm8Q\",     \"evictingProviderId\": null,     \"callback\": null,     \"filesToProcess\": 1,     \"filesProcessed\": 1,     \"filesReplicated\": 1,     \"filesEvicted\": 0,     \"filesFailed\": 0,     \"bytesReplicated\": 10485760000,     \"scheduleTime\": 1504688800,     \"startTime\": 15046888765,     \"finishTime\": 1504688814,     \"lastUpdate\": 1504988814,     \"minHist\": {         \"ASDxicvuisodr78w979879wer\": [419430400, 1153433600, 1258291200, 1468006400, 1048576000, 1048576000, 1048576000, 1153433600, 629145600, 1258291200, 0, 0, 0, 0, 0, 0, 0, 0, 0]     },     \"hrHist\": {         \"ASDxicvuisodr78w979879wer\": [10485760000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     },     \"dyHist\": {         \"ASDxicvuisodr78w979879wer\": [10485760000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     },     \"mthHist\": {         \"ASDxicvuisodr78w979879wer\": [10485760000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     } } ``` 

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
api_instance = oneprovider_client.TransferApi(oneprovider_client.ApiClient(configuration))
tid = 'tid_example' # str | Transfer Id.

try:
    # Get transfer status
    api_response = api_instance.get_transfer_status(tid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferApi->get_transfer_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tid** | **str**| Transfer Id. | 

### Return type

[**TransferStatus**](TransferStatus.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rerun_transfer**
> InlineResponse2013 rerun_transfer(tid)

Rerun ended transfer

Reruns ended transfer by creating a new, identical transfer.  This operation requires:   * `space_schedule_replication` when rerunning replication   * `space_schedule_eviction` when rerunning eviction   * `space_schedule_replication` and `space_schedule_eviction` when rerunning migration  Additionally, rerunning transfers using views requires `space_query_views` privilege.  ***Example cURL requests***  **Rerun finished transfer** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/transfers/$TRANSFER_ID/rerun\" ``` 

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
api_instance = oneprovider_client.TransferApi(oneprovider_client.ApiClient(configuration))
tid = 'tid_example' # str | Transfer Id.

try:
    # Rerun ended transfer
    api_response = api_instance.rerun_transfer(tid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferApi->rerun_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tid** | **str**| Transfer Id. | 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

