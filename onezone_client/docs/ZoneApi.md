# onezone_client.ZoneApi

All URIs are relative to */api/v3/onezone*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_configuration**](ZoneApi.md#get_configuration) | **GET** /configuration | Returns public configuration of Onezone service.
[**health**](ZoneApi.md#health) | **GET** /health | Check cluster health
[**list_privileges**](ZoneApi.md#list_privileges) | **GET** /privileges | List all admin privileges.
[**test_image**](ZoneApi.md#test_image) | **GET** /test_image | Get test image.

# **get_configuration**
> Configuration get_configuration()

Returns public configuration of Onezone service.

Returns public information about the Onezone service.  This endpoint does not require authentication.  ***Example cURL requests***  **Get public information about the Onezone service** ```bash curl https://$ZONE_HOST/api/v3/onezone/configuration  {   \"name\": \"Example zone\",   \"domain\": \"zone.example.com\",   \"version\": \"21.02.3\",   \"build\": \"g52dbeca23\",   \"subdomainDelegationSupported\": true,   \"compatibleOneproviderVersions\": [       \"20.02.1\",       \"20.02.2\",       \"21.02.3\"   ],   \"compatibilityRegistryRevision\": 2022122100,   \"supportedIdPs\": [     {       \"id\": \"google\",       \"offlineAccess\": true     },     {       \"id\": \"basicAuth\",       \"offlineAccess\": false     }   ],   \"availableSpaceTags\": {     \"general\": [         \"big-data\",         \"demo\",         \"open-data\",         \"simulation\"     ],     \"domains\": [         \"agriculture\",         \"forestry\",         \"justice\",         \"science\"     ]   } } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ZoneApi(onezone_client.ApiClient(configuration))

try:
    # Returns public configuration of Onezone service.
    api_response = api_instance.get_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoneApi->get_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Configuration**](Configuration.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health**
> health()

Check cluster health

Returns status code indicating onezone service health status. This endpoint does not require authentication. 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ZoneApi(onezone_client.ApiClient(configuration))

try:
    # Check cluster health
    api_instance.health()
except ApiException as e:
    print("Exception when calling ZoneApi->health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_privileges**
> InlineResponse200 list_privileges()

List all admin privileges.

Returns list of all possible Onezone admin privileges.  This endpoint does not require authentication.  ***Example cURL requests***  **Get list of all Onezone admin privileges** ```bash curl https://$ZONE_HOST/api/v3/onezone/privileges  {   \"admin\": [     \"oz_view_privileges\",     \"oz_set_privileges\",     \"oz_users_list\",     \"oz_users_view\",     \"oz_users_create\",     \"oz_users_manage_passwords\",     \"oz_users_update\",     \"oz_users_delete\",     \"oz_users_list_relationships\",     \"oz_users_add_relationships\",     \"oz_users_remove_relationships\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_groups_create\",     \"oz_groups_update\",     \"oz_groups_delete\",     \"oz_groups_view_privileges\",     \"oz_groups_set_privileges\",     \"oz_groups_list_relationships\",     \"oz_groups_add_relationships\",     \"oz_groups_remove_relationships\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_spaces_create\",     \"oz_spaces_update\",     \"oz_spaces_delete\",     \"oz_spaces_view_privileges\",     \"oz_spaces_set_privileges\",     \"oz_spaces_list_relationships\",     \"oz_spaces_add_relationships\",     \"oz_spaces_remove_relationships\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_shares_create\",     \"oz_shares_update\",     \"oz_shares_delete\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_providers_update\",     \"oz_providers_delete\",     \"oz_providers_list_relationships\",     \"oz_providers_invite\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handle_services_create\",     \"oz_handle_services_update\",     \"oz_handle_services_delete\",     \"oz_handle_services_view_privileges\",     \"oz_handle_services_set_privileges\",     \"oz_handle_services_list_relationships\",     \"oz_handle_services_add_relationships\",     \"oz_handle_services_remove_relationships\",     \"oz_handles_list\",     \"oz_handles_view\",     \"oz_handles_create\",     \"oz_handles_update\",     \"oz_handles_delete\",     \"oz_handles_view_privileges\",     \"oz_handles_set_privileges\",     \"oz_handles_list_relationships\",     \"oz_handles_add_relationships\",     \"oz_handles_remove_relationships\",     \"oz_harvesters_list\",     \"oz_harvesters_view\",     \"oz_harvesters_create\",     \"oz_harvesters_update\",     \"oz_harvesters_delete\",     \"oz_harvesters_view_privileges\",     \"oz_harvesters_set_privileges\",     \"oz_harvesters_list_relationships\",     \"oz_harvesters_add_relationships\",     \"oz_harvesters_remove_relationships\",     \"oz_clusters_list\",     \"oz_clusters_view\",     \"oz_clusters_update\",     \"oz_clusters_view_privileges\",     \"oz_clusters_set_privileges\",     \"oz_clusters_list_relationships\",     \"oz_clusters_add_relationships\",     \"oz_clusters_remove_relationships\"   ],   \"viewer\": [     \"oz_users_list\",     \"oz_users_view\",     \"oz_users_list_relationships\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_groups_list_relationships\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_spaces_list_relationships\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_providers_list_relationships\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handle_services_list_relationships\",     \"oz_handles_list\",     \"oz_handles_view\",     \"oz_handles_list_relationships\",     \"oz_harvesters_list\",     \"oz_harvesters_view\",     \"oz_harvesters_list_relationships\",     \"oz_clusters_list\",     \"oz_clusters_view\",     \"oz_clusters_list_relationships\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ZoneApi(onezone_client.ApiClient(configuration))

try:
    # List all admin privileges.
    api_response = api_instance.list_privileges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoneApi->list_privileges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_image**
> test_image()

Get test image.

This endpoint returns a dummy image in `.png` format. It is used internally by web applications across Onedata to check connectivity with certain services. This endpoint does not require authentication. 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ZoneApi(onezone_client.ApiClient(configuration))

try:
    # Get test image.
    api_instance.test_image()
except ApiException as e:
    print("Exception when calling ZoneApi->test_image: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

