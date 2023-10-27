# Share

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_id** | **str** | Share Id. | 
**name** | **str** | The name of the share. | 
**description** | **str** | Description of the share contents, interpreted as markdown format when displayed in GUI. | 
**public_url** | **str** | Publicly accessible link that can be used to view the contents of the share in a web browser. Anyone with the link will be able to access the share browser, without any authentication.  | 
**public_rest_url** | **str** | URL to the publicly accessible REST endpoint, which can be used to programmatically access the share information and data. The endpoint does not require any authentication.  | 
**space_id** | **str** | The Id of the space in which the share was created. *Not included in public share details.*  | [optional] 
**root_file_id** | **str** | Public Id of shared file or directory, allowing read access to its contents without authentication. | 
**file_type** | **str** | Denotes the type of the shared element (file or directory) | 
**handle_id** | **str** | The Id of open data Handle (e.g. DOI or PID) assigned to this share or null. | 
**creator** | [**Subject**](Subject.md) |  | [optional] 
**creation_time** | [**Timestamp**](Timestamp.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

