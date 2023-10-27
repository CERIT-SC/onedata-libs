# FileDistributionDistributionPerProvider

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Indicates whether fetching file distribution for this provider was successful. | [optional] 
**logical_size** | **int** | Logical size of file/dir as seen by this provider (only if &#x60;success&#x60; &#x3D; true). | [optional] 
**distribution_per_storage** | [**dict(str, FileDistributionDistributionPerStorage)**](FileDistributionDistributionPerStorage.md) | Map with file distribution per storage.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

