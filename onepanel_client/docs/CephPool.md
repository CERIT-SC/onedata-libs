# CephPool

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the pool. | [optional] 
**copies_number** | **int** | Desired number of object replicas in the pool. When below this number the pool still may be used in &#x27;degraded&#x27; mode. Defaults to &#x60;2&#x60; if there are at least 2 OSDs, &#x60;1&#x60; otherwise. | [optional] 
**min_copies_number** | **int** | Minimum number of object replicas in the pool. Below this threshold any I/O for the pool is disabled. Must be lower or equal to &#x27;copiesNumber&#x27;. Defaults to &#x60;min(2, copiesNumber)&#x60; if there are at least 2 OSDs, &#x60;1&#x60; otherwise. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

