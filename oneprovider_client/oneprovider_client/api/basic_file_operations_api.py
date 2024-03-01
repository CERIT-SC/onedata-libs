# coding: utf-8

"""
    Oneprovider

    # Overview  This is the RESTful API definition of Oneprovider component of Onedata data management system [onedata.org](http://onedata.org).  > This API is defined using [Swagger](http://swagger.io/), the JSON specification can be used to automatically generate > client libraries - [swagger.json](../../../swagger/oneprovider/swagger.json).  All paths below are relative to a common Oneprovider basepath which is `/api/v3/oneprovider`, thus a complete example query for 'mode' file attributes would be: ``` https://ONEPROVIDER_HOSTNAME/api/v3/oneprovider/data/$FILE_ID?attribute=mode ``` Please note that currently the default port for Oneprovider instances is `443`.  In addition to REST API, Oneprovider also provides support for [CDMI](http://onedata.org/#/home/documentation/doc/advanced/cdmi.html) protocol.   ## Authentication To use the APIs, the REST client must authenticate with the Oneprovider service and present a proof of authorization to perform a specific operation. This is done using access tokens, which can be generated using the Onedata GUI or Onezone's REST API.  The token is passed in the request header like this: ``` X-Auth-Token: MIIFrzCCA5egAwIBAgIBEzANBgkqhkiG9w0BAQUFADBcMQswCQYDVQQGEwJQTDET... ```  The authorization to perform a specific operation depends on the authenticated user's privileges in the corresponding space, file level permissions (posix, ACL) and caveats (restrictions) inscribed in the provided access token.   ## Data management basics The Onedata system organizes all user data into logical containers called spaces. <!--- TODO VFS-7218 uncomment when the new docs are deployed --> <!--- For more information, please refer to the [documentation](https://onedata.org/#/home/documentation). -->  Files and directories in Onedata can be globally identified using unique File Ids or logical paths. Whenever possible, it is recommended to use File Ids, due to better performance and no need for escaping or encoding.  ### File path All logical paths in Onedata use the slash (`/`) delimiter and must start with a space name: ```lang-none /CMS 1/file.txt /MyExperiment/directory/subdirectory/image.jpg ```  When referencing files by path in the REST API, make sure to urlencode the path in the URL: ```bash {...}/CMS%201/file.txt ```  ### File Id  File Id is a unique, global identifier associated with a file or directory and can be used universally in the REST and CDMI APIs. There are several ways to find out the File Id of given file or directory: <!---  @TODO VFS-7218 remove redundant information and provide a link to the new docs -->  **Web GUI** - click on Information in the file/directory context menu and look for File Id.  **REST API** - use the File Id resolution endpoint. Below example returns the File Id of `/CMS 1/file.txt`, where `CMS 1` is the space name:  ```bash curl -H \"X-Auth-Token: ${ACCESS_TOKEN}\" \\ -X POST \"https://${ONEPROVIDER_DOMAIN}/api/v3/oneprovider/lookup-file-id/CMS%201/file.txt\" {     \"fileId\": \"094576776E667431723230677767776C6B497031394E445F6E3868677873...\" } ```  ### Space Id  Space Id is a unique, global identifier associated with a space and can be used universally in the REST APIs. In order to find out the Space Id:  **Web GUI** - click on Information in the file/directory context menu and look for Space Id.  **REST API** - use the [Get all user spaces](#operation/get_all_spaces) endpoint.  The Space Id can be used interchangeably with the space root directory's File Id in the path-based enpoints.  **Remove specific file relative to the space root** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_ID/path/dir1/file.txt\" # is equivalent to curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_ROOT_FILE_ID/path/dir1/file.txt\" ``` **Remove specific file relative to any parent directory** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$PARENT_FILE_ID/path/dir1/file.txt\" ```   ## API structure  The API is divided into the following sections:  ### Space management These methods provide means for getting basic information about spaces directly from the Oneprovider service, but also allows to define database views.  ### File access and management The API provides capabilities for:   - browsing files in spaces and directories,   - creating and deleting files as well as updating their content   - querying for file attributes, such as 'mode' file permissions and updating them,   - managing custom file metadata (xattrs, JSON, RDF),   - manual registration of files for imported storages.  More information can be found [here](#section/Overview/Data-management-basics).  ### Replica and QoS management These methods allow viewing file replica distribution, requesting file replication (transfers) between Oneproviders, viewing ongoing and historical transfers data, as well as managing QoS requirements that trigger automatic replication according to the QoS rules.  ### Share management Offers methods for creating, modyfying and deleting shares. Shares are files or directories that were made publicly available, so that they can be viewed by everyone through a public URL.  ### Dataset & archive management API for managing datasets - designated files or directories that are used to facilitate building collections of data meaningful for the users with additional features, such as write protection and archivisation mechanisms.  ### Automation Basic API for scheduling and viewing workflow executions.  ### Monitoring The API provides means for subscribing (through HTTP long-polling technique) for file related events such as reads, writes or deletes which are returned as complete file metadata records with sequence numbers representing their current version.  ### Service information Publicly available, basic configuration of the Oneprovider service.  Detailed examples of API usage are available in the documentation of each operation.   # noqa: E501

    OpenAPI spec version: 21.02.3
    Contact: info@onedata.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from oneprovider_client.api_client import ApiClient


class BasicFileOperationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_file(self, name, id, **kwargs):  # noqa: E501
        """Create file in directory  # noqa: E501

        Creates a file in the directory specified by [$PARENT_ID](#operation/lookup_file_id).  If the file already exists, the operation fails with an error.  The file type can be of: - `REG` (regular file) - in this case, **the data sent in request body (if any) is saved as file content**. - `DIR` (directory). - `LNK` (hard link) - requires that `target_file_id` pointing to a regular file is specified. - `SYMLNK` (symbolic link) - requires that `target_file_path` is specified. When creating symbolic link with absolute path starting from specific space it is necessary to do so by replacing `/$SPACE_NAME/` in path by special prefix in the form `<__onedata_space_id:$SPACE_ID>/` (where $SPACE_ID is actual space id)  ***Example cURL requests***  **Create file** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$PARENT_ID/children?name=$NAME\" -H \"Content-Type: application/octet-stream\" -d \"@file.dat\"  {    \"fileId\": \"094576776E667431723230677767776C6B497031394E445F6E3868677873...\" } ```  **Create directory** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$PARENT_ID/children?name=$NAME&type=DIR\"  {    \"fileId\": \"000000006CB6637368617265477569642333396432363661656463656266...\" } ```  **Create hard link** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$PARENT_ID/children?name=$NAME&type=LNK&target_file_id=$TARGET_FILE_ID\"  {    \"fileId\": \"000000184465677569642373706163655F73706163653123737061636531...\" } ```  **Create symbolic link** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$PARENT_ID/children?name=$NAME&type=SYMLNK&target_file_path=$TARGET_FILE_PATH\"  {    \"fileId\": \"00989AB98890037368617265477569642333396432363661656463656266...\" } ```  See also [Create file at path](#operation/create_file_at_path).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_file(name, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name of the file. (required)
        :param str id: Id of the parent directory. (required)
        :param Object body: File content to be written at specified offset (relevant only if `type == "REG"`).
        :param str type: Type of the file.
        :param int mode: POSIX file permissions in decimal format.
        :param int offset: Offset at which the data sent as request body will be written to the file (relevant only if `type == \"REG\"`). 
        :param str target_file_id: The Id of the file to which the hard link should point (relevant only if `type == \"LNK\"`). 
        :param str target_file_path: Path to which the symbolic link should point (relevant only if `type == \"SYMLNK\"`). 
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_file_with_http_info(name, id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_file_with_http_info(name, id, **kwargs)  # noqa: E501
            return data

    def create_file_with_http_info(self, name, id, **kwargs):  # noqa: E501
        """Create file in directory  # noqa: E501

        Creates a file in the directory specified by [$PARENT_ID](#operation/lookup_file_id).  If the file already exists, the operation fails with an error.  The file type can be of: - `REG` (regular file) - in this case, **the data sent in request body (if any) is saved as file content**. - `DIR` (directory). - `LNK` (hard link) - requires that `target_file_id` pointing to a regular file is specified. - `SYMLNK` (symbolic link) - requires that `target_file_path` is specified. When creating symbolic link with absolute path starting from specific space it is necessary to do so by replacing `/$SPACE_NAME/` in path by special prefix in the form `<__onedata_space_id:$SPACE_ID>/` (where $SPACE_ID is actual space id)  ***Example cURL requests***  **Create file** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$PARENT_ID/children?name=$NAME\" -H \"Content-Type: application/octet-stream\" -d \"@file.dat\"  {    \"fileId\": \"094576776E667431723230677767776C6B497031394E445F6E3868677873...\" } ```  **Create directory** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$PARENT_ID/children?name=$NAME&type=DIR\"  {    \"fileId\": \"000000006CB6637368617265477569642333396432363661656463656266...\" } ```  **Create hard link** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$PARENT_ID/children?name=$NAME&type=LNK&target_file_id=$TARGET_FILE_ID\"  {    \"fileId\": \"000000184465677569642373706163655F73706163653123737061636531...\" } ```  **Create symbolic link** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$PARENT_ID/children?name=$NAME&type=SYMLNK&target_file_path=$TARGET_FILE_PATH\"  {    \"fileId\": \"00989AB98890037368617265477569642333396432363661656463656266...\" } ```  See also [Create file at path](#operation/create_file_at_path).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_file_with_http_info(name, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name of the file. (required)
        :param str id: Id of the parent directory. (required)
        :param Object body: File content to be written at specified offset (relevant only if `type == "REG"`).
        :param str type: Type of the file.
        :param int mode: POSIX file permissions in decimal format.
        :param int offset: Offset at which the data sent as request body will be written to the file (relevant only if `type == \"REG\"`). 
        :param str target_file_id: The Id of the file to which the hard link should point (relevant only if `type == \"LNK\"`). 
        :param str target_file_path: Path to which the symbolic link should point (relevant only if `type == \"SYMLNK\"`). 
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'id', 'body', 'type', 'mode', 'offset', 'target_file_id', 'target_file_path']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `create_file`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'mode' in params:
            query_params.append(('mode', params['mode']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'target_file_id' in params:
            query_params.append(('target_file_id', params['target_file_id']))  # noqa: E501
        if 'target_file_path' in params:
            query_params.append(('target_file_path', params['target_file_path']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}/children', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse201',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_file_at_path(self, id, path, **kwargs):  # noqa: E501
        """Create file at path  # noqa: E501

        Creates a file at path specified in the URL, relative to the base directory given in the `id` parameter (see the parameter description for details). If the parent path does not exist and `create_parents` flag is set to true, the operation will attempt to create intermediate parent directories.  If the file already exists, the operation fails with an error.  The file type can be of: - `REG` (regular file) - in this case, the **data sent in request body (if any) is saved as file content**. - `DIR` (directory). - `LNK` (hard link) - requires that `target_file_id` pointing to a regular file is specified. - `SYMLNK` (symbolic link) - requires that `target_file_path` is specified. When creating symbolic link with absolute path starting from specific space it is necessary to do so by replacing `/$SPACE_NAME/` in path by special prefix in the form `<__onedata_space_id:$SPACE_ID>/` (where $SPACE_ID is actual space id)  ***Example cURL requests***  **Create file** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/dir1/$NAME\" -H \"Content-Type: application/octet-stream\" -d \"@file.dat\"  {    \"fileId\": \"094576776E667431723230677767776C6B497031394E445F6E3868677873...\" } ```  **Create directory** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/$NAME?type=DIR\"  {    \"fileId\": \"000000006CB6637368617265477569642333396432363661656463656266...\" } ```  **Create hard link** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/$NAME&type=LNK&target_file_id=$TARGET_FILE_ID\"  {    \"fileId\": \"000000184465677569642373706163655F73706163653123737061636531...\" } ```  **Create symbolic link** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/$NAME&type=SYMLNK&target_file_path=$TARGET_FILE_PATH\"  {    \"fileId\": \"00989AB98890037368617265477569642333396432363661656463656266...\" } ```  See also [Create file in directory](#operation/create_file).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_file_at_path(id, path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the base directory, relative to which the path remainder will be resolved. It can be a **Space Id** (in which case the space root directory is taken), or a **File Id** of any existing directory (including the space root directory). See [Data](#section/Overview/Data-management-basics) section for more information.  (required)
        :param str path: Path relative to the base directory (specified in the id parameter). (required)
        :param Object body: File content to be written at specified offset (relevant only if `type == "REG"`).
        :param str type: Type of the file.
        :param int mode: POSIX file permissions in decimal format.
        :param bool create_parents: Allows to create unexistient directories specified in path parameter.
        :param int offset: Offset at which the data sent as request body will be written to the file (relevant only if `type == \"REG\"`). 
        :param str target_file_id: The Id of the file to which the hard link should point (relevant only if `type == \"LNK\"`). 
        :param str target_file_path: Path to which the symbolic link should point (relevant only if `type == \"SYMLNK\"`). 
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_file_at_path_with_http_info(id, path, **kwargs)  # noqa: E501
        else:
            (data) = self.create_file_at_path_with_http_info(id, path, **kwargs)  # noqa: E501
            return data

    def create_file_at_path_with_http_info(self, id, path, **kwargs):  # noqa: E501
        """Create file at path  # noqa: E501

        Creates a file at path specified in the URL, relative to the base directory given in the `id` parameter (see the parameter description for details). If the parent path does not exist and `create_parents` flag is set to true, the operation will attempt to create intermediate parent directories.  If the file already exists, the operation fails with an error.  The file type can be of: - `REG` (regular file) - in this case, the **data sent in request body (if any) is saved as file content**. - `DIR` (directory). - `LNK` (hard link) - requires that `target_file_id` pointing to a regular file is specified. - `SYMLNK` (symbolic link) - requires that `target_file_path` is specified. When creating symbolic link with absolute path starting from specific space it is necessary to do so by replacing `/$SPACE_NAME/` in path by special prefix in the form `<__onedata_space_id:$SPACE_ID>/` (where $SPACE_ID is actual space id)  ***Example cURL requests***  **Create file** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/dir1/$NAME\" -H \"Content-Type: application/octet-stream\" -d \"@file.dat\"  {    \"fileId\": \"094576776E667431723230677767776C6B497031394E445F6E3868677873...\" } ```  **Create directory** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/$NAME?type=DIR\"  {    \"fileId\": \"000000006CB6637368617265477569642333396432363661656463656266...\" } ```  **Create hard link** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/$NAME&type=LNK&target_file_id=$TARGET_FILE_ID\"  {    \"fileId\": \"000000184465677569642373706163655F73706163653123737061636531...\" } ```  **Create symbolic link** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/$NAME&type=SYMLNK&target_file_path=$TARGET_FILE_PATH\"  {    \"fileId\": \"00989AB98890037368617265477569642333396432363661656463656266...\" } ```  See also [Create file in directory](#operation/create_file).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_file_at_path_with_http_info(id, path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the base directory, relative to which the path remainder will be resolved. It can be a **Space Id** (in which case the space root directory is taken), or a **File Id** of any existing directory (including the space root directory). See [Data](#section/Overview/Data-management-basics) section for more information.  (required)
        :param str path: Path relative to the base directory (specified in the id parameter). (required)
        :param Object body: File content to be written at specified offset (relevant only if `type == "REG"`).
        :param str type: Type of the file.
        :param int mode: POSIX file permissions in decimal format.
        :param bool create_parents: Allows to create unexistient directories specified in path parameter.
        :param int offset: Offset at which the data sent as request body will be written to the file (relevant only if `type == \"REG\"`). 
        :param str target_file_id: The Id of the file to which the hard link should point (relevant only if `type == \"LNK\"`). 
        :param str target_file_path: Path to which the symbolic link should point (relevant only if `type == \"SYMLNK\"`). 
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'path', 'body', 'type', 'mode', 'create_parents', 'offset', 'target_file_id', 'target_file_path']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_file_at_path" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_file_at_path`")  # noqa: E501
        # verify the required parameter 'path' is set
        if ('path' not in params or
                params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `create_file_at_path`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'path' in params:
            path_params['path'] = params['path']  # noqa: E501

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'mode' in params:
            query_params.append(('mode', params['mode']))  # noqa: E501
        if 'create_parents' in params:
            query_params.append(('create_parents', params['create_parents']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'target_file_id' in params:
            query_params.append(('target_file_id', params['target_file_id']))  # noqa: E501
        if 'target_file_path' in params:
            query_params.append(('target_file_path', params['target_file_path']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}/path/{path}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse201',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def download_file_content(self, id, **kwargs):  # noqa: E501
        """Download file content  # noqa: E501

        Returns the content of a file or directory specified by [$FILE_ID](#operation/lookup_file_id).  If $FILE_ID is a regular file, returns its binary content. Partial content download is also supported using [Range header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Range).  If $FILE_ID is a directory, returns a TAR archive with its contents. Any nested files or subdirectories to which the client does not have access (e.g. due to insufficient POSIX permissions or ACLs) are omitted in the resulting archive. Request for directory download results in a redirection URL (in Location header) that contains the ID of a temporary download session. The URL can be used to download the tarball, with support for resuming interrupted downloads using the Range header (where the range start is the number of already downloaded bytes and the range end is omitted).   ***Example cURL requests***  **Download entire file content** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/content\"  abcdefghijklmno ```  **Download only part of the file content** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/content\" \\ -H \"Range: bytes=5-8\"  fghi ```  **Download a directory as tar archive** ```bash curl -sD - -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$DIR_ID/content\" | grep location  location: https://$PROVIDER_HOST/download/$DOWNLOAD_ID ```  ``` curl https://$PROVIDER_HOST/download/$DOWNLOAD_ID > directory.tar ```  **Download a directory as tar archive in a single request** ```bash curl -L -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$DIR_ID/content\" ```  **Resume download of a directory (previous download failed after 12345678 bytes)** ```bash curl -H \"Range: bytes=12345678-\" https://$PROVIDER_HOST/download/$DOWNLOAD_ID >> directory.tar ```  **Download a directory as tar archive in a single request without resolving symlinks** ```bash curl -L -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$DIR_ID/content?follow_symlinks=false\" ```  See also [Download file content by path](#operation/download_file_content_by_path).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_file_content(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the file. (required)
        :param bool follow_symlinks: Flag controlling whether symbolic links in requested download should be resolved.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_file_content_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.download_file_content_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def download_file_content_with_http_info(self, id, **kwargs):  # noqa: E501
        """Download file content  # noqa: E501

        Returns the content of a file or directory specified by [$FILE_ID](#operation/lookup_file_id).  If $FILE_ID is a regular file, returns its binary content. Partial content download is also supported using [Range header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Range).  If $FILE_ID is a directory, returns a TAR archive with its contents. Any nested files or subdirectories to which the client does not have access (e.g. due to insufficient POSIX permissions or ACLs) are omitted in the resulting archive. Request for directory download results in a redirection URL (in Location header) that contains the ID of a temporary download session. The URL can be used to download the tarball, with support for resuming interrupted downloads using the Range header (where the range start is the number of already downloaded bytes and the range end is omitted).   ***Example cURL requests***  **Download entire file content** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/content\"  abcdefghijklmno ```  **Download only part of the file content** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/content\" \\ -H \"Range: bytes=5-8\"  fghi ```  **Download a directory as tar archive** ```bash curl -sD - -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$DIR_ID/content\" | grep location  location: https://$PROVIDER_HOST/download/$DOWNLOAD_ID ```  ``` curl https://$PROVIDER_HOST/download/$DOWNLOAD_ID > directory.tar ```  **Download a directory as tar archive in a single request** ```bash curl -L -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$DIR_ID/content\" ```  **Resume download of a directory (previous download failed after 12345678 bytes)** ```bash curl -H \"Range: bytes=12345678-\" https://$PROVIDER_HOST/download/$DOWNLOAD_ID >> directory.tar ```  **Download a directory as tar archive in a single request without resolving symlinks** ```bash curl -L -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$DIR_ID/content?follow_symlinks=false\" ```  See also [Download file content by path](#operation/download_file_content_by_path).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_file_content_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the file. (required)
        :param bool follow_symlinks: Flag controlling whether symbolic links in requested download should be resolved.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'follow_symlinks']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_file_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `download_file_content`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'follow_symlinks' in params:
            query_params.append(('follow_symlinks', params['follow_symlinks']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}/content', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def download_file_content_by_path(self, id, path, **kwargs):  # noqa: E501
        """Download file content by path  # noqa: E501

        Returns the content of a file or directory by path specified in the URL, relative to the base directory given in the `id` parameter (see the parameter description for details).  If requested file is a regular file, returns its binary content. Partial content download is also supported using [Range header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Range).  If requested file is a directory, returns a TAR archive with its contents. Any nested files or subdirectories to which the client does not have access (e.g. due to insufficient POSIX permissions or ACLs) are omitted in the resulting archive. Request for directory download results in a redirection URL (in Location header) that contains the ID of a temporary download session. The URL can be used to download the tarball, with support for resuming interrupted downloads using the Range header (where the range start is the number of already downloaded bytes and the range end is omitted).   ***Example cURL requests***  **Download entire file content** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/dir1/dir2/file\" \\  abcdefghijklmno ```  **Download only part of the file content** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/dir1/dir2/file\" \\ -H \"Range: bytes=5-8\"  fghi ```  **Download a directory as tar archive** ```bash curl -sD - -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/dir1\" | grep location  location: https://$PROVIDER_HOST/download/$DOWNLOAD_ID ```  ``` curl https://$PROVIDER_HOST/download/$DOWNLOAD_ID > directory.tar ```  **Download a directory as tar archive in a single request** ```bash curl -L -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/dir1\" ```  **Resume download of a directory (previous download failed after 12345678 bytes)** ```bash curl -H \"Range: bytes=12345678-\" https://$PROVIDER_HOST/download/$DOWNLOAD_ID >> directory.tar ```  **Download a directory as tar archive in a single request without resolving symlinks** ```bash curl -L -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/dir1?follow_symlinks=false\" ```  See also [Download file content by ID](#operation/download_file_content).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_file_content_by_path(id, path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the base directory, relative to which the path remainder will be resolved. It can be a **Space Id** (in which case the space root directory is taken), or a **File Id** of any existing directory (including the space root directory). See [Data](#section/Overview/Data-management-basics) section for more information.  (required)
        :param str path: Path relative to the base directory (specified in the id parameter). (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_file_content_by_path_with_http_info(id, path, **kwargs)  # noqa: E501
        else:
            (data) = self.download_file_content_by_path_with_http_info(id, path, **kwargs)  # noqa: E501
            return data

    def download_file_content_by_path_with_http_info(self, id, path, **kwargs):  # noqa: E501
        """Download file content by path  # noqa: E501

        Returns the content of a file or directory by path specified in the URL, relative to the base directory given in the `id` parameter (see the parameter description for details).  If requested file is a regular file, returns its binary content. Partial content download is also supported using [Range header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Range).  If requested file is a directory, returns a TAR archive with its contents. Any nested files or subdirectories to which the client does not have access (e.g. due to insufficient POSIX permissions or ACLs) are omitted in the resulting archive. Request for directory download results in a redirection URL (in Location header) that contains the ID of a temporary download session. The URL can be used to download the tarball, with support for resuming interrupted downloads using the Range header (where the range start is the number of already downloaded bytes and the range end is omitted).   ***Example cURL requests***  **Download entire file content** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/dir1/dir2/file\" \\  abcdefghijklmno ```  **Download only part of the file content** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/dir1/dir2/file\" \\ -H \"Range: bytes=5-8\"  fghi ```  **Download a directory as tar archive** ```bash curl -sD - -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/dir1\" | grep location  location: https://$PROVIDER_HOST/download/$DOWNLOAD_ID ```  ``` curl https://$PROVIDER_HOST/download/$DOWNLOAD_ID > directory.tar ```  **Download a directory as tar archive in a single request** ```bash curl -L -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/dir1\" ```  **Resume download of a directory (previous download failed after 12345678 bytes)** ```bash curl -H \"Range: bytes=12345678-\" https://$PROVIDER_HOST/download/$DOWNLOAD_ID >> directory.tar ```  **Download a directory as tar archive in a single request without resolving symlinks** ```bash curl -L -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/dir1?follow_symlinks=false\" ```  See also [Download file content by ID](#operation/download_file_content).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_file_content_by_path_with_http_info(id, path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the base directory, relative to which the path remainder will be resolved. It can be a **Space Id** (in which case the space root directory is taken), or a **File Id** of any existing directory (including the space root directory). See [Data](#section/Overview/Data-management-basics) section for more information.  (required)
        :param str path: Path relative to the base directory (specified in the id parameter). (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'path']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_file_content_by_path" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `download_file_content_by_path`")  # noqa: E501
        # verify the required parameter 'path' is set
        if ('path' not in params or
                params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `download_file_content_by_path`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'path' in params:
            path_params['path'] = params['path']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}/path/{path}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_attrs(self, id, **kwargs):  # noqa: E501
        """Get file attributes  # noqa: E501

        This method returns either all or only selected basic attributes associated with file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Get file size** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID?attribute=size&attribute=name\"  {     \"name\": \"File1.txt\"     \"size\": 100 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_attrs(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: File, directory or space Id (required)
        :param str attribute: Name of attribute to query for. Can be provided multiple times.  When accessing file via share mode following attributes are unavailable:  `owner_id`, `storage_group_id`, `storage_user_id`, `provider_id`, `hardlinks_count` 
        :return: FileAttributes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_attrs_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_attrs_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_attrs_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get file attributes  # noqa: E501

        This method returns either all or only selected basic attributes associated with file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Get file size** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID?attribute=size&attribute=name\"  {     \"name\": \"File1.txt\"     \"size\": 100 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_attrs_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: File, directory or space Id (required)
        :param str attribute: Name of attribute to query for. Can be provided multiple times.  When accessing file via share mode following attributes are unavailable:  `owner_id`, `storage_group_id`, `storage_user_id`, `provider_id`, `hardlinks_count` 
        :return: FileAttributes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'attribute']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_attrs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_attrs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'attribute' in params:
            if isinstance(params['attribute'], list) or isinstance(params['attribute'], tuple):
                for param in params['attribute']:
                    query_params.append(('attribute', param))  # noqa: E501
            else:
                query_params.append(('attribute', params['attribute']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FileAttributes',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_file_hardlinks(self, id, **kwargs):  # noqa: E501
        """Get file hard links  # noqa: E501

        Returns Ids of all hard links (including this one) associated with file specified by [$FILE_ID](#operation/lookup_file_id).  **Get file hard links** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/hardlinks\"  [     \"094576776E667431723230677767776C6B497031394E445F6E3868677873...\",     \"000000006CB6637368617265477569642333396432363661656463656266...\" ] ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_file_hardlinks(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: File Id. (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_file_hardlinks_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_file_hardlinks_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_file_hardlinks_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get file hard links  # noqa: E501

        Returns Ids of all hard links (including this one) associated with file specified by [$FILE_ID](#operation/lookup_file_id).  **Get file hard links** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/hardlinks\"  [     \"094576776E667431723230677767776C6B497031394E445F6E3868677873...\",     \"000000006CB6637368617265477569642333396432363661656463656266...\" ] ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_file_hardlinks_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: File Id. (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_file_hardlinks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_file_hardlinks`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}/hardlinks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_symlink_value(self, id, **kwargs):  # noqa: E501
        """Get symbolic link value  # noqa: E501

        Returns the value of symbolic link specified by [$FILE_ID](#operation/lookup_file_id) (the path to where the link is pointing).  **Get symbolic link value** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/symlink_value\"  ../../Dir1/File1 ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_symlink_value(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the symbolic link. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_symlink_value_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_symlink_value_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_symlink_value_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get symbolic link value  # noqa: E501

        Returns the value of symbolic link specified by [$FILE_ID](#operation/lookup_file_id) (the path to where the link is pointing).  **Get symbolic link value** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/symlink_value\"  ../../Dir1/File1 ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_symlink_value_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the symbolic link. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_symlink_value" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_symlink_value`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}/symlink_value', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_children(self, id, **kwargs):  # noqa: E501
        """List directory files and subdirectories  # noqa: E501

        Returns the list of directory files and subdirectories for directory specified by [$DIR_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Get files in space subdirectory** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$DIR_ID/children?attribute=size&attribute=name&limit=2\"  {     \"children\": [         {              \"name\": File1.txt             \"size\": 1024         },         {              \"name\": File2.txt             \"size\": 16384         }     ],     \"isLast\": false,     \"nextPageToken\": \"g2gDZAAKbGlua190b2tlbmgCZAAMY2FjaGVkX3Rva2VuWgADY...\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_children(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the directory. (required)
        :param int limit: Allows specifying maximum number of files that should be returned. If there are more files, they can be retrieved using `token` query parameter. 
        :param str token: Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding `nextPageToken`. Cannot be provided alongside the `index` or `tune_for_large_continuous_listing` parameters. 
        :param str attribute: Name of attribute to be returned for each entry. Can be provided multiple times. When accessing a file via share mode, the following attributes are unavailable: `owner_id`, `storage_group_id`, `storage_user_id`, `provider_id`, `hardlinks_count`. If not provided, default attributes of `file_id` and `name` will be returned. 
        :param str index: Determines the starting point for listing - it will be started from given file name (inclusively). Cannot be provided alongside the `token` parameter. 
        :param bool tune_for_large_continuous_listing: This option increases performance of listing large directories (with thousands of files) when using subsequent calls with paging tokens.<br/> **CAUTION!!** When enabled, there is no guarantee that changes in the file tree performed after the start of listing will be included. Therefore it shouldn't be used when the listing result is expected to be up to date with the state of the file tree at the moment of listing. It should be avoided if the interval between subsequent listings is longer than 10 seconds, otherwise the listing performance will be much worse.<br/> Overusing this option may cause a significant load on the Oneprovider.<br/> Cannot be provided alongside the `token` parameter. 
        :return: DirectoryChildren
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_children_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_children_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_children_with_http_info(self, id, **kwargs):  # noqa: E501
        """List directory files and subdirectories  # noqa: E501

        Returns the list of directory files and subdirectories for directory specified by [$DIR_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Get files in space subdirectory** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$DIR_ID/children?attribute=size&attribute=name&limit=2\"  {     \"children\": [         {              \"name\": File1.txt             \"size\": 1024         },         {              \"name\": File2.txt             \"size\": 16384         }     ],     \"isLast\": false,     \"nextPageToken\": \"g2gDZAAKbGlua190b2tlbmgCZAAMY2FjaGVkX3Rva2VuWgADY...\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_children_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the directory. (required)
        :param int limit: Allows specifying maximum number of files that should be returned. If there are more files, they can be retrieved using `token` query parameter. 
        :param str token: Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding `nextPageToken`. Cannot be provided alongside the `index` or `tune_for_large_continuous_listing` parameters. 
        :param str attribute: Name of attribute to be returned for each entry. Can be provided multiple times. When accessing a file via share mode, the following attributes are unavailable: `owner_id`, `storage_group_id`, `storage_user_id`, `provider_id`, `hardlinks_count`. If not provided, default attributes of `file_id` and `name` will be returned. 
        :param str index: Determines the starting point for listing - it will be started from given file name (inclusively). Cannot be provided alongside the `token` parameter. 
        :param bool tune_for_large_continuous_listing: This option increases performance of listing large directories (with thousands of files) when using subsequent calls with paging tokens.<br/> **CAUTION!!** When enabled, there is no guarantee that changes in the file tree performed after the start of listing will be included. Therefore it shouldn't be used when the listing result is expected to be up to date with the state of the file tree at the moment of listing. It should be avoided if the interval between subsequent listings is longer than 10 seconds, otherwise the listing performance will be much worse.<br/> Overusing this option may cause a significant load on the Oneprovider.<br/> Cannot be provided alongside the `token` parameter. 
        :return: DirectoryChildren
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'limit', 'token', 'attribute', 'index', 'tune_for_large_continuous_listing']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_children" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_children`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501
        if 'attribute' in params:
            if isinstance(params['attribute'], list) or isinstance(params['attribute'], tuple):
                for param in params['attribute']:
                    query_params.append(('attribute', param))  # noqa: E501
            else:
                query_params.append(('attribute', params['attribute']))  # noqa: E501

        if 'index' in params:
            query_params.append(('index', params['index']))  # noqa: E501
        if 'tune_for_large_continuous_listing' in params:
            query_params.append(('tune_for_large_continuous_listing', params['tune_for_large_continuous_listing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}/children', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirectoryChildren',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_files_recursively(self, id, **kwargs):  # noqa: E501
        """List files recursively  # noqa: E501

        Recursively lists non-directory files (i.e regular files, symbolic links and hardlinks) in directory specified by [$DIR_ID](#operation/lookup_file_id) (listing root). Files are listed in lexicographical order by their paths, which are relative to the listing root directory. If there is no access to specified directory, its own relative path (`\".\"`) will be included in the `inaccessiblePaths` field and the listing result (i.e. `files` field) will be empty.  ***Example cURL requests***  **List files recursively** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$DIR_ID/files?start_after=ParentDirName/Dir1\"  {     \"files\": [         {             \"file_id\": \"FILE_ID1\",             \"path\": \"ParentDirName/Dir2\"         },         {             \"file_id\": \"FILE_ID2\",             \"path\": \"ParentDirName/File1.txt\"         },     ],     \"inaccessiblePaths\": [         \"ParentDirName/Dir3\"     ],     \"isLast\": false,     \"nextPageToken\": \"$PAGING_TOKEN\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_files_recursively(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the directory. (required)
        :param int limit: Specifies the maximum number of entries that can be returned in one result batch. If there are more files, they can be retrieved using options that specify a custom starting point. 
        :param str token: Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding `nextPageToken`. Cannot be provided alongside the `start_after` parameter. 
        :param str start_after: Determines the starting point for listing - it will be started from the first file path lexicographically larger than the provided path. 
        :param str prefix: Only files with paths that begin with this value will be listed. 
        :param str attribute: Name of attribute to be returned for each entry. Can be provided multiple times. When accessing a file via share mode, the following attributes are unavailable: `owner_id`, `storage_group_id`, `storage_user_id`, `provider_id`, `hardlinks_count`. If not provided, default attributes of `file_id` and `path` will be returned. 
        :return: RecursiveFileList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_files_recursively_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_files_recursively_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_files_recursively_with_http_info(self, id, **kwargs):  # noqa: E501
        """List files recursively  # noqa: E501

        Recursively lists non-directory files (i.e regular files, symbolic links and hardlinks) in directory specified by [$DIR_ID](#operation/lookup_file_id) (listing root). Files are listed in lexicographical order by their paths, which are relative to the listing root directory. If there is no access to specified directory, its own relative path (`\".\"`) will be included in the `inaccessiblePaths` field and the listing result (i.e. `files` field) will be empty.  ***Example cURL requests***  **List files recursively** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$DIR_ID/files?start_after=ParentDirName/Dir1\"  {     \"files\": [         {             \"file_id\": \"FILE_ID1\",             \"path\": \"ParentDirName/Dir2\"         },         {             \"file_id\": \"FILE_ID2\",             \"path\": \"ParentDirName/File1.txt\"         },     ],     \"inaccessiblePaths\": [         \"ParentDirName/Dir3\"     ],     \"isLast\": false,     \"nextPageToken\": \"$PAGING_TOKEN\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_files_recursively_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the directory. (required)
        :param int limit: Specifies the maximum number of entries that can be returned in one result batch. If there are more files, they can be retrieved using options that specify a custom starting point. 
        :param str token: Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding `nextPageToken`. Cannot be provided alongside the `start_after` parameter. 
        :param str start_after: Determines the starting point for listing - it will be started from the first file path lexicographically larger than the provided path. 
        :param str prefix: Only files with paths that begin with this value will be listed. 
        :param str attribute: Name of attribute to be returned for each entry. Can be provided multiple times. When accessing a file via share mode, the following attributes are unavailable: `owner_id`, `storage_group_id`, `storage_user_id`, `provider_id`, `hardlinks_count`. If not provided, default attributes of `file_id` and `path` will be returned. 
        :return: RecursiveFileList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'limit', 'token', 'start_after', 'prefix', 'attribute']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_files_recursively" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_files_recursively`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501
        if 'start_after' in params:
            query_params.append(('start_after', params['start_after']))  # noqa: E501
        if 'prefix' in params:
            query_params.append(('prefix', params['prefix']))  # noqa: E501
        if 'attribute' in params:
            if isinstance(params['attribute'], list) or isinstance(params['attribute'], tuple):
                for param in params['attribute']:
                    query_params.append(('attribute', param))  # noqa: E501
            else:
                query_params.append(('attribute', params['attribute']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}/files', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RecursiveFileList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_file(self, id, **kwargs):  # noqa: E501
        """Remove file  # noqa: E501

        Removes file specified by [$FILE_ID](#operation/lookup_file_id). In case of a directory, all its children are recursively removed - note that the operation will fail part-way if the client does not have permissions to remove some of the nested files/directories.  ***Example cURL requests***  **Remove specific file** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID\" ``` See also [Remove file at path](#operation/remove_file_at_path).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_file(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: File or directory Id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_file_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_file_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def remove_file_with_http_info(self, id, **kwargs):  # noqa: E501
        """Remove file  # noqa: E501

        Removes file specified by [$FILE_ID](#operation/lookup_file_id). In case of a directory, all its children are recursively removed - note that the operation will fail part-way if the client does not have permissions to remove some of the nested files/directories.  ***Example cURL requests***  **Remove specific file** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID\" ``` See also [Remove file at path](#operation/remove_file_at_path).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_file_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: File or directory Id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_file_at_path(self, id, path, **kwargs):  # noqa: E501
        """Remove file at path  # noqa: E501

        Removes file by path specified in the URL, relative to the base directory given in the `id` parameter (see the parameter description for details).  In case of a directory, all its children are recursively removed - note that the operation will fail part-way if the client does not have permissions to remove some of the nested files/directories.  ***Example cURL requests***  **Remove specific file** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/dir1/file.txt\" ```  See also [Remove file by ID](#operation/remove_file).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_file_at_path(id, path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the base directory, relative to which the path remainder will be resolved. It can be a **Space Id** (in which case the space root directory is taken), or a **File Id** of any existing directory (including the space root directory). See [Data](#section/Overview/Data-management-basics) section for more information.  (required)
        :param str path: Path relative to the base directory (specified in the id parameter). (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_file_at_path_with_http_info(id, path, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_file_at_path_with_http_info(id, path, **kwargs)  # noqa: E501
            return data

    def remove_file_at_path_with_http_info(self, id, path, **kwargs):  # noqa: E501
        """Remove file at path  # noqa: E501

        Removes file by path specified in the URL, relative to the base directory given in the `id` parameter (see the parameter description for details).  In case of a directory, all its children are recursively removed - note that the operation will fail part-way if the client does not have permissions to remove some of the nested files/directories.  ***Example cURL requests***  **Remove specific file** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_OR_PARENT_ID/path/dir1/file.txt\" ```  See also [Remove file by ID](#operation/remove_file).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_file_at_path_with_http_info(id, path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the base directory, relative to which the path remainder will be resolved. It can be a **Space Id** (in which case the space root directory is taken), or a **File Id** of any existing directory (including the space root directory). See [Data](#section/Overview/Data-management-basics) section for more information.  (required)
        :param str path: Path relative to the base directory (specified in the id parameter). (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'path']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_file_at_path" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_file_at_path`")  # noqa: E501
        # verify the required parameter 'path' is set
        if ('path' not in params or
                params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `remove_file_at_path`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'path' in params:
            path_params['path'] = params['path']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}/path/{path}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_attr(self, id, **kwargs):  # noqa: E501
        """Set file attribute  # noqa: E501

        This method allows to set a value of a regular file attribute for a file specified by [$FILE_ID](#operation/lookup_file_id).  Currently only POSIX mode can be changed by sending: ``` { \"mode\": \"0777\" } ``` where the POSIX mode is specified in octal notation.  ***Example cURL requests***  **Set file POSIX mode** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X PUT \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID\" \\ -H 'Content-Type: application/json' -d '{ \"mode\": \"0777\" }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_attr(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: File, directory or space Id (required)
        :param dict(str, str) body: Attribute name and value.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_attr_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_attr_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def set_attr_with_http_info(self, id, **kwargs):  # noqa: E501
        """Set file attribute  # noqa: E501

        This method allows to set a value of a regular file attribute for a file specified by [$FILE_ID](#operation/lookup_file_id).  Currently only POSIX mode can be changed by sending: ``` { \"mode\": \"0777\" } ``` where the POSIX mode is specified in octal notation.  ***Example cURL requests***  **Set file POSIX mode** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X PUT \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID\" \\ -H 'Content-Type: application/json' -d '{ \"mode\": \"0777\" }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_attr_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: File, directory or space Id (required)
        :param dict(str, str) body: Attribute name and value.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_attr" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `set_attr`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def test_for_hardlink_between_files(self, id, hid, **kwargs):  # noqa: E501
        """Test for hard link between files  # noqa: E501

        Checks whether one file is a hard link to the other one. Both files are specified by [$FILE_ID](#operation/lookup_file_id). The relation is symmetric; the order of the files in the URL does not matter.  **Test for hard link between files** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID1/hardlinks/$FILE_ID2\"  # return code = 0 (HTTP code = 204) -> true # return code != 0 (HTTP code = 404) -> false ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.test_for_hardlink_between_files(id, hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: First File Id. (required)
        :param str hid: Second File Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.test_for_hardlink_between_files_with_http_info(id, hid, **kwargs)  # noqa: E501
        else:
            (data) = self.test_for_hardlink_between_files_with_http_info(id, hid, **kwargs)  # noqa: E501
            return data

    def test_for_hardlink_between_files_with_http_info(self, id, hid, **kwargs):  # noqa: E501
        """Test for hard link between files  # noqa: E501

        Checks whether one file is a hard link to the other one. Both files are specified by [$FILE_ID](#operation/lookup_file_id). The relation is symmetric; the order of the files in the URL does not matter.  **Test for hard link between files** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID1/hardlinks/$FILE_ID2\"  # return code = 0 (HTTP code = 204) -> true # return code != 0 (HTTP code = 404) -> false ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.test_for_hardlink_between_files_with_http_info(id, hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: First File Id. (required)
        :param str hid: Second File Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'hid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method test_for_hardlink_between_files" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `test_for_hardlink_between_files`")  # noqa: E501
        # verify the required parameter 'hid' is set
        if ('hid' not in params or
                params['hid'] is None):
            raise ValueError("Missing the required parameter `hid` when calling `test_for_hardlink_between_files`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'hid' in params:
            path_params['hid'] = params['hid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}/hardlinks/{hid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_file_content(self, id, **kwargs):  # noqa: E501
        """Update file content  # noqa: E501

        Updates content of file specified by [$FILE_ID](#operation/lookup_file_id).  The file must exist beforehand, otherwise the operation fails with an error.  The `offset` query parameter can be used to start writing from a certain byte in the file, in such case the file is NOT truncated (bytes beyond the overwritten fragment will be preserved). If no `offset` query is given, the file is truncated  and the previous file content is completely overwritten.  ***Example cURL requests***  **Update file content starting from specified offset:** ```bash # originally, the file content is  \"abcdefghijklmno\"  curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/content?offset=4\" \\ -H \"Content-Type: application/octet-stream\" -d \"WXYZ\"  # upon success, the file content is \"abcdWXYZijklmno\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_file_content(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the file. (required)
        :param Object body: File content to be written at specified offset.
        :param int offset: Offset at which the data sent as request body will be written to the file. If not specified, the file will be completely overwritten. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_file_content_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_file_content_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def update_file_content_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update file content  # noqa: E501

        Updates content of file specified by [$FILE_ID](#operation/lookup_file_id).  The file must exist beforehand, otherwise the operation fails with an error.  The `offset` query parameter can be used to start writing from a certain byte in the file, in such case the file is NOT truncated (bytes beyond the overwritten fragment will be preserved). If no `offset` query is given, the file is truncated  and the previous file content is completely overwritten.  ***Example cURL requests***  **Update file content starting from specified offset:** ```bash # originally, the file content is  \"abcdefghijklmno\"  curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/content?offset=4\" \\ -H \"Content-Type: application/octet-stream\" -d \"WXYZ\"  # upon success, the file content is \"abcdWXYZijklmno\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_file_content_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the file. (required)
        :param Object body: File content to be written at specified offset.
        :param int offset: Offset at which the data sent as request body will be written to the file. If not specified, the file will be completely overwritten. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_file_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_file_content`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}/content', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
