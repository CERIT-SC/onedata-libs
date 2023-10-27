# onepanel_client.SpaceSupportApi

All URIs are relative to */api/v3/onepanel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_provider_spaces**](SpaceSupportApi.md#get_provider_spaces) | **GET** /provider/spaces | Get provider spaces
[**get_space_details**](SpaceSupportApi.md#get_space_details) | **GET** /provider/spaces/{id} | Get space details
[**modify_space**](SpaceSupportApi.md#modify_space) | **PATCH** /provider/spaces/{id} | Modify space details
[**revoke_space_support**](SpaceSupportApi.md#revoke_space_support) | **DELETE** /provider/spaces/{id} | Revoke space support for a space
[**support_space**](SpaceSupportApi.md#support_space) | **POST** /provider/spaces | Support space

# **get_provider_spaces**
> ProviderSpaces get_provider_spaces()

Get provider spaces

Returns the list of spaces supported by the provider.  ***Example cURL requests***  **Get provider space ids** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET https://$OP_PANEL_HOST/api/v3/onepanel/provider/spaces  {     \"ids\": [         \"0614a7a1512271ceeae95539872eeeabched69\",         \"06911eba60e6ba947f86f799ce975042chad21\",         \"109b7d84c00cd45a88b6cdb852dba5b3ch84db\"     ] } ``` 

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
api_instance = onepanel_client.SpaceSupportApi(onepanel_client.ApiClient(configuration))

try:
    # Get provider spaces
    api_response = api_instance.get_provider_spaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceSupportApi->get_provider_spaces: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProviderSpaces**](ProviderSpaces.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space_details**
> SpaceDetails get_space_details(id)

Get space details

Returns details of space specified by space Id in the path.  ***Example cURL requests***  **Get space details** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET https://$OP_PANEL_HOST/api/v3/onepanel/provider/spaces/$SPACE_ID  {     \"supportingProviders\": {         \"03c7e42a793912307b01b1bbb72a3a6bch4c1c\": 10000000     },     \"storageId\": \"18a42a43b1b2d92455ffa09e9a15df7fch4f82\",     \"spaceOccupancy\": 0,     \"name\": \"someSpace\",     \"localStorages\": [\"18a42a43b1b2d92455ffa09e9a15df7fch4f82\"],     \"importedStorage\": false,     \"id\": \"16403a6c45105010dc7103e31874cb3echac41\",     \"accountingEnabled\": false,     \"dirStatsServiceEnabled\": true,     \"dirStatsServiceStatus\": \"initializing\" } ``` 

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
api_instance = onepanel_client.SpaceSupportApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a space which details should be returned.

try:
    # Get space details
    api_response = api_instance.get_space_details(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceSupportApi->get_space_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a space which details should be returned. | 

### Return type

[**SpaceDetails**](SpaceDetails.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_space**
> modify_space(body, id)

Modify space details

Modifies the space import/update strategies.  ***Example cURL requests***  **Modify space support size** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X PATCH https://$OP_PANEL_HOST/api/v3/onepanel/provider/spaces/$SPACE_ID \\ -H \"Content-Type: application/json\" -d '{\"size\": \"30000000\"}' ``` 

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
api_instance = onepanel_client.SpaceSupportApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.SpaceModifyRequest() # SpaceModifyRequest | 
id = 'id_example' # str | The Id of a space which details should be modified.

try:
    # Modify space details
    api_instance.modify_space(body, id)
except ApiException as e:
    print("Exception when calling SpaceSupportApi->modify_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpaceModifyRequest**](SpaceModifyRequest.md)|  | 
 **id** | **str**| The Id of a space which details should be modified. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_space_support**
> revoke_space_support(id)

Revoke space support for a space

Allows provider to revoke storage support for a specific space. Users with access to this space will no longer be able to store data on the resources of this provider.  ***Example cURL requests***  **Revoke space support** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X DELETE https://$OP_PANEL_HOST/api/v3/onepanel/provider/spaces/$SPACE_ID ``` 

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
api_instance = onepanel_client.SpaceSupportApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a space to be removed.

try:
    # Revoke space support for a space
    api_instance.revoke_space_support(id)
except ApiException as e:
    print("Exception when calling SpaceSupportApi->revoke_space_support: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a space to be removed. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_space**
> Id support_space(body)

Support space

Supports an existing space.  ***Example cURL requests***  **Support space** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST https://$OP_PANEL_HOST/api/v3/onepanel/provider/spaces \\ -H \"Content-Type: application/json\" -d '{     \"token\": \"MDAU02QHLaaJ00go\",     \"size\": \"10000000\",     \"storageId\": \"18a42a43b1b2d9e9a1f82\" }'  {     \"id\": \"16403a6c45105010dc7103e31874cb3echac41\" } ``` 

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
api_instance = onepanel_client.SpaceSupportApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.SpaceSupportRequest() # SpaceSupportRequest | Specification of the space support request including support size and token.


try:
    # Support space
    api_response = api_instance.support_space(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceSupportApi->support_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpaceSupportRequest**](SpaceSupportRequest.md)| Specification of the space support request including support size and token.
 | 

### Return type

[**Id**](Id.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

