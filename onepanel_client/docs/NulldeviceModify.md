# NulldeviceModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of storage.  &#x60;type &#x3D; \&quot;nulldevice\&quot;&#x60;  POSIX compatible storage which emulates behavior of &#x60;/dev/null&#x60; on local filesystem. Allows running various performance tests, which are not impacted by actual storage latency. Skip storage detection option is obligatory for this type of storage.  | 
**latency_min** | **int** | Minimum latency in milliseconds, which should be simulated for selected operations.  | [optional] 
**latency_max** | **int** | Maximum latency in milliseconds, which should be simulated for selected operations.  | [optional] 
**timeout_probability** | **float** | Probability (0.0, 1.0), with which an operation should return a timeout error.  | [optional] 
**filter** | **str** | Comma-separated list of filesystem operations, for which latency and timeout should be simulated. Empty or &#x27;*&#x27; mean all operations will be affected.  | [optional] 
**simulated_filesystem_parameters** | **str** | Specifies the parameters for a simulated null device filesystem. For example &#x60;2-2:2-2:0-1&#x60; will generate a filesystem tree which has 2 directories (&#x60;0&#x60; and &#x60;1&#x60;) and 2 files (&#x60;2&#x60; and &#x60;3&#x60;) in the root of the filesystem, each of these directories will have 2 subdirectories (&#x60;0&#x60; and &#x60;1&#x60;) and 2 files (&#x60;2&#x60; and &#x60;3&#x60;) and each of these subdirectories has only a single file (&#x60;0&#x60;). In order to specify the size of generated files, a size in bytes needs to be added as the last component of the parameter specification, for example &#x60;2-2:2-2:0-1:1048576&#x60;. Default empty string disables the simulated filesystem feature.  | [optional] 
**simulated_filesystem_grow_speed** | **float** | Determines the simulated filesystem grow rate. Default 0.0 value will cause all the files and directories defined by the &#x60;simulatedFilesystemParameters&#x60; specification to be visible immediately. For example value of 0.01 will increase the number of the visible filesystem entries by 1 file per 100 seconds, while 100.0 will increase it by 100 files per second.  | [optional] 
**enable_data_verification** | **bool** | Enables data verification for &#x60;read&#x60; and &#x60;write&#x60; operations. Read operations will always return a predictable pattern of characters based on &#x60;offset&#x60; and &#x60;size&#x60;, and &#x60;write&#x60; operations will fail with I/O error, if the input data does not match the pattern at a given &#x60;offset&#x60;.  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

