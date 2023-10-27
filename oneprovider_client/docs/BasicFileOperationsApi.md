# oneprovider_client.BasicFileOperationsApi

All URIs are relative to */api/v3/oneprovider*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file**](BasicFileOperationsApi.md#create_file) | **POST** /data/{id}/children | Create file in directory
[**create_file_at_path**](BasicFileOperationsApi.md#create_file_at_path) | **PUT** /data/{id}/path/{path} | Create file at path
[**download_file_content**](BasicFileOperationsApi.md#download_file_content) | **GET** /data/{id}/content | Download file content
[**download_file_content_by_path**](BasicFileOperationsApi.md#download_file_content_by_path) | **GET** /data/{id}/path/{path} | Download file content by path
[**get_attrs**](BasicFileOperationsApi.md#get_attrs) | **GET** /data/{id} | Get file attributes
[**get_file_hardlinks**](BasicFileOperationsApi.md#get_file_hardlinks) | **GET** /data/{id}/hardlinks | Get file hard links
[**get_symlink_value**](BasicFileOperationsApi.md#get_symlink_value) | **GET** /data/{id}/symlink_value | Get symbolic link value
[**list_children**](BasicFileOperationsApi.md#list_children) | **GET** /data/{id}/children | List directory files and subdirectories
[**list_files_recursively**](BasicFileOperationsApi.md#list_files_recursively) | **GET** /data/{id}/files | List files recursively
[**remove_file**](BasicFileOperationsApi.md#remove_file) | **DELETE** /data/{id} | Remove file
[**remove_file_at_path**](BasicFileOperationsApi.md#remove_file_at_path) | **DELETE** /data/{id}/path/{path} | Remove file at path
[**set_attr**](BasicFileOperationsApi.md#set_attr) | **PUT** /data/{id} | Set file attribute
[**test_for_hardlink_between_files**](BasicFileOperationsApi.md#test_for_hardlink_between_files) | **GET** /data/{id}/hardlinks/{hid} | Test for hard link between files
[**update_file_content**](BasicFileOperationsApi.md#update_file_content) | **PUT** /data/{id}/content | Update file content

# **create_file**
> InlineResponse201 create_file(name, id, body=body, type=type, mode=mode, offset=offset, target_file_id=target_file_id, target_file_path=target_file_path)

Create file in directory

Creates a file in the directory specified by [$PARENT_ID](#operation/lookup_file_id).  If the file already exists, the operation fails with an error.  The file type can be of: - `REG` (regular file) - in this case, **the data sent in request body (if any) is saved as file content**. - `DIR` (directory). - `LNK` (hard link) - requires that `target_file_id` pointing to a regular file is specified. - `SYMLNK` (symbolic link) - requires that `target_file_path` is specified. When creating symbolic link with absolute path starting from specific space it is necessary to do so by replacing `/$SPACE_NAME/` in path by special prefix in the form `<__onedata_space_id:$SPACE_ID>/` (where $SPACE_ID is actual space id)  ***Example cURL requests***  **Create file** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$PARENT_ID/children?name=$NAME\" -H \"Content-Type: application/octet-stream\" -d \"@file.dat\"  {    \"fileId\": \"094576776E667431723230677767776C6B497031394E445F6E3868677873...\" } ```  **Create directory** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$PARENT_ID/children?name=$NAME&type=DIR\"  {    \"fileId\": \"000000006CB6637368617265477569642333396432363661656463656266...\" } ```  **Create hard link** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$PARENT_ID/children?name=$NAME&type=LNK&target_file_id=$TARGET_FILE_ID\"  {    \"fileId\": \"000000184465677569642373706163655F73706163653123737061636531...\" } ```  **Create symbolic link** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$PARENT_ID/children?name=$NAME&type=SYMLNK&target_file_path=$TARGET_FILE_PATH\"  {    \"fileId\": \"00989AB98890037368617265477569642333396432363661656463656266...\" } ```  See also [Create file at path](#operation/create_file_at_path). 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.BasicFileOperationsApi(oneprovider_client.ApiClient(configuration))
name = 'name_example' # str | Name of the file.
id = 'id_example' # str | Id of the parent directory.
body = oneprovider_client.Object() # Object | File content to be written at specified offset (relevant only if `type == "REG"`). (optional)
type = 'REG' # str | Type of the file. (optional) (default to REG)
mode = 56 # int | POSIX file permissions in decimal format. (optional)
offset = 0 # int | Offset at which the data sent as request body will be written to the file (relevant only if `type == \"REG\"`).  (optional) (default to 0)
target_file_id = 'target_file_id_example' # str | The Id of the file to which the hard link should point (relevant only if `type == \"LNK\"`).  (optional)
target_file_path = 'target_file_path_example' # str | Path to which the symbolic link should point (relevant only if `type == \"SYMLNK\"`).  (optional)

try:
    # Create file in directory
    api_response = api_instance.create_file(name, id, body=body, type=type, mode=mode, offset=offset, target_file_id=target_file_id, target_file_path=target_file_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasicFileOperationsApi->create_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the file. | 
 **id** | **str**| Id of the parent directory. | 
 **body** | **Object**| File content to be written at specified offset (relevant only if &#x60;type &#x3D;&#x3D; &quot;REG&quot;&#x60;). | [optional] 
 **type** | **str**| Type of the file. | [optional] [default to REG]
 **mode** | **int**| POSIX file permissions in decimal format. | [optional] 
 **offset** | **int**| Offset at which the data sent as request body will be written to the file (relevant only if &#x60;type &#x3D;&#x3D; \&quot;REG\&quot;&#x60;).  | [optional] [default to 0]
 **target_file_id** | **str**| The Id of the file to which the hard link should point (relevant only if &#x60;type &#x3D;&#x3D; \&quot;LNK\&quot;&#x60;).  | [optional] 
 **target_file_path** | **str**| Path to which the symbolic link should point (relevant only if &#x60;type &#x3D;&#x3D; \&quot;SYMLNK\&quot;&#x60;).  | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file_at_path**
> InlineResponse201 create_file_at_path(id, path, body=body, type=type, mode=mode, create_parents=create_parents, offset=offset, target_file_id=target_file_id, target_file_path=target_file_path)

Create file at path

Creates a file at path specified in the URL, relative to the base directory given in the `id` parameter (see the parameter description for details). If the parent path does not exist and `create_parents` flag is set to true, the operation will attempt to create intermediate parent directories.  If the file already exists, the operation fails with an error.  The file type can be of: - `REG` (regular file) - in this case, the **data sent in request body (if any) is saved as file content**. - `DIR` (directory). - `LNK` (hard link) - requires that `target_file_id` pointing to a regular file is specified. - `SYMLNK` (symbolic link) - requires that `target_file_path` is specified. When creating symbolic link with absolute path starting from specific space it is necessary to do so by replacing `/$SPACE_NAME/` in path by special prefix in the form `<__onedata_space_id:$SPACE_ID>/` (where $SPACE_ID is actual space id)  ***Example cURL requests***  **Create file** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/dir1/$NAME\" -H \"Content-Type: application/octet-stream\" -d \"@file.dat\"  {    \"fileId\": \"094576776E667431723230677767776C6B497031394E445F6E3868677873...\" } ```  **Create directory** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/$NAME?type=DIR\"  {    \"fileId\": \"000000006CB6637368617265477569642333396432363661656463656266...\" } ```  **Create hard link** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/$NAME&type=LNK&target_file_id=$TARGET_FILE_ID\"  {    \"fileId\": \"000000184465677569642373706163655F73706163653123737061636531...\" } ```  **Create symbolic link** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/$NAME&type=SYMLNK&target_file_path=$TARGET_FILE_PATH\"  {    \"fileId\": \"00989AB98890037368617265477569642333396432363661656463656266...\" } ```  See also [Create file in directory](#operation/create_file). 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.BasicFileOperationsApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | ID of the base directory, relative to which the path remainder will be resolved. It can be a **Space Id** (in which case the space root directory is taken), or a **File Id** of any existing directory (including the space root directory). See [Data](#section/Overview/Data-management-basics) section for more information. 
path = 'path_example' # str | Path relative to the base directory (specified in the id parameter).
body = oneprovider_client.Object() # Object | File content to be written at specified offset (relevant only if `type == "REG"`). (optional)
type = 'REG' # str | Type of the file. (optional) (default to REG)
mode = 56 # int | POSIX file permissions in decimal format. (optional)
create_parents = false # bool | Allows to create unexistient directories specified in path parameter. (optional) (default to false)
offset = 0 # int | Offset at which the data sent as request body will be written to the file (relevant only if `type == \"REG\"`).  (optional) (default to 0)
target_file_id = 'target_file_id_example' # str | The Id of the file to which the hard link should point (relevant only if `type == \"LNK\"`).  (optional)
target_file_path = 'target_file_path_example' # str | Path to which the symbolic link should point (relevant only if `type == \"SYMLNK\"`).  (optional)

try:
    # Create file at path
    api_response = api_instance.create_file_at_path(id, path, body=body, type=type, mode=mode, create_parents=create_parents, offset=offset, target_file_id=target_file_id, target_file_path=target_file_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasicFileOperationsApi->create_file_at_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the base directory, relative to which the path remainder will be resolved. It can be a **Space Id** (in which case the space root directory is taken), or a **File Id** of any existing directory (including the space root directory). See [Data](#section/Overview/Data-management-basics) section for more information.  | 
 **path** | **str**| Path relative to the base directory (specified in the id parameter). | 
 **body** | **Object**| File content to be written at specified offset (relevant only if &#x60;type &#x3D;&#x3D; &quot;REG&quot;&#x60;). | [optional] 
 **type** | **str**| Type of the file. | [optional] [default to REG]
 **mode** | **int**| POSIX file permissions in decimal format. | [optional] 
 **create_parents** | **bool**| Allows to create unexistient directories specified in path parameter. | [optional] [default to false]
 **offset** | **int**| Offset at which the data sent as request body will be written to the file (relevant only if &#x60;type &#x3D;&#x3D; \&quot;REG\&quot;&#x60;).  | [optional] [default to 0]
 **target_file_id** | **str**| The Id of the file to which the hard link should point (relevant only if &#x60;type &#x3D;&#x3D; \&quot;LNK\&quot;&#x60;).  | [optional] 
 **target_file_path** | **str**| Path to which the symbolic link should point (relevant only if &#x60;type &#x3D;&#x3D; \&quot;SYMLNK\&quot;&#x60;).  | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file_content**
> str download_file_content(id, follow_symlinks=follow_symlinks)

Download file content

Returns the content of a file or directory specified by [$FILE_ID](#operation/lookup_file_id).  If $FILE_ID is a regular file, returns its binary content. Partial content download is also supported using [Range header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Range).  If $FILE_ID is a directory, returns a TAR archive with its contents. Any nested files or subdirectories to which the client does not have access (e.g. due to insufficient POSIX permissions or ACLs) are omitted in the resulting archive. Request for directory download results in a redirection URL (in Location header) that contains the ID of a temporary download session. The URL can be used to download the tarball, with support for resuming interrupted downloads using the Range header (where the range start is the number of already downloaded bytes and the range end is omitted).   ***Example cURL requests***  **Download entire file content** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/content\"  abcdefghijklmno ```  **Download only part of the file content** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/content\" \\ -H \"Range: bytes=5-8\"  fghi ```  **Download a directory as tar archive** ```bash curl -sD - -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$DIR_ID/content\" | grep location  location: https://$PROVIDER_HOST/download/$DOWNLOAD_ID ```  ``` curl https://$PROVIDER_HOST/download/$DOWNLOAD_ID > directory.tar ```  **Download a directory as tar archive in a single request** ```bash curl -L -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$DIR_ID/content\" ```  **Resume download of a directory (previous download failed after 12345678 bytes)** ```bash curl -H \"Range: bytes=12345678-\" https://$PROVIDER_HOST/download/$DOWNLOAD_ID >> directory.tar ```  **Download a directory as tar archive in a single request without resolving symlinks** ```bash curl -L -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$DIR_ID/content?follow_symlinks=false\" ```  See also [Download file content by path](#operation/download_file_content_by_path). 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.BasicFileOperationsApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | Id of the file.
follow_symlinks = true # bool | Flag controlling whether symbolic links in requested download should be resolved. (optional) (default to true)

try:
    # Download file content
    api_response = api_instance.download_file_content(id, follow_symlinks=follow_symlinks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasicFileOperationsApi->download_file_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the file. | 
 **follow_symlinks** | **bool**| Flag controlling whether symbolic links in requested download should be resolved. | [optional] [default to true]

### Return type

**str**

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file_content_by_path**
> str download_file_content_by_path(id, path)

Download file content by path

Returns the content of a file or directory by path specified in the URL, relative to the base directory given in the `id` parameter (see the parameter description for details).  If requested file is a regular file, returns its binary content. Partial content download is also supported using [Range header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Range).  If requested file is a directory, returns a TAR archive with its contents. Any nested files or subdirectories to which the client does not have access (e.g. due to insufficient POSIX permissions or ACLs) are omitted in the resulting archive. Request for directory download results in a redirection URL (in Location header) that contains the ID of a temporary download session. The URL can be used to download the tarball, with support for resuming interrupted downloads using the Range header (where the range start is the number of already downloaded bytes and the range end is omitted).   ***Example cURL requests***  **Download entire file content** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/dir1/dir2/file\" \\  abcdefghijklmno ```  **Download only part of the file content** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/dir1/dir2/file\" \\ -H \"Range: bytes=5-8\"  fghi ```  **Download a directory as tar archive** ```bash curl -sD - -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/dir1\" | grep location  location: https://$PROVIDER_HOST/download/$DOWNLOAD_ID ```  ``` curl https://$PROVIDER_HOST/download/$DOWNLOAD_ID > directory.tar ```  **Download a directory as tar archive in a single request** ```bash curl -L -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/dir1\" ```  **Resume download of a directory (previous download failed after 12345678 bytes)** ```bash curl -H \"Range: bytes=12345678-\" https://$PROVIDER_HOST/download/$DOWNLOAD_ID >> directory.tar ```  **Download a directory as tar archive in a single request without resolving symlinks** ```bash curl -L -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/dir1?follow_symlinks=false\" ```  See also [Download file content by ID](#operation/download_file_content). 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.BasicFileOperationsApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | ID of the base directory, relative to which the path remainder will be resolved. It can be a **Space Id** (in which case the space root directory is taken), or a **File Id** of any existing directory (including the space root directory). See [Data](#section/Overview/Data-management-basics) section for more information. 
path = 'path_example' # str | Path relative to the base directory (specified in the id parameter).

try:
    # Download file content by path
    api_response = api_instance.download_file_content_by_path(id, path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasicFileOperationsApi->download_file_content_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the base directory, relative to which the path remainder will be resolved. It can be a **Space Id** (in which case the space root directory is taken), or a **File Id** of any existing directory (including the space root directory). See [Data](#section/Overview/Data-management-basics) section for more information.  | 
 **path** | **str**| Path relative to the base directory (specified in the id parameter). | 

### Return type

**str**

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attrs**
> FileAttributes get_attrs(id, attribute=attribute)

Get file attributes

This method returns either all or only selected basic attributes associated with file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Get file size** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID?attribute=size&attribute=name\"  {     \"name\": \"File1.txt\"     \"size\": 100 } ``` 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.BasicFileOperationsApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | File, directory or space Id
attribute = 'attribute_example' # str | Name of attribute to query for. Can be provided multiple times.  When accessing file via share mode following attributes are unavailable:  `owner_id`, `storage_group_id`, `storage_user_id`, `provider_id`, `hardlinks_count`  (optional)

try:
    # Get file attributes
    api_response = api_instance.get_attrs(id, attribute=attribute)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasicFileOperationsApi->get_attrs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File, directory or space Id | 
 **attribute** | **str**| Name of attribute to query for. Can be provided multiple times.  When accessing file via share mode following attributes are unavailable:  &#x60;owner_id&#x60;, &#x60;storage_group_id&#x60;, &#x60;storage_user_id&#x60;, &#x60;provider_id&#x60;, &#x60;hardlinks_count&#x60;  | [optional] 

### Return type

[**FileAttributes**](FileAttributes.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_hardlinks**
> list[str] get_file_hardlinks(id)

Get file hard links

Returns Ids of all hard links (including this one) associated with file specified by [$FILE_ID](#operation/lookup_file_id).  **Get file hard links** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/hardlinks\"  [     \"094576776E667431723230677767776C6B497031394E445F6E3868677873...\",     \"000000006CB6637368617265477569642333396432363661656463656266...\" ] ``` 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.BasicFileOperationsApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | File Id.

try:
    # Get file hard links
    api_response = api_instance.get_file_hardlinks(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasicFileOperationsApi->get_file_hardlinks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File Id. | 

### Return type

**list[str]**

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_symlink_value**
> str get_symlink_value(id)

Get symbolic link value

Returns the value of symbolic link specified by [$FILE_ID](#operation/lookup_file_id) (the path to where the link is pointing).  **Get symbolic link value** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/symlink_value\"  ../../Dir1/File1 ``` 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.BasicFileOperationsApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | Id of the symbolic link.

try:
    # Get symbolic link value
    api_response = api_instance.get_symlink_value(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasicFileOperationsApi->get_symlink_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the symbolic link. | 

### Return type

**str**

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_children**
> DirectoryChildren list_children(id, limit=limit, token=token, attribute=attribute, index=index, tune_for_large_continuous_listing=tune_for_large_continuous_listing)

List directory files and subdirectories

Returns the list of directory files and subdirectories for directory specified by [$DIR_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Get files in space subdirectory** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$DIR_ID/children?attribute=size&attribute=name&limit=2\"  {     \"children\": [         {              \"name\": File1.txt             \"size\": 1024         },         {              \"name\": File2.txt             \"size\": 16384         }     ],     \"isLast\": false,     \"nextPageToken\": \"g2gDZAAKbGlua190b2tlbmgCZAAMY2FjaGVkX3Rva2VuWgADY...\" } ``` 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.BasicFileOperationsApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | Id of the directory.
limit = 1000 # int | Allows specifying maximum number of files that should be returned. If there are more files, they can be retrieved using `token` query parameter.  (optional) (default to 1000)
token = 'null' # str | Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding `nextPageToken`. Cannot be provided alongside the `index` or `tune_for_large_continuous_listing` parameters.  (optional) (default to null)
attribute = 'attribute_example' # str | Name of attribute to be returned for each entry. Can be provided multiple times. When accessing a file via share mode, the following attributes are unavailable: `owner_id`, `storage_group_id`, `storage_user_id`, `provider_id`, `hardlinks_count`. If not provided, default attributes of `file_id` and `name` will be returned.  (optional)
index = 'index_example' # str | Determines the starting point for listing - it will be started from given file name (inclusively). Cannot be provided alongside the `token` parameter.  (optional)
tune_for_large_continuous_listing = false # bool | This option increases performance of listing large directories (with thousands of files) when using subsequent calls with paging tokens.<br/> **CAUTION!!** When enabled, there is no guarantee that changes in the file tree performed after the start of listing will be included. Therefore it shouldn't be used when the listing result is expected to be up to date with the state of the file tree at the moment of listing. It should be avoided if the interval between subsequent listings is longer than 10 seconds, otherwise the listing performance will be much worse.<br/> Overusing this option may cause a significant load on the Oneprovider.<br/> Cannot be provided alongside the `token` parameter.  (optional) (default to false)

try:
    # List directory files and subdirectories
    api_response = api_instance.list_children(id, limit=limit, token=token, attribute=attribute, index=index, tune_for_large_continuous_listing=tune_for_large_continuous_listing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasicFileOperationsApi->list_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the directory. | 
 **limit** | **int**| Allows specifying maximum number of files that should be returned. If there are more files, they can be retrieved using &#x60;token&#x60; query parameter.  | [optional] [default to 1000]
 **token** | **str**| Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding &#x60;nextPageToken&#x60;. Cannot be provided alongside the &#x60;index&#x60; or &#x60;tune_for_large_continuous_listing&#x60; parameters.  | [optional] [default to null]
 **attribute** | **str**| Name of attribute to be returned for each entry. Can be provided multiple times. When accessing a file via share mode, the following attributes are unavailable: &#x60;owner_id&#x60;, &#x60;storage_group_id&#x60;, &#x60;storage_user_id&#x60;, &#x60;provider_id&#x60;, &#x60;hardlinks_count&#x60;. If not provided, default attributes of &#x60;file_id&#x60; and &#x60;name&#x60; will be returned.  | [optional] 
 **index** | **str**| Determines the starting point for listing - it will be started from given file name (inclusively). Cannot be provided alongside the &#x60;token&#x60; parameter.  | [optional] 
 **tune_for_large_continuous_listing** | **bool**| This option increases performance of listing large directories (with thousands of files) when using subsequent calls with paging tokens.&lt;br/&gt; **CAUTION!!** When enabled, there is no guarantee that changes in the file tree performed after the start of listing will be included. Therefore it shouldn&#x27;t be used when the listing result is expected to be up to date with the state of the file tree at the moment of listing. It should be avoided if the interval between subsequent listings is longer than 10 seconds, otherwise the listing performance will be much worse.&lt;br/&gt; Overusing this option may cause a significant load on the Oneprovider.&lt;br/&gt; Cannot be provided alongside the &#x60;token&#x60; parameter.  | [optional] [default to false]

### Return type

[**DirectoryChildren**](DirectoryChildren.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_files_recursively**
> RecursiveFileList list_files_recursively(id, limit=limit, token=token, start_after=start_after, prefix=prefix, attribute=attribute)

List files recursively

Recursively lists non-directory files (i.e regular files, symbolic links and hardlinks) in directory specified by [$DIR_ID](#operation/lookup_file_id) (listing root). Files are listed in lexicographical order by their paths, which are relative to the listing root directory. If there is no access to specified directory, its own relative path (`\".\"`) will be included in the `inaccessiblePaths` field and the listing result (i.e. `files` field) will be empty.  ***Example cURL requests***  **List files recursively** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$DIR_ID/files?start_after=ParentDirName/Dir1\"  {     \"files\": [         {             \"file_id\": \"FILE_ID1\",             \"path\": \"ParentDirName/Dir2\"         },         {             \"file_id\": \"FILE_ID2\",             \"path\": \"ParentDirName/File1.txt\"         },     ],     \"inaccessiblePaths\": [         \"ParentDirName/Dir3\"     ],     \"isLast\": false,     \"nextPageToken\": \"$PAGING_TOKEN\" } ``` 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.BasicFileOperationsApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | Id of the directory.
limit = 1000 # int | Specifies the maximum number of entries that can be returned in one result batch. If there are more files, they can be retrieved using options that specify a custom starting point.  (optional) (default to 1000)
token = 'token_example' # str | Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding `nextPageToken`. Cannot be provided alongside the `start_after` parameter.  (optional)
start_after = 'start_after_example' # str | Determines the starting point for listing - it will be started from the first file path lexicographically larger than the provided path.  (optional)
prefix = 'prefix_example' # str | Only files with paths that begin with this value will be listed.  (optional)
attribute = 'attribute_example' # str | Name of attribute to be returned for each entry. Can be provided multiple times. When accessing a file via share mode, the following attributes are unavailable: `owner_id`, `storage_group_id`, `storage_user_id`, `provider_id`, `hardlinks_count`. If not provided, default attributes of `file_id` and `path` will be returned.  (optional)

try:
    # List files recursively
    api_response = api_instance.list_files_recursively(id, limit=limit, token=token, start_after=start_after, prefix=prefix, attribute=attribute)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasicFileOperationsApi->list_files_recursively: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the directory. | 
 **limit** | **int**| Specifies the maximum number of entries that can be returned in one result batch. If there are more files, they can be retrieved using options that specify a custom starting point.  | [optional] [default to 1000]
 **token** | **str**| Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding &#x60;nextPageToken&#x60;. Cannot be provided alongside the &#x60;start_after&#x60; parameter.  | [optional] 
 **start_after** | **str**| Determines the starting point for listing - it will be started from the first file path lexicographically larger than the provided path.  | [optional] 
 **prefix** | **str**| Only files with paths that begin with this value will be listed.  | [optional] 
 **attribute** | **str**| Name of attribute to be returned for each entry. Can be provided multiple times. When accessing a file via share mode, the following attributes are unavailable: &#x60;owner_id&#x60;, &#x60;storage_group_id&#x60;, &#x60;storage_user_id&#x60;, &#x60;provider_id&#x60;, &#x60;hardlinks_count&#x60;. If not provided, default attributes of &#x60;file_id&#x60; and &#x60;path&#x60; will be returned.  | [optional] 

### Return type

[**RecursiveFileList**](RecursiveFileList.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_file**
> remove_file(id)

Remove file

Removes file specified by [$FILE_ID](#operation/lookup_file_id). In case of a directory, all its children are recursively removed - note that the operation will fail part-way if the client does not have permissions to remove some of the nested files/directories.  ***Example cURL requests***  **Remove specific file** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID\" ``` See also [Remove file at path](#operation/remove_file_at_path). 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.BasicFileOperationsApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | File or directory Id

try:
    # Remove file
    api_instance.remove_file(id)
except ApiException as e:
    print("Exception when calling BasicFileOperationsApi->remove_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File or directory Id | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_file_at_path**
> remove_file_at_path(id, path)

Remove file at path

Removes file by path specified in the URL, relative to the base directory given in the `id` parameter (see the parameter description for details).  In case of a directory, all its children are recursively removed - note that the operation will fail part-way if the client does not have permissions to remove some of the nested files/directories.  ***Example cURL requests***  **Remove specific file** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/dir1/file.txt\" ```  See also [Remove file by ID](#operation/remove_file). 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.BasicFileOperationsApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | ID of the base directory, relative to which the path remainder will be resolved. It can be a **Space Id** (in which case the space root directory is taken), or a **File Id** of any existing directory (including the space root directory). See [Data](#section/Overview/Data-management-basics) section for more information. 
path = 'path_example' # str | Path relative to the base directory (specified in the id parameter).

try:
    # Remove file at path
    api_instance.remove_file_at_path(id, path)
except ApiException as e:
    print("Exception when calling BasicFileOperationsApi->remove_file_at_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the base directory, relative to which the path remainder will be resolved. It can be a **Space Id** (in which case the space root directory is taken), or a **File Id** of any existing directory (including the space root directory). See [Data](#section/Overview/Data-management-basics) section for more information.  | 
 **path** | **str**| Path relative to the base directory (specified in the id parameter). | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_attr**
> set_attr(id, body=body)

Set file attribute

This method allows to set a value of a regular file attribute for a file specified by [$FILE_ID](#operation/lookup_file_id).  Currently only POSIX mode can be changed by sending: ``` { \"mode\": \"0777\" } ``` where the POSIX mode is specified in octal notation.  ***Example cURL requests***  **Set file POSIX mode** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X PUT \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID\" \\ -H 'Content-Type: application/json' -d '{ \"mode\": \"0777\" }' ``` 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.BasicFileOperationsApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | File, directory or space Id
body = NULL # dict(str, str) | Attribute name and value. (optional)

try:
    # Set file attribute
    api_instance.set_attr(id, body=body)
except ApiException as e:
    print("Exception when calling BasicFileOperationsApi->set_attr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File, directory or space Id | 
 **body** | [**dict(str, str)**](dict.md)| Attribute name and value. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_for_hardlink_between_files**
> test_for_hardlink_between_files(id, hid)

Test for hard link between files

Checks whether one file is a hard link to the other one. Both files are specified by [$FILE_ID](#operation/lookup_file_id). The relation is symmetric; the order of the files in the URL does not matter.  **Test for hard link between files** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID1/hardlinks/$FILE_ID2\"  # return code = 0 (HTTP code = 204) -> true # return code != 0 (HTTP code = 404) -> false ``` 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.BasicFileOperationsApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | First File Id.
hid = 'hid_example' # str | Second File Id.

try:
    # Test for hard link between files
    api_instance.test_for_hardlink_between_files(id, hid)
except ApiException as e:
    print("Exception when calling BasicFileOperationsApi->test_for_hardlink_between_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| First File Id. | 
 **hid** | **str**| Second File Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file_content**
> update_file_content(id, body=body, offset=offset)

Update file content

Updates content of file specified by [$FILE_ID](#operation/lookup_file_id).  The file must exist beforehand, otherwise the operation fails with an error.  The `offset` query parameter can be used to start writing from a certain byte in the file, in such case the file is NOT truncated (bytes beyond the overwritten fragment will be preserved). If no `offset` query is given, the file is truncated  and the previous file content is completely overwritten.  ***Example cURL requests***  **Update file content starting from specified offset:** ```bash # originally, the file content is  \"abcdefghijklmno\"  curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/content?offset=4\" \\ -H \"Content-Type: application/octet-stream\" -d \"WXYZ\"  # upon success, the file content is \"abcdWXYZijklmno\" ``` 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.BasicFileOperationsApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | Id of the file.
body = oneprovider_client.Object() # Object | File content to be written at specified offset. (optional)
offset = 0 # int | Offset at which the data sent as request body will be written to the file. If not specified, the file will be completely overwritten.  (optional) (default to 0)

try:
    # Update file content
    api_instance.update_file_content(id, body=body, offset=offset)
except ApiException as e:
    print("Exception when calling BasicFileOperationsApi->update_file_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the file. | 
 **body** | **Object**| File content to be written at specified offset. | [optional] 
 **offset** | **int**| Offset at which the data sent as request body will be written to the file. If not specified, the file will be completely overwritten.  | [optional] [default to 0]

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

