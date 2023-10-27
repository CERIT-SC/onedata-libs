# Dataset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**DatasetState**](DatasetState.md) |  | 
**dataset_id** | **str** | Dataset Id. | 
**parent_id** | **str** | Parent dataset Id or &#x60;null&#x60; in case of top dataset. | [optional] 
**root_file_id** | **str** | Id of file or directory being the dataset root. Once the dataset has been established the root file can no longer be changed. Even after detaching dataset it can be reattached only to the same file and only if it still exists.  | 
**root_file_type** | [**FileType**](FileType.md) |  | 
**root_file_path** | **str** | Path to the file or directory in the virtual file system. For datasets in &#x60;detached&#x60; state this field is frozen and shows the value it had at the time of detaching. It is done for archival purposes as file may have been renamed or removed.  | 
**root_file_deleted** | **bool** | Flag informing whether dataset&#x27;s root file has been deleted.  Only relevant for detached datasets. If the root file has been deleted, it is no longer possible to reattach the dataset.  | [optional] 
**protection_flags** | [**DatasetProtectionFlags**](DatasetProtectionFlags.md) |  | 
**effective_protection_flags** | [**DatasetProtectionFlags**](DatasetProtectionFlags.md) |  | 
**creation_time** | [**Timestamp**](Timestamp.md) |  | 
**archive_count** | **int** | Number of archives created from the dataset.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

