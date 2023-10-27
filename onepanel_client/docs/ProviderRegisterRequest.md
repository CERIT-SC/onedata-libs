# ProviderRegisterRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name under which the provider should be registered in a zone.  | 
**token_provision_method** | **str** | Indicates how the Oneprovider registration token will be provided: * &#x60;\&quot;inline\&quot;&#x60; - the registration token must be placed in the **token**   field (consult for more information). * &#x60;\&quot;fromFile\&quot;&#x60; - the registration token will be read from given file,   specified in the **tokenFile** field (consult for more information).  | [optional] [default to 'inline']
**token** | **str** | Registration token obtained from Onezone. This token identifies the Onezone service where the Oneprovider will be registered and authorizes the registration request. Required when the &#x60;tokenProvisionMethod&#x60; is set to &#x60;\&quot;inline\&quot;&#x60;.  | [optional] 
**token_file** | **str** | Absolute path to the file containing the Oneprovider registration token. The token (and nothing else) should be placed in the file as plaintext. The file does not have to pre-exist - it may be created after this request is made (Onepanel will wait for the file to appear for some time). Required when the &#x60;tokenProvisionMethod&#x60; is set to &#x60;\&quot;fromFile\&quot;&#x60;.  | [optional] 
**subdomain_delegation** | **bool** | If enabled, the storage provider will be assigned a subdomain in onezone&#x27;s domain and &#x27;subdomain&#x27; property must be provided. If disabled, &#x27;domain&#x27; property should be provided.  | [default to False]
**subdomain** | **str** | Unique subdomain in onezone&#x27;s domain for the storage provider. Required if subdomain delegation is enabled.  | [optional] 
**domain** | **str** | The fully qualified domain name of the storage provider or its IP address (only for single-node deployments or clusters with a reverse proxy). Required if subdomain delegation is disabled.  | [optional] 
**geo_longitude** | **float** | The geographical longitude of the storage provider.  | [optional] 
**geo_latitude** | **float** | The geographical latitude of the storage provider.  | [optional] 
**admin_email** | **str** | Email address of the Oneprovider administrator. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

