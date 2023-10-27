# WebCert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lets_encrypt** | **bool** | If true, the certificate is obtained from Let&#x27;s Encrypt service and renewed automatically. Otherwise, the certificate management is up to the administrator.  | 
**expiration_time** | **str** | Installed certificate&#x27;s expiration time in ISO 8601 format.  | 
**creation_time** | **str** | Installed certificate&#x27;s creation time in ISO 8601 format.  | 
**status** | **str** | Describes certificate validity status. | 
**paths** | [**WebCertPaths**](WebCertPaths.md) |  | 
**domain** | **str** | The domain (Common Name) for which current certificate was issued.  | 
**issuer** | **str** | Issuer value of the current certificate.  | 
**last_renewal_success** | **str** | Date and time in ISO 8601 format. Represents last successful Let&#x27;s Encrypt certification. If there are no successful attempts its value is null. This property is omitted if letsEncrypt is off.  | [optional] 
**last_renewal_failure** | **str** | Date and time in ISO 8601 format. Represents last unsuccessful Let&#x27;s Encrypt certification. If there are no successful attempts its value is null. This property is omitted if letsEncrypt is off.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

