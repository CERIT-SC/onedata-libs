# ArchiveRecallDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_id** | **str** | Id of the archive that is being recalled. | 
**dataset_id** | **str** | Id of the dataset from which the archive was created. | [optional] 
**start_time** | **int** | Timestamp in milliseconds (UNIX epoch) when the recall started (null if not started yet). | [optional] 
**finish_time** | **int** | Timestamp in milliseconds (UNIX epoch) when the recall finished (null if not finished yet). | [optional] 
**total_file_count** | **int** | Number of files in source archive (number of files that is to be copied by recall). | 
**total_byte_size** | **int** | Number of bytes in source archive (number of bytes that is to be copied by recall). | 
**last_error** | [**ArchiveRecallDetailsLastError**](ArchiveRecallDetailsLastError.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

