# ClusterDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the cluster record. | 
**type** | **str** | Type of the cluster. | 
**service_id** | **str** | The Id of the service hosted on this cluster - depending on the type equal to the Oneprovider Id or \&quot;onezone\&quot; in case of Onezone cluster  | 
**worker_version** | [**VersionInfo**](VersionInfo.md) |  | 
**onepanel_version** | [**VersionInfo**](VersionInfo.md) |  | 
**onepanel_proxy** | **bool** | Is Onepanel proxy enabled - if so, onepanel GUI is served on cluster&#x27;s domain at port 443 (rather than 9443).  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

