# Harvester

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**harvester_id** | **str** | Unique harvester Id. | 
**name** | **str** | The name of the harvester. | 
**public** | **bool** | Whether given harvester is public.  More on public harvesters: [Query harvester index](#operation/query_harvester_index)    | 
**harvesting_backend_type** | **str** | Type of external harvesting backend that will provide persistence and analytics for harvested metadata. Can be chosen from predefined backends and optionally custom ones configured by Onezone admins. Can be omitted if default harvester backend is set up in Onezone. | 
**harvesting_backend_endpoint** | **str** | Endpoint where the specified harvesting backend can be reached by Onezone to feed incoming metadata and perform queries. Can be omitted if default harvester backend is set up in Onezone. | 
**creator** | [**Subject**](Subject.md) |  | 
**creation_time** | [**Timestamp**](Timestamp.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

