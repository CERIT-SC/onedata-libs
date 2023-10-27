# Handle

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handle_id** | **str** | Unique Id of the handle in Onedata. | 
**public_handle** | **str** | Unique Id of the handle as registered in the handle service. Depending on the handle service, can be an Id (DOI: 10.5072/w95Zlng) or an URL (PID: http://hdl.handle.net/21.T15999/TgAl7s0).  | 
**handle_service_id** | **str** | Id of the service where the handle was registered. *Not included in public handle details.*  | [optional] 
**resource_type** | **str** | The type of resource to be registered. | 
**resource_id** | **str** | The Id of the resource, corresponding to resourceType (currently, always a share Id). | 
**metadata** | **str** | Dublin Core metadata for the resource encoded in XML. | 
**timestamp** | **str** | Timestamp of the last Handle modification. | 
**creator** | [**Subject**](Subject.md) |  | [optional] 
**creation_time** | [**Timestamp**](Timestamp.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

