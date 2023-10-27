# onezone_client.ProviderApi

All URIs are relative to */api/v3/onezone*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_current_time**](ProviderApi.md#check_current_time) | **GET** /provider/public/get_current_time | Show current clock time
[**check_my_ip**](ProviderApi.md#check_my_ip) | **GET** /provider/public/check_my_ip | Show client IP address
[**get_current_provider_details**](ProviderApi.md#get_current_provider_details) | **GET** /provider | Get current provider details
[**get_current_provider_domain_config**](ProviderApi.md#get_current_provider_domain_config) | **GET** /provider/domain_config | Get current provider&#x27;s domain config
[**get_effective_group_provider_membership_intermediaries**](ProviderApi.md#get_effective_group_provider_membership_intermediaries) | **GET** /providers/{id}/effective_groups/{gid}/membership | Get effective group&#x27;s provider membership intermediaries
[**get_effective_provider_group**](ProviderApi.md#get_effective_provider_group) | **GET** /providers/{id}/effective_groups/{gid} | Get group of provider
[**get_effective_provider_user**](ProviderApi.md#get_effective_provider_user) | **GET** /providers/{id}/effective_users/{uid} | Get effective user of provider
[**get_effective_user_provider_membership_intermediaries**](ProviderApi.md#get_effective_user_provider_membership_intermediaries) | **GET** /providers/{id}/effective_users/{uid}/membership | Get effective user&#x27;s provider membership intermediaries
[**get_provider_details**](ProviderApi.md#get_provider_details) | **GET** /providers/{id} | Get provider details
[**get_provider_domain_config**](ProviderApi.md#get_provider_domain_config) | **GET** /providers/{id}/domain_config | Get provider&#x27;s domain config
[**get_provider_space**](ProviderApi.md#get_provider_space) | **GET** /providers/{id}/spaces/{sid} | Get space supported by provider
[**get_supported_space**](ProviderApi.md#get_supported_space) | **GET** /provider/spaces/{sid} | Get space details by provider
[**list_current_provider_supported_spaces**](ProviderApi.md#list_current_provider_supported_spaces) | **GET** /provider/spaces | List current provider&#x27;s supported spaces
[**list_effective_provider_groups**](ProviderApi.md#list_effective_provider_groups) | **GET** /providers/{id}/effective_groups | List effective groups of provider
[**list_effective_provider_users**](ProviderApi.md#list_effective_provider_users) | **GET** /providers/{id}/effective_users | List effective users of provider
[**list_provider_supported_spaces**](ProviderApi.md#list_provider_supported_spaces) | **GET** /providers/{id}/spaces | List provider&#x27;s supported spaces
[**map_idp_group**](ProviderApi.md#map_idp_group) | **POST** /provider/public/map_idp_group | Map IdP group to Onezone group
[**map_idp_user**](ProviderApi.md#map_idp_user) | **POST** /provider/public/map_idp_user | Map IdP user to Onezone user
[**modify_provider**](ProviderApi.md#modify_provider) | **PATCH** /provider | Modify provider details
[**modify_supported_space**](ProviderApi.md#modify_supported_space) | **PATCH** /provider/spaces/{sid} | Modify supported space
[**oz_providers_list**](ProviderApi.md#oz_providers_list) | **GET** /providers | List providers
[**register_provider**](ProviderApi.md#register_provider) | **POST** /providers | Register provider
[**remove_provider**](ProviderApi.md#remove_provider) | **DELETE** /providers/{id} | Remove provider
[**remove_space_support**](ProviderApi.md#remove_space_support) | **DELETE** /provider/spaces/{sid} | Remove space support
[**unregister_provider**](ProviderApi.md#unregister_provider) | **DELETE** /provider | Unregister provider
[**verify_provider_identity**](ProviderApi.md#verify_provider_identity) | **POST** /provider/public/verify_provider_identity | Verify the identity of given provider

# **check_current_time**
> int check_current_time()

Show current clock time

Returns current clock time of this Onezone instance, in milliseconds since epoch.  This operation has public access.  ***Example cURL requests***  **Check provider IP** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET https://onezone.example.com/api/v3/onezone/provider/public/get_current_time ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))

try:
    # Show current clock time
    api_response = api_instance.check_current_time()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->check_current_time: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_my_ip**
> str check_my_ip()

Show client IP address

Returns the IP of the request peer. Will return the external IP (as seen by the Onezone).  This operation has public access.  ***Example cURL requests***  **Check provider IP** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET https://onezone.example.com/api/v3/onezone/provider/public/check_my_ip ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))

try:
    # Show client IP address
    api_response = api_instance.check_my_ip()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->check_my_ip: %s\n" % e)
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

# **get_current_provider_details**
> ProviderDetails get_current_provider_details()

Get current provider details

Returns information about the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Get information about provider** ```bash curl -H \"x-auth-token: $TOKEN\" https://$ZONE_HOST/api/v3/onezone/provider  {   \"providerId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"name\": \"Example provider\",   \"domain\": \"provider1.example.com\",   \"latitude\": 50.0647,   \"longitude\": 19.945,   \"clusterId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"online\": true,   \"creationTime\": 1576152793 } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))

try:
    # Get current provider details
    api_response = api_instance.get_current_provider_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->get_current_provider_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProviderDetails**](ProviderDetails.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_provider_domain_config**
> ProviderDomainConfig get_current_provider_domain_config()

Get current provider's domain config

Returns the domain config of the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Get provider's domain config** ```bash curl -sS -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/provider/domain_config  {   \"subdomainDelegation\": true,   \"domain\": \"provider1.onezone.example.com\",   \"subdomain\": \"provider1\",   \"ipList\": [\"172.17.0.1\", \"172.17.0.2\", \"172.17.0.3\"] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))

try:
    # Get current provider's domain config
    api_response = api_instance.get_current_provider_domain_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->get_current_provider_domain_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProviderDomainConfig**](ProviderDomainConfig.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_group_provider_membership_intermediaries**
> MembershipIntermediaries get_effective_group_provider_membership_intermediaries(id, gid)

Get effective group's provider membership intermediaries

Returns the effective group's (`{gid}`) provider membership intermediaries - spaces from which the group inherits access to the provider (`{id}`).  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user (`{uid}`) who is an effective member of the group (`{gid}`), * as user who has `oz_providers_view` admin privilege.  ***Example cURL requests***  **Get effective group's provider membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/effective_groups/$GROUP_ID/membership  {   \"intermediaries\": [     {\"type\": \"space\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"space\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"}   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Provider Id.
gid = 'gid_example' # str | Group Id.

try:
    # Get effective group's provider membership intermediaries
    api_response = api_instance.get_effective_group_provider_membership_intermediaries(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->get_effective_group_provider_membership_intermediaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider Id. | 
 **gid** | **str**| Group Id. | 

### Return type

[**MembershipIntermediaries**](MembershipIntermediaries.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_provider_group**
> Group get_effective_provider_group(id, gid)

Get group of provider

Returns the details of an effective group of a specific provider.  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user who has `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get group of a provider** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/groups/$GROUP_ID  {   \"groupId\":\"051f1a51d80c664b0d9528d81ee56a93\",   \"name\":\"new_group\",   \"type\":\"team\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Provider Id.
gid = 'gid_example' # str | Group Id.

try:
    # Get group of provider
    api_response = api_instance.get_effective_provider_group(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->get_effective_provider_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider Id. | 
 **gid** | **str**| Group Id. | 

### Return type

[**Group**](Group.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_provider_user**
> User get_effective_provider_user(id, uid)

Get effective user of provider

Returns the details of an effective user of a specific provider. This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user who has `oz_users_view` admin privilege.  ***Example cURL requests***  **Get effective user of a provider** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/effective_users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\",    \"emails\" : [],    \"linkedAccounts\" : [] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Provider Id.
uid = 'uid_example' # str | User Id.

try:
    # Get effective user of provider
    api_response = api_instance.get_effective_provider_user(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->get_effective_provider_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**User**](User.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_user_provider_membership_intermediaries**
> MembershipIntermediaries get_effective_user_provider_membership_intermediaries(id, uid)

Get effective user's provider membership intermediaries

Returns the effective user's (`{uid}`) provider membership intermediaries - spaces from which the user inherits access to the provider (`{id}`).  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user (`{uid}`) who is an effective member of the provider (`{id}`), * as user who has `oz_providers_view` admin privilege.  ***Example cURL requests***  **Get effective user's provider membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/effective_users/$USER_ID/membership  {   \"intermediaries\": [     {\"type\": \"space\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"space\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"}   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Provider Id.
uid = 'uid_example' # str | User Id.

try:
    # Get effective user's provider membership intermediaries
    api_response = api_instance.get_effective_user_provider_membership_intermediaries(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->get_effective_user_provider_membership_intermediaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider Id. | 
 **uid** | **str**| User Id. | 

### Return type

[**MembershipIntermediaries**](MembershipIntermediaries.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider_details**
> ProviderDetails get_provider_details(id)

Get provider details

Returns the information about a specific Oneprovider service that is registered in Onezone.  This operation requires any of the following authentication: * as any provider (providers are allowed to view each other's data), * as user who is an effective member in a space supported by the subject provider, * as user who has `oz_providers_view` admin privilege.  ***Example cURL requests***  **Get specific provider details** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID  {   \"providerId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"name\": \"Example provider\",   \"domain\": \"provider1.example.com\",   \"latitude\": 50.0647,   \"longitude\": 19.945,   \"clusterId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"online\": true,   \"creationTime\": 1576152793 } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Provider Id.

try:
    # Get provider details
    api_response = api_instance.get_provider_details(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->get_provider_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider Id. | 

### Return type

[**ProviderDetails**](ProviderDetails.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider_domain_config**
> ProviderDomainConfig get_provider_domain_config(id)

Get provider's domain config

Returns the domain config of specific provider.  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user who has `oz_providers_view` admin privilege.  ***Example cURL requests***  **Get provider's domain config** ```bash curl -sS -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/domain_config  {   \"subdomainDelegation\": true,   \"domain\": \"provider1.onezone.example.com\",   \"subdomain\": \"provider1\",   \"ipList\": [\"172.17.0.1\", \"172.17.0.2\", \"172.17.0.3\"] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Provider Id.

try:
    # Get provider's domain config
    api_response = api_instance.get_provider_domain_config(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->get_provider_domain_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider Id. | 

### Return type

[**ProviderDomainConfig**](ProviderDomainConfig.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider_space**
> Space get_provider_space(id, sid)

Get space supported by provider

Returns the details of space supported by a specific provider.  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user who has `oz_spaces_view` admin privilege.  ***Example cURL requests***  **Get space supported by provider** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/spaces/$SPACE_ID  {   \"spaceId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_space1\",   \"providers\": {     \"296ebe3c20e9666dc489b647f8647f12\" : 5368709120   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebfc1a770c3\"   },   \"creationTime\": 1576152793 } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Provider Id.
sid = 'sid_example' # str | Space Id.

try:
    # Get space supported by provider
    api_response = api_instance.get_provider_space(id, sid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->get_provider_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider Id. | 
 **sid** | **str**| Space Id. | 

### Return type

[**Space**](Space.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_space**
> Space get_supported_space(sid)

Get space details by provider

Returns information about a specific space supported by the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Get space details** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/provider/spaces/$SPACE_ID  {   \"spaceId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_space1\",   \"providers\": {     \"296ebe3c20e9666dc489b647f8647f12\" : 5368709120   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebfc1a770c3\"   },   \"creationTime\": 1576152793 } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))
sid = 'sid_example' # str | Space Id.

try:
    # Get space details by provider
    api_response = api_instance.get_supported_space(sid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->get_supported_space: %s\n" % e)
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

# **list_current_provider_supported_spaces**
> Spaces list_current_provider_supported_spaces()

List current provider's supported spaces

Returns the list of spaces managed by the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Get spaces supported by provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET https://$ZONE_HOST/api/v3/onezone/provider/spaces  {   \"spaces\": [     \"1ad4551e2c127fac3850374eeb2dfec4\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))

try:
    # List current provider's supported spaces
    api_response = api_instance.list_current_provider_supported_spaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->list_current_provider_supported_spaces: %s\n" % e)
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

# **list_effective_provider_groups**
> Groups list_effective_provider_groups(id)

List effective groups of provider

Returns the list of effective groups of a specific provider.  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user who has `oz_providers_list_relationships` admin privilege.  ***Example cURL requests***  **List groups of a provider** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/groups  {   \"groups\": [     \"1ad4551e2c127fac3850374eeb2dfec4\",     \"a6c6e47cc477aa4d3f8c61ce71df9850\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Provider Id.

try:
    # List effective groups of provider
    api_response = api_instance.list_effective_provider_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->list_effective_provider_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider Id. | 

### Return type

[**Groups**](Groups.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_effective_provider_users**
> Users list_effective_provider_users(id)

List effective users of provider

Returns the list of effective users of a specific provider.  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user who has `oz_providers_list_relationships` admin privilege.  ***Example cURL requests***  **List effective users of a provider** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/users  {   \"users\": [     \"1ad4551e2c127fac3850374eeb2dfec4\",     \"a6c6e47cc477aa4d3f8c61ce71df9850\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Provider Id.

try:
    # List effective users of provider
    api_response = api_instance.list_effective_provider_users(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->list_effective_provider_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider Id. | 

### Return type

[**Users**](Users.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_provider_supported_spaces**
> Spaces list_provider_supported_spaces(id)

List provider's supported spaces

Returns the list of spaces supported by specific provider.  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user who has `oz_providers_list_relationships` admin privilege.  ***Example cURL requests***  **List spaces supported by provider** ```bash curlsS -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/spaces  {   \"spaces\": [     \"1ad4551e2c127fac3850374eeb2dfec4\",     \"a6c6e47cc477aa4d3f8c61ce71df9850\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Provider Id.

try:
    # List provider's supported spaces
    api_response = api_instance.list_provider_supported_spaces(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->list_provider_supported_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider Id. | 

### Return type

[**Spaces**](Spaces.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_idp_group**
> InlineResponse20011 map_idp_group(body)

Map IdP group to Onezone group

Maps external IdP group Id into internal group Id in Onezone. The IdP must have group mapping enabled.  The group does not have to exist in Onezone or the IdP - this method merely transforms the Id using a deterministic procedure. It can be used to predict the group Id in Onezone before it is created.  This operation has public access.  ***Example cURL requests***  **Map IdP group to Onezone group** ```bash curl -H 'Content-type: application/json' \\ -d '{\"idp\": \"elixir\", \"groupId\": \"elixir:members\"}' \\ -X POST https://onezone.example.com/api/v3/onezone/provider/public/map_idp_group  {   \"groupId\": \"302da048de67e2ea05f0af1d0fe7c8a2\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))
body = onezone_client.PublicMapIdpGroupBody() # PublicMapIdpGroupBody | Mapping parameters

try:
    # Map IdP group to Onezone group
    api_response = api_instance.map_idp_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->map_idp_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PublicMapIdpGroupBody**](PublicMapIdpGroupBody.md)| Mapping parameters | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_idp_user**
> InlineResponse20010 map_idp_user(body)

Map IdP user to Onezone user

Maps external IdP user id into internal user id in Onezone.  The user does not have to exist in Onezone or the IdP - this method merely transforms the Id using a deterministic procedure. It can be used to predict the user Id in Onezone before it is created.  This operation has public access.  ***Example cURL requests***  **Map IdP user to Onezone user** ```bash curl -H 'Content-type: application/json' \\ -d '{\"idp\": \"elixir\", \"userId\": \"dqs1ew2afn9q28rnweu8fb23r9jqwtfg\"}' \\ -X POST https://onezone.example.com/api/v3/onezone/provider/public/map_idp_user  {   \"userId\": \"0fe7c8a20ffdf07480c46f084bc3b8d5\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))
body = onezone_client.PublicMapIdpUserBody() # PublicMapIdpUserBody | Mapping parameters

try:
    # Map IdP user to Onezone user
    api_response = api_instance.map_idp_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->map_idp_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PublicMapIdpUserBody**](PublicMapIdpUserBody.md)| Mapping parameters | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_provider**
> modify_provider(body)

Modify provider details

Updates information about the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Update provider geo location** ```bash curl -H \"x-auth-token: $TOKEN\" -H \"Content-type: application/json\" -X PATCH \\ -d '{\"latitude\": 50.068968,\"longitude\": 20.909444}'  \\ https://$ZONE_HOST/api/v3/onezone/provider ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))
body = onezone_client.ProviderUpdateRequest() # ProviderUpdateRequest | Provider data.

try:
    # Modify provider details
    api_instance.modify_provider(body)
except ApiException as e:
    print("Exception when calling ProviderApi->modify_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProviderUpdateRequest**](ProviderUpdateRequest.md)| Provider data. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_supported_space**
> modify_supported_space(sid)

Modify supported space

Modifies the support size of a space supported by the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Change supported size** ```bash curl -H \"x-auth-token: $TOKEN\" -H \"Content-type: application/json\" \\ -X PATCH -d '{\"size\": 1024000}' \\ https://$ZONE_HOST/api/v3/onezone/provider/spaces/$SPACE_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))
sid = 'sid_example' # str | Space Id.

try:
    # Modify supported space
    api_instance.modify_supported_space(sid)
except ApiException as e:
    print("Exception when calling ProviderApi->modify_supported_space: %s\n" % e)
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

# **oz_providers_list**
> Providers oz_providers_list()

List providers

Returns the list of providers registered in the Onezone service.  This operation requires `oz_providers_list` admin privilege.  ***Example cURL requests***  **Get list of providers** ```bash curl -Ssk -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers  {   \"providers\": [     \"WEavnRE7c49EU2sjF0Rz7l_kpiA1IBrwbDxNfH87Plc\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))

try:
    # List providers
    api_response = api_instance.oz_providers_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->oz_providers_list: %s\n" % e)
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

# **register_provider**
> ProviderRegistrationResponse register_provider(body)

Register provider

Registers a Oneprovider in Onezone service. Upon success, a new cluster is created, with the registering user linked to it. The cluster Id is the same as Oneprovider Id.  Requires a valid provider registration token - see:   * [Create provider registration token for self](#operation/user_create_provider_registration_token_for_self)   * [Create provider registration token for a user](#operation/user_create_provider_registration_token)  This operation has public access.  ***Example cURL requests***  **Register provider** ```bash curl -H \"Content-type: application/json\" -X POST -d '{   \"token\" : \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaW...\",   \"name\" : \"My provider\",   \"adminEmail\" : \"person@example.com\",   \"subdomainDelegation\" : \"false\",   \"domain\" : \"my-provider.example.com\",   \"latitude\" : \"50.0647\",   \"longitude\" : \"19.9450\", }' \\ https://$ZONE_HOST/api/v3/onezone/providers ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))
body = onezone_client.ProviderRegistrationRequest() # ProviderRegistrationRequest | Provider reqistration request.

try:
    # Register provider
    api_response = api_instance.register_provider(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->register_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProviderRegistrationRequest**](ProviderRegistrationRequest.md)| Provider reqistration request. | 

### Return type

[**ProviderRegistrationResponse**](ProviderRegistrationResponse.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_provider**
> remove_provider(id)

Remove provider

Removes (unregisters) given Oneprovider from Onezone.  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `oz_providers_delete` admin privilege.  ***Example cURL requests***  **Get specific provider details** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Provider Id.

try:
    # Remove provider
    api_instance.remove_provider(id)
except ApiException as e:
    print("Exception when calling ProviderApi->remove_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_space_support**
> remove_space_support(sid)

Remove space support

Revokes support for a space supported by the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Revoke space support** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/provider/spaces/$SPACE_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))
sid = 'sid_example' # str | Space Id.

try:
    # Remove space support
    api_instance.remove_space_support(sid)
except ApiException as e:
    print("Exception when calling ProviderApi->remove_space_support: %s\n" % e)
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

# **unregister_provider**
> unregister_provider()

Unregister provider

Allows Oneprovider service to unregister from Onezone - concerns the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Unregister provider from Onezone** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE  \\ https://$ZONE_HOST/api/v3/onezone/provider ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))

try:
    # Unregister provider
    api_instance.unregister_provider()
except ApiException as e:
    print("Exception when calling ProviderApi->unregister_provider: %s\n" % e)
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

# **verify_provider_identity**
> verify_provider_identity(body)

Verify the identity of given provider

Verifies the identity of given provider based on its identity token.  This operation has public access.  ***Example cURL requests***  **Check provider IP** ```bash curl -H \"X-Auth-Token: $TOKEN\" -H \"Content-type: application/json\" \\ -d '{\"providerId\": \"f3a3fbcc6e85e1b7829e4901a8e1809\", \"token\": \"JKAxNWxvY2F0aW9uIG9uZXp...\"}' \\ -X POST https://onezone.example.com/api/v3/onezone/provider/public/verify_provider_identity ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ProviderApi(onezone_client.ApiClient(configuration))
body = onezone_client.PublicVerifyProviderIdentityBody() # PublicVerifyProviderIdentityBody | Identity parameters

try:
    # Verify the identity of given provider
    api_instance.verify_provider_identity(body)
except ApiException as e:
    print("Exception when calling ProviderApi->verify_provider_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PublicVerifyProviderIdentityBody**](PublicVerifyProviderIdentityBody.md)| Identity parameters | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

