# ProviderRegistrationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Token for registering a new Oneprovider. If Onezone allows regular users to freely register Oneproviders, it can be obtained from GUI or REST API. Otherwise, only a Onezone admin can issue such token.  | 
**name** | **str** | Oneprovider name. | 
**admin_email** | **str** | Contact email address of the Oneprovider admin. | 
**subdomain_delegation** | **bool** | If enabled, the Oneprovider will be assigned a subdomain in Onezone&#x27;s domain and &#x27;subdomain&#x27;, &#x27;ipList&#x27; properties must be provided. If disabled, &#x27;domain&#x27; property must be provided.  | 
**subdomain** | **str** | Unique subdomain in onezone&#x27;s domain for the Oneprovider. Required if subdomain delegation is enabled.  | [optional] 
**ip_list** | **list[str]** | List of Oneprovider&#x27;s IPv4 addresses to be advertised by Onezone&#x27;s DNS. Required if subdomain delegation is enabled.  | [optional] 
**domain** | **str** | The fully qualified domain name of the Oneprovider or its IP address (only for single-node deployments or clusters with a reverse proxy). Required if subdomain delegation is disabled.  | [optional] 
**latitude** | **float** | The geographical latitude of the Oneprovider&#x27;s data center location. | [optional] 
**longitude** | **float** | The geographical longitude of the Oneprovider&#x27;s data center location. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

