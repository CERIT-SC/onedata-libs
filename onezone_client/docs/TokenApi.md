# onezone_client.TokenApi

All URIs are relative to */api/v3/onezone*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confine_token**](TokenApi.md#confine_token) | **POST** /tokens/confine | Confine a token
[**create_named_token_for_current_provider**](TokenApi.md#create_named_token_for_current_provider) | **POST** /provider/tokens/named | Create named token for current provider
[**create_named_token_for_current_user**](TokenApi.md#create_named_token_for_current_user) | **POST** /user/tokens/named | Create named token for current user
[**create_named_token_for_provider**](TokenApi.md#create_named_token_for_provider) | **POST** /providers/{id}/tokens/named | Create named token for a provider
[**create_named_token_for_user**](TokenApi.md#create_named_token_for_user) | **POST** /users/{id}/tokens/named | Create named token for a user
[**create_temporary_token_for_current_provider**](TokenApi.md#create_temporary_token_for_current_provider) | **POST** /provider/tokens/temporary | Create temporary token for current provider
[**create_temporary_token_for_current_user**](TokenApi.md#create_temporary_token_for_current_user) | **POST** /user/tokens/temporary | Create temporary token for current user
[**create_temporary_token_for_provider**](TokenApi.md#create_temporary_token_for_provider) | **POST** /providers/{id}/tokens/temporary | Create temporary token for a provider
[**create_temporary_token_for_user**](TokenApi.md#create_temporary_token_for_user) | **POST** /users/{id}/tokens/temporary | Create temporary token for a user
[**delete_named_token**](TokenApi.md#delete_named_token) | **DELETE** /tokens/named/{id} | Delete named token
[**delete_named_tokens_of_current_provider**](TokenApi.md#delete_named_tokens_of_current_provider) | **DELETE** /provider/tokens/named | Delete named tokens of current provider
[**delete_named_tokens_of_current_user**](TokenApi.md#delete_named_tokens_of_current_user) | **DELETE** /user/tokens/named | Delete named tokens of current user
[**delete_named_tokens_of_provider**](TokenApi.md#delete_named_tokens_of_provider) | **DELETE** /providers/{id}/tokens/named | Delete named tokens of a provider
[**delete_named_tokens_of_user**](TokenApi.md#delete_named_tokens_of_user) | **DELETE** /users/{id}/tokens/named | Delete named tokens of a user
[**examine_token**](TokenApi.md#examine_token) | **POST** /tokens/examine | Examine a token
[**get_named_token**](TokenApi.md#get_named_token) | **GET** /tokens/named/{id} | Get named token
[**get_named_token_of_current_provider_by_name**](TokenApi.md#get_named_token_of_current_provider_by_name) | **GET** /provider/tokens/named/name/{name} | Get named token of current provider by name
[**get_named_token_of_current_user_by_name**](TokenApi.md#get_named_token_of_current_user_by_name) | **GET** /user/tokens/named/name/{name} | Get named token of current user by name
[**get_named_token_of_provider_by_name**](TokenApi.md#get_named_token_of_provider_by_name) | **GET** /providers/{id}/tokens/named/name/{name} | Get named token of a provider by name
[**get_named_token_of_user_by_name**](TokenApi.md#get_named_token_of_user_by_name) | **GET** /users/{id}/tokens/named/name/{name} | Get named token of a user by name
[**get_named_token_status**](TokenApi.md#get_named_token_status) | **GET** /tokens/named/{id}/status | Get named token status
[**get_temporary_token_generation_of_current_provider**](TokenApi.md#get_temporary_token_generation_of_current_provider) | **GET** /provider/tokens/temporary | Get temporary token generation of current provider
[**get_temporary_token_generation_of_current_user**](TokenApi.md#get_temporary_token_generation_of_current_user) | **GET** /user/tokens/temporary | Get temporary token generation of current user
[**get_temporary_token_generation_of_provider**](TokenApi.md#get_temporary_token_generation_of_provider) | **GET** /providers/{id}/tokens/temporary | Get temporary token generation of a provider
[**get_temporary_token_generation_of_user**](TokenApi.md#get_temporary_token_generation_of_user) | **GET** /users/{id}/tokens/temporary | Get temporary token generation of a user
[**list_all_named_tokens**](TokenApi.md#list_all_named_tokens) | **GET** /tokens/named | List all named tokens
[**list_named_tokens_of_current_provider**](TokenApi.md#list_named_tokens_of_current_provider) | **GET** /provider/tokens/named | List named tokens of current provider
[**list_named_tokens_of_current_user**](TokenApi.md#list_named_tokens_of_current_user) | **GET** /user/tokens/named | List named tokens of current user
[**list_named_tokens_of_provider**](TokenApi.md#list_named_tokens_of_provider) | **GET** /providers/{id}/tokens/named | List named tokens of a provider
[**list_named_tokens_of_user**](TokenApi.md#list_named_tokens_of_user) | **GET** /users/{id}/tokens/named | List named tokens of a user
[**modify_named_token**](TokenApi.md#modify_named_token) | **PATCH** /tokens/named/{id} | Modify named token
[**revoke_all_temporary_tokens_of_current_provider**](TokenApi.md#revoke_all_temporary_tokens_of_current_provider) | **DELETE** /provider/tokens/temporary | Revoke all temporary tokens of current provider
[**revoke_all_temporary_tokens_of_current_user**](TokenApi.md#revoke_all_temporary_tokens_of_current_user) | **DELETE** /user/tokens/temporary | Revoke all temporary tokens of current user
[**revoke_all_temporary_tokens_of_provider**](TokenApi.md#revoke_all_temporary_tokens_of_provider) | **DELETE** /providers/{id}/tokens/temporary | Revoke all temporary tokens of a provider
[**revoke_all_temporary_tokens_of_user**](TokenApi.md#revoke_all_temporary_tokens_of_user) | **DELETE** /users/{id}/tokens/temporary | Revoke all temporary tokens of a user
[**verify_access_token**](TokenApi.md#verify_access_token) | **POST** /tokens/verify_access_token | Verify an access token
[**verify_identity_token**](TokenApi.md#verify_identity_token) | **POST** /tokens/verify_identity_token | Verify an identity token
[**verify_invite_token**](TokenApi.md#verify_invite_token) | **POST** /tokens/verify_invite_token | Verify an invite token

# **confine_token**
> InlineResponse20012 confine_token(body)

Confine a token

Confines (restricts) a token provided in serialized form with given caveats. Returns the confined token. Does not verify the token.  This operation has public access.  ***Example cURL requests***  **Confine a token** ```bash curl -d '{   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaW\",   \"caveats\": [{\"type\": \"time\", \"validUntil\": 1571147494}] }' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/tokens/confine ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
body = onezone_client.TokensConfineBody() # TokensConfineBody | The token to be confined and caveats.

try:
    # Confine a token
    api_response = api_instance.confine_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->confine_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokensConfineBody**](TokensConfineBody.md)| The token to be confined and caveats. | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_named_token_for_current_provider**
> NamedTokenCreateResponse create_named_token_for_current_provider(body)

Create named token for current provider

Creates a new named token for the provider. The token name must be unique for the provider.  This operation can be invoked on behalf of the current provider only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create named token for current provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X POST -d '{\"name\": \"new-token\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/provider/tokens/named ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
body = onezone_client.NamedTokenCreateRequest() # NamedTokenCreateRequest | Properties of the new named token.

try:
    # Create named token for current provider
    api_response = api_instance.create_named_token_for_current_provider(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->create_named_token_for_current_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NamedTokenCreateRequest**](NamedTokenCreateRequest.md)| Properties of the new named token. | 

### Return type

[**NamedTokenCreateResponse**](NamedTokenCreateResponse.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_named_token_for_current_user**
> NamedTokenCreateResponse create_named_token_for_current_user(body)

Create named token for current user

Creates a new named token for the user. The token name must be unique for the user.  In case of invite tokens, invite / add member privileges are required in the target entity to create a token. For example, `space_add_group` in the space when creating a `groupJoinSpace` invite token.  This operation can be invoked on behalf of the current user only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create named token for current user** ```bash curl -u username:password -X POST -d '{\"name\": \"new-token-1\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/user/tokens/named ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
body = onezone_client.NamedTokenCreateRequest() # NamedTokenCreateRequest | Properties of the new named token.

try:
    # Create named token for current user
    api_response = api_instance.create_named_token_for_current_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->create_named_token_for_current_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NamedTokenCreateRequest**](NamedTokenCreateRequest.md)| Properties of the new named token. | 

### Return type

[**NamedTokenCreateResponse**](NamedTokenCreateResponse.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_named_token_for_provider**
> NamedTokenCreateResponse create_named_token_for_provider(body, id)

Create named token for a provider

Creates a new named token for specific provider. The token name must be unique for the provider.  This operation is available for the subject provider (`id`), or the provider's cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create named token for a provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X POST -d '{\"name\": \"new-token\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/tokens/named/ ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
body = onezone_client.NamedTokenCreateRequest() # NamedTokenCreateRequest | Properties of the new named token.
id = 'id_example' # str | Provider Id

try:
    # Create named token for a provider
    api_response = api_instance.create_named_token_for_provider(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->create_named_token_for_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NamedTokenCreateRequest**](NamedTokenCreateRequest.md)| Properties of the new named token. | 
 **id** | **str**| Provider Id | 

### Return type

[**NamedTokenCreateResponse**](NamedTokenCreateResponse.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_named_token_for_user**
> NamedTokenCreateResponse create_named_token_for_user(body, id)

Create named token for a user

Creates a new named token for specific user. The token name must be unique for the user.  In case of invite tokens, invite / add member privileges are required in the target entity to create a token. For example, `space_add_group` in the space when creating a `groupJoinSpace` invite token.  This operation is available for the token owner (subject), otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create named token for a user** ```bash curl -u username:password -X POST -d '{\"name\": \"new-token-1\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/tokens/named ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
body = onezone_client.NamedTokenCreateRequest() # NamedTokenCreateRequest | Properties of the new named token.
id = 'id_example' # str | User Id

try:
    # Create named token for a user
    api_response = api_instance.create_named_token_for_user(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->create_named_token_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NamedTokenCreateRequest**](NamedTokenCreateRequest.md)| Properties of the new named token. | 
 **id** | **str**| User Id | 

### Return type

[**NamedTokenCreateResponse**](NamedTokenCreateResponse.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_temporary_token_for_current_provider**
> InlineResponse20012 create_temporary_token_for_current_provider(body)

Create temporary token for current provider

Creates a new temporary token for the provider. Temporary tokens must be confined with a time caveat and are not persisted (cannot be retrieved, listed, revoked, updated or deleted). However, it is possible to revoke all existing temporary tokens of the provider: [see more](#operation/revoke_all_temporary_tokens_of_current_provider)).  This operation can be invoked on behalf of the current provider only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create temporary token for current provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X POST \\ -d '{\"type\": {\"accessToken\":{}}, \"caveats\": [{\"type\": \"time\", \"validUntil\": 1571147494}]}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/provider/tokens/temporary ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
body = onezone_client.TemporaryTokenCreateRequest() # TemporaryTokenCreateRequest | Properties of the new temporary token.

try:
    # Create temporary token for current provider
    api_response = api_instance.create_temporary_token_for_current_provider(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->create_temporary_token_for_current_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemporaryTokenCreateRequest**](TemporaryTokenCreateRequest.md)| Properties of the new temporary token. | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_temporary_token_for_current_user**
> InlineResponse20012 create_temporary_token_for_current_user(body)

Create temporary token for current user

Creates a new temporary token for the user. Temporary tokens must be confined with a time caveat and are not persisted (cannot be retrieved, listed, revoked, updated or deleted). However, it is possible to revoke all existing temporary tokens of the user: [see more](#operation/revoke_all_temporary_tokens_of_current_user)).  In case of invite tokens, invite / add member privileges are required in the target entity to create a token. For example, `space_add_group` in the space when creating a `groupJoinSpace` invite token.  This operation can be invoked on behalf of the current user only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create temporary token for current user** ```bash curl -u username:password -X POST \\ -d '{\"type\": {\"accessToken\":{}}, \"caveats\": [{\"type\": \"time\", \"validUntil\": 1571147494}]}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/user/tokens/temporary ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
body = onezone_client.TemporaryTokenCreateRequest() # TemporaryTokenCreateRequest | Properties of the new temporary token.

try:
    # Create temporary token for current user
    api_response = api_instance.create_temporary_token_for_current_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->create_temporary_token_for_current_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemporaryTokenCreateRequest**](TemporaryTokenCreateRequest.md)| Properties of the new temporary token. | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_temporary_token_for_provider**
> InlineResponse20012 create_temporary_token_for_provider(body, id)

Create temporary token for a provider

Creates a new temporary token for specific provider. Temporary tokens must be confined with a time caveat and are not persisted (cannot be retrieved, listed, revoked, updated or deleted). However, it is possible to revoke all existing temporary tokens of the provider: [see more](#operation/revoke_all_temporary_tokens_of_provider)).  This operation is available for the subject provider (`id`), or the provider's cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create temporary token for a provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X POST \\ -d '{\"type\": {\"accessToken\":{}}, \"caveats\": [{\"type\": \"time\", \"validUntil\": 1571147494}]}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/tokens/temporary ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
body = onezone_client.TemporaryTokenCreateRequest() # TemporaryTokenCreateRequest | Properties of the new temporary token.
id = 'id_example' # str | Provider Id

try:
    # Create temporary token for a provider
    api_response = api_instance.create_temporary_token_for_provider(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->create_temporary_token_for_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemporaryTokenCreateRequest**](TemporaryTokenCreateRequest.md)| Properties of the new temporary token. | 
 **id** | **str**| Provider Id | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_temporary_token_for_user**
> InlineResponse20012 create_temporary_token_for_user(body, id)

Create temporary token for a user

Creates a new temporary token for specific user. Temporary tokens must be confined with a time caveat and are not persisted (cannot be retrieved, listed, revoked, updated or deleted). However, it is possible to revoke all existing temporary tokens of the user: [see more](#operation/revoke_all_temporary_tokens_of_user)).  In case of invite tokens, invite / add member privileges are required in the target entity to create a token. For example, `space_add_group` in the space when creating a `groupJoinSpace` invite token.  This operation is available for the currently authorized user, otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create temporary token for a user** ```bash curl -u username:password -X POST \\ -d '{\"type\": {\"accessToken\":{}}, \"caveats\": [{\"type\": \"time\", \"validUntil\": 1571147494}]}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/tokens/temporary ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
body = onezone_client.TemporaryTokenCreateRequest() # TemporaryTokenCreateRequest | Properties of the new temporary token.
id = 'id_example' # str | User Id

try:
    # Create temporary token for a user
    api_response = api_instance.create_temporary_token_for_user(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->create_temporary_token_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemporaryTokenCreateRequest**](TemporaryTokenCreateRequest.md)| Properties of the new temporary token. | 
 **id** | **str**| User Id | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_named_token**
> delete_named_token(id)

Delete named token

Deletes a specific named token.  This operation is available for the token owner (subject), or (in case of provider tokens) cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Delete named token** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/tokens/named/$TOKEN_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Token Id

try:
    # Delete named token
    api_instance.delete_named_token(id)
except ApiException as e:
    print("Exception when calling TokenApi->delete_named_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Token Id | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_named_tokens_of_current_provider**
> delete_named_tokens_of_current_provider()

Delete named tokens of current provider

Deletes all provider's named tokens.  This operation can be invoked on behalf of the current provider only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Delete named tokens of current provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/provider/tokens/named ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))

try:
    # Delete named tokens of current provider
    api_instance.delete_named_tokens_of_current_provider()
except ApiException as e:
    print("Exception when calling TokenApi->delete_named_tokens_of_current_provider: %s\n" % e)
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

# **delete_named_tokens_of_current_user**
> delete_named_tokens_of_current_user()

Delete named tokens of current user

Deletes all user's named tokens.  This operation can be invoked on behalf of the current user only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Delete named tokens of current user** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/tokens/named ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))

try:
    # Delete named tokens of current user
    api_instance.delete_named_tokens_of_current_user()
except ApiException as e:
    print("Exception when calling TokenApi->delete_named_tokens_of_current_user: %s\n" % e)
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

# **delete_named_tokens_of_provider**
> delete_named_tokens_of_provider(id)

Delete named tokens of a provider

Deletes all named tokens belonging to a specific provider.  This operation is available for the subject provider (`id`), or the provider's cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Delete named tokens of a provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/tokens/named ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Provider Id

try:
    # Delete named tokens of a provider
    api_instance.delete_named_tokens_of_provider(id)
except ApiException as e:
    print("Exception when calling TokenApi->delete_named_tokens_of_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider Id | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_named_tokens_of_user**
> delete_named_tokens_of_user(id)

Delete named tokens of a user

Deletes all named tokens belonging to a specific user.  This operation is available for the currently authorized user, otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Delete named tokens of a user** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/tokens/named ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | User Id

try:
    # Delete named tokens of a user
    api_instance.delete_named_tokens_of_user(id)
except ApiException as e:
    print("Exception when calling TokenApi->delete_named_tokens_of_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User Id | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **examine_token**
> ExaminedToken examine_token(body)

Examine a token

Examines a token provided in serialized form. Returns all the information that can be inferred from the token. Does not verify the token.  This operation has public access.  ***Example cURL requests***  **Examine a token** ```bash curl -d '{\"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaW\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/tokens/examine ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
body = onezone_client.TokensExamineBody() # TokensExamineBody | The token to be examined (encapsulated in an object).

try:
    # Examine a token
    api_response = api_instance.examine_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->examine_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokensExamineBody**](TokensExamineBody.md)| The token to be examined (encapsulated in an object). | 

### Return type

[**ExaminedToken**](ExaminedToken.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_named_token**
> NamedToken get_named_token(id)

Get named token

Returns the information about a specific named token.  This operation is available for the token owner (subject), or (in case of provider tokens) cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Get named token** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/tokens/named/$TOKEN_ID {   \"id\": \"2b5d0dd5aa6443a69277b5ce0544fec2\",   \"name\": \"my-token-1\",   \"subject\": {     \"type\": \"user\",     \"id\": \"1b510f18b3b05611871c0acdffa9aed4\"   },   \"type\": {     \"inviteToken\": {       \"inviteType\": \"userJoinCluster\",       \"clusterId\": \"fb73f7ceff5abd995357abbe01c812ce\"     }   },   \"caveats\": [     {       \"type\": \"time\",       \"validUntil\": 1571147494     },     {       \"type\": \"ip\",       \"whitelist\": [         \"189.34.15.0/8\",         \"127.0.0.0/24\",         \"167.73.12.17\"       ]     }   ],   \"metadata\": {     \"creationTime\": 1564721024,     \"usageLimit\": 15,     \"usageCount\": 3,     \"privileges\": [       \"space_view\",       \"space_read_data\",       \"space_view_views\",       \"space_view_statistics\"     ],     \"custom\": {       \"jobName\": \"experiment-15\",       \"vm\": \"worker156.cloud.local\"     }   },   \"revoked\": false,   \"token\": \"MDAxNWxvY2F0aW9uIG9uZXpvbmUKMDAzYmlkZW50aWZpZXIgOEhmSEFSSGdrbHFCa1pWSTR\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Token Id

try:
    # Get named token
    api_response = api_instance.get_named_token(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->get_named_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Token Id | 

### Return type

[**NamedToken**](NamedToken.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_named_token_of_current_provider_by_name**
> NamedToken get_named_token_of_current_provider_by_name(name)

Get named token of current provider by name

Returns the information about a provider's named token by token name.  This operation can be invoked on behalf of the current provider only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Get named token of current provider by name** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/provider/tokens/named/name/my-token-1 {   \"id\": \"2b5d0dd5aa6443a69277b5ce0544fec2\",   \"name\": \"my-token-1\",   \"subject\": {     \"type\": \"provider\",     \"id\": \"6ebe7ac282e0188b5336b5d8cfa564d5\"   },   \"type\": {     \"inviteToken\": {       \"inviteType\": \"userJoinCluster\",       \"clusterId\": \"fb73f7ceff5abd995357abbe01c812ce\"     }   },   \"caveats\": [     {       \"type\": \"time\",       \"validUntil\": 1571147494     },     {       \"type\": \"ip\",       \"whitelist\": [         \"189.34.15.0/8\",         \"127.0.0.0/24\",         \"167.73.12.17\"       ]     }   ],   \"metadata\": {     \"creationTime\": 1564721024,     \"usageLimit\": 15,     \"usageCount\": 3,     \"privileges\": [       \"space_view\",       \"space_read_data\",       \"space_view_views\",       \"space_view_statistics\"     ],     \"custom\": {       \"jobName\": \"experiment-15\",       \"vm\": \"worker156.cloud.local\"     }   },   \"revoked\": false,   \"token\": \"MDAxNWxvY2F0aW9uIG9uZXpvbmUKMDAzYmlkZW50aWZpZXIgOEhmSEFSSGdrbHFCa1pWSTR\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
name = 'name_example' # str | Token name

try:
    # Get named token of current provider by name
    api_response = api_instance.get_named_token_of_current_provider_by_name(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->get_named_token_of_current_provider_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Token name | 

### Return type

[**NamedToken**](NamedToken.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_named_token_of_current_user_by_name**
> NamedToken get_named_token_of_current_user_by_name(name)

Get named token of current user by name

Returns the information about a user's named token by token name.  This operation can be invoked on behalf of the current user only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Get named token of current user by name** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/tokens/named/name/my-token-1 {   \"id\": \"2b5d0dd5aa6443a69277b5ce0544fec2\",   \"name\": \"my-token-1\",   \"subject\": {     \"type\": \"user\",     \"id\": \"c26bab23d12f7389c3c311caf9c15902\"   },   \"type\": {     \"inviteToken\": {       \"inviteType\": \"userJoinCluster\",       \"clusterId\": \"fb73f7ceff5abd995357abbe01c812ce\"     }   },   \"caveats\": [     {       \"type\": \"time\",       \"validUntil\": 1571147494     },     {       \"type\": \"ip\",       \"whitelist\": [         \"189.34.15.0/8\",         \"127.0.0.0/24\",         \"167.73.12.17\"       ]     }   ],   \"metadata\": {     \"creationTime\": 1564721024,     \"usageLimit\": 15,     \"usageCount\": 3,     \"privileges\": [       \"space_view\",       \"space_read_data\",       \"space_view_views\",       \"space_view_statistics\"     ],     \"custom\": {       \"jobName\": \"experiment-15\",       \"vm\": \"worker156.cloud.local\"     }   },   \"revoked\": false,   \"token\": \"MDAxNWxvY2F0aW9uIG9uZXpvbmUKMDAzYmlkZW50aWZpZXIgOEhmSEFSSGdrbHFCa1pWSTR\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
name = 'name_example' # str | Token name

try:
    # Get named token of current user by name
    api_response = api_instance.get_named_token_of_current_user_by_name(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->get_named_token_of_current_user_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Token name | 

### Return type

[**NamedToken**](NamedToken.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_named_token_of_provider_by_name**
> NamedToken get_named_token_of_provider_by_name(id, name)

Get named token of a provider by name

Returns the information about a specific provider's named token by token name.  This operation is available for the subject provider (`id`), or the provider's cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Get named token of a provider by name** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/tokens/named/name/my-token-1 {   \"id\": \"2b5d0dd5aa6443a69277b5ce0544fec2\",   \"name\": \"my-token-1\",   \"subject\": {     \"type\": \"provider\",     \"id\": \"6ebe7ac282e0188b5336b5d8cfa564d5\"   },   \"type\": {     \"inviteToken\": {       \"inviteType\": \"userJoinCluster\",       \"clusterId\": \"fb73f7ceff5abd995357abbe01c812ce\"     }   },   \"caveats\": [     {       \"type\": \"time\",       \"validUntil\": 1571147494     },     {       \"type\": \"ip\",       \"whitelist\": [         \"189.34.15.0/8\",         \"127.0.0.0/24\",         \"167.73.12.17\"       ]     }   ],   \"metadata\": {     \"creationTime\": 1564721024,     \"usageLimit\": 15,     \"usageCount\": 3,     \"privileges\": [       \"space_view\",       \"space_read_data\",       \"space_view_views\",       \"space_view_statistics\"     ],     \"custom\": {       \"jobName\": \"experiment-15\",       \"vm\": \"worker156.cloud.local\"     }   },   \"revoked\": false,   \"token\": \"MDAxNWxvY2F0aW9uIG9uZXpvbmUKMDAzYmlkZW50aWZpZXIgOEhmSEFSSGdrbHFCa1pWSTR\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Provider Id
name = 'name_example' # str | Token name

try:
    # Get named token of a provider by name
    api_response = api_instance.get_named_token_of_provider_by_name(id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->get_named_token_of_provider_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider Id | 
 **name** | **str**| Token name | 

### Return type

[**NamedToken**](NamedToken.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_named_token_of_user_by_name**
> NamedToken get_named_token_of_user_by_name(id, name)

Get named token of a user by name

Returns the information about a specific user's named token by token name.  This operation is available for the token owner (subject), otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Get named token of a user by name** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/tokens/named/name/my-token-1 {   \"id\": \"2b5d0dd5aa6443a69277b5ce0544fec2\",   \"name\": \"my-token-1\",   \"subject\": {     \"type\": \"user\",     \"id\": \"c26bab23d12f7389c3c311caf9c15902\"   },   \"type\": {     \"inviteToken\": {       \"inviteType\": \"userJoinCluster\",       \"clusterId\": \"fb73f7ceff5abd995357abbe01c812ce\"     }   },   \"caveats\": [     {       \"type\": \"time\",       \"validUntil\": 1571147494     },     {       \"type\": \"ip\",       \"whitelist\": [         \"189.34.15.0/8\",         \"127.0.0.0/24\",         \"167.73.12.17\"       ]     }   ],   \"metadata\": {     \"creationTime\": 1564721024,     \"usageLimit\": 15,     \"usageCount\": 3,     \"privileges\": [       \"space_view\",       \"space_read_data\",       \"space_view_views\",       \"space_view_statistics\"     ],     \"custom\": {       \"jobName\": \"experiment-15\",       \"vm\": \"worker156.cloud.local\"     }   },   \"revoked\": false,   \"token\": \"MDAxNWxvY2F0aW9uIG9uZXpvbmUKMDAzYmlkZW50aWZpZXIgOEhmSEFSSGdrbHFCa1pWSTR\" } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | User Id
name = 'name_example' # str | Token name

try:
    # Get named token of a user by name
    api_response = api_instance.get_named_token_of_user_by_name(id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->get_named_token_of_user_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User Id | 
 **name** | **str**| Token name | 

### Return type

[**NamedToken**](NamedToken.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_named_token_status**
> NamedTokenStatus get_named_token_status(id)

Get named token status

Returns the status of a specific named token - information if the token is currently revoked.  This operation is available for: * the token owner (subject) * in case of user tokens - a provider that supports the user * in case of provider tokens - the provider cluster member * admins with `oz_tokens_manage` privilege.  ***Example cURL requests***  **Get named token status** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/tokens/named/$TOKEN_ID/status {   \"revoked\": false } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Token Id

try:
    # Get named token status
    api_response = api_instance.get_named_token_status(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->get_named_token_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Token Id | 

### Return type

[**NamedTokenStatus**](NamedTokenStatus.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_temporary_token_generation_of_current_provider**
> TemporaryTokenGeneration get_temporary_token_generation_of_current_provider()

Get temporary token generation of current provider

Returns the generation of temporary tokens of the provider. The generation is an increasing number that denotes the generation of shared token secret - if the secret changes (temporary tokens are revoked), the generation is incremented.  This operation can be invoked on behalf of the current provider only.  ***Example cURL requests***  **Get temporary token generation of current provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/provider/tokens/temporary  {   \"generation\": 3 } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))

try:
    # Get temporary token generation of current provider
    api_response = api_instance.get_temporary_token_generation_of_current_provider()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->get_temporary_token_generation_of_current_provider: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TemporaryTokenGeneration**](TemporaryTokenGeneration.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_temporary_token_generation_of_current_user**
> TemporaryTokenGeneration get_temporary_token_generation_of_current_user()

Get temporary token generation of current user

Returns the generation of temporary tokens of the user. The generation is an increasing number that denotes the generation of shared token secret - if the secret changes (temporary tokens are revoked), the generation is incremented.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get temporary token generation of current user** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/tokens/temporary  {   \"generation\": 3 } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))

try:
    # Get temporary token generation of current user
    api_response = api_instance.get_temporary_token_generation_of_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->get_temporary_token_generation_of_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TemporaryTokenGeneration**](TemporaryTokenGeneration.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_temporary_token_generation_of_provider**
> TemporaryTokenGeneration get_temporary_token_generation_of_provider(id)

Get temporary token generation of a provider

Returns the generation of temporary tokens of a specific provider. The generation is an increasing number that denotes the generation of shared token secret - if the secret changes (temporary tokens are revoked), the generation is incremented.  This operation is available for the subject provider (`id`), or the provider's cluster member. Otherwise requires `oz_tokens_manage` admin privilege.  ***Example cURL requests***  **Get temporary token generation of a provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/tokens/temporary  {   \"generation\": 3 } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | User Id

try:
    # Get temporary token generation of a provider
    api_response = api_instance.get_temporary_token_generation_of_provider(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->get_temporary_token_generation_of_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User Id | 

### Return type

[**TemporaryTokenGeneration**](TemporaryTokenGeneration.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_temporary_token_generation_of_user**
> TemporaryTokenGeneration get_temporary_token_generation_of_user(id)

Get temporary token generation of a user

Returns the generation of temporary tokens of a specific user. The generation is an increasing number that denotes the generation of shared token secret - if the secret changes (temporary tokens are revoked), the generation is incremented.  This operation is available for the currently authorized user and provider that supports the user, otherwise requires `oz_tokens_manage` admin privilege.  ***Example cURL requests***  **Get temporary token generation of a user** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/tokens/temporary  {   \"generation\": 3 } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | User Id

try:
    # Get temporary token generation of a user
    api_response = api_instance.get_temporary_token_generation_of_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->get_temporary_token_generation_of_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User Id | 

### Return type

[**TemporaryTokenGeneration**](TemporaryTokenGeneration.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_named_tokens**
> Tokens list_all_named_tokens()

List all named tokens

Returns the list of all tokens in the system. The results include ids of users' and providers' named tokens - temporary tokens are not included as they are not persisted in the system.  Requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **List all named tokens** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/tokens  {   \"tokens\": [     \"2b5d0dd5aa6443a69277b5ce0544fec2\",     \"818bf8d4404c2bcee2b47f024f6c0890\",     \"4a5e5dabcd55e03f1e9237eeca2548ff\",     \"81336b59656653a481d1e65168f3f213\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))

try:
    # List all named tokens
    api_response = api_instance.list_all_named_tokens()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->list_all_named_tokens: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Tokens**](Tokens.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_named_tokens_of_current_provider**
> Tokens list_named_tokens_of_current_provider()

List named tokens of current provider

Returns the list of provider's named tokens.  This operation can be invoked on behalf of the current provider only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **List named tokens of current provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/provider/tokens/named  {   \"tokens\": [     \"2b5d0dd5aa6443a69277b5ce0544fec2\",     \"818bf8d4404c2bcee2b47f024f6c0890\",     \"4a5e5dabcd55e03f1e9237eeca2548ff\",     \"81336b59656653a481d1e65168f3f213\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))

try:
    # List named tokens of current provider
    api_response = api_instance.list_named_tokens_of_current_provider()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->list_named_tokens_of_current_provider: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Tokens**](Tokens.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_named_tokens_of_current_user**
> Tokens list_named_tokens_of_current_user()

List named tokens of current user

Returns the list of user's named tokens.  This operation can be invoked on behalf of the current user only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **List named tokens of current user** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/tokens/named  {   \"tokens\": [     \"2b5d0dd5aa6443a69277b5ce0544fec2\",     \"818bf8d4404c2bcee2b47f024f6c0890\",     \"4a5e5dabcd55e03f1e9237eeca2548ff\",     \"81336b59656653a481d1e65168f3f213\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))

try:
    # List named tokens of current user
    api_response = api_instance.list_named_tokens_of_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->list_named_tokens_of_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Tokens**](Tokens.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_named_tokens_of_provider**
> Tokens list_named_tokens_of_provider(id)

List named tokens of a provider

Returns the list of specific provider's named tokens.  This operation is available for the subject provider (`id`), or the provider's cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **List named tokens of a provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/tokens/named  {   \"tokens\": [     \"2b5d0dd5aa6443a69277b5ce0544fec2\",     \"818bf8d4404c2bcee2b47f024f6c0890\",     \"4a5e5dabcd55e03f1e9237eeca2548ff\",     \"81336b59656653a481d1e65168f3f213\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Provider Id

try:
    # List named tokens of a provider
    api_response = api_instance.list_named_tokens_of_provider(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->list_named_tokens_of_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider Id | 

### Return type

[**Tokens**](Tokens.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_named_tokens_of_user**
> Tokens list_named_tokens_of_user(id)

List named tokens of a user

Returns the list of specific user's named tokens.  This operation is available for the currently authorized user, otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **List named tokens of a user** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/tokens/named  {   \"tokens\": [     \"2b5d0dd5aa6443a69277b5ce0544fec2\",     \"818bf8d4404c2bcee2b47f024f6c0890\",     \"4a5e5dabcd55e03f1e9237eeca2548ff\",     \"81336b59656653a481d1e65168f3f213\"   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | User Id

try:
    # List named tokens of a user
    api_response = api_instance.list_named_tokens_of_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->list_named_tokens_of_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User Id | 

### Return type

[**Tokens**](Tokens.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_named_token**
> modify_named_token(body, id)

Modify named token

Modifies a specific named token. Supports renaming the token, toggling the revoked flag and modifying the metadata.  This operation is available for the token owner (subject), or (in case of provider tokens) cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Modify named token** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"revoked\": true}' \\ https://$ZONE_HOST/api/v3/onezone/tokens/named/$TOKEN_ID ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
body = onezone_client.NamedTokenUpdateRequest() # NamedTokenUpdateRequest | Named token update request
id = 'id_example' # str | Token Id

try:
    # Modify named token
    api_instance.modify_named_token(body, id)
except ApiException as e:
    print("Exception when calling TokenApi->modify_named_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NamedTokenUpdateRequest**](NamedTokenUpdateRequest.md)| Named token update request | 
 **id** | **str**| Token Id | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_all_temporary_tokens_of_current_provider**
> revoke_all_temporary_tokens_of_current_provider()

Revoke all temporary tokens of current provider

Immediately revokes (invalidates) all temporary tokens belonging to the provider. The operation cannot be undone.  This operation can be invoked on behalf of the current provider only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Revoke all temporary tokens of current provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/provider/tokens/temporary ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))

try:
    # Revoke all temporary tokens of current provider
    api_instance.revoke_all_temporary_tokens_of_current_provider()
except ApiException as e:
    print("Exception when calling TokenApi->revoke_all_temporary_tokens_of_current_provider: %s\n" % e)
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

# **revoke_all_temporary_tokens_of_current_user**
> revoke_all_temporary_tokens_of_current_user()

Revoke all temporary tokens of current user

Immediately revokes (invalidates) all temporary tokens belonging to the user. The operation cannot be undone.  This operation can be invoked on behalf of the current user only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Revoke all temporary tokens of current user** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/tokens/temporary ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))

try:
    # Revoke all temporary tokens of current user
    api_instance.revoke_all_temporary_tokens_of_current_user()
except ApiException as e:
    print("Exception when calling TokenApi->revoke_all_temporary_tokens_of_current_user: %s\n" % e)
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

# **revoke_all_temporary_tokens_of_provider**
> revoke_all_temporary_tokens_of_provider(id)

Revoke all temporary tokens of a provider

Immediately revokes (invalidates) all temporary tokens belonging to a specific provider. The operation cannot be undone.  This operation is available for the subject provider (`id`), or the provider's cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Revoke all temporary tokens of a provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/tokens/temporary ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Provider Id

try:
    # Revoke all temporary tokens of a provider
    api_instance.revoke_all_temporary_tokens_of_provider(id)
except ApiException as e:
    print("Exception when calling TokenApi->revoke_all_temporary_tokens_of_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider Id | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_all_temporary_tokens_of_user**
> revoke_all_temporary_tokens_of_user(id)

Revoke all temporary tokens of a user

Immediately revokes (invalidates) all temporary tokens belonging to a specific user. The operation cannot be undone.  This operation is available for the currently authorized user, otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Revoke all temporary tokens of a user** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/tokens/temporary ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | User Id

try:
    # Revoke all temporary tokens of a user
    api_instance.revoke_all_temporary_tokens_of_user(id)
except ApiException as e:
    print("Exception when calling TokenApi->revoke_all_temporary_tokens_of_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User Id | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_access_token**
> VerifyTokenResponse verify_access_token(body=body)

Verify an access token

Verifies an [access token](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[access-tokens].html) provided in serialized form. Upon success, returns the token's subject.  Optionally, contextual information that may be required to verify token caveats can be provided in the request body:  * IP address of the token bearer - defaults to the requesting client's IP, * identity token of the service which is handling the request - defaults to `null`, * consumer's identity token - consumer defaults to the authenticated client   if valid token credentials are sent with this request, or `null` otherwise, * interface to which the token bearer has connected - defaults to `null` (undefined interface), * information if data access caveats should be allowed in the token - defaults to `false`.  If the token cannot be positively verified, HTTP code 4xx is returned with an error describing the reason of failure.  This operation has public access.  ***Example cURL requests***  **Verify an access token** ```bash curl -d '{\"token\": \"MDAxNmxvY2F00aW9uIHZ2...\", \"peerIp\": \"38.190.241.12\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/tokens/verify_access_token  {   \"subject\": {     \"type\": \"user\",     \"id\": \"1b510f18b3b05611871c0acdffa9aed4\"   },   \"ttl\": 3600 } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
body = onezone_client.VerifyAccessTokenRequest() # VerifyAccessTokenRequest | The token to be verified and optionally peer's IP address. (optional)

try:
    # Verify an access token
    api_response = api_instance.verify_access_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->verify_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyAccessTokenRequest**](VerifyAccessTokenRequest.md)| The token to be verified and optionally peer&#x27;s IP address. | [optional] 

### Return type

[**VerifyTokenResponse**](VerifyTokenResponse.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_identity_token**
> VerifyTokenResponse verify_identity_token(body)

Verify an identity token

Verifies an [identity token](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[identity-tokens].html) provided in serialized form. Identity token is a token that carries proof of identity, but does not carry authorization to perform any operations in the system. Upon success, returns the token's subject.  Optionally, contextual information that may be required to verify token caveats can be provided in the request body:  * IP address of the token bearer - defaults to the requesting client's IP, * consumer's identity token - consumer defaults to the authenticated client   if valid token credentials are sent with this request, or `null` otherwise, * interface to which the token bearer has connected - defaults to `null` (undefined interface).  If the token cannot be positively verified, HTTP code 4xx is returned with an error describing the reason of failure.  This operation has public access.  ***Example cURL requests***  **Verify an identity token** ```bash curl -d '{\"token\": \"MDAxNmxvY2F00aW9uIHZ2...\", \"peerIp\": \"38.190.241.12\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/tokens/verify_identity_token  {   \"subject\": {     \"type\": \"user\",     \"id\": \"1b510f18b3b05611871c0acdffa9aed4\"   },   \"ttl\": 3600 } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
body = onezone_client.VerifyIdentityTokenRequest() # VerifyIdentityTokenRequest | The token to be verified and optionally peer's IP address.

try:
    # Verify an identity token
    api_response = api_instance.verify_identity_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->verify_identity_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyIdentityTokenRequest**](VerifyIdentityTokenRequest.md)| The token to be verified and optionally peer&#x27;s IP address. | 

### Return type

[**VerifyTokenResponse**](VerifyTokenResponse.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_invite_token**
> VerifyTokenResponse verify_invite_token(body)

Verify an invite token

Verifies an [invite token](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[invite-tokens].html) provided in serialized form. Upon success, returns the token's subject. Does not check if the token can be effectively consumed (only if prerequisites are satisfied - the token itself is valid).  Optionally, contextual information that may be required to verify token caveats can be provided in the request body:  * IP address of the token bearer - defaults to the requesting client's IP, * consumer's identity token - consumer defaults to the authenticated client   if valid token credentials are sent with this request, or `null` otherwise, * expected invite token type, which will cause verification to fail if it   does not match the actual token type. If not specified, the procedure will   check if given token is an invite token of any type.  If the token cannot be positively verified, HTTP code 4xx is returned with an error describing the reason of failure.  This operation has public access.  ***Example cURL requests***  **Verify an invite token** ```bash curl -d '{   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaW\",   \"peerIp\": \"38.190.241.12\",   \"expectedInviteType\": \"userJoinGroup\" }' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/tokens/verify_invite_token  {   \"subject\": {     \"type\": \"user\",     \"id\": \"1b510f18b3b05611871c0acdffa9aed4\"   },   \"ttl\": 3600 } ``` 

### Example
```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.TokenApi(onezone_client.ApiClient(configuration))
body = onezone_client.VerifyInviteTokenRequest() # VerifyInviteTokenRequest | The token to be verified and optional parameters.

try:
    # Verify an invite token
    api_response = api_instance.verify_invite_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->verify_invite_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyInviteTokenRequest**](VerifyInviteTokenRequest.md)| The token to be verified and optional parameters. | 

### Return type

[**VerifyTokenResponse**](VerifyTokenResponse.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

