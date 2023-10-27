# onepanel_client.CurrentUserApi

All URIs are relative to */api/v3/onepanel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cluster**](CurrentUserApi.md#get_cluster) | **GET** /user/clusters/{id} | Get details of a user&#x27;s cluster
[**get_clusters**](CurrentUserApi.md#get_clusters) | **GET** /user/clusters | List user&#x27;s clusters
[**get_current_user**](CurrentUserApi.md#get_current_user) | **GET** /user | Get details of authenticated user

# **get_cluster**
> ClusterDetails get_cluster(id)

Get details of a user's cluster

Returns details of the specified cluster. 

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
api_instance = onepanel_client.CurrentUserApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id which details should be returned.

try:
    # Get details of a user's cluster
    api_response = api_instance.get_cluster(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrentUserApi->get_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id which details should be returned. | 

### Return type

[**ClusterDetails**](ClusterDetails.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusters**
> Ids get_clusters()

List user's clusters

Lists clusters to which current user belongs. 

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
api_instance = onepanel_client.CurrentUserApi(onepanel_client.ApiClient(configuration))

try:
    # List user's clusters
    api_response = api_instance.get_clusters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrentUserApi->get_clusters: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Ids**](Ids.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user**
> CurrentUser get_current_user()

Get details of authenticated user

Returns the details of the user performing the query. 

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
api_instance = onepanel_client.CurrentUserApi(onepanel_client.ApiClient(configuration))

try:
    # Get details of authenticated user
    api_response = api_instance.get_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrentUserApi->get_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrentUser**](CurrentUser.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

