# NFSModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of storage.  &#x60;type &#x3D; \&quot;nfs\&quot;&#x60;    NFS storage.  | 
**host** | **str** | The hostname (IP address or FQDN) of NFS server. | [optional] 
**version** | **int** | The NFS protocol version. Allowed values are 3 (default) and 4 (experimental). | [optional] 
**volume** | **str** | The name of the NFS volume (export). | [optional] 
**connection_pool_size** | **int** | The size of NFS connection pool. | [optional] 
**dir_cache** | **bool** | Enables directory caching. | [optional] 
**read_ahead** | **int** | The size of readahead in bytes. | [optional] 
**auto_reconnect** | **int** | The number of automatic reconnect attempts to the server. Setting &#x60;-1&#x60; enables infinite number of reconnects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

