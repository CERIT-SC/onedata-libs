# onezone_client.HandleServiceApi

All URIs are relative to */api/v3/onezone*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_handle_service**](HandleServiceApi.md#add_handle_service) | **POST** /handle_services | Add handle service
[**add_handle_service_group**](HandleServiceApi.md#add_handle_service_group) | **PUT** /handle_services/{id}/groups/{gid} | Add handle service group
[**add_handle_service_user**](HandleServiceApi.md#add_handle_service_user) | **PUT** /handle_services/{id}/users/{uid} | Add handle service user
[**get_effective_handle_service_group**](HandleServiceApi.md#get_effective_handle_service_group) | **GET** /handle_services/{id}/effective_groups/{gid} | Get effective handle service group
[**get_effective_handle_service_user**](HandleServiceApi.md#get_effective_handle_service_user) | **GET** /handle_services/{id}/effective_users/{uid} | Get effective handle service user
[**get_handle_service**](HandleServiceApi.md#get_handle_service) | **GET** /handle_services/{id} | Get handle service
[**get_handle_service_group**](HandleServiceApi.md#get_handle_service_group) | **GET** /handle_services/{id}/groups/{gid} | Get handle service group details
[**get_handle_service_handle**](HandleServiceApi.md#get_handle_service_handle) | **GET** /handle_services/{id}/handles/{hid} | Get handle from handle service
[**get_handle_service_user**](HandleServiceApi.md#get_handle_service_user) | **GET** /handle_services/{id}/users/{uid} | Get handle service user
[**handle_service_update**](HandleServiceApi.md#handle_service_update) | **PATCH** /handle_services/{id} | Modify handle service
[**list_effective_group_handle_service_privileges**](HandleServiceApi.md#list_effective_group_handle_service_privileges) | **GET** /handle_services/{id}/effective_groups/{gid}/privileges | List effective group&#x27;s handle service privileges
[**list_effective_handle_service_groups**](HandleServiceApi.md#list_effective_handle_service_groups) | **GET** /handle_services/{id}/effective_groups | List effective handle service groups
[**list_effective_handle_service_users**](HandleServiceApi.md#list_effective_handle_service_users) | **GET** /handle_services/{id}/effective_users | Get effective handle service users
[**list_effective_user_handle_service_privileges**](HandleServiceApi.md#list_effective_user_handle_service_privileges) | **GET** /handle_services/{id}/effective_users/{uid}/privileges | List effective user&#x27;s handle service privileges
[**list_group_handle_service_privileges**](HandleServiceApi.md#list_group_handle_service_privileges) | **GET** /handle_services/{id}/groups/{gid}/privileges | List group&#x27;s handle service privileges
[**list_handle_service_groups**](HandleServiceApi.md#list_handle_service_groups) | **GET** /handle_services/{id}/groups | List handle service groups
[**list_handle_service_privileges**](HandleServiceApi.md#list_handle_service_privileges) | **GET** /handle_services/privileges | List all handle service privileges
[**list_handle_service_users**](HandleServiceApi.md#list_handle_service_users) | **GET** /handle_services/{id}/users | Get handle service users
[**list_handle_services**](HandleServiceApi.md#list_handle_services) | **GET** /handle_services | List handle services
[**list_handleservice_handles**](HandleServiceApi.md#list_handleservice_handles) | **GET** /handle_services/{id}/handles | List handle service handles
[**list_user_handle_service_privileges**](HandleServiceApi.md#list_user_handle_service_privileges) | **GET** /handle_services/{id}/users/{uid}/privileges | List user&#x27;s handle service privileges
[**remove_handle_service**](HandleServiceApi.md#remove_handle_service) | **DELETE** /handle_services/{id} | Unregister handle service
[**remove_handle_service_group**](HandleServiceApi.md#remove_handle_service_group) | **DELETE** /handle_services/{id}/groups/{gid} | Remove handle service group
[**remove_handle_service_user**](HandleServiceApi.md#remove_handle_service_user) | **DELETE** /handle_services/{id}/users/{uid} | Remove handle service user
[**update_group_handle_service_privileges**](HandleServiceApi.md#update_group_handle_service_privileges) | **PATCH** /handle_services/{id}/users/{uid}/privileges | Update user&#x27;s handle service privileges
[**update_group_handle_service_privileges_0**](HandleServiceApi.md#update_group_handle_service_privileges_0) | **PATCH** /handle_services/{id}/groups/{gid}/privileges | Update group&#x27;s handle service privileges

# **add_handle_service**
> add_handle_service(body)

Add handle service

Allows to register a new handle service.  This operation requires `oz_handle_services_create` admin privilege.  See also:   [Create a new handle service for the current user](#operation/add_user_handle_service)   [Create a new handle service for given group](#operation/add_group_handle_service)    ***Example cURL requests***  **Add handle services** ```bash curl -u username:password -X POST -H \"Content-type: application/json\" \\ -d '{ ... }' https://$ZONE_HOST/api/v3/onezone/handle_services ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
body = onezone_client.HandleService() # HandleService | 

try:
    # Add handle service
    api_instance.add_handle_service(body)
except ApiException as e:
    print("Exception when calling HandleServiceApi->add_handle_service: %s\n" % e)
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

# **add_handle_service_group**
> add_handle_service_group(id, gid, body=body)

Add handle service group

Allows to add a group to a handle service.  This operation requires `handle_service_update` privilege or `oz_handle_services_add_relationships` and `oz_groups_add_relationships` admin privilege.  ***Example cURL requests***  **Add handle service user** ```bash curl -u username:password -X PUT \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/groups/$GROUP_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle service Id.
gid = 'gid_example' # str | The Id of the group to add to handle service.
body = onezone_client.GroupsGidBody1() # GroupsGidBody1 |  (optional)

try:
    # Add handle service group
    api_instance.add_handle_service_group(id, gid, body=body)
except ApiException as e:
    print("Exception when calling HandleServiceApi->add_handle_service_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle service Id. | 
 **gid** | **str**| The Id of the group to add to handle service. | 
 **body** | [**GroupsGidBody1**](GroupsGidBody1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_handle_service_user**
> add_handle_service_user(id, uid, body=body)

Add handle service user

Allows to add a user to a handle service.  This operation requires `handle_service_update` privilege or `oz_handle_services_add_relationships` and `oz_users_add_relationships` admin privilege.  ***Example cURL requests***  **Add handle service user** ```bash curl -u username:password -X PUT \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/users/$USER_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle service Id.
uid = 'uid_example' # str | The Id of the user to add to handle service.
body = onezone_client.UsersUidBody2() # UsersUidBody2 |  (optional)

try:
    # Add handle service user
    api_instance.add_handle_service_user(id, uid, body=body)
except ApiException as e:
    print("Exception when calling HandleServiceApi->add_handle_service_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle service Id. | 
 **uid** | **str**| The Id of the user to add to handle service. | 
 **body** | [**UsersUidBody2**](UsersUidBody2.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_handle_service_group**
> Group get_effective_handle_service_group(id, gid)

Get effective handle service group

Get details of a group with effective access to handle service.  This operation requires `handle_service_view` privilege or `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get effective handle service group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/effective_groups/$GROUP_ID  {   \"groupId\":\"HwUpk8jrwxKOe45uzLFX2GVa8lKEasj4q253sptVqF8\",   \"name\":\"Group name\",   \"type\":\"team\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle service Id.
gid = 'gid_example' # str | The Id of the group to return information about.

try:
    # Get effective handle service group
    api_response = api_instance.get_effective_handle_service_group(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleServiceApi->get_effective_handle_service_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle service Id. | 
 **gid** | **str**| The Id of the group to return information about. | 

### Return type

[**Group**](Group.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_handle_service_user**
> User get_effective_handle_service_user(id, uid)

Get effective handle service user

Allows to get a user to a handle service.  This operation requires `handle_service_view` privilege or `oz_users_view` admin privilege.  ***Example cURL requests***  **Get effective handle service user** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/effective_users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle service Id.
uid = 'uid_example' # str | The Id of the user to return information about.

try:
    # Get effective handle service user
    api_response = api_instance.get_effective_handle_service_user(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleServiceApi->get_effective_handle_service_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle service Id. | 
 **uid** | **str**| The Id of the user to return information about. | 

### Return type

[**User**](User.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_handle_service**
> HandleService get_handle_service(id)

Get handle service

Returns the properties of a specific handle service.  This operation requires `oz_handle_services_view` admin privilege or handle service membership.  ***Example cURL requests***  **Get handle services** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID  {   \"handleServiceId\": \"0fe7c8a20ffdf07480c46f084bc3b8d5\",   \"name\": \"MyCommunity Handle service\",   \"proxyEndpoint\": \"https://localhost:17000/handle_proxy\",   \"serviceProperties\": {     \"allowTemplateOverride\": false,     \"doiEndpoint\": \"/doi\",     \"host\": \"https://mds.test.datacite.org\",     \"identifierTemplate\": \"{{space.name}}-{{space.guid}}\",     \"mediaEndpoint\": \"/media\",     \"metadataEndpoint\": \"/metadata\",     \"password\": \"pa$$word\",     \"prefix\": 10.5072,     \"type\": \"DOI\",     \"username\": \"alice\"   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle service Id.

try:
    # Get handle service
    api_response = api_instance.get_handle_service(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleServiceApi->get_handle_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle service Id. | 

### Return type

[**HandleService**](HandleService.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_handle_service_group**
> Group get_handle_service_group(id, gid)

Get handle service group details

Get details of a group with access to handle service.  This operation requires `handle_service_view` privilege or `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get group handle service** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/groups/$GROUP_ID  {   \"groupId\":\"HwUpk8jrwxKOe45uzLFX2GVa8lKEasj4q253sptVqF8\",   \"name\":\"Group name\",   \"type\":\"team\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle service Id.
gid = 'gid_example' # str | The Id of the group to return information about.

try:
    # Get handle service group details
    api_response = api_instance.get_handle_service_group(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleServiceApi->get_handle_service_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle service Id. | 
 **gid** | **str**| The Id of the group to return information about. | 

### Return type

[**Group**](Group.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_handle_service_handle**
> Handle get_handle_service_handle(id, hid)

Get handle from handle service

Returns the details of a specific handle registered by handle service.  This operation requires `handle_service_view` privilege or `oz_handles_view` admin privilege.  ***Example cURL requests***  **Get handle services handle** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/13c6bf68ed88dd01f396571f976b148d/handles/$HANDLE_ID  {   \"handleId\": \"95b663a6467c72ab1256865efef9e387\",   \"handleServiceId\": \"97c27230017cd54c1220189e357322c4\",   \"resourceType\": \"Share\",   \"resourceId\": \"d6ee1aecf03b23f09756d6a49e435455\",   \"metadata\": \"<?xml version=\\\"1.0\\\"?>       <!DOCTYPE rdf:RDF SYSTEM \\\\\"http://dublincore.org/2000/12/01-dcmes-xml-dtd.dtd\\\">       <rdf:RDF xmlns:rdf=\\\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\\\"                xmlns:dc=\\\"http://purl.org/dc/elements/1.1/\\\">         <rdf:Description rdf:about=\\\"http://example.com/resouces/1\\\">           <dc:title>Example Resource</dc:title>           <dc:creator>John Doe</dc:creator>           <dc:publisher>MIT</dc:publisher>           <dc:date>2000-06-06</dc:date>         </rdf:Description>       </rdf:RDF>\",   \"timestamp\": \"1997-07-16T19:20\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle service Id.
hid = 'hid_example' # str | Handle Id.

try:
    # Get handle from handle service
    api_response = api_instance.get_handle_service_handle(id, hid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleServiceApi->get_handle_service_handle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle service Id. | 
 **hid** | **str**| Handle Id. | 

### Return type

[**Handle**](Handle.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_handle_service_user**
> User get_handle_service_user(id, uid)

Get handle service user

Allows to get a user to a handle service.  This operation requires `handle_service_view` privilege or `oz_users_view` admin privilege.  ***Example cURL requests***  **Add handle service user** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle service Id.
uid = 'uid_example' # str | The Id of the user to return information about.

try:
    # Get handle service user
    api_response = api_instance.get_handle_service_user(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleServiceApi->get_handle_service_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle service Id. | 
 **uid** | **str**| The Id of the user to return information about. | 

### Return type

[**User**](User.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_service_update**
> handle_service_update(body, id)

Modify handle service

Allows to update a registered handle service.  This operation requires `handle_service_update` privilege or `oz_handle_services_update` admin privilege.  ***Example cURL requests***  **Modify handle service password** ```bash curl -u username:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"name\": \"New handle service name\"}' \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
body = onezone_client.HandleServiceUpdate() # HandleServiceUpdate | 
id = 'id_example' # str | Handle service Id.

try:
    # Modify handle service
    api_instance.handle_service_update(body, id)
except ApiException as e:
    print("Exception when calling HandleServiceApi->handle_service_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HandleServiceUpdate**](HandleServiceUpdate.md)|  | 
 **id** | **str**| Handle service Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_group_handle_service_privileges**
> InlineResponse20014 list_effective_group_handle_service_privileges(id, gid)

List effective group's handle service privileges

Returns the list of effective group's (`{gid}`) privileges in a handle service (`{id}`).  Effective privileges are a sum of group's privileges and privileges inherited from its parent group memberships.  This operation requires `handle_service_view` privilege or `oz_handle_services_view_privileges` admin privilege.  ***Example cURL requests***  **List effective group's privileges in a handle service** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/effective_groups/$GROUP_ID/privileges  {   \"privileges\": [     \"handle_service_register_handle\",     \"handle_service_update\",     \"handle_service_view\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle service Id.
gid = 'gid_example' # str | Effective group Id.

try:
    # List effective group's handle service privileges
    api_response = api_instance.list_effective_group_handle_service_privileges(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleServiceApi->list_effective_group_handle_service_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle service Id. | 
 **gid** | **str**| Effective group Id. | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_handle_service_groups**
> Groups list_effective_handle_service_groups(id)

List effective handle service groups

Returns all groups with effective access to a handle service instance  This operation requires `handle_service_view` privilege or `oz_handle_services_list_relationships` admin privilege.  ***Example cURL requests***  **Get effective handle service groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/effective_groups  {   \"groups\": [     \"9d9687a61855be21a31c34359b1fa0d4\",     \"89389b5483bb60288e6f0a7af488e710\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle service Id.

try:
    # List effective handle service groups
    api_response = api_instance.list_effective_handle_service_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleServiceApi->list_effective_handle_service_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle service Id. | 

### Return type

[**Groups**](Groups.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_handle_service_users**
> Users list_effective_handle_service_users(id)

Get effective handle service users

Returns all users with access to a handle service instance  This operation requires `handle_service_view` privilege or `oz_handle_services_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle service users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/effective_users  {   \"users\": [     \"9d9687a61855be21a31c34359b1fa0d4\",     \"89389b5483bb60288e6f0a7af488e710\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle service Id.

try:
    # Get effective handle service users
    api_response = api_instance.list_effective_handle_service_users(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleServiceApi->list_effective_handle_service_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle service Id. | 

### Return type

[**Users**](Users.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_user_handle_service_privileges**
> InlineResponse20014 list_effective_user_handle_service_privileges(id, uid)

List effective user's handle service privileges

Returns the list of effective user's (`{uid}`) privileges in a handle service (`{id}`).  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation requires `handle_service_view` privilege or `oz_handle_services_view_privileges` admin privilege.  ***Example cURL requests***  **List effective user's privileges in a handle service** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/effective_users/$USER_ID/privileges  {   \"privileges\": [     \"handle_service_register_handle\",     \"handle_service_update\",     \"handle_service_view\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle service Id.
uid = 'uid_example' # str | Effective user Id.

try:
    # List effective user's handle service privileges
    api_response = api_instance.list_effective_user_handle_service_privileges(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleServiceApi->list_effective_user_handle_service_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle service Id. | 
 **uid** | **str**| Effective user Id. | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_handle_service_privileges**
> InlineResponse20014 list_group_handle_service_privileges(id, gid)

List group's handle service privileges

Returns the list of group's (`{gid}`) privileges in a handle service (`{id}`).  This operation requires `handle_service_view` privilege. For administrator who does not belong to this group `oz_handle_services_view_privileges` privilege is required.  ***Example cURL requests***  **List group's privileges in a handle service** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/groups/$GROUP_ID/privileges  {   \"privileges\": [     \"handle_service_register_handle\",     \"handle_service_update\",     \"handle_service_view\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle service Id.
gid = 'gid_example' # str | Effective group Id.

try:
    # List group's handle service privileges
    api_response = api_instance.list_group_handle_service_privileges(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleServiceApi->list_group_handle_service_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle service Id. | 
 **gid** | **str**| Effective group Id. | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_handle_service_groups**
> Groups list_handle_service_groups(id)

List handle service groups

Returns all groups with access to a handle service instance  This operation requires `handle_service_view` privilege or `oz_handle_services_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle service groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/groups  {   \"groups\": [     \"9d9687a61855be21a31c34359b1fa0d4\",     \"89389b5483bb60288e6f0a7af488e710\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle service Id.

try:
    # List handle service groups
    api_response = api_instance.list_handle_service_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleServiceApi->list_handle_service_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle service Id. | 

### Return type

[**Groups**](Groups.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_handle_service_privileges**
> InlineResponse20013 list_handle_service_privileges()

List all handle service privileges

Returns list of all possible handle service privileges.  This endpoint does not require authentication.  ***Example cURL requests***  **Get list of all handle service privileges** ```bash curl https://$ZONE_HOST/api/v3/onezone/handle_services/privileges  {   \"admin\": [     \"handle_service_view\",     \"handle_service_update\",     \"handle_service_delete\",     \"handle_service_register_handle\",     \"handle_service_list_handles\"   ],   \"member\": [     \"handle_service_view\",     \"handle_service_register_handle\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))

try:
    # List all handle service privileges
    api_response = api_instance.list_handle_service_privileges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleServiceApi->list_handle_service_privileges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_handle_service_users**
> Users list_handle_service_users(id)

Get handle service users

Returns all users with access to a handle service instance  This operation requires `handle_service_view` privilege or `oz_handle_services_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle service users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/users  {   \"users\": [     \"9d9687a61855be21a31c34359b1fa0d4\",     \"89389b5483bb60288e6f0a7af488e710\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle service Id.

try:
    # Get handle service users
    api_response = api_instance.list_handle_service_users(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleServiceApi->list_handle_service_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle service Id. | 

### Return type

[**Users**](Users.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_handle_services**
> HandleServices list_handle_services()

List handle services

Returns the list of registered handle services.  This operation requires `oz_handle_services_list` admin privilege.   ***Example cURL requests***  **Get handle services** ```bash curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/handle_services  {   \"handle_services\": [     \"0fe7c8a20ffdf07480c46f084bc3b8d5\",     \"302da048de67e2ea05f0af1d0fe7c8a2\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))

try:
    # List handle services
    api_response = api_instance.list_handle_services()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleServiceApi->list_handle_services: %s\n" % e)
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

# **list_handleservice_handles**
> Handles list_handleservice_handles(id)

List handle service handles

Returns the list of Ids of all handles registered by handle service.  This operation requires `handle_service_list_handles` privilege or `oz_handle_services_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle services handles** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/13c6bf68ed88dd01f396571f976b148d/handles  {   \"handles\": [     \"0fe7c8a20ffdf07480c46f084bc3b8d5\",     \"302da048de67e2ea05f0af1d0fe7c8a2\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle service Id.

try:
    # List handle service handles
    api_response = api_instance.list_handleservice_handles(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleServiceApi->list_handleservice_handles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle service Id. | 

### Return type

[**Handles**](Handles.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_handle_service_privileges**
> InlineResponse20014 list_user_handle_service_privileges(id, uid)

List user's handle service privileges

Returns the list of user's (`{uid}`) privileges in a handle service (`{id}`).  This operation requires `handle_service_view` privilege or `oz_handle_services_view_privileges` admin privilege.  ***Example cURL requests***  **List user's privileges in a handle service** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/users/$USER_ID/privileges  {   \"privileges\": [     \"handle_service_register_handle\",     \"handle_service_update\",     \"handle_service_view\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle service Id.
uid = 'uid_example' # str | Effective group Id.

try:
    # List user's handle service privileges
    api_response = api_instance.list_user_handle_service_privileges(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandleServiceApi->list_user_handle_service_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle service Id. | 
 **uid** | **str**| Effective group Id. | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_handle_service**
> remove_handle_service(id)

Unregister handle service

Allows to unregister a registeed handle service.  This operation requires `handle_service_delete` privilege or `oz_handle_services_delete` admin privilege.  ***Example cURL requests***  **Unregister handle service** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle service Id.

try:
    # Unregister handle service
    api_instance.remove_handle_service(id)
except ApiException as e:
    print("Exception when calling HandleServiceApi->remove_handle_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle service Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_handle_service_group**
> remove_handle_service_group(id, gid)

Remove handle service group

Allows to remove a group from access to a handle service.  This operation requires `handle_service_update` privilege or `oz_handle_services_remove_relationships` and `oz_groups_remove_relationships` admin privilege.  ***Example cURL requests***  **Remove handle service group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/groups/$GROUP_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle service Id.
gid = 'gid_example' # str | The Id of the group to remove from handle service.

try:
    # Remove handle service group
    api_instance.remove_handle_service_group(id, gid)
except ApiException as e:
    print("Exception when calling HandleServiceApi->remove_handle_service_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle service Id. | 
 **gid** | **str**| The Id of the group to remove from handle service. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_handle_service_user**
> remove_handle_service_user(id, uid)

Remove handle service user

Allows to remove a user from access to a handle service.  This operation requires `handle_service_update` privilege or `oz_handle_services_remove_relationships` and `oz_users_remove_relationships` admin privilege.  ***Example cURL requests***  **Remove handle service user** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/users/$USER_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Handle service Id.
uid = 'uid_example' # str | The Id of the user to remove from handle service.

try:
    # Remove handle service user
    api_instance.remove_handle_service_user(id, uid)
except ApiException as e:
    print("Exception when calling HandleServiceApi->remove_handle_service_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Handle service Id. | 
 **uid** | **str**| The Id of the user to remove from handle service. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_handle_service_privileges**
> update_group_handle_service_privileges(body, id, uid)

Update user's handle service privileges

Updates user's (`{uid}`) privileges in a handle service (`{id}`).  This operation requires `handle_service_update` privilege or `oz_handle_services_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update user's privileges in a handle service** ```bash curl -u username:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"handle_service_register_handle\"], \"revoke\": [\"handle_service_update\"]}' \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/users/$USER_ID/privileges ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
body = ['body_example'] # list[str] | Handle service privileges update request.
id = 'id_example' # str | Handle service Id.
uid = 'uid_example' # str | User Id.

try:
    # Update user's handle service privileges
    api_instance.update_group_handle_service_privileges(body, id, uid)
except ApiException as e:
    print("Exception when calling HandleServiceApi->update_group_handle_service_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| Handle service privileges update request. | 
 **id** | **str**| Handle service Id. | 
 **uid** | **str**| User Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_handle_service_privileges_0**
> update_group_handle_service_privileges_0(body, id, gid)

Update group's handle service privileges

Updates group's (`{gid}`) privileges in a handle service (`{id}`).  This operation requires `handle_service_update` privilege. For administrator who does not belong to this group `oz_handle_services_set_privileges` privilege is required.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update group's privileges in a handle service** ```bash curl -u username:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"handle_service_register_handle\"], \"revoke\": [\"handle_service_update\"]}' \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/groups/$GROUP_ID/privileges ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.HandleServiceApi(onezone_client.ApiClient(configuration))
body = onezone_client.HandleServicePrivilegesUpdate() # HandleServicePrivilegesUpdate | Handle service privileges update request.
id = 'id_example' # str | Handle service Id.
gid = 'gid_example' # str | Group Id.

try:
    # Update group's handle service privileges
    api_instance.update_group_handle_service_privileges_0(body, id, gid)
except ApiException as e:
    print("Exception when calling HandleServiceApi->update_group_handle_service_privileges_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HandleServicePrivilegesUpdate**](HandleServicePrivilegesUpdate.md)| Handle service privileges update request. | 
 **id** | **str**| Handle service Id. | 
 **gid** | **str**| Group Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

