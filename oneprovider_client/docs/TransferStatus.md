# TransferStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Requested type of transfer. | 
**user_id** | **str** | Id of the user that started the transfer. | 
**rerun_id** | **str** | If the transfer was rerun, this field contains the Id of the new transfer, otherwise null. | 
**effective_job_transfer_id** | **str** | Last transfer Id in chain made of &#x60;rerunId&#x60;. | [optional] 
**space_id** | **str** | Id of space in context of which transfer was performed. | 
**data_source_type** | **str** | Indicates the method of determining files to be transferred.        &#x60;type &#x3D; \&quot;file\&quot;&#x60; - this transfer covers a single file or a whole directory (recursively). When scheduling such transfer, the user must have permissions to access the file/directory.      &#x60;type &#x3D; \&quot;view\&quot;&#x60; - this transfer covers files that are returned as a result of querying chosen view. The view must be defined on all providers involved in the process and querying it must return a valid list of file ids to be transferred. For more information about views, please see [here](https://onedata.org/#/home/documentation/doc/using_onedata/replication_management.html#advanced-operations-using-views).  | 
**file_id** | **str** | Id of the transferred file or directory. | [optional] 
**file_path** | **str** | Path to the file or directory in the virtual file system. | [optional] 
**view_name** | **str** | Name of the view that was queried to obtain the list of files to transfer.  | [optional] 
**query_view_params** | [**QueryViewParams**](QueryViewParams.md) |  | [optional] 
**transfer_status** | **str** | Overall status of transfer. | 
**effective_job_status** | **str** | Overall status of effective transfer job (the last one in chain made of &#x60;rerunId&#x60;).  | [optional] 
**replication_status** | **str** | The status of transfer replication phase. | 
**eviction_status** | **str** | The status of transfer eviction phase. | 
**replicating_provider_id** | **str** | Id of provider to which data was copied, ensuring that the provider has a complete replica at the end of the process.  | 
**evicting_provider_id** | **str** | Id of provider from which replica(s) were removed. | 
**callback** | **str** | Optional callback URL, which will be invoked on transfer completion. | 
**files_to_process** | **int** | Total number of files in this transfer. | 
**files_processed** | **int** | Number of files already processed. | 
**files_replicated** | **int** | Number of files already replicated. | 
**files_evicted** | **int** | Number of files already evicted. | 
**files_failed** | **int** | Number of files for which eviction or replication has failed. | 
**bytes_replicated** | **int** | Number of bytes already replicated. | 
**schedule_time** | **int** | Schedule time in seconds (POSIX epoch timestamp). | 
**start_time** | **int** | Start time in seconds (POSIX epoch timestamp). | 
**finish_time** | **int** | Finish time in seconds (POSIX epoch timestamp). | 
**last_update** | **int** | Last transfer update time in seconds (POSIX epoch timestamp). | 
**min_hist** | **dict(str, list[int])** | Replication statistics within the last minute, per provider. | 
**hr_hist** | **dict(str, list[int])** | Replication statistics within the last hour, per provider. | 
**dy_hist** | **dict(str, list[int])** | Replication statistics within the last day, per provider. | 
**mth_hist** | **dict(str, list[int])** | Replication statistics within the last month, per provider. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

