# XRootDCredentials

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the storage. Must be given explicitly and must match the actual type of subject storage - this redundancy is needed due to limitations of OpenAPI polymorphism.  | 
**credentials_type** | **str** | Determines the types of credentials provided in the credentials field.  | [optional] [default to 'none']
**credentials** | **str** | The credentials to authenticate with the XRootD server. For &#x60;pwd&#x60; credentials type, this field should contain simply user and password, e.g. &#x60;admin:password&#x60;. For &#x60;none&#x60; this field is ignored.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

