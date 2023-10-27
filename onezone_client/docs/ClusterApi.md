# onezone_client.ClusterApi

All URIs are relative to */api/v3/onezone*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cluster_user**](ClusterApi.md#add_cluster_user) | **PUT** /clusters/{id}/users/{uid} | Add user to cluster
[**add_group_to_cluster**](ClusterApi.md#add_group_to_cluster) | **PUT** /clusters/{id}/groups/{gid} | Add group to cluster
[**create_cluster_group**](ClusterApi.md#create_cluster_group) | **POST** /clusters/{id}/groups | Create group in cluster
[**create_cluster_group_invite_token**](ClusterApi.md#create_cluster_group_invite_token) | **POST** /clusters/{id}/groups/token | Create cluster invite token for group
[**create_cluster_user_invite_token**](ClusterApi.md#create_cluster_user_invite_token) | **POST** /clusters/{id}/users/token | Create cluster user invite token
[**get_cluster**](ClusterApi.md#get_cluster) | **GET** /clusters/{id} | Get cluster details
[**get_cluster_effective_group**](ClusterApi.md#get_cluster_effective_group) | **GET** /clusters/{id}/effective_groups/{gid} | Get cluster&#x27;s effective group details
[**get_cluster_effective_user**](ClusterApi.md#get_cluster_effective_user) | **GET** /clusters/{id}/effective_users/{uid} | Get cluster&#x27;s effective user details
[**get_cluster_group**](ClusterApi.md#get_cluster_group) | **GET** /clusters/{id}/groups/{gid} | Get cluster group details
[**get_cluster_user**](ClusterApi.md#get_cluster_user) | **GET** /clusters/{id}/users/{uid} | Get cluster&#x27;s user details
[**get_effective_group_cluster_membership_intermediaries**](ClusterApi.md#get_effective_group_cluster_membership_intermediaries) | **GET** /clusters/{id}/effective_groups/{gid}/membership | Get effective group&#x27;s cluster membership intermediaries
[**get_effective_user_cluster_membership_intermediaries**](ClusterApi.md#get_effective_user_cluster_membership_intermediaries) | **GET** /clusters/{id}/effective_users/{uid}/membership | Get effective user&#x27;s cluster membership intermediaries
[**list_cluster_effective_groups**](ClusterApi.md#list_cluster_effective_groups) | **GET** /clusters/{id}/effective_groups | List cluster&#x27;s effective groups
[**list_cluster_effective_users**](ClusterApi.md#list_cluster_effective_users) | **GET** /clusters/{id}/effective_users | List cluster&#x27;s effective users
[**list_cluster_groups**](ClusterApi.md#list_cluster_groups) | **GET** /clusters/{id}/groups | List cluster&#x27;s groups
[**list_cluster_privileges**](ClusterApi.md#list_cluster_privileges) | **GET** /clusters/privileges | List all cluster privileges
[**list_cluster_users**](ClusterApi.md#list_cluster_users) | **GET** /clusters/{id}/users | List cluster&#x27;s users
[**list_effective_group_cluster_privileges**](ClusterApi.md#list_effective_group_cluster_privileges) | **GET** /clusters/{id}/effective_groups/{gid}/privileges | List effective group&#x27;s cluster privileges
[**list_effective_user_cluster_privileges**](ClusterApi.md#list_effective_user_cluster_privileges) | **GET** /clusters/{id}/effective_users/{uid}/privileges | List effective user&#x27;s cluster privileges
[**list_group_cluster_privileges**](ClusterApi.md#list_group_cluster_privileges) | **GET** /clusters/{id}/groups/{gid}/privileges | List group&#x27;s cluster privileges
[**list_user_cluster_privileges**](ClusterApi.md#list_user_cluster_privileges) | **GET** /clusters/{id}/users/{uid}/privileges | List user&#x27;s cluster privileges
[**modify_cluster**](ClusterApi.md#modify_cluster) | **PATCH** /clusters/{id} | Modify cluster details
[**oz_clusters_list**](ClusterApi.md#oz_clusters_list) | **GET** /clusters | List all clusters
[**remove_cluster_group**](ClusterApi.md#remove_cluster_group) | **DELETE** /clusters/{id}/groups/{gid} | Remove group from cluster
[**remove_cluster_user**](ClusterApi.md#remove_cluster_user) | **DELETE** /clusters/{id}/users/{uid} | Remove user from cluster
[**update_group_cluster_privileges**](ClusterApi.md#update_group_cluster_privileges) | **PATCH** /clusters/{id}/groups/{gid}/privileges | Update group&#x27;s privileges in a cluster
[**update_user_cluster_privileges**](ClusterApi.md#update_user_cluster_privileges) | **PATCH** /clusters/{id}/users/{uid}/privileges | Update user&#x27;s cluster privileges

# **add_cluster_user**
> add_cluster_user(id, uid, body=body)

Add user to cluster

Adds user {uid} as member of cluster {id}. Optionally, privileges can be passed in the request body, otherwise default privileges will be set for the user in this cluster.  This operation can only be invoked by the user {uid} to add himself to the cluster (if he is not a member already) and requires `cluster_add_user` privilege in the cluster. If `privileges` are specified in the request, `cluster_set_privileges` privilege is also required.  Administrators having the `oz_clusters_add_relationships` and `oz_users_add_relationships` admin privileges can add any user to any cluster, though `oz_clusters_set_privileges` privilege is required if `privileges` are specified in the request.  ***Example cURL requests***  **Add user to cluster** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/users/$USER_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
uid = 'uid_example' # str | User Id.
body = onezone_client.UsersUidBody5() # UsersUidBody5 |  (optional)

try:
    # Add user to cluster
    api_instance.add_cluster_user(id, uid, body=body)
except ApiException as e:
    print("Exception when calling ClusterApi->add_cluster_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id. | 
 **uid** | **str**| User Id. | 
 **body** | [**UsersUidBody5**](UsersUidBody5.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_group_to_cluster**
> add_group_to_cluster(id, gid, body=body)

Add group to cluster

Adds group {gid} as member of cluster {id}. Optionally, privileges can be passed in the request body, otherwise default privileges will be set for the group in this cluster.  This operation requires `cluster_add_group` privilege in the cluster and `group_add_cluster` privilege in the group. If `privileges` are specified in the request, `cluster_set_privileges` privilege is also required.  For administrator who does not belong to the group / cluster, `oz_groups_add_relationships` and `oz_clusters_add_relationships` privileges are required, and `oz_clusters_set_privileges` if `privileges` are specified in the request.  ***Example cURL requests***  **Add group to cluster** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\  https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups/$GROUP_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
gid = 'gid_example' # str | Group Id.
body = onezone_client.GroupsGidBody4() # GroupsGidBody4 |  (optional)

try:
    # Add group to cluster
    api_instance.add_group_to_cluster(id, gid, body=body)
except ApiException as e:
    print("Exception when calling ClusterApi->add_group_to_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id. | 
 **gid** | **str**| Group Id. | 
 **body** | [**GroupsGidBody4**](GroupsGidBody4.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_group**
> create_cluster_group(body, id)

Create group in cluster

Creates a new group belonging to the cluster of {id}.  This operation requires `cluster_add_group` privilege. For administrator who does not belong to this group `oz_clusters_add_relationships` and `oz_groups_create` privileges are required.  ***Example cURL requests***  **Create group in cluster** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
body = onezone_client.GroupCreateRequest() # GroupCreateRequest | Group properties.
id = 'id_example' # str | Cluster Id.

try:
    # Create group in cluster
    api_instance.create_cluster_group(body, id)
except ApiException as e:
    print("Exception when calling ClusterApi->create_cluster_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupCreateRequest**](GroupCreateRequest.md)| Group properties. | 
 **id** | **str**| Cluster Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_group_invite_token**
> ClusterInviteToken create_cluster_group_invite_token(id)

Create cluster invite token for group

This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token allowing to add a group to a specific cluster.  This operation requires `cluster_add_group` privilege or `oz_clusters_add_relationships` admin privilege.  ***Example cURL requests***  **Create cluster invitation token for group** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups/token  {   \"token\": \"MDAxNmxvY0cGUgKWsjcpnrLE00RtOd2F00cGUgKWsjcpnrLE00RtOdhmnQycSICwMsugo\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.

try:
    # Create cluster invite token for group
    api_response = api_instance.create_cluster_group_invite_token(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->create_cluster_group_invite_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id. | 

### Return type

[**ClusterInviteToken**](ClusterInviteToken.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_user_invite_token**
> ClusterInviteToken create_cluster_user_invite_token(id)

Create cluster user invite token

This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token allowing new user to join a cluster.  This operation requires `cluster_add_user` privilege. For administrators who do not have to be members of this cluster, `oz_clusters_add_relationships` privilege is required.  ***Example cURL requests***  **Create cluster user invite token** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/users/token  {   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaWVyIG00zcEJ2UDVuOHhkQUNhdk9hbTlyNnIwNldPSzVhc\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.

try:
    # Create cluster user invite token
    api_response = api_instance.create_cluster_user_invite_token(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->create_cluster_user_invite_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id. | 

### Return type

[**ClusterInviteToken**](ClusterInviteToken.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster**
> Cluster get_cluster(id)

Get cluster details

Returns the details about a specific cluster.  This operation requires membership in the cluster or `oz_clusters_view` admin privilege.  ***Example cURL requests***  **Get cluster details** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID  {   \"clusterId\": \"f8d843beda24e54545455ecc0f4b8886\",   \"type\": \"oneprovider\",   \"workerVersion\": {     \"release\": \"21.02.3\",     \"build\": \"1-gfabf02d\",     \"gui\": \"129c549fbe9b3e730c3d9910492228566e39e1236945766a74381405cc57fb04\"   },   \"onepanelVersion\": {     \"release\": \"21.02.3\",     \"build\": \"3-89fc6bad\",     \"gui\": \"68e7e1472adb719ddf2d88908775091dfb10e5d0b916f06125ea1af4056044e3\"   },   \"online\": true,   \"onepanelProxy\": false,   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.

try:
    # Get cluster details
    api_response = api_instance.get_cluster(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_effective_group**
> Group get_cluster_effective_group(id, gid)

Get cluster's effective group details

Returns details about a specific effective group in a cluster.  This operation requires `cluster_view` privilege or `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get effective cluster group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_groups/$GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_groupX\",   \"type\": \"team\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
gid = 'gid_example' # str | Group Id.

try:
    # Get cluster's effective group details
    api_response = api_instance.get_cluster_effective_group(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_effective_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id. | 
 **gid** | **str**| Group Id. | 

### Return type

[**Group**](Group.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_effective_user**
> User get_cluster_effective_user(id, uid)

Get cluster's effective user details

Returns details about a specific effective user in a cluster.  This operation requires `cluster_view` privilege or `oz_users_view` admin privilege.  ***Example cURL requests***  **Get effective cluster user details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_users/$USER_ID  {   \"userId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"fullName\" : \"John Doe\",   \"username\" : \"jodoe\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
uid = 'uid_example' # str | User Id.

try:
    # Get cluster's effective user details
    api_response = api_instance.get_cluster_effective_user(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_effective_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**User**](User.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_group**
> Group get_cluster_group(id, gid)

Get cluster group details

Returns details about a specific group in a cluster.  This operation requires `cluster_view` privilege. For administrators who do not have to be members of this cluster, `oz_groups_view` privilege is required.  ***Example cURL requests***  **Get cluster group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups/$GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_groupX\",   \"type\": \"team\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
gid = 'gid_example' # str | Group Id.

try:
    # Get cluster group details
    api_response = api_instance.get_cluster_group(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id. | 
 **gid** | **str**| Group Id. | 

### Return type

[**Group**](Group.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_user**
> User get_cluster_user(id, uid)

Get cluster's user details

Returns basic information about a specific user in a cluster.  This operation requires `cluster_view` privilege. For administrators who do not have to be members of this cluster, `oz_users_view` privilege is required.  ***Example cURL requests***  **Get cluster user data** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
uid = 'uid_example' # str | User Id.

try:
    # Get cluster's user details
    api_response = api_instance.get_cluster_user(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**User**](User.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_group_cluster_membership_intermediaries**
> MembershipIntermediaries get_effective_group_cluster_membership_intermediaries(id, gid)

Get effective group's cluster membership intermediaries

Returns the effective group's (`{gid}`) cluster membership intermediaries - entities from which the group inherits membership in the cluster (`{id}`). Special keyword `\"self\"` in entity id indicates that the group (`{gid}`) has a direct membership in the cluster (`{id}`).  This operation requires any of the following authentication: * as user who is an effective member of the group (`{gid}`), * as user who has `cluster_view` privilege in the cluster (`{id}`), * as user who has `oz_clusters_view` admin privilege.  ***Example cURL requests***  **Get effective group's cluster membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_groups/$GROUP_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"cluster\", \"id\": \"self\"}   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
gid = 'gid_example' # str | Group Id.

try:
    # Get effective group's cluster membership intermediaries
    api_response = api_instance.get_effective_group_cluster_membership_intermediaries(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_effective_group_cluster_membership_intermediaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id. | 
 **gid** | **str**| Group Id. | 

### Return type

[**MembershipIntermediaries**](MembershipIntermediaries.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_user_cluster_membership_intermediaries**
> MembershipIntermediaries get_effective_user_cluster_membership_intermediaries(id, uid)

Get effective user's cluster membership intermediaries

Returns the effective user's (`{uid}`) cluster membership intermediaries - entities from which the user inherits membership in the cluster (`{id}`). Special keyword `\"self\"` in entity id indicates that the user (`{uid}`) has a direct membership in the cluster (`{id}`).  This operation requires any of the following authentication: * as user (`{uid}`) who is an effective member of the cluster (`{id}`), * as user who has `cluster_view` privilege in the cluster (`{id}`), * as user who has `oz_clusters_view` admin privilege.  ***Example cURL requests***  **Get effective user's cluster membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_users/$USER_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"cluster\", \"id\": \"self\"}   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
uid = 'uid_example' # str | User Id.

try:
    # Get effective user's cluster membership intermediaries
    api_response = api_instance.get_effective_user_cluster_membership_intermediaries(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_effective_user_cluster_membership_intermediaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**MembershipIntermediaries**](MembershipIntermediaries.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_effective_groups**
> Groups list_cluster_effective_groups(id)

List cluster's effective groups

Returns the list of effective groups belonging to a specific cluster.  This operation requires `cluster_view` privilege or `oz_clusters_list_relationships` admin privilege.  ***Example cURL requests***  **Get cluster effective groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_groups  {   \"groups\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.

try:
    # List cluster's effective groups
    api_response = api_instance.list_cluster_effective_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_cluster_effective_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id. | 

### Return type

[**Groups**](Groups.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_effective_users**
> Users list_cluster_effective_users(id)

List cluster's effective users

Returns the list of effective users belonging to a specific cluster.  This operation requires `cluster_view` privilege or `oz_clusters_list_relationships` admin privilege.  ***Example cURL requests***  **Get cluster effective users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_users  {   \"users\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.

try:
    # List cluster's effective users
    api_response = api_instance.list_cluster_effective_users(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_cluster_effective_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id. | 

### Return type

[**Users**](Users.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_groups**
> Groups list_cluster_groups(id)

List cluster's groups

Returns the list of groups belonging to a specific cluster.  This operation requires `cluster_view` privilege. For administrator who does not belong to this cluster `oz_clusters_list_relationships` privilege is required.  ***Example cURL requests***  **Get cluster groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups  {   \"groups\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.

try:
    # List cluster's groups
    api_response = api_instance.list_cluster_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_cluster_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id. | 

### Return type

[**Groups**](Groups.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_privileges**
> InlineResponse20019 list_cluster_privileges()

List all cluster privileges

Returns list of all possible cluster privileges.  This endpoint does not require authentication.  ***Example cURL requests***  **Get list of all cluster privileges** ```bash curl https://$ZONE_HOST/api/v3/onezone/clusters/privileges  {   \"admin\": [     \"cluster_view\",     \"cluster_update\",     \"cluster_delete\",     \"cluster_view_privileges\",     \"cluster_set_privileges\",     \"cluster_add_user\",     \"cluster_remove_user\",     \"cluster_add_group\",     \"cluster_remove_group\"   ],   \"manager\": [     \"cluster_view\",     \"cluster_add_user\",     \"cluster_remove_user\",     \"cluster_add_group\",     \"cluster_remove_group\"   ],   \"member\": [     \"cluster_view\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))

try:
    # List all cluster privileges
    api_response = api_instance.list_cluster_privileges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_cluster_privileges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_users**
> Users list_cluster_users(id)

List cluster's users

Returns the list of users belonging to a specific cluster.  This operation requires `cluster_view` privilege. For administrators who do not have to be members of this cluster, `oz_clusters_list_relationships` privilege is required.  ***Example cURL requests***  **Get cluster users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/users  {   \"users\": [     \"a5b469a2b0516b662a49da74d6d7d7bc\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.

try:
    # List cluster's users
    api_response = api_instance.list_cluster_users(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_cluster_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id. | 

### Return type

[**Users**](Users.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_group_cluster_privileges**
> InlineResponse20020 list_effective_group_cluster_privileges(id, gid)

List effective group's cluster privileges

Returns the list of effective group's (`{gid}`) privileges in a cluster (`{id}`).  Effective privileges are a sum of group's privileges and privileges inherited from its parent group memberships.  This operation requires `cluster_view_privileges` privilege or `oz_clusters_view_privileges` admin privilege.  ***Example cURL requests***  **List effective groups's privileges in a cluster** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_groups/$GROUP_ID/privileges  {   \"privileges\": [     \"cluster_view\",     \"cluster_update\",     \"cluster_delete\",     \"cluster_view_privileges\",     \"cluster_set_privileges\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
gid = 'gid_example' # str | Group Id.

try:
    # List effective group's cluster privileges
    api_response = api_instance.list_effective_group_cluster_privileges(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_effective_group_cluster_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id. | 
 **gid** | **str**| Group Id. | 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_user_cluster_privileges**
> InlineResponse20020 list_effective_user_cluster_privileges(id, uid)

List effective user's cluster privileges

Returns the list of effective user's (`{uid}`) privileges in a cluster (`{id}`).  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation requires `cluster_view_privileges` privilege or `oz_clusters_view_privileges` admin privilege.  ***Example cURL requests***  **List effective user's privileges in a cluster** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_users/$USER_ID/privileges  {   \"privileges\": [     \"cluster_view\",     \"cluster_update\",     \"cluster_delete\",     \"cluster_view_privileges\",     \"cluster_set_privileges\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
uid = 'uid_example' # str | User Id.

try:
    # List effective user's cluster privileges
    api_response = api_instance.list_effective_user_cluster_privileges(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_effective_user_cluster_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_cluster_privileges**
> InlineResponse20020 list_group_cluster_privileges(id, gid)

List group's cluster privileges

Returns the list of group's (`{gid}`) privileges in a cluster (`{id}`).  This operation requires `cluster_view_privileges` privilege or `oz_clusters_view_privileges` admin privilege.  ***Example cURL requests***  **List groups's privileges in a cluster** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups/$GROUP_ID/privileges  {   \"privileges\": [     \"cluster_view\",     \"cluster_update\",     \"cluster_delete\",     \"cluster_view_privileges\",     \"cluster_set_privileges\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
gid = 'gid_example' # str | Group Id.

try:
    # List group's cluster privileges
    api_response = api_instance.list_group_cluster_privileges(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_group_cluster_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id. | 
 **gid** | **str**| Group Id. | 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_cluster_privileges**
> InlineResponse20020 list_user_cluster_privileges(id, uid)

List user's cluster privileges

Returns the list of user's (`{uid}`) privileges in a cluster (`{id}`).  This operation requires `cluster_view_privileges` privilege. For administrators who do not have to be members of this cluster, `oz_clusters_view_privileges` privilege is required.  ***Example cURL requests***  **List user's privileges in a cluster** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/users/$USER_ID/privileges  {   \"privileges\": [     \"cluster_view\",     \"cluster_update\",     \"cluster_delete\",     \"cluster_view_privileges\",     \"cluster_set_privileges\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
uid = 'uid_example' # str | User Id.

try:
    # List user's cluster privileges
    api_response = api_instance.list_user_cluster_privileges(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_user_cluster_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_cluster**
> modify_cluster(body, id)

Modify cluster details

Updates the details about a cluster.  This operation requires `cluster_update` privilege or `oz_clusters_update` admin privilege.  ***Example cURL requests***  **Change cluster name** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"name\": \"new_cluster12\"}' \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
body = onezone_client.ClusterUpdateRequest() # ClusterUpdateRequest | Cluster data.
id = 'id_example' # str | Cluster Id.

try:
    # Modify cluster details
    api_instance.modify_cluster(body, id)
except ApiException as e:
    print("Exception when calling ClusterApi->modify_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterUpdateRequest**](ClusterUpdateRequest.md)| Cluster data. | 
 **id** | **str**| Cluster Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oz_clusters_list**
> Clusters oz_clusters_list()

List all clusters

Returns the list of all clusters managed by the Onezone service.  This operation requires `oz_clusters_list` admin privilege.  ***Example cURL requests***  **List all clusters** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters  {   \"clusters\": [     \"S0Y9FSe9TFJFFzzLtBEs8\",     \"IkHBv8CoAFmbFU4fj26\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))

try:
    # List all clusters
    api_response = api_instance.oz_clusters_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->oz_clusters_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Clusters**](Clusters.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_cluster_group**
> remove_cluster_group(id, gid)

Remove group from cluster

Removes a specific group from cluster.  For regular users, who belong to this cluster it requires `cluster_remove_group` privilege to remove a group from this cluster.  For administrators, who are not members of this cluster, `oz_clusters_remove_relationships` privilege is required.  ***Example cURL requests***  **Get cluster group details** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups/$GROUP_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
gid = 'gid_example' # str | Group Id.

try:
    # Remove group from cluster
    api_instance.remove_cluster_group(id, gid)
except ApiException as e:
    print("Exception when calling ClusterApi->remove_cluster_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id. | 
 **gid** | **str**| Group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_cluster_user**
> remove_cluster_user(id, uid)

Remove user from cluster

Removes user from specific cluster.  This operation requires `cluster_remove_user` privilege in the cluster or `oz_clusters_remove_relationships` and `oz_users_remove_relationships` admin privileges.  ***Example cURL requests***  **Get cluster user data** ```bash curl -u admin:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/users/$USER_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
uid = 'uid_example' # str | User Id.

try:
    # Remove user from cluster
    api_instance.remove_cluster_user(id, uid)
except ApiException as e:
    print("Exception when calling ClusterApi->remove_cluster_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cluster Id. | 
 **uid** | **str**| User Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_cluster_privileges**
> update_group_cluster_privileges(body, id, gid)

Update group's privileges in a cluster

Updates group's (`{gid}`) privileges in a cluster (`{id}`).  This operation requires `cluster_set_privileges` privilege or `oz_clusters_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update group's privileges in a cluster** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"cluster_view\", \"cluster_update\"], \"revoke\": [\"cluster_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups/$GROUP_ID/privileges ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
body = onezone_client.ClusterPrivilegesUpdate() # ClusterPrivilegesUpdate | Cluster privileges update request.
id = 'id_example' # str | Cluster Id.
gid = 'gid_example' # str | Group Id.

try:
    # Update group's privileges in a cluster
    api_instance.update_group_cluster_privileges(body, id, gid)
except ApiException as e:
    print("Exception when calling ClusterApi->update_group_cluster_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterPrivilegesUpdate**](ClusterPrivilegesUpdate.md)| Cluster privileges update request. | 
 **id** | **str**| Cluster Id. | 
 **gid** | **str**| Group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_cluster_privileges**
> update_user_cluster_privileges(body, id, uid)

Update user's cluster privileges

Updates user's (`{uid}`) privileges in a cluster (`{id}`).  This operation requires `cluster_set_privileges` privilege. For administrators who do not have to be members of this cluster, `oz_clusters_set_privileges` privilege is required.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update user's privileges in a cluster** ```bash curl -u admin:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"cluster_view\", \"cluster_update\"], \"revoke\": [\"cluster_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/users/$USER_ID/privileges ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
body = onezone_client.ClusterPrivilegesUpdate() # ClusterPrivilegesUpdate | Cluster privileges update request.
id = 'id_example' # str | Cluster Id.
uid = 'uid_example' # str | User Id.

try:
    # Update user's cluster privileges
    api_instance.update_user_cluster_privileges(body, id, uid)
except ApiException as e:
    print("Exception when calling ClusterApi->update_user_cluster_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterPrivilegesUpdate**](ClusterPrivilegesUpdate.md)| Cluster privileges update request. | 
 **id** | **str**| Cluster Id. | 
 **uid** | **str**| User Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

