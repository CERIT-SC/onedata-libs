# StorageImport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Mode of the storage import within the space.  In case of &#x60;auto&#x60; mode, the storage will be automatically scanned and data will be imported from storage into the assigned Onedata space without need for copying the data.  Configuration of the auto storage import can be passed in the &#x60;autoStorageImportConfig&#x60; parameter. It is possible to enable periodical scans for automatic detection of changes on the storage (refer to the option &#x60;continuousScan&#x60; in the config).  In case of &#x60;manual&#x60; mode, the files must be registered manually by the space users with REST API. Registration of directories is not supported. For more info please read: https://onedata.org/#/home/api/stable/oneprovider?anchor&#x3D;tag/File-registration  | [optional] [default to 'auto']
**auto_storage_import_config** | [**AutoStorageImportConfig**](AutoStorageImportConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

