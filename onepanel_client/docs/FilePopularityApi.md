# onepanel_client.FilePopularityApi

All URIs are relative to */api/v3/onepanel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_file_popularity**](FilePopularityApi.md#configure_file_popularity) | **PATCH** /provider/spaces/{id}/file-popularity/configuration | Configure file popularity mechanism in the space
[**get_file_popularity_configuration**](FilePopularityApi.md#get_file_popularity_configuration) | **GET** /provider/spaces/{id}/file-popularity/configuration | Get file popularity configuration

# **configure_file_popularity**
> TaskId configure_file_popularity(body, id)

Configure file popularity mechanism in the space

Configures the file popularity mechanism in the space. The mechanism is responsible for collecting file popularity usage statistics per space support. Creates a view which can be queried to fetch the least popular files. The view is sorted in an increasing order by the popularity function value. The popularity function is defined as  ``` P(lastOpenHour, avgOpenCountPerDay) = w1 * lastOpenHour + w2 * min(avgOpenCountPerDay, MAX_AVG_OPEN_COUNT_PER_DAY) where: * lastOpenHour - parameter which is equal to timestamp (in hours since 01.01.1970) of last open operation on given file * w1 - weight of lastOpenHour parameter * avgOpenCountPerDay - parameter equal to moving average of number of open operations on given file per day. Value is calculated over last 30 days. * w2 - weight of avgOpenCountPerDay parameter * MAX_AVG_OPEN_COUNT_PER_DAY - upper boundary for avgOpenCountPerDay parameter ``` 

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
api_instance = onepanel_client.FilePopularityApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.SpaceFilePopularityConfiguration() # SpaceFilePopularityConfiguration | Configuration of the file-popularity mechanism in the space.
id = 'id_example' # str | The Id of a space.

try:
    # Configure file popularity mechanism in the space
    api_response = api_instance.configure_file_popularity(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilePopularityApi->configure_file_popularity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpaceFilePopularityConfiguration**](SpaceFilePopularityConfiguration.md)| Configuration of the file-popularity mechanism in the space. | 
 **id** | **str**| The Id of a space. | 

### Return type

[**TaskId**](TaskId.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_popularity_configuration**
> SpaceFilePopularityConfiguration get_file_popularity_configuration(id)

Get file popularity configuration

Returns configuration of file popularity mechanism in the space specified by space Id in the path. 

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
api_instance = onepanel_client.FilePopularityApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a space of which file-popularity configuration should be returned.

try:
    # Get file popularity configuration
    api_response = api_instance.get_file_popularity_configuration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilePopularityApi->get_file_popularity_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a space of which file-popularity configuration should be returned. | 

### Return type

[**SpaceFilePopularityConfiguration**](SpaceFilePopularityConfiguration.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

