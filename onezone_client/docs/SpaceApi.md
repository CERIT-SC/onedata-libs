# onezone_client.SpaceApi

All URIs are relative to */api/v3/onezone*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group_to_space**](SpaceApi.md#add_group_to_space) | **PUT** /spaces/{id}/groups/{gid} | Add group to space
[**add_space_owner**](SpaceApi.md#add_space_owner) | **PUT** /spaces/{id}/owners/{uid} | Add space owner
[**add_space_user**](SpaceApi.md#add_space_user) | **PUT** /spaces/{id}/users/{uid} | Add user to space
[**cease_support_by_provider**](SpaceApi.md#cease_support_by_provider) | **DELETE** /spaces/{id}/providers/{pid} | Ceases space support by provider
[**create_space**](SpaceApi.md#create_space) | **POST** /spaces | Create new space
[**create_space_group**](SpaceApi.md#create_space_group) | **POST** /spaces/{id}/groups | Create group in space
[**create_space_group_token**](SpaceApi.md#create_space_group_token) | **POST** /spaces/{id}/groups/token | Create space invite token for group
[**create_space_support_token**](SpaceApi.md#create_space_support_token) | **POST** /spaces/{id}/providers/token | Create space support token
[**create_space_user_invite_token**](SpaceApi.md#create_space_user_invite_token) | **POST** /spaces/{id}/users/token | Create space user invite token
[**get_effective_group_space_membership_intermediaries**](SpaceApi.md#get_effective_group_space_membership_intermediaries) | **GET** /spaces/{id}/effective_groups/{gid}/membership | Get effective group&#x27;s space membership intermediaries
[**get_effective_space_group**](SpaceApi.md#get_effective_space_group) | **GET** /spaces/{id}/effective_groups/{gid} | Get effective space group details
[**get_effective_space_user**](SpaceApi.md#get_effective_space_user) | **GET** /spaces/{id}/effective_users/{uid} | Get effective space user details
[**get_effective_user_space_membership_intermediaries**](SpaceApi.md#get_effective_user_space_membership_intermediaries) | **GET** /spaces/{id}/effective_users/{uid}/membership | Get effective user&#x27;s space membership intermediaries
[**get_membership_requester_info**](SpaceApi.md#get_membership_requester_info) | **GET** /spaces/marketplace/{id}/request/{rid}/requester_info | Get membership requester info
[**get_space**](SpaceApi.md#get_space) | **GET** /spaces/{id} | Get space details
[**get_space_data_in_marketplace**](SpaceApi.md#get_space_data_in_marketplace) | **GET** /spaces/marketplace/{id} | Get space details in the Marketplace
[**get_space_group**](SpaceApi.md#get_space_group) | **GET** /spaces/{id}/groups/{gid} | Get space&#x27;s group details
[**get_space_harvester**](SpaceApi.md#get_space_harvester) | **GET** /spaces/{id}/harvesters/{hid} | Get harvester details
[**get_space_provider**](SpaceApi.md#get_space_provider) | **GET** /spaces/{id}/providers/{pid} | Get space provider details
[**get_space_share**](SpaceApi.md#get_space_share) | **GET** /spaces/{id}/shares/{sid} | Get space share
[**get_space_user**](SpaceApi.md#get_space_user) | **GET** /spaces/{id}/users/{uid} | Get space user details
[**list_effective_group_space_privileges**](SpaceApi.md#list_effective_group_space_privileges) | **GET** /spaces/{id}/effective_groups/{gid}/privileges | List effective group&#x27;s space privileges
[**list_effective_space_groups**](SpaceApi.md#list_effective_space_groups) | **GET** /spaces/{id}/effective_groups | List effective space groups
[**list_effective_space_users**](SpaceApi.md#list_effective_space_users) | **GET** /spaces/{id}/effective_users | List effective space users
[**list_effective_user_space_privileges**](SpaceApi.md#list_effective_user_space_privileges) | **GET** /spaces/{id}/effective_users/{uid}/privileges | List effective user&#x27;s space privileges
[**list_group_space_privileges**](SpaceApi.md#list_group_space_privileges) | **GET** /spaces/{id}/groups/{gid}/privileges | List group&#x27;s space privileges
[**list_marketplace**](SpaceApi.md#list_marketplace) | **POST** /spaces/marketplace/list | List the Space Marketplace
[**list_space_groups**](SpaceApi.md#list_space_groups) | **GET** /spaces/{id}/groups | List space groups
[**list_space_harvesters**](SpaceApi.md#list_space_harvesters) | **GET** /spaces/{id}/harvesters | List space harvesters
[**list_space_owners**](SpaceApi.md#list_space_owners) | **GET** /spaces/{id}/owners | List space owners
[**list_space_privileges**](SpaceApi.md#list_space_privileges) | **GET** /spaces/privileges | List all space privileges
[**list_space_providers**](SpaceApi.md#list_space_providers) | **GET** /spaces/{id}/providers | List space providers
[**list_space_shares**](SpaceApi.md#list_space_shares) | **GET** /spaces/{id}/shares | List space shares
[**list_space_users**](SpaceApi.md#list_space_users) | **GET** /spaces/{id}/users | List space users
[**list_spaces**](SpaceApi.md#list_spaces) | **GET** /spaces | List all spaces
[**list_user_space_privileges**](SpaceApi.md#list_user_space_privileges) | **GET** /spaces/{id}/users/{uid}/privileges | List user&#x27;s space privileges
[**modify_space**](SpaceApi.md#modify_space) | **PATCH** /spaces/{id} | Modify space details
[**remove_space**](SpaceApi.md#remove_space) | **DELETE** /spaces/{id} | Remove space
[**remove_space_from_harvester**](SpaceApi.md#remove_space_from_harvester) | **DELETE** /spaces/{id}/harvesters/{hid} | Remove space from harvester.
[**remove_space_group**](SpaceApi.md#remove_space_group) | **DELETE** /spaces/{id}/groups/{gid} | Remove group from space
[**remove_space_owner**](SpaceApi.md#remove_space_owner) | **DELETE** /spaces/{id}/owners/{uid} | Remove space owner
[**remove_space_user**](SpaceApi.md#remove_space_user) | **DELETE** /spaces/{id}/users/{uid} | Remove user from space
[**request_space_membership**](SpaceApi.md#request_space_membership) | **POST** /spaces/marketplace/{id}/request | Request space membership via Marketplace
[**resolve_space_membership_request**](SpaceApi.md#resolve_space_membership_request) | **POST** /spaces/marketplace/{id}/request/{rid}/resolve | Resolve space membership request
[**space_join_harvester**](SpaceApi.md#space_join_harvester) | **POST** /spaces/{id}/harvesters/join | Join space to a harvester
[**update_group_space_privileges**](SpaceApi.md#update_group_space_privileges) | **PATCH** /spaces/{id}/groups/{gid}/privileges | Update group privileges to space
[**update_support_parameters_of_provider**](SpaceApi.md#update_support_parameters_of_provider) | **PATCH** /spaces/{id}/providers/{pid}/support_parameters | Update space support parameters of provider
[**update_user_space_privileges**](SpaceApi.md#update_user_space_privileges) | **PATCH** /spaces/{id}/users/{uid}/privileges | Update user&#x27;s space privileges

# **add_group_to_space**
> add_group_to_space(id, gid, body=body)

Add group to space

Adds group {gid} as member of space {id}. Optional privileges can be passed in the request body, otherwise default privileges will be set for the group in this space.  This operation requires `space_add_group` privilege in the space and `group_add_space` privilege in the group. If `privileges` are specified in the request, `space_set_privileges` privilege is also required.  For administrator who does not belong to the group / space, `oz_groups_add_relationships` and `oz_spaces_add_relationships` privileges are required, and `oz_spaces_set_privileges` if `privileges` are specified in the request.  ***Example cURL requests***  **Add group to space** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\  https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups/$GROUP_ID ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
gid = 'gid_example' # str | Group Id.
body = onezone_client.GroupsGidBody() # GroupsGidBody |  (optional)

try:
    # Add group to space
    api_instance.add_group_to_space(id, gid, body=body)
except ApiException as e:
    print("Exception when calling SpaceApi->add_group_to_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **gid** | **str**| Group Id. | 
 **body** | [**GroupsGidBody**](GroupsGidBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_space_owner**
> add_space_owner(id, uid)

Add space owner

Adds user `{uid}` as an owner of space `{id}`. Ownership can only be granted to effective members of the space - if the desired user is not a member, they have to be added to the space first. If the new owner is only an indirect member (via a group), he is automatically added as a direct member when granted ownership.  Space owners are members of the space (users) that have absolute power regarding the space API and files (analogical to \"root\", but in the scope of one space). Being an owner means that user privileges are essentially ignored and all API operations are allowed.  This operation requires any of the following authentication: * as user who is currently an owner of the space (`{id}`), * as user who has `oz_spaces_set_privileges` admin privilege.  ***Example cURL requests***  **Add space space owner** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/owners/$USER_ID ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
uid = 'uid_example' # str | User Id.

try:
    # Add space owner
    api_instance.add_space_owner(id, uid)
except ApiException as e:
    print("Exception when calling SpaceApi->add_space_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **uid** | **str**| User Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_space_user**
> add_space_user(id, uid, body=body)

Add user to space

Adds user {uid} as member of space {id}. Optional privileges can be passed in the request body, otherwise default privileges will be set for the user in this space.  This operation can only be invoked by the user {uid} to add himself to the space (if he is not a member already) and requires `space_add_user` privilege in the space. If `privileges` are specified in the request, `space_set_privileges` privilege is also required.  Administrators having the `oz_spaces_add_relationships` and `oz_users_add_relationships` admin privileges can add any user to any space, though `oz_spaces_set_privileges` privilege is required if `privileges` are specified in the request.  ***Example cURL requests***  **Add user to space** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/users/$USER_ID ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
uid = 'uid_example' # str | User Id.
body = onezone_client.UsersUidBody1() # UsersUidBody1 |  (optional)

try:
    # Add user to space
    api_instance.add_space_user(id, uid, body=body)
except ApiException as e:
    print("Exception when calling SpaceApi->add_space_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **uid** | **str**| User Id. | 
 **body** | [**UsersUidBody1**](UsersUidBody1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cease_support_by_provider**
> cease_support_by_provider(id, pid)

Ceases space support by provider

Ceases the space's support from given provider. WARNING: this will cause irreversible data loss if the data located in given space on given provider is not replicated beforehand.  This operation requires `space_remove_support` privilege or `oz_spaces_remove_relationships` admin privilege.  ***Example cURL requests***  **Remove space support** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/providers/$PROVIDER_ID ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
pid = 'pid_example' # str | Provider Id.

try:
    # Ceases space support by provider
    api_instance.cease_support_by_provider(id, pid)
except ApiException as e:
    print("Exception when calling SpaceApi->cease_support_by_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **pid** | **str**| Provider Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_space**
> create_space(body=body)

Create new space

Creates new space.  This operation requires `oz_spaces_create` admin privilege.  See also:   [Create a new space for the current user](#operation/create_user_space)   [Create a new space for given group](#operation/create_space_for_group)    ***Example cURL requests***  **Create new space** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"name\" : \"new_space\" }' \\ https://$ZONE_HOST/api/v3/onezone/spaces ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
body = onezone_client.SpacesBody() # SpacesBody | Space creation data. (optional)

try:
    # Create new space
    api_instance.create_space(body=body)
except ApiException as e:
    print("Exception when calling SpaceApi->create_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpacesBody**](SpacesBody.md)| Space creation data. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_space_group**
> create_space_group(body, id)

Create group in space

Creates a new group belonging to the space of {id}.  This operation requires `space_add_group` privilege. For administrator who does not belong to this group `oz_spaces_add_relationships` and `oz_groups_create` privileges are required.  ***Example cURL requests***  **Create group in space** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
body = onezone_client.GroupCreateRequest() # GroupCreateRequest | Group properties.
id = 'id_example' # str | Space Id.

try:
    # Create group in space
    api_instance.create_space_group(body, id)
except ApiException as e:
    print("Exception when calling SpaceApi->create_space_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupCreateRequest**](GroupCreateRequest.md)| Group properties. | 
 **id** | **str**| Space Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_space_group_token**
> SpaceInviteToken create_space_group_token(id)

Create space invite token for group

This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user).  Creates a token allowing to add a group to a specific space.  This operation requires `space_add_group` privilege or `oz_spaces_add_relationships` admin privilege.  ***Example cURL requests***  **Create space invitation token for group** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups/token  {   \"token\": \"MDAxNmxvY0cGUgKWsjcpnrLE00RtOd2F00cGUgKWsjcpnrLE00RtOdhmnQycSICwMsugo\" } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.

try:
    # Create space invite token for group
    api_response = api_instance.create_space_group_token(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->create_space_group_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 

### Return type

[**SpaceInviteToken**](SpaceInviteToken.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_space_support_token**
> SpaceSupportToken create_space_support_token(id)

Create space support token

This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user).  Creates a token which can be submitted to a selected provider in order to add storage support for the space.  This operation requires `space_add_support` privilege or `oz_spaces_add_relationships` admin privilege.  ***Example cURL requests***  **Create space support token** ```bash curl -u admin:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/providers/token  {   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaWVyIHZjUGlIcGkweGZta1ZOdEp00eUNINVNvR2001Wl\" } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.

try:
    # Create space support token
    api_response = api_instance.create_space_support_token(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->create_space_support_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 

### Return type

[**SpaceSupportToken**](SpaceSupportToken.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_space_user_invite_token**
> SpaceInviteToken create_space_user_invite_token(id)

Create space user invite token

This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token allowing new user to join a space.  This operation requires `space_add_user` privilege. For administrators who do not have to be members of this space, `oz_spaces_add_relationships` privilege is required.  ***Example cURL requests***  **Create space user invite token** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/users/token  {   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaWVyIG00zcEJ2UDVuOHhkQUNhdk9hbTlyNnIwNldPSzVhc\" } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.

try:
    # Create space user invite token
    api_response = api_instance.create_space_user_invite_token(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->create_space_user_invite_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 

### Return type

[**SpaceInviteToken**](SpaceInviteToken.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_group_space_membership_intermediaries**
> MembershipIntermediaries get_effective_group_space_membership_intermediaries(id, gid)

Get effective group's space membership intermediaries

Returns the effective group's (`{gid}`) space membership intermediaries - entities from which the group inherits access to the space (`{id}`). Special keyword `\"self\"` in entity id indicates that the group (`{gid}`) has a direct access to the space (`{id}`).  This operation requires any of the following authentication: * as user who is an effective member of the group (`{gid}`), * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space, * as user who has `oz_spaces_view` admin privilege.  ***Example cURL requests***  **Get effective group's space membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_groups/$GROUP_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"space\", \"id\": \"self\"}   ] } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
gid = 'gid_example' # str | Group Id.

try:
    # Get effective group's space membership intermediaries
    api_response = api_instance.get_effective_group_space_membership_intermediaries(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->get_effective_group_space_membership_intermediaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **gid** | **str**| Group Id. | 

### Return type

[**MembershipIntermediaries**](MembershipIntermediaries.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_space_group**
> Group get_effective_space_group(id, gid)

Get effective space group details

Returns details about a specific effective group in a space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get effective space group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_groups/$GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_groupX\",   \"type\": \"team\" } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
gid = 'gid_example' # str | Group Id.

try:
    # Get effective space group details
    api_response = api_instance.get_effective_space_group(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->get_effective_space_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **gid** | **str**| Group Id. | 

### Return type

[**Group**](Group.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_space_user**
> User get_effective_space_user(id, uid)

Get effective space user details

Returns details about a specific effective user in a space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_users_view` admin privilege.  ***Example cURL requests***  **Get effective space user details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_users/$USER_ID  {   \"userId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"fullName\" : \"John Doe\",   \"username\" : \"jodoe\" } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
uid = 'uid_example' # str | User Id.

try:
    # Get effective space user details
    api_response = api_instance.get_effective_space_user(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->get_effective_space_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**User**](User.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_user_space_membership_intermediaries**
> MembershipIntermediaries get_effective_user_space_membership_intermediaries(id, uid)

Get effective user's space membership intermediaries

Returns the effective user's (`{uid}`) space membership intermediaries - entities from which the user inherits access to the space (`{id}`). Special keyword `\"self\"` in entity id indicates that the user (`{uid}`) has a direct access to the space (`{id}`).  This operation requires any of the following authentication: * as user (`{uid}`) who is an effective member of the space (`{id}`), * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_view` admin privilege.  ***Example cURL requests***  **Get effective user's space membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_users/$USER_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"space\", \"id\": \"self\"}   ] } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
uid = 'uid_example' # str | User Id.

try:
    # Get effective user's space membership intermediaries
    api_response = api_instance.get_effective_user_space_membership_intermediaries(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->get_effective_user_space_membership_intermediaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**MembershipIntermediaries**](MembershipIntermediaries.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_membership_requester_info**
> SpaceMembershipRequesterInfo get_membership_requester_info(id, rid)

Get membership requester info

Get requester info for a specific space membership request made via the Marketplace.  This operation requires privilege `space_manage_in_marketplace` or `oz_spaces_view` admin privilege.  ***Example cURL requests***  **Get space membership requester info** ```bash curl -u admin:password -H \"Content-type: application/json\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/marketplace/$SPACE_ID/request/$REQUEST_ID/requester_info  {   \"userId\": \"585110fde9d1a52c93f8eb22c0614e47\",   \"fullName\": \"Joe Joester\",   \"username\": \"JoJo\",   \"contactEmail\": user@example.com } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
rid = 'rid_example' # str | Space membership request Id.

try:
    # Get membership requester info
    api_response = api_instance.get_membership_requester_info(id, rid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->get_membership_requester_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **rid** | **str**| Space membership request Id. | 

### Return type

[**SpaceMembershipRequesterInfo**](SpaceMembershipRequesterInfo.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space**
> Space get_space(id)

Get space details

Returns the details about a specific space.  This operation requires any of the following authentication: * as user who is an effective member of the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_view` admin privilege.  ***Example cURL requests***  **Get space details** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID  {   \"spaceId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"My Private space\",   \"description\": \"My Private data\",   \"organizationName\": \"\",   \"tags\": [\"images\", \"sport\"],   \"advertisedInMarketplace\": false,   \"marketplaceContactEmail\": \"\",   \"providers\": {     \"296ebe3c20e9666dc489b647f8647f12\": 5368709120,     \"dcf12429647c204896eebe3b6f686967\": 14400000   },   \"supportParametersRegistry\": {     \"296ebe3c20e9666dc489b647f8647f12\": {       \"accountingEnabled\": false,       \"dirStatsServiceEnabled\": true,       \"dirStatsServiceStatus\": \"enabled\"     },     \"dcf12429647c204896eebe3b6f686967\": {       \"accountingEnabled\": false,       \"dirStatsServiceEnabled\": false,       \"dirStatsServiceStatus\": \"stopping\"     }   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebfc1a770c3\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.

try:
    # Get space details
    api_response = api_instance.get_space(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->get_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 

### Return type

[**Space**](Space.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space_data_in_marketplace**
> SpaceMarketplaceData get_space_data_in_marketplace(id)

Get space details in the Marketplace

Returns the Marketplace related details about a specific space.  This operation can be performed by any user, but only for spaces advertised in the Marketplace.  ***Example cURL requests***  **Get space details in the Marketplace** ```bash curl -H \"x-auth-token: $TOKEN\" -H \\ https://$ZONE_HOST/api/v3/onezone/spaces/marketplace/$SPACE_ID  {   \"name\": \"Meteo dataset\",   \"index\": \"Meteo dataset@2c0160248ba9a66f45da751ca459535a\",   \"description\": \"This dataset contains meteorological data for major Polish cities in years 2012-2014.\",   \"organizationName\": \"ACK Cyfronet AGH\",   \"tags\": [\"archival\", \"big-data\", \"open-data\", \"environment\"],   \"providerNames\": [\"krakow\", \"paris\"],   \"totalSupportSize\": 30500000000,   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.

try:
    # Get space details in the Marketplace
    api_response = api_instance.get_space_data_in_marketplace(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->get_space_data_in_marketplace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 

### Return type

[**SpaceMarketplaceData**](SpaceMarketplaceData.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space_group**
> Group get_space_group(id, gid)

Get space's group details

Returns details about a specific group in a space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get space group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups/$GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_groupX\",   \"type\": \"team\" } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
gid = 'gid_example' # str | Group Id.

try:
    # Get space's group details
    api_response = api_instance.get_space_group(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->get_space_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **gid** | **str**| Group Id. | 

### Return type

[**Group**](Group.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space_harvester**
> Harvester get_space_harvester(id, hid)

Get harvester details

Returns details about a specific harvester in a space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_harvesters_view` admin privilege.  ***Example cURL requests***  **Get space harvester details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/harvesters/$HARVESTER_ID  {   \"harvesterId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_harvester1\",   \"public\" : true,   \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\",   \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
hid = 'hid_example' # str | Harvester Id.

try:
    # Get harvester details
    api_response = api_instance.get_space_harvester(id, hid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->get_space_harvester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **hid** | **str**| Harvester Id. | 

### Return type

[**Harvester**](Harvester.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space_provider**
> ProviderDetails get_space_provider(id, pid)

Get space provider details

Returns details about a specific provider supporting the space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_providers_view` admin privilege.  ***Example cURL requests***  **Get space provider details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/providers/$PROVIDER_ID  {   \"providerId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"name\": \"Example provider\",   \"domain\": \"provider1.example.com\",   \"latitude\": 50.0647,   \"longitude\": 19.945,   \"clusterId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"online\": true,   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
pid = 'pid_example' # str | Provider Id.

try:
    # Get space provider details
    api_response = api_instance.get_space_provider(id, pid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->get_space_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **pid** | **str**| Provider Id. | 

### Return type

[**ProviderDetails**](ProviderDetails.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space_share**
> Share get_space_share(id, sid)

Get space share

Returns the details about a share from specific space.  NOTE: Only Oneprovider API supports creating / deleting shares and is preferred for all share operations. Onezone API is limited to retrieving and modifying share details.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_shares_view` admin privilege.  ***Example cURL requests***  **Get space share** ```bash curl -u username:password -H \"Content-type: application/json\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/shares/$SHARE_ID  {   \"shareId\": \"1f4b762b1380946e73aeca574c77f14c\",   \"name\": \"Experiment XYZ\",   \"description\": \"# Experiment XYZ\\nThis collection contains results from Experiment XYZ.\",   \"publicUrl\": \"https://example.com/shares/1f4b762b1380946e73aeca574c77f14c\",   \"publicRestUrl\": \"https://example.com/api/v3/onezone/shares/1f4b762b1380946e73aeca574c77f14c/public\",   \"fileType\": \"dir\",   \"rootFileId\": \"00000000006CB663736861726547756964233339643236366165646365\\   6266666164353939663761373734313235363166342336656331613534313362366634653\\   2623031613563383561386664373937653223316634623736326231333830393436653733\\   6165636135373463373766313463\",   \"spaceId\": \"6ec1a5413b6f4e2b01a5c85a8fd797e2\",   \"handleId\" \"70570c0ebcd081835ca29560708fd98f\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
sid = 'sid_example' # str | Share Id.

try:
    # Get space share
    api_response = api_instance.get_space_share(id, sid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->get_space_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **sid** | **str**| Share Id. | 

### Return type

[**Share**](Share.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space_user**
> User get_space_user(id, uid)

Get space user details

Returns basic information about a specific user in a space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_users_view` admin privilege.  ***Example cURL requests***  **Get space user data** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\" } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
uid = 'uid_example' # str | User Id.

try:
    # Get space user details
    api_response = api_instance.get_space_user(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->get_space_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**User**](User.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_group_space_privileges**
> InlineResponse2009 list_effective_group_space_privileges(id, gid)

List effective group's space privileges

Returns the list of effective group's (`{gid}`) privileges in a space (`{id}`).  Effective privileges are a sum of group's privileges and privileges inherited from its parent group memberships.  This operation requires any of the following authentication: * as user who has `space_view_privileges` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_groups_view_privileges` admin privilege.  ***Example cURL requests***  **List effective groups's privileges in a space** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_groups/$GROUP_ID/privileges  {   \"privileges\": [     \"space_view\",     \"space_update\",     \"space_delete\",     \"space_view_privileges\",     \"space_set_privileges\"   ] } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
gid = 'gid_example' # str | Group Id.

try:
    # List effective group's space privileges
    api_response = api_instance.list_effective_group_space_privileges(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->list_effective_group_space_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **gid** | **str**| Group Id. | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_space_groups**
> Groups list_effective_space_groups(id)

List effective space groups

Returns the list of effective groups belonging to a specific space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_list_relationships` admin privilege.  ***Example cURL requests***  **Get space effective groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_groups  {   \"groups\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.

try:
    # List effective space groups
    api_response = api_instance.list_effective_space_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->list_effective_space_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 

### Return type

[**Groups**](Groups.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_space_users**
> Users list_effective_space_users(id)

List effective space users

Returns the list of effective users belonging to a specific space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_list_relationships` admin privilege.  ***Example cURL requests***  **Get space effective users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_users  {   \"users\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.

try:
    # List effective space users
    api_response = api_instance.list_effective_space_users(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->list_effective_space_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 

### Return type

[**Users**](Users.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_user_space_privileges**
> InlineResponse2009 list_effective_user_space_privileges(id, uid)

List effective user's space privileges

Returns the list of effective user's (`{uid}`) privileges in a space (`{id}`).  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation requires any of the following authentication: * as user who has `space_view_privileges` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_users_view_privileges` admin privilege.  ***Example cURL requests***  **List effective user's privileges in a space** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_users/$USER_ID/privileges  {   \"privileges\": [     \"space_view\",     \"space_update\",     \"space_delete\",     \"space_view_privileges\",     \"space_set_privileges\"   ] } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
uid = 'uid_example' # str | User Id.

try:
    # List effective user's space privileges
    api_response = api_instance.list_effective_user_space_privileges(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->list_effective_user_space_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_space_privileges**
> InlineResponse2009 list_group_space_privileges(id, gid)

List group's space privileges

Returns the list of group's (`{gid}`) privileges in a space (`{id}`).  This operation requires any of the following authentication: * as user who has `space_view_privileges` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_view_privileges` admin privilege.  ***Example cURL requests***  **List groups's privileges in a space** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups/$GROUP_ID/privileges  {   \"privileges\": [     \"space_view\",     \"space_update\",     \"space_delete\",     \"space_view_privileges\",     \"space_set_privileges\"   ] } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
gid = 'gid_example' # str | Group Id.

try:
    # List group's space privileges
    api_response = api_instance.list_group_space_privileges(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->list_group_space_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **gid** | **str**| Group Id. | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_marketplace**
> InlineResponse2007 list_marketplace(body=body)

List the Space Marketplace

List spaces advertised in the Marketplace.  ***Example cURL requests***  **List spaces advertised in the Marketplace** ```bash curl -H \"x-auth-token: $TOKEN\" -H \"Content-type: application/json\" \\ -X POST -d '{ \"limit\" : 2 }' \\ https://$ZONE_HOST/api/v3/onezone/spaces/marketplace/list  {   \"spaces\": [     {       \"spaceId\": \"d6ee1aecf03b23f09756d6a49e435455\",        \"index\": \"aqua@d6ee1aecf03b23f09756d6a49e435455\"     },     {       \"spaceId\": \"3b23a49e1aecf06d6555d6e4354f097e\",        \"index\": \"terra@3b23a49e1aecf06d6555d6e4354f097e\"     }   ],   \"isLast\": false,   \"nextPageToken\": \"UkdseU1qWTBNak16TXpNNU5qUXpNak0yTXpZMk1UWTFOalEyTXpZMU5qSTJOalky\" } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
body = onezone_client.MarketplaceListBody() # MarketplaceListBody | Space Marketplace listing options. (optional)

try:
    # List the Space Marketplace
    api_response = api_instance.list_marketplace(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->list_marketplace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MarketplaceListBody**](MarketplaceListBody.md)| Space Marketplace listing options. | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_space_groups**
> Groups list_space_groups(id)

List space groups

Returns the list of groups belonging to a specific space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_list_relationships` admin privilege.  ***Example cURL requests***  **Get space groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups  {   \"groups\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.

try:
    # List space groups
    api_response = api_instance.list_space_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->list_space_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 

### Return type

[**Groups**](Groups.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_space_harvesters**
> Harvesters list_space_harvesters(id)

List space harvesters

Returns the list of harvesters of a specific space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_list_relationships` admin privilege.  ***Example cURL requests***  **Get space harvesters** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/harvesters  {   \"harvesters\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.

try:
    # List space harvesters
    api_response = api_instance.list_space_harvesters(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->list_space_harvesters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 

### Return type

[**Harvesters**](Harvesters.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_space_owners**
> Users list_space_owners(id)

List space owners

Returns the list of owners of a specific space.  Space owners are members (users) of the space that have absolute power regarding the space API and files (analogical to \"root\", but in the scope of one space). Being an owner means that user privileges are essentially ignored and all API operations are allowed.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_view` admin privilege.  ***Example cURL requests***  **Get space owners** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/owners  {   \"users\": [     \"a5b469a2b0516b662a49da74d6d7d7bc\"   ] } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.

try:
    # List space owners
    api_response = api_instance.list_space_owners(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->list_space_owners: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 

### Return type

[**Users**](Users.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_space_privileges**
> InlineResponse2006 list_space_privileges()

List all space privileges

Returns list of all possible space privileges.  This endpoint does not require authentication.  ***Example cURL requests***  **Get list of all space privileges** ```bash curl https://$ZONE_HOST/api/v3/onezone/spaces/privileges  {   \"admin\": [     \"space_view\",     \"space_update\",     \"space_delete\",     \"space_view_privileges\",     \"space_set_privileges\",     \"space_read_data\",     \"space_write_data\",     \"space_register_files\",     \"space_manage_shares\",     \"space_view_views\",     \"space_manage_views\",     \"space_query_views\",     \"space_view_statistics\",     \"space_view_changes_stream\",     \"space_view_transfers\",     \"space_schedule_replication\",     \"space_cancel_replication\",     \"space_schedule_eviction\",     \"space_cancel_eviction\",     \"space_view_qos\",     \"space_manage_qos\",     \"space_add_user\",     \"space_remove_user\",     \"space_add_group\",     \"space_remove_group\",     \"space_add_provider\",     \"space_remove_provider\",     \"space_add_harvester\",     \"space_remove_harvester\"   ],   \"manager\": [     \"space_view\",     \"space_view_privileges\",     \"space_read_data\",     \"space_write_data\",     \"space_register_files\",     \"space_manage_shares\",     \"space_view_views\",     \"space_query_views\",     \"space_view_statistics\",     \"space_view_changes_stream\",     \"space_view_transfers\",     \"space_schedule_replication\",     \"space_view_qos\",     \"space_add_user\",     \"space_remove_user\",     \"space_add_group\",     \"space_remove_group\",     \"space_add_harvester\",     \"space_remove_harvester\"   ],   \"member\": [     \"space_view\",     \"space_read_data\",     \"space_write_data\",     \"space_view_transfers\"   ] } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))

try:
    # List all space privileges
    api_response = api_instance.list_space_privileges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->list_space_privileges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_space_providers**
> Providers list_space_providers(id)

List space providers

Returns the list of providers supporting specific space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_list_relationships` admin privilege.  ***Example cURL requests***  **Get space support token** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/providers  {   \"providers\": [     \"MDAxNmxvYZjUGlIcGkweGZta1ZOdEp00eUNINVNvR2001Wl\"   ] } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.

try:
    # List space providers
    api_response = api_instance.list_space_providers(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->list_space_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 

### Return type

[**Providers**](Providers.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_space_shares**
> Shares list_space_shares(id)

List space shares

Returns the list of shares from specific space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_list_relationships` admin privilege.  ***Example cURL requests***  **List space shares** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/shares  {   \"shares\": [     \"MDAxNmxvYZjUGlIcGkweGZta1ZOdEp00eUNINVNvR2001Wl\"   ] } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.

try:
    # List space shares
    api_response = api_instance.list_space_shares(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->list_space_shares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 

### Return type

[**Shares**](Shares.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_space_users**
> Users list_space_users(id)

List space users

Returns the list of users belonging to a specific space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_list_relationships` admin privilege.  ***Example cURL requests***  **Get space users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/users  {   \"users\": [     \"a5b469a2b0516b662a49da74d6d7d7bc\"   ] } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.

try:
    # List space users
    api_response = api_instance.list_space_users(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->list_space_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 

### Return type

[**Users**](Users.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_spaces**
> Spaces list_spaces()

List all spaces

Returns the list of all spaces managed by the Onezone service.  This operation requires `oz_spaces_list` admin privilege.  ***Example cURL requests***  **List all spaces** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces  {   \"spaces\": [     \"d6ee1aecf03b23f09756d6a49e435455\",     \"3b23a49e1aecf06d6555d6e4354f097e\"   ] } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))

try:
    # List all spaces
    api_response = api_instance.list_spaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->list_spaces: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Spaces**](Spaces.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_space_privileges**
> InlineResponse2009 list_user_space_privileges(id, uid)

List user's space privileges

Returns the list of user's (`{uid}`) privileges in a space (`{id}`).  This operation requires any of the following authentication: * as user who has `space_view_privileges` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_view_privileges` admin privilege.  ***Example cURL requests***  **List user's privileges in a space** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/users/$USER_ID/privileges  {   \"privileges\": [     \"space_view\",     \"space_update\",     \"space_delete\",     \"space_view_privileges\",     \"space_set_privileges\"   ] } ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
uid = 'uid_example' # str | User Id.

try:
    # List user's space privileges
    api_response = api_instance.list_user_space_privileges(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->list_user_space_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_space**
> modify_space(body, id)

Modify space details

Updates the details about a space.  This operation requires `space_update` privilege or `oz_spaces_update` admin privilege.  ***Example cURL requests***  **Change space name** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"name\": \"new_space12\"}' \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
body = onezone_client.SpacesIdBody() # SpacesIdBody | Space parameters
id = 'id_example' # str | Space Id.

try:
    # Modify space details
    api_instance.modify_space(body, id)
except ApiException as e:
    print("Exception when calling SpaceApi->modify_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpacesIdBody**](SpacesIdBody.md)| Space parameters | 
 **id** | **str**| Space Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_space**
> remove_space(id)

Remove space

Removes a specific space.  This operation requires `space_delete` privilege or `oz_spaces_delete` admin privilege.  ***Example cURL requests***  **Remove space** ```bash curl -u admin:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.

try:
    # Remove space
    api_instance.remove_space(id)
except ApiException as e:
    print("Exception when calling SpaceApi->remove_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_space_from_harvester**
> remove_space_from_harvester(id, hid)

Remove space from harvester.

Removes the space {id} from harvester {hid} (metadata from given space will no longer be submitted to given harvester).  This operation requires `space_remove_harvester` privilege. For administrator who does not belong to this group `oz_spaces_remove_relationships` and `oz_harvesters_remove_relationships` privileges are required.  ***Example cURL requests***  **Get space harvester details** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/harvesters/$HARVESTER_ID ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
hid = 'hid_example' # str | Harvester Id.

try:
    # Remove space from harvester.
    api_instance.remove_space_from_harvester(id, hid)
except ApiException as e:
    print("Exception when calling SpaceApi->remove_space_from_harvester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **hid** | **str**| Harvester Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_space_group**
> remove_space_group(id, gid)

Remove group from space

Removes a specific group from space.  For regular users, who belong to this space it requires `space_remove_group` privilege to remove a group from this space.  For administrators, who are not members of this space, `oz_spaces_remove_relationships` privilege is required.  ***Example cURL requests***  **Get space group details** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups/$GROUP_ID ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
gid = 'gid_example' # str | Group Id.

try:
    # Remove group from space
    api_instance.remove_space_group(id, gid)
except ApiException as e:
    print("Exception when calling SpaceApi->remove_space_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **gid** | **str**| Group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_space_owner**
> remove_space_owner(id, uid)

Remove space owner

Removes user `{uid}` from the owners of space `{id}`. The user is not removed from the space as a member, but his ownership is revoked.  This operation will fail if the `{uid}` is the last owner of the space. First, ownership must be granted to another user so that the space has at least one owner.  This operation requires any of the following authentication: * as user who is currently an owner of the space (`{id}`), * as user who has `oz_spaces_set_privileges` admin privilege.  ***Example cURL requests***  **Remove space owner** ```bash curl -u admin:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/owners/$USER_ID ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
uid = 'uid_example' # str | User Id.

try:
    # Remove space owner
    api_instance.remove_space_owner(id, uid)
except ApiException as e:
    print("Exception when calling SpaceApi->remove_space_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **uid** | **str**| User Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_space_user**
> remove_space_user(id, uid)

Remove user from space

Removes user from specific space.  This operation requires `space_remove_user` or requires `oz_spaces_add_relationships` and `oz_users_add_relationships` admin privilege.  ***Example cURL requests***  **Remove user from space** ```bash curl -u admin:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/users/$USER_ID ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
uid = 'uid_example' # str | User Id.

try:
    # Remove user from space
    api_instance.remove_space_user(id, uid)
except ApiException as e:
    print("Exception when calling SpaceApi->remove_space_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **uid** | **str**| User Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_space_membership**
> InlineResponse2008 request_space_membership(body, id)

Request space membership via Marketplace

Request space membership for a space advertised in the Marketplace as currently authenticated user.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Request space membership via Marketplace** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"contactEmail\" : \"user@example.com\"}' \\ https://$ZONE_HOST/api/v3/onezone/spaces/marketplace/$SPACE_ID/request ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
body = onezone_client.IdRequestBody() # IdRequestBody | Space membership request body.
id = 'id_example' # str | Space Id.

try:
    # Request space membership via Marketplace
    api_response = api_instance.request_space_membership(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->request_space_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdRequestBody**](IdRequestBody.md)| Space membership request body. | 
 **id** | **str**| Space Id. | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_space_membership_request**
> resolve_space_membership_request(body, id, rid)

Resolve space membership request

Resolve space membership request made via the Marketplace.  This operation requires privilege `space_manage_in_marketplace` and, in case of positive resolution, `space_add_user` in space for which  the request was made.  ***Example cURL requests***  **Resolve space membership request** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"requestId\": \"97216a666edd09945880a0785ad66a7b\", \"decision\": \"grant\"}' \\ https://$ZONE_HOST/api/v3/onezone/spaces/marketplace/$SPACE_ID/request/$REQUEST_ID/resolve ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
body = onezone_client.RidResolveBody() # RidResolveBody | Space membership request resolution body.
id = 'id_example' # str | Space Id.
rid = 'rid_example' # str | Space membership request Id.

try:
    # Resolve space membership request
    api_instance.resolve_space_membership_request(body, id, rid)
except ApiException as e:
    print("Exception when calling SpaceApi->resolve_space_membership_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RidResolveBody**](RidResolveBody.md)| Space membership request resolution body. | 
 **id** | **str**| Space Id. | 
 **rid** | **str**| Space membership request Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **space_join_harvester**
> space_join_harvester(id, body=body)

Join space to a harvester

Joins the space to an existing harvester based on provided `spaceJoinHarvester` invitation token (the space becomes a metadata source for the harvester).  This operation requires `space_add_harvester` privilege. For administrator who does not belong to this space `oz_harvesters_add_relationships` and `oz_spaces_add_relationships` privilege is required.  ***Example cURL requests***  **Join space to a harvester** ```bash curl -u admin:password -H \"Content-type: application/json\" \\ -d '{\"token\":\"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVuJ3l02U1JXzstRdK00ZHbso02rRcG8bJLAo\"}' \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/harvesters/join ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
body = onezone_client.HarvesterInviteToken() # HarvesterInviteToken | spaceJoinHarvester invite token. (optional)

try:
    # Join space to a harvester
    api_instance.space_join_harvester(id, body=body)
except ApiException as e:
    print("Exception when calling SpaceApi->space_join_harvester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **body** | [**HarvesterInviteToken**](HarvesterInviteToken.md)| spaceJoinHarvester invite token. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_space_privileges**
> update_group_space_privileges(body, id, gid)

Update group privileges to space

Updates group's (`{gid}`) privileges in a space (`{id}`).  This operation requires `space_set_privileges` privilege or `oz_spaces_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update group's privileges in a space** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"space_view\", \"space_update\"], \"revoke\": [\"space_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups/$GROUP_ID/privileges ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
body = onezone_client.SpacePrivilegesUpdate() # SpacePrivilegesUpdate | Space privileges update request.
id = 'id_example' # str | Space Id.
gid = 'gid_example' # str | Group Id.

try:
    # Update group privileges to space
    api_instance.update_group_space_privileges(body, id, gid)
except ApiException as e:
    print("Exception when calling SpaceApi->update_group_space_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpacePrivilegesUpdate**](SpacePrivilegesUpdate.md)| Space privileges update request. | 
 **id** | **str**| Space Id. | 
 **gid** | **str**| Group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_support_parameters_of_provider**
> update_support_parameters_of_provider(id, pid, body=body)

Update space support parameters of provider

Updates space support parameters of a provider in the space.  Authorization depends on the modified parameters (see respective descriptions).  ***Example cURL requests***  **Update space support parameters of provider** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"dirStatsServiceEnabled\": true}' \\ https://$HOST/api/v3/onezone/spaces/$SPACE_ID/providers/$PROVIDER_ID/support_parameters ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Space Id.
pid = 'pid_example' # str | Provider Id.
body = onezone_client.SupportParameters() # SupportParameters |  (optional)

try:
    # Update space support parameters of provider
    api_instance.update_support_parameters_of_provider(id, pid, body=body)
except ApiException as e:
    print("Exception when calling SpaceApi->update_support_parameters_of_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Space Id. | 
 **pid** | **str**| Provider Id. | 
 **body** | [**SupportParameters**](SupportParameters.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_space_privileges**
> update_user_space_privileges(body, id, uid)

Update user's space privileges

Updates user's (`{uid}`) privileges in a space (`{id}`).  This operation requires `space_set_privileges` privilege. For administrators who do not have to be members of this space, `oz_spaces_set_privileges` privilege is required.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update user's privileges in a space** ```bash curl -u admin:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"space_view\", \"space_update\"], \"revoke\": [\"space_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/users/$USER_ID/privileges ``` 

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
api_instance = onezone_client.SpaceApi(onezone_client.ApiClient(configuration))
body = onezone_client.SpacePrivilegesUpdate() # SpacePrivilegesUpdate | Space privileges update request.
id = 'id_example' # str | Space Id.
uid = 'uid_example' # str | User Id.

try:
    # Update user's space privileges
    api_instance.update_user_space_privileges(body, id, uid)
except ApiException as e:
    print("Exception when calling SpaceApi->update_user_space_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpacePrivilegesUpdate**](SpacePrivilegesUpdate.md)| Space privileges update request. | 
 **id** | **str**| Space Id. | 
 **uid** | **str**| User Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

