# onepanel_client.LUMADBApi

All URIs are relative to */api/v3/onepanel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**luma_clear_db**](LUMADBApi.md#luma_clear_db) | **DELETE** /provider/storages/{id}/luma/db | Clear LUMA DB
[**luma_get_acl_group_to_onedata_group_mapping**](LUMADBApi.md#luma_get_acl_group_to_onedata_group_mapping) | **GET** /provider/storages/{id}/luma/db/storage_import/posix_compatible/acl_group_to_onedata_group/{groupname} | Lookup mapping of ACL group
[**luma_get_acl_user_to_onedata_user_mapping**](LUMADBApi.md#luma_get_acl_user_to_onedata_user_mapping) | **GET** /provider/storages/{id}/luma/db/storage_import/posix_compatible/acl_user_to_onedata_user/{username} | Lookup mapping of ACL user
[**luma_get_config**](LUMADBApi.md#luma_get_config) | **GET** /provider/storages/{id}/luma/config | Get LUMA DB configuration
[**luma_get_default_posix_credentials**](LUMADBApi.md#luma_get_default_posix_credentials) | **GET** /provider/storages/{id}/luma/db/storage_access/posix_compatible/default_credentials/{space_id} | Lookup default posix credentials
[**luma_get_display_credentials**](LUMADBApi.md#luma_get_display_credentials) | **GET** /provider/storages/{id}/luma/db/display_credentials/all/default/{space_id} | Lookup default display credentials
[**luma_get_onedata_user_to_credentials_mapping**](LUMADBApi.md#luma_get_onedata_user_to_credentials_mapping) | **GET** /provider/storages/{id}/luma/db/storage_access/all/onedata_user_to_credentials/{onedata_user_id} | Lookup Onedata user to credentials mapping
[**luma_get_uid_to_onedata_user_mapping**](LUMADBApi.md#luma_get_uid_to_onedata_user_mapping) | **GET** /provider/storages/{id}/luma/db/storage_import/posix_compatible/uid_to_onedata_user/{uid} | Lookup mapping of UID
[**luma_remove_acl_group_to_onedata_group_mapping**](LUMADBApi.md#luma_remove_acl_group_to_onedata_group_mapping) | **DELETE** /provider/storages/{id}/luma/db/storage_import/posix_compatible/acl_group_to_onedata_group/{groupname} | Remove mapping of ACL group
[**luma_remove_acl_user_to_onedata_user_mapping**](LUMADBApi.md#luma_remove_acl_user_to_onedata_user_mapping) | **DELETE** /provider/storages/{id}/luma/db/storage_import/posix_compatible/acl_user_to_onedata_user/{username} | Remove mapping of ACL user
[**luma_remove_default_posix_credentials**](LUMADBApi.md#luma_remove_default_posix_credentials) | **DELETE** /provider/storages/{id}/luma/db/storage_access/posix_compatible/default_credentials/{space_id} | Remove default posix credentials
[**luma_remove_display_credentials**](LUMADBApi.md#luma_remove_display_credentials) | **DELETE** /provider/storages/{id}/luma/db/display_credentials/all/default/{space_id} | Remove default display credentials
[**luma_remove_onedata_user_to_credentials_mapping**](LUMADBApi.md#luma_remove_onedata_user_to_credentials_mapping) | **DELETE** /provider/storages/{id}/luma/db/storage_access/all/onedata_user_to_credentials/{onedata_user_id} | Remove Onedata user to credentials mapping
[**luma_remove_uid_to_onedata_user_mapping**](LUMADBApi.md#luma_remove_uid_to_onedata_user_mapping) | **DELETE** /provider/storages/{id}/luma/db/storage_import/posix_compatible/uid_to_onedata_user/{uid} | Remove mapping of UID

# **luma_clear_db**
> luma_clear_db(id)

Clear LUMA DB

Clears all LUMA DB entries for given storage. LUMA DB will be repopulated using currently setup feed. 

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
api_instance = onepanel_client.LUMADBApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage for which LUMA DB will be cleared

try:
    # Clear LUMA DB
    api_instance.luma_clear_db(id)
except ApiException as e:
    print("Exception when calling LUMADBApi->luma_clear_db: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a storage for which LUMA DB will be cleared | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **luma_get_acl_group_to_onedata_group_mapping**
> LumaOnedataGroup luma_get_acl_group_to_onedata_group_mapping(id, groupname)

Lookup mapping of ACL group

Returns mapping of ACL group on the specific storage to Onedata group stored in LUMA DB. This endpoint is relevant **only for POSIX compatible storages**. 

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
api_instance = onepanel_client.LUMADBApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage constituting space support for which onedata group mapping should be returned. 
groupname = 56 # int | The ACL name of the group on the storage. 

try:
    # Lookup mapping of ACL group
    api_response = api_instance.luma_get_acl_group_to_onedata_group_mapping(id, groupname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LUMADBApi->luma_get_acl_group_to_onedata_group_mapping: %s\n" % e)
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

# **luma_get_acl_user_to_onedata_user_mapping**
> LumaOnedataUser luma_get_acl_user_to_onedata_user_mapping(id, username)

Lookup mapping of ACL user

Returns mapping of ACL user on the specific storage to Onedata user stored in LUMA DB. Mapping will be acquired again using currently setup LUMA feed. This endpoint is relevant **only for POSIX compatible storages**. 

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
api_instance = onepanel_client.LUMADBApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage constituting space support for which onedata user mapping should be returned. 
username = 56 # int | The ACL name of the user on the storage. 

try:
    # Lookup mapping of ACL user
    api_response = api_instance.luma_get_acl_user_to_onedata_user_mapping(id, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LUMADBApi->luma_get_acl_user_to_onedata_user_mapping: %s\n" % e)
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

# **luma_get_config**
> LumaConfig luma_get_config(id)

Get LUMA DB configuration

Returns configuration of Local User Mapping database (LUMA DB) for the storage. 

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
api_instance = onepanel_client.LUMADBApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage for which LUMA DB configuration should be returned.

try:
    # Get LUMA DB configuration
    api_response = api_instance.luma_get_config(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LUMADBApi->luma_get_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a storage for which LUMA DB configuration should be returned. | 

### Return type

[**LumaConfig**](LumaConfig.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **luma_get_default_posix_credentials**
> PosixCompatibleCredentials luma_get_default_posix_credentials(id, space_id)

Lookup default posix credentials

Returns default storage credentials for the space supported by POSIX-compatible storage that are stored in LUMA DB. GID will be used as a component of storage credentials for each member of the space. Both UID and GID will be used as to represent owner of the space directory on storage. This endpoint is relevant **only for POSIX compatible storages**. 

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
api_instance = onepanel_client.LUMADBApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage constituting space support for which default storage credentials should be returned. 
space_id = 'space_id_example' # str | The Id of a space constituting space support for which default storage credentials should be returned. 

try:
    # Lookup default posix credentials
    api_response = api_instance.luma_get_default_posix_credentials(id, space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LUMADBApi->luma_get_default_posix_credentials: %s\n" % e)
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

# **luma_get_display_credentials**
> PosixCompatibleCredentials luma_get_display_credentials(id, space_id)

Lookup default display credentials

Returns default display credentials for the space support that are stored in LUMA DB. These are POSIX credentials (UID & GID) which are returned in getattr response. They are used to present file owners in the result of e.g. `ls` or `stat` operation in Oneclient or when fetching file attributes via REST API. 

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
api_instance = onepanel_client.LUMADBApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage constituting space support for which default display credentials should be returned. 
space_id = 'space_id_example' # str | The Id of a space constituting space support for which default display credentials should be returned. 

try:
    # Lookup default display credentials
    api_response = api_instance.luma_get_display_credentials(id, space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LUMADBApi->luma_get_display_credentials: %s\n" % e)
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

# **luma_get_onedata_user_to_credentials_mapping**
> LumaStorageUser luma_get_onedata_user_to_credentials_mapping(id, onedata_user_id)

Lookup Onedata user to credentials mapping

Returns mapping of the Onedata user to user on the specific storage stored in LUMA DB. 

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
api_instance = onepanel_client.LUMADBApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage for which user mapping should be returned. 
onedata_user_id = 'onedata_user_id_example' # str | The Id of a user for which mapping should be returned. 

try:
    # Lookup Onedata user to credentials mapping
    api_response = api_instance.luma_get_onedata_user_to_credentials_mapping(id, onedata_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LUMADBApi->luma_get_onedata_user_to_credentials_mapping: %s\n" % e)
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

# **luma_get_uid_to_onedata_user_mapping**
> LumaOnedataUser luma_get_uid_to_onedata_user_mapping(id, uid)

Lookup mapping of UID

Returns mapping of UID on the specific storage to Onedata user stored in LUMA DB. Mapping will be acquired again using currently setup LUMA feed. This endpoint is relevant **only for POSIX compatible storages**. 

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
api_instance = onepanel_client.LUMADBApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage constituting space support for which onedata user mapping should be returned. 
uid = 56 # int | The UID of the user on the storage. 

try:
    # Lookup mapping of UID
    api_response = api_instance.luma_get_uid_to_onedata_user_mapping(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LUMADBApi->luma_get_uid_to_onedata_user_mapping: %s\n" % e)
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

# **luma_remove_acl_group_to_onedata_group_mapping**
> luma_remove_acl_group_to_onedata_group_mapping(id, groupname)

Remove mapping of ACL group

Removes mapping of ACL group on the specific storage to Onedata group from LUMA DB. Mapping will be acquired again using currently setup LUMA feed. This endpoint is relevant **only for POSIX compatible storages**. 

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
api_instance = onepanel_client.LUMADBApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage constituting space support for which onedata group mapping should be removed. 
groupname = 56 # int | The ACL name of the group on the storage. 

try:
    # Remove mapping of ACL group
    api_instance.luma_remove_acl_group_to_onedata_group_mapping(id, groupname)
except ApiException as e:
    print("Exception when calling LUMADBApi->luma_remove_acl_group_to_onedata_group_mapping: %s\n" % e)
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

# **luma_remove_acl_user_to_onedata_user_mapping**
> luma_remove_acl_user_to_onedata_user_mapping(id, username)

Remove mapping of ACL user

Removes mapping of ACL user on the specific storage to Onedata user from LUMA DB. This endpoint is relevant **only for POSIX compatible storages**. 

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
api_instance = onepanel_client.LUMADBApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage constituting space support for which onedata user mapping should be removed. 
username = 56 # int | The ACL name of the user on the storage. 

try:
    # Remove mapping of ACL user
    api_instance.luma_remove_acl_user_to_onedata_user_mapping(id, username)
except ApiException as e:
    print("Exception when calling LUMADBApi->luma_remove_acl_user_to_onedata_user_mapping: %s\n" % e)
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

# **luma_remove_default_posix_credentials**
> luma_remove_default_posix_credentials(id, space_id)

Remove default posix credentials

Removes default storage credentials for the space supported by POSIX-compatible storage from LUMA DB. Default storage credentials will be acquired again using currently setup LUMA feed. This endpoint is relevant **only for POSIX compatible storages**. 

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
api_instance = onepanel_client.LUMADBApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage constituting space support for which default storage credentials should be removed. 
space_id = 'space_id_example' # str | The Id of a space constituting space support for which default storage credentials should be removed. 

try:
    # Remove default posix credentials
    api_instance.luma_remove_default_posix_credentials(id, space_id)
except ApiException as e:
    print("Exception when calling LUMADBApi->luma_remove_default_posix_credentials: %s\n" % e)
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

# **luma_remove_display_credentials**
> luma_remove_display_credentials(id, space_id)

Remove default display credentials

Removes default display credentials for the space support from LUMA DB. Default display credentials will be acquired again using currently setup LUMA feed. 

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
api_instance = onepanel_client.LUMADBApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage constituting space support for which default display credentials should be removed. 
space_id = 'space_id_example' # str | The Id of a space constituting space support for which default display credentials should be removed. 

try:
    # Remove default display credentials
    api_instance.luma_remove_display_credentials(id, space_id)
except ApiException as e:
    print("Exception when calling LUMADBApi->luma_remove_display_credentials: %s\n" % e)
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

# **luma_remove_onedata_user_to_credentials_mapping**
> luma_remove_onedata_user_to_credentials_mapping(id, onedata_user_id)

Remove Onedata user to credentials mapping

Removes mapping of the Onedata user to user on the specific storage from LUMA DB. Mapping will be acquired again using currently setup LUMA feed. 

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
api_instance = onepanel_client.LUMADBApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage for which user mapping should be removed. 
onedata_user_id = 'onedata_user_id_example' # str | The Id of a user for which mapping should be removed. 

try:
    # Remove Onedata user to credentials mapping
    api_instance.luma_remove_onedata_user_to_credentials_mapping(id, onedata_user_id)
except ApiException as e:
    print("Exception when calling LUMADBApi->luma_remove_onedata_user_to_credentials_mapping: %s\n" % e)
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

# **luma_remove_uid_to_onedata_user_mapping**
> luma_remove_uid_to_onedata_user_mapping(id, uid)

Remove mapping of UID

Removes mapping of UID on the specific storage to Onedata user from LUMA DB. This endpoint is relevant **only for POSIX compatible storages**. 

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
api_instance = onepanel_client.LUMADBApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a storage constituting space support for which onedata user mapping should be removed. 
uid = 56 # int | The UID of the user on the storage. 

try:
    # Remove mapping of UID
    api_instance.luma_remove_uid_to_onedata_user_mapping(id, uid)
except ApiException as e:
    print("Exception when calling LUMADBApi->luma_remove_uid_to_onedata_user_mapping: %s\n" % e)
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

