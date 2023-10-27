# onepanel_client.UserManagementApi

All URIs are relative to */api/v3/onepanel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_onezone_user**](UserManagementApi.md#add_onezone_user) | **POST** /zone/users | Create Onezone user
[**change_user_password**](UserManagementApi.md#change_user_password) | **PATCH** /zone/users/{id} | Set password for Onezone user
[**get_onezone_user**](UserManagementApi.md#get_onezone_user) | **GET** /zone/users/{id} | Get Onezone user details
[**get_onezone_users**](UserManagementApi.md#get_onezone_users) | **GET** /zone/users | List Onezone users

# **add_onezone_user**
> Id add_onezone_user(body)

Create Onezone user

Creates a new Onezone user account with Basic (username & password) authentication enabled.  ***Example cURL requests***  **Create Onezone user with username & password** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST https://$OZ_PANEL_HOST/api/v3/onepanel/zone/users \\ -H \"Content-Type: application/json\" -d '{     \"username\": \"someUser\",     \"password\": \"somePassword\" }'  {     \"id\": \"b519b3ac46823b2b83b6cb85e1b16f4fchaa0f\" } ``` 

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
api_instance = onepanel_client.UserManagementApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.OnezoneUserCreateRequest() # OnezoneUserCreateRequest | The user configuration details.

try:
    # Create Onezone user
    api_response = api_instance.add_onezone_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserManagementApi->add_onezone_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OnezoneUserCreateRequest**](OnezoneUserCreateRequest.md)| The user configuration details. | 

### Return type

[**Id**](Id.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_password**
> change_user_password(body, id)

Set password for Onezone user

Sets a new password for a Onezone user using Basic authentication.  ***Example cURL requests***  **Set Onezone user password** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X PATCH https://$OZ_PANEL_HOST/api/v3/onepanel/zone/users/$USER_ID \\ -H \"Content-Type: application/json\" -d '{\"newPassword\": \"someNewPassword\"}' ``` 

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
api_instance = onepanel_client.UserManagementApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.PasswordChangeRequest() # PasswordChangeRequest | 
id = 'id_example' # str | Id of the user whose password is changed.

try:
    # Set password for Onezone user
    api_instance.change_user_password(body, id)
except ApiException as e:
    print("Exception when calling UserManagementApi->change_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordChangeRequest**](PasswordChangeRequest.md)|  | 
 **id** | **str**| Id of the user whose password is changed. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_onezone_user**
> OnezoneUser get_onezone_user(id)

Get Onezone user details

Returns the configuration information of the Onezone user.  ***Example cURL requests***  **Get Onezone user details** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET https://$OZ_PANEL_HOST/api/v3/onepanel/zone/users/$USER_ID  {     \"username\": \"someUser\",     \"userId\": \"b519b3ac46823b2b83b6cb85e1b16f4fchaa0f\",     \"fullName\": \"Unnamed User\" } ``` 

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
api_instance = onepanel_client.UserManagementApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | Id of the user to be described.

try:
    # Get Onezone user details
    api_response = api_instance.get_onezone_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserManagementApi->get_onezone_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the user to be described. | 

### Return type

[**OnezoneUser**](OnezoneUser.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_onezone_users**
> Ids get_onezone_users()

List Onezone users

List Ids of Onezone users.  ***Example cURL requests***  **Get Onezone user ids** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET https://$OZ_PANEL_HOST/api/v3/onepanel/zone/users  {     \"ids\": [         \"f891d1ddf693232bbf0c11fe3cd9f7e7cheda9\",         \"eefc8a11e1776d0797969ccf0b59c6dcch73dc\",         \"ec0a39261b325cdc74e9c2d6b54fa786ch0419\"     ] } ``` 

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
api_instance = onepanel_client.UserManagementApi(onepanel_client.ApiClient(configuration))

try:
    # List Onezone users
    api_response = api_instance.get_onezone_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserManagementApi->get_onezone_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Ids**](Ids.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

