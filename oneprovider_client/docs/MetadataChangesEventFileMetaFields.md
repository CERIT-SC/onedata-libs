# MetadataChangesEventFileMetaFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | File name. | [optional] 
**type** | [**FileType**](FileType.md) |  | [optional] 
**mode** | **int** | POSIX file permissions. | [optional] 
**owner** | **str** | File owner. | [optional] 
**provider_id** | **str** | Id of provider which created this file. | [optional] 
**shares** | **list[str]** | Array of this file shares Ids. | [optional] 
**deleted** | **bool** | Set to &#x27;true&#x27; when file itself was deleted but file metadata must remain for some time. Otherwise false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

