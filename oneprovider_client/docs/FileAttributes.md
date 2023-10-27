# FileAttributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | File name. | [optional] 
**type** | [**FileType**](FileType.md) |  | [optional] 
**mode** | **str** | POSIX file permissions as string expressing octal notation. | [optional] 
**size** | **int** | Size of the file in bytes. | [optional] 
**atime** | **int** | Last access timestamp (in seconds). | [optional] 
**mtime** | **int** | Last modification timestamp (in seconds). | [optional] 
**ctime** | **int** | Last attributes modification timestamp (in seconds). | [optional] 
**owner_id** | **str** | Id of the owner of this file. | [optional] 
**file_id** | **str** | Id of the file. | [optional] 
**parent_id** | **str** | Id of the parent directory or &#x60;null&#x60; in case of file tree root. | [optional] 
**provider_id** | **str** | Id of the provider on which this file was created. | [optional] 
**storage_user_id** | **str** | Id of the owner of this file on storage. | [optional] 
**storage_group_id** | **str** | Id of the group owner of this file on storage. | [optional] 
**shares** | **list[str]** | The list of Ids of shares created for this file. | [optional] 
**hardlinks_count** | **int** | The number of hard links (including this one) associated with this file.  | [optional] 
**index** | **str** | File index that can be provided as starting point when listing files.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

