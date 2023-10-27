# WebdavCredentials

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the storage. Must be given explicitly and must match the actual type of subject storage - this redundancy is needed due to limitations of OpenAPI polymorphism.  | 
**credentials_type** | **str** | Determines the types of credentials provided in the credentials field.  | [optional] [default to 'none']
**credentials** | **str** | The credentials to authenticate with the WebDAV server. &#x60;basic&#x60; credentials should be provided in the form &#x60;username:password&#x60;, for &#x60;token&#x60; just the token. In case of &#x60;oauth2&#x60;, this field should contain the username for the WebDAV, while the token will be obtained and refreshed automatically in the background. For &#x60;none&#x60; this field is ignored.  | [optional] 
**oauth2_id_p** | **str** | In case &#x60;oauth2&#x60; credential type is selected and Onezone is configured with support for multiple external IdP&#x27;s, this field must contain the name of the IdP which authenticates requests to the WebDAV endpoint. If Onezone has only one external IdP, it will be selected automatically.  | [optional] 
**onedata_access_token** | **str** | When registering storage with feed of LUMA DB set to&#x60;auto&#x60; and with &#x60;oauth2&#x60; external IdP, this field must contain a valid Onedata access token of the user on whose behalf the WebDAV storage will be accessed by all users with access to any space supported by this storage.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

