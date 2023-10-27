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


class DatasetApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def establish_dataset(self, body, **kwargs):  # noqa: E501
        """Establish dataset  # noqa: E501

        Establishes a dataset with the specified file/directory as the dataset's root. For each file/directory, only one dataset can be established.  This operation requires `space_manage_datasets` privilege.  ***Example cURL requests***  **Establish dataset** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/datasets\" \\ -H \"Content-Type: application/json\" -d '{     \"rootFileId\": \"'$FILE_ID'\",     \"protectionFlags\": [\"data_protection\"] }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.establish_dataset(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DatasetEstablishRequest body: Dataset properties. (required)
        :return: InlineResponse2016
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.establish_dataset_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.establish_dataset_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def establish_dataset_with_http_info(self, body, **kwargs):  # noqa: E501
        """Establish dataset  # noqa: E501

        Establishes a dataset with the specified file/directory as the dataset's root. For each file/directory, only one dataset can be established.  This operation requires `space_manage_datasets` privilege.  ***Example cURL requests***  **Establish dataset** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/datasets\" \\ -H \"Content-Type: application/json\" -d '{     \"rootFileId\": \"'$FILE_ID'\",     \"protectionFlags\": [\"data_protection\"] }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.establish_dataset_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DatasetEstablishRequest body: Dataset properties. (required)
        :return: InlineResponse2016
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
                    " to method establish_dataset" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `establish_dataset`")  # noqa: E501

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
            '/datasets', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2016',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dataset(self, did, **kwargs):  # noqa: E501
        """Get dataset information  # noqa: E501

        Returns the basic information about a dataset.  ***Example cURL requests***  **Get the basic information about dataset** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/datasets/$DATASET_ID\"  {     \"state\": \"attached\",     \"datasetId\": \"1f4b762b1380946e73aeca574c77f14c\",     \"parentId\": null,     \"rootFileId\": \"00000000006CB663736861726547756964233339643236366165646365...\",     \"rootFileType\": \"DIR\",     \"rootFilePath\": \"/MySpace/dir\",     \"rootFileDeleted\": false,     \"protectionFlags\": [\"data_protection\"],     \"effectiveProtectionFlags\": [\"data_protection\", \"metadata_protection\"],     \"creationTime\": 1576152793,     \"archiveCount\": 5 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dataset(did, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str did: Dataset Id (required)
        :return: Dataset
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dataset_with_http_info(did, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dataset_with_http_info(did, **kwargs)  # noqa: E501
            return data

    def get_dataset_with_http_info(self, did, **kwargs):  # noqa: E501
        """Get dataset information  # noqa: E501

        Returns the basic information about a dataset.  ***Example cURL requests***  **Get the basic information about dataset** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/datasets/$DATASET_ID\"  {     \"state\": \"attached\",     \"datasetId\": \"1f4b762b1380946e73aeca574c77f14c\",     \"parentId\": null,     \"rootFileId\": \"00000000006CB663736861726547756964233339643236366165646365...\",     \"rootFileType\": \"DIR\",     \"rootFilePath\": \"/MySpace/dir\",     \"rootFileDeleted\": false,     \"protectionFlags\": [\"data_protection\"],     \"effectiveProtectionFlags\": [\"data_protection\", \"metadata_protection\"],     \"creationTime\": 1576152793,     \"archiveCount\": 5 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dataset_with_http_info(did, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str did: Dataset Id (required)
        :return: Dataset
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['did']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'did' is set
        if ('did' not in params or
                params['did'] is None):
            raise ValueError("Missing the required parameter `did` when calling `get_dataset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'did' in params:
            path_params['did'] = params['did']  # noqa: E501

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
            '/datasets/{did}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Dataset',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_file_dataset_summary(self, id, **kwargs):  # noqa: E501
        """Get dataset summary for file or directory  # noqa: E501

        Returns dataset summary for a file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Get file's dataset summary** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/dataset/summary\"  {     \"directDataset\": null,     \"effectiveAncestorDatasets\": [\"1f4b762b1380946e73aeca574c77f14c\", \"64233339643236366165646365626666\"],     \"effectiveProtectionFlags\": [\"data_protection\", \"metadata_protection\"] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_file_dataset_summary(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the file or directory. (required)
        :return: DatasetSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_file_dataset_summary_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_file_dataset_summary_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_file_dataset_summary_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get dataset summary for file or directory  # noqa: E501

        Returns dataset summary for a file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Get file's dataset summary** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/dataset/summary\"  {     \"directDataset\": null,     \"effectiveAncestorDatasets\": [\"1f4b762b1380946e73aeca574c77f14c\", \"64233339643236366165646365626666\"],     \"effectiveProtectionFlags\": [\"data_protection\", \"metadata_protection\"] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_file_dataset_summary_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the file or directory. (required)
        :return: DatasetSummary
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
                    " to method get_file_dataset_summary" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_file_dataset_summary`")  # noqa: E501

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
            '/data/{id}/dataset/summary', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DatasetSummary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_dataset_children(self, did, **kwargs):  # noqa: E501
        """List child datasets of a dataset  # noqa: E501

        Returns the list of child datasets of a specific dataset. The list of top datasets in a space can be acquired using [this endpoint](#operation/list_space_top_datasets).  ***Example cURL requests***  **List child datasets** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/datasets/$DATASET_ID/children\"  {     \"datasets\": [         {             \"datasetId\": \"1f4b762b1380946e73aeca574c77f14c\",             \"name\": \"File1.txt\"         },         {             \"datasetId\": \"64233339643236366165646365626666\",             \"name\": \"Dir2\"         }     ],     \"nextPageToken\": \"RGlyMjY0MjMzMzM5NjQzMjM2MzY2MTY1NjQ2MzY1NjI2NjY2\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_dataset_children(did, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str did: Dataset Id (required)
        :param int limit: Allows specifying maximum number of entries that should be returned. If there are more child datasets, they can be retrieved using `offset` or `token` query parameters. 
        :param int offset: Offset determining beginning of the list of datasets returned in the response. Expressed in number of entries, further adjusts the starting point of listing indicated by `index` or `token` parameters. The value can be negative, in such case entries preceding the starting point will be returned. 
        :param str index: Determines the starting point for listing. The listing will (inclusively) start from the first dataset whose name is lexicographically greater or equal to the specified index. Since the index may include characters that are not URL-safe, it should always be urlencoded. 
        :param str token: Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding `nextPageToken`. If both `token` and `index` are passed, the `token` prevails. 
        :return: Datasets
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_dataset_children_with_http_info(did, **kwargs)  # noqa: E501
        else:
            (data) = self.list_dataset_children_with_http_info(did, **kwargs)  # noqa: E501
            return data

    def list_dataset_children_with_http_info(self, did, **kwargs):  # noqa: E501
        """List child datasets of a dataset  # noqa: E501

        Returns the list of child datasets of a specific dataset. The list of top datasets in a space can be acquired using [this endpoint](#operation/list_space_top_datasets).  ***Example cURL requests***  **List child datasets** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/datasets/$DATASET_ID/children\"  {     \"datasets\": [         {             \"datasetId\": \"1f4b762b1380946e73aeca574c77f14c\",             \"name\": \"File1.txt\"         },         {             \"datasetId\": \"64233339643236366165646365626666\",             \"name\": \"Dir2\"         }     ],     \"nextPageToken\": \"RGlyMjY0MjMzMzM5NjQzMjM2MzY2MTY1NjQ2MzY1NjI2NjY2\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_dataset_children_with_http_info(did, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str did: Dataset Id (required)
        :param int limit: Allows specifying maximum number of entries that should be returned. If there are more child datasets, they can be retrieved using `offset` or `token` query parameters. 
        :param int offset: Offset determining beginning of the list of datasets returned in the response. Expressed in number of entries, further adjusts the starting point of listing indicated by `index` or `token` parameters. The value can be negative, in such case entries preceding the starting point will be returned. 
        :param str index: Determines the starting point for listing. The listing will (inclusively) start from the first dataset whose name is lexicographically greater or equal to the specified index. Since the index may include characters that are not URL-safe, it should always be urlencoded. 
        :param str token: Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding `nextPageToken`. If both `token` and `index` are passed, the `token` prevails. 
        :return: Datasets
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['did', 'limit', 'offset', 'index', 'token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_dataset_children" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'did' is set
        if ('did' not in params or
                params['did'] is None):
            raise ValueError("Missing the required parameter `did` when calling `list_dataset_children`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'did' in params:
            path_params['did'] = params['did']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'index' in params:
            query_params.append(('index', params['index']))  # noqa: E501
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
            '/datasets/{did}/children', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Datasets',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_space_top_datasets(self, sid, state, **kwargs):  # noqa: E501
        """List space top datasets  # noqa: E501

        Returns the list of space's top datasets - ones that do not have any parent dataset. In special case when dataset has been established for space root directory, there is only one top dataset.  Datasets in each space are divided into two separate trees based on their states: * `attached` - this tree represents the hierarchy of datasets, which corresponds   to the hierarchy of files in the space. It can be perceived as a \"compressed\"   file tree, containing only the nodes corresponding to files/directories marked   as a dataset. For example, dataset A is child of dataset B because   B's root directory is ancestor to A's root file and no directory between   them is a root of any attached dataset. Consequently, moving dataset's root file   to other location may change the dataset location in the tree.  * `detached` - this tree represents the hierarchy of datasets for the moment   of detachment and does not change when root files are moved. Individual   datasets from this tree can be reattached, causing the tree to be   restructured in specific cases.  ***Example cURL requests***  **List space top datasets** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/datasets?state=attached\"  {     \"datasets\": [         {             \"datasetId\": \"1f4b762b1380946e73aeca574c77f14c\",             \"name\": \"File1.txt\"         },         {             \"datasetId\": \"64233339643236366165646365626666\",             \"name\": \"Dir2\"         }     ],     \"nextPageToken\": \"RGlyMjY0MjMzMzM5NjQzMjM2MzY2MTY1NjQ2MzY1NjI2NjY2\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_space_top_datasets(sid, state, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id (required)
        :param str state: The dataset tree to list from. (required)
        :param int limit: Allows specifying maximum number of entries that should be returned. If there are more datasets, they can be retrieved using `offset` or `token` query parameters. 
        :param int offset: Offset determining beginning of the list of datasets returned in the response. Expressed in number of entries, further adjusts the starting point of listing indicated by `index` or `token` parameters. The value can be negative, in such case entries preceding the starting point will be returned. 
        :param str index: Determines the starting point for listing. The listing will (inclusively) start from the first dataset whose name is lexicographically greater or equal to the specified index. Since the index may include characters that are not URL-safe, it should always be urlencoded. 
        :param str token: Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding `nextPageToken`. If both `token` and `index` are passed, the `token` prevails. 
        :return: Datasets
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_space_top_datasets_with_http_info(sid, state, **kwargs)  # noqa: E501
        else:
            (data) = self.list_space_top_datasets_with_http_info(sid, state, **kwargs)  # noqa: E501
            return data

    def list_space_top_datasets_with_http_info(self, sid, state, **kwargs):  # noqa: E501
        """List space top datasets  # noqa: E501

        Returns the list of space's top datasets - ones that do not have any parent dataset. In special case when dataset has been established for space root directory, there is only one top dataset.  Datasets in each space are divided into two separate trees based on their states: * `attached` - this tree represents the hierarchy of datasets, which corresponds   to the hierarchy of files in the space. It can be perceived as a \"compressed\"   file tree, containing only the nodes corresponding to files/directories marked   as a dataset. For example, dataset A is child of dataset B because   B's root directory is ancestor to A's root file and no directory between   them is a root of any attached dataset. Consequently, moving dataset's root file   to other location may change the dataset location in the tree.  * `detached` - this tree represents the hierarchy of datasets for the moment   of detachment and does not change when root files are moved. Individual   datasets from this tree can be reattached, causing the tree to be   restructured in specific cases.  ***Example cURL requests***  **List space top datasets** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/datasets?state=attached\"  {     \"datasets\": [         {             \"datasetId\": \"1f4b762b1380946e73aeca574c77f14c\",             \"name\": \"File1.txt\"         },         {             \"datasetId\": \"64233339643236366165646365626666\",             \"name\": \"Dir2\"         }     ],     \"nextPageToken\": \"RGlyMjY0MjMzMzM5NjQzMjM2MzY2MTY1NjQ2MzY1NjI2NjY2\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_space_top_datasets_with_http_info(sid, state, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id (required)
        :param str state: The dataset tree to list from. (required)
        :param int limit: Allows specifying maximum number of entries that should be returned. If there are more datasets, they can be retrieved using `offset` or `token` query parameters. 
        :param int offset: Offset determining beginning of the list of datasets returned in the response. Expressed in number of entries, further adjusts the starting point of listing indicated by `index` or `token` parameters. The value can be negative, in such case entries preceding the starting point will be returned. 
        :param str index: Determines the starting point for listing. The listing will (inclusively) start from the first dataset whose name is lexicographically greater or equal to the specified index. Since the index may include characters that are not URL-safe, it should always be urlencoded. 
        :param str token: Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding `nextPageToken`. If both `token` and `index` are passed, the `token` prevails. 
        :return: Datasets
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sid', 'state', 'limit', 'offset', 'index', 'token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_space_top_datasets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `list_space_top_datasets`")  # noqa: E501
        # verify the required parameter 'state' is set
        if ('state' not in params or
                params['state'] is None):
            raise ValueError("Missing the required parameter `state` when calling `list_space_top_datasets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sid' in params:
            path_params['sid'] = params['sid']  # noqa: E501

        query_params = []
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'index' in params:
            query_params.append(('index', params['index']))  # noqa: E501
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
            '/spaces/{sid}/datasets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Datasets',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_dataset(self, did, **kwargs):  # noqa: E501
        """Remove dataset  # noqa: E501

        Removes a specific dataset. This procedure does not modify any files or directories that were a part of the dataset. <!--- TODO VFS-7304 Add information that datasets can be deleted only if they have no archives -->  This operation requires `space_manage_datasets` privilege.  ***Example cURL requests***  **Remove dataset** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/datasets/$DATASET_ID\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_dataset(did, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str did: Dataset Id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_dataset_with_http_info(did, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_dataset_with_http_info(did, **kwargs)  # noqa: E501
            return data

    def remove_dataset_with_http_info(self, did, **kwargs):  # noqa: E501
        """Remove dataset  # noqa: E501

        Removes a specific dataset. This procedure does not modify any files or directories that were a part of the dataset. <!--- TODO VFS-7304 Add information that datasets can be deleted only if they have no archives -->  This operation requires `space_manage_datasets` privilege.  ***Example cURL requests***  **Remove dataset** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/datasets/$DATASET_ID\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_dataset_with_http_info(did, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str did: Dataset Id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['did']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_dataset" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'did' is set
        if ('did' not in params or
                params['did'] is None):
            raise ValueError("Missing the required parameter `did` when calling `remove_dataset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'did' in params:
            path_params['did'] = params['did']  # noqa: E501

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
            '/datasets/{did}', 'DELETE',
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

    def update_dataset(self, body, did, **kwargs):  # noqa: E501
        """Update dataset  # noqa: E501

        Changes dataset properties.  This operation requires `space_manage_datasets` privilege.  ***Example cURL requests***  **Change dataset protection flags** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X PATCH \"https://$PROVIDER_HOST/api/v3/oneprovider/datasets/$DATASET_ID\" \\ -H \"Content-Type: application/json\" -d '{     \"setProtectionFlags\": [\"metadata_protection\"],     \"unsetProtectionFlags\": [\"data_protection\"] }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_dataset(body, did, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DatasetUpdateRequest body: Dataset properties (required)
        :param str did: Dataset Id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_dataset_with_http_info(body, did, **kwargs)  # noqa: E501
        else:
            (data) = self.update_dataset_with_http_info(body, did, **kwargs)  # noqa: E501
            return data

    def update_dataset_with_http_info(self, body, did, **kwargs):  # noqa: E501
        """Update dataset  # noqa: E501

        Changes dataset properties.  This operation requires `space_manage_datasets` privilege.  ***Example cURL requests***  **Change dataset protection flags** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X PATCH \"https://$PROVIDER_HOST/api/v3/oneprovider/datasets/$DATASET_ID\" \\ -H \"Content-Type: application/json\" -d '{     \"setProtectionFlags\": [\"metadata_protection\"],     \"unsetProtectionFlags\": [\"data_protection\"] }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_dataset_with_http_info(body, did, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DatasetUpdateRequest body: Dataset properties (required)
        :param str did: Dataset Id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'did']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_dataset" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_dataset`")  # noqa: E501
        # verify the required parameter 'did' is set
        if ('did' not in params or
                params['did'] is None):
            raise ValueError("Missing the required parameter `did` when calling `update_dataset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'did' in params:
            path_params['did'] = params['did']  # noqa: E501

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
            '/datasets/{did}', 'PATCH',
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
