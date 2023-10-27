# OnezoneUserCreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | User&#x27;s human-readable identifier, unique across the system. Makes it easier to identify the user and can be used for signing in with password.  | 
**password** | **str** | User&#x27;s password (in plaintext). | 
**full_name** | **str** | User&#x27;s full name (given names + surname). | [optional] 
**groups** | **list[str]** | Ids of Onezone groups to which the user should be added. The groups must already exist.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

