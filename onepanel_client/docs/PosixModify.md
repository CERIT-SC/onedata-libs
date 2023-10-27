# PosixModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of storage.  &#x60;type &#x3D; \&quot;posix\&quot;&#x60;  Any POSIX compatible storage, typically attached over high-throughput local network, such as NFS.  | 
**mount_point** | **str** | The absolute path to the directory where the POSIX storage is mounted on the cluster nodes.  | [optional] 
**root_uid** | **int** | UID of the user on whose behalf operations in the admin context will be performed on the storage. | [optional] 
**root_gid** | **int** | GID of the group on whose behalf operations in the admin context will be performed on the storage. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

