# CephMonitor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Host on which given monitor should be deployed. There may be only one monitor per host. Attempts at creating additional monitors at the same host will be ignored. | 
**ip** | **str** | Local IP to be used for communication between Ceph nodes. If not specified it will be autodetected. | [optional] 
**id** | **str** | Monitor identifier. Equal to the hostname of the node where monitor is deployed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

