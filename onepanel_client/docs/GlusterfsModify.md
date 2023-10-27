# GlusterfsModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of storage.  &#x60;type &#x3D; \&quot;glusterfs\&quot;&#x60;  [GlusterFS](https://www.gluster.org/) volume directly attached to the Oneprovider.  | 
**volume** | **str** | The name of the volume to use as a storage backend. | [optional] 
**hostname** | **str** | The hostname (IP address or FQDN) of GlusterFS volume server. | [optional] 
**port** | **int** | The GlusterFS port on volume server. | [optional] 
**transport** | **str** | The transport protocol to use to connect to the volume server. | [optional] 
**mount_point** | **str** | Relative mountpoint within the volume which should be used by Oneprovider. | [optional] 
**xlator_options** | **str** | Volume specific GlusterFS translator options, in the format:   TRANSLATOR1.OPTION1&#x3D;VALUE1;TRANSLATOR2.OPTION2&#x3D;VALUE2;...  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

