# LinkedAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idp** | **str** | Id of the Identity Provider, as specified in Onezone&#x27;s auth.config. | 
**subject_id** | **str** | Unique user Id assigned by the Identity Provider. | 
**full_name** | **str** | User&#x27;s full name (given names + surname). | [optional] 
**username** | **str** | User&#x27;s human-readable identifier, unique across the system. Makes it easier to identify the user and can be used for signing in with password.  | [optional] 
**emails** | **list[str]** | The list of user email accounts. | [optional] 
**entitlements** | **list[str]** | A list of strings denoting user group memberships as acquired from the identity provider. Memberships are in Onedata normalized form.  | [optional] 
**custom** | **object** | Custom user data collected upon login, depending on Onezone auth.config. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

