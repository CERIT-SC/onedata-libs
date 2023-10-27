# HarvesterUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the harvester. | [optional] 
**harvesting_backend_type** | **str** | Type of external harvesting backend that will provide persistence and analytics for harvested metadata. Can be chosen from predefined backends and optionally custom ones configured by Onezone admins. | [optional] 
**harvesting_backend_endpoint** | **str** | Endpoint where the specified harvesting backend can be reached by Onezone to feed incoming metadata and perform queries. Note that this option should be used only when changing to a new location of the same harvester backend. Otherwise [create a new harvester](#operation/create_harvester). | [optional] 
**public** | **bool** | Public harvester allows any user to query its indices. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

