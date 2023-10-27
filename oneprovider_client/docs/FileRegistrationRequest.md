# FileRegistrationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**space_id** | **str** | Id of the space in which the file will be registered - the space must be supported by the storage hosting the file (&#x60;storageId&#x60;). The space support must have &#x60;manual import mode&#x60;.  | [optional] 
**storage_id** | **str** | Id of the storage hosting the file - the storage must support the target space (&#x60;spaceId&#x60;). The storage must be configured as an &#x60;imported storage&#x60; with &#x60;canonical&#x60; path type.  | [optional] 
**storage_file_id** | **str** | Identifier of the file on storage, relevant for given storage backend:    * path on POSIX-compatible or canonical object storages, e.g. &#x60;/dir/file.txt&#x60;    * URL on HTTP based storages, e.g. &#x60;https://www.example.org/data/21/run123.tar&#x60;  | [optional] 
**destination_path** | **str** | An absolute path in space where file should be created. | [optional] 
**size** | **int** | Size of the file in bytes. If not passed, it will be acquired from storage. If storage does not support the &#x60;stat&#x60; operation or equivalent used for acquiring files metadata, registration will fail if this value is missing.  | [optional] 
**mode** | **str** | User defined POSIX file permissions in octal format. If not passed, it will be acquired from storage or default &#x60;\&quot;664\&quot;&#x60; mode will be used.  | [optional] 
**atime** | **int** | User defined last access timestamp (in seconds). If not passed, it will be acquired from storage or current timestamp will be used.  | [optional] 
**mtime** | **int** | User defined last modification timestamp (in seconds). If not passed, it will be acquired from storage or current timestamp will be used.  | [optional] 
**ctime** | **int** | User defined last attributes modification timestamp (in seconds). If not passed, it will be acquired from storage or current timestamp will be used.  | [optional] 
**uid** | **str** | User defined of the Id of the owner of this file on storage. If not passed, it will be acquired from storage or &#x60;0&#x60; will be used. This value will be mapped, using LUMA DB, to acquire Onedata user Id of the file owner.  | [optional] 
**gid** | **str** | User defined Id of the group owner of this file on storage. If not passed, it will be acquired from storage or &#x60;0&#x60; will be used. This value will be used as display GID in &#x60;getattr&#x60; operation.  | [optional] 
**xattrs** | **dict(str, str)** | Map with extended attributes key-value pairs which will be attached to newly created file. | [optional] 
**json** | **dict(str, str)** | Map with custom JSON metadata which will be attached to newly created file. | [optional] 
**rdf** | **str** | Base64 encoded RDF metadata which will be attached to newly created file. | [optional] 
**auto_detect_attributes** | **bool** | Flag which determines whether additional &#x60;stat&#x60; operation (or equivalent) should be performed on the storage to automatically detect file attributes - they will be used if not provided explicitly in the request. The detection also ensures that the file exists - it is performed if the flag is set to &#x60;true&#x60;, even if all attributes are provided. If this flag is set to &#x60;false&#x60;, default attributes are used if not provided explicitly. The only exception is the &#x60;size&#x60; attribute, which is mandatory. The registration request will fail if &#x60;autoDetectAttributes&#x60; is set to &#x60;false&#x60; and &#x60;size&#x60; is not provided. It is possible to register a file that does not exist on storage if &#x60;autoDetectAttributes&#x60; is set to &#x60;false&#x60;. Such file will be visible in Onedata but not accessible.  | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

