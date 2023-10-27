# ProviderModifyRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name under which the provider has been registered in a zone. | [optional] 
**subdomain_delegation** | **bool** | If enabled, the storage provider will be assigned a subdomain in onezone&#x27;s domain and &#x27;subdomain&#x27; property must be provided. If disabled, &#x27;domain&#x27; property should be provided.  | [optional] 
**subdomain** | **str** | Unique subdomain in onezone&#x27;s domain for the provider. This property is required only if subdomain delegation is enabled. Otherwise it is ignored.  | [optional] 
**domain** | **str** | The fully qualified domain name of the provider or its IP address (only for single-node deployments or clusters with a reverse proxy). This property is required only if subdomain delegation is disabled. Otherwise it is ignored.  | [optional] 
**geo_longitude** | **float** | The geographical longitude of the provider. | [optional] 
**geo_latitude** | **float** | The geographical latitude of the provider. | [optional] 
**admin_email** | **str** | Email address of the oneprovider administrator. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

