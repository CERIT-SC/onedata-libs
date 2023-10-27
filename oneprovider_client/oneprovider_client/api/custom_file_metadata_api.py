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


class CustomFileMetadataApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_json_metadata(self, id, **kwargs):  # noqa: E501
        """Get file json metadata  # noqa: E501

        This method returns the json metadata associated with file specified by [$FILE_ID](#operation/lookup_file_id).  By default the method returns the complete json metadata. But it is possible to request only a part of the document by specifying `filter_type` and `filter` attributes in the query.  Supported filter types are:   * **keypath** - list of JSON keys which point to requested JSON object,     separated by `.`, array elements should be expressed as `[i]`     (e.g. `key1.key2.[2].key3`)  ***Example cURL requests***  **Get specific JSON value from metadata document** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/json?filter_type=keypath&filter=key1.key2.[2].key3  {\"key4\": \"value\"} ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_json_metadata(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the file. (required)
        :param str filter_type: The type of filter to apply to the metadata document.
        :param str filter: The filter to apply to the metadata document before returning. Required if `filter_type` is specified. 
        :param bool inherited: When set to true, this operation will merge the metadata documents from parent directories as well as entire space into a single JSON document. 
        :param bool resolve_symlink: Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`). 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_json_metadata_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_json_metadata_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_json_metadata_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get file json metadata  # noqa: E501

        This method returns the json metadata associated with file specified by [$FILE_ID](#operation/lookup_file_id).  By default the method returns the complete json metadata. But it is possible to request only a part of the document by specifying `filter_type` and `filter` attributes in the query.  Supported filter types are:   * **keypath** - list of JSON keys which point to requested JSON object,     separated by `.`, array elements should be expressed as `[i]`     (e.g. `key1.key2.[2].key3`)  ***Example cURL requests***  **Get specific JSON value from metadata document** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/json?filter_type=keypath&filter=key1.key2.[2].key3  {\"key4\": \"value\"} ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_json_metadata_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the file. (required)
        :param str filter_type: The type of filter to apply to the metadata document.
        :param str filter: The filter to apply to the metadata document before returning. Required if `filter_type` is specified. 
        :param bool inherited: When set to true, this operation will merge the metadata documents from parent directories as well as entire space into a single JSON document. 
        :param bool resolve_symlink: Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`). 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'filter_type', 'filter', 'inherited', 'resolve_symlink']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_json_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_json_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'filter_type' in params:
            query_params.append(('filter_type', params['filter_type']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'inherited' in params:
            query_params.append(('inherited', params['inherited']))  # noqa: E501
        if 'resolve_symlink' in params:
            query_params.append(('resolve_symlink', params['resolve_symlink']))  # noqa: E501

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
            '/data/{id}/metadata/json', 'GET',
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

    def get_rdf_metadata(self, id, **kwargs):  # noqa: E501
        """Get file rdf metadata  # noqa: E501

        This method returns the rdf metadata for a file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Get complete RDF metadata document for file**  ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/rdf  <RDF><homepage>https://www.onedata.org</homepage></RDF> ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rdf_metadata(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the file. (required)
        :param bool resolve_symlink: Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`). 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_rdf_metadata_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_rdf_metadata_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_rdf_metadata_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get file rdf metadata  # noqa: E501

        This method returns the rdf metadata for a file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Get complete RDF metadata document for file**  ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/rdf  <RDF><homepage>https://www.onedata.org</homepage></RDF> ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rdf_metadata_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the file. (required)
        :param bool resolve_symlink: Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`). 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'resolve_symlink']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_rdf_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_rdf_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'resolve_symlink' in params:
            query_params.append(('resolve_symlink', params['resolve_symlink']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/rdf+xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}/metadata/rdf', 'GET',
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

    def get_xattrs(self, id, **kwargs):  # noqa: E501
        """Get file extended attributes  # noqa: E501

        This method returns the selected extended attributes associated with file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Get extended file attributes** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/xattrs?attribute=license\"  {     \"license\": \"CC-0\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_xattrs(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the file. (required)
        :param str attribute: Name of attribute to query for.
        :param bool inherited: When set to true, this operation returns attributes including those inherited from parent directories and from the space root directory. If the same attribute is set on different nesting levels, the lowest level takes precedence (e.g. file attributes override the attributes from its parent directory). 
        :param bool show_internal: When set to true, this operation returns all attributes including those normally not shown (e.g. json/rdf metadata, acl and cdmi attributes). 
        :param bool resolve_symlink: Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`). 
        :return: dict(str, str)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_xattrs_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_xattrs_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_xattrs_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get file extended attributes  # noqa: E501

        This method returns the selected extended attributes associated with file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Get extended file attributes** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/xattrs?attribute=license\"  {     \"license\": \"CC-0\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_xattrs_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the file. (required)
        :param str attribute: Name of attribute to query for.
        :param bool inherited: When set to true, this operation returns attributes including those inherited from parent directories and from the space root directory. If the same attribute is set on different nesting levels, the lowest level takes precedence (e.g. file attributes override the attributes from its parent directory). 
        :param bool show_internal: When set to true, this operation returns all attributes including those normally not shown (e.g. json/rdf metadata, acl and cdmi attributes). 
        :param bool resolve_symlink: Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`). 
        :return: dict(str, str)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'attribute', 'inherited', 'show_internal', 'resolve_symlink']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_xattrs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_xattrs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'attribute' in params:
            query_params.append(('attribute', params['attribute']))  # noqa: E501
        if 'inherited' in params:
            query_params.append(('inherited', params['inherited']))  # noqa: E501
        if 'show_internal' in params:
            query_params.append(('show_internal', params['show_internal']))  # noqa: E501
        if 'resolve_symlink' in params:
            query_params.append(('resolve_symlink', params['resolve_symlink']))  # noqa: E501

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
            '/data/{id}/metadata/xattrs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, str)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_json_metadata(self, id, **kwargs):  # noqa: E501
        """Remove file json metadata  # noqa: E501

        Removes json metadata from the file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Remove file json metadata** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/json ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_json_metadata(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the file. (required)
        :param bool resolve_symlink: Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`). 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_json_metadata_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_json_metadata_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def remove_json_metadata_with_http_info(self, id, **kwargs):  # noqa: E501
        """Remove file json metadata  # noqa: E501

        Removes json metadata from the file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Remove file json metadata** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/json ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_json_metadata_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the file. (required)
        :param bool resolve_symlink: Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`). 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'resolve_symlink']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_json_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_json_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'resolve_symlink' in params:
            query_params.append(('resolve_symlink', params['resolve_symlink']))  # noqa: E501

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
            '/data/{id}/metadata/json', 'DELETE',
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

    def remove_rdf_metadata(self, id, **kwargs):  # noqa: E501
        """Remove file rdf metadata  # noqa: E501

        Removes rdf metadata from the file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Remove file rdf metadata** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/rdf ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_rdf_metadata(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the file. (required)
        :param bool resolve_symlink: Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`). 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_rdf_metadata_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_rdf_metadata_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def remove_rdf_metadata_with_http_info(self, id, **kwargs):  # noqa: E501
        """Remove file rdf metadata  # noqa: E501

        Removes rdf metadata from the file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Remove file rdf metadata** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/rdf ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_rdf_metadata_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the file. (required)
        :param bool resolve_symlink: Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`). 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'resolve_symlink']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_rdf_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_rdf_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'resolve_symlink' in params:
            query_params.append(('resolve_symlink', params['resolve_symlink']))  # noqa: E501

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
            '/data/{id}/metadata/rdf', 'DELETE',
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

    def remove_xattrs(self, body, id, **kwargs):  # noqa: E501
        """Remove file xattrs  # noqa: E501

        Removes specific xattrs from the file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Remove specific file xattrs** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/xattrs \\ -H 'Content-Type: application/json' -d '{ \"keys\": [\"license\"] }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_xattrs(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MetadataXattrsBody body: The xattrs to remove. (required)
        :param str id: Id of the file. (required)
        :param bool resolve_symlink: Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`). 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_xattrs_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_xattrs_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def remove_xattrs_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Remove file xattrs  # noqa: E501

        Removes specific xattrs from the file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Remove specific file xattrs** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/xattrs \\ -H 'Content-Type: application/json' -d '{ \"keys\": [\"license\"] }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_xattrs_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MetadataXattrsBody body: The xattrs to remove. (required)
        :param str id: Id of the file. (required)
        :param bool resolve_symlink: Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`). 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id', 'resolve_symlink']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_xattrs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `remove_xattrs`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_xattrs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'resolve_symlink' in params:
            query_params.append(('resolve_symlink', params['resolve_symlink']))  # noqa: E501

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
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}/metadata/xattrs', 'DELETE',
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

    def set_json_metadata(self, body, id, **kwargs):  # noqa: E501
        """Set file json metadata  # noqa: E501

        This method allows to set json metadata for a file specified by [$FILE_ID](#operation/lookup_file_id).  This operation will replace the previous json metadata if any.  ***Example cURL requests***  **Set JSON metadata for file** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/json \\ -H \"Content-Type: application/json\" -d '{     \"key1\": {         \"key2\": [\"val1\", \"val2\", \"val3\", \"val4\"]     } }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_json_metadata(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: The json metadata. (required)
        :param str id: Id of the file. (required)
        :param str filter_type: The type of filter to apply to the metadata document.
        :param str filter: The filter allowing to set specific metadata document key. Required if `filter_type` is specified. 
        :param bool resolve_symlink: Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`). 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_json_metadata_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_json_metadata_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def set_json_metadata_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Set file json metadata  # noqa: E501

        This method allows to set json metadata for a file specified by [$FILE_ID](#operation/lookup_file_id).  This operation will replace the previous json metadata if any.  ***Example cURL requests***  **Set JSON metadata for file** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/json \\ -H \"Content-Type: application/json\" -d '{     \"key1\": {         \"key2\": [\"val1\", \"val2\", \"val3\", \"val4\"]     } }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_json_metadata_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: The json metadata. (required)
        :param str id: Id of the file. (required)
        :param str filter_type: The type of filter to apply to the metadata document.
        :param str filter: The filter allowing to set specific metadata document key. Required if `filter_type` is specified. 
        :param bool resolve_symlink: Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`). 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id', 'filter_type', 'filter', 'resolve_symlink']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_json_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `set_json_metadata`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `set_json_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'filter_type' in params:
            query_params.append(('filter_type', params['filter_type']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'resolve_symlink' in params:
            query_params.append(('resolve_symlink', params['resolve_symlink']))  # noqa: E501

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
            '/data/{id}/metadata/json', 'PUT',
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

    def set_rdf_metadata(self, body, id, **kwargs):  # noqa: E501
        """Set file rdf metadata  # noqa: E501

        This method allows to set specific rdf metadata for a file specified by [$FILE_ID](#operation/lookup_file_id).  This operation will replace the previous rdf metadata if any.  ***Example cURL requests***  **Set RDF metadata for space from RDF file** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/rdf \\ -H \"Content-Type: application/rdf+xml\" -d \"@./space1_dublincore.rdf\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_rdf_metadata(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: The rdf metadata. (required)
        :param str id: Id of the file. (required)
        :param bool resolve_symlink: Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`). 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_rdf_metadata_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_rdf_metadata_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def set_rdf_metadata_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Set file rdf metadata  # noqa: E501

        This method allows to set specific rdf metadata for a file specified by [$FILE_ID](#operation/lookup_file_id).  This operation will replace the previous rdf metadata if any.  ***Example cURL requests***  **Set RDF metadata for space from RDF file** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/rdf \\ -H \"Content-Type: application/rdf+xml\" -d \"@./space1_dublincore.rdf\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_rdf_metadata_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: The rdf metadata. (required)
        :param str id: Id of the file. (required)
        :param bool resolve_symlink: Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`). 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id', 'resolve_symlink']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_rdf_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `set_rdf_metadata`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `set_rdf_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'resolve_symlink' in params:
            query_params.append(('resolve_symlink', params['resolve_symlink']))  # noqa: E501

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
            ['application/rdf+xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}/metadata/rdf', 'PUT',
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

    def set_xattr(self, id, **kwargs):  # noqa: E501
        """Set file extended attribute  # noqa: E501

        This method allows to set a value of a given extended file attributes (leaving other ones intact) for a file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Set extended file attribute** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/xattrs\" \\ -H 'Content-Type: application/json' -d '{ \"license\": \"CC-0\" }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_xattr(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the file. (required)
        :param dict(str, str) body: Extended attribute name and value.
        :param bool resolve_symlink: Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`). 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_xattr_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_xattr_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def set_xattr_with_http_info(self, id, **kwargs):  # noqa: E501
        """Set file extended attribute  # noqa: E501

        This method allows to set a value of a given extended file attributes (leaving other ones intact) for a file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Set extended file attribute** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/xattrs\" \\ -H 'Content-Type: application/json' -d '{ \"license\": \"CC-0\" }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_xattr_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Id of the file. (required)
        :param dict(str, str) body: Extended attribute name and value.
        :param bool resolve_symlink: Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`). 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body', 'resolve_symlink']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_xattr" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `set_xattr`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'resolve_symlink' in params:
            query_params.append(('resolve_symlink', params['resolve_symlink']))  # noqa: E501

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
            '/data/{id}/metadata/xattrs', 'PUT',
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
