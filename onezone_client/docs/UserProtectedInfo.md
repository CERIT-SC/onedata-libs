# UserProtectedInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | Unique user Id. | 
**full_name** | **str** | User&#x27;s full name (given names + surname). | 
**username** | **str** | User&#x27;s human-readable identifier, unique across the system. Makes it easier to identify the user and can be used for signing in with password.  | 
**linked_accounts** | [**list[LinkedAccount]**](LinkedAccount.md) | The list of accounts linked to this user. | 
**emails** | **list[str]** |  | 
**basic_auth_enabled** | **bool** | Denotes if this user is allowed to authenticate with username &amp; password. | 
**blocked** | **bool** | Denotes if this user&#x27;s account has been blocked by the administrators. | 
**creation_time** | [**Timestamp**](Timestamp.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

