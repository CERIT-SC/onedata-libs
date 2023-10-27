# onezone_client.HarvesterApi

All URIs are relative to */api/v3/onezone*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group_to_harvester**](HarvesterApi.md#add_group_to_harvester) | **PUT** /harvesters/{id}/groups/{gid} | Add group to harvester
[**add_harvester_user**](HarvesterApi.md#add_harvester_user) | **PUT** /harvesters/{id}/users/{uid} | Add user to harvester
[**add_space_to_harvester**](HarvesterApi.md#add_space_to_harvester) | **PUT** /harvesters/{id}/spaces/{sid} | Add space to harvester
[**create_harvester**](HarvesterApi.md#create_harvester) | **POST** /harvesters | Create new harvester
[**create_harvester_group**](HarvesterApi.md#create_harvester_group) | **POST** /harvesters/{id}/groups | Create group in harvester
[**create_harvester_group_token**](HarvesterApi.md#create_harvester_group_token) | **POST** /harvesters/{id}/groups/token | Create harvester invite token for group
[**create_harvester_index**](HarvesterApi.md#create_harvester_index) | **POST** /harvesters/{id}/indices | Create new index in harvester
[**create_harvester_invite_space_token**](HarvesterApi.md#create_harvester_invite_space_token) | **POST** /harvesters/{id}/spaces/token | Create harvester invite token for space
[**create_harvester_user_invite_token**](HarvesterApi.md#create_harvester_user_invite_token) | **POST** /harvesters/{id}/users/token | Create harvester user invite token
[**get_effective_group_harvester_membership_intermediaries**](HarvesterApi.md#get_effective_group_harvester_membership_intermediaries) | **GET** /harvesters/{id}/effective_groups/{gid}/membership | Get effective group&#x27;s harvester membership intermediaries
[**get_effective_harvester_group**](HarvesterApi.md#get_effective_harvester_group) | **GET** /harvesters/{id}/effective_groups/{gid} | Get effective harvester group details
[**get_effective_harvester_user**](HarvesterApi.md#get_effective_harvester_user) | **GET** /harvesters/{id}/effective_users/{uid} | Get effective harvester user details
[**get_effective_user_harvester_membership_intermediaries**](HarvesterApi.md#get_effective_user_harvester_membership_intermediaries) | **GET** /harvesters/{id}/effective_users/{uid}/membership | Get effective user&#x27;s harvester membership intermediaries
[**get_harvester**](HarvesterApi.md#get_harvester) | **GET** /harvesters/{id} | Get harvester details
[**get_harvester_config**](HarvesterApi.md#get_harvester_config) | **GET** /harvesters/{id}/gui_plugin_config | Get harvester configuration
[**get_harvester_group**](HarvesterApi.md#get_harvester_group) | **GET** /harvesters/{id}/groups/{gid} | Get harvester&#x27;s group details
[**get_harvester_index**](HarvesterApi.md#get_harvester_index) | **GET** /harvesters/{id}/indices/{idx} | Get harvester index details
[**get_harvester_index_stats**](HarvesterApi.md#get_harvester_index_stats) | **GET** /harvesters/{id}/indices/{idx}/stats | Get harvester index stats
[**get_harvester_space**](HarvesterApi.md#get_harvester_space) | **GET** /harvesters/{id}/spaces/{sid} | Get harvester space details
[**get_harvester_user**](HarvesterApi.md#get_harvester_user) | **GET** /harvesters/{id}/users/{uid} | Get harvester user details
[**harvester_join_space**](HarvesterApi.md#harvester_join_space) | **POST** /harvesters/{id}/spaces/join | Join harvester to a space
[**list_effective_group_harvester_privileges**](HarvesterApi.md#list_effective_group_harvester_privileges) | **GET** /harvesters/{id}/effective_groups/{gid}/privileges | List effective group&#x27;s harvester privileges
[**list_effective_harvester_groups**](HarvesterApi.md#list_effective_harvester_groups) | **GET** /harvesters/{id}/effective_groups | List effective harvester groups
[**list_effective_harvester_users**](HarvesterApi.md#list_effective_harvester_users) | **GET** /harvesters/{id}/effective_users | List effective harvester users
[**list_effective_user_harvester_privileges**](HarvesterApi.md#list_effective_user_harvester_privileges) | **GET** /harvesters/{id}/effective_users/{uid}/privileges | List effective user&#x27;s harvester privileges
[**list_group_harvester_privileges**](HarvesterApi.md#list_group_harvester_privileges) | **GET** /harvesters/{id}/groups/{gid}/privileges | List group&#x27;s harvester privileges
[**list_harvester_groups**](HarvesterApi.md#list_harvester_groups) | **GET** /harvesters/{id}/groups | List harvester groups
[**list_harvester_indices**](HarvesterApi.md#list_harvester_indices) | **GET** /harvesters/{id}/indices | List harvester indices
[**list_harvester_privileges**](HarvesterApi.md#list_harvester_privileges) | **GET** /harvesters/privileges | List all harvester privileges
[**list_harvester_spaces**](HarvesterApi.md#list_harvester_spaces) | **GET** /harvesters/{id}/spaces | List harvester spaces
[**list_harvester_users**](HarvesterApi.md#list_harvester_users) | **GET** /harvesters/{id}/users | List harvester users
[**list_user_harvester_privileges**](HarvesterApi.md#list_user_harvester_privileges) | **GET** /harvesters/{id}/users/{uid}/privileges | List user&#x27;s harvester privileges
[**modify_harvester**](HarvesterApi.md#modify_harvester) | **PATCH** /harvesters/{id} | Modify harvester details
[**modify_harvester_config**](HarvesterApi.md#modify_harvester_config) | **PATCH** /harvesters/{id}/gui_plugin_config | Modify harvester configuration
[**modify_harvester_index**](HarvesterApi.md#modify_harvester_index) | **PATCH** /harvesters/{id}/indices/{idx} | Modify harvester index
[**oz_harvesters_list**](HarvesterApi.md#oz_harvesters_list) | **GET** /harvesters | List all harvesters
[**query_harvester_index**](HarvesterApi.md#query_harvester_index) | **POST** /harvesters/{id}/indices/{idx}/query | Query harvester index
[**remove_harvested_index_metadata**](HarvesterApi.md#remove_harvested_index_metadata) | **DELETE** /harvesters/{id}/indices/{idx}/metadata | Remove harvested index metadata
[**remove_harvested_metadata**](HarvesterApi.md#remove_harvested_metadata) | **DELETE** /harvesters/{id}/metadata | Remove harvested metadata
[**remove_harvester**](HarvesterApi.md#remove_harvester) | **DELETE** /harvesters/{id} | Remove harvester
[**remove_harvester_group**](HarvesterApi.md#remove_harvester_group) | **DELETE** /harvesters/{id}/groups/{gid} | Remove group from harvester
[**remove_harvester_index**](HarvesterApi.md#remove_harvester_index) | **DELETE** /harvesters/{id}/indices/{idx} | Remove harvester index
[**remove_harvester_space**](HarvesterApi.md#remove_harvester_space) | **DELETE** /harvesters/{id}/spaces/{sid} | Remove harvester space
[**remove_harvester_user**](HarvesterApi.md#remove_harvester_user) | **DELETE** /harvesters/{id}/users/{uid} | Remove user from harvester
[**update_group_harvester_privileges**](HarvesterApi.md#update_group_harvester_privileges) | **PATCH** /harvesters/{id}/groups/{gid}/privileges | Update group privileges to harvester
[**update_user_harvester_privileges**](HarvesterApi.md#update_user_harvester_privileges) | **PATCH** /harvesters/{id}/users/{uid}/privileges | Update user&#x27;s harvester privileges

# **add_group_to_harvester**
> add_group_to_harvester(id, gid, body=body)

Add group to harvester

Adds group {gid} as member of harvester {id}. Optional privileges can be passed in the request body, otherwise default privileges will be set for the group in this harvester.  This operation requires `harvester_add_group` privilege in the harvester and `group_add_harvester` privilege in the group. If `privileges` are specified in the request, `harvester_set_privileges` privilege is also required.  For administrator who does not belong to the group / harvester, `oz_groups_add_relationships` and `oz_harvesters_add_relationships` privileges are required, and `oz_harvesters_set_privileges` if `privileges` are specified in the request.  ***Example cURL requests***  **Add group to harvester** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\  https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups/$GROUP_ID ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
gid = 'gid_example' # str | Group Id.
body = onezone_client.GroupsGidBody3() # GroupsGidBody3 |  (optional)

try:
    # Add group to harvester
    api_instance.add_group_to_harvester(id, gid, body=body)
except ApiException as e:
    print("Exception when calling HarvesterApi->add_group_to_harvester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **gid** | **str**| Group Id. | 
 **body** | [**GroupsGidBody3**](GroupsGidBody3.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_harvester_user**
> add_harvester_user(id, uid, body=body)

Add user to harvester

Adds user {uid} as member of harvester {id}. Optional privileges can be passed in the request body, otherwise default privileges will be set for the user in this harvester.  This operation can only be invoked by the user {uid} to add himself to the harvester (if he is not a member already) and requires `harvester_invite_user` privilege in the harvester. If `privileges` are specified in the request, `harvester_set_privileges` privilege is also required.  Administrators having the `oz_harvesters_add_relationships` and `oz_users_add_relationships` admin privileges can add any user to any harvester, though `oz_harvesters_set_privileges` privilege is required if `privileges` are specified in the request.  ***Example cURL requests***  **Add user to harvester** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/users/$USER_ID ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
uid = 'uid_example' # str | User Id.
body = onezone_client.UsersUidBody4() # UsersUidBody4 |  (optional)

try:
    # Add user to harvester
    api_instance.add_harvester_user(id, uid, body=body)
except ApiException as e:
    print("Exception when calling HarvesterApi->add_harvester_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **uid** | **str**| User Id. | 
 **body** | [**UsersUidBody4**](UsersUidBody4.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_space_to_harvester**
> add_space_to_harvester(id, sid, body=body)

Add space to harvester

Adds space {sid} as member of harvester {id}.  This operation requires `harvester_add_space` privilege in the harvester and `space_add_harvester` privilege in the space.  For administrator who does not belong to the space / harvester, `oz_spaces_add_relationships` and `oz_harvesters_add_relationships` privileges are required.  ***Example cURL requests***  **Add space to harvester** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\  https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/spaces/$SPACE_ID ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
sid = 'sid_example' # str | Space Id.
body = ['body_example'] # list[str] |  (optional)

try:
    # Add space to harvester
    api_instance.add_space_to_harvester(id, sid, body=body)
except ApiException as e:
    print("Exception when calling HarvesterApi->add_space_to_harvester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **sid** | **str**| Space Id. | 
 **body** | [**list[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_harvester**
> create_harvester(body)

Create new harvester

Creates new harvester.  This operation requires `oz_harvesters_create` admin privilege.  See also:   [Create a new harvester for the current user](#operation/create_user_harvester)   [Create a new harvester for given group](#operation/create_harvester_for_group)    ***Example cURL requests***  **Create new harvester** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"name\" : \"new_harvester\", \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\", \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\"  \\ \"guiPluginConfig\" : { \"typeMapping\": [ { \"id\": 0, \"name\": \"Type 1\" }, { \"id\": 1, \"name\": \"Type 1\" } ],                        \"externalHelpLink\": \"http://example.com/some_help_page\",                        \"refreshDataTimeout\": 1000 }                     }' \\ https://$ZONE_HOST/api/v3/onezone/harvesters ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
body = onezone_client.HarvesterCreateRequest() # HarvesterCreateRequest | Harvester properties.

try:
    # Create new harvester
    api_instance.create_harvester(body)
except ApiException as e:
    print("Exception when calling HarvesterApi->create_harvester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HarvesterCreateRequest**](HarvesterCreateRequest.md)| Harvester properties. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_harvester_group**
> create_harvester_group(body, id)

Create group in harvester

Creates a new group belonging to the harvester of {id}.  This operation requires `harvester_add_group` privilege. For administrator who does not belong to this group `oz_harvesters_add_relationships` and `oz_groups_create` privileges are required.  ***Example cURL requests***  **Create group in harvester** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
body = onezone_client.GroupCreateRequest() # GroupCreateRequest | Group properties.
id = 'id_example' # str | Harvester Id.

try:
    # Create group in harvester
    api_instance.create_harvester_group(body, id)
except ApiException as e:
    print("Exception when calling HarvesterApi->create_harvester_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupCreateRequest**](GroupCreateRequest.md)| Group properties. | 
 **id** | **str**| Harvester Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_harvester_group_token**
> HarvesterInviteToken create_harvester_group_token(id)

Create harvester invite token for group

This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token allowing to add a group to a specific harvester.  This operation requires `harvester_add_group` privilege or `oz_harvesters_add_relationships` admin privilege.  ***Example cURL requests***  **Create harvester invitation token for group** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups/token  {   \"token\": \"MDAxNmxvY0cGUgKWsjcpnrLE00RtOd2F00cGUgKWsjcpnrLE00RtOdhmnQycSICwMsugo\" } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.

try:
    # Create harvester invite token for group
    api_response = api_instance.create_harvester_group_token(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->create_harvester_group_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 

### Return type

[**HarvesterInviteToken**](HarvesterInviteToken.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_harvester_index**
> create_harvester_index(body, id)

Create new index in harvester

Creates new index in given harvester.  This operation requires `oz_harvesters_update` admin privilege.  ***Example cURL requests***  **Create new index in harvester** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"name\" : \"My study index\", \"guiPluginName\" : \"study\"}\\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
body = onezone_client.HarvesterIndexCreateRequest() # HarvesterIndexCreateRequest | Index properties.
id = 'id_example' # str | Harvester Id.

try:
    # Create new index in harvester
    api_instance.create_harvester_index(body, id)
except ApiException as e:
    print("Exception when calling HarvesterApi->create_harvester_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HarvesterIndexCreateRequest**](HarvesterIndexCreateRequest.md)| Index properties. | 
 **id** | **str**| Harvester Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_harvester_invite_space_token**
> HarvesterInviteToken create_harvester_invite_space_token(id)

Create harvester invite token for space

This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token which can be can be consumed to add a space to a harvester.  This operation requires `harvester_invite_space` privilege or `oz_harvesters_add_relationships` admin privilege.  ***Example cURL requests***  **Create harvester invite space token** ```bash curl -u admin:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/spaces/token  {   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaWVyIHZjUGlIcGkweGZta1ZOdEp00eUNINVNvR2001Wl\" } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.

try:
    # Create harvester invite token for space
    api_response = api_instance.create_harvester_invite_space_token(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->create_harvester_invite_space_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 

### Return type

[**HarvesterInviteToken**](HarvesterInviteToken.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_harvester_user_invite_token**
> HarvesterInviteToken create_harvester_user_invite_token(id)

Create harvester user invite token

This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token allowing new user to join a harvester.  This operation requires `harvester_invite_user` privilege. For administrators who do not have to be members of this harvester, `oz_harvesters_add_relationships` privilege is required.  ***Example cURL requests***  **Create harvester user invite token** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/users/token  {   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaWVyIG00zcEJ2UDVuOHhkQUNhdk9hbTlyNnIwNldPSzVhc\" } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.

try:
    # Create harvester user invite token
    api_response = api_instance.create_harvester_user_invite_token(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->create_harvester_user_invite_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 

### Return type

[**HarvesterInviteToken**](HarvesterInviteToken.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_group_harvester_membership_intermediaries**
> MembershipIntermediaries get_effective_group_harvester_membership_intermediaries(id, gid)

Get effective group's harvester membership intermediaries

Returns the effective group's (`{gid}`) harvester membership intermediaries - entities from which the group inherits access to the harvester (`{id}`). Special keyword `\"self\"` in entity id indicates that the group (`{gid}`) has a direct access to the harvester (`{id}`).  This operation requires any of the following authorization: * as user who is an effective member of the group (`{gid}`) * as user who has `harvester_view` privilege in the harvester (`{id}`) * as user who has `oz_harvesters_view` admin privilege.  ***Example cURL requests***  **Get effective group's harvester membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_groups/$GROUP_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"harvester\", \"id\": \"self\"}   ] } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
gid = 'gid_example' # str | Group Id.

try:
    # Get effective group's harvester membership intermediaries
    api_response = api_instance.get_effective_group_harvester_membership_intermediaries(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->get_effective_group_harvester_membership_intermediaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **gid** | **str**| Group Id. | 

### Return type

[**MembershipIntermediaries**](MembershipIntermediaries.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_harvester_group**
> Group get_effective_harvester_group(id, gid)

Get effective harvester group details

Returns details about a specific effective group in a harvester.  This operation requires `harvester_view` privilege or `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get effective harvester group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_groups/$GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_groupX\",   \"type\": \"team\" } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
gid = 'gid_example' # str | Group Id.

try:
    # Get effective harvester group details
    api_response = api_instance.get_effective_harvester_group(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->get_effective_harvester_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **gid** | **str**| Group Id. | 

### Return type

[**Group**](Group.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_harvester_user**
> User get_effective_harvester_user(id, uid)

Get effective harvester user details

Returns details about a specific effective user in a harvester.  This operation requires `harvester_view` privilege or `oz_users_view` admin privilege.  ***Example cURL requests***  **Get effective harvester user details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_users/$USER_ID  {   \"userId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"username\" : \"jodoe\",   \"fullName\" : \"John Doe\" } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
uid = 'uid_example' # str | User Id.

try:
    # Get effective harvester user details
    api_response = api_instance.get_effective_harvester_user(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->get_effective_harvester_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**User**](User.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_user_harvester_membership_intermediaries**
> MembershipIntermediaries get_effective_user_harvester_membership_intermediaries(id, uid)

Get effective user's harvester membership intermediaries

Returns the effective user's (`{uid}`) harvester membership intermediaries - entities from which the user inherits access to the harvester (`{id}`). Special keyword `\"self\"` in entity id indicates that the user (`{uid}`) has a direct access to the harvester (`{id}`).  This operation requires any of the following authorization: * as user (`{uid}`) who is an effective member of the harvester (`{id}`) * as user who has `harvester_view` privilege in the harvester (`{id}`) * as user who has `oz_harvesters_view` admin privilege.  ***Example cURL requests***  **Get effective user's harvester membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_users/$USER_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"harvester\", \"id\": \"self\"}   ] } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
uid = 'uid_example' # str | User Id.

try:
    # Get effective user's harvester membership intermediaries
    api_response = api_instance.get_effective_user_harvester_membership_intermediaries(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->get_effective_user_harvester_membership_intermediaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**MembershipIntermediaries**](MembershipIntermediaries.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_harvester**
> Harvester get_harvester(id)

Get harvester details

Returns the details about a specific harvester.  If called by user who is not member of the harvester, requires `oz_harvesters_view` admin privilege.  ***Example cURL requests***  **Get harvester details** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID  {   \"harvesterId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_harvester1\",   \"public\" : true,   \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\",   \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.

try:
    # Get harvester details
    api_response = api_instance.get_harvester(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->get_harvester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 

### Return type

[**Harvester**](Harvester.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_harvester_config**
> HarvesterGuiPluginConfig get_harvester_config(id)

Get harvester configuration

Returns JSON configuration for harvester GUI plugin.  If called by user who is not member of the harvester, requires `oz_harvesters_view` admin privilege.  ***Example cURL requests***  **Get harvester details** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/config  {   \"config\" : {     \"typeMapping\": [ { \"id\": 0, \"name\": \"Type 1\" }, { \"id\": 1, \"name\": \"Type 1\" } ],     \"externalHelpLink\": \"http://example.com/some_help_page\",     \"refreshDataTimeout\": 1000   } } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.

try:
    # Get harvester configuration
    api_response = api_instance.get_harvester_config(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->get_harvester_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 

### Return type

[**HarvesterGuiPluginConfig**](HarvesterGuiPluginConfig.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_harvester_group**
> Group get_harvester_group(id, gid)

Get harvester's group details

Returns details about a specific group in a harvester.  This operation requires `harvester_view` privilege. For administrators who do not have to be members of this harvester, `oz_groups_view` privilege is required.  ***Example cURL requests***  **Get harvester group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups/$GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_groupX\",   \"type\": \"team\" } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
gid = 'gid_example' # str | Group Id.

try:
    # Get harvester's group details
    api_response = api_instance.get_harvester_group(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->get_harvester_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **gid** | **str**| Group Id. | 

### Return type

[**Group**](Group.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_harvester_index**
> HarvesterIndex get_harvester_index(id, idx)

Get harvester index details

Returns details about a specific index in the harvester.  For users who are members of harvester it requires `harvester_view`. For administrators who do not have to be members of this harvester, `oz_harvesters_view` privilege is required.  ***Example cURL requests***  **Get harvester space details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices/$INDEX_ID  {   \"indexId\": \"H8ez0CwDZ7JMYRWn1ipmBpgJHPXzIXj0-upGkf9tk\",   \"name\": \"My study index\"   \"guiPluginName\": \"study\"   \"schema\": \"{ \\\"mappings\\\": { \\\"properties\\\": { \\\"foo\\\": { \\\"type\\\": \\\"keyword\\\" } } } }\"   \"includeMetadata\": [\"json\", \"xattrs\"]   \"includeFileDetails\": [\"fileName\", \"metadataExistenceFlags\"]   \"includeRejectionReason\": false   \"retryOnRejection\": true } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
idx = 'idx_example' # str | Index Id.

try:
    # Get harvester index details
    api_response = api_instance.get_harvester_index(id, idx)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->get_harvester_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **idx** | **str**| Index Id. | 

### Return type

[**HarvesterIndex**](HarvesterIndex.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_harvester_index_stats**
> HarvesterIndexStatsDetails get_harvester_index_stats(id, idx)

Get harvester index stats

Returns details about harvesting stats of a specific index in the harvester.  For users who are members of harvester it requires `harvester_view`. For administrators who do not have to be members of this harvester, `oz_harvesters_view` privilege is required.  ***Example cURL requests***  **Get harvester index stats** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices/$INDEX_ID  {   $SPACE_ID1 : {     $PROVIDER_ID1 : {       \"currentSeq\" : 5,       \"maxSeq\" : 8,       \"error\" : null,       \"lastUpdate\" : 1557928576,       \"archival\" : false     },     $PROVIDER_ID2 : {       \"currentSeq\" : 8,       \"maxSeq\" : 13,       \"error\" : \"Service unavailable: temporary failure.\",       \"lastUpdate\" : 1557928576,       \"archival\" : false     }   },   $SPACE_ID2 : {     $PROVIDER_ID1 : {       \"currentSeq\" : 13,       \"maxSeq\" : 21,       \"error\" : null,       \"lastUpdate\" : 1557928576,       \"archival\" : false     },     $PROVIDER_ID3 : {       \"currentSeq\" : 21,       \"maxSeq\" : 34,       \"error\" : null,       \"lastUpdate\" : 1557928576,       \"archival\" : true     }   } } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
idx = 'idx_example' # str | Index Id.

try:
    # Get harvester index stats
    api_response = api_instance.get_harvester_index_stats(id, idx)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->get_harvester_index_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **idx** | **str**| Index Id. | 

### Return type

[**HarvesterIndexStatsDetails**](HarvesterIndexStatsDetails.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_harvester_space**
> Space get_harvester_space(id, sid)

Get harvester space details

Returns details about a specific space in the harvester.  For users who are members of harvester it requires `harvester_view`. For administrators who do not have to be members of this harvester, `oz_spaces_view` privilege is required.  ***Example cURL requests***  **Get harvester space details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/spaces/$SPACE_ID  {   \"spaceId\": \"H8ez0CwDZ7JMYRWn1ipmBpgJHPXzIXj0-upGkf9tk\",   \"name\": \"example\" } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
sid = 'sid_example' # str | Space Id.

try:
    # Get harvester space details
    api_response = api_instance.get_harvester_space(id, sid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->get_harvester_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **sid** | **str**| Space Id. | 

### Return type

[**Space**](Space.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_harvester_user**
> User get_harvester_user(id, uid)

Get harvester user details

Returns basic information about a specific user in a harvester.  This operation requires `harvester_view` privilege. For administrators who do not have to be members of this harvester, `oz_users_view` privilege is required.  ***Example cURL requests***  **Get harvester user data** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\" } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
uid = 'uid_example' # str | User Id.

try:
    # Get harvester user details
    api_response = api_instance.get_harvester_user(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->get_harvester_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**User**](User.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **harvester_join_space**
> harvester_join_space(id, body=body)

Join harvester to a space

Joins the harvester to an existing space based on provided `harvesterJoinSpace` invitation token (the space becomes a metadata source for the harvester).  This operation requires `harvester_add_space` privilege. For administrator who does not belong to this space `oz_harvesters_add_relationships` and `oz_spaces_add_relationships` privilege is required.  ***Example cURL requests***  **Join harvester to a space** ```bash curl -u admin:password -H \"Content-type: application/json\" \\ -d '{\"token\":\"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVuJ3l02U1JXzstRdK00ZHbso02rRcG8bJLAo\"}' \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/spaces/join ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
body = onezone_client.SpaceInviteToken() # SpaceInviteToken | harvesterJoinSpace invite token. (optional)

try:
    # Join harvester to a space
    api_instance.harvester_join_space(id, body=body)
except ApiException as e:
    print("Exception when calling HarvesterApi->harvester_join_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **body** | [**SpaceInviteToken**](SpaceInviteToken.md)| harvesterJoinSpace invite token. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_group_harvester_privileges**
> InlineResponse20018 list_effective_group_harvester_privileges(id, gid)

List effective group's harvester privileges

Returns the list of effective group's (`{gid}`) privileges in a harvester (`{id}`).  Effective privileges are a sum of group's privileges and privileges inherited from its parent group memberships.  This operation requires `harvester_view_privileges` privilege or `oz_harvesters_view_privileges` admin privilege.  ***Example cURL requests***  **List effective groups's privileges in a harvester** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_groups/$GROUP_ID/privileges  {   \"privileges\": [     \"harvester_view\",     \"harvester_update\",     \"harvester_delete\",     \"harvester_view_privileges\",     \"harvester_set_privileges\"   ] } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
gid = 'gid_example' # str | Group Id.

try:
    # List effective group's harvester privileges
    api_response = api_instance.list_effective_group_harvester_privileges(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->list_effective_group_harvester_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **gid** | **str**| Group Id. | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_harvester_groups**
> Groups list_effective_harvester_groups(id)

List effective harvester groups

Returns the effective list of groups belonging to a specific harvester.  This operation requires `harvester_view` privilege or `oz_harvesters_list_relationships` admin privilege.  ***Example cURL requests***  **Get harvester effective groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_groups  {   \"groups\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.

try:
    # List effective harvester groups
    api_response = api_instance.list_effective_harvester_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->list_effective_harvester_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 

### Return type

[**Groups**](Groups.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_harvester_users**
> Users list_effective_harvester_users(id)

List effective harvester users

Returns the effective list of users belonging to a specific harvester.  This operation requires `harvester_view` privilege or `oz_harvesters_list_relationships` admin privilege.  ***Example cURL requests***  **Get harvester effective users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_users  {   \"users\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.

try:
    # List effective harvester users
    api_response = api_instance.list_effective_harvester_users(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->list_effective_harvester_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 

### Return type

[**Users**](Users.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_user_harvester_privileges**
> InlineResponse20018 list_effective_user_harvester_privileges(id, uid)

List effective user's harvester privileges

Returns the list of effective user's (`{uid}`) privileges in a harvester (`{id}`).  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation requires `harvester_view_privileges` privilege or `oz_harvesters_view_privileges` admin privilege.  ***Example cURL requests***  **List effective user's privileges in a harvester** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_users/$USER_ID/privileges  {   \"privileges\": [     \"harvester_view\",     \"harvester_update\",     \"harvester_delete\",     \"harvester_view_privileges\",     \"harvester_set_privileges\"   ] } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
uid = 'uid_example' # str | User Id.

try:
    # List effective user's harvester privileges
    api_response = api_instance.list_effective_user_harvester_privileges(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->list_effective_user_harvester_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_harvester_privileges**
> InlineResponse20018 list_group_harvester_privileges(id, gid)

List group's harvester privileges

Returns the list of group's (`{gid}`) privileges in a harvester (`{id}`).  This operation requires `harvester_view_privileges` privilege or `oz_harvesters_view_privileges` admin privilege.  ***Example cURL requests***  **List groups's privileges in a harvester** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups/$GROUP_ID/privileges  {   \"privileges\": [     \"harvester_view\",     \"harvester_update\",     \"harvester_delete\",     \"harvester_view_privileges\",     \"harvester_set_privileges\"   ] } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
gid = 'gid_example' # str | Group Id.

try:
    # List group's harvester privileges
    api_response = api_instance.list_group_harvester_privileges(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->list_group_harvester_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **gid** | **str**| Group Id. | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_harvester_groups**
> Groups list_harvester_groups(id)

List harvester groups

Returns the list of groups belonging to a specific harvester.  This operation requires `harvester_view` privilege in the harvester.  For administrator who does not belong to the harvester, `oz_harvesters_list_relationships` privilege is required.  ***Example cURL requests***  **Get harvester groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups  {   \"groups\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.

try:
    # List harvester groups
    api_response = api_instance.list_harvester_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->list_harvester_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 

### Return type

[**Groups**](Groups.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_harvester_indices**
> HarvesterIndices list_harvester_indices(id)

List harvester indices

Returns the list of indices in specific harvester.  For users who are members of harvester it requires `harvester_view`.  For administrators who do not have to be members of this harvester, `oz_harvesters_view` privilege is required.  ***Example cURL requests***  **Get harvester index** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices  {   \"indices\": [     \"MDAxNmxvYZjUGlIcGkweGZta1ZOdEp00eUNINVNvR2001Wl\"   ] } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.

try:
    # List harvester indices
    api_response = api_instance.list_harvester_indices(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->list_harvester_indices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 

### Return type

[**HarvesterIndices**](HarvesterIndices.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_harvester_privileges**
> InlineResponse20017 list_harvester_privileges()

List all harvester privileges

Returns list of all possible harvester privileges.  This endpoint does not require authentication.  ***Example cURL requests***  **Get list of all harvester privileges** ```bash curl https://$ZONE_HOST/api/v3/onezone/harvesters/privileges  {   \"admin\": [     \"harvester_view\",     \"harvester_update\",     \"harvester_delete\",     \"harvester_view_privileges\",     \"harvester_set_privileges\",     \"harvester_add_user\",     \"harvester_remove_user\",     \"harvester_add_group\",     \"harvester_remove_group\",     \"harvester_add_space\",     \"harvester_remove_space\"   ],   \"manager\": [     \"harvester_view\",     \"harvester_add_user\",     \"harvester_remove_user\",     \"harvester_add_group\",     \"harvester_remove_group\",     \"harvester_add_space\",     \"harvester_remove_space\"   ],   \"member\": [     \"harvester_view\"   ] } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))

try:
    # List all harvester privileges
    api_response = api_instance.list_harvester_privileges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->list_harvester_privileges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_harvester_spaces**
> Spaces list_harvester_spaces(id)

List harvester spaces

Returns the list of spaces in specific harvester.  For users who are members of harvester it requires `harvester_view`.  For administrators who do not have to be members of this harvester, `oz_harvesters_list_relationships` privilege is required.  ***Example cURL requests***  **List harvester spaces** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/spaces  {   \"spaces\": [     \"MDAxNmxvYZjUGlIcGkweGZta1ZOdEp00eUNINVNvR2001Wl\"   ] } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.

try:
    # List harvester spaces
    api_response = api_instance.list_harvester_spaces(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->list_harvester_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 

### Return type

[**Spaces**](Spaces.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_harvester_users**
> Users list_harvester_users(id)

List harvester users

Returns the list of users belonging to a specific harvester.  This operation requires `harvester_view` privilege. For administrators who do not have to be members of this harvester, `oz_harvesters_list_relationships` privilege is required.  ***Example cURL requests***  **Get harvester users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/users  {   \"users\": [     \"a5b469a2b0516b662a49da74d6d7d7bc\"   ] } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.

try:
    # List harvester users
    api_response = api_instance.list_harvester_users(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->list_harvester_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 

### Return type

[**Users**](Users.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_harvester_privileges**
> InlineResponse20018 list_user_harvester_privileges(id, uid)

List user's harvester privileges

Returns the list of user's (`{uid}`) privileges in a harvester (`{id}`).  This operation requires `harvester_view_privileges` privilege. For administrators who do not have to be members of this harvester, `oz_harvesters_view_privileges` privilege is required.  ***Example cURL requests***  **List user's privileges in a harvester** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/users/$USER_ID/privileges  {   \"privileges\": [     \"harvester_view\",     \"harvester_update\",     \"harvester_delete\",     \"harvester_view_privileges\",     \"harvester_set_privileges\"   ] } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
uid = 'uid_example' # str | User Id.

try:
    # List user's harvester privileges
    api_response = api_instance.list_user_harvester_privileges(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->list_user_harvester_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_harvester**
> modify_harvester(body, id)

Modify harvester details

Updates the details about a harvester.  This operation requires `harvester_update` privilege or `oz_harvesters_update` admin privilege.  ***Example cURL requests***  **Change harvester name** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"name\": \"new_harvester12\"}' \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
body = onezone_client.HarvesterUpdateRequest() # HarvesterUpdateRequest | Harvester parameters
id = 'id_example' # str | Harvester Id.

try:
    # Modify harvester details
    api_instance.modify_harvester(body, id)
except ApiException as e:
    print("Exception when calling HarvesterApi->modify_harvester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HarvesterUpdateRequest**](HarvesterUpdateRequest.md)| Harvester parameters | 
 **id** | **str**| Harvester Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_harvester_config**
> modify_harvester_config(body, id)

Modify harvester configuration

Updates harvester GUI plugin configuration.  This operation requires `harvester_update` privilege or `oz_harvesters_update` admin privilege.  ***Example cURL requests***  **Change harvester name** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"config\": {}}' \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/config ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
body = onezone_client.HarvesterGuiPluginConfig() # HarvesterGuiPluginConfig | New harvester config
id = 'id_example' # str | Harvester Id.

try:
    # Modify harvester configuration
    api_instance.modify_harvester_config(body, id)
except ApiException as e:
    print("Exception when calling HarvesterApi->modify_harvester_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HarvesterGuiPluginConfig**](HarvesterGuiPluginConfig.md)| New harvester config | 
 **id** | **str**| Harvester Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_harvester_index**
> modify_harvester_index(body, id, idx)

Modify harvester index

Modifies harvester index.  This operation requires `harvester_update` privilege or `oz_harvesters_update` admin privilege.  ***Example cURL requests***  **Change harvester name** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"name\" : \"new_name\", \"guiPluginName\" : \"new_gui_plugin_name\"}' \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices/$INDEX_ID ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
body = onezone_client.IndicesIdxBody() # IndicesIdxBody | The new data of the index.
id = 'id_example' # str | Harvester Id.
idx = 'idx_example' # str | Index Id.

try:
    # Modify harvester index
    api_instance.modify_harvester_index(body, id, idx)
except ApiException as e:
    print("Exception when calling HarvesterApi->modify_harvester_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IndicesIdxBody**](IndicesIdxBody.md)| The new data of the index. | 
 **id** | **str**| Harvester Id. | 
 **idx** | **str**| Index Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oz_harvesters_list**
> Harvesters oz_harvesters_list()

List all harvesters

Returns the list of all harvesters managed by the Onezone service.  This operation requires `oz_harvesters_list` admin privilege.  ***Example cURL requests***  **List all harvesters** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters  {   \"harvesters\": [     \"S0Y9FSe9TFJFFzzLtBEs8\",     \"IkHBv8CoAFmbFU4fj26\"   ] } ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))

try:
    # List all harvesters
    api_response = api_instance.oz_harvesters_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->oz_harvesters_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Harvesters**](Harvesters.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_harvester_index**
> HarvesterQueryResponse query_harvester_index(body, id, idx)

Query harvester index

Performs query to index {idx} in harvester {id}.  This operation does not require any privileges when the harvester is public  otherwise being member of the harvester is required. For administrators who do not have to be members of this harvester, `oz_harvesters_view` privilege is required.  Request body and response depend on selected `harvester_plugin`. Below examples are for `elasticsearch_plugin`.  ***Example cURL requests***  **query harvester index** ```bash curl -u username:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"method\" : \"get\", \"path\" : \"resource_id\"}'  https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices/$INDEX_ID/query ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
body = onezone_client.HarvesterQuery() # HarvesterQuery | 
id = 'id_example' # str | Harvester Id.
idx = 'idx_example' # str | Index Id.

try:
    # Query harvester index
    api_response = api_instance.query_harvester_index(body, id, idx)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HarvesterApi->query_harvester_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HarvesterQuery**](HarvesterQuery.md)|  | 
 **id** | **str**| Harvester Id. | 
 **idx** | **str**| Index Id. | 

### Return type

[**HarvesterQueryResponse**](HarvesterQueryResponse.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_harvested_index_metadata**
> remove_harvested_index_metadata(id, idx)

Remove harvested index metadata

Schedules removal of all harvested metadata in given index.\\ See also: [Remove index](#operation/remove_harvester_index)  This operation requires `harvester_update` privilege or `oz_harvesters_update` admin privilege.  ***Example cURL requests***  **Remove harvested index metadata** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices/$INDEX_ID ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
idx = 'idx_example' # str | Index Id.

try:
    # Remove harvested index metadata
    api_instance.remove_harvested_index_metadata(id, idx)
except ApiException as e:
    print("Exception when calling HarvesterApi->remove_harvested_index_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **idx** | **str**| Index Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_harvested_metadata**
> remove_harvested_metadata(id)

Remove harvested metadata

Schedules removal of harvested metadata in all indices in given harvester.\\ See also: [Remove harvester](#operation/remove_harvester)  This operation requires `harvester_delete` privilege or `oz_harvesters_delete` admin privilege.  ***Example cURL requests***  **Remove harvested metadata** ```bash curl -u admin:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.

try:
    # Remove harvested metadata
    api_instance.remove_harvested_metadata(id)
except ApiException as e:
    print("Exception when calling HarvesterApi->remove_harvested_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_harvester**
> remove_harvester(id)

Remove harvester

Removes a specific harvester. **It will be no longer possible to access harvested data through onezone service**.\\ If you wish to remove harvested metadata see:  [Remove harvested data](#operation/remove_harvested_data)  This operation requires `harvester_delete` privilege or `oz_harvesters_delete` admin privilege.  ***Example cURL requests***  **Remove harvester** ```bash curl -u admin:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.

try:
    # Remove harvester
    api_instance.remove_harvester(id)
except ApiException as e:
    print("Exception when calling HarvesterApi->remove_harvester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_harvester_group**
> remove_harvester_group(id, gid)

Remove group from harvester

Removes a specific group from harvester.  For regular users, who belong to this harvester it requires `harvester_remove_group` privilege to remove a group from this harvester.  For administrators, who are not members of this harvester, `oz_harvesters_remove_relationships` privilege is required.  ***Example cURL requests***  **Get harvester group details** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups/$GROUP_ID ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
gid = 'gid_example' # str | Group Id.

try:
    # Remove group from harvester
    api_instance.remove_harvester_group(id, gid)
except ApiException as e:
    print("Exception when calling HarvesterApi->remove_harvester_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **gid** | **str**| Group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_harvester_index**
> remove_harvester_index(id, idx)

Remove harvester index

Removes index from a specific harvester. **It will be no longer possible to access harvested data through onezone service**.\\ If you wish to remove harvested metadata see: [Remove harvested metadata in index](#operation/remove_harvested_index_data)  This operation requires `harvester_update` privilege or `oz_harvesters_update` admin privilege.  ***Example cURL requests***  **Remove harvester index** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices/$INDEX_ID ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
idx = 'idx_example' # str | Index Id.

try:
    # Remove harvester index
    api_instance.remove_harvester_index(id, idx)
except ApiException as e:
    print("Exception when calling HarvesterApi->remove_harvester_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **idx** | **str**| Index Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_harvester_space**
> remove_harvester_space(id, sid)

Remove harvester space

Removes space from a specific harvester.  This operation requires `harvester_remove_space` privilege or `oz_harvesters_remove_relationships` admin privilege.  ***Example cURL requests***  **Remove harvester space** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/spaces/$SPACE_ID ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
sid = 'sid_example' # str | Space Id.

try:
    # Remove harvester space
    api_instance.remove_harvester_space(id, sid)
except ApiException as e:
    print("Exception when calling HarvesterApi->remove_harvester_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **sid** | **str**| Space Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_harvester_user**
> remove_harvester_user(id, uid)

Remove user from harvester

Removes user from specific harvester.  This operation requires `harvester_remove_user` or requires `oz_harvesters_add_relationships` and `oz_users_add_relationships` admin privilege.  ***Example cURL requests***  **Get harvester user data** ```bash curl -u admin:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/users/$USER_ID ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Harvester Id.
uid = 'uid_example' # str | User Id.

try:
    # Remove user from harvester
    api_instance.remove_harvester_user(id, uid)
except ApiException as e:
    print("Exception when calling HarvesterApi->remove_harvester_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Harvester Id. | 
 **uid** | **str**| User Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_harvester_privileges**
> update_group_harvester_privileges(body, id, gid)

Update group privileges to harvester

Updates group's (`{gid}`) privileges in a harvester (`{id}`).  This operation requires `harvester_set_privileges` privilege or `oz_harvesters_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update group's privileges in a harvester** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"harvester_view\", \"harvester_update\"], \"revoke\": [\"harvester_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups/$GROUP_ID/privileges ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
body = onezone_client.HarvesterPrivilegesUpdate() # HarvesterPrivilegesUpdate | Harvester privileges update request.
id = 'id_example' # str | Harvester Id.
gid = 'gid_example' # str | Group Id.

try:
    # Update group privileges to harvester
    api_instance.update_group_harvester_privileges(body, id, gid)
except ApiException as e:
    print("Exception when calling HarvesterApi->update_group_harvester_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HarvesterPrivilegesUpdate**](HarvesterPrivilegesUpdate.md)| Harvester privileges update request. | 
 **id** | **str**| Harvester Id. | 
 **gid** | **str**| Group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_harvester_privileges**
> update_user_harvester_privileges(body, id, uid)

Update user's harvester privileges

Updates user's (`{uid}`) privileges in a harvester (`{id}`).  This operation requires `harvester_set_privileges` privilege. For administrators who do not have to be members of this harvester, `oz_harvesters_set_privileges` privilege is required.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update user's privileges in a harvester** ```bash curl -u admin:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"harvester_view\", \"harvester_update\"], \"revoke\": [\"harvester_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/users/$USER_ID/privileges ``` 

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
api_instance = onezone_client.HarvesterApi(onezone_client.ApiClient(configuration))
body = onezone_client.HarvesterPrivilegesUpdate() # HarvesterPrivilegesUpdate | Harvester privileges update request.
id = 'id_example' # str | Harvester Id.
uid = 'uid_example' # str | User Id.

try:
    # Update user's harvester privileges
    api_instance.update_user_harvester_privileges(body, id, uid)
except ApiException as e:
    print("Exception when calling HarvesterApi->update_user_harvester_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HarvesterPrivilegesUpdate**](HarvesterPrivilegesUpdate.md)| Harvester privileges update request. | 
 **id** | **str**| Harvester Id. | 
 **uid** | **str**| User Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

