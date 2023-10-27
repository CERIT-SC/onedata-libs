# AutoStorageImportInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Describes status of current (or last finished) auto storage import scan in given space. | 
**start** | **int** | Time at which current (or last finished) scan has been started. | 
**stop** | **int** | Time at which current (or last finished) scan has been stopped. | 
**created_files** | **int** | Counter of created files (both directories and regular files) that has been detected during current (or last finished) scan. | 
**modified_files** | **int** | Counter of modified files (both directories and regular files) that has been detected during current (or last finished) scan. | 
**deleted_files** | **int** | Counter of deleted files (both directories and regular files) that has been detected during current (or last finished) scan. | 
**unmodified_files** | **int** | Counter of unmodified files (both directories and regular files) that has been detected during current (or last finished) scan. | 
**failed_files** | **int** | Counter of files (both directories and regular files) for which the processing has failed during current (or last finished) scan. | 
**next_scan** | **int** | Estimated time at which next scan will be enqueued. | [optional] 
**total_scans** | **int** | Total number of performed scans. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

