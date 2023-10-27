# onepanel_client.LUMADBLocalFeedApi

All URIs are relative to */api/v3/onepanel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**local_feed_add_onedata_user_to_credentials_mapping**](LUMADBLocalFeedApi.md#local_feed_add_onedata_user_to_credentials_mapping) | **POST** /provider/storages/{id}/luma/local_feed/storage_access/all/onedata_user_to_credentials | Insert Onedata user to credentials mapping into local feed
[**local_feed_get_acl_group_to_onedata_group_mapping**](LUMADBLocalFeedApi.md#local_feed_get_acl_group_to_onedata_group_mapping) | **GET** /provider/storages/{id}/luma/local_feed/storage_import/posix_compatible/acl_group_to_onedata_group/{groupname} | Lookup mapping of ACL group in local feed
[**local_feed_get_acl_user_to_onedata_user_mapping**](LUMADBLocalFeedApi.md#local_feed_get_acl_user_to_onedata_user_mapping) | **GET** /provider/storages/{id}/luma/local_feed/storage_import/posix_compatible/acl_user_to_onedata_user/{username} | Lookup mapping of ACL user in local feed
[**local_feed_get_default_posix_credentials**](LUMADBLocalFeedApi.md#local_feed_get_default_posix_credentials) | **GET** /provider/storages/{id}/luma/local_feed/storage_access/posix_compatible/default_credentials/{space_id} | Lookup default posix credentials in local feed
[**local_feed_get_display_credentials**](LUMADBLocalFeedApi.md#local_feed_get_display_credentials) | **GET** /provider/storages/{id}/luma/local_feed/display_credentials/all/default/{space_id} | Lookup default display credentials in local feed
[**local_feed_get_onedata_user_to_credentials_mapping**](LUMADBLocalFeedApi.md#local_feed_get_onedata_user_to_credentials_mapping) | **GET** /provider/storages/{id}/luma/local_feed/storage_access/all/onedata_user_to_credentials/{onedata_user_id} | Lookup Onedata user to credentials mapping in local feed
[**local_feed_get_uid_to_onedata_user_mapping**](LUMADBLocalFeedApi.md#local_feed_get_uid_to_onedata_user_mapping) | **GET** /provider/storages/{id}/luma/local_feed/storage_import/posix_compatible/uid_to_onedata_user/{uid} | Lookup mapping of UID in local feed
[**local_feed_modify_onedata_user_to_credentials_mapping**](LUMADBLocalFeedApi.md#local_feed_modify_onedata_user_to_credentials_mapping) | **PATCH** /provider/storages/{id}/luma/local_feed/storage_access/all/onedata_user_to_credentials/{onedata_user_id} | Update Onedata user to credentials mapping in local feed
[**local_feed_remove_acl_group_to_onedata_group_mapping**](LUMADBLocalFeedApi.md#local_feed_remove_acl_group_to_onedata_group_mapping) | **DELETE** /provider/storages/{id}/luma/local_feed/storage_import/posix_compatible/acl_group_to_onedata_group/{groupname} | Remove mapping of ACL group from local feed
[**local_feed_remove_acl_user_to_onedata_user_mapping**](LUMADBLocalFeedApi.md#local_feed_remove_acl_user_to_onedata_user_mapping) | **DELETE** /provider/storages/{id}/luma/local_feed/storage_import/posix_compatible/acl_user_to_onedata_user/{username} | Remove mapping of ACL user from local feed
[**local_feed_remove_default_posix_credentials**](LUMADBLocalFeedApi.md#local_feed_remove_default_posix_credentials) | **DELETE** /provider/storages/{id}/luma/local_feed/storage_access/posix_compatible/default_credentials/{space_id} | Remove default posix credentials from local feed
[**local_feed_remove_display_credentials**](LUMADBLocalFeedApi.md#local_feed_remove_display_credentials) | **DELETE** /provider/storages/{id}/luma/local_feed/display_credentials/all/default/{space_id} | Remove default display credentials from local feed
[**local_feed_remove_onedata_user_to_credentials_mapping**](LUMADBLocalFeedApi.md#local_feed_remove_onedata_user_to_credentials_mapping) | **DELETE** /provider/storages/{id}/luma/local_feed/storage_access/all/onedata_user_to_credentials/{onedata_user_id} | Remove Onedata user to credentials mapping from local feed
[**local_feed_remove_uid_to_onedata_user_mapping**](LUMADBLocalFeedApi.md#local_feed_remove_uid_to_onedata_user_mapping) | **DELETE** /provider/storages/{id}/luma/local_feed/storage_import/posix_compatible/uid_to_onedata_user/{uid} | Remove mapping of UID from local feed
[**local_feed_set_acl_group_to_onedata_group_mapping**](LUMADBLocalFeedApi.md#local_feed_set_acl_group_to_onedata_group_mapping) | **PUT** /provider/storages/{id}/luma/local_feed/storage_import/posix_compatible/acl_group_to_onedata_group/{groupname} | Insert mapping of ACL group into local feed
[**local_feed_set_acl_user_to_onedata_user_mapping**](LUMADBLocalFeedApi.md#local_feed_set_acl_user_to_onedata_user_mapping) | **PUT** /provider/storages/{id}/luma/local_feed/storage_import/posix_compatible/acl_user_to_onedata_user/{username} | Insert mapping of ACL user into local feed
[**local_feed_set_default_posix_credentials**](LUMADBLocalFeedApi.md#local_feed_set_default_posix_credentials) | **PUT** /provider/storages/{id}/luma/local_feed/storage_access/posix_compatible/default_credentials/{space_id} | Insert default posix credentials into local feed
[**local_feed_set_display_credentials**](LUMADBLocalFeedApi.md#local_feed_set_display_credentials) | **PUT** /provider/storages/{id}/luma/local_feed/display_credentials/all/default/{space_id} | Insert default display credentials into local feed
[**local_feed_set_uid_to_onedata_user_mapping**](LUMADBLocalFeedApi.md#local_feed_set_uid_to_onedata_user_mapping) | **PUT** /provider/storages/{id}/luma/local_feed/storage_import/posix_compatible/uid_to_onedata_user/{uid} | Insert mapping of UID into local feed

# **local_feed_add_onedata_user_to_credentials_mapping**
> local_feed_add_onedata_user_to_credentials_mapping(body, id)

Insert Onedata user to credentials mapping into local feed

Adds mapping of Onedata user to user on the specific storage to local feed. Returns an error if the storage has a different LUMA feed than `local`. 

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
api_instance = onepanel_client.LUMADBLocalFeedApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.LumaUserMapping() # LumaUserMapping | New user mapping

id = 'id_example' # str | The Id of a storage for which user mapping should be added. 

try:
    # Insert Onedata user to credentials mapping into local feed
    api_instance.local_feed_add_onedata_user_to_credentials_mapping(body, id)
except ApiException as e:
    print("Exception when calling LUMADBLocalFeedApi->local_feed_add_onedata_user_to_credentials_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LumaUserMapping**](LumaUserMapping.md)| New user mapping
 | 
 **id** | **str**| The Id of a storage for which user mapping should be added.  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_feed_get_acl_group_to_onedata_group_mapping**
> LumaOnedataGroup local_feed_get_acl_group_to_onedata_group_mapping(id, groupname)

Lookup mapping of ACL group in local feed

Returns mapping of ACL group on the specific storage to Onedata group defined in local feed. Returns an error if the storage has a different LUMA feed than `local`. This endpoint is relevant **only for POSIX compatible storages**. 

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
api_instance = onepanel_client.LUMADBLocalFeedApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage constituting space support for which onedata group mapping should be returned. 
groupname = 56 # int | The ACL name of the group on the storage. 

try:
    # Lookup mapping of ACL group in local feed
    api_response = api_instance.local_feed_get_acl_group_to_onedata_group_mapping(id, groupname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LUMADBLocalFeedApi->local_feed_get_acl_group_to_onedata_group_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a storage constituting space support for which onedata group mapping should be returned.  | 
 **groupname** | **int**| The ACL name of the group on the storage.  | 

### Return type

[**LumaOnedataGroup**](LumaOnedataGroup.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_feed_get_acl_user_to_onedata_user_mapping**
> LumaOnedataUser local_feed_get_acl_user_to_onedata_user_mapping(id, username)

Lookup mapping of ACL user in local feed

Returns mapping of ACL user on the specific storage to Onedata user defined in local feed. Returns an error if the storage has a different LUMA feed than `local`. This endpoint is relevant **only for POSIX compatible storages**. 

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
api_instance = onepanel_client.LUMADBLocalFeedApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage constituting space support for which onedata user mapping should be returned. 
username = 56 # int | The ACL name of the user on the storage. 

try:
    # Lookup mapping of ACL user in local feed
    api_response = api_instance.local_feed_get_acl_user_to_onedata_user_mapping(id, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LUMADBLocalFeedApi->local_feed_get_acl_user_to_onedata_user_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a storage constituting space support for which onedata user mapping should be returned.  | 
 **username** | **int**| The ACL name of the user on the storage.  | 

### Return type

[**LumaOnedataUser**](LumaOnedataUser.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_feed_get_default_posix_credentials**
> PosixCompatibleCredentials local_feed_get_default_posix_credentials(id, space_id)

Lookup default posix credentials in local feed

Returns default storage credentials for the space supported by POSIX-compatible storage that are defined in local feed. GID will be used as a component of storage credentials for each member of the space. Both UID and GID will be used as to represent owner of the space directory on storage. Returns an error if the storage has a different LUMA feed than `local`. This endpoint is relevant **only for POSIX compatible storages**. 

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
api_instance = onepanel_client.LUMADBLocalFeedApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage constituting space support for which default storage credentials should be returned. 
space_id = 'space_id_example' # str | The Id of a space constituting space support for which default storage credentials should be returned. 

try:
    # Lookup default posix credentials in local feed
    api_response = api_instance.local_feed_get_default_posix_credentials(id, space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LUMADBLocalFeedApi->local_feed_get_default_posix_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a storage constituting space support for which default storage credentials should be returned.  | 
 **space_id** | **str**| The Id of a space constituting space support for which default storage credentials should be returned.  | 

### Return type

[**PosixCompatibleCredentials**](PosixCompatibleCredentials.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_feed_get_display_credentials**
> PosixCompatibleCredentials local_feed_get_display_credentials(id, space_id)

Lookup default display credentials in local feed

Returns default display credentials for the space support that are defined in local feed. These are POSIX credentials (UID & GID) which are returned in getattr response. They are used to present file owners in the result of e.g. `ls` or `stat` operation in Oneclient or when fetching file attributes via REST API. Returns an error if the storage has a different LUMA feed than `local`. 

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
api_instance = onepanel_client.LUMADBLocalFeedApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage constituting space support for which default display credentials should be returned. 
space_id = 'space_id_example' # str | The Id of a space constituting space support for which default display credentials should be returned. 

try:
    # Lookup default display credentials in local feed
    api_response = api_instance.local_feed_get_display_credentials(id, space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LUMADBLocalFeedApi->local_feed_get_display_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a storage constituting space support for which default display credentials should be returned.  | 
 **space_id** | **str**| The Id of a space constituting space support for which default display credentials should be returned.  | 

### Return type

[**PosixCompatibleCredentials**](PosixCompatibleCredentials.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_feed_get_onedata_user_to_credentials_mapping**
> LumaStorageUser local_feed_get_onedata_user_to_credentials_mapping(id, onedata_user_id)

Lookup Onedata user to credentials mapping in local feed

Returns mapping of the Onedata user to user on the specific storage defined in local feed. Returns an error if the storage has a different LUMA feed than `local`. 

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
api_instance = onepanel_client.LUMADBLocalFeedApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage for which user mapping should be returned. 
onedata_user_id = 'onedata_user_id_example' # str | The Id of a user for which mapping should be returned. 

try:
    # Lookup Onedata user to credentials mapping in local feed
    api_response = api_instance.local_feed_get_onedata_user_to_credentials_mapping(id, onedata_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LUMADBLocalFeedApi->local_feed_get_onedata_user_to_credentials_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a storage for which user mapping should be returned.  | 
 **onedata_user_id** | **str**| The Id of a user for which mapping should be returned.  | 

### Return type

[**LumaStorageUser**](LumaStorageUser.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_feed_get_uid_to_onedata_user_mapping**
> LumaOnedataUser local_feed_get_uid_to_onedata_user_mapping(id, uid)

Lookup mapping of UID in local feed

Returns mapping of UID on the specific storage to Onedata user defined in local feed. Returns an error if the storage has a different LUMA feed than `local`. This endpoint is relevant **only for POSIX compatible storages**. 

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
api_instance = onepanel_client.LUMADBLocalFeedApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage constituting space support for which onedata user mapping should be returned. 
uid = 56 # int | The UID of the user on the storage. 

try:
    # Lookup mapping of UID in local feed
    api_response = api_instance.local_feed_get_uid_to_onedata_user_mapping(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LUMADBLocalFeedApi->local_feed_get_uid_to_onedata_user_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a storage constituting space support for which onedata user mapping should be returned.  | 
 **uid** | **int**| The UID of the user on the storage.  | 

### Return type

[**LumaOnedataUser**](LumaOnedataUser.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_feed_modify_onedata_user_to_credentials_mapping**
> local_feed_modify_onedata_user_to_credentials_mapping(body, id, onedata_user_id)

Update Onedata user to credentials mapping in local feed

Modifies mapping of the Onedata user to user on the specific storage in local feed. Returns an error if the storage has a different LUMA feed than `local`. 

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
api_instance = onepanel_client.LUMADBLocalFeedApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.LumaStorageUser() # LumaStorageUser | New user mapping

id = 'id_example' # str | The Id of a storage for which user mapping should be updated. 
onedata_user_id = 'onedata_user_id_example' # str | The Id of a user for which mapping should be updated. 

try:
    # Update Onedata user to credentials mapping in local feed
    api_instance.local_feed_modify_onedata_user_to_credentials_mapping(body, id, onedata_user_id)
except ApiException as e:
    print("Exception when calling LUMADBLocalFeedApi->local_feed_modify_onedata_user_to_credentials_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LumaStorageUser**](LumaStorageUser.md)| New user mapping
 | 
 **id** | **str**| The Id of a storage for which user mapping should be updated.  | 
 **onedata_user_id** | **str**| The Id of a user for which mapping should be updated.  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_feed_remove_acl_group_to_onedata_group_mapping**
> local_feed_remove_acl_group_to_onedata_group_mapping(id, groupname)

Remove mapping of ACL group from local feed

Removes mapping of ACL group on the specific storage to Onedata group from local feed. Returns an error if the storage has a different LUMA feed than `local`. This endpoint is relevant **only for POSIX compatible storages**. 

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
api_instance = onepanel_client.LUMADBLocalFeedApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage constituting space support for which onedata group mapping should be removed. 
groupname = 56 # int | The ACL name of the group on the storage. 

try:
    # Remove mapping of ACL group from local feed
    api_instance.local_feed_remove_acl_group_to_onedata_group_mapping(id, groupname)
except ApiException as e:
    print("Exception when calling LUMADBLocalFeedApi->local_feed_remove_acl_group_to_onedata_group_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a storage constituting space support for which onedata group mapping should be removed.  | 
 **groupname** | **int**| The ACL name of the group on the storage.  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_feed_remove_acl_user_to_onedata_user_mapping**
> local_feed_remove_acl_user_to_onedata_user_mapping(id, username)

Remove mapping of ACL user from local feed

Removes mapping of ACL user on the specific storage to Onedata user from local feed. Returns an error if the storage has a different LUMA feed than `local`. This endpoint is relevant **only for POSIX compatible storages**. 

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
api_instance = onepanel_client.LUMADBLocalFeedApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage constituting space support for which onedata user mapping should be removed. 
username = 56 # int | The ACL name of the user on the storage. 

try:
    # Remove mapping of ACL user from local feed
    api_instance.local_feed_remove_acl_user_to_onedata_user_mapping(id, username)
except ApiException as e:
    print("Exception when calling LUMADBLocalFeedApi->local_feed_remove_acl_user_to_onedata_user_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a storage constituting space support for which onedata user mapping should be removed.  | 
 **username** | **int**| The ACL name of the user on the storage.  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_feed_remove_default_posix_credentials**
> local_feed_remove_default_posix_credentials(id, space_id)

Remove default posix credentials from local feed

Removes default storage credentials for the space supported by POSIX-compatible storage from local feed. Returns an error if the storage has a different LUMA feed than `local`. This endpoint is relevant **only for POSIX compatible storages**. 

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
api_instance = onepanel_client.LUMADBLocalFeedApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage constituting space support for which default storage credentials should be removed. 
space_id = 'space_id_example' # str | The Id of a space constituting space support for which default storage credentials should be removed. 

try:
    # Remove default posix credentials from local feed
    api_instance.local_feed_remove_default_posix_credentials(id, space_id)
except ApiException as e:
    print("Exception when calling LUMADBLocalFeedApi->local_feed_remove_default_posix_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a storage constituting space support for which default storage credentials should be removed.  | 
 **space_id** | **str**| The Id of a space constituting space support for which default storage credentials should be removed.  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_feed_remove_display_credentials**
> local_feed_remove_display_credentials(id, space_id)

Remove default display credentials from local feed

Removes default display credentials for the space support from local feed. Returns an error if the storage has a different LUMA feed than `local`. 

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
api_instance = onepanel_client.LUMADBLocalFeedApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage constituting space support for which default display credentials should be removed. 
space_id = 'space_id_example' # str | The Id of a space constituting space support for which default display credentials should be removed. 

try:
    # Remove default display credentials from local feed
    api_instance.local_feed_remove_display_credentials(id, space_id)
except ApiException as e:
    print("Exception when calling LUMADBLocalFeedApi->local_feed_remove_display_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a storage constituting space support for which default display credentials should be removed.  | 
 **space_id** | **str**| The Id of a space constituting space support for which default display credentials should be removed.  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_feed_remove_onedata_user_to_credentials_mapping**
> local_feed_remove_onedata_user_to_credentials_mapping(id, onedata_user_id)

Remove Onedata user to credentials mapping from local feed

Removes mapping of the Onedata user to user on the specific storage local feed. Returns an error if the storage has a different LUMA feed than `local`. 

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
api_instance = onepanel_client.LUMADBLocalFeedApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage for which user mapping should be removed. 
onedata_user_id = 'onedata_user_id_example' # str | The Id of a user for which mapping should be removed. 

try:
    # Remove Onedata user to credentials mapping from local feed
    api_instance.local_feed_remove_onedata_user_to_credentials_mapping(id, onedata_user_id)
except ApiException as e:
    print("Exception when calling LUMADBLocalFeedApi->local_feed_remove_onedata_user_to_credentials_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a storage for which user mapping should be removed.  | 
 **onedata_user_id** | **str**| The Id of a user for which mapping should be removed.  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_feed_remove_uid_to_onedata_user_mapping**
> local_feed_remove_uid_to_onedata_user_mapping(id, uid)

Remove mapping of UID from local feed

Removes mapping of UID on the specific storage to Onedata user from local feed. Returns an error if the storage has a different LUMA feed than `local`. This endpoint is relevant **only for POSIX compatible storages**. 

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
api_instance = onepanel_client.LUMADBLocalFeedApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage constituting space support for which onedata user mapping should be removed. 
uid = 56 # int | The UID of the user on the storage. 

try:
    # Remove mapping of UID from local feed
    api_instance.local_feed_remove_uid_to_onedata_user_mapping(id, uid)
except ApiException as e:
    print("Exception when calling LUMADBLocalFeedApi->local_feed_remove_uid_to_onedata_user_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a storage constituting space support for which onedata user mapping should be removed.  | 
 **uid** | **int**| The UID of the user on the storage.  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_feed_set_acl_group_to_onedata_group_mapping**
> local_feed_set_acl_group_to_onedata_group_mapping(body, id, groupname)

Insert mapping of ACL group into local feed

Sets mapping of ACL group on the specific storage to Onedata group in local feed. Returns an error if the storage has a different LUMA feed than `local`. This endpoint is relevant **only for POSIX compatible storages**. 

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
api_instance = onepanel_client.LUMADBLocalFeedApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.LumaOnedataGroup() # LumaOnedataGroup | Credentials identifying group in the Onedata system.
id = 'id_example' # str | The Id of a storage constituting space support for which onedata group mapping should be set. 
groupname = 56 # int | The ACL name of the group on the storage. 

try:
    # Insert mapping of ACL group into local feed
    api_instance.local_feed_set_acl_group_to_onedata_group_mapping(body, id, groupname)
except ApiException as e:
    print("Exception when calling LUMADBLocalFeedApi->local_feed_set_acl_group_to_onedata_group_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LumaOnedataGroup**](LumaOnedataGroup.md)| Credentials identifying group in the Onedata system. | 
 **id** | **str**| The Id of a storage constituting space support for which onedata group mapping should be set.  | 
 **groupname** | **int**| The ACL name of the group on the storage.  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_feed_set_acl_user_to_onedata_user_mapping**
> local_feed_set_acl_user_to_onedata_user_mapping(body, id, username)

Insert mapping of ACL user into local feed

Sets mapping of ACL user on the specific storage to Onedata user in local feed. Returns an error if the storage has a different LUMA feed than `local`. This endpoint is relevant **only for POSIX compatible storages**. 

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
api_instance = onepanel_client.LUMADBLocalFeedApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.LumaOnedataUser() # LumaOnedataUser | Credentials identifying user in the Onedata system.
id = 'id_example' # str | The Id of a storage constituting space support for for which onedata user mapping should be set. 
username = 56 # int | The ACL name of the user on the storage. 

try:
    # Insert mapping of ACL user into local feed
    api_instance.local_feed_set_acl_user_to_onedata_user_mapping(body, id, username)
except ApiException as e:
    print("Exception when calling LUMADBLocalFeedApi->local_feed_set_acl_user_to_onedata_user_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LumaOnedataUser**](LumaOnedataUser.md)| Credentials identifying user in the Onedata system. | 
 **id** | **str**| The Id of a storage constituting space support for for which onedata user mapping should be set.  | 
 **username** | **int**| The ACL name of the user on the storage.  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_feed_set_default_posix_credentials**
> local_feed_set_default_posix_credentials(body, id, space_id)

Insert default posix credentials into local feed

Sets default storage credentials for the space supported by POSIX-compatible storage in local feed. Returns an error if the storage has a different LUMA feed than `local`. This endpoint is relevant **only for POSIX compatible storages**. 

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
api_instance = onepanel_client.LUMADBLocalFeedApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.PosixCompatibleCredentials() # PosixCompatibleCredentials | New default storage credentials for the space support.

id = 'id_example' # str | The Id of a storage constituting space support for which default storage credentials should be set. 
space_id = 'space_id_example' # str | The Id of a space constituting space support for which default storage credentials should be set. 

try:
    # Insert default posix credentials into local feed
    api_instance.local_feed_set_default_posix_credentials(body, id, space_id)
except ApiException as e:
    print("Exception when calling LUMADBLocalFeedApi->local_feed_set_default_posix_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PosixCompatibleCredentials**](PosixCompatibleCredentials.md)| New default storage credentials for the space support.
 | 
 **id** | **str**| The Id of a storage constituting space support for which default storage credentials should be set.  | 
 **space_id** | **str**| The Id of a space constituting space support for which default storage credentials should be set.  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_feed_set_display_credentials**
> local_feed_set_display_credentials(body, id, space_id)

Insert default display credentials into local feed

Sets default display credentials for the space support in local feed. Returns an error if the storage has a different LUMA feed than `local`. 

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
api_instance = onepanel_client.LUMADBLocalFeedApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.PosixCompatibleCredentials() # PosixCompatibleCredentials | New default display credentials for the space support.

id = 'id_example' # str | The Id of a storage constituting space support for which default display credentials should be set. 
space_id = 'space_id_example' # str | The Id of a space constituting space support for which default display credentials should be set. 

try:
    # Insert default display credentials into local feed
    api_instance.local_feed_set_display_credentials(body, id, space_id)
except ApiException as e:
    print("Exception when calling LUMADBLocalFeedApi->local_feed_set_display_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PosixCompatibleCredentials**](PosixCompatibleCredentials.md)| New default display credentials for the space support.
 | 
 **id** | **str**| The Id of a storage constituting space support for which default display credentials should be set.  | 
 **space_id** | **str**| The Id of a space constituting space support for which default display credentials should be set.  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_feed_set_uid_to_onedata_user_mapping**
> local_feed_set_uid_to_onedata_user_mapping(body, id, uid)

Insert mapping of UID into local feed

Sets mapping of UID on the specific storage to Onedata user in local feed. Returns an error if the storage has a different LUMA feed than `local`. This endpoint is relevant **only for POSIX compatible storages**. 

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
api_instance = onepanel_client.LUMADBLocalFeedApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.LumaOnedataUser() # LumaOnedataUser | Credentials identifying user in the Onedata system.
id = 'id_example' # str | The Id of a storage constituting space support for which onedata user mapping should be set. 
uid = 56 # int | The UID of the user on the storage. 

try:
    # Insert mapping of UID into local feed
    api_instance.local_feed_set_uid_to_onedata_user_mapping(body, id, uid)
except ApiException as e:
    print("Exception when calling LUMADBLocalFeedApi->local_feed_set_uid_to_onedata_user_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LumaOnedataUser**](LumaOnedataUser.md)| Credentials identifying user in the Onedata system. | 
 **id** | **str**| The Id of a storage constituting space support for which onedata user mapping should be set.  | 
 **uid** | **int**| The UID of the user on the storage.  | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

