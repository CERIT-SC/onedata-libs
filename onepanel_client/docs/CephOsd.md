# CephOsd

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Host on which given OSD should be deployed. It must be the full host name and not an \&quot;alias\&quot; as used in Oneprovider cluster deployment. | 
**id** | **int** | Id of the OSD. | 
**uuid** | **str** | UUID of the OSD daemon. If provided, will be used to skip deployment of existing OSDs (identified by the UUID). Must be a 32-character hex string. By default will be generated automatically. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

