# Loopdevice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the OSD. Available types are: - blockdevice - formats a raw block device to store the data - loopdevice - stores data in a file mounted as loop device  | 
**path** | **str** | Path of the loopdevice file to be created. If omitted, default path will be generated according to following template: /volumes/persistence/ceph-loopdevices/osd-{uuid}.loop  | [optional] 
**size** | **int** | Size in bytes of the loopdevice file. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

