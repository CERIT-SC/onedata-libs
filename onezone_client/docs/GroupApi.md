# onezone_client.GroupApi

All URIs are relative to */api/v3/onezone*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_child_group**](GroupApi.md#add_child_group) | **PUT** /groups/{id}/children/{cid} | Add child group
[**add_group_handle_service**](GroupApi.md#add_group_handle_service) | **POST** /groups/{id}/handle_services | Create a new handle service for given group.
[**add_group_user**](GroupApi.md#add_group_user) | **PUT** /groups/{id}/users/{uid} | Add user to group
[**create_child_group**](GroupApi.md#create_child_group) | **POST** /groups/{id}/children | Create child group
[**create_child_group_token**](GroupApi.md#create_child_group_token) | **POST** /groups/{id}/children/token | Create child group invitation token
[**create_group**](GroupApi.md#create_group) | **POST** /groups | Create new group
[**create_group_handle**](GroupApi.md#create_group_handle) | **POST** /groups/{id}/handles | Create a new handle for given group
[**create_harvester_for_group**](GroupApi.md#create_harvester_for_group) | **POST** /groups/{id}/harvesters | Create a new harvester for given group
[**create_parent_group**](GroupApi.md#create_parent_group) | **POST** /groups/{id}/parents | Create a new parent group for given group
[**create_space_for_group**](GroupApi.md#create_space_for_group) | **POST** /groups/{id}/spaces | Create a new space for given group
[**create_user_group_invite_token**](GroupApi.md#create_user_group_invite_token) | **POST** /groups/{id}/users/token | Create user invite token for group
[**get_child_group**](GroupApi.md#get_child_group) | **GET** /groups/{id}/children/{cid} | Get child group details
[**get_effective_child_group**](GroupApi.md#get_effective_child_group) | **GET** /groups/{id}/effective_children/{cid} | Get effective child group details
[**get_effective_child_group_membership_intermediaries**](GroupApi.md#get_effective_child_group_membership_intermediaries) | **GET** /groups/{id}/effective_children/{cid}/membership | Get effective child&#x27;s group membership intermediaries
[**get_effective_children_groups**](GroupApi.md#get_effective_children_groups) | **GET** /groups/{id}/effective_children | Get effective child groups
[**get_effective_group_handle**](GroupApi.md#get_effective_group_handle) | **GET** /groups/{id}/effective_handles/{hid} | Get effective group handle details
[**get_effective_group_harvester**](GroupApi.md#get_effective_group_harvester) | **GET** /groups/{id}/effective_harvesters/{hid} | Get effective group harvester details
[**get_effective_group_space**](GroupApi.md#get_effective_group_space) | **GET** /groups/{id}/effective_spaces/{sid} | Get effective group space details
[**get_effective_group_user**](GroupApi.md#get_effective_group_user) | **GET** /groups/{id}/effective_users/{uid} | Get effective group user details
[**get_effective_parent_group**](GroupApi.md#get_effective_parent_group) | **GET** /groups/{id}/effective_parents/{pid} | Get effective parent group details
[**get_effective_user_group_membership_intermediaries**](GroupApi.md#get_effective_user_group_membership_intermediaries) | **GET** /groups/{id}/effective_users/{uid}/membership | Get effective user&#x27;s group membership intermediaries
[**get_group**](GroupApi.md#get_group) | **GET** /groups/{id} | Get group details
[**get_group_cluster**](GroupApi.md#get_group_cluster) | **GET** /groups/{id}/clusters/{cid} | Get group&#x27;s cluster details
[**get_group_effective_cluster**](GroupApi.md#get_group_effective_cluster) | **GET** /groups/{id}/effective_clusters/{cid} | Get group&#x27;s effective cluster details
[**get_group_effective_handle_service**](GroupApi.md#get_group_effective_handle_service) | **GET** /groups/{id}/effective_handle_services/{hsid} | Get effective group handle service details
[**get_group_effective_provider**](GroupApi.md#get_group_effective_provider) | **GET** /groups/{id}/effective_providers/{pid} | Get group&#x27;s effective provider details
[**get_group_handle**](GroupApi.md#get_group_handle) | **GET** /groups/{id}/handles/{hid} | Get group handle details
[**get_group_handle_service**](GroupApi.md#get_group_handle_service) | **GET** /groups/{id}/handle_services/{hsid} | Get group handle service details
[**get_group_harvester**](GroupApi.md#get_group_harvester) | **GET** /groups/{id}/harvesters/{hid} | Get group&#x27;s harvester details
[**get_group_space**](GroupApi.md#get_group_space) | **GET** /groups/{id}/spaces/{sid} | Get group&#x27;s space details
[**get_group_spaces_in_effective_provider**](GroupApi.md#get_group_spaces_in_effective_provider) | **GET** /groups/{id}/effective_providers/{pid}/spaces | Get group&#x27;s spaces that are supported by given effective provider
[**get_group_user**](GroupApi.md#get_group_user) | **GET** /groups/{id}/users/{uid} | Get group user details
[**get_parent_group**](GroupApi.md#get_parent_group) | **GET** /groups/{id}/parents/{pid} | Get parent group details
[**group_join_cluster**](GroupApi.md#group_join_cluster) | **POST** /groups/{id}/clusters/join | Join group to a cluster
[**group_join_harvester**](GroupApi.md#group_join_harvester) | **POST** /groups/{id}/harvesters/join | Join harvester by group
[**group_join_space**](GroupApi.md#group_join_space) | **POST** /groups/{id}/spaces/join | Join space by group
[**group_leave_cluster**](GroupApi.md#group_leave_cluster) | **DELETE** /groups/{id}/clusters/{cid} | Leave cluster
[**group_leave_handle**](GroupApi.md#group_leave_handle) | **DELETE** /groups/{id}/handles/{hid} | Group leave handle
[**group_leave_handle_service**](GroupApi.md#group_leave_handle_service) | **DELETE** /groups/{id}/handle_services/{hsid} | Group leave handle service
[**join_parent_group**](GroupApi.md#join_parent_group) | **POST** /groups/{id}/parents/join | Join parent group
[**leave_parent_group**](GroupApi.md#leave_parent_group) | **DELETE** /groups/{id}/parents/{pid} | Leave parent group
[**list_child_group_privileges**](GroupApi.md#list_child_group_privileges) | **GET** /groups/{id}/children/{cid}/privileges | List child&#x27;s group privileges
[**list_child_groups**](GroupApi.md#list_child_groups) | **GET** /groups/{id}/children | Get child groups
[**list_effective_child_group_privileges**](GroupApi.md#list_effective_child_group_privileges) | **GET** /groups/{id}/effective_children/{cid}/privileges | List effective child&#x27;s group privileges
[**list_effective_group_handle_services**](GroupApi.md#list_effective_group_handle_services) | **GET** /groups/{id}/effective_handle_services | List effective group handle services
[**list_effective_group_handles**](GroupApi.md#list_effective_group_handles) | **GET** /groups/{id}/effective_handles | List effective group handles
[**list_effective_group_harvesters**](GroupApi.md#list_effective_group_harvesters) | **GET** /groups/{id}/effective_harvesters | List effective group&#x27;s harvesters
[**list_effective_group_providers**](GroupApi.md#list_effective_group_providers) | **GET** /groups/{id}/effective_providers | List effective group&#x27;s providers
[**list_effective_group_spaces**](GroupApi.md#list_effective_group_spaces) | **GET** /groups/{id}/effective_spaces | List effective group&#x27;s spaces
[**list_effective_group_users**](GroupApi.md#list_effective_group_users) | **GET** /groups/{id}/effective_users | List effective group users
[**list_effective_parent_groups**](GroupApi.md#list_effective_parent_groups) | **GET** /groups/{id}/effective_parents | List effective parent groups
[**list_effective_user_group_privileges**](GroupApi.md#list_effective_user_group_privileges) | **GET** /groups/{id}/effective_users/{uid}/privileges | List effective user&#x27;s group privileges
[**list_group_admin_privileges**](GroupApi.md#list_group_admin_privileges) | **GET** /groups/{id}/privileges | List group&#x27;s admin privileges
[**list_group_clusters**](GroupApi.md#list_group_clusters) | **GET** /groups/{id}/clusters | List group&#x27;s clusters
[**list_group_effective_admin_privileges**](GroupApi.md#list_group_effective_admin_privileges) | **GET** /groups/{id}/effective_privileges | List group&#x27;s effective admin privileges
[**list_group_effective_clusters**](GroupApi.md#list_group_effective_clusters) | **GET** /groups/{id}/effective_clusters | List group&#x27;s effective clusters
[**list_group_handle_services**](GroupApi.md#list_group_handle_services) | **GET** /groups/{id}/handle_services | List group handle services
[**list_group_handles**](GroupApi.md#list_group_handles) | **GET** /groups/{id}/handles | List group handles
[**list_group_harvesters**](GroupApi.md#list_group_harvesters) | **GET** /groups/{id}/harvesters | List group&#x27;s harvesters
[**list_group_privileges**](GroupApi.md#list_group_privileges) | **GET** /groups/privileges | List all group privileges
[**list_group_spaces**](GroupApi.md#list_group_spaces) | **GET** /groups/{id}/spaces | List group&#x27;s spaces
[**list_group_users**](GroupApi.md#list_group_users) | **GET** /groups/{id}/users | List group users
[**list_groups**](GroupApi.md#list_groups) | **GET** /groups | List all groups
[**list_parent_groups**](GroupApi.md#list_parent_groups) | **GET** /groups/{id}/parents | List parent groups
[**list_user_group_privileges**](GroupApi.md#list_user_group_privileges) | **GET** /groups/{id}/users/{uid}/privileges | List user&#x27;s group privileges
[**modify_group**](GroupApi.md#modify_group) | **PATCH** /groups/{id} | Modify group details
[**remove_child_group**](GroupApi.md#remove_child_group) | **DELETE** /groups/{id}/children/{cid} | Remove child group
[**remove_group**](GroupApi.md#remove_group) | **DELETE** /groups/{id} | Remove group
[**remove_group_admin_privileges**](GroupApi.md#remove_group_admin_privileges) | **DELETE** /groups/{id}/privileges | Remove group&#x27;s admin privileges
[**remove_group_from_harvester**](GroupApi.md#remove_group_from_harvester) | **DELETE** /groups/{id}/harvesters/{hid} | Remove group from harvester
[**remove_group_from_space**](GroupApi.md#remove_group_from_space) | **DELETE** /groups/{id}/spaces/{sid} | Remove group from space
[**remove_group_user**](GroupApi.md#remove_group_user) | **DELETE** /groups/{id}/users/{uid} | Remove user from group
[**update_child_group_privileges**](GroupApi.md#update_child_group_privileges) | **PATCH** /groups/{id}/children/{cid}/privileges | Update child&#x27;s group privileges
[**update_group_admin_privileges**](GroupApi.md#update_group_admin_privileges) | **PATCH** /groups/{id}/privileges | Update group&#x27;s admin privileges
[**update_user_group_privileges**](GroupApi.md#update_user_group_privileges) | **PATCH** /groups/{id}/users/{uid}/privileges | Update user&#x27;s group privileges

# **add_child_group**
> add_child_group(id, cid, body=body)

Add child group

Adds group {cid} as child group of group {id}. Optional privileges can be passed in the request body, otherwise default privileges will be set for the child group in this group.  This operation requires `group_add_child` privilege in the parent group and `group_add_parent` privilege in the child group. If `privileges` are specified in the request, `group_set_privileges` privilege is also required.  For administrator who does not belong to those groups, `oz_groups_add_relationships` privilege is required, and `oz_groups_set_privileges` if `privileges` are specified in the request.  ***Example cURL requests***  **Add child group** ```bash curl -u username:password -X PUT \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/children/$CHILD_GROUP_ID ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
cid = 'cid_example' # str | Child group Id.
body = onezone_client.ChildrenCidBody() # ChildrenCidBody |  (optional)

try:
    # Add child group
    api_instance.add_child_group(id, cid, body=body)
except ApiException as e:
    print("Exception when calling GroupApi->add_child_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **cid** | **str**| Child group Id. | 
 **body** | [**ChildrenCidBody**](ChildrenCidBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_group_handle_service**
> add_group_handle_service(body, id)

Create a new handle service for given group.

Creates a new handle service for group.  This operation requires `group_create_handle_service` privilege and `oz_handle_services_create` admin privilege. For administrator who does not belong to this group `oz_handle_services_create` and `oz_groups_add_relationships` privileges are required.  ***Example cURL requests***  **Add group handle services** ```bash curl -u username:password -X POST -H \"Content-type: application/json\" \\ -d '{ ... }' https://$ZONE_HOST/api/v3/onezone/groups/4ebd9efd1e67f6c18695db1d762a914a/handle_services ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
body = onezone_client.HandleServiceCreateRequest() # HandleServiceCreateRequest | 
id = 'id_example' # str | Group Id.

try:
    # Create a new handle service for given group.
    api_instance.add_group_handle_service(body, id)
except ApiException as e:
    print("Exception when calling GroupApi->add_group_handle_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HandleServiceCreateRequest**](HandleServiceCreateRequest.md)|  | 
 **id** | **str**| Group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_group_user**
> add_group_user(id, uid, body=body)

Add user to group

Adds user {uid} as member of group {id}. Optional privileges can be passed in the request body, otherwise default privileges will be set for the user in this group.  This operation can only be invoked by the user {uid} to add himself to the group (if he is not a member already) and requires `group_add_user` privilege in the group. If `privileges` are specified in the request, `group_set_privileges` privilege is also required.  Administrators having the `oz_groups_add_relationships` and `oz_users_add_relationships` admin privileges can add any user to any group, though `oz_groups_set_privileges` privilege is required if `privileges` are specified in the request.  ***Example cURL requests***  **Generate user group invite token** ```bash curl -u admin:password -X PUT \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/users/$USER_ID ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
uid = 'uid_example' # str | User Id.
body = onezone_client.UsersUidBody() # UsersUidBody |  (optional)

try:
    # Add user to group
    api_instance.add_group_user(id, uid, body=body)
except ApiException as e:
    print("Exception when calling GroupApi->add_group_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **uid** | **str**| User Id. | 
 **body** | [**UsersUidBody**](UsersUidBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_child_group**
> create_child_group(body, id)

Create child group

Creates a new child group belonging to the group of {id}.  This operation requires `group_add_child` privilege. For administrator who does not belong to this group `oz_groups_add_relationships` and `oz_groups_create` privileges are required.  ***Example cURL requests***  **Create child group** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/children ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
body = onezone_client.GroupCreateRequest() # GroupCreateRequest | Group properties.
id = 'id_example' # str | Group Id.

try:
    # Create child group
    api_instance.create_child_group(body, id)
except ApiException as e:
    print("Exception when calling GroupApi->create_child_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupCreateRequest**](GroupCreateRequest.md)| Group properties. | 
 **id** | **str**| Group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_child_group_token**
> GroupInviteToken create_child_group_token(id)

Create child group invitation token

This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token that can be used to add a group as child group of group with {id}.  This operation requires `group_add_child` privilege. For administrator who does not belong to this group `oz_groups_add_relationships` privilege is required.  ***Example cURL requests***  **Create invitation token for child group** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID  {   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaWVyIZdrenY00SX\" } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # Create child group invitation token
    api_response = api_instance.create_child_group_token(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->create_child_group_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**GroupInviteToken**](GroupInviteToken.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> create_group(body)

Create new group

Creates a new group.  This operation requires `oz_groups_create` privilege.    See also:   [Create a new group for the current user](#operation/create_group_for_user)   [Create a new parent group for given group](#operation/create_parent_group)    ***Example cURL requests***  **Create new group of type `team`** ```bash  curl -u username:password -H \"Content-type: application/json\" \\  -X POST -d '{ \"name\":\"new_group\" , \"type\":\"team\" }' \\  https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
body = onezone_client.GroupCreateRequest() # GroupCreateRequest | Group properties.

try:
    # Create new group
    api_instance.create_group(body)
except ApiException as e:
    print("Exception when calling GroupApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupCreateRequest**](GroupCreateRequest.md)| Group properties. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group_handle**
> create_group_handle(body, id)

Create a new handle for given group

Creates a new handle on behalf of a group.  This operation requires `group_create_handle` privilege in the group and `handle_service_register_handle` privilege in the handle service specified in the `handleServiceId` field.   For administrator who does not belong to this group `oz_groups_add_relationships` and `oz_handles_create` privilege is required.   ***Example cURL requests***  **Create new group handle** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"handleServiceId\": \"ddb06ed993bae95f2f430664fff122f7\", \"resourceType\": \"Share\", \"resourceId\": \"4fa683cbda8d8f686d15d42720af431d\", \"metadata\": \"<?xml version=\\'1.0\\'?>...\" }' https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/handles ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
body = onezone_client.HandleRegistrationRequest() # HandleRegistrationRequest | New handle parameters.
id = 'id_example' # str | Group Id.

try:
    # Create a new handle for given group
    api_instance.create_group_handle(body, id)
except ApiException as e:
    print("Exception when calling GroupApi->create_group_handle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HandleRegistrationRequest**](HandleRegistrationRequest.md)| New handle parameters. | 
 **id** | **str**| Group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_harvester_for_group**
> create_harvester_for_group(body, id)

Create a new harvester for given group

Creates a new harvester for a specific group.  This operation requires `group_add_harvester` privilege. For administrator who does not belong to this group `oz_groups_add_relationships` and `oz_harvesters_create` privileges are required.  ***Example cURL requests***  **Create new harvester for group** ```bash curl -u admin:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"name\" : \"new_harvester\", \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\", \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\"  \\ \"config\" : { \"typeMapping\": [ { \"id\": 0, \"name\": \"Type 1\" }, { \"id\": 1, \"name\": \"Type 1\" } ],              \"externalHelpLink\": \"http://example.com/some_help_page\",              \"refreshDataTimeout\": 1000 }, \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/harvesters ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
body = onezone_client.HarvesterCreateRequest() # HarvesterCreateRequest | Harvester properties.
id = 'id_example' # str | Group Id.

try:
    # Create a new harvester for given group
    api_instance.create_harvester_for_group(body, id)
except ApiException as e:
    print("Exception when calling GroupApi->create_harvester_for_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HarvesterCreateRequest**](HarvesterCreateRequest.md)| Harvester properties. | 
 **id** | **str**| Group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_parent_group**
> create_parent_group(body, id)

Create a new parent group for given group

Creates a new group for the current group. The group automatically becomes a member of this group.  This operation requires `group_add_parent` privilege. For administrator who does not belong to this group `oz_groups_add_relationships` and `oz_groups_create` privileges are required.  ***Example cURL requests***  **Create new group** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"name\" : \"test_group\" , \"type\" : \"team\" }' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/parents ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
body = onezone_client.Group() # Group | New group parameters.
id = 'id_example' # str | Group Id.

try:
    # Create a new parent group for given group
    api_instance.create_parent_group(body, id)
except ApiException as e:
    print("Exception when calling GroupApi->create_parent_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Group**](Group.md)| New group parameters. | 
 **id** | **str**| Group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_space_for_group**
> create_space_for_group(id, body=body)

Create a new space for given group

Creates a new space for a specific group.  This operation requires `group_add_space` privilege. For administrator who does not belong to this group `oz_groups_add_relationships` and `oz_spaces_create` privileges are required.  ***Example cURL requests***  **Create new space for group** ```bash curl -u admin:password -H \"Content-type: application/json\" \\ -X POST -d '{\"name\": \"new_space\"}' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/spaces ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
body = onezone_client.IdSpacesBody() # IdSpacesBody |  (optional)

try:
    # Create a new space for given group
    api_instance.create_space_for_group(id, body=body)
except ApiException as e:
    print("Exception when calling GroupApi->create_space_for_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **body** | [**IdSpacesBody**](IdSpacesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_group_invite_token**
> GroupInviteToken create_user_group_invite_token(id)

Create user invite token for group

This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token allowing new user to join the group.  This operation requires `group_add_user` privilege. For administrator who does not belong to this group `oz_groups_add_relationships` privilege is required.  ***Example cURL requests***  **Generate user group invite token** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/users/token  {   \"token\": \"MDAxNmxvY2F00aW9uIHJlZlFTUbnZpdGVthHo8xmai4RqqBO2MZM00mrYGgo\" } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # Create user invite token for group
    api_response = api_instance.create_user_group_invite_token(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->create_user_group_invite_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**GroupInviteToken**](GroupInviteToken.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_child_group**
> Group get_child_group(id, cid)

Get child group details

Returns information about a specific child group.  This operation requires `group_view` privilege. For administrator who does not belong to this group  `oz_groups_view` privilege is required.  ***Example cURL requests***  **Get child group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/children/$CHILD_GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_group1\",   \"type\": \"team\" } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
cid = 'cid_example' # str | Child group Id.

try:
    # Get child group details
    api_response = api_instance.get_child_group(id, cid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_child_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **cid** | **str**| Child group Id. | 

### Return type

[**Group**](Group.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_child_group**
> Group get_effective_child_group(id, cid)

Get effective child group details

Returns information about a specific effective child group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_view` privilege is required.  ***Example cURL requests***  **Get effective child details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_children/$CHILD_GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_group1\",   \"type\": \"team\" } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
cid = 'cid_example' # str | Effective child group Id.

try:
    # Get effective child group details
    api_response = api_instance.get_effective_child_group(id, cid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_effective_child_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **cid** | **str**| Effective child group Id. | 

### Return type

[**Group**](Group.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_child_group_membership_intermediaries**
> MembershipIntermediaries get_effective_child_group_membership_intermediaries(id, cid)

Get effective child's group membership intermediaries

Returns the effective child's (`{cid}`) group membership intermediaries - entities from which the child inherits access to the group (`{id}`). Special keyword `\"self\"` in entity id indicates that the child (`{cid}`) has a direct access to the group (`{id}`).  This operation requires any of the following authentication: * as user who is an effective member of the child group (`{cid}`), * as user who has `group_view` privilege in the group (`{id}`), * as user who has `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get effective child's group membership intermediaries** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_children/$CHILD_GROUP_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"group\", \"id\": \"self\"}   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
cid = 'cid_example' # str | Child Id.

try:
    # Get effective child's group membership intermediaries
    api_response = api_instance.get_effective_child_group_membership_intermediaries(id, cid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_effective_child_group_membership_intermediaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **cid** | **str**| Child Id. | 

### Return type

[**MembershipIntermediaries**](MembershipIntermediaries.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_children_groups**
> Groups get_effective_children_groups(id)

Get effective child groups

Returns the list of effective child groups of a specific group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get effective child groups** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_children  {   \"groups\": [] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # Get effective child groups
    api_response = api_instance.get_effective_children_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_effective_children_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**Groups**](Groups.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_group_handle**
> Handle get_effective_group_handle(id, hid)

Get effective group handle details

Returns the details of a specific effective handle.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_handles_view` privilege is required.  ***Example cURL requests***  **Get effective handle details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_handles/$HANDLE_ID  {   \"publicHandle\": \"10.5072/w95Zlng\",   \"handleId\": \"95b663a6467c72ab1256865efef9e387\",   \"handleServiceId\": \"97c27230017cd54c1220189e357322c4\",   \"resourceType\": \"Share\",   \"resourceId\": \"d6ee1aecf03b23f09756d6a49e435455\",   \"metadata\": \"<?xml version=\\\"1.0\\\"?>       <!DOCTYPE rdf:RDF SYSTEM \\\\\"http://dublincore.org/2000/12/01-dcmes-xml-dtd.dtd\\\">       <rdf:RDF xmlns:rdf=\\\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\\\"                xmlns:dc=\\\"http://purl.org/dc/elements/1.1/\\\">         <rdf:Description rdf:about=\\\"http://example.com/resouces/1\\\">           <dc:title>Example Resource</dc:title>           <dc:creator>John Doe</dc:creator>           <dc:publisher>MIT</dc:publisher>           <dc:date>2000-06-06</dc:date>         </rdf:Description>       </rdf:RDF>\",   \"timestamp\": \"1997-07-16T19:20\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
hid = 'hid_example' # str | Handle Id.

try:
    # Get effective group handle details
    api_response = api_instance.get_effective_group_handle(id, hid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_effective_group_handle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **hid** | **str**| Handle Id. | 

### Return type

[**Handle**](Handle.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_group_harvester**
> Harvester get_effective_group_harvester(id, hid)

Get effective group harvester details

Returns information about a specific effective harvester to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_harvesters_view` privilege is required.  ***Example cURL requests***  **Get group's harvester details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_harvesters/$HARVESTER_ID  {   \"harvesterId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_harvester1\",   \"public\" : true,   \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\",   \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
hid = 'hid_example' # str | Effective harvester Id.

try:
    # Get effective group harvester details
    api_response = api_instance.get_effective_group_harvester(id, hid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_effective_group_harvester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **hid** | **str**| Effective harvester Id. | 

### Return type

[**Harvester**](Harvester.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_group_space**
> Space get_effective_group_space(id, sid)

Get effective group space details

Returns information about a specific effective space to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_spaces_view` privilege is required.  ***Example cURL requests***  **Get group's space details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_spaces/$SPACE_ID  {   \"spaceId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_space1\",   \"providers\": {     \"296ebe3c20e9666dc489b647f8647f12\" : 5368709120   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebfc1a770c3\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
sid = 'sid_example' # str | Effective space Id.

try:
    # Get effective group space details
    api_response = api_instance.get_effective_group_space(id, sid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_effective_group_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **sid** | **str**| Effective space Id. | 

### Return type

[**Space**](Space.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_group_user**
> User get_effective_group_user(id, uid)

Get effective group user details

Returns information about a specific effective group user.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_users_view` privilege is required.  ***Example cURL requests***  **Get group user details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\", } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
uid = 'uid_example' # str | User Id.

try:
    # Get effective group user details
    api_response = api_instance.get_effective_group_user(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_effective_group_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**User**](User.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_parent_group**
> Group get_effective_parent_group(id, pid)

Get effective parent group details

Returns details about a specific effective parent group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_view` privilege is required.  ***Example cURL requests***  **Get effective parent group details** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_parents/$PARENT_GROUP_ID  {   \"groupId\": \"9OqgExw00RwaU2MXT51\",   \"name\": \"Group1\",   \"type\": \"organization\" } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
pid = 'pid_example' # str | Effective parent group Id.

try:
    # Get effective parent group details
    api_response = api_instance.get_effective_parent_group(id, pid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_effective_parent_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **pid** | **str**| Effective parent group Id. | 

### Return type

[**Group**](Group.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_user_group_membership_intermediaries**
> MembershipIntermediaries get_effective_user_group_membership_intermediaries(id, uid)

Get effective user's group membership intermediaries

Returns the effective user's (`{uid}`) group membership intermediaries - entities from which the user inherits access to the group (`{id}`). Special keyword `\"self\"` in entity id indicates that the user (`{uid}`) has a direct access to the group (`{id}`).  This operation requires any of the following authentication: * as user (`{uid}`) who is an effective member of the group (`{id}`), * as user who has `group_view` privilege in the group (`{id}`), * as user who has `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get effective user's group membership intermediaries** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_users/$USER_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"group\", \"id\": \"self\"}   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
uid = 'uid_example' # str | User Id.

try:
    # Get effective user's group membership intermediaries
    api_response = api_instance.get_effective_user_group_membership_intermediaries(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_effective_user_group_membership_intermediaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**MembershipIntermediaries**](MembershipIntermediaries.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> Group get_group(id)

Get group details

Returns the information about a specific group.  This operation requires membership in the group or `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID  {   \"groupId\": \"a4d3bc73aada63052310652d421609f1\",   \"name\": \"Test group\",   \"type\": \"team\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # Get group details
    api_response = api_instance.get_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**Group**](Group.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_cluster**
> Cluster get_group_cluster(id, cid)

Get group's cluster details

Returns the details of a specific group's cluster.  This operation can be invoked on behalf of the current group only.  ***Example cURL requests***  **Get group's cluster details** ```bash curl -u groupname:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/group/clusters/$CLUSTER_ID  {   \"clusterId\": \"f8d843beda24e54545455ecc0f4b8886\",   \"type\": \"oneprovider\",   \"workerVersion\": {     \"release\": \"21.02.3\",     \"build\": \"1-gfabf02d\",     \"gui\": \"129c549fbe9b3e730c3d9910492228566e39e1236945766a74381405cc57fb04\"   },   \"onepanelVersion\": {     \"release\": \"21.02.3\",     \"build\": \"3-89fc6bad\",     \"gui\": \"68e7e1472adb719ddf2d88908775091dfb10e5d0b916f06125ea1af4056044e3\"   },   \"online\": true,   \"onepanelProxy\": false,   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
cid = 'cid_example' # str | Cluster Id.

try:
    # Get group's cluster details
    api_response = api_instance.get_group_cluster(id, cid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **cid** | **str**| Cluster Id. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_effective_cluster**
> Cluster get_group_effective_cluster(id, cid)

Get group's effective cluster details

Returns information about a specific effective cluster to which the group belongs.  This operation can be invoked on behalf of the current group only.  ***Example cURL requests***  **Get group's effective cluster details** ```bash curl -u groupname:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/group/clusters/$CLUSTER_ID  {   \"clusterId\": \"f8d843beda24e54545455ecc0f4b8886\",   \"type\": \"oneprovider\",   \"workerVersion\": {     \"release\": \"21.02.3\",     \"build\": \"1-gfabf02d\",     \"gui\": \"129c549fbe9b3e730c3d9910492228566e39e1236945766a74381405cc57fb04\"   },   \"onepanelVersion\": {     \"release\": \"21.02.3\",     \"build\": \"3-89fc6bad\",     \"gui\": \"68e7e1472adb719ddf2d88908775091dfb10e5d0b916f06125ea1af4056044e3\"   },   \"online\": true,   \"onepanelProxy\": false,   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
cid = 'cid_example' # str | Cluster Id.

try:
    # Get group's effective cluster details
    api_response = api_instance.get_group_effective_cluster(id, cid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_effective_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **cid** | **str**| Cluster Id. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_effective_handle_service**
> HandleService get_group_effective_handle_service(id, hsid)

Get effective group handle service details

Returns the details of a specific effective handle service.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_handle_services_view` privilege is required.  ***Example cURL requests***  **Get effective handle service details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_handle_services/$HANDLE_SERVICE_ID  {   \"handleServiceId\": \"0fe7c8a20ffdf07480c46f084bc3b8d5\",   \"name\": \"MyCommunity Handle service\",   \"proxyEndpoint\": \"https://localhost:17000/handle_proxy\",   \"serviceProperties\": {     \"allowTemplateOverride\": false,     \"doiEndpoint\": \"/doi\",     \"host\": \"https://mds.test.datacite.org\",     \"identifierTemplate\": \"{{space.name}}-{{space.guid}}\",     \"mediaEndpoint\": \"/media\",     \"metadataEndpoint\": \"/metadata\",     \"password\": \"pa$$word\",     \"prefix\": 10.5072,     \"type\": \"DOI\",     \"username\": \"alice\"   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
hsid = 'hsid_example' # str | Handle service Id.

try:
    # Get effective group handle service details
    api_response = api_instance.get_group_effective_handle_service(id, hsid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_effective_handle_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **hsid** | **str**| Handle service Id. | 

### Return type

[**HandleService**](HandleService.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_effective_provider**
> ProviderDetails get_group_effective_provider(id, pid)

Get group's effective provider details

Returns information about a specific effective provider for the group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_providers_view` privilege is required.  ***Example cURL requests***  **Get group's effective provider details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_providers/$PROVIDER_ID  {   \"providerId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"name\": \"Example provider\",   \"domain\": \"provider1.example.com\",   \"latitude\": 50.0647,   \"longitude\": 19.945,   \"clusterId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"online\": true,   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
pid = 'pid_example' # str | Effective provider Id.

try:
    # Get group's effective provider details
    api_response = api_instance.get_group_effective_provider(id, pid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_effective_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **pid** | **str**| Effective provider Id. | 

### Return type

[**ProviderDetails**](ProviderDetails.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_handle**
> Handle get_group_handle(id, hid)

Get group handle details

Returns the details of a specific handle.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_handles_view` privilege is required.  ***Example cURL requests***  **Get handle details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/handles/$HANDLE_ID  {   \"publicHandle\": \"10.5072/w95Zlng\",   \"handleId\": \"95b663a6467c72ab1256865efef9e387\",   \"handleServiceId\": \"97c27230017cd54c1220189e357322c4\",   \"resourceType\": \"Share\",   \"resourceId\": \"d6ee1aecf03b23f09756d6a49e435455\",   \"metadata\": \"<?xml version=\\\"1.0\\\"?>       <!DOCTYPE rdf:RDF SYSTEM \\\\\"http://dublincore.org/2000/12/01-dcmes-xml-dtd.dtd\\\">       <rdf:RDF xmlns:rdf=\\\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\\\"                xmlns:dc=\\\"http://purl.org/dc/elements/1.1/\\\">         <rdf:Description rdf:about=\\\"http://example.com/resouces/1\\\">           <dc:title>Example Resource</dc:title>           <dc:creator>John Doe</dc:creator>           <dc:publisher>MIT</dc:publisher>           <dc:date>2000-06-06</dc:date>         </rdf:Description>       </rdf:RDF>\",   \"timestamp\": \"1997-07-16T19:20\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
hid = 'hid_example' # str | Handle Id.

try:
    # Get group handle details
    api_response = api_instance.get_group_handle(id, hid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_handle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **hid** | **str**| Handle Id. | 

### Return type

[**Handle**](Handle.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_handle_service**
> HandleService get_group_handle_service(id, hsid)

Get group handle service details

Returns the details of a specific handle service.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_handle_services_view` privilege is required.  ***Example cURL requests***  **Get handle service details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/handle_services/$HANDLE_SERVICE_ID  {   \"name\": \"MyCommunity Handle service\",   \"handleServiceId\": \"0fe7c8a20ffdf07480c46f084bc3b8d5\",   \"proxyEndpoint\": \"https://localhost:17000/handle_proxy\",   \"serviceProperties\": {     \"allowTemplateOverride\": false,     \"doiEndpoint\": \"/doi\",     \"host\": \"https://mds.test.datacite.org\",     \"identifierTemplate\": \"{{space.name}}-{{space.guid}}\",     \"mediaEndpoint\": \"/media\",     \"metadataEndpoint\": \"/metadata\",     \"password\": \"pa$$word\",     \"prefix\": 10.5072,     \"type\": \"DOI\",     \"username\": \"alice\"   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
hsid = 'hsid_example' # str | Handle service Id.

try:
    # Get group handle service details
    api_response = api_instance.get_group_handle_service(id, hsid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_handle_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **hsid** | **str**| Handle service Id. | 

### Return type

[**HandleService**](HandleService.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_harvester**
> Harvester get_group_harvester(id, hid)

Get group's harvester details

Returns information about a specific harvester to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_harvesters_view` privilege is required.  ***Example cURL requests***  **Get group's harvester details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/harvesters/$HARVESTER_ID  {   \"harvesterId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_harvester1\",   \"public\" : true,   \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\",   \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
hid = 'hid_example' # str | Harvester Id.

try:
    # Get group's harvester details
    api_response = api_instance.get_group_harvester(id, hid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_harvester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **hid** | **str**| Harvester Id. | 

### Return type

[**Harvester**](Harvester.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_space**
> Space get_group_space(id, sid)

Get group's space details

Returns information about a specific space to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_spaces_view` privilege is required.  ***Example cURL requests***  **Get group's space details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/spaces/$SPACE_ID  {   \"spaceId\": \"7e1af0c5f0bfdfe9d2e7edb731247f5f\",   \"name\": \"Personal space\",   \"providers\": {     \"296ebe3c20e9666dc489b647f8647f12\" : 5368709120   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebfc1a770c3\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
sid = 'sid_example' # str | Space Id.

try:
    # Get group's space details
    api_response = api_instance.get_group_space(id, sid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **sid** | **str**| Space Id. | 

### Return type

[**Space**](Space.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_spaces_in_effective_provider**
> ProviderDetails get_group_spaces_in_effective_provider(id, pid)

Get group's spaces that are supported by given effective provider

Returns the list of group's spaces that are supported by given effective provider.  This operation requires `group_view` privilege.  ***Example cURL requests***  **Get groups's spaces supported by effective provider** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_providers/$PROVIDER_ID/spaces  {   \"spaces\": [     \"6825604b0eb6a47b8b7a04b6369eb24d\"   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
pid = 'pid_example' # str | Effective provider Id.

try:
    # Get group's spaces that are supported by given effective provider
    api_response = api_instance.get_group_spaces_in_effective_provider(id, pid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_spaces_in_effective_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **pid** | **str**| Effective provider Id. | 

### Return type

[**ProviderDetails**](ProviderDetails.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_user**
> User get_group_user(id, uid)

Get group user details

Returns basic information about a user {uid} in group {id}.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_users_view` privilege is required.  ***Example cURL requests***  **Generate user group invite token** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\", } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
uid = 'uid_example' # str | User Id.

try:
    # Get group user details
    api_response = api_instance.get_group_user(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**User**](User.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parent_group**
> Group get_parent_group(id, pid)

Get parent group details

Returns details about a specific parent group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_view` privilege is required.  ***Example cURL requests***  **Get parent group details** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/parents/$PARENT_GROUP_ID  {   \"groupId\": \"9OqgExw00RwaU2MXT51\",   \"name\": \"Group1\",   \"type\": \"organization\" } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
pid = 'pid_example' # str | Parent group Id.

try:
    # Get parent group details
    api_response = api_instance.get_parent_group(id, pid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_parent_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **pid** | **str**| Parent group Id. | 

### Return type

[**Group**](Group.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_join_cluster**
> group_join_cluster(body, id)

Join group to a cluster

Join an existing cluster using an inivitation token.  ***Example cURL requests***  **Join group to an existing cluster** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"token\" : \"MDAxNmxvY2F00aW9uRVM2TVo5UlZ5cGFjZV9jcmLciFsOgyUkPI3f02le6PM01IX8go\" }'  \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/clusters/join ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
body = onezone_client.ClusterInviteToken() # ClusterInviteToken | Token for joining a cluster.
id = 'id_example' # str | Group Id.

try:
    # Join group to a cluster
    api_instance.group_join_cluster(body, id)
except ApiException as e:
    print("Exception when calling GroupApi->group_join_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterInviteToken**](ClusterInviteToken.md)| Token for joining a cluster. | 
 **id** | **str**| Group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_join_harvester**
> group_join_harvester(id, body=body)

Join harvester by group

Joins the group to an existing harvester based on provided harvester invitation token.  This operation requires `group_add_harvester` privilege. For administrator who does not belong to this group `oz_harvesters_add_relationships` and `oz_groups_add_relationships` privilege is required.  ***Example cURL requests***  **Join group's harvester** ```bash curl -u admin:password -H \"Content-type: application/json\" \\ -d '{\"token\":\"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVuJ3l02U1JXzstRdK00ZHbso02rRcG8bJLAo\"}' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/harvesters/join ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
body = onezone_client.HarvesterInviteToken() # HarvesterInviteToken | Harvester join token. (optional)

try:
    # Join harvester by group
    api_instance.group_join_harvester(id, body=body)
except ApiException as e:
    print("Exception when calling GroupApi->group_join_harvester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **body** | [**HarvesterInviteToken**](HarvesterInviteToken.md)| Harvester join token. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_join_space**
> group_join_space(id, body=body)

Join space by group

Joins the group to an existing space based on provided space invitation token.  This operation requires `group_add_space` privilege. For administrator who does not belong to this group `oz_spaces_add_relationships` and `oz_groups_add_relationships` privilege is required.  ***Example cURL requests***  **Join group's space** ```bash curl -u admin:password -H \"Content-type: application/json\" \\ -d '{\"token\":\"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVuJ3l02U1JXzstRdK00ZHbso02rRcG8bJLAo\"}' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/spaces/join ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
body = onezone_client.SpaceInviteToken() # SpaceInviteToken | Space join token. (optional)

try:
    # Join space by group
    api_instance.group_join_space(id, body=body)
except ApiException as e:
    print("Exception when calling GroupApi->group_join_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **body** | [**SpaceInviteToken**](SpaceInviteToken.md)| Space join token. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_leave_cluster**
> group_leave_cluster(id, cid)

Leave cluster

Removes the groups membership in a specific cluster.  ***Example cURL requests***  **Group leave cluster** ```bash curl -u groupname:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/clusters/$CLUSTER_ID ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
cid = 'cid_example' # str | Cluster Id.

try:
    # Leave cluster
    api_instance.group_leave_cluster(id, cid)
except ApiException as e:
    print("Exception when calling GroupApi->group_leave_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **cid** | **str**| Cluster Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_leave_handle**
> group_leave_handle(id, hid)

Group leave handle

Removes the group's ownership or access to a specific handle.  This operation requires `group_leave_handle` privilege. For administrator who does not belong to this group `oz_groups_remove_relationships` and `oz_handles_remove_relationships` privileges are required.  ***Example cURL requests***  **Delete user space** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/handles/$HANDLE_ID ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
hid = 'hid_example' # str | Handle Id.

try:
    # Group leave handle
    api_instance.group_leave_handle(id, hid)
except ApiException as e:
    print("Exception when calling GroupApi->group_leave_handle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **hid** | **str**| Handle Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_leave_handle_service**
> group_leave_handle_service(id, hsid)

Group leave handle service

Removes the group's ownership or access to a specific handle service.  This operation requires `group_leave_handle_service` privilege. For administrator who does not belong to this group `oz_groups_remove_relationships` and `oz_handle_services_remove_relationships` privilege is required.  ***Example cURL requests***  **Delete user handle service** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/handle_services/$HANDLE_SERVICE_ID ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
hsid = 'hsid_example' # str | Handle service Id.

try:
    # Group leave handle service
    api_instance.group_leave_handle_service(id, hsid)
except ApiException as e:
    print("Exception when calling GroupApi->group_leave_handle_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **hsid** | **str**| Handle service Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_parent_group**
> join_parent_group(id, body=body)

Join parent group

Adds given group as a child group of a specific group based on provided token.  The parent group to which the group will be added is identified from the token (the token is issued in the context of a group).  This operation requires `group_add_parent` privilege. For administrator who does not belong to this group `oz_groups_add_relationships` privilege is required.  ***Example cURL requests***  **Join parent group**  ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d  '{\"token\":\"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaW\"}'  \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/parents/join ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
body = onezone_client.GroupInviteToken() # GroupInviteToken | Group join token. (optional)

try:
    # Join parent group
    api_instance.join_parent_group(id, body=body)
except ApiException as e:
    print("Exception when calling GroupApi->join_parent_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **body** | [**GroupInviteToken**](GroupInviteToken.md)| Group join token. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leave_parent_group**
> leave_parent_group(id, pid)

Leave parent group

Removes the group access to a specific parent group.  This operation requires `group_leave_parent` privilege. For administrator who does not belong to this group `oz_groups_remove_relationships` privilege is required.  ***Example cURL requests***  **Leave parent group as group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/parents/$PARENT_GROUP_ID ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
pid = 'pid_example' # str | Parent group Id.

try:
    # Leave parent group
    api_instance.leave_parent_group(id, pid)
except ApiException as e:
    print("Exception when calling GroupApi->leave_parent_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **pid** | **str**| Parent group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_child_group_privileges**
> InlineResponse2005 list_child_group_privileges(id, cid)

List child's group privileges

Returns the list of child group's (`{cid}`) privileges in a group (`{id}`).  This operation requires `group_view_privileges` privilege. For administrator who does not belong to this group `oz_groups_view_privileges` privilege is required.  ***Example cURL requests***  **List child group's privileges in a group** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/children/$CHILD_GROUP_ID/privileges  {   \"privileges\": [     \"group_view\",     \"group_update\",     \"group_delete\",     \"group_view_privileges\",     \"group_set_privileges\"   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
cid = 'cid_example' # str | Child group Id.

try:
    # List child's group privileges
    api_response = api_instance.list_child_group_privileges(id, cid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_child_group_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **cid** | **str**| Child group Id. | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_child_groups**
> Groups list_child_groups(id)

Get child groups

Returns the list of child groups of a specific group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get child groups** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/children  {   \"groups\": [] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # Get child groups
    api_response = api_instance.list_child_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_child_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**Groups**](Groups.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_child_group_privileges**
> InlineResponse2005 list_effective_child_group_privileges(id, cid)

List effective child's group privileges

Returns the list of effective child group's (`{cid}`) privileges in a group (`{id}`).  Effective privileges are a sum of child group's privileges and privileges inherited from its parent group memberships.  This operation requires `group_view_privileges` privilege. For administrator who does not belong to this group `oz_groups_view_privileges` privilege is required.  ***Example cURL requests***  **List effective child group's privileges in a group** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_children/$CHILD_GROUP_ID/privileges  {   \"privileges\": [     \"group_view\",     \"group_update\",     \"group_delete\",     \"group_view_privileges\",     \"group_set_privileges\"   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
cid = 'cid_example' # str | Effective child group Id.

try:
    # List effective child's group privileges
    api_response = api_instance.list_effective_child_group_privileges(id, cid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_effective_child_group_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **cid** | **str**| Effective child group Id. | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_group_handle_services**
> HandleServices list_effective_group_handle_services(id)

List effective group handle services

Returns the list of registered group effective handle services.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group effective handle services** ```bash curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_handle_services  {   \"handle_services\": [     \"95b663a6467c72ab1256865efef9e387\",     \"67222da37f90559bcca1f85edd745e5c\"   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # List effective group handle services
    api_response = api_instance.list_effective_group_handle_services(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_effective_group_handle_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**HandleServices**](HandleServices.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_group_handles**
> Handles list_effective_group_handles(id)

List effective group handles

Returns the list of effective groups' handles.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **List effective group handles** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_handles  {   \"handles\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # List effective group handles
    api_response = api_instance.list_effective_group_handles(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_effective_group_handles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**Handles**](Handles.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_group_harvesters**
> Harvesters list_effective_group_harvesters(id)

List effective group's harvesters

Returns the effective list of harvesters to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group effective harvesters** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_harvesters  {   \"harvesters\": [     \"GVC8lKEasj4q253sptVqF8HwUpk8jrwxKOe45uzLFX2\"   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # List effective group's harvesters
    api_response = api_instance.list_effective_group_harvesters(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_effective_group_harvesters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**Harvesters**](Harvesters.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_group_providers**
> Providers list_effective_group_providers(id)

List effective group's providers

Returns the list of effective providers supporting group spaces.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group effective providers** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_providers ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # List effective group's providers
    api_response = api_instance.list_effective_group_providers(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_effective_group_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**Providers**](Providers.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_group_spaces**
> Spaces list_effective_group_spaces(id)

List effective group's spaces

Returns the list of effective spaces to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group effective spaces** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_spaces  {   \"spaces\": [     \"GVC8lKEasj4q253sptVqF8HwUpk8jrwxKOe45uzLFX2\"   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # List effective group's spaces
    api_response = api_instance.list_effective_group_spaces(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_effective_group_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**Spaces**](Spaces.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_group_users**
> Users list_effective_group_users(id)

List effective group users

Returns the list of effective group users, which includes both who directly belong to the group, as well as users who belong to the group indirectly through its parent groups.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get effective group users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_users  {   \"users\":  [     \"lb0NvUXIVguzjQ3dBOXAyd1c11fWKB5dKJDQ6YvB7a0\"   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # List effective group users
    api_response = api_instance.list_effective_group_users(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_effective_group_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**Users**](Users.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_parent_groups**
> Groups list_effective_parent_groups(id)

List effective parent groups

Returns the effective parent groups of a specific group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get effective parent groups** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_parents  {   \"groups\": [] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # List effective parent groups
    api_response = api_instance.list_effective_parent_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_effective_parent_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**Groups**](Groups.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_user_group_privileges**
> InlineResponse2005 list_effective_user_group_privileges(id, uid)

List effective user's group privileges

Returns the list of effective user's (`{uid}`) privileges in a group (`{id}`).  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation requires `group_view_privileges` privilege. For administrator who does not belong to this group `oz_groups_view_privileges` privilege is required.  ***Example cURL requests***  **List effective user's privileges in a group** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_users/$USER_ID/privileges  {   \"privileges\": [     \"group_view\",     \"group_update\",     \"group_delete\",     \"group_view_privileges\",     \"group_set_privileges\"   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
uid = 'uid_example' # str | User Id.

try:
    # List effective user's group privileges
    api_response = api_instance.list_effective_user_group_privileges(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_effective_user_group_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_admin_privileges**
> InlineResponse2001 list_group_admin_privileges(id)

List group's admin privileges

Returns the list of group's (`{id}`) admin privileges in Onezone.  This operation requires `oz_view_privileges` admin privilege.  ***Example cURL requests***  **List group's admin privileges in Onezone** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/privileges  {   \"privileges\": [     \"oz_view_privileges\",     \"oz_users_list\",     \"oz_users_view\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handles_list\",     \"oz_handles_view\"   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # List group's admin privileges
    api_response = api_instance.list_group_admin_privileges(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_group_admin_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_clusters**
> Clusters list_group_clusters(id)

List group's clusters

Returns the list of clusters to which the group has access.  ***Example cURL requests***  **Get group's clusters** ```bash curl -u groupname:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/group/GVC8lKEasj4q253sptVqF8HwUpk8j/clusters  {   \"clusters\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # List group's clusters
    api_response = api_instance.list_group_clusters(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_group_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**Clusters**](Clusters.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_effective_admin_privileges**
> InlineResponse2001 list_group_effective_admin_privileges(id)

List group's effective admin privileges

Returns the list of group's (`{id}`) effective admin privileges in Onezone.  Effective privileges are a sum of group's privileges and privileges inherited from its parent group memberships.  This operation requires `oz_view_privileges` admin privilege.  ***Example cURL requests***  **List group's effective admin privileges in Onezone** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_privileges  {   \"privileges\": [     \"oz_view_privileges\",     \"oz_users_list\",     \"oz_users_view\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handles_list\",     \"oz_handles_view\"   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # List group's effective admin privileges
    api_response = api_instance.list_group_effective_admin_privileges(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_group_effective_admin_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_effective_clusters**
> Clusters list_group_effective_clusters(id)

List group's effective clusters

Returns the list of effective clusters to which the group has access.  ***Example cURL requests***  **Get group's effective clusters** ```bash curl -u groupname:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_clusters  {   \"clusters\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # List group's effective clusters
    api_response = api_instance.list_group_effective_clusters(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_group_effective_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**Clusters**](Clusters.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_handle_services**
> HandleServices list_group_handle_services(id)

List group handle services

Returns the list of registered group handle services.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group handle services** ```bash curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/handle_services  {   \"handle_services\": [     \"0fe7c8a20ffdf07480c46f084bc3b8d5\",     \"302da048de67e2ea05f0af1d0fe7c8a2\"   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # List group handle services
    api_response = api_instance.list_group_handle_services(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_group_handle_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**HandleServices**](HandleServices.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_handles**
> Handles list_group_handles(id)

List group handles

Returns the list of groups handles.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group handles** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/handles  {   \"handles\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # List group handles
    api_response = api_instance.list_group_handles(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_group_handles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**Handles**](Handles.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_harvesters**
> Harvesters list_group_harvesters(id)

List group's harvesters

Returns the list of harvesters to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group harvesters** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/harvesters  {   \"harvesters\": [     \"GVC8lKEasj4q253sptVqF8HwUpk8jrwxKOe45uzLFX2\"   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # List group's harvesters
    api_response = api_instance.list_group_harvesters(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_group_harvesters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**Harvesters**](Harvesters.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_privileges**
> InlineResponse2004 list_group_privileges()

List all group privileges

Returns list of all possible group privileges.  This endpoint does not require authentication.  ***Example cURL requests***  **Get list of all group privileges** ```bash curl https://$ZONE_HOST/api/v3/onezone/groups/privileges  {   \"admin\": [     \"group_view\",     \"group_update\",     \"group_delete\",     \"group_view_privileges\",     \"group_set_privileges\",     \"group_add_parent\",     \"group_leave_parent\",     \"group_add_child\",     \"group_remove_child\",     \"group_add_user\",     \"group_remove_user\",     \"group_add_space\",     \"group_leave_space\",     \"group_create_handle_service\",     \"group_leave_handle_service\",     \"group_create_handle\",     \"group_leave_handle\",     \"group_add_harvester\",     \"group_remove_harvester\"   ],   \"manager\": [     \"group_view\",     \"group_view_privileges\",     \"group_add_parent\",     \"group_leave_parent\",     \"group_add_child\",     \"group_remove_child\",     \"group_add_user\",     \"group_remove_user\",     \"group_add_harvester\",     \"group_remove_harvester\"   ],   \"member\": [     \"group_view\"   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))

try:
    # List all group privileges
    api_response = api_instance.list_group_privileges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_group_privileges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_spaces**
> Spaces list_group_spaces(id)

List group's spaces

Returns the list of spaces to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group spaces** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/spaces  {   \"spaces\": [     \"GVC8lKEasj4q253sptVqF8HwUpk8jrwxKOe45uzLFX2\"   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # List group's spaces
    api_response = api_instance.list_group_spaces(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_group_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**Spaces**](Spaces.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_users**
> Users list_group_users(id)

List group users

Returns the list of users belonging to a specific group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/users  {   \"users\": [     \"a5b469a2b0516b662a49da74d6d7d7bc\"   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # List group users
    api_response = api_instance.list_group_users(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_group_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**Users**](Users.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_groups**
> Groups list_groups()

List all groups

Returns the list of all groups in the system.  Requires `oz_groups_list` admin privilege.  ***Example cURL requests***  **List all groups in the system** ```bash  curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/groups ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))

try:
    # List all groups
    api_response = api_instance.list_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Groups**](Groups.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_parent_groups**
> Groups list_parent_groups(id)

List parent groups

Returns the parent groups of a specific group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get parent groups** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/parents  {   \"groups\": [] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # List parent groups
    api_response = api_instance.list_parent_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_parent_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

[**Groups**](Groups.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_group_privileges**
> InlineResponse2005 list_user_group_privileges(id, uid)

List user's group privileges

Returns the list of user's (`{uid}`) privileges in a group (`{id}`).  This operation requires `group_view_privileges` privilege. For administrator who does not belong to this group `oz_groups_view_privileges` privilege is required.  ***Example cURL requests***  **List user's privileges in a group** ```bash curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/users/$USER_ID/privileges  {   \"privileges\": [     \"group_view\",     \"group_update\",     \"group_delete\",     \"group_view_privileges\",     \"group_set_privileges\"   ] } ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
uid = 'uid_example' # str | User Id.

try:
    # List user's group privileges
    api_response = api_instance.list_user_group_privileges(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_user_group_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_group**
> modify_group(body, id)

Modify group details

Updates the details about a group.  This operation requires `group_update` privilege. For administrator who does not belong to this group `oz_groups_update` privilege is required.  ***Example cURL requests***  **Modify group name** ```bash curl -u admin:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"name\": \"new_group_name\"}' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
body = onezone_client.GroupUpdateRequest() # GroupUpdateRequest | Group parameters
id = 'id_example' # str | Group Id.

try:
    # Modify group details
    api_instance.modify_group(body, id)
except ApiException as e:
    print("Exception when calling GroupApi->modify_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupUpdateRequest**](GroupUpdateRequest.md)| Group parameters | 
 **id** | **str**| Group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_child_group**
> remove_child_group(id, cid)

Remove child group

Removes a specific child with {cid} from parent group with {id}.  This operation requires `group_remove_child` privilege. For administrator who does not belong to this group `oz_groups_remove_relationships` privilege is required.  ***Example cURL requests***  **Remove child group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/children/$CHILD_GROUP_ID ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
cid = 'cid_example' # str | Child group Id.

try:
    # Remove child group
    api_instance.remove_child_group(id, cid)
except ApiException as e:
    print("Exception when calling GroupApi->remove_child_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **cid** | **str**| Child group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_group**
> remove_group(id)

Remove group

Removes a specific group.  This operation requires `group_delete` privilege. For administrator who does not belong to this group `oz_groups_delete` privilege is required.  ***Example cURL requests***  **Remove group** ```bash curl -u admin:password -X DELETE  \\ https://$ZONE_HOST/api/v3/onezone/user/groups/$GROUP_ID ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # Remove group
    api_instance.remove_group(id)
except ApiException as e:
    print("Exception when calling GroupApi->remove_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_group_admin_privileges**
> remove_group_admin_privileges(id)

Remove group's admin privileges

Removes all group's (`{id}`) admin privileges in Onezone.  This operation requires `oz_set_privileges` admin privilege.  ***Example cURL requests***  **Remove all group's admin privileges in Onezone** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/privileges ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.

try:
    # Remove group's admin privileges
    api_instance.remove_group_admin_privileges(id)
except ApiException as e:
    print("Exception when calling GroupApi->remove_group_admin_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_group_from_harvester**
> remove_group_from_harvester(id, hid)

Remove group from harvester

Removes the group {id} from harvester {hid} (the group will no longer have access to harvester).  This operation requires `group_leave_harvester` privilege. For administrator who does not belong to this group `oz_groups_remove_relationships` and `oz_harvesters_remove_relationships` privileges are required.  ***Example cURL requests***  **Remove harvester from group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/harvesters/$HARVESTER_ID ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
hid = 'hid_example' # str | Harvester Id.

try:
    # Remove group from harvester
    api_instance.remove_group_from_harvester(id, hid)
except ApiException as e:
    print("Exception when calling GroupApi->remove_group_from_harvester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **hid** | **str**| Harvester Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_group_from_space**
> remove_group_from_space(id, sid)

Remove group from space

Removes the group {id} from space {sid} (the group will no longer have access to space).  This operation requires `group_leave_space` privilege. For administrator who does not belong to this group `oz_groups_remove_relationships` and `oz_spaces_remove_relationships` privileges are required.  ***Example cURL requests***  **Remove space from group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/spaces/$SPACE_ID ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
sid = 'sid_example' # str | Space Id.

try:
    # Remove group from space
    api_instance.remove_group_from_space(id, sid)
except ApiException as e:
    print("Exception when calling GroupApi->remove_group_from_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **sid** | **str**| Space Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_group_user**
> remove_group_user(id, uid)

Remove user from group

Removes the user {uid} from a group {id} (the user will no longer have access to spaces accessible to the group).  This operation requires `group_remove_user` privilege. For administrator who does not belong to this group `oz_groups_remove_relationships` and `oz_users_remove_relationships` privileges are required.  ***Example cURL requests***  **Remove user from group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/users/$USER_ID ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Group Id.
uid = 'uid_example' # str | User Id.

try:
    # Remove user from group
    api_instance.remove_group_user(id, uid)
except ApiException as e:
    print("Exception when calling GroupApi->remove_group_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group Id. | 
 **uid** | **str**| User Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_child_group_privileges**
> update_child_group_privileges(body, id, cid)

Update child's group privileges

Updates child group's (`{cid}`) privileges in a group (`{id}`).  This operation requires `group_set_privileges` privilege. For administrator who does not belong to this group `oz_groups_set_privileges` privilege is required.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update child group's privileges in a group** ```bash curl -u username:password -H \"Content-type: application/json\" -X PATCH \\ -d '{\"grant\": [\"group_view\", \"group_update\"], \"revoke\": [\"group_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/children/$CHILD_GROUP_ID/privileges ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
body = onezone_client.GroupPrivilegesUpdate() # GroupPrivilegesUpdate | Group privileges update request.
id = 'id_example' # str | Group Id.
cid = 'cid_example' # str | Child group Id.

try:
    # Update child's group privileges
    api_instance.update_child_group_privileges(body, id, cid)
except ApiException as e:
    print("Exception when calling GroupApi->update_child_group_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupPrivilegesUpdate**](GroupPrivilegesUpdate.md)| Group privileges update request. | 
 **id** | **str**| Group Id. | 
 **cid** | **str**| Child group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_admin_privileges**
> update_group_admin_privileges(body, id)

Update group's admin privileges

Updates group's (`{id}`) admin privileges in Onezone.  This operation requires `oz_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update group's admin privileges in Onezone** ```bash curl -H \"Content-type: application/json\" -X PATCH \\ -d '{\"grant\": [\"oz_spaces_list\"], \"revoke\": [\"oz_groups_update\"]}' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/privileges ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
body = onezone_client.AdminPrivilegesUpdate() # AdminPrivilegesUpdate | admin privileges update request.
id = 'id_example' # str | Group Id.

try:
    # Update group's admin privileges
    api_instance.update_group_admin_privileges(body, id)
except ApiException as e:
    print("Exception when calling GroupApi->update_group_admin_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminPrivilegesUpdate**](AdminPrivilegesUpdate.md)| admin privileges update request. | 
 **id** | **str**| Group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_group_privileges**
> update_user_group_privileges(body, id, uid)

Update user's group privileges

Updates user's (`{uid}`) privileges in a group (`{id}`).  This operation requires `group_set_privileges` privilege. For administrator who does not belong to this group `oz_groups_set_privileges` privilege is required.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update user's privileges in a group** ```bash curl -H \"Content-type: application/json\" -X PATCH \\ -d '{\"grant\": [\"group_view\", \"group_update\"], \"revoke\": [\"group_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/users/$USER_ID/privileges ``` 

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
api_instance = onezone_client.GroupApi(onezone_client.ApiClient(configuration))
body = onezone_client.GroupPrivilegesUpdate() # GroupPrivilegesUpdate | Group privileges update request.
id = 'id_example' # str | Group Id.
uid = 'uid_example' # str | User Id.

try:
    # Update user's group privileges
    api_instance.update_user_group_privileges(body, id, uid)
except ApiException as e:
    print("Exception when calling GroupApi->update_user_group_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupPrivilegesUpdate**](GroupPrivilegesUpdate.md)| Group privileges update request. | 
 **id** | **str**| Group Id. | 
 **uid** | **str**| User Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

