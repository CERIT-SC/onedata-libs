# ProviderDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Id assigned by a zone. | 
**name** | **str** | The name under which the Oneprovider has been registered in a zone. | 
**subdomain_delegation** | **bool** | If enabled, the storage Oneprovider has a subdomain in onezone&#x27;s domain and &#x27;subdomain&#x27; property must be provided.  | 
**subdomain** | **str** | Unique subdomain in onezone&#x27;s domain for the Oneprovider. Required if subdomain delegation is enabled.  | [optional] 
**domain** | **str** | The fully qualified domain name of the Oneprovider or its IP address (only for single-node deployments or clusters with a reverse proxy).  | 
**admin_email** | **str** | Email address of the Oneprovider administrator. Omitted if it could not be retrievied. | [optional] 
**geo_longitude** | **float** | The geographical longitude of the Oneprovider. | 
**geo_latitude** | **float** | The geographical latitude of the Oneprovider. | 
**onezone_domain_name** | **str** | The domain name of a zone where this storage Oneprovider is registered. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

