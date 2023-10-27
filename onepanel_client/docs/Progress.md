# Progress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_nodes** | **bool** | True after user assigned services to cluster nodes and they were deployed. | [optional] 
**cluster_ips** | **bool** | True after user provided public IPs of cluster nodes or confirmed autodetected defaults. Also true if interactiveDeployment was disabled. | [optional] 
**web_certificate** | **bool** | True after user decided whether to use Let&#x27;s Encrypt certificates or if interactiveDeployment was disabled. | [optional] 
**dns_check** | **bool** | True after user reviewed results of DNS check or if interactiveDeployment was disabled. | [optional] 
**storage_setup** | **bool** | True after at least one storage was added to op_worker. Omitted in Onezone panel. | [optional] 
**is_registered** | **bool** | True if the Oneprovider is registered at Onezone. Omitted in Onezone panel. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

