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


class ArchiveApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_archive_recall(self, id, **kwargs):  # noqa: E501
        """Cancel an archive recall  # noqa: E501

        Cancels an ongoing archive recall, identified by the root [FILE_ID] to which the archive  is being recalled.  **Cancel archive recall** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/recall/cancel\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_archive_recall(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: File Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_archive_recall_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_archive_recall_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def cancel_archive_recall_with_http_info(self, id, **kwargs):  # noqa: E501
        """Cancel an archive recall  # noqa: E501

        Cancels an ongoing archive recall, identified by the root [FILE_ID] to which the archive  is being recalled.  **Cancel archive recall** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/recall/cancel\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_archive_recall_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: File Id. (required)
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
                    " to method cancel_archive_recall" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `cancel_archive_recall`")  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}/recall/cancel', 'POST',
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

    def create_archive(self, body, **kwargs):  # noqa: E501
        """Create archive from a dataset  # noqa: E501

        Creates an archive of a dataset - a snapshot of its data and metadata.  This operation requires `space_manage_datasets` and `space_create_archives` privileges.  ***Example cURL requests***  **Create archive from a dataset** <!--- TODO VFS-7616 add metadata structure to the example-->  ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/archives\" \\ -H \"Content-Type: application/json\" -d '{     \"datasetId\": \"'$DATASET_ID'\",     \"config\": {         \"incremental\": {\"enabled\": true},         \"includeDip\": false,         \"layout\": \"bagit\",         \"createNestedArchives\": true,         \"followSymlinks\": true     },     \"preservedCallback\": \"https://example.org/preserved_archives\",     \"deletedCallback\": \"https://example.org/deleted_archives\",     \"description\": \"Archived dataset with experiment data from 2021.\" }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_archive(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ArchiveCreateRequest body: Dataset properties. (required)
        :return: InlineResponse2017
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_archive_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_archive_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_archive_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create archive from a dataset  # noqa: E501

        Creates an archive of a dataset - a snapshot of its data and metadata.  This operation requires `space_manage_datasets` and `space_create_archives` privileges.  ***Example cURL requests***  **Create archive from a dataset** <!--- TODO VFS-7616 add metadata structure to the example-->  ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/archives\" \\ -H \"Content-Type: application/json\" -d '{     \"datasetId\": \"'$DATASET_ID'\",     \"config\": {         \"incremental\": {\"enabled\": true},         \"includeDip\": false,         \"layout\": \"bagit\",         \"createNestedArchives\": true,         \"followSymlinks\": true     },     \"preservedCallback\": \"https://example.org/preserved_archives\",     \"deletedCallback\": \"https://example.org/deleted_archives\",     \"description\": \"Archived dataset with experiment data from 2021.\" }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_archive_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ArchiveCreateRequest body: Dataset properties. (required)
        :return: InlineResponse2017
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_archive" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_archive`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/archives', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2017',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_archive(self, aid, **kwargs):  # noqa: E501
        """Delete archive  # noqa: E501

        Initializes process of purging an archive. First, the archived data is deleted from the storage, then all the information concerning the archive is deleted. The process may be time consuming therefore it is possible to pass callback URL on which the POST request will be performed to notify that the process has finished. The callback request will include JSON `{\"archiveId\": $ARCHIVE_ID}` as a body to determine which archive has been deleted.  This operation requires `space_manage_datasets` and `space_remove_archives` privileges.  ***Example cURL requests***  **Delete archive** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/archives/$ARCHIVE_ID/delete\" \\ -H \"Content-Type: application/json\" -d '{     \"deletedCallback\": \"https://example.org/deleted_archives\" }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_archive(aid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str aid: Id of a specific archive to be deleted. (required)
        :param ArchiveDeleteRequest body: Parameters for initializing purging of an archive.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_archive_with_http_info(aid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_archive_with_http_info(aid, **kwargs)  # noqa: E501
            return data

    def delete_archive_with_http_info(self, aid, **kwargs):  # noqa: E501
        """Delete archive  # noqa: E501

        Initializes process of purging an archive. First, the archived data is deleted from the storage, then all the information concerning the archive is deleted. The process may be time consuming therefore it is possible to pass callback URL on which the POST request will be performed to notify that the process has finished. The callback request will include JSON `{\"archiveId\": $ARCHIVE_ID}` as a body to determine which archive has been deleted.  This operation requires `space_manage_datasets` and `space_remove_archives` privileges.  ***Example cURL requests***  **Delete archive** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/archives/$ARCHIVE_ID/delete\" \\ -H \"Content-Type: application/json\" -d '{     \"deletedCallback\": \"https://example.org/deleted_archives\" }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_archive_with_http_info(aid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str aid: Id of a specific archive to be deleted. (required)
        :param ArchiveDeleteRequest body: Parameters for initializing purging of an archive.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_archive" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aid' is set
        if ('aid' not in params or
                params['aid'] is None):
            raise ValueError("Missing the required parameter `aid` when calling `delete_archive`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'aid' in params:
            path_params['aid'] = params['aid']  # noqa: E501

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
            '/archives/{aid}/delete', 'POST',
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

    def get_archive(self, aid, **kwargs):  # noqa: E501
        """Get archive information  # noqa: E501

        Returns the basic information about an archive.  This operation requires `space_view_archives` privilege.  ***Example cURL requests***  **Get the basic information about archive** <!--- TODO VFS-7616 add metadata structure to the example-->  ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/archives/$ARCHIVE_ID\"  {     \"archiveId\": \"ae6f78c89a97c9e78e891105f703bcb8\",     \"state\": \"preserved\",     \"datasetId\": \"1f4b762b1380946e73aeca574c77f14c\",     \"rootDirectoryId\": \"00000000006CB663736861726547756964233339643236366165646365\",     \"creationTime\": 1576152793,     \"config\": {       \"incremental\": {\"enabled\": true},       \"includeDip\": false,       \"layout\": \"bagit\",     },     \"preservedCallback\": \"https://example.org/preserved_archives\",     \"deletedCallback\": null,     \"description\": \"Archived dataset with experiment data from 2021.\",     \"stats\": {         \"filesArchived\": 7940,         \"filesFailed\": 3,         \"bytesArchived\": 879245378924537     },     \"baseArchiveId\": \"ae6f78c89a97c9e78e891105f703bcb8\",     \"relatedAipId\": \"e891105f703bcb8ae6f78c89a97c9e78\",     \"relatedDipId\": \"78e891105f703bcb8ae6f78c89a97c9e\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_archive(aid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str aid: Archive Id (required)
        :return: Archive
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_archive_with_http_info(aid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_archive_with_http_info(aid, **kwargs)  # noqa: E501
            return data

    def get_archive_with_http_info(self, aid, **kwargs):  # noqa: E501
        """Get archive information  # noqa: E501

        Returns the basic information about an archive.  This operation requires `space_view_archives` privilege.  ***Example cURL requests***  **Get the basic information about archive** <!--- TODO VFS-7616 add metadata structure to the example-->  ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/archives/$ARCHIVE_ID\"  {     \"archiveId\": \"ae6f78c89a97c9e78e891105f703bcb8\",     \"state\": \"preserved\",     \"datasetId\": \"1f4b762b1380946e73aeca574c77f14c\",     \"rootDirectoryId\": \"00000000006CB663736861726547756964233339643236366165646365\",     \"creationTime\": 1576152793,     \"config\": {       \"incremental\": {\"enabled\": true},       \"includeDip\": false,       \"layout\": \"bagit\",     },     \"preservedCallback\": \"https://example.org/preserved_archives\",     \"deletedCallback\": null,     \"description\": \"Archived dataset with experiment data from 2021.\",     \"stats\": {         \"filesArchived\": 7940,         \"filesFailed\": 3,         \"bytesArchived\": 879245378924537     },     \"baseArchiveId\": \"ae6f78c89a97c9e78e891105f703bcb8\",     \"relatedAipId\": \"e891105f703bcb8ae6f78c89a97c9e78\",     \"relatedDipId\": \"78e891105f703bcb8ae6f78c89a97c9e\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_archive_with_http_info(aid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str aid: Archive Id (required)
        :return: Archive
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_archive" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aid' is set
        if ('aid' not in params or
                params['aid'] is None):
            raise ValueError("Missing the required parameter `aid` when calling `get_archive`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'aid' in params:
            path_params['aid'] = params['aid']  # noqa: E501

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
            '/archives/{aid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Archive',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_archive_recall_details(self, id, **kwargs):  # noqa: E501
        """Get details of an archive recall  # noqa: E501

        If this file is a root of a past or ongoing archive recall, returns its details. Otherwise,  returns `404 NOT FOUND` error.  **Get archive recall details** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/recall/details\"  {     \"archiveId\": \"$ARCHIVE_ID\",     \"datasetId\": \"$DATASET_ID\",     \"startTime\": 1643103923417,     \"finishTime\": 1643103933417,     \"totalFileCount\" : 1,     \"totalByteSize\": 65536,     \"lastError\": {         \"fileId\": \"$FILE_ID\",         \"reason\": {           \"description\": \"The resource could not be found.\",           \"id\": \"notFound\"         }     } } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_archive_recall_details(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: File Id. (required)
        :return: ArchiveRecallDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_archive_recall_details_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_archive_recall_details_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_archive_recall_details_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get details of an archive recall  # noqa: E501

        If this file is a root of a past or ongoing archive recall, returns its details. Otherwise,  returns `404 NOT FOUND` error.  **Get archive recall details** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/recall/details\"  {     \"archiveId\": \"$ARCHIVE_ID\",     \"datasetId\": \"$DATASET_ID\",     \"startTime\": 1643103923417,     \"finishTime\": 1643103933417,     \"totalFileCount\" : 1,     \"totalByteSize\": 65536,     \"lastError\": {         \"fileId\": \"$FILE_ID\",         \"reason\": {           \"description\": \"The resource could not be found.\",           \"id\": \"notFound\"         }     } } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_archive_recall_details_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: File Id. (required)
        :return: ArchiveRecallDetails
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
                    " to method get_archive_recall_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_archive_recall_details`")  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}/recall/details', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArchiveRecallDetails',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_archive_recall_progress(self, id, **kwargs):  # noqa: E501
        """Get progress of an archive recall  # noqa: E501

        If this file is a root of a past or ongoing archive recall, returns its progress. Otherwise,  returns `404 NOT FOUND` error. This resource is only available on the Oneprovider performing the recall.  **Get archive recall progress** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/recall/progress\"  {     \"filesCopied\": 8,     \"bytesCopied\": 16384,     \"filesFailed\": 1 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_archive_recall_progress(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: File Id. (required)
        :return: ArchiveRecallProgress
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_archive_recall_progress_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_archive_recall_progress_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_archive_recall_progress_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get progress of an archive recall  # noqa: E501

        If this file is a root of a past or ongoing archive recall, returns its progress. Otherwise,  returns `404 NOT FOUND` error. This resource is only available on the Oneprovider performing the recall.  **Get archive recall progress** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/recall/progress\"  {     \"filesCopied\": 8,     \"bytesCopied\": 16384,     \"filesFailed\": 1 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_archive_recall_progress_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: File Id. (required)
        :return: ArchiveRecallProgress
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
                    " to method get_archive_recall_progress" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_archive_recall_progress`")  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}/recall/progress', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArchiveRecallProgress',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_dataset_archives(self, did, **kwargs):  # noqa: E501
        """List archives of a dataset  # noqa: E501

        Returns the list of archives created from a specific dataset.  This operation requires `space_view_archives` privilege.  ***Example cURL requests***  **List dataset archives** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/datasets/$DATASET_ID/archives\"  {     \"archives\": [\"d0f08b098804da5504609b2c54b507b3\", \"5a1e63f7cf5282a206144f77822c3f10\"],     \"nextPageToken\": \"UkdseU1qWTBNak16TXpNNU5qUXpNak0yTXpZMk1UWTFOalEyTXpZMU5qSTJOalky\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_dataset_archives(did, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str did: Dataset Id (required)
        :param int limit: Allows specifying maximum number of entries that should be returned. If there are more archives, they can be retrieved using `offset` or `token` query parameters. 
        :param int offset: Offset determining beginning of the list of archives returned in the response. Expressed in number of entries, further adjusts the starting point of listing indicated by `token` parameter. The value can be negative, in such case entries preceding the starting point will be returned. 
        :param str token: Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding `nextPageToken`. 
        :return: Archives
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_dataset_archives_with_http_info(did, **kwargs)  # noqa: E501
        else:
            (data) = self.list_dataset_archives_with_http_info(did, **kwargs)  # noqa: E501
            return data

    def list_dataset_archives_with_http_info(self, did, **kwargs):  # noqa: E501
        """List archives of a dataset  # noqa: E501

        Returns the list of archives created from a specific dataset.  This operation requires `space_view_archives` privilege.  ***Example cURL requests***  **List dataset archives** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/datasets/$DATASET_ID/archives\"  {     \"archives\": [\"d0f08b098804da5504609b2c54b507b3\", \"5a1e63f7cf5282a206144f77822c3f10\"],     \"nextPageToken\": \"UkdseU1qWTBNak16TXpNNU5qUXpNak0yTXpZMk1UWTFOalEyTXpZMU5qSTJOalky\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_dataset_archives_with_http_info(did, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str did: Dataset Id (required)
        :param int limit: Allows specifying maximum number of entries that should be returned. If there are more archives, they can be retrieved using `offset` or `token` query parameters. 
        :param int offset: Offset determining beginning of the list of archives returned in the response. Expressed in number of entries, further adjusts the starting point of listing indicated by `token` parameter. The value can be negative, in such case entries preceding the starting point will be returned. 
        :param str token: Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding `nextPageToken`. 
        :return: Archives
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['did', 'limit', 'offset', 'token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_dataset_archives" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'did' is set
        if ('did' not in params or
                params['did'] is None):
            raise ValueError("Missing the required parameter `did` when calling `list_dataset_archives`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'did' in params:
            path_params['did'] = params['did']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501

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
            '/datasets/{did}/archives', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Archives',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def recall_archive(self, body, aid, **kwargs):  # noqa: E501
        """Recall archive  # noqa: E501

        Initializes process of recalling an archive. The recall creates a copy of the archive content in specified destination.  This operation requires `space_recall_archives` privilege.  ***Example cURL requests***  **Recall archive** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/archives/$ARCHIVE_ID/recall\" \\ -H \"Content-Type: application/json\" -d '{     \"parentDirectoryId\": \"$PARENT_DIRECTORY_ID\",     \"targetFileName\": \"example_name\" }'  {     \"rootFileId\": \"$ROOT_FILE_ID\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.recall_archive(body, aid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ArchiveRecallRequest body: Parameters for initializing recall of an archive. (required)
        :param str aid: Id of a specific archive to be recalled. (required)
        :return: ArchiveRecallResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.recall_archive_with_http_info(body, aid, **kwargs)  # noqa: E501
        else:
            (data) = self.recall_archive_with_http_info(body, aid, **kwargs)  # noqa: E501
            return data

    def recall_archive_with_http_info(self, body, aid, **kwargs):  # noqa: E501
        """Recall archive  # noqa: E501

        Initializes process of recalling an archive. The recall creates a copy of the archive content in specified destination.  This operation requires `space_recall_archives` privilege.  ***Example cURL requests***  **Recall archive** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/archives/$ARCHIVE_ID/recall\" \\ -H \"Content-Type: application/json\" -d '{     \"parentDirectoryId\": \"$PARENT_DIRECTORY_ID\",     \"targetFileName\": \"example_name\" }'  {     \"rootFileId\": \"$ROOT_FILE_ID\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.recall_archive_with_http_info(body, aid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ArchiveRecallRequest body: Parameters for initializing recall of an archive. (required)
        :param str aid: Id of a specific archive to be recalled. (required)
        :return: ArchiveRecallResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'aid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method recall_archive" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `recall_archive`")  # noqa: E501
        # verify the required parameter 'aid' is set
        if ('aid' not in params or
                params['aid'] is None):
            raise ValueError("Missing the required parameter `aid` when calling `recall_archive`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'aid' in params:
            path_params['aid'] = params['aid']  # noqa: E501

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
            '/archives/{aid}/recall', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArchiveRecallResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_archive(self, body, aid, **kwargs):  # noqa: E501
        """Update archive  # noqa: E501

        Changes archive properties.  This operation requires `space_manage_datasets` and `space_create_archives` privileges.  ***Example cURL requests***  **Change archive description and callbacks** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X PATCH \"https://$PROVIDER_HOST/api/v3/oneprovider/archives/$ARCHIVE_ID\" \\ -H \"Content-Type: application/json\" -d '{     \"description\": \"New archive description\",     \"preservedCallback\": \"https://archives.org/preserved_archives\",     \"deletedCallback\": \"https://archives.org/deleted_archives\" }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_archive(body, aid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ArchiveUpdateRequest body: Archive properties (required)
        :param str aid: Archive Id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_archive_with_http_info(body, aid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_archive_with_http_info(body, aid, **kwargs)  # noqa: E501
            return data

    def update_archive_with_http_info(self, body, aid, **kwargs):  # noqa: E501
        """Update archive  # noqa: E501

        Changes archive properties.  This operation requires `space_manage_datasets` and `space_create_archives` privileges.  ***Example cURL requests***  **Change archive description and callbacks** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X PATCH \"https://$PROVIDER_HOST/api/v3/oneprovider/archives/$ARCHIVE_ID\" \\ -H \"Content-Type: application/json\" -d '{     \"description\": \"New archive description\",     \"preservedCallback\": \"https://archives.org/preserved_archives\",     \"deletedCallback\": \"https://archives.org/deleted_archives\" }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_archive_with_http_info(body, aid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ArchiveUpdateRequest body: Archive properties (required)
        :param str aid: Archive Id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'aid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_archive" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_archive`")  # noqa: E501
        # verify the required parameter 'aid' is set
        if ('aid' not in params or
                params['aid'] is None):
            raise ValueError("Missing the required parameter `aid` when calling `update_archive`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'aid' in params:
            path_params['aid'] = params['aid']  # noqa: E501

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
            '/archives/{aid}', 'PATCH',
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
