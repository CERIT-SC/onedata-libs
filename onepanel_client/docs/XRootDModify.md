# XRootDModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of storage.  &#x60;type &#x3D; \&quot;xrootd\&quot;&#x60;  Storage backend compatible with [XRootD](http://www.xrootd.org/) protocol.  | 
**url** | **str** | Full URL of the XRootD server, including scheme (root or http) and path, e.g. &#x60;root://192.168.0.1//data&#x60;. Please note, that XRootD URL format requires double slash after host to indicate absolute path.  | [optional] 
**credentials_type** | **str** | Determines the types of credentials provided in the credentials field.  | [optional] 
**credentials** | **str** | The credentials to authenticate with the XRootD server. For &#x60;pwd&#x60; credentials type, this field should contain simply user and password, e.g. &#x60;admin:password&#x60;. For &#x60;none&#x60; this field is ignored.  | [optional] 
**file_mode_mask** | **str** | Defines the file permissions mask, which is used to map XRootD file mode to POSIX mode. For instance a fileModeMask &#x60;0664&#x60; for readable file on XRootD would result in a file which is readable for all users, but file which is writeable in XRootD will be only writeable by user and group.  | [optional] 
**dir_mode_mask** | **str** | Defines the directory permissions mask, which is used to map XRootD dir mode to POSIX mode. For instance a dirModeMask &#x60;0770&#x60; for readable directory on XRootD would result in a directory which is readable for owner and group but not for others.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

