# onezone_client.HandleApi

All URIs are relative to */api/v3/onezone*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_handle_group**](HandleApi.md#add_handle_group) | **PUT** /handles/{id}/groups/{gid} | Add handle group
[**add_handle_user**](HandleApi.md#add_handle_user) | **PUT** /handles/{id}/users/{uid} | Add handle user
[**get_effective_handle_group**](HandleApi.md#get_effective_handle_group) | **GET** /handles/{id}/effective_groups/{gid} | Get effective handle group
[**get_effective_handle_user**](HandleApi.md#get_effective_handle_user) | **GET** /handles/{id}/effective_users/{uid} | Get effective handle user
[**get_handle**](HandleApi.md#get_handle) | **GET** /handles/{id} | Get handle
[**get_handle_group**](HandleApi.md#get_handle_group) | **GET** /handles/{id}/groups/{gid} | Get handle group
[**get_handle_user**](HandleApi.md#get_handle_user) | **GET** /handles/{id}/users/{uid} | Get handle user
[**get_public_handle_details**](HandleApi.md#get_public_handle_details) | **GET** /handles/{id}/public | Get public handle details
[**handle_service_register_handle**](HandleApi.md#handle_service_register_handle) | **POST** /handles | Register handle
[**handle_update**](HandleApi.md#handle_update) | **PATCH** /handles/{id} | Modify handle
[**list_effective_group_handle_privileges**](HandleApi.md#list_effective_group_handle_privileges) | **GET** /handles/{id}/effective_groups/{gid}/privileges | List effective group&#x27;s handle privileges
[**list_effective_handle_groups**](HandleApi.md#list_effective_handle_groups) | **GET** /handles/{id}/effective_groups | Get effective handle groups
[**list_effective_handle_users**](HandleApi.md#list_effective_handle_users) | **GET** /handles/{id}/effective_users | List effective handle users
[**list_effective_user_handle_privileges**](HandleApi.md#list_effective_user_handle_privileges) | **GET** /handles/{id}/effective_users/{uid}/privileges | List effective user&#x27;s handle privileges
[**list_group_handle_privileges**](HandleApi.md#list_group_handle_privileges) | **GET** /handles/{id}/groups/{gid}/privileges | List group&#x27;s handle privileges
[**list_handle_groups**](HandleApi.md#list_handle_groups) | **GET** /handles/{id}/groups | List handle groups
[**list_handle_privileges**](HandleApi.md#list_handle_privileges) | **GET** /handles/privileges | List all handle privileges
[**list_handle_users**](HandleApi.md#list_handle_users) | **GET** /handles/{id}/users | List handle users
[**list_handles**](HandleApi.md#list_handles) | **GET** /handles | List handles
[**list_user_handle_privileges**](HandleApi.md#list_user_handle_privileges) | **GET** /handles/{id}/users/{uid}/privileges | List user handle privileges
[**remove_handle**](HandleApi.md#remove_handle) | **DELETE** /handles/{id} | Unregister handle
[**remove_handle_group**](HandleApi.md#remove_handle_group) | **DELETE** /handles/{id}/groups/{gid} | Remove handle group
[**remove_handle_user**](HandleApi.md#remove_handle_user) | **DELETE** /handles/{id}/users/{uid} | Remove handle user
[**update_group_handle_privileges**](HandleApi.md#update_group_handle_privileges) | **PATCH** /handles/{id}/groups/{gid}/privileges | Update handle groups privileges
[**update_handle_user_privileges**](HandleApi.md#update_handle_user_privileges) | **PATCH** /handles/{id}/users/{uid}/privileges | Update user handle privileges

# **add_handle_group**
> add_handle_group(id, gid, body=body)

Add handle group

Allows to add a group to a handle.  This operation requires `handle_update` privilege or `oz_handles_add_relationships` and `oz_groups_add_relationships` admin privilege.  ***Example cURL requests***  **Add handle group** ```bash curl -u username:password -X PUT \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/groups/$GROUP_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle Id.
gid = 'gid_example' # str | The Id of the group to add to handle.
body = onezone_client.GroupsGidBody2() # GroupsGidBody2 |  (optional)

try:
    # Add handle group
    api_instance.add_handle_group(id, gid, body=body)
except ApiException as e:
    print("Exception when calling HandleApi->add_handle_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle Id. | 
 **gid** | **str**| The Id of the group to add to handle. | 
 **body** | [**GroupsGidBody2**](GroupsGidBody2.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_handle_user**
> add_handle_user(id, uid, body=body)

Add handle user

Allows to add a user to a handle.  This operation requires `handle_update` privilege or `oz_handles_add_relationships` and `oz_users_add_relationships` admin privilege.  ***Example cURL requests***  **Add handle user** ```bash curl -u username:password -X PUT \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/users/$USER_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle Id.
uid = 'uid_example' # str | The Id of the user to add to handle.
body = onezone_client.UsersUidBody3() # UsersUidBody3 |  (optional)

try:
    # Add handle user
    api_instance.add_handle_user(id, uid, body=body)
except ApiException as e:
    print("Exception when calling HandleApi->add_handle_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle Id. | 
 **uid** | **str**| The Id of the user to add to handle. | 
 **body** | [**UsersUidBody3**](UsersUidBody3.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_handle_group**
> Group get_effective_handle_group(id, gid)

Get effective handle group

Returns the details of an effective group with access to handle.  This operation requires `handle_view` privilege or `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get effective handle group** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/effective_groups/$GROUP_ID  {   \"groupId\":\"HwUpk8jrwxKOe45uzLFX2GVa8lKEasj4q253sptVqF8\",   \"name\":\"Group name\",   \"type\":\"team\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle Id.
gid = 'gid_example' # str | The Id of the group to add to handle.

try:
    # Get effective handle group
    api_response = api_instance.get_effective_handle_group(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleApi->get_effective_handle_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle Id. | 
 **gid** | **str**| The Id of the group to add to handle. | 

### Return type

[**Group**](Group.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_handle_user**
> User get_effective_handle_user(id, uid)

Get effective handle user

Returns effective handle user details.  This operation requires `handle_view` privilege or `oz_users_view` admin privilege.  ***Example cURL requests***  **Add handle user** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/effective_users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle Id.
uid = 'uid_example' # str | The Id of the user to add to handle.

try:
    # Get effective handle user
    api_response = api_instance.get_effective_handle_user(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleApi->get_effective_handle_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle Id. | 
 **uid** | **str**| The Id of the user to add to handle. | 

### Return type

[**User**](User.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_handle**
> Handle get_handle(id)

Get handle

Returns the details of a specific handle.  This operation requires `handle_view` privilege or `oz_handles_view` admin privilege.  ***Example cURL requests***  **Get handle** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID  {   \"publicHandle\": \"10.5072/w95Zlng\",   \"handleId\": \"95b663a6467c72ab1256865efef9e387\",   \"handleServiceId\": \"97c27230017cd54c1220189e357322c4\",   \"resourceType\": \"Share\",   \"resourceId\": \"d6ee1aecf03b23f09756d6a49e435455\",   \"metadata\": \"<?xml version=\\\"1.0\\\"?>       <!DOCTYPE rdf:RDF SYSTEM \\\\\"http://dublincore.org/2000/12/01-dcmes-xml-dtd.dtd\\\">       <rdf:RDF xmlns:rdf=\\\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\\\"                xmlns:dc=\\\"http://purl.org/dc/elements/1.1/\\\">         <rdf:Description rdf:about=\\\"http://example.com/resouces/1\\\">           <dc:title>Example Resource</dc:title>           <dc:creator>John Doe</dc:creator>           <dc:publisher>MIT</dc:publisher>           <dc:date>2000-06-06</dc:date>         </rdf:Description>       </rdf:RDF>\",   \"timestamp\": \"1997-07-16T19:20\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | The handle Id.

try:
    # Get handle
    api_response = api_instance.get_handle(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleApi->get_handle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The handle Id. | 

### Return type

[**Handle**](Handle.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_handle_group**
> Group get_handle_group(id, gid)

Get handle group

Returns the details of a group with access to handle.  This operation requires `handle_view` privilege or `oz_groups_view` admin privilege.  ***Example cURL requests***  **Add handle group** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/groups/$GROUP_ID  {   \"groupId\":\"HwUpk8jrwxKOe45uzLFX2GVa8lKEasj4q253sptVqF8\",   \"name\":\"Group name\",   \"type\":\"team\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle Id.
gid = 'gid_example' # str | The Id of the group to add to handle.

try:
    # Get handle group
    api_response = api_instance.get_handle_group(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleApi->get_handle_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle Id. | 
 **gid** | **str**| The Id of the group to add to handle. | 

### Return type

[**Group**](Group.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_handle_user**
> User get_handle_user(id, uid)

Get handle user

Allows to add a user to a handle.  This operation requires `handle_view` privilege or `oz_users_view` admin privilege.  ***Example cURL requests***  **Get handle user** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle Id.
uid = 'uid_example' # str | The Id of the user to add to handle.

try:
    # Get handle user
    api_response = api_instance.get_handle_user(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleApi->get_handle_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle Id. | 
 **uid** | **str**| The Id of the user to add to handle. | 

### Return type

[**User**](User.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_handle_details**
> Handle get_public_handle_details(id)

Get public handle details

Returns the publicly available details of a specific handle. This endpoint is available for anyone knowing the handle Id, without authentication.  ***Example cURL requests***  **Get public handle details** ```bash curl -X GET https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/public  {   \"handleId\": \"95b663a6467c72ab1256865efef9e387\",   \"publicHandle\": \"10.5072/w95Zlng\",   \"resourceType\": \"Share\",   \"resourceId\": \"d6ee1aecf03b23f09756d6a49e435455\",   \"metadata\": \"<?xml version=\\\"1.0\\\"?>       <!DOCTYPE rdf:RDF SYSTEM \\\\\"http://dublincore.org/2000/12/01-dcmes-xml-dtd.dtd\\\">       <rdf:RDF xmlns:rdf=\\\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\\\"                xmlns:dc=\\\"http://purl.org/dc/elements/1.1/\\\">         <rdf:Description rdf:about=\\\"http://example.com/resouces/1\\\">           <dc:title>Example Resource</dc:title>           <dc:creator>John Doe</dc:creator>           <dc:publisher>MIT</dc:publisher>           <dc:date>2000-06-06</dc:date>         </rdf:Description>       </rdf:RDF>\",   \"timestamp\": \"1997-07-16T19:20\",   \"creationTime\": 1576152793 } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | The handle Id.

try:
    # Get public handle details
    api_response = api_instance.get_public_handle_details(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleApi->get_public_handle_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The handle Id. | 

### Return type

[**Handle**](Handle.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_service_register_handle**
> handle_service_register_handle(body)

Register handle

Allows to register a new handle identifier, using a specific handle service.  The handle service must be registered in Onedata separately.  See also:   [Create a new handle for the current user](#operation/create_user_handle)   [Create a new handle for given group](#operation/create_group_handle)    This operation requires `handle_service_register_handle` privilege, which needs to be assigned to a specific handle service or `oz_handles_create` admin privilege.  ***Example cURL requests***  **Register handle** ```bash curl -u username:password -X POST -H \"Content-type: application/json\" \\ -d '{ \"handleServiceId\": \"ddb06ed993bae95f2f430664fff122f7\", \"resourceType\": \"Share\", \"resourceId\": \"4fa683cbda8d8f686d15d42720af431d\", \"metadata\": \"<?xml version=\\'1.0\\'?>...\" }' \\ https://$ZONE_HOST/api/v3/onezone/handles ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
body = onezone_client.HandleRegistrationRequest() # HandleRegistrationRequest | 

try:
    # Register handle
    api_instance.handle_service_register_handle(body)
except ApiException as e:
    print("Exception when calling HandleApi->handle_service_register_handle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HandleRegistrationRequest**](HandleRegistrationRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_update**
> handle_update(body, id)

Modify handle

Allows to update a registered handle, currently it only allows to modify the handle metadata property.  This operation requires `handle_update` privilege or `oz_handles_update` admin privilege.  ***Example cURL requests***  **Modify handle resource** ```bash curl -u username:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"metadata\": \"<?xml...\"}' \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
body = onezone_client.HandlesIdBody() # HandlesIdBody | 
id = 'id_example' # str | 

try:
    # Modify handle
    api_instance.handle_update(body, id)
except ApiException as e:
    print("Exception when calling HandleApi->handle_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HandlesIdBody**](HandlesIdBody.md)|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_group_handle_privileges**
> InlineResponse20016 list_effective_group_handle_privileges(id, gid)

List effective group's handle privileges

Returns the list of effective group's (`{gid}`) privileges in a handle (`{id}`).  Effective privileges are a sum of group's privileges and privileges inherited from its parent group memberships.  This operation requires `handle_view` privilege or `oz_handles_view_privileges` admin privilege.  ***Example cURL requests***  **List effective group's privileges in a handle** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/effective_groups/$GROUP_ID/privileges  {   \"privileges\": [     \"handle_delete\",     \"handle_update\",     \"handle_view\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle Id.
gid = 'gid_example' # str | Group Id.

try:
    # List effective group's handle privileges
    api_response = api_instance.list_effective_group_handle_privileges(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleApi->list_effective_group_handle_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle Id. | 
 **gid** | **str**| Group Id. | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_handle_groups**
> Groups list_effective_handle_groups(id)

Get effective handle groups

Returns effective groups with access to a handle instance.  This operation requires `handle_view` privilege or `oz_handles_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/effective_groups  {   \"groups\": [     \"16969b9d4d1f1457b7c1d061022f6b96\",     \"a6c6e47cc477aa4d3f8c61ce71df9850\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle Id.

try:
    # Get effective handle groups
    api_response = api_instance.list_effective_handle_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleApi->list_effective_handle_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle Id. | 

### Return type

[**Groups**](Groups.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_handle_users**
> Users list_effective_handle_users(id)

List effective handle users

Returns effective list of users with access to a handle instance.  This operation requires `handle_view` privilege or `oz_handles_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/effective_users  {   \"users\": [     \"5bcd19ea6b3e308347fd12ccefc96b09\",     \"cef7eb7463ed17acd3ffd9bc53b796ea\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle Id.

try:
    # List effective handle users
    api_response = api_instance.list_effective_handle_users(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleApi->list_effective_handle_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle Id. | 

### Return type

[**Users**](Users.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_user_handle_privileges**
> InlineResponse20016 list_effective_user_handle_privileges(id, uid)

List effective user's handle privileges

Returns the list of effective user's (`{uid}`) privileges in a handle (`{id}`).  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation requires `handle_view` privilege or `oz_handles_view_privileges` admin privilege.  ***Example cURL requests***  **List effective user's privileges in a handle** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/effective_users/$USER_ID/privileges  {   \"privileges\": [     \"handle_delete\",     \"handle_update\",     \"handle_view\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle Id.
uid = 'uid_example' # str | User Id.

try:
    # List effective user's handle privileges
    api_response = api_instance.list_effective_user_handle_privileges(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleApi->list_effective_user_handle_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_handle_privileges**
> InlineResponse20016 list_group_handle_privileges(id, gid)

List group's handle privileges

Returns the list of group's (`{gid}`) privileges in a handle (`{id}`).  This operation requires `handle_view` privilege or `oz_handles_view_privileges` admin privilege.  ***Example cURL requests***  **List group's privileges in a handle** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/groups/$GROUP_ID/privileges  {   \"privileges\": [     \"handle_delete\",     \"handle_update\",     \"handle_view\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle Id.
gid = 'gid_example' # str | Group Id.

try:
    # List group's handle privileges
    api_response = api_instance.list_group_handle_privileges(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleApi->list_group_handle_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle Id. | 
 **gid** | **str**| Group Id. | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_handle_groups**
> Groups list_handle_groups(id)

List handle groups

Returns all groups with access to a handle instance  This operation requires `handle_view` privilege or `oz_handles_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/groups  {   \"groups\": [     \"16969b9d4d1f1457b7c1d061022f6b96\",     \"a6c6e47cc477aa4d3f8c61ce71df9850\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle Id.

try:
    # List handle groups
    api_response = api_instance.list_handle_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleApi->list_handle_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle Id. | 

### Return type

[**Groups**](Groups.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_handle_privileges**
> InlineResponse20015 list_handle_privileges()

List all handle privileges

Returns list of all possible handle privileges.  This endpoint does not require authentication.  ***Example cURL requests***  **Get list of all handle privileges** ```bash curl https://$ZONE_HOST/api/v3/onezone/handles/privileges  {   \"admin\": [     \"handle_view\",     \"handle_update\",     \"handle_delete\"   ],   \"member\": [     \"handle_view\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))

try:
    # List all handle privileges
    api_response = api_instance.list_handle_privileges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleApi->list_handle_privileges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_handle_users**
> Users list_handle_users(id)

List handle users

Returns all users with access to a handle instance  This operation requires `handle_view` privilege or `oz_handles_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/users  {   \"users\": [     \"5bcd19ea6b3e308347fd12ccefc96b09\",     \"cef7eb7463ed17acd3ffd9bc53b796ea\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle Id.

try:
    # List handle users
    api_response = api_instance.list_handle_users(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleApi->list_handle_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle Id. | 

### Return type

[**Users**](Users.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_handles**
> Handles list_handles()

List handles

Returns the list of Ids of all handles registered in Onezone.  This operation requires `oz_handles_list` admin privilege.  ***Example cURL requests***  **Get handles** ```bash curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/handles  {   \"handles\": [     \"0fe7c8a20ffdf07480c46f084bc3b8d5\",     \"302da048de67e2ea05f0af1d0fe7c8a2\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))

try:
    # List handles
    api_response = api_instance.list_handles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleApi->list_handles: %s\n" % e)
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

# **list_user_handle_privileges**
> InlineResponse20016 list_user_handle_privileges(id, uid)

List user handle privileges

Returns the list of user's (`{uid}`) privileges in a handle (`{id}`).  This operation requires `handle_view` privilege or `oz_handles_view_privileges` admin privilege.  ***Example cURL requests***  **List handle user privileges** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/users/$USER_ID/privileges  {   \"privileges\": [     \"handle_delete\",     \"handle_update\",     \"handle_view\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle Id.
uid = 'uid_example' # str | User Id.

try:
    # List user handle privileges
    api_response = api_instance.list_user_handle_privileges(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleApi->list_user_handle_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_handle**
> remove_handle(id)

Unregister handle

Allows to unregister a registered handle.  This operation requires `handle_delete` privilege or `oz_handles_delete` admin privilege.  ***Example cURL requests***  **Unregister handle** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Unregister handle
    api_instance.remove_handle(id)
except ApiException as e:
    print("Exception when calling HandleApi->remove_handle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_handle_group**
> remove_handle_group(id, gid)

Remove handle group

Allows to remove a group from access to a handle.  This operation requires `handle_update` privilege or `oz_handles_remove_relationships` and `oz_groups_remove_relationships` admin privilege.  ***Example cURL requests***  **Remove handle service group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/groups/$GROUP_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle Id.
gid = 'gid_example' # str | The Id of the group to remove from handle.

try:
    # Remove handle group
    api_instance.remove_handle_group(id, gid)
except ApiException as e:
    print("Exception when calling HandleApi->remove_handle_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle Id. | 
 **gid** | **str**| The Id of the group to remove from handle. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_handle_user**
> remove_handle_user(id, uid)

Remove handle user

Allows to revoke users access to a handle.  This operation requires `handle_update` privilege or `oz_handles_remove_relationships` and `oz_users_remove_relationships` admin privilege.  ***Example cURL requests***  **Remove handle service user** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/users/$USER_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle Id.
uid = 'uid_example' # str | The Id of the user to remove from handle.

try:
    # Remove handle user
    api_instance.remove_handle_user(id, uid)
except ApiException as e:
    print("Exception when calling HandleApi->remove_handle_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle Id. | 
 **uid** | **str**| The Id of the user to remove from handle. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_handle_privileges**
> update_group_handle_privileges(body, id, gid)

Update handle groups privileges

Updates group's (`{gid}`) privileges in a handle (`{id}`).  This operation requires `handle_update` privilege or `oz_handles_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update group's privileges in a handle** ```bash curl -u username:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"handle_view\"], \"revoke\": [\"handle_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/groups/$GROUP_ID/privileges ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
body = onezone_client.HandlePrivilegesUpdate() # HandlePrivilegesUpdate | Handle privileges update request.
id = 'id_example' # str | Handle Id.
gid = 'gid_example' # str | Group Id.

try:
    # Update handle groups privileges
    api_instance.update_group_handle_privileges(body, id, gid)
except ApiException as e:
    print("Exception when calling HandleApi->update_group_handle_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HandlePrivilegesUpdate**](HandlePrivilegesUpdate.md)| Handle privileges update request. | 
 **id** | **str**| Handle Id. | 
 **gid** | **str**| Group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_handle_user_privileges**
> update_handle_user_privileges(body, id, uid)

Update user handle privileges

Updates user's (`{uid}`) privileges in a handle (`{id}`).  This operation requires `handle_update` privilege or `oz_handles_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update group's privileges in a handle** ```bash curl -u username:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"handle_view\"], \"revoke\": [\"handle_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/users/$USER_ID/privileges ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleApi(onezone_client.ApiClient(configuration))
body = onezone_client.HandlePrivilegesUpdate() # HandlePrivilegesUpdate | Handle privileges update request.
id = 'id_example' # str | Handle Id.
uid = 'uid_example' # str | User Id.

try:
    # Update user handle privileges
    api_instance.update_handle_user_privileges(body, id, uid)
except ApiException as e:
    print("Exception when calling HandleApi->update_handle_user_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HandlePrivilegesUpdate**](HandlePrivilegesUpdate.md)| Handle privileges update request. | 
 **id** | **str**| Handle Id. | 
 **uid** | **str**| User Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

