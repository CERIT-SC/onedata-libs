# HarvesterIndex

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index_id** | **str** | Unique Id of the index. | 
**name** | **str** | The name of the index. | 
**schema** | **str** | Schema of the index provided as string (e.g. encoded JSON). | 
**gui_plugin_name** | **str** | Mapping of index name to one recognized by gui plugin. Allows to specify this index to be used by GUI plugin to produce search results. Recognized gui index names are listed in gui plugin manifest. | 
**include_metadata** | **list[str]** | Specifies what types of file metadata should be harvested in this index. At least one type must be given. | 
**include_file_details** | **list[str]** | Specifies what file details should be harvested alongside the metadata. Enabling &#x60;metadataExistenceFlags&#x60; will add boolean flags saying whether the file has any metadata of certain type. The &#x60;fileName&#x60; field may be utilized by the GUI plugin to improve the browsing experience. | 
**include_rejection_reason** | **bool** | If enabled, all harvesting errors (e.g. when the index rejects a payload due to non-matching schema) are stored as text in the index, which may be useful for later analysis. | 
**retry_on_rejection** | **bool** | If enabled, all payloads rejected by the harvesting backend will be automatically analysed for offending data (e.g. fields that do not match the schema), pruned and submitted again. This might slow down the harvesting process and cause nonconformant metadata to be lost. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

