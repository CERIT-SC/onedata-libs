# onepanel_client.ClusterApi

All URIs are relative to */api/v3/onepanel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cluster_host**](ClusterApi.md#add_cluster_host) | **POST** /hosts | Add given host to the cluster
[**create_invite_token**](ClusterApi.md#create_invite_token) | **POST** /invite_tokens | Create node invite token
[**create_user_invite_token**](ClusterApi.md#create_user_invite_token) | **POST** /cluster/invite_user_token | Generate cluster invitation token for a user
[**get_cluster_cookie**](ClusterApi.md#get_cluster_cookie) | **GET** /cookie | Get cluster cookie
[**get_cluster_hosts**](ClusterApi.md#get_cluster_hosts) | **GET** /hosts | Get cluster hosts
[**get_cluster_members_summary**](ClusterApi.md#get_cluster_members_summary) | **GET** /cluster/members_summary | Get summary of members in this cluster
[**get_configuration**](ClusterApi.md#get_configuration) | **GET** /configuration | Get public configuration
[**get_current_cluster**](ClusterApi.md#get_current_cluster) | **GET** /cluster | Get details of this cluster
[**get_node**](ClusterApi.md#get_node) | **GET** /node | Get information about current onepanel node
[**get_progress**](ClusterApi.md#get_progress) | **GET** /progress | Get deployment progress
[**get_task_status**](ClusterApi.md#get_task_status) | **GET** /tasks/{id} | Get background task result
[**join_cluster**](ClusterApi.md#join_cluster) | **POST** /join_cluster | Join existing cluster
[**modify_progress**](ClusterApi.md#modify_progress) | **PATCH** /progress | Modify progress markers
[**remove_cluster_host**](ClusterApi.md#remove_cluster_host) | **DELETE** /hosts/{host} | Remove host from cluster

# **add_cluster_host**
> Host add_cluster_host(body)

Add given host to the cluster

Adds given host to the current cluster. The host can be specified by any address by which it is reachable. Upon success returns proper hostname used to address the new host in cluster management. 

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
api_instance = onepanel_client.ClusterApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.HostAddRequest() # HostAddRequest | 

try:
    # Add given host to the cluster
    api_response = api_instance.add_cluster_host(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->add_cluster_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostAddRequest**](HostAddRequest.md)|  | 

### Return type

[**Host**](Host.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invite_token**
> InviteToken create_invite_token()

Create node invite token

Creates node invite token. The token can be used by other nodes to [join cluster](#operation/join_cluster). 

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
api_instance = onepanel_client.ClusterApi(onepanel_client.ApiClient(configuration))

try:
    # Create node invite token
    api_response = api_instance.create_invite_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->create_invite_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InviteToken**](InviteToken.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_invite_token**
> Token create_user_invite_token()

Generate cluster invitation token for a user

Returns a token which can be used to add a Onezone user as a member of this cluster. 

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
api_instance = onepanel_client.ClusterApi(onepanel_client.ApiClient(configuration))

try:
    # Generate cluster invitation token for a user
    api_response = api_instance.create_user_invite_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->create_user_invite_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Token**](Token.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_cookie**
> str get_cluster_cookie()

Get cluster cookie

Returns cookie of a cluster this host belongs to. The cookie is a character sequence that is common for all the cluster nodes. The cookies are used for authentication between distributed Erlang Onedata processes. 

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
api_instance = onepanel_client.ClusterApi(onepanel_client.ApiClient(configuration))

try:
    # Get cluster cookie
    api_response = api_instance.get_cluster_cookie()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_cookie: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_hosts**
> list[str] get_cluster_hosts()

Get cluster hosts

Returns the list of administrative cluster hosts. 

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
api_instance = onepanel_client.ClusterApi(onepanel_client.ApiClient(configuration))

try:
    # Get cluster hosts
    api_response = api_instance.get_cluster_hosts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_hosts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_members_summary**
> ClusterMembersSummary get_cluster_members_summary()

Get summary of members in this cluster

Returns aggregated counts of users and groups belonging to this cluster. 

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
api_instance = onepanel_client.ClusterApi(onepanel_client.ApiClient(configuration))

try:
    # Get summary of members in this cluster
    api_response = api_instance.get_cluster_members_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_members_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterMembersSummary**](ClusterMembersSummary.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration**
> Configuration get_configuration()

Get public configuration

Returns public configuration details.

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
api_instance = onepanel_client.ClusterApi(onepanel_client.ApiClient(configuration))

try:
    # Get public configuration
    api_response = api_instance.get_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Configuration**](Configuration.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_cluster**
> ClusterDetails get_current_cluster()

Get details of this cluster

Returns details of this cluster. 

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
api_instance = onepanel_client.ClusterApi(onepanel_client.ApiClient(configuration))

try:
    # Get details of this cluster
    api_response = api_instance.get_current_cluster()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_current_cluster: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterDetails**](ClusterDetails.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node**
> Node get_node()

Get information about current onepanel node

Returns information about current onepanel node. 

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
api_instance = onepanel_client.ClusterApi(onepanel_client.ApiClient(configuration))

try:
    # Get information about current onepanel node
    api_response = api_instance.get_node()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_node: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Node**](Node.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_progress**
> Progress get_progress()

Get deployment progress

Returns deployment markers state.

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
api_instance = onepanel_client.ClusterApi(onepanel_client.ApiClient(configuration))

try:
    # Get deployment progress
    api_response = api_instance.get_progress()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_progress: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Progress**](Progress.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_status**
> TaskStatus get_task_status(id)

Get background task result

Returns result of an asynchronous operation, e.g. database service configuration. 

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
api_instance = onepanel_client.ClusterApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The requested task Id.

try:
    # Get background task result
    api_response = api_instance.get_task_status(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_task_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The requested task Id. | 

### Return type

[**TaskStatus**](TaskStatus.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_cluster**
> join_cluster(body)

Join existing cluster

Adds this host to administrative cluster. The host handling this request has to be newly started or removed from previous cluster. It cannot have emergency passphrase or other configuration data set. Therefore this request does not need authorization. 

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
api_instance = onepanel_client.ClusterApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.InviteToken() # InviteToken | 

try:
    # Join existing cluster
    api_instance.join_cluster(body)
except ApiException as e:
    print("Exception when calling ClusterApi->join_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InviteToken**](InviteToken.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_progress**
> modify_progress(body)

Modify progress markers

Sets or unsets markers for completed deployment stages.

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
api_instance = onepanel_client.ClusterApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.ProgressModify() # ProgressModify | 

try:
    # Modify progress markers
    api_instance.modify_progress(body)
except ApiException as e:
    print("Exception when calling ClusterApi->modify_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProgressModify**](ProgressModify.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_cluster_host**
> remove_cluster_host(host)

Remove host from cluster

Removes a node from the administrative cluster. This operation removes all user and configuration data from the host. 

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
api_instance = onepanel_client.ClusterApi(onepanel_client.ApiClient(configuration))
host = 'host_example' # str | Hostname of a node to be removed from the cluster.

try:
    # Remove host from cluster
    api_instance.remove_cluster_host(host)
except ApiException as e:
    print("Exception when calling ClusterApi->remove_cluster_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| Hostname of a node to be removed from the cluster. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

