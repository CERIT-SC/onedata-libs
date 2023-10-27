# Archive

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_id** | **str** | Archive Id. | 
**state** | [**ArchiveState**](ArchiveState.md) |  | 
**dataset_id** | **str** | Id of the dataset from which the archive has been created. | 
**root_directory_id** | **str** | Id of the hidden directory in the space where the archive is stored.  | 
**creation_time** | [**Timestamp**](Timestamp.md) |  | 
**config** | [**ArchiveConfig**](ArchiveConfig.md) |  | [optional] 
**description** | [**ArchiveDescription**](ArchiveDescription.md) |  | 
**preserved_callback** | [**ArchivePreservedCallback**](ArchivePreservedCallback.md) |  | [optional] 
**deleted_callback** | [**ArchiveDeletedCallback**](ArchiveDeletedCallback.md) |  | [optional] 
**stats** | [**ArchiveStats**](ArchiveStats.md) |  | 
**base_archive_id** | [**ArchiveBase**](ArchiveBase.md) |  | [optional] 
**related_aip_id** | **str** | Id of the related archival information package (AIP) archive. Can be null when there is no such archive.  | [optional] 
**related_dip_id** | **str** | Id of the related dissemination information package (DIP) archive. Can be null when there is no such archive.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

