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


class SpaceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_spaces(self, **kwargs):  # noqa: E501
        """Get all user spaces  # noqa: E501

        Returns the list of all user spaces.  ***Example cURL requests***  **List all user spaces** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces\"  [     {         \"spaceId\": \"fb519d81146bcc635b890ff03a5da0fdch34fe\",         \"fileId\": \"094576776E667431723230677767776C6B497031394E445F6E3868677873...\",         \"name\": \"Space1\"     },     {         \"spaceId\": \"e14039c53235c44f2f25dce4c90b1f0acha61c\",         \"fileId\": \"000000184465677569642373706163655F73706163653123737061636531...\",         \"name\": \"Space2\"     } ] ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_spaces(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[InlineResponse200]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_spaces_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_spaces_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_spaces_with_http_info(self, **kwargs):  # noqa: E501
        """Get all user spaces  # noqa: E501

        Returns the list of all user spaces.  ***Example cURL requests***  **List all user spaces** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces\"  [     {         \"spaceId\": \"fb519d81146bcc635b890ff03a5da0fdch34fe\",         \"fileId\": \"094576776E667431723230677767776C6B497031394E445F6E3868677873...\",         \"name\": \"Space1\"     },     {         \"spaceId\": \"e14039c53235c44f2f25dce4c90b1f0acha61c\",         \"fileId\": \"000000184465677569642373706163655F73706163653123737061636531...\",         \"name\": \"Space2\"     } ] ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_spaces_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[InlineResponse200]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_spaces" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/spaces', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse200]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_space(self, sid, **kwargs):  # noqa: E501
        """Get basic space information  # noqa: E501

        Returns the basic information about space with given Id.  ***Example cURL requests***  **Get information about a specific space** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID\"  {     \"name\": \"My Space 1\",     \"providers\": [         {             \"providerId\": \"a0b1d2e6ad583ba1b14caf3b71bc6129ch4f74\",             \"providerName\": \"MyPrivateCloud\"         },         {             \"providerId\": \"b107606a22f006b82f6f665a9e6f116cch0500\",             \"providerName\": \"PublicCloud1\"         }     ],     \"spaceId\": \"fb519d81146bcc635b890ff03a5da0fdch34fe\",     \"fileId\": \"094576776E667431723230677767776C6B497031394E445F6E3868677873...\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id. (required)
        :return: Space
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_space_with_http_info(sid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_space_with_http_info(sid, **kwargs)  # noqa: E501
            return data

    def get_space_with_http_info(self, sid, **kwargs):  # noqa: E501
        """Get basic space information  # noqa: E501

        Returns the basic information about space with given Id.  ***Example cURL requests***  **Get information about a specific space** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID\"  {     \"name\": \"My Space 1\",     \"providers\": [         {             \"providerId\": \"a0b1d2e6ad583ba1b14caf3b71bc6129ch4f74\",             \"providerName\": \"MyPrivateCloud\"         },         {             \"providerId\": \"b107606a22f006b82f6f665a9e6f116cch0500\",             \"providerName\": \"PublicCloud1\"         }     ],     \"spaceId\": \"fb519d81146bcc635b890ff03a5da0fdch34fe\",     \"fileId\": \"094576776E667431723230677767776C6B497031394E445F6E3868677873...\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_with_http_info(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id. (required)
        :return: Space
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_space" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `get_space`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sid' in params:
            path_params['sid'] = params['sid']  # noqa: E501

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
            '/spaces/{sid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Space',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
