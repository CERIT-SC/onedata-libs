# CephModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the modified storage. Must be given explicitly and must match the actual type of subject storage - this redundancy is needed due to limitations of OpenAPI polymorphism.  &#x60;type &#x3D; \&quot;ceph\&quot;&#x60;  (**DEPRECATED** - use Ceph RADOS instead) storage backend compatible with [Ceph](http://ceph.com/ceph-storage/) object storage, using the deprecated &#x60;libradosstriper&#x60; library.  | 
**username** | **str** | The username of the Ceph cluster administrator. | [optional] 
**key** | **str** | The admin key to access the Ceph cluster. | [optional] 
**monitor_hostname** | **str** | The monitor hostname. | [optional] 
**cluster_name** | **str** | The Ceph cluster name. | [optional] 
**pool_name** | **str** | The Ceph pool name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

