# XRootD

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the storage. Must be given explicitly and must match the actual type of subject storage - this redundancy is needed due to limitations of OpenAPI polymorphism.  | 
**timeout** | **int** | Storage operation timeout in milliseconds. | [optional] 
**skip_storage_detection** | **bool** | If true, detecting whether storage is directly accessible by the Oneclient will not be performed. This option should be set to true on readonly storages.  | [optional] [default to False]
**luma_feed** | **str** | Type of feed for LUMA DB. Feed is a source of user/group mappings used to populate the LUMA DB. For more info please read: https://onedata.org/#/home/documentation/doc/administering_onedata/luma.html  | [optional] [default to 'auto']
**luma_feed_url** | **str** | URL of external feed for LUMA DB. Relevant only if lumaFeed equals &#x60;external&#x60;. | [optional] 
**luma_feed_api_key** | **str** | API key checked by external service used as feed for LUMA DB. Relevant only if lumaFeed equals &#x60;external&#x60;.  | [optional] 
**qos_parameters** | **dict(str, str)** | Map with key-value pairs used for describing storage QoS parameters. | [optional] 
**imported_storage** | **bool** | Defines whether storage contains existing data to be imported.  | [optional] [default to False]
**archive_storage** | **bool** | Defines whether storage supports long-term dataset archiving.  | [optional] [default to False]
**readonly** | **bool** | Defines whether the storage is readonly. If enabled, Oneprovider will block any operation that writes, modifies or deletes data on the storage. Such storage can only be used to import data into the space. Mandatory to ensure proper behaviour if the backend storage is actually configured as readonly. This option is available only for imported storages.  | [optional] [default to False]
**credentials_type** | **str** | Determines the types of credentials provided in the credentials field.  | [optional] [default to 'none']
**credentials** | **str** | The credentials to authenticate with the XRootD server. For &#x60;pwd&#x60; credentials type, this field should contain simply user and password, e.g. &#x60;admin:password&#x60;. For &#x60;none&#x60; this field is ignored.  | [optional] 
**url** | **str** | Full URL of the XRootD server, including scheme (root or http) and path, e.g. &#x60;root://192.168.0.1//data&#x60;. Please note, that XRootD URL format requires double slash after host to indicate absolute path.  | 
**file_mode_mask** | **str** | Defines the file permissions mask, which is used to map XRootD file mode to POSIX mode. For instance a fileModeMask &#x60;0664&#x60; for readable file on XRootD would result in a file which is readable for all users, but file which is writeable in XRootD will be only writeable by user and group.  | [optional] [default to '0664']
**dir_mode_mask** | **str** | Defines the directory permissions mask, which is used to map XRootD dir mode to POSIX mode. For instance a dirModeMask &#x60;0770&#x60; for readable directory on XRootD would result in a directory which is readable for owner and group but not for others.  | [optional] [default to '0775']
**storage_path_type** | **str** | Determines how the logical file paths will be mapped on the storage. &#x27;canonical&#x27; paths reflect the logical file names and directory structure, however each rename operation will require renaming the files on the storage. &#x27;flat&#x27; paths are based on unique file UUID&#x27;s and do not require on-storage rename when logical file name is changed.  | [optional] [default to 'canonical']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

