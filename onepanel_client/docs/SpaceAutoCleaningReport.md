# SpaceAutoCleaningReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of an auto-cleaning report. | 
**index** | **str** | Index of an auto-cleaning report. It can be used to list report Ids starting from given report.  | 
**started_at** | **str** | Start time of an auto-cleaning run in ISO 8601 format. | 
**stopped_at** | **str** | Finish time of an auto-cleaning run in ISO 8601 format. | 
**released_bytes** | **int** | Number of bytes deleted during an auto-cleaning run. | 
**bytes_to_release** | **int** | Number of bytes that should be deleted. | 
**files_number** | **int** | Number of deleted files. | 
**status** | **str** | Status of an auto-cleaning run. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

