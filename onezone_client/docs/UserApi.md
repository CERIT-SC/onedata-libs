# onezone_client.UserApi

All URIs are relative to */api/v3/onezone*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acquire_idp_access_token**](UserApi.md#acquire_idp_access_token) | **POST** /user/idp_access_token/{idp} | Acquire IdP access token
[**add_user_handle_service**](UserApi.md#add_user_handle_service) | **POST** /user/handle_services | Create a new handle service for the current user
[**change_user_basic_auth_settings**](UserApi.md#change_user_basic_auth_settings) | **PATCH** /users/{id}/basic_auth | Change user&#x27;s basic auth settings
[**change_user_password**](UserApi.md#change_user_password) | **PATCH** /user/password | Change user&#x27;s password
[**create_client_token**](UserApi.md#create_client_token) | **POST** /user/client_tokens | Generate user access token
[**create_provider_registration_token_for_current_user**](UserApi.md#create_provider_registration_token_for_current_user) | **POST** /user/clusters/provider_registration_token | Create provider registration token for current user
[**create_provider_registration_token_for_user**](UserApi.md#create_provider_registration_token_for_user) | **POST** /users/{id}/clusters/provider_registration_token | Create provider registration token for a user
[**create_user**](UserApi.md#create_user) | **POST** /users | Create new user
[**create_user_group**](UserApi.md#create_user_group) | **POST** /user/groups | Create a new group for the current user
[**create_user_handle**](UserApi.md#create_user_handle) | **POST** /user/handles | Create a new handle for the current user
[**create_user_harvester**](UserApi.md#create_user_harvester) | **POST** /user/harvesters | Create a new harvester for the current user
[**create_user_space**](UserApi.md#create_user_space) | **POST** /user/spaces | Create a new space for the current user
[**get_current_user**](UserApi.md#get_current_user) | **GET** /user | Get current user details
[**get_effective_user_harvester**](UserApi.md#get_effective_user_harvester) | **GET** /user/effective_harvesters/{hid} | Get effective harvester details
[**get_effective_user_space**](UserApi.md#get_effective_user_space) | **GET** /user/effective_spaces/{sid} | Get effective space details
[**get_space_membership_requests**](UserApi.md#get_space_membership_requests) | **GET** /user/space_membership_requests | Get summary of space membership requests
[**get_user**](UserApi.md#get_user) | **GET** /users/{id} | Get user details
[**get_user_cluster**](UserApi.md#get_user_cluster) | **GET** /user/clusters/{cid} | Get user&#x27;s cluster details
[**get_user_effective_cluster**](UserApi.md#get_user_effective_cluster) | **GET** /user/effective_clusters/{cid} | Get user&#x27;s effective cluster details
[**get_user_effective_group**](UserApi.md#get_user_effective_group) | **GET** /user/effective_groups/{gid} | Get effective group details
[**get_user_effective_handle**](UserApi.md#get_user_effective_handle) | **GET** /user/effective_handles/{hid} | Get effective handle details
[**get_user_effective_handle_service**](UserApi.md#get_user_effective_handle_service) | **GET** /user/effective_handle_services/{hsid} | Get effective handle service details
[**get_user_effective_provider**](UserApi.md#get_user_effective_provider) | **GET** /user/effective_providers/{pid} | Get user&#x27;s effective provider details
[**get_user_group**](UserApi.md#get_user_group) | **GET** /user/groups/{gid} | Get group details
[**get_user_handle**](UserApi.md#get_user_handle) | **GET** /user/handles/{hid} | Get handle details
[**get_user_handle_service**](UserApi.md#get_user_handle_service) | **GET** /user/handle_services/{hsid} | Get user handle service details
[**get_user_harvester**](UserApi.md#get_user_harvester) | **GET** /user/harvesters/{hid} | Get harvester details
[**get_user_space**](UserApi.md#get_user_space) | **GET** /user/spaces/{sid} | Get space details
[**get_user_space_alias**](UserApi.md#get_user_space_alias) | **GET** /user/spaces/{sid}/alias | Get user space alias
[**get_user_spaces_in_effective_provider**](UserApi.md#get_user_spaces_in_effective_provider) | **GET** /user/effective_providers/{pid}/spaces | Get user&#x27;s spaces that are supported by given effective provider
[**join_group**](UserApi.md#join_group) | **POST** /user/groups/join | Join group
[**join_harvester**](UserApi.md#join_harvester) | **POST** /user/harvesters/join | Join harvester
[**join_space**](UserApi.md#join_space) | **POST** /user/spaces/join | Join space
[**leave_group**](UserApi.md#leave_group) | **DELETE** /user/groups/{gid} | Leave group
[**leave_handle_service**](UserApi.md#leave_handle_service) | **DELETE** /user/handle_services/{hsid} | Leave handle service
[**leave_space**](UserApi.md#leave_space) | **DELETE** /user/spaces/{sid} | Leave space
[**list_client_tokens**](UserApi.md#list_client_tokens) | **GET** /user/client_tokens | List user access tokens
[**list_current_user_admin_privileges**](UserApi.md#list_current_user_admin_privileges) | **GET** /user/privileges | List current user privileges
[**list_current_user_effective_admin_privileges**](UserApi.md#list_current_user_effective_admin_privileges) | **GET** /user/effective_privileges | List current user effective privileges
[**list_effective_user_groups**](UserApi.md#list_effective_user_groups) | **GET** /user/effective_groups | List effective user groups
[**list_effective_user_harvesters**](UserApi.md#list_effective_user_harvesters) | **GET** /user/effective_harvesters | List effective user harvesters
[**list_effective_user_providers**](UserApi.md#list_effective_user_providers) | **GET** /user/effective_providers | List user effective providers
[**list_effective_user_spaces**](UserApi.md#list_effective_user_spaces) | **GET** /user/effective_spaces | List effective user spaces
[**list_user_admin_privileges**](UserApi.md#list_user_admin_privileges) | **GET** /users/{id}/privileges | List user admin privileges
[**list_user_clusters**](UserApi.md#list_user_clusters) | **GET** /user/clusters | List user&#x27;s clusters
[**list_user_effective_admin_privileges**](UserApi.md#list_user_effective_admin_privileges) | **GET** /users/{id}/effective_privileges | List user&#x27;s effective admin privileges
[**list_user_effective_clusters**](UserApi.md#list_user_effective_clusters) | **GET** /user/effective_clusters | List user&#x27;s effective clusters
[**list_user_effective_handle_services**](UserApi.md#list_user_effective_handle_services) | **GET** /user/effective_handle_services | List user effective handle services
[**list_user_effective_handles**](UserApi.md#list_user_effective_handles) | **GET** /user/effective_handles | Get user effective handles
[**list_user_groups**](UserApi.md#list_user_groups) | **GET** /user/groups | List user groups
[**list_user_handle_services**](UserApi.md#list_user_handle_services) | **GET** /user/handle_services | List user handle services
[**list_user_handles**](UserApi.md#list_user_handles) | **GET** /user/handles | List user handles
[**list_user_harvesters**](UserApi.md#list_user_harvesters) | **GET** /user/harvesters | List user harvesters
[**list_user_spaces**](UserApi.md#list_user_spaces) | **GET** /user/spaces | List user spaces
[**modify_current_user**](UserApi.md#modify_current_user) | **PATCH** /user | Modify current user
[**oz_users_list**](UserApi.md#oz_users_list) | **GET** /users | List all users
[**remove_client_token**](UserApi.md#remove_client_token) | **DELETE** /user/client_tokens/{tid} | Delete access token
[**remove_current_user**](UserApi.md#remove_current_user) | **DELETE** /user | Remove current user
[**remove_current_user_admin_privileges**](UserApi.md#remove_current_user_admin_privileges) | **DELETE** /user/privileges | Remove current user&#x27;s admin privileges
[**remove_user**](UserApi.md#remove_user) | **DELETE** /users/{id} | Remove user
[**remove_user_admin_privileges**](UserApi.md#remove_user_admin_privileges) | **DELETE** /users/{id}/privileges | Remove user&#x27;s admin privileges
[**remove_user_handle**](UserApi.md#remove_user_handle) | **DELETE** /user/handles/{hid} | Leave handle
[**remove_user_space_alias**](UserApi.md#remove_user_space_alias) | **DELETE** /user/spaces/{sid}/alias | Remove space alias
[**set_user_space_alias**](UserApi.md#set_user_space_alias) | **PUT** /user/spaces/{sid}/alias | Set user space alias
[**toggle_user_access_block**](UserApi.md#toggle_user_access_block) | **PATCH** /users/{id}/access_block | Block or unblock user access
[**update_current_user_admin_privileges**](UserApi.md#update_current_user_admin_privileges) | **PATCH** /user/privileges | Update current user&#x27;s admin privileges
[**update_user_admin_privileges**](UserApi.md#update_user_admin_privileges) | **PATCH** /users/{id}/privileges | Update user&#x27;s admin privileges
[**user_join_cluster**](UserApi.md#user_join_cluster) | **POST** /user/clusters/join | Join cluster
[**user_leave_cluster**](UserApi.md#user_leave_cluster) | **DELETE** /user/clusters/{cid} | Leave cluster
[**user_leave_harvester**](UserApi.md#user_leave_harvester) | **DELETE** /user/harvesters/{hid} | Leave harvester

# **acquire_idp_access_token**
> IdPAccessToken acquire_idp_access_token(idp)

Acquire IdP access token

Acquires an access token issued by given IdP for the current user. This operation requires that the IdP is configured to support offline access - issues refresh tokens upon user's login to Onezone, which are later used to acquire new access tokens when they expire. Offline access can be configured by the Onezone admin.  The user must first log in to Onezone using given IdP, otherwise the operation will return a 404 error.  This operation can be invoked on behalf of current user only.  ***Example cURL requests***  **Acquire IdP access token** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/user/idp_access_token/github ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
idp = 'idp_example' # str | IdP identifier.

try:
    # Acquire IdP access token
    api_response = api_instance.acquire_idp_access_token(idp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->acquire_idp_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp** | **str**| IdP identifier. | 

### Return type

[**IdPAccessToken**](IdPAccessToken.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_handle_service**
> add_user_handle_service(body)

Create a new handle service for the current user

Allows to register a new handle service.  This operation can be invoked on behalf of the current user only and requires `oz_handle_service_create` admin privilege.  ***Example cURL requests***  **Add user handle services** ```bash curl -u username:password -X POST -H \"Content-type: application/json\" \\ -d '{ ... }' https://$ZONE_HOST/api/v3/onezone/user/handle_services ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
body = onezone_client.HandleService() # HandleService | 

try:
    # Create a new handle service for the current user
    api_instance.add_user_handle_service(body)
except ApiException as e:
    print("Exception when calling UserApi->add_user_handle_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HandleService**](HandleService.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_basic_auth_settings**
> change_user_basic_auth_settings(body, id)

Change user's basic auth settings

Changes user's basic auth settings - the ability to authenticate with username & password, and/or the password itself.  This operation requires `oz_users_manage_passwords` admin privilege.  ***Example cURL requests***  **Change user's basic auth settings** ```bash curl -u admin:password -H \"Content-type: application/json\" -X PATCH  \\ -d '{\"basicAuthEnabled\": true, \"newPassword\": \"password123\"}' \\ https://$ZONE_HOST/api/v3/onezone/users/c5cb69ce45940468596ed16310a45e49/basic_auth ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
body = onezone_client.UserBasicAuthSettingsUpdate() # UserBasicAuthSettingsUpdate | User basic auth settings update request.
id = 'id_example' # str | User Id.

try:
    # Change user's basic auth settings
    api_instance.change_user_basic_auth_settings(body, id)
except ApiException as e:
    print("Exception when calling UserApi->change_user_basic_auth_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserBasicAuthSettingsUpdate**](UserBasicAuthSettingsUpdate.md)| User basic auth settings update request. | 
 **id** | **str**| User Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_password**
> change_user_password(body)

Change user's password

Changes user's password, the old password must be given.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Change user's password** ```bash curl -u username:password -H \"Content-type: application/json\" -X PATCH  \\ -d '{\"oldPassword\": \"password\", \"newPassword\": \"password123\"}' \\ https://$ZONE_HOST/api/v3/onezone/user/password ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
body = onezone_client.UserPasswordUpdate() # UserPasswordUpdate | User password update request.

try:
    # Change user's password
    api_instance.change_user_password(body)
except ApiException as e:
    print("Exception when calling UserApi->change_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserPasswordUpdate**](UserPasswordUpdate.md)| User password update request. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client_token**
> ClientToken create_client_token()

Generate user access token

This enpoint is deprecated and will be removed in future release, please use [this one](#operation/create_named_token_for_current_user).  Creates new user token. The token is returned in the response body.  This operation can be invoked on behalf of currently authenticated user only.  ***Example cURL requests***  **Generate user token** ```bash curl -u username:password -X POST -d '' -H 'content-type: application/json' \\   https://$ZONE_HOST/api/v3/onezone/user/client_tokens  {   \"token\": \"MDAxNWxvY2F00aW9uIG9uZXpvbmUKMDAzYmlkZW500aWZpZXIgSlVxNGFLVkJSTXVFN3FLbHNQVHlNX00lLeHpYZXNWdVFSMGNfMldpOXFZNAowMDFhY2lkIHRpbWUgPCAxNTIyMzU4MzMzCjAwMmZzaWduYXR1cmUgv02ByyOA9802H02rPMB7Y9mIhDVAjYDmjAUjtrMs13znukK\" } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # Generate user access token
    api_response = api_instance.create_client_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_client_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClientToken**](ClientToken.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_provider_registration_token_for_current_user**
> ProviderRegistrationToken create_provider_registration_token_for_current_user()

Create provider registration token for current user

This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token for the current user allowing him to register a new provider in Onezone. After the registration, the user's account will be automatically linked to the new Oneprovider cluster (granting him access to Oneprovider's onepanel).  This operation can be invoked on behalf of the current user only.  If registration policy in Onezone is configured as `open`, any user can generate the token for himself. In case of `restricted` policy, this operation requires `oz_providers_invite` privilege.  ***Example cURL requests***  **Create provider registration token for current user** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/user/clusters/$CLUSTER_ID  {   \"token\": [     \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaW-0Y8\"   ] } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # Create provider registration token for current user
    api_response = api_instance.create_provider_registration_token_for_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_provider_registration_token_for_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProviderRegistrationToken**](ProviderRegistrationToken.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_provider_registration_token_for_user**
> ProviderRegistrationToken create_provider_registration_token_for_user(id)

Create provider registration token for a user

This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token for a specific user allowing him to register a new provider in Onezone. After the registration, the user's account will be automatically linked to the new Oneprovider cluster (granting him access to Oneprovider's onepanel).  If registration policy in Onezone is configured as `open`, any user can generate the token for himself. In case of `restricted` policy or issuing the token for another user, this operation requires `oz_providers_invite` privilege.  ***Example cURL requests***  **Create provider registration token for a user** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/clusters/$CLUSTER_ID  {   \"token\": [     \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaW-0Y8\"   ] } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | User Id.

try:
    # Create provider registration token for a user
    api_response = api_instance.create_provider_registration_token_for_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_provider_registration_token_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User Id. | 

### Return type

[**ProviderRegistrationToken**](ProviderRegistrationToken.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> create_user(body)

Create new user

Creates a new user.  This operation requires `oz_users_create` admin privilege.  ***Example cURL requests***  **Create new user** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"username\" : \"new_user\", \"password\": \"lS1c6FD2mxB2ff\" }' \\ https://$ZONE_HOST/api/v3/onezone/users ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
body = onezone_client.UserCreateRequest() # UserCreateRequest | User name.

try:
    # Create new user
    api_instance.create_user(body)
except ApiException as e:
    print("Exception when calling UserApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreateRequest**](UserCreateRequest.md)| User name. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_group**
> create_user_group(body)

Create a new group for the current user

Creates a new group for the current user. The user automatically becomes a member of this group.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Create new group** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"name\" : \"test_group\" , \"type\" : \"team\" }' \\ https://$ZONE_HOST/api/v3/onezone/user/groups ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
body = onezone_client.Group() # Group | New group parameters.

try:
    # Create a new group for the current user
    api_instance.create_user_group(body)
except ApiException as e:
    print("Exception when calling UserApi->create_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Group**](Group.md)| New group parameters. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_handle**
> create_user_handle(body)

Create a new handle for the current user

Creates a new handle as current user.  This operation can be invoked on behalf of the current user only and requires 'handle_service_register_handle' privilege in the handle service where the new handle is to be registered  ***Example cURL requests***  **Create new user handle** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"handleServiceId\": \"ddb06ed993bae95f2f430664fff122f7\", \"resourceType\": \"Share\", \"resourceId\": \"4fa683cbda8d8f686d15d42720af431d\", \"metadata\": \"<?xml version=\\'1.0\\'?>...\" }' https://$ZONE_HOST/api/v3/onezone/user/handles ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
body = onezone_client.HandleRegistrationRequest() # HandleRegistrationRequest | New handle parameters.

try:
    # Create a new handle for the current user
    api_instance.create_user_handle(body)
except ApiException as e:
    print("Exception when calling UserApi->create_user_handle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HandleRegistrationRequest**](HandleRegistrationRequest.md)| New handle parameters. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_harvester**
> create_user_harvester(body)

Create a new harvester for the current user

Creates a new harvester as current user. The user automaticaly becomes the harvesters' member.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Create new user harvester** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -X POST -d '{ \"name\" : \"new_harvester\", \"endpoint\" : \"example.elastic.com:9200\", \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\"  \\ \"config\" : { \"typeMapping\": [ { \"id\": 0, \"name\": \"Type 1\" }, { \"id\": 1, \"name\": \"Type 1\" } ],              \"externalHelpLink\": \"http://example.com/some_help_page\",              \"refreshDataTimeout\": 1000 }, \\ https://$ZONE_HOST/api/v3/onezone/user/harvesters ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
body = onezone_client.HarvesterCreateRequest() # HarvesterCreateRequest | New harvester parameters.

try:
    # Create a new harvester for the current user
    api_instance.create_user_harvester(body)
except ApiException as e:
    print("Exception when calling UserApi->create_user_harvester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HarvesterCreateRequest**](HarvesterCreateRequest.md)| New harvester parameters. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_space**
> create_user_space(body)

Create a new space for the current user

Creates a new space as current user. The user automaticaly becomes the spaces' member.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Create new user space** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"name\" : \"test_space\"}' https://$ZONE_HOST/api/v3/onezone/user/spaces ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
body = onezone_client.SpaceCreateRequest() # SpaceCreateRequest | New space parameters.

try:
    # Create a new space for the current user
    api_instance.create_user_space(body)
except ApiException as e:
    print("Exception when calling UserApi->create_user_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpaceCreateRequest**](SpaceCreateRequest.md)| New space parameters. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user**
> UserProtectedInfo get_current_user()

Get current user details

Returns details about currently authenticated user.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user details** ```bash curl -u admin:password -X GET https://$ZONE_HOST/api/v3/onezone/user  {   \"userId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"fullName\": \"Rudolf Lingens\",   \"username\": \"r.lingens\",   \"linkedAccounts\": [     {       \"idp\": \"github\",       \"subjectId\": \"1978f5775ae2dc16730418bf3fc81764\"     },     {       \"idp\": \"elixir\",       \"subjectId\": \"38bf3fc2f4c16730481764bd775ae2d1\"     }   ],   \"emails\": [     \"rudolf.lingens@example.com\",     \"john.doe@example.com\"   ],   \"basicAuthEnabled\": false,   \"blocked\": false,   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # Get current user details
    api_response = api_instance.get_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserProtectedInfo**](UserProtectedInfo.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_user_harvester**
> Harvester get_effective_user_harvester(hid)

Get effective harvester details

Returns information about a specific effective harvester to which the user has access.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective harvester** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_harvesters/$HARVESTER_ID  {   \"harvesterId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_harvester1\",   \"public\" : true,   \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\",   \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
hid = 'hid_example' # str | Harvester Id.

try:
    # Get effective harvester details
    api_response = api_instance.get_effective_user_harvester(hid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_effective_user_harvester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hid** | **str**| Harvester Id. | 

### Return type

[**Harvester**](Harvester.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_user_space**
> Space get_effective_user_space(sid)

Get effective space details

Returns information about a specific effective space to which the user has access.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective space** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_spaces/$SPACE_ID  {   \"spaceId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_space1\",   \"providers\": {     \"296ebe3c20e9666dc489b647f8647f12\" : 5368709120   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebfc1a770c3\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
sid = 'sid_example' # str | Space Id.

try:
    # Get effective space details
    api_response = api_instance.get_effective_user_space(sid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_effective_user_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Space Id. | 

### Return type

[**Space**](Space.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space_membership_requests**
> SpaceMembershipRequests get_space_membership_requests()

Get summary of space membership requests

Returns the summary of user's space membership requests.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get summary of space membership requests** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/space_membership_requests  {   \"pending\": {     \"715f5cf924cf8f69899a4ee8bbce8120\": {       \"requestId\": \"585110fde9d1a52c93f8eb22c0614e47\",       \"contactEmail\": \"user@example.com\",       \"lastActivity\": 1563819329     },     \"6db7e3095d8aedf5c145ef576339b10d\": {       \"requestId\": \"97216a666edd09945880a0785ad66a7b\",       \"contactEmail\": \"user@example.com\",       \"lastActivity\": 1563819923     }   },   \"rejected\": {      \"ee7aa1c60642646b9a5d1962dcd02b89\": {       \"requestId\": \"8467b1458989b8454a2faa8b5a45df7b\",       \"contactEmail\": \"user@example.com\",       \"lastActivity\": 1563823164     }   } } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # Get summary of space membership requests
    api_response = api_instance.get_space_membership_requests()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_space_membership_requests: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SpaceMembershipRequests**](SpaceMembershipRequests.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserProtectedInfo get_user(id)

Get user details

Returns the information about a specific user.  This operation requires `oz_users_view` admin privilege.  ***Example cURL requests***  **Get user details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID  {   \"userId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"fullName\": \"Rudolf Lingens\",   \"username\": \"r.lingens\",   \"linkedAccounts\": [     {       \"idp\": \"github\",       \"subjectId\": \"1978f5775ae2dc16730418bf3fc81764\"     },     {       \"idp\": \"elixir\",       \"subjectId\": \"38bf3fc2f4c16730481764bd775ae2d1\"     }   ],   \"emails\": [     \"rudolf.lingens@example.com\",     \"john.doe@example.com\"   ],   \"basicAuthEnabled\": false,   \"blocked\": false,   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | User Id.

try:
    # Get user details
    api_response = api_instance.get_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User Id. | 

### Return type

[**UserProtectedInfo**](UserProtectedInfo.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_cluster**
> Cluster get_user_cluster(cid)

Get user's cluster details

Returns the details of a specific user's cluster.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user's cluster details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/clusters/$CLUSTER_ID  {   \"clusterId\": \"f8d843beda24e54545455ecc0f4b8886\",   \"type\": \"oneprovider\",   \"workerVersion\": {     \"release\": \"21.02.3\",     \"build\": \"1-gfabf02d\",     \"gui\": \"129c549fbe9b3e730c3d9910492228566e39e1236945766a74381405cc57fb04\"   },   \"onepanelVersion\": {     \"release\": \"21.02.3\",     \"build\": \"3-89fc6bad\",     \"gui\": \"68e7e1472adb719ddf2d88908775091dfb10e5d0b916f06125ea1af4056044e3\"   },   \"online\": true,   \"onepanelProxy\": false,   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
cid = 'cid_example' # str | Cluster Id.

try:
    # Get user's cluster details
    api_response = api_instance.get_user_cluster(cid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| Cluster Id. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_effective_cluster**
> Cluster get_user_effective_cluster(cid)

Get user's effective cluster details

Returns information about a specific user's effective cluster.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user's effective cluster details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/clusters/$CLUSTER_ID  {   \"clusterId\": \"f8d843beda24e54545455ecc0f4b8886\",   \"type\": \"oneprovider\",   \"workerVersion\": {     \"release\": \"21.02.3\",     \"build\": \"1-gfabf02d\",     \"gui\": \"129c549fbe9b3e730c3d9910492228566e39e1236945766a74381405cc57fb04\"   },   \"onepanelVersion\": {     \"release\": \"21.02.3\",     \"build\": \"3-89fc6bad\",     \"gui\": \"68e7e1472adb719ddf2d88908775091dfb10e5d0b916f06125ea1af4056044e3\"   },   \"online\": true,   \"onepanelProxy\": false,   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
cid = 'cid_example' # str | Cluster Id.

try:
    # Get user's effective cluster details
    api_response = api_instance.get_user_effective_cluster(cid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_effective_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| Cluster Id. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_effective_group**
> Group get_user_effective_group(gid)

Get effective group details

Returns information about a specific effective group to which the user has access.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user's effective group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_groups/$GROUP_ID  {   \"groupId\": \"59fec3bd894eef1cdae81623f477e370\",   \"name\": \"admins\",   \"type\": \"team\" } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
gid = 'gid_example' # str | Group Id.

try:
    # Get effective group details
    api_response = api_instance.get_user_effective_group(gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_effective_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | **str**| Group Id. | 

### Return type

[**Group**](Group.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_effective_handle**
> Handle get_user_effective_handle(hid)

Get effective handle details

Returns information about a specific effective handle to which the user has access.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective handle** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_handles/$HANDLE_ID  {   \"publicHandle\": \"10.5072/w95Zlng\",   \"handleId\": \"95b663a6467c72ab1256865efef9e387\",   \"handleServiceId\": \"97c27230017cd54c1220189e357322c4\",   \"resourceType\": \"Share\",   \"resourceId\": \"d6ee1aecf03b23f09756d6a49e435455\",   \"metadata\": \"<?xml version=\\\"1.0\\\"?>       <!DOCTYPE rdf:RDF SYSTEM \\\\\"http://dublincore.org/2000/12/01-dcmes-xml-dtd.dtd\\\">       <rdf:RDF xmlns:rdf=\\\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\\\"                xmlns:dc=\\\"http://purl.org/dc/elements/1.1/\\\">         <rdf:Description rdf:about=\\\"http://example.com/resouces/1\\\">           <dc:title>Example Resource</dc:title>           <dc:creator>John Doe</dc:creator>           <dc:publisher>MIT</dc:publisher>           <dc:date>2000-06-06</dc:date>         </rdf:Description>       </rdf:RDF>\",   \"timestamp\": \"1997-07-16T19:20\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
hid = 'hid_example' # str | Handle Id.

try:
    # Get effective handle details
    api_response = api_instance.get_user_effective_handle(hid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_effective_handle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hid** | **str**| Handle Id. | 

### Return type

[**Handle**](Handle.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_effective_handle_service**
> HandleService get_user_effective_handle_service(hsid)

Get effective handle service details

Returns information about a specific effective handle service for the user.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective handle service** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_handle_services/$HANDLE_SERVICE_ID  {     \"name\": \"MyCommunity Handle service\",     \"proxyEndpoint\": \"https://localhost:17000/handle_proxy\",     \"serviceProperties\": {         \"allowTemplateOverride\": false,         \"doiEndpoint\": \"/doi\",         \"host\": \"https://mds.test.datacite.org\",         \"identifierTemplate\": \"{{space.name}}-{{space.guid}}\",         \"mediaEndpoint\": \"/media\",         \"metadataEndpoint\": \"/metadata\",         \"password\": \"pa$$word\",         \"prefix\": 10.5072,         \"type\": \"DOI\",         \"username\": \"alice\"     } } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
hsid = 'hsid_example' # str | Handle service Id.

try:
    # Get effective handle service details
    api_response = api_instance.get_user_effective_handle_service(hsid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_effective_handle_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hsid** | **str**| Handle service Id. | 

### Return type

[**HandleService**](HandleService.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_effective_provider**
> ProviderDetails get_user_effective_provider(pid)

Get user's effective provider details

Returns information about a specific effective provider for the user.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective provider** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_providers/$PROVIDER_ID  {   \"providerId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"name\": \"Example provider\",   \"domain\": \"provider1.example.com\",   \"latitude\": 50.0647,   \"longitude\": 19.945,   \"clusterId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"online\": true,   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
pid = 'pid_example' # str | Provider Id.

try:
    # Get user's effective provider details
    api_response = api_instance.get_user_effective_provider(pid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_effective_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**| Provider Id. | 

### Return type

[**ProviderDetails**](ProviderDetails.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_group**
> Group get_user_group(gid)

Get group details

Returns information about a specific group to which the user has access.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/groups/$GROUP_ID  {   \"groupId\": \"59fec3bd894eef1cdae81623f477e370\",   \"name\": \"admins\",   \"type\": \"team\" } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
gid = 'gid_example' # str | Group Id.

try:
    # Get group details
    api_response = api_instance.get_user_group(gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | **str**| Group Id. | 

### Return type

[**Group**](Group.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_handle**
> Handle get_user_handle(hid)

Get handle details

Returns the details of a specific handle.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get handle details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/handles/$HANDLE_ID  {   \"publicHandle\": \"10.5072/w95Zlng\",   \"handleId\": \"95b663a6467c72ab1256865efef9e387\",   \"handleServiceId\": \"97c27230017cd54c1220189e357322c4\",   \"resourceType\": \"Share\",   \"resourceId\": \"d6ee1aecf03b23f09756d6a49e435455\",   \"metadata\": \"<?xml version=\\\"1.0\\\"?>       <!DOCTYPE rdf:RDF SYSTEM \\\\\"http://dublincore.org/2000/12/01-dcmes-xml-dtd.dtd\\\">       <rdf:RDF xmlns:rdf=\\\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\\\"                xmlns:dc=\\\"http://purl.org/dc/elements/1.1/\\\">         <rdf:Description rdf:about=\\\"http://example.com/resouces/1\\\">           <dc:title>Example Resource</dc:title>           <dc:creator>John Doe</dc:creator>           <dc:publisher>MIT</dc:publisher>           <dc:date>2000-06-06</dc:date>         </rdf:Description>       </rdf:RDF>\",   \"timestamp\": \"1997-07-16T19:20\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
hid = 'hid_example' # str | Handle Id.

try:
    # Get handle details
    api_response = api_instance.get_user_handle(hid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_handle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hid** | **str**| Handle Id. | 

### Return type

[**Handle**](Handle.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_handle_service**
> HandleService get_user_handle_service(hsid)

Get user handle service details

Returns the details of a specific handle service.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get handle service details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/handle_services/$HANDLE_SERVICE_ID  {     \"name\": \"MyCommunity Handle service\",     \"proxyEndpoint\": \"https://localhost:17000/handle_proxy\",     \"serviceProperties\": {         \"allowTemplateOverride\": false,         \"doiEndpoint\": \"/doi\",         \"host\": \"https://mds.test.datacite.org\",         \"identifierTemplate\": \"{{space.name}}-{{space.guid}}\",         \"mediaEndpoint\": \"/media\",         \"metadataEndpoint\": \"/metadata\",         \"password\": \"pa$$word\",         \"prefix\": 10.5072,         \"type\": \"DOI\",         \"username\": \"alice\"     } } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
hsid = 'hsid_example' # str | Handle service Id.

try:
    # Get user handle service details
    api_response = api_instance.get_user_handle_service(hsid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_handle_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hsid** | **str**| Handle service Id. | 

### Return type

[**HandleService**](HandleService.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_harvester**
> Harvester get_user_harvester(hid)

Get harvester details

Returns the details of a specific harvester.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get harvester details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/harvesters/$HARVESTER_ID  {   \"harvesterId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_harvester1\",   \"public\" : true,   \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\",   \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
hid = 'hid_example' # str | Harvester Id.

try:
    # Get harvester details
    api_response = api_instance.get_user_harvester(hid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_harvester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hid** | **str**| Harvester Id. | 

### Return type

[**Harvester**](Harvester.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_space**
> Space get_user_space(sid)

Get space details

Returns the details of a specific space.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get space details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/spaces/$SPACE_ID  {   \"spaceId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_space1\",   \"providers\": {     \"296ebe3c20e9666dc489b647f8647f12\" : 5368709120   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebfc1a770c3\"   },   \"creationTime\": 1576152793 } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
sid = 'sid_example' # str | Space Id.

try:
    # Get space details
    api_response = api_instance.get_user_space(sid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Space Id. | 

### Return type

[**Space**](Space.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_space_alias**
> SpaceAlias get_user_space_alias(sid)

Get user space alias

Returns the alias (user defined name) for a specific space. Will return 404 NOT FOUND if no alias is defined for the space.  NOTE: Space aliases are not yet implemented - setting an alias is possible but will have no effect.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get space alias** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/spaces/$SPACE_ID/alias  {   \"alias\": \"Test space 2\" } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
sid = 'sid_example' # str | Space Id.

try:
    # Get user space alias
    api_response = api_instance.get_user_space_alias(sid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_space_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Space Id. | 

### Return type

[**SpaceAlias**](SpaceAlias.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_spaces_in_effective_provider**
> Spaces get_user_spaces_in_effective_provider(pid)

Get user's spaces that are supported by given effective provider

Returns the list of user's spaces that are supported by given effective provider.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user's spaces supported by effective provider** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_providers/$PROVIDER_ID/spaces  {   \"spaces\": [     \"6825604b0eb6a47b8b7a04b6369eb24d\"   ] } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
pid = 'pid_example' # str | Provider Id.

try:
    # Get user's spaces that are supported by given effective provider
    api_response = api_instance.get_user_spaces_in_effective_provider(pid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_spaces_in_effective_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**| Provider Id. | 

### Return type

[**Spaces**](Spaces.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_group**
> join_group(body)

Join group

Join existing group using an invitation token.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Join group**  ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"token\": \"9ef3973a007d616cb6b3e95829dec18a\" }' \\ https://$ZONE_HOST/api/v3/onezone/user/groups/join ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
body = onezone_client.GroupInviteToken() # GroupInviteToken | Token for joining a group.

try:
    # Join group
    api_instance.join_group(body)
except ApiException as e:
    print("Exception when calling UserApi->join_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupInviteToken**](GroupInviteToken.md)| Token for joining a group. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_harvester**
> join_harvester(body)

Join harvester

Join existing harvester using invitation token.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Join existing harvester** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"token\" : \"MDAxNmxvY2F00aW9uRVM2TVo5UlZ5cGFjZV9jcmLciFsOgyUkPI3f02le6PM01IX8go\" }'  \\ https://$ZONE_HOST/api/v3/onezone/user/harvesters/join ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
body = onezone_client.HarvesterInviteToken() # HarvesterInviteToken | Token for joining a harvester.

try:
    # Join harvester
    api_instance.join_harvester(body)
except ApiException as e:
    print("Exception when calling UserApi->join_harvester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HarvesterInviteToken**](HarvesterInviteToken.md)| Token for joining a harvester. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_space**
> join_space(body)

Join space

Join existing space using an invitation token.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Join an existing space** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"token\" : \"MDAxNmxvY2F00aW9uRVM2TVo5UlZ5cGFjZV9jcmLciFsOgyUkPI3f02le6PM01IX8go\" }'  \\ https://$ZONE_HOST/api/v3/onezone/user/spaces/join ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
body = onezone_client.SpaceInviteToken() # SpaceInviteToken | Token for joining a space.

try:
    # Join space
    api_instance.join_space(body)
except ApiException as e:
    print("Exception when calling UserApi->join_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpaceInviteToken**](SpaceInviteToken.md)| Token for joining a space. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leave_group**
> leave_group(gid)

Leave group

Removes the current user from a specific group.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Leave group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/groups/$GROUP_ID ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
gid = 'gid_example' # str | Group Id.

try:
    # Leave group
    api_instance.leave_group(gid)
except ApiException as e:
    print("Exception when calling UserApi->leave_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | **str**| Group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leave_handle_service**
> leave_handle_service(hsid)

Leave handle service

Removes the user's ownership or access to a specific handle service.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Delete user handle service** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/handle_services/$HANDLE_SERVICE_ID ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
hsid = 'hsid_example' # str | Handle service Id.

try:
    # Leave handle service
    api_instance.leave_handle_service(hsid)
except ApiException as e:
    print("Exception when calling UserApi->leave_handle_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hsid** | **str**| Handle service Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leave_space**
> leave_space(sid)

Leave space

Removes the user's ownership or access to a specific space.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Delete user space** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/spaces/$SPACE_ID ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
sid = 'sid_example' # str | Space Id.

try:
    # Leave space
    api_instance.leave_space(sid)
except ApiException as e:
    print("Exception when calling UserApi->leave_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Space Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_tokens**
> ClientTokens list_client_tokens()

List user access tokens

This enpoint is deprecated and will be removed in future release, please use [this one](#operation/list_named_tokens_of_current_user).  Returns the list of user tokens.  This operation can be invoked on behalf of currently authenticated user only.  ***Example cURL requests***  **Get user tokens** ```bash curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/user/client_tokens  {   \"tokens: [      \"12da582337ff25cc86db30580b20d3cd\"   ] } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # List user access tokens
    api_response = api_instance.list_client_tokens()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_client_tokens: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClientTokens**](ClientTokens.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_current_user_admin_privileges**
> InlineResponse2001 list_current_user_admin_privileges()

List current user privileges

Returns the list of currently authenticated user's admin privileges in Onezone.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **List current user's admin privileges in Onezone** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/user/privileges  {   \"privileges\": [     \"oz_view_privileges\",     \"oz_users_list\",     \"oz_users_view\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handles_list\",     \"oz_handles_view\"   ] } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # List current user privileges
    api_response = api_instance.list_current_user_admin_privileges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_current_user_admin_privileges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_current_user_effective_admin_privileges**
> InlineResponse2001 list_current_user_effective_admin_privileges()

List current user effective privileges

Returns the list of currently authenticated user's admin privileges in Onezone.  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **List user's effective admin privileges in Onezone** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/user/effective_privileges  {   \"privileges\": [     \"oz_view_privileges\",     \"oz_users_list\",     \"oz_users_view\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handles_list\",     \"oz_handles_view\"   ] } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # List current user effective privileges
    api_response = api_instance.list_current_user_effective_admin_privileges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_current_user_effective_admin_privileges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_user_groups**
> Groups list_effective_user_groups()

List effective user groups

Returns the list of user's effective groups.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective groups** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_groups  {   \"groups\": [     \"admins\"   ] } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # List effective user groups
    api_response = api_instance.list_effective_user_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_effective_user_groups: %s\n" % e)
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

# **list_effective_user_harvesters**
> Harvesters list_effective_user_harvesters()

List effective user harvesters

Returns the list of user's effective harvesters.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective harvesters** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_harvesters  {   \"harvesters\": [     \"40090ed592dc7975d2a9cd6bbe6c9a67\"   ] } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # List effective user harvesters
    api_response = api_instance.list_effective_user_harvesters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_effective_user_harvesters: %s\n" % e)
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

# **list_effective_user_providers**
> Providers list_effective_user_providers()

List user effective providers

Returns the list of user's effective providers.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective providers** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_providers  {   \"providers\": [     \"LKJASHGDFKLJHASKLJDH\"   ] } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # List user effective providers
    api_response = api_instance.list_effective_user_providers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_effective_user_providers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Providers**](Providers.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_user_spaces**
> Spaces list_effective_user_spaces()

List effective user spaces

Returns the list of user's effective spaces.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective spaces** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_spaces  {   \"spaces\": [     \"40090ed592dc7975d2a9cd6bbe6c9a67\"   ] } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # List effective user spaces
    api_response = api_instance.list_effective_user_spaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_effective_user_spaces: %s\n" % e)
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

# **list_user_admin_privileges**
> InlineResponse2001 list_user_admin_privileges(id)

List user admin privileges

Returns the list of user's (`{id}`) admin privileges in Onezone.  This operation requires `oz_view_privileges` admin privilege.  ***Example cURL requests***  **List user's admin privileges in Onezone** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/privileges  {   \"privileges\": [     \"oz_view_privileges\",     \"oz_users_list\",     \"oz_users_view\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handles_list\",     \"oz_handles_view\"   ] } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | User Id.

try:
    # List user admin privileges
    api_response = api_instance.list_user_admin_privileges(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_admin_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User Id. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_clusters**
> Clusters list_user_clusters()

List user's clusters

Returns the list of user's clusters.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user's clusters** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/clusters  {   \"clusters\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # List user's clusters
    api_response = api_instance.list_user_clusters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_clusters: %s\n" % e)
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

# **list_user_effective_admin_privileges**
> InlineResponse2001 list_user_effective_admin_privileges(id)

List user's effective admin privileges

Returns the list of user's (`{id}`) admin privileges in Onezone.  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation requires `oz_view_privileges` admin privilege.  ***Example cURL requests***  **List user's effective admin privileges in Onezone** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/effective_privileges   {   \"privileges\": [     \"oz_view_privileges\",     \"oz_users_list\",     \"oz_users_view\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handles_list\",     \"oz_handles_view\"   ] } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | User Id.

try:
    # List user's effective admin privileges
    api_response = api_instance.list_user_effective_admin_privileges(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_effective_admin_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User Id. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_effective_clusters**
> Clusters list_user_effective_clusters()

List user's effective clusters

Returns the list of user's effective clusters.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user's effective clusters** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_clusters  {   \"clusters\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # List user's effective clusters
    api_response = api_instance.list_user_effective_clusters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_effective_clusters: %s\n" % e)
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

# **list_user_effective_handle_services**
> HandleServices list_user_effective_handle_services()

List user effective handle services

Returns the list of user's effective handle services.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective handle services** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_handle_services  {   \"handle_services\": [     \"LKJASHGDFKLJHASKLJDH\"   ] } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # List user effective handle services
    api_response = api_instance.list_user_effective_handle_services()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_effective_handle_services: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HandleServices**](HandleServices.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_effective_handles**
> Handles list_user_effective_handles()

Get user effective handles

Returns the list of user's effective handles.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective handles** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_handles  {   \"handles\": [     \"8f8304077af3a834f0d484cd673073f0\"   ] } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # Get user effective handles
    api_response = api_instance.list_user_effective_handles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_effective_handles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Handles**](Handles.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_groups**
> Groups list_user_groups()

List user groups

Returns the list of user's groups.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user groups** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/groups  {   \"groups\": [     \"13c6bf68ed88dd01f396571f976b148d\"   ] } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # List user groups
    api_response = api_instance.list_user_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_groups: %s\n" % e)
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

# **list_user_handle_services**
> HandleServices list_user_handle_services()

List user handle services

Returns the list of registered user handle services.  ***Example cURL requests***  **Get user handle services** ```bash curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/user/handle_services  {   \"handle_services\": [     \"0fe7c8a20ffdf07480c46f084bc3b8d5\",     \"302da048de67e2ea05f0af1d0fe7c8a2\"   ] } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # List user handle services
    api_response = api_instance.list_user_handle_services()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_handle_services: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HandleServices**](HandleServices.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_handles**
> Handles list_user_handles()

List user handles

Returns the list of users' handles.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user handles** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/handles  {   \"handles\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # List user handles
    api_response = api_instance.list_user_handles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_handles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Handles**](Handles.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_harvesters**
> InlineResponse2003 list_user_harvesters()

List user harvesters

Returns the list of users' harvesters.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user harvesters** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/harvesters  {   \"harvesters\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # List user harvesters
    api_response = api_instance.list_user_harvesters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_harvesters: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_spaces**
> InlineResponse2002 list_user_spaces()

List user spaces

Returns the list of users' spaces.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user spaces** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/spaces  {   \"spaces\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # List user spaces
    api_response = api_instance.list_user_spaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_spaces: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_current_user**
> modify_current_user(body)

Modify current user

Modifies user account details based on information provided in the request body.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Change user fullName** ```bash curl -u username:password -H \"Content-type: application/json\" -X PATCH  \\ -d '{\"fullName\": \"John Doe\"}' \\ https://$ZONE_HOST/api/v3/onezone/user ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
body = onezone_client.UserUpdateRequest() # UserUpdateRequest | User data.

try:
    # Modify current user
    api_instance.modify_current_user(body)
except ApiException as e:
    print("Exception when calling UserApi->modify_current_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserUpdateRequest**](UserUpdateRequest.md)| User data. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oz_users_list**
> Users oz_users_list()

List all users

Returns the list of all users in the system.  Requires `oz_users_list` admin privilege.  ***Example cURL requests***  **List all users in the system** ```bash  curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/users ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # List all users
    api_response = api_instance.oz_users_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->oz_users_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Users**](Users.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_client_token**
> remove_client_token(tid)

Delete access token

This enpoint is deprecated and will be removed in future release, please use [this one](#operation/delete_named_token_of_current_user).  Removes a specific access token.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Delete user access token** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/client_tokens/PMPs42mROSS7Rg7z7BwU9JYpSof4SvIW5v14uQY8X08 ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
tid = 'tid_example' # str | Token.

try:
    # Delete access token
    api_instance.remove_client_token(tid)
except ApiException as e:
    print("Exception when calling UserApi->remove_client_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tid** | **str**| Token. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_current_user**
> remove_current_user()

Remove current user

Removes the account of currently authenticated user.  ***Example cURL requests***  **Remove user account** ```bash curl -u username:password -X DELETE  \\ https://$ZONE_HOST/api/v3/onezone/user ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # Remove current user
    api_instance.remove_current_user()
except ApiException as e:
    print("Exception when calling UserApi->remove_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_current_user_admin_privileges**
> remove_current_user_admin_privileges()

Remove current user's admin privileges

Removes all currently authenticated user's admin privileges in Onezone.  This operation can be invoked on behalf of the current user only and requires `oz_set_privileges` admin privilege.  ***Example cURL requests***  **Remove all user's admin privileges in Onezone** ```bash curl -u username:password  -X DELETE  \\ https://$ZONE_HOST/api/v3/onezone/users/privileges ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))

try:
    # Remove current user's admin privileges
    api_instance.remove_current_user_admin_privileges()
except ApiException as e:
    print("Exception when calling UserApi->remove_current_user_admin_privileges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user**
> remove_user(id)

Remove user

Removes a specific user.  This operation requires `oz_users_delete` admin privilege.  ***Example cURL requests***  **Remove user** ```bash curl -u admin:password -X DELETE  \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | User Id.

try:
    # Remove user
    api_instance.remove_user(id)
except ApiException as e:
    print("Exception when calling UserApi->remove_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_admin_privileges**
> remove_user_admin_privileges(id)

Remove user's admin privileges

Removes all user's (`{id}`) admin privileges in Onezone.  This operation requires `oz_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Removes all user's admin privileges in Onezone** ```bash curl -u username:password -X DELETE  \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/privileges ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | User Id.

try:
    # Remove user's admin privileges
    api_instance.remove_user_admin_privileges(id)
except ApiException as e:
    print("Exception when calling UserApi->remove_user_admin_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_handle**
> remove_user_handle(hid)

Leave handle

Removes the user's ownership or access to a specific space.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Delete user space** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/handles/$HANDLE_ID ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
hid = 'hid_example' # str | Handle Id.

try:
    # Leave handle
    api_instance.remove_user_handle(hid)
except ApiException as e:
    print("Exception when calling UserApi->remove_user_handle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hid** | **str**| Handle Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_space_alias**
> remove_user_space_alias(sid)

Remove space alias

Removes the alias (user defined name) for a specific space.  NOTE: Space aliases are not yet implemented - setting an alias is possible but will have no effect.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Remove user space alias** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/spaces/$SPACE_ID/alias ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
sid = 'sid_example' # str | Space Id.

try:
    # Remove space alias
    api_instance.remove_user_space_alias(sid)
except ApiException as e:
    print("Exception when calling UserApi->remove_user_space_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Space Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_space_alias**
> SpaceAlias set_user_space_alias(body, sid)

Set user space alias

Sets the alias (user defined name) for a specific space.  NOTE: Space aliases are not yet implemented - setting an alias is possible but will have no effect.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Set space alias** ```bash curl -u username:password -X PUT -d '{\"alias\": \"Space alias\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/user/spaces/$SPACE_ID/alias ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
body = onezone_client.SpaceAlias() # SpaceAlias | New space alias.
sid = 'sid_example' # str | Space Id.

try:
    # Set user space alias
    api_response = api_instance.set_user_space_alias(body, sid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->set_user_space_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpaceAlias**](SpaceAlias.md)| New space alias. | 
 **sid** | **str**| Space Id. | 

### Return type

[**SpaceAlias**](SpaceAlias.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_user_access_block**
> toggle_user_access_block(body, id)

Block or unblock user access

Allows to block or unblock access to Onedata services for a specific user.  This operation requires `oz_users_update` admin privilege.  ***Example cURL requests***  **Block or unblock user access** ```bash curl -u admin:password -X PATCH https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/access_block \\ -H \"Content-Type: application/json\" -d '{\"blocked\": true}' ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
body = onezone_client.UserAccessBlockUpdate() # UserAccessBlockUpdate | User access block modification request.
id = 'id_example' # str | User Id.

try:
    # Block or unblock user access
    api_instance.toggle_user_access_block(body, id)
except ApiException as e:
    print("Exception when calling UserApi->toggle_user_access_block: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAccessBlockUpdate**](UserAccessBlockUpdate.md)| User access block modification request. | 
 **id** | **str**| User Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_current_user_admin_privileges**
> update_current_user_admin_privileges(body=body)

Update current user's admin privileges

Updates currently authenticated user's admin privileges in Onezone.  This operation can be invoked on behalf of the current user only and requires `oz_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Updates current user's admin privileges in Onezone** ```bash curl -u username:password -H \"Content-type: application/json\" -X PATCH \\ -d '{\"grant\": [\"oz_spaces_list\"], \"revoke\": [\"oz_groups_update\"]}' \\ https://$ZONE_HOST/api/v3/onezone/user/privileges ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
body = onezone_client.AdminPrivilegesUpdate() # AdminPrivilegesUpdate | User admin privileges. (optional)

try:
    # Update current user's admin privileges
    api_instance.update_current_user_admin_privileges(body=body)
except ApiException as e:
    print("Exception when calling UserApi->update_current_user_admin_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminPrivilegesUpdate**](AdminPrivilegesUpdate.md)| User admin privileges. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_admin_privileges**
> update_user_admin_privileges(id, body=body)

Update user's admin privileges

Updates user's (`{id}`) admin privileges in Onezone.  This operation requires `oz_set_privileges` admin privilege.  ***Example cURL requests***  **Updates user's admin privileges in Onezone** ```bash curl -u username:password -H \"Content-type: application/json\" -X PATCH \\ -d '{\"grant\": [\"oz_spaces_list\"], \"revoke\": [\"oz_groups_update\"]}' \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/privileges ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | User Id.
body = onezone_client.AdminPrivilegesUpdate() # AdminPrivilegesUpdate | User admin privileges. (optional)

try:
    # Update user's admin privileges
    api_instance.update_user_admin_privileges(id, body=body)
except ApiException as e:
    print("Exception when calling UserApi->update_user_admin_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User Id. | 
 **body** | [**AdminPrivilegesUpdate**](AdminPrivilegesUpdate.md)| User admin privileges. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_join_cluster**
> user_join_cluster(body)

Join cluster

Join an existing cluster using an inivitation token.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Join an existing cluster** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"token\" : \"MDAxNmxvY2F00aW9uRVM2TVo5UlZ5cGFjZV9jcmLciFsOgyUkPI3f02le6PM01IX8go\" }'  \\ https://$ZONE_HOST/api/v3/onezone/user/clusters/join ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
body = onezone_client.ClusterInviteToken() # ClusterInviteToken | Token for joining a cluster.

try:
    # Join cluster
    api_instance.user_join_cluster(body)
except ApiException as e:
    print("Exception when calling UserApi->user_join_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterInviteToken**](ClusterInviteToken.md)| Token for joining a cluster. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_leave_cluster**
> user_leave_cluster(cid)

Leave cluster

Removes the users membership in a specific cluster.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **User leave cluster** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/clusters/$CLUSTER_ID ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
cid = 'cid_example' # str | Cluster Id.

try:
    # Leave cluster
    api_instance.user_leave_cluster(cid)
except ApiException as e:
    print("Exception when calling UserApi->user_leave_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| Cluster Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_leave_harvester**
> user_leave_harvester(hid)

Leave harvester

Removes the users ownership or access to a specific harvester.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Delete user harvester** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/harvesters/$HARVESTER_ID ``` 

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
api_instance = onezone_client.UserApi(onezone_client.ApiClient(configuration))
hid = 'hid_example' # str | Harvester Id.

try:
    # Leave harvester
    api_instance.user_leave_harvester(hid)
except ApiException as e:
    print("Exception when calling UserApi->user_leave_harvester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hid** | **str**| Harvester Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

