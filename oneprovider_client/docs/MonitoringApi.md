# oneprovider_client.MonitoringApi

All URIs are relative to */api/v3/oneprovider*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_space_changes**](MonitoringApi.md#get_space_changes) | **POST** /changes/metadata/{sid} | Subscribe to file events

# **get_space_changes**
> MetadataChangesEvent get_space_changes(body, sid, timeout=timeout, last_seq=last_seq)

Subscribe to file events

This method subscribes through HTTP streaming on events of specific type for a given space.  Until the connection is kept alive, the events will be streamed to subscribers as soon as they are occur. The optional `timeout` parameter can be used to automatically disconnect  when no events occur in a given time window.  This operation requires `space_view_changes_stream` privilege.  ***Example cURL requests***  **Listen to space change events** ```bash curl -N -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/changes/metadata/$SPACE_ID\" \\ -H \"Content-Type: application/json\" -d \"@./changes_req.json\" ``` 

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
api_instance = oneprovider_client.MonitoringApi(oneprovider_client.ApiClient(configuration))
body = oneprovider_client.MetadataChangesStreamRequest() # MetadataChangesStreamRequest | Specification of metadata changes to observe.
sid = 'sid_example' # str | Space Id.
timeout = 56 # int | Optional timeout in milliseconds, which allows to automatically break connection when no event occured in specified time. By default the timeout is unlimited.  (optional)
last_seq = 56 # int | Last known file metadata sequence number  (optional)

try:
    # Subscribe to file events
    api_response = api_instance.get_space_changes(body, sid, timeout=timeout, last_seq=last_seq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringApi->get_space_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataChangesStreamRequest**](MetadataChangesStreamRequest.md)| Specification of metadata changes to observe. | 
 **sid** | **str**| Space Id. | 
 **timeout** | **int**| Optional timeout in milliseconds, which allows to automatically break connection when no event occured in specified time. By default the timeout is unlimited.  | [optional] 
 **last_seq** | **int**| Last known file metadata sequence number  | [optional] 

### Return type

[**MetadataChangesEvent**](MetadataChangesEvent.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

