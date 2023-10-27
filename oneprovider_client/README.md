# oneprovider_client
# Overview  
This is the RESTful API definition of Oneprovider component of Onedata data management system [onedata.org](http://onedata.org).  

> This API is defined using [Swagger](http://swagger.io/), the JSON specification can be used to automatically generate > client libraries - [swagger.json](../../../swagger/oneprovider/swagger.json).  
 
All paths below are relative to a common Oneprovider basepath which is `/api/v3/oneprovider`, thus a complete example query for 'mode' file attributes would be: 
``` 
https://ONEPROVIDER_HOSTNAME/api/v3/oneprovider/data/$FILE_ID?attribute=mode 
```
Please note that currently the default port for Oneprovider instances is `443`.  
In addition to REST API, Oneprovider also provides support for [CDMI](http://onedata.org/#/home/documentation/doc/advanced/cdmi.html) protocol.   

## Authentication 
To use the APIs, the REST client must authenticate with the Oneprovider service and present a proof of authorization to perform a specific operation. This is done using access tokens, which can be generated using the Onedata GUI or Onezone's REST API.  
The token is passed in the request header like this: 
``` 
X-Auth-Token: MIIFrzCCA5egAwIBAgIBEzANBgkqhkiG9w0BAQUFADBcMQswCQYDVQQGEwJQTDET... 
```  
The authorization to perform a specific operation depends on the authenticated user's privileges in the corresponding space, file level permissions (posix, ACL) and caveats (restrictions) inscribed in the provided access token.   

## Data management basics 
The Onedata system organizes all user data into logical containers called spaces. <!--- TODO VFS-7218 uncomment when the new docs are deployed --> <!--- For more information, please refer to the [documentation](https://onedata.org/#/home/documentation). -->  
Files and directories in Onedata can be globally identified using unique File Ids or logical paths. Whenever possible, it is recommended to use File Ids, due to better performance and no need for escaping or encoding.  
### File path 
All logical paths in Onedata use the slash (`/`) delimiter and must start with a space name: 
```lang-none 
/CMS 1/file.txt /MyExperiment/directory/subdirectory/image.jpg 
```  
When referencing files by path in the REST API, make sure to urlencode the path in the URL: 
```bash 
{...}/CMS%201/file.txt 
```  

### File Id  
File Id is a unique, global identifier associated with a file or directory and can be used universally in the REST and CDMI APIs. There are several ways to find out the File Id of given file or directory: <!---  @TODO VFS-7218 remove redundant information and provide a link to the new docs -->  
**Web GUI** - click on Information in the file/directory context menu and look for File Id.  
**REST API** - use the File Id resolution endpoint. Below example returns the File Id of `/CMS 1/file.txt`, where `CMS 1` is the space name: 
```bash
curl -H \"X-Auth-Token: ${ACCESS_TOKEN}\" \\ -X POST \"https://${ONEPROVIDER_DOMAIN}/api/v3/oneprovider/lookup-file-id/CMS%201/file.txt\" {     \"fileId\": \"094576776E667431723230677767776C6B497031394E445F6E3868677873...\" } 
```  

### Space Id  
Space Id is a unique, global identifier associated with a space and can be used universally in the REST APIs. In order to find out the Space Id:  
**Web GUI** - click on Information in the file/directory context menu and look for Space Id.  
**REST API** - use the [Get all user spaces](#operation/get_all_spaces) endpoint.  The Space Id can be used interchangeably with the space root directory's File Id in the path-based enpoints.  
**Remove specific file relative to the space root** 
```bash 
curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_ID/path/dir1/file.txt\" # is equivalent to curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_ROOT_FILE_ID/path/dir1/file.txt\" 
``` 
**Remove specific file relative to any parent directory** 
```bash 
curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$PARENT_FILE_ID/path/dir1/file.txt\" 
``` 
## API structure  
The API is divided into the following sections:  

### Space management 
These methods provide means for getting basic information about spaces directly from the Oneprovider service, but also allows to define database views.  
### File access and management The API provides capabilities for:
- browsing files in spaces and directories,  
- creating and deleting files as well as updating their content  
- querying for file attributes, such as 'mode' file permissions and updating them,  
- managing custom file metadata (xattrs, JSON, RDF),   
- manual registration of files for imported storages.
More information can be found [here](#section/Overview/Data-management-basics).  

### Replica and QoS management 
These methods allow viewing file replica distribution, requesting file replication (transfers) between Oneproviders, viewing ongoing and historical transfers data, as well as managing QoS requirements that trigger automatic replication according to the QoS rules.
### Share management 
Offers methods for creating, modyfying and deleting shares. Shares are files or directories that were made publicly available, so that they can be viewed by everyone through a public URL.  
### Dataset & archive management 
API for managing datasets - designated files or directories that are used to facilitate building collections of data meaningful for the users with additional features, such as write protection and archivisation mechanisms.  
### Automation Basic 
API for scheduling and viewing workflow executions.  
### Monitoring 
The API provides means for subscribing (through HTTP long-polling technique) for file related events such as reads, writes or deletes which are returned as complete file metadata records with sequence numbers representing their current version.  
### Service information 
Publicly available, basic configuration of the Oneprovider service.  Detailed examples of API usage are available in the documentation of each operation. 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 21.02.3
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [https://onedata.org/support](https://onedata.org/support)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import oneprovider_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import oneprovider_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = oneprovider_client.ArchiveApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | File Id.

try:
    # Cancel an archive recall
    api_instance.cancel_archive_recall(id)
except ApiException as e:
    print("Exception when calling ArchiveApi->cancel_archive_recall: %s\n" % e)

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
api_instance = oneprovider_client.ArchiveApi(oneprovider_client.ApiClient(configuration))
body = oneprovider_client.ArchiveCreateRequest() # ArchiveCreateRequest | Dataset properties.

try:
    # Create archive from a dataset
    api_response = api_instance.create_archive(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->create_archive: %s\n" % e)

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
api_instance = oneprovider_client.ArchiveApi(oneprovider_client.ApiClient(configuration))
aid = 'aid_example' # str | Id of a specific archive to be deleted.
body = oneprovider_client.ArchiveDeleteRequest() # ArchiveDeleteRequest | Parameters for initializing purging of an archive. (optional)

try:
    # Delete archive
    api_instance.delete_archive(aid, body=body)
except ApiException as e:
    print("Exception when calling ArchiveApi->delete_archive: %s\n" % e)

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
api_instance = oneprovider_client.ArchiveApi(oneprovider_client.ApiClient(configuration))
aid = 'aid_example' # str | Archive Id

try:
    # Get archive information
    api_response = api_instance.get_archive(aid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->get_archive: %s\n" % e)

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
api_instance = oneprovider_client.ArchiveApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | File Id.

try:
    # Get details of an archive recall
    api_response = api_instance.get_archive_recall_details(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->get_archive_recall_details: %s\n" % e)

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
api_instance = oneprovider_client.ArchiveApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | File Id.

try:
    # Get progress of an archive recall
    api_response = api_instance.get_archive_recall_progress(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->get_archive_recall_progress: %s\n" % e)

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
api_instance = oneprovider_client.ArchiveApi(oneprovider_client.ApiClient(configuration))
did = 'did_example' # str | Dataset Id
limit = 1000 # int | Allows specifying maximum number of entries that should be returned. If there are more archives, they can be retrieved using `offset` or `token` query parameters.  (optional) (default to 1000)
offset = 0 # int | Offset determining beginning of the list of archives returned in the response. Expressed in number of entries, further adjusts the starting point of listing indicated by `token` parameter. The value can be negative, in such case entries preceding the starting point will be returned.  (optional) (default to 0)
token = 'null' # str | Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding `nextPageToken`.  (optional) (default to null)

try:
    # List archives of a dataset
    api_response = api_instance.list_dataset_archives(did, limit=limit, offset=offset, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->list_dataset_archives: %s\n" % e)

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
api_instance = oneprovider_client.ArchiveApi(oneprovider_client.ApiClient(configuration))
body = oneprovider_client.ArchiveRecallRequest() # ArchiveRecallRequest | Parameters for initializing recall of an archive.
aid = 'aid_example' # str | Id of a specific archive to be recalled.

try:
    # Recall archive
    api_response = api_instance.recall_archive(body, aid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->recall_archive: %s\n" % e)

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
api_instance = oneprovider_client.ArchiveApi(oneprovider_client.ApiClient(configuration))
body = oneprovider_client.ArchiveUpdateRequest() # ArchiveUpdateRequest | Archive properties
aid = 'aid_example' # str | Archive Id

try:
    # Update archive
    api_instance.update_archive(body, aid)
except ApiException as e:
    print("Exception when calling ArchiveApi->update_archive: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */api/v3/oneprovider*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ArchiveApi* | [**cancel_archive_recall**](docs/ArchiveApi.md#cancel_archive_recall) | **POST** /data/{id}/recall/cancel | Cancel an archive recall
*ArchiveApi* | [**create_archive**](docs/ArchiveApi.md#create_archive) | **POST** /archives | Create archive from a dataset
*ArchiveApi* | [**delete_archive**](docs/ArchiveApi.md#delete_archive) | **POST** /archives/{aid}/delete | Delete archive
*ArchiveApi* | [**get_archive**](docs/ArchiveApi.md#get_archive) | **GET** /archives/{aid} | Get archive information
*ArchiveApi* | [**get_archive_recall_details**](docs/ArchiveApi.md#get_archive_recall_details) | **GET** /data/{id}/recall/details | Get details of an archive recall
*ArchiveApi* | [**get_archive_recall_progress**](docs/ArchiveApi.md#get_archive_recall_progress) | **GET** /data/{id}/recall/progress | Get progress of an archive recall
*ArchiveApi* | [**list_dataset_archives**](docs/ArchiveApi.md#list_dataset_archives) | **GET** /datasets/{did}/archives | List archives of a dataset
*ArchiveApi* | [**recall_archive**](docs/ArchiveApi.md#recall_archive) | **POST** /archives/{aid}/recall | Recall archive
*ArchiveApi* | [**update_archive**](docs/ArchiveApi.md#update_archive) | **PATCH** /archives/{aid} | Update archive
*BasicFileOperationsApi* | [**create_file**](docs/BasicFileOperationsApi.md#create_file) | **POST** /data/{id}/children | Create file in directory
*BasicFileOperationsApi* | [**create_file_at_path**](docs/BasicFileOperationsApi.md#create_file_at_path) | **PUT** /data/{id}/path/{path} | Create file at path
*BasicFileOperationsApi* | [**download_file_content**](docs/BasicFileOperationsApi.md#download_file_content) | **GET** /data/{id}/content | Download file content
*BasicFileOperationsApi* | [**download_file_content_by_path**](docs/BasicFileOperationsApi.md#download_file_content_by_path) | **GET** /data/{id}/path/{path} | Download file content by path
*BasicFileOperationsApi* | [**get_attrs**](docs/BasicFileOperationsApi.md#get_attrs) | **GET** /data/{id} | Get file attributes
*BasicFileOperationsApi* | [**get_file_hardlinks**](docs/BasicFileOperationsApi.md#get_file_hardlinks) | **GET** /data/{id}/hardlinks | Get file hard links
*BasicFileOperationsApi* | [**get_symlink_value**](docs/BasicFileOperationsApi.md#get_symlink_value) | **GET** /data/{id}/symlink_value | Get symbolic link value
*BasicFileOperationsApi* | [**list_children**](docs/BasicFileOperationsApi.md#list_children) | **GET** /data/{id}/children | List directory files and subdirectories
*BasicFileOperationsApi* | [**list_files_recursively**](docs/BasicFileOperationsApi.md#list_files_recursively) | **GET** /data/{id}/files | List files recursively
*BasicFileOperationsApi* | [**remove_file**](docs/BasicFileOperationsApi.md#remove_file) | **DELETE** /data/{id} | Remove file
*BasicFileOperationsApi* | [**remove_file_at_path**](docs/BasicFileOperationsApi.md#remove_file_at_path) | **DELETE** /data/{id}/path/{path} | Remove file at path
*BasicFileOperationsApi* | [**set_attr**](docs/BasicFileOperationsApi.md#set_attr) | **PUT** /data/{id} | Set file attribute
*BasicFileOperationsApi* | [**test_for_hardlink_between_files**](docs/BasicFileOperationsApi.md#test_for_hardlink_between_files) | **GET** /data/{id}/hardlinks/{hid} | Test for hard link between files
*BasicFileOperationsApi* | [**update_file_content**](docs/BasicFileOperationsApi.md#update_file_content) | **PUT** /data/{id}/content | Update file content
*CustomFileMetadataApi* | [**get_json_metadata**](docs/CustomFileMetadataApi.md#get_json_metadata) | **GET** /data/{id}/metadata/json | Get file json metadata
*CustomFileMetadataApi* | [**get_rdf_metadata**](docs/CustomFileMetadataApi.md#get_rdf_metadata) | **GET** /data/{id}/metadata/rdf | Get file rdf metadata
*CustomFileMetadataApi* | [**get_xattrs**](docs/CustomFileMetadataApi.md#get_xattrs) | **GET** /data/{id}/metadata/xattrs | Get file extended attributes
*CustomFileMetadataApi* | [**remove_json_metadata**](docs/CustomFileMetadataApi.md#remove_json_metadata) | **DELETE** /data/{id}/metadata/json | Remove file json metadata
*CustomFileMetadataApi* | [**remove_rdf_metadata**](docs/CustomFileMetadataApi.md#remove_rdf_metadata) | **DELETE** /data/{id}/metadata/rdf | Remove file rdf metadata
*CustomFileMetadataApi* | [**remove_xattrs**](docs/CustomFileMetadataApi.md#remove_xattrs) | **DELETE** /data/{id}/metadata/xattrs | Remove file xattrs
*CustomFileMetadataApi* | [**set_json_metadata**](docs/CustomFileMetadataApi.md#set_json_metadata) | **PUT** /data/{id}/metadata/json | Set file json metadata
*CustomFileMetadataApi* | [**set_rdf_metadata**](docs/CustomFileMetadataApi.md#set_rdf_metadata) | **PUT** /data/{id}/metadata/rdf | Set file rdf metadata
*CustomFileMetadataApi* | [**set_xattr**](docs/CustomFileMetadataApi.md#set_xattr) | **PUT** /data/{id}/metadata/xattrs | Set file extended attribute
*DatasetApi* | [**establish_dataset**](docs/DatasetApi.md#establish_dataset) | **POST** /datasets | Establish dataset
*DatasetApi* | [**get_dataset**](docs/DatasetApi.md#get_dataset) | **GET** /datasets/{did} | Get dataset information
*DatasetApi* | [**get_file_dataset_summary**](docs/DatasetApi.md#get_file_dataset_summary) | **GET** /data/{id}/dataset/summary | Get dataset summary for file or directory
*DatasetApi* | [**list_dataset_children**](docs/DatasetApi.md#list_dataset_children) | **GET** /datasets/{did}/children | List child datasets of a dataset
*DatasetApi* | [**list_space_top_datasets**](docs/DatasetApi.md#list_space_top_datasets) | **GET** /spaces/{sid}/datasets | List space top datasets
*DatasetApi* | [**remove_dataset**](docs/DatasetApi.md#remove_dataset) | **DELETE** /datasets/{did} | Remove dataset
*DatasetApi* | [**update_dataset**](docs/DatasetApi.md#update_dataset) | **PATCH** /datasets/{did} | Update dataset
*FileDistributionApi* | [**get_file_distribution**](docs/FileDistributionApi.md#get_file_distribution) | **GET** /data/{id}/distribution | Get file distribution
*FileDistributionApi* | [**get_file_storage_locations**](docs/FileDistributionApi.md#get_file_storage_locations) | **GET** /data/{id}/storage_locations | Get file storage locations
*FilePathResolutionApi* | [**lookup_file_id**](docs/FilePathResolutionApi.md#lookup_file_id) | **POST** /lookup-file-id/{path} | Lookup file id
*MiscellaneousApi* | [**get_directory_size_stats**](docs/MiscellaneousApi.md#get_directory_size_stats) | **GET** /data/{id}/dir_size_stats | Get directory size statistics
*MiscellaneousApi* | [**register_file**](docs/MiscellaneousApi.md#register_file) | **POST** /data/register | Register file
*MonitoringApi* | [**get_space_changes**](docs/MonitoringApi.md#get_space_changes) | **POST** /changes/metadata/{sid} | Subscribe to file events
*OneproviderApi* | [**get_configuration**](docs/OneproviderApi.md#get_configuration) | **GET** /configuration | Get public information
*OneproviderApi* | [**health**](docs/OneproviderApi.md#health) | **GET** /health | Check cluster health
*OneproviderApi* | [**test_image**](docs/OneproviderApi.md#test_image) | **GET** /test_image | Get test image
*QoSApi* | [**add_qos_requirement**](docs/QoSApi.md#add_qos_requirement) | **POST** /qos_requirements | Add QoS requirement
*QoSApi* | [**evaluate_qos_expression**](docs/QoSApi.md#evaluate_qos_expression) | **POST** /spaces/{sid}/evaluate_qos_expression | Evaluate QoS expression
*QoSApi* | [**get_file_qos_summary**](docs/QoSApi.md#get_file_qos_summary) | **GET** /data/{id}/qos/summary | Get QoS summary for file or directory
*QoSApi* | [**get_qos_requirement**](docs/QoSApi.md#get_qos_requirement) | **GET** /qos_requirements/{qid} | Get QoS requirement
*QoSApi* | [**get_qos_requirement_audit_log**](docs/QoSApi.md#get_qos_requirement_audit_log) | **GET** /qos_requirements/{qid}/audit_log | Get QoS audit log
*QoSApi* | [**remove_qos_requirement**](docs/QoSApi.md#remove_qos_requirement) | **DELETE** /qos_requirements/{qid} | Remove QoS requirement
*ShareApi* | [**create_share**](docs/ShareApi.md#create_share) | **POST** /shares | Create share
*ShareApi* | [**get_share**](docs/ShareApi.md#get_share) | **GET** /shares/{shid} | Get share info
*ShareApi* | [**remove_share**](docs/ShareApi.md#remove_share) | **DELETE** /shares/{shid} | Remove share
*ShareApi* | [**update_share**](docs/ShareApi.md#update_share) | **PATCH** /shares/{shid} | Update share
*SpaceApi* | [**get_all_spaces**](docs/SpaceApi.md#get_all_spaces) | **GET** /spaces | Get all user spaces
*SpaceApi* | [**get_space**](docs/SpaceApi.md#get_space) | **GET** /spaces/{sid} | Get basic space information
*TransferApi* | [**cancel_transfer**](docs/TransferApi.md#cancel_transfer) | **DELETE** /transfers/{tid} | Cancel specific transfer
*TransferApi* | [**create_transfer**](docs/TransferApi.md#create_transfer) | **POST** /transfers | Create transfer
*TransferApi* | [**get_all_transfers**](docs/TransferApi.md#get_all_transfers) | **GET** /spaces/{sid}/transfers | Get all space transfers
*TransferApi* | [**get_transfer_status**](docs/TransferApi.md#get_transfer_status) | **GET** /transfers/{tid} | Get transfer status
*TransferApi* | [**rerun_transfer**](docs/TransferApi.md#rerun_transfer) | **POST** /transfers/{tid}/rerun | Rerun ended transfer
*ViewApi* | [**create_space_view**](docs/ViewApi.md#create_space_view) | **PUT** /spaces/{sid}/views/{view_name} | Create view
*ViewApi* | [**get_space_view**](docs/ViewApi.md#get_space_view) | **GET** /spaces/{sid}/views/{view_name} | Get view
*ViewApi* | [**get_space_views**](docs/ViewApi.md#get_space_views) | **GET** /spaces/{sid}/views | Get all space views
*ViewApi* | [**query_space_view**](docs/ViewApi.md#query_space_view) | **GET** /spaces/{sid}/views/{view_name}/query | Query view
*ViewApi* | [**remove_space_view**](docs/ViewApi.md#remove_space_view) | **DELETE** /spaces/{sid}/views/{view_name} | Remove view
*ViewApi* | [**remove_view_reduce_function**](docs/ViewApi.md#remove_view_reduce_function) | **DELETE** /spaces/{sid}/views/{view_name}/reduce | Remove view reduce function
*ViewApi* | [**update_space_view**](docs/ViewApi.md#update_space_view) | **PATCH** /spaces/{sid}/views/{view_name} | Update view
*ViewApi* | [**update_view_reduce_function**](docs/ViewApi.md#update_view_reduce_function) | **PUT** /spaces/{sid}/views/{view_name}/reduce | Update view reduce function
*WorkflowExecutionApi* | [**cancel_workflow_execution**](docs/WorkflowExecutionApi.md#cancel_workflow_execution) | **POST** /automation/execution/workflows/{wid}/cancel | Cancel workflow execution
*WorkflowExecutionApi* | [**delete_workflow_execution**](docs/WorkflowExecutionApi.md#delete_workflow_execution) | **DELETE** /automation/execution/workflows/{wid} | Delete workflow execution
*WorkflowExecutionApi* | [**force_continue_workflow_execution**](docs/WorkflowExecutionApi.md#force_continue_workflow_execution) | **POST** /automation/execution/workflows/{wid}/force_continue | Force continue workflow execution
*WorkflowExecutionApi* | [**get_workflow_execution_details**](docs/WorkflowExecutionApi.md#get_workflow_execution_details) | **GET** /automation/execution/workflows/{wid} | Get workflow execution details
*WorkflowExecutionApi* | [**list_workflow_executions**](docs/WorkflowExecutionApi.md#list_workflow_executions) | **GET** /spaces/{sid}/automation/execution/workflows | List workflow executions
*WorkflowExecutionApi* | [**pause_workflow_execution**](docs/WorkflowExecutionApi.md#pause_workflow_execution) | **POST** /automation/execution/workflows/{wid}/pause | Pause workflow execution
*WorkflowExecutionApi* | [**rerun_workflow_execution**](docs/WorkflowExecutionApi.md#rerun_workflow_execution) | **POST** /automation/execution/workflows/{wid}/rerun | Rerun workflow execution
*WorkflowExecutionApi* | [**resume_workflow_execution**](docs/WorkflowExecutionApi.md#resume_workflow_execution) | **POST** /automation/execution/workflows/{wid}/resume | Resume workflow execution
*WorkflowExecutionApi* | [**retry_workflow_execution**](docs/WorkflowExecutionApi.md#retry_workflow_execution) | **POST** /automation/execution/workflows/{wid}/retry | Retry workflow execution
*WorkflowExecutionApi* | [**schedule_workflow_execution**](docs/WorkflowExecutionApi.md#schedule_workflow_execution) | **POST** /automation/execution/workflows | Schedule workflow execution

## Documentation For Models

 - [Archive](docs/Archive.md)
 - [ArchiveBase](docs/ArchiveBase.md)
 - [ArchiveConfig](docs/ArchiveConfig.md)
 - [ArchiveCreateNestedArchives](docs/ArchiveCreateNestedArchives.md)
 - [ArchiveCreateRequest](docs/ArchiveCreateRequest.md)
 - [ArchiveDeleteRequest](docs/ArchiveDeleteRequest.md)
 - [ArchiveDeletedCallback](docs/ArchiveDeletedCallback.md)
 - [ArchiveDescription](docs/ArchiveDescription.md)
 - [ArchiveFollowSymlinks](docs/ArchiveFollowSymlinks.md)
 - [ArchiveIncludeDip](docs/ArchiveIncludeDip.md)
 - [ArchiveIncremental](docs/ArchiveIncremental.md)
 - [ArchiveLayout](docs/ArchiveLayout.md)
 - [ArchivePreservedCallback](docs/ArchivePreservedCallback.md)
 - [ArchiveRecallDetails](docs/ArchiveRecallDetails.md)
 - [ArchiveRecallDetailsLastError](docs/ArchiveRecallDetailsLastError.md)
 - [ArchiveRecallProgress](docs/ArchiveRecallProgress.md)
 - [ArchiveRecallRequest](docs/ArchiveRecallRequest.md)
 - [ArchiveRecallResponse](docs/ArchiveRecallResponse.md)
 - [ArchiveState](docs/ArchiveState.md)
 - [ArchiveStats](docs/ArchiveStats.md)
 - [ArchiveUpdateRequest](docs/ArchiveUpdateRequest.md)
 - [Archives](docs/Archives.md)
 - [AtmWorkflowExecutionDetails](docs/AtmWorkflowExecutionDetails.md)
 - [AtmWorkflowExecutionDetailsLanes](docs/AtmWorkflowExecutionDetailsLanes.md)
 - [AtmWorkflowExecutionLaneRunDetails](docs/AtmWorkflowExecutionLaneRunDetails.md)
 - [AtmWorkflowExecutionLaneRunDetailsParallelBoxes](docs/AtmWorkflowExecutionLaneRunDetailsParallelBoxes.md)
 - [AtmWorkflowExecutionScheduleRequest](docs/AtmWorkflowExecutionScheduleRequest.md)
 - [Configuration](docs/Configuration.md)
 - [Dataset](docs/Dataset.md)
 - [DatasetEstablishRequest](docs/DatasetEstablishRequest.md)
 - [DatasetProtectionFlags](docs/DatasetProtectionFlags.md)
 - [DatasetState](docs/DatasetState.md)
 - [DatasetSummary](docs/DatasetSummary.md)
 - [DatasetUpdateRequest](docs/DatasetUpdateRequest.md)
 - [Datasets](docs/Datasets.md)
 - [DatasetsDatasets](docs/DatasetsDatasets.md)
 - [DirSizeStatsQuery](docs/DirSizeStatsQuery.md)
 - [DirSizeStatsResponse](docs/DirSizeStatsResponse.md)
 - [DirectoryChildren](docs/DirectoryChildren.md)
 - [EffectiveFileProtectionFlags](docs/EffectiveFileProtectionFlags.md)
 - [Error](docs/Error.md)
 - [ErrorJson](docs/ErrorJson.md)
 - [File](docs/File.md)
 - [FileAttributes](docs/FileAttributes.md)
 - [FileDistribution](docs/FileDistribution.md)
 - [FileDistributionDistributionPerProvider](docs/FileDistributionDistributionPerProvider.md)
 - [FileDistributionDistributionPerStorage](docs/FileDistributionDistributionPerStorage.md)
 - [FileDistributionError](docs/FileDistributionError.md)
 - [FileRegistrationRequest](docs/FileRegistrationRequest.md)
 - [FileType](docs/FileType.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [InlineResponse2011](docs/InlineResponse2011.md)
 - [InlineResponse2012](docs/InlineResponse2012.md)
 - [InlineResponse2013](docs/InlineResponse2013.md)
 - [InlineResponse2014](docs/InlineResponse2014.md)
 - [InlineResponse2015](docs/InlineResponse2015.md)
 - [InlineResponse2016](docs/InlineResponse2016.md)
 - [InlineResponse2017](docs/InlineResponse2017.md)
 - [InlineResponse2018](docs/InlineResponse2018.md)
 - [IsLast](docs/IsLast.md)
 - [Layout](docs/Layout.md)
 - [ListPageToken](docs/ListPageToken.md)
 - [MetadataChangesEvent](docs/MetadataChangesEvent.md)
 - [MetadataChangesEventCustomMetadata](docs/MetadataChangesEventCustomMetadata.md)
 - [MetadataChangesEventFileLocation](docs/MetadataChangesEventFileLocation.md)
 - [MetadataChangesEventFileLocationFields](docs/MetadataChangesEventFileLocationFields.md)
 - [MetadataChangesEventFileMeta](docs/MetadataChangesEventFileMeta.md)
 - [MetadataChangesEventFileMetaFields](docs/MetadataChangesEventFileMetaFields.md)
 - [MetadataChangesEventTimes](docs/MetadataChangesEventTimes.md)
 - [MetadataChangesEventTimesFields](docs/MetadataChangesEventTimesFields.md)
 - [MetadataChangesStreamRequest](docs/MetadataChangesStreamRequest.md)
 - [MetadataChangesStreamRequestCustomMetadata](docs/MetadataChangesStreamRequestCustomMetadata.md)
 - [MetadataChangesStreamRequestFileLocation](docs/MetadataChangesStreamRequestFileLocation.md)
 - [MetadataChangesStreamRequestFileMeta](docs/MetadataChangesStreamRequestFileMeta.md)
 - [MetadataChangesStreamRequestTimes](docs/MetadataChangesStreamRequestTimes.md)
 - [MetadataXattrsBody](docs/MetadataXattrsBody.md)
 - [Metrics](docs/Metrics.md)
 - [Provider](docs/Provider.md)
 - [QosCreateRequest](docs/QosCreateRequest.md)
 - [QosRequirement](docs/QosRequirement.md)
 - [QosRequirementAuditLog](docs/QosRequirementAuditLog.md)
 - [QosRequirementAuditLogContent](docs/QosRequirementAuditLogContent.md)
 - [QosRequirementAuditLogLogEntries](docs/QosRequirementAuditLogLogEntries.md)
 - [QosSummary](docs/QosSummary.md)
 - [QueryViewParams](docs/QueryViewParams.md)
 - [RRD](docs/RRD.md)
 - [RRDMeta](docs/RRDMeta.md)
 - [RecursiveFileList](docs/RecursiveFileList.md)
 - [Share](docs/Share.md)
 - [ShareCreateRequest](docs/ShareCreateRequest.md)
 - [Shares](docs/Shares.md)
 - [SharesShidBody](docs/SharesShidBody.md)
 - [Slice](docs/Slice.md)
 - [Space](docs/Space.md)
 - [StorageDetails](docs/StorageDetails.md)
 - [StorageFileLocations](docs/StorageFileLocations.md)
 - [StorageFileLocationsLocationsPerProvider](docs/StorageFileLocationsLocationsPerProvider.md)
 - [TSWindowInfo](docs/TSWindowInfo.md)
 - [TimeSeriesLayout](docs/TimeSeriesLayout.md)
 - [TimeSeriesSlice](docs/TimeSeriesSlice.md)
 - [Timestamp](docs/Timestamp.md)
 - [TransferCreateRequest](docs/TransferCreateRequest.md)
 - [TransferStatus](docs/TransferStatus.md)
 - [View](docs/View.md)
 - [ViewOptions](docs/ViewOptions.md)
 - [Views](docs/Views.md)
 - [WidRerunBody](docs/WidRerunBody.md)
 - [WidRetryBody](docs/WidRetryBody.md)

## Documentation For Authorization


## api_key1

- **Type**: API key
- **API key parameter name**: X-Auth-Token
- **Location**: HTTP header

## api_key2

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

info@onedata.org
