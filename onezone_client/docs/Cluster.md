# Cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | The id of the cluster - depending on the type equal to the Oneprovider Id or \&quot;onezone\&quot; in case of Onezone cluster  | 
**type** | **str** | Type of the cluster | 
**worker_version** | [**VersionInfo**](VersionInfo.md) |  | 
**onepanel_version** | [**VersionInfo**](VersionInfo.md) |  | 
**onepanel_proxy** | **bool** | Is onepanel proxy enabled - if so, onepanel GUI is served on cluster&#x27;s domain at port 443 (rather than 9443).  | 
**creator** | [**Subject**](Subject.md) |  | 
**creation_time** | [**Timestamp**](Timestamp.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

