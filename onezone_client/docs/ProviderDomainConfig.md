# ProviderDomainConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subdomain_delegation** | **bool** | True if this Oneprovider has been assigned a subdomain in Onezone&#x27;s domain.  | [optional] 
**domain** | **str** | The fully qualified domain name of the Oneprovider or its IP address (only for single-node deployments or clusters with a reverse proxy).  | [optional] 
**subdomain** | **str** | Unique subdomain in Onezone&#x27;s domain for the Oneprovider. Applicable if subdomain delegation is enabled, null otherwise.  | [optional] 
**ip_list** | **list[str]** | The list of IP addresses advertised by Onezone on behalf of the Oneprovider. Applicable if subdomain delegation is enabled, empty list otherwise.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

