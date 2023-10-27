# ProviderClusterConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | Hostname suffix common for all services in the cluster. Together with a node hostname constitutes a fully qualified domain name (FQDN) of the node. May be skipped to allow unrelated hostnames for each node.  | [optional] [default to '']
**nodes** | [**dict(str, ZoneClusterConfigurationNodes)**](ZoneClusterConfigurationNodes.md) | The collection of nodes aliases associated with nodes properties. | 
**databases** | [**ClusterDatabases**](ClusterDatabases.md) |  | 
**managers** | [**ClusterManagers**](ClusterManagers.md) |  | 
**workers** | [**ClusterWorkers**](ClusterWorkers.md) |  | 
**storages** | [**StorageCreateRequest**](StorageCreateRequest.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

