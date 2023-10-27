# EmbeddedcephModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the storage and corresponding Ceph pool. | [optional] 
**copies_number** | **int** | Desired number of object replicas in the pool. When below this number the pool still may be used in &#x27;degraded&#x27; mode. Defaults to &#x60;2&#x60; if there are at least 2 OSDs, &#x60;1&#x60; otherwise. | [optional] 
**min_copies_number** | **int** | Minimum number of object replicas in the pool. Below this threshold any I/O for the pool is disabled. Must be lower or equal to &#x27;copiesNumber&#x27;. Defaults to &#x60;min(2, copiesNumber)&#x60; if there are at least 2 OSDs, &#x60;1&#x60; otherwise. | [optional] 
**type** | **str** | The type of storage.  &#x60;type &#x3D; \&quot;embeddedceph\&quot;&#x60;  Embedded Ceph cluster that has been deployed during deployment of Oneprovider. For more information on embedded Ceph deployment please see [here](https://onedata.org/#/home/documentation/stable/doc/administering_onedata/ceph_cluster_deployment.html).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

