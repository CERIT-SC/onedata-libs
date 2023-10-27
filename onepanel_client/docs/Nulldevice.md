# Nulldevice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of storage.  &#x60;type &#x3D; \&quot;nulldevice\&quot;&#x60;  POSIX compatible storage which emulates behavior of &#x60;/dev/null&#x60; on local filesystem. Allows running various performance tests, which are not impacted by actual storage latency. Skip storage detection option is obligatory for this type of storage.  | 
**timeout** | **int** | Storage operation timeout in milliseconds. | [optional] 
**skip_storage_detection** | **bool** | If true, detecting whether storage is directly accessible by the Oneclient will not be performed. This option should be set to true on readonly storages.  | [optional] [default to False]
**luma_feed** | **str** | Type of feed for LUMA DB. Feed is a source of user/group mappings used to populate the LUMA DB. For more info please read: https://onedata.org/#/home/documentation/doc/administering_onedata/luma.html  | [optional] [default to 'auto']
**luma_feed_url** | **str** | URL of external feed for LUMA DB. Relevant only if lumaFeed equals &#x60;external&#x60;. | [optional] 
**luma_feed_api_key** | **str** | API key checked by external service used as feed for LUMA DB. Relevant only if lumaFeed equals &#x60;external&#x60;.  | [optional] 
**qos_parameters** | **dict(str, str)** | Map with key-value pairs used for describing storage QoS parameters. | [optional] 
**imported_storage** | **bool** | Defines whether storage contains existing data to be imported.  | [optional] [default to False]
**archive_storage** | **bool** | Defines whether storage supports long-term dataset archiving.  | [optional] [default to False]
**readonly** | **bool** | Defines whether the storage is readonly. If enabled, Oneprovider will block any operation that writes, modifies or deletes data on the storage. Such storage can only be used to import data into the space. Mandatory to ensure proper behaviour if the backend storage is actually configured as readonly. This option is available only for imported storages.  | [optional] [default to False]
**latency_min** | **int** | Minimum latency in milliseconds, which should be simulated for selected operations.  | [optional] 
**latency_max** | **int** | Maximum latency in milliseconds, which should be simulated for selected operations.  | [optional] 
**timeout_probability** | **float** | Probability (0.0, 1.0), with which an operation should return a timeout error.  | [optional] [default to 0.0]
**filter** | **str** | Comma-separated list of filesystem operations, for which latency and timeout should be simulated. Empty or &#x27;*&#x27; mean all operations will be affected.  | [optional] [default to '*']
**storage_path_type** | **str** | Determines how the logical file paths will be mapped on the storage. &#x27;canonical&#x27; paths reflect the logical file names and directory structure, however each rename operation will require renaming the files on the storage. &#x27;flat&#x27; paths are based on unique file UUID&#x27;s and do not require on-storage rename when logical file name is changed.  | [optional] [default to 'canonical']
**simulated_filesystem_parameters** | **str** | Specifies the parameters for a simulated null device filesystem. For example &#x60;2-2:2-2:0-1&#x60; will generate a filesystem tree which has 2 directories (&#x60;0&#x60; and &#x60;1&#x60;) and 2 files (&#x60;2&#x60; and &#x60;3&#x60;) in the root of the filesystem, each of these directories will have 2 subdirectories (&#x60;0&#x60; and &#x60;1&#x60;) and 2 files (&#x60;2&#x60; and &#x60;3&#x60;) and each of these subdirectories has only a single file (&#x60;0&#x60;). In order to specify the size of generated files, a size in bytes needs to be added as the last component of the parameter specification, for example &#x60;2-2:2-2:0-1:1048576&#x60;. Default empty string disables the simulated filesystem feature.  | [optional] [default to '']
**simulated_filesystem_grow_speed** | **float** | Determines the simulated filesystem grow rate. Default 0.0 value will cause all the files and directories defined by the &#x60;simulatedFilesystemParameters&#x60; specification to be visible immediately. For example value of 0.01 will increase the number of the visible filesystem entries by 1 file per 100 seconds, while 100.0 will increase it by 100 files per second.  | [optional] [default to 0.0]
**enable_data_verification** | **bool** | Enables data verification for &#x60;read&#x60; and &#x60;write&#x60; operations. Read operations will always return a predictable pattern of characters based on &#x60;offset&#x60; and &#x60;size&#x60;, and &#x60;write&#x60; operations will fail with I/O error, if the input data does not match the pattern at a given &#x60;offset&#x60;.  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

