# SpaceModifyRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | The storage space size in bytes that provider is willing to assign to the space.  | [optional] 
**auto_storage_import_config** | [**AutoStorageImportConfig**](AutoStorageImportConfig.md) |  | [optional] 
**accounting_enabled** | **bool** | Indicates if accounting is enabled. The accounting mechanism utilizes directory  statistics to keep track of quota usage within a space for the corresponding  supporting provider.  | [optional] 
**dir_stats_service_enabled** | **bool** | Indicates if the directory statistics service is enabled.  The service gathers statistics concerning logical and physical directory size, file count and update times. It cannot be disabled if accounting is enabled.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

