# CephCredentials

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the storage. Must be given explicitly and must match the actual type of subject storage - this redundancy is needed due to limitations of OpenAPI polymorphism.  | 
**username** | **str** | The username of the Ceph cluster user. In case of configuring storage, this field must be equal to name of the Ceph cluster admin.  | 
**key** | **str** | The key to access the Ceph cluster. In case of configuring storage, the key must be the key of admin user passed in &#x60;username&#x60;.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

