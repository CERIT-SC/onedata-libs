# HarvesterIndexStatsDetailsSpaceIdProviderId

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_seq** | **int** | Highest sequence number in given space in given provider already harvested in this index | 
**max_seq** | **int** | Highest known sequence in given space in given provider | 
**error** | **str** | Short description of encountered error if last harvesting failed | 
**last_update** | [**Timestamp**](Timestamp.md) |  | 
**archival** | **bool** | Stats are marked archival when it is no longer possible to harvest metadata in given space in given provider (e.g space was removed from harvester) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

