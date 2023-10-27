# SpaceDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Id of the space. | 
**name** | **str** | The name of the space. | 
**storage_id** | **str** | Id of storage that supports this space on provider that is associated with this panel.  | 
**local_storages** | **list[str]** | The list of IDs of cluster storage resources. | 
**supporting_providers** | **dict(str, int)** | The collection of provider IDs with associated supported storage space in bytes.  | 
**storage_import** | [**StorageImport**](StorageImport.md) |  | [optional] 
**space_occupancy** | **int** | Amount of storage [b] used by data from given space on that storage. | 
**accounting_enabled** | **bool** | Indicates if accounting is enabled. The accounting mechanism utilizes directory  statistics to keep track of quota usage within a space for the corresponding  supporting provider.  | 
**dir_stats_service_enabled** | **bool** | Indicates if the directory statistics service is enabled.  The service gathers statistics concerning logical and physical directory size, file count and update times. It cannot be disabled if accounting is enabled.  | 
**dir_stats_service_status** | **str** | Current status of directory statistics service. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

