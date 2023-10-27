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


class ViewApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_space_view(self, body, sid, view_name, **kwargs):  # noqa: E501
        """Create view  # noqa: E501

        This method creates or replaces an existing view with a new one.  This operation requires `space_manage_views` privilege.  ***Example cURL requests***  **Create space view** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/$VIEW_NAME?spatial=false&providers[]=$PROVIDER_ID_1&providers[]=$PROVIDER_ID_2 \\ -H \"Content-Type: application/javascript\" -d \"@./my_view1.js\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_space_view(body, sid, view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: The view map function. (required)
        :param str sid: Space Id in which view will be created.  (required)
        :param str view_name: Name of the view. (required)
        :param bool spatial: Specifies whether view is spatial or not.
        :param int update_min_changes: Minimum number of document changes to trigger re-viewing.
        :param int replica_update_min_changes: Minimum number of document changes to trigger re-viewing of a replica view.
        :param list[str] providers: Providers which will create view.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_space_view_with_http_info(body, sid, view_name, **kwargs)  # noqa: E501
        else:
            (data) = self.create_space_view_with_http_info(body, sid, view_name, **kwargs)  # noqa: E501
            return data

    def create_space_view_with_http_info(self, body, sid, view_name, **kwargs):  # noqa: E501
        """Create view  # noqa: E501

        This method creates or replaces an existing view with a new one.  This operation requires `space_manage_views` privilege.  ***Example cURL requests***  **Create space view** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/$VIEW_NAME?spatial=false&providers[]=$PROVIDER_ID_1&providers[]=$PROVIDER_ID_2 \\ -H \"Content-Type: application/javascript\" -d \"@./my_view1.js\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_space_view_with_http_info(body, sid, view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: The view map function. (required)
        :param str sid: Space Id in which view will be created.  (required)
        :param str view_name: Name of the view. (required)
        :param bool spatial: Specifies whether view is spatial or not.
        :param int update_min_changes: Minimum number of document changes to trigger re-viewing.
        :param int replica_update_min_changes: Minimum number of document changes to trigger re-viewing of a replica view.
        :param list[str] providers: Providers which will create view.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'sid', 'view_name', 'spatial', 'update_min_changes', 'replica_update_min_changes', 'providers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_space_view" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_space_view`")  # noqa: E501
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `create_space_view`")  # noqa: E501
        # verify the required parameter 'view_name' is set
        if ('view_name' not in params or
                params['view_name'] is None):
            raise ValueError("Missing the required parameter `view_name` when calling `create_space_view`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sid' in params:
            path_params['sid'] = params['sid']  # noqa: E501
        if 'view_name' in params:
            path_params['view_name'] = params['view_name']  # noqa: E501

        query_params = []
        if 'spatial' in params:
            query_params.append(('spatial', params['spatial']))  # noqa: E501
        if 'update_min_changes' in params:
            query_params.append(('update_min_changes', params['update_min_changes']))  # noqa: E501
        if 'replica_update_min_changes' in params:
            query_params.append(('replica_update_min_changes', params['replica_update_min_changes']))  # noqa: E501
        if 'providers' in params:
            query_params.append(('providers[]', params['providers']))  # noqa: E501
            collection_formats['providers[]'] = 'multi'  # noqa: E501

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
            ['application/javascript'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/spaces/{sid}/views/{view_name}', 'PUT',
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

    def get_space_view(self, sid, view_name, **kwargs):  # noqa: E501
        """Get view  # noqa: E501

        This method returns a JSON describing specific view.  This operation requires `space_view_views` privilege.  ***Example cURL requests***  **Get information about specific view** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/$VIEW_NAME  {     \"spatial\": false,     \"mapFunction\": \"function (id, type, meta, ctx) {\\\\n        if(type == \\\\'custom_metadata\\\\' && meta[\\\\'onexattr\\\\']) {\\\\n            return [meta[\\\\'onexattr\\\\'], id];\\\\n        }\\\\n        return null;\\\\n    }\"     \"reduceFunction\": null,     \"viewOptions\": {         \"update_min_changes\": 100     },     \"providers\": [         \"6b9bc70630547d925861a27e1f050dfe\"     ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_view(sid, view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id in which view exist.  (required)
        :param str view_name: Name of the view. (required)
        :return: View
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_space_view_with_http_info(sid, view_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_space_view_with_http_info(sid, view_name, **kwargs)  # noqa: E501
            return data

    def get_space_view_with_http_info(self, sid, view_name, **kwargs):  # noqa: E501
        """Get view  # noqa: E501

        This method returns a JSON describing specific view.  This operation requires `space_view_views` privilege.  ***Example cURL requests***  **Get information about specific view** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/$VIEW_NAME  {     \"spatial\": false,     \"mapFunction\": \"function (id, type, meta, ctx) {\\\\n        if(type == \\\\'custom_metadata\\\\' && meta[\\\\'onexattr\\\\']) {\\\\n            return [meta[\\\\'onexattr\\\\'], id];\\\\n        }\\\\n        return null;\\\\n    }\"     \"reduceFunction\": null,     \"viewOptions\": {         \"update_min_changes\": 100     },     \"providers\": [         \"6b9bc70630547d925861a27e1f050dfe\"     ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_view_with_http_info(sid, view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id in which view exist.  (required)
        :param str view_name: Name of the view. (required)
        :return: View
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sid', 'view_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_space_view" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `get_space_view`")  # noqa: E501
        # verify the required parameter 'view_name' is set
        if ('view_name' not in params or
                params['view_name'] is None):
            raise ValueError("Missing the required parameter `view_name` when calling `get_space_view`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sid' in params:
            path_params['sid'] = params['sid']  # noqa: E501
        if 'view_name' in params:
            path_params['view_name'] = params['view_name']  # noqa: E501

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
            '/spaces/{sid}/views/{view_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='View',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_space_views(self, sid, **kwargs):  # noqa: E501
        """Get all space views  # noqa: E501

        Returns the list of all view names in a space. The list is broken down into pages, each with length less or equal to the limit parameter. If the nextPageToken in the response has non-null value, there are more names to list - provide the token in the page_token parameter in the following request.  This operation requires `space_view_views` privilege.  ***Example cURL requests***  **List at most 3 view names starting from page id 757136151113c2f** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views?limit=3&page_token=757136151113c2f\"  {     \"views\": [         \"favourites\",         \"images\",         \"videos\"     ],     \"nextPageToken\": \"8471726779817b3a\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_views(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id in which to list views.  (required)
        :param int limit: Allows to limit the number of returned views. 
        :param str page_token: Allows to start the listing from a certain point, identified by the page token. 
        :return: Views
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_space_views_with_http_info(sid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_space_views_with_http_info(sid, **kwargs)  # noqa: E501
            return data

    def get_space_views_with_http_info(self, sid, **kwargs):  # noqa: E501
        """Get all space views  # noqa: E501

        Returns the list of all view names in a space. The list is broken down into pages, each with length less or equal to the limit parameter. If the nextPageToken in the response has non-null value, there are more names to list - provide the token in the page_token parameter in the following request.  This operation requires `space_view_views` privilege.  ***Example cURL requests***  **List at most 3 view names starting from page id 757136151113c2f** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views?limit=3&page_token=757136151113c2f\"  {     \"views\": [         \"favourites\",         \"images\",         \"videos\"     ],     \"nextPageToken\": \"8471726779817b3a\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_views_with_http_info(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id in which to list views.  (required)
        :param int limit: Allows to limit the number of returned views. 
        :param str page_token: Allows to start the listing from a certain point, identified by the page token. 
        :return: Views
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sid', 'limit', 'page_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_space_views" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `get_space_views`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sid' in params:
            path_params['sid'] = params['sid']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'page_token' in params:
            query_params.append(('page_token', params['page_token']))  # noqa: E501

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
            '/spaces/{sid}/views', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Views',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def query_space_view(self, sid, view_name, **kwargs):  # noqa: E501
        """Query view  # noqa: E501

        This method returns the list of result objects for files which match the query on a predefined view. Those objects contains following fields: * ``id`` - for use as `startkey_docid` or `endkey_docid` in following queries * ``key`` - the first element of list returned by user defined mapping/spatial function * ``value`` - the second element of list returned by user defined mapping/spatial function * ``geometry`` - describes geometry of data (only available in case of spatial views)  Currently, views are defined per space, i.e. the result will be limited to files and directories in a space for which the view was defined.  This operation supports also custom view query attributes as provided by [Couchbase](http://docs.couchbase.com/admin/admin/Views/views-querying.html).  Additionaly, Couchbase [spatial queries](http://docs.couchbase.com/admin/admin/Views/views-geospatial.html) are possible using `bbox` query parameter. These queries are possible on views which emit values conforming to the [GeoJSON](http://geojson.org/) format.  This operation requires `space_query_views` privilege.  ***Example cURL requests***  **Get 4 files from view skipping first 10**  With example map function used: ```javascript function (id, type, meta, ctx) {     if(type == 'custom_metadata' && meta['onexattr']) {         return [meta['onexattr'], id];     }     return null; } ```  ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/VIEW_NAME/query?skip=10&limit=4  [     {         \"id\": \"fd18b793d446099ae84f8bd5c054ad34\",         \"key\": 1,         \"value\": \"00000000002C45416775696423633062636533343133336336636633393238336134323333396430656461393323737061636531\"     },     {         \"id\": \"2785dbd91120e341265f9ee2370ccf08\",         \"key\": 2,         \"value\": \"00000000002CF7DB6775696423396261373964653764643866336432393436323262313133393738643338383323737061636531\"     },     {         \"id\": \"60a9e6da61e12deeb3e6c688fe861c01\",         \"key\": 3,         \"value\": \"00000000002C47916775696423336330336538623730333439353233383631313966346139343731316631656323737061636531\"     },     {         \"id\": \"651d696a8446e92ab55de163f9b8594d\",         \"key\": 4,         \"value\": \"00000000002CA8906775696423633835366438613139666565336337666165623538303736356465383039356223737061636531\"     },     ... ] ```  **Get list of files associated with geospatial coordinates**  With example spatial function used: ```javascript function (id, type, meta, ctx) {     if(type == 'custom_metadata' && meta['onexattr']) {         return [meta['onexattr'], id];     }     return null; } ```  ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/$VIEW_NAME/query?spatial=true&stale=false  [     {         \"geometry\": {             \"type\": \"Point\",             \"coordinates\": [0, 0]         },         \"id\": \"36cfb018c312653e65b346c421d7a678\",         \"key\": [[0, 0], [0, 0]],         \"value\": \"00000000002C5DA36775696423663535633934306564393632656530666133663330633137393362333765356223737061636531\"     },     {         \"geometry\": {             \"type\": \"Point\",             \"coordinates\": [5.1, 10.22]         },         \"id\": \"972eb78ff8e262c4bebdc11799c20f51\",         \"key\": [[5.1, 5.1], [10.22, 10.22]],         \"value\": \"00000000002C678A6775696423363030666461383130623030386333616664363637396666653334366137656623737061636531\"     } ] ```  **Get file popularity for a specific space** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/file-popularity/query?spatial=true&start_range=\\[1,0,0,0,0,0\\]&end_range=\\[null,null,null,null,null,null\\]\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_space_view(sid, view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id in which view exist. (required)
        :param str view_name: Name of the view. (required)
        :param bool descending: Return the documents in descending order (by key).
        :param str key: Return only documents that match the specified key. Key must be specified as a JSON value. 
        :param str keys: Return only documents that match any of the keys specified within the given array. Keys must be specified as a JSON array, escaped properly. Sorting is not applied when using this option. 
        :param int limit: Limit the number of the returned documents to the specified number. 
        :param int skip: Skip this number of records before starting to return the results. 
        :param str startkey: Return records with a value equal to or greater than the specified key. Key must be specified as a JSON value. 
        :param str startkey_docid: Return records starting with the specified document Id. 
        :param str endkey: Stop returning records when the specified key is reached. Key must be specified as a JSON value. 
        :param str endkey_docid: Stop returning records when the specified document Id is reached. 
        :param bool inclusive_end: Specifies whether the specified end key is included in the result. ***Note:*** Do not use `inclusive_end` with `key` or `keys`. 
        :param str stale: Allow records from a stale view to be used. Allowed values are `ok`, `update_after` or `false`. 
        :param str bbox: Specify the bounding box for a spatial query (e.g. ?bbox=-180,-90,0,0) 
        :param bool spatial: Enable spatial type of query. When querying the file-popularity view, the `start_range` and `end_range` constraints should be specified as 6-dimensional arrays, with the following fields: `[SizeLowerLimit, LastOpenHoursEpochLowerLimit, TotalOpenLowerLimit, HoursOpenAvgLowerLimit, DayOpenAvgLowerLimit, MonthOpenAvgLowerLimit]`. 
        :param str start_range: Array specifying the range in spatial queries (e.g. `start_range=[1,0,0,0,0,0]`).
        :param str end_range: Array specifying the range in spatial queries (e.g. `end_range=[null,null,null,null,null,null]`).
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.query_space_view_with_http_info(sid, view_name, **kwargs)  # noqa: E501
        else:
            (data) = self.query_space_view_with_http_info(sid, view_name, **kwargs)  # noqa: E501
            return data

    def query_space_view_with_http_info(self, sid, view_name, **kwargs):  # noqa: E501
        """Query view  # noqa: E501

        This method returns the list of result objects for files which match the query on a predefined view. Those objects contains following fields: * ``id`` - for use as `startkey_docid` or `endkey_docid` in following queries * ``key`` - the first element of list returned by user defined mapping/spatial function * ``value`` - the second element of list returned by user defined mapping/spatial function * ``geometry`` - describes geometry of data (only available in case of spatial views)  Currently, views are defined per space, i.e. the result will be limited to files and directories in a space for which the view was defined.  This operation supports also custom view query attributes as provided by [Couchbase](http://docs.couchbase.com/admin/admin/Views/views-querying.html).  Additionaly, Couchbase [spatial queries](http://docs.couchbase.com/admin/admin/Views/views-geospatial.html) are possible using `bbox` query parameter. These queries are possible on views which emit values conforming to the [GeoJSON](http://geojson.org/) format.  This operation requires `space_query_views` privilege.  ***Example cURL requests***  **Get 4 files from view skipping first 10**  With example map function used: ```javascript function (id, type, meta, ctx) {     if(type == 'custom_metadata' && meta['onexattr']) {         return [meta['onexattr'], id];     }     return null; } ```  ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/VIEW_NAME/query?skip=10&limit=4  [     {         \"id\": \"fd18b793d446099ae84f8bd5c054ad34\",         \"key\": 1,         \"value\": \"00000000002C45416775696423633062636533343133336336636633393238336134323333396430656461393323737061636531\"     },     {         \"id\": \"2785dbd91120e341265f9ee2370ccf08\",         \"key\": 2,         \"value\": \"00000000002CF7DB6775696423396261373964653764643866336432393436323262313133393738643338383323737061636531\"     },     {         \"id\": \"60a9e6da61e12deeb3e6c688fe861c01\",         \"key\": 3,         \"value\": \"00000000002C47916775696423336330336538623730333439353233383631313966346139343731316631656323737061636531\"     },     {         \"id\": \"651d696a8446e92ab55de163f9b8594d\",         \"key\": 4,         \"value\": \"00000000002CA8906775696423633835366438613139666565336337666165623538303736356465383039356223737061636531\"     },     ... ] ```  **Get list of files associated with geospatial coordinates**  With example spatial function used: ```javascript function (id, type, meta, ctx) {     if(type == 'custom_metadata' && meta['onexattr']) {         return [meta['onexattr'], id];     }     return null; } ```  ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/$VIEW_NAME/query?spatial=true&stale=false  [     {         \"geometry\": {             \"type\": \"Point\",             \"coordinates\": [0, 0]         },         \"id\": \"36cfb018c312653e65b346c421d7a678\",         \"key\": [[0, 0], [0, 0]],         \"value\": \"00000000002C5DA36775696423663535633934306564393632656530666133663330633137393362333765356223737061636531\"     },     {         \"geometry\": {             \"type\": \"Point\",             \"coordinates\": [5.1, 10.22]         },         \"id\": \"972eb78ff8e262c4bebdc11799c20f51\",         \"key\": [[5.1, 5.1], [10.22, 10.22]],         \"value\": \"00000000002C678A6775696423363030666461383130623030386333616664363637396666653334366137656623737061636531\"     } ] ```  **Get file popularity for a specific space** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/file-popularity/query?spatial=true&start_range=\\[1,0,0,0,0,0\\]&end_range=\\[null,null,null,null,null,null\\]\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_space_view_with_http_info(sid, view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id in which view exist. (required)
        :param str view_name: Name of the view. (required)
        :param bool descending: Return the documents in descending order (by key).
        :param str key: Return only documents that match the specified key. Key must be specified as a JSON value. 
        :param str keys: Return only documents that match any of the keys specified within the given array. Keys must be specified as a JSON array, escaped properly. Sorting is not applied when using this option. 
        :param int limit: Limit the number of the returned documents to the specified number. 
        :param int skip: Skip this number of records before starting to return the results. 
        :param str startkey: Return records with a value equal to or greater than the specified key. Key must be specified as a JSON value. 
        :param str startkey_docid: Return records starting with the specified document Id. 
        :param str endkey: Stop returning records when the specified key is reached. Key must be specified as a JSON value. 
        :param str endkey_docid: Stop returning records when the specified document Id is reached. 
        :param bool inclusive_end: Specifies whether the specified end key is included in the result. ***Note:*** Do not use `inclusive_end` with `key` or `keys`. 
        :param str stale: Allow records from a stale view to be used. Allowed values are `ok`, `update_after` or `false`. 
        :param str bbox: Specify the bounding box for a spatial query (e.g. ?bbox=-180,-90,0,0) 
        :param bool spatial: Enable spatial type of query. When querying the file-popularity view, the `start_range` and `end_range` constraints should be specified as 6-dimensional arrays, with the following fields: `[SizeLowerLimit, LastOpenHoursEpochLowerLimit, TotalOpenLowerLimit, HoursOpenAvgLowerLimit, DayOpenAvgLowerLimit, MonthOpenAvgLowerLimit]`. 
        :param str start_range: Array specifying the range in spatial queries (e.g. `start_range=[1,0,0,0,0,0]`).
        :param str end_range: Array specifying the range in spatial queries (e.g. `end_range=[null,null,null,null,null,null]`).
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sid', 'view_name', 'descending', 'key', 'keys', 'limit', 'skip', 'startkey', 'startkey_docid', 'endkey', 'endkey_docid', 'inclusive_end', 'stale', 'bbox', 'spatial', 'start_range', 'end_range']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_space_view" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `query_space_view`")  # noqa: E501
        # verify the required parameter 'view_name' is set
        if ('view_name' not in params or
                params['view_name'] is None):
            raise ValueError("Missing the required parameter `view_name` when calling `query_space_view`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sid' in params:
            path_params['sid'] = params['sid']  # noqa: E501
        if 'view_name' in params:
            path_params['view_name'] = params['view_name']  # noqa: E501

        query_params = []
        if 'descending' in params:
            query_params.append(('descending', params['descending']))  # noqa: E501
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501
        if 'keys' in params:
            query_params.append(('keys', params['keys']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'startkey' in params:
            query_params.append(('startkey', params['startkey']))  # noqa: E501
        if 'startkey_docid' in params:
            query_params.append(('startkey_docid', params['startkey_docid']))  # noqa: E501
        if 'endkey' in params:
            query_params.append(('endkey', params['endkey']))  # noqa: E501
        if 'endkey_docid' in params:
            query_params.append(('endkey_docid', params['endkey_docid']))  # noqa: E501
        if 'inclusive_end' in params:
            query_params.append(('inclusive_end', params['inclusive_end']))  # noqa: E501
        if 'stale' in params:
            query_params.append(('stale', params['stale']))  # noqa: E501
        if 'bbox' in params:
            query_params.append(('bbox', params['bbox']))  # noqa: E501
        if 'spatial' in params:
            query_params.append(('spatial', params['spatial']))  # noqa: E501
        if 'start_range' in params:
            query_params.append(('start_range', params['start_range']))  # noqa: E501
        if 'end_range' in params:
            query_params.append(('end_range', params['end_range']))  # noqa: E501

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
            '/spaces/{sid}/views/{view_name}/query', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_space_view(self, sid, view_name, **kwargs):  # noqa: E501
        """Remove view  # noqa: E501

        This method removes an existing view.  This operation requires `space_manage_views` privilege.  ***Example cURL requests***  **Remove existing view** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/$VIEW_NAME ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_space_view(sid, view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id in which view exist.  (required)
        :param str view_name: Name of the view. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_space_view_with_http_info(sid, view_name, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_space_view_with_http_info(sid, view_name, **kwargs)  # noqa: E501
            return data

    def remove_space_view_with_http_info(self, sid, view_name, **kwargs):  # noqa: E501
        """Remove view  # noqa: E501

        This method removes an existing view.  This operation requires `space_manage_views` privilege.  ***Example cURL requests***  **Remove existing view** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/$VIEW_NAME ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_space_view_with_http_info(sid, view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id in which view exist.  (required)
        :param str view_name: Name of the view. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sid', 'view_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_space_view" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `remove_space_view`")  # noqa: E501
        # verify the required parameter 'view_name' is set
        if ('view_name' not in params or
                params['view_name'] is None):
            raise ValueError("Missing the required parameter `view_name` when calling `remove_space_view`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sid' in params:
            path_params['sid'] = params['sid']  # noqa: E501
        if 'view_name' in params:
            path_params['view_name'] = params['view_name']  # noqa: E501

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
            '/spaces/{sid}/views/{view_name}', 'DELETE',
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

    def remove_view_reduce_function(self, sid, view_name, **kwargs):  # noqa: E501
        """Remove view reduce function  # noqa: E501

        This method removes the view reduce function.  This operation requires `space_manage_views` privilege.  ***Example cURL requests***  **Remove view reduce function** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/$VIEW_NAME/reduce ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_view_reduce_function(sid, view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id in which view exist.  (required)
        :param str view_name: Name of the view. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_view_reduce_function_with_http_info(sid, view_name, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_view_reduce_function_with_http_info(sid, view_name, **kwargs)  # noqa: E501
            return data

    def remove_view_reduce_function_with_http_info(self, sid, view_name, **kwargs):  # noqa: E501
        """Remove view reduce function  # noqa: E501

        This method removes the view reduce function.  This operation requires `space_manage_views` privilege.  ***Example cURL requests***  **Remove view reduce function** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/$VIEW_NAME/reduce ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_view_reduce_function_with_http_info(sid, view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id in which view exist.  (required)
        :param str view_name: Name of the view. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sid', 'view_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_view_reduce_function" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `remove_view_reduce_function`")  # noqa: E501
        # verify the required parameter 'view_name' is set
        if ('view_name' not in params or
                params['view_name'] is None):
            raise ValueError("Missing the required parameter `view_name` when calling `remove_view_reduce_function`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sid' in params:
            path_params['sid'] = params['sid']  # noqa: E501
        if 'view_name' in params:
            path_params['view_name'] = params['view_name']  # noqa: E501

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
            '/spaces/{sid}/views/{view_name}/reduce', 'DELETE',
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

    def update_space_view(self, sid, view_name, **kwargs):  # noqa: E501
        """Update view  # noqa: E501

        This method updates existing view definition.  It takes the same arguments as PUT. Only specified parameters will be overwritten.  This operation requires `space_manage_views` privilege.  ***Example cURL requests***  **Update space view** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PATCH https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/$VIEW_NAME?update_min_changes=10 \\ -H \"Content-Type: application/javascript\" -d \"@./my_improved_view1.js\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_space_view(sid, view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id in which view exist.  (required)
        :param str view_name: Name of the view. (required)
        :param str body: The view map function.
        :param bool spatial: Specifies whether view is spatial or not.
        :param int update_min_changes: Minimum number of document changes to trigger re-viewing.
        :param int replica_update_min_changes: Minimum number of document changes to trigger re-viewing of a replica view.
        :param list[str] providers: Providers which will create view.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_space_view_with_http_info(sid, view_name, **kwargs)  # noqa: E501
        else:
            (data) = self.update_space_view_with_http_info(sid, view_name, **kwargs)  # noqa: E501
            return data

    def update_space_view_with_http_info(self, sid, view_name, **kwargs):  # noqa: E501
        """Update view  # noqa: E501

        This method updates existing view definition.  It takes the same arguments as PUT. Only specified parameters will be overwritten.  This operation requires `space_manage_views` privilege.  ***Example cURL requests***  **Update space view** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PATCH https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/$VIEW_NAME?update_min_changes=10 \\ -H \"Content-Type: application/javascript\" -d \"@./my_improved_view1.js\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_space_view_with_http_info(sid, view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id in which view exist.  (required)
        :param str view_name: Name of the view. (required)
        :param str body: The view map function.
        :param bool spatial: Specifies whether view is spatial or not.
        :param int update_min_changes: Minimum number of document changes to trigger re-viewing.
        :param int replica_update_min_changes: Minimum number of document changes to trigger re-viewing of a replica view.
        :param list[str] providers: Providers which will create view.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sid', 'view_name', 'body', 'spatial', 'update_min_changes', 'replica_update_min_changes', 'providers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_space_view" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `update_space_view`")  # noqa: E501
        # verify the required parameter 'view_name' is set
        if ('view_name' not in params or
                params['view_name'] is None):
            raise ValueError("Missing the required parameter `view_name` when calling `update_space_view`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sid' in params:
            path_params['sid'] = params['sid']  # noqa: E501
        if 'view_name' in params:
            path_params['view_name'] = params['view_name']  # noqa: E501

        query_params = []
        if 'spatial' in params:
            query_params.append(('spatial', params['spatial']))  # noqa: E501
        if 'update_min_changes' in params:
            query_params.append(('update_min_changes', params['update_min_changes']))  # noqa: E501
        if 'replica_update_min_changes' in params:
            query_params.append(('replica_update_min_changes', params['replica_update_min_changes']))  # noqa: E501
        if 'providers' in params:
            query_params.append(('providers[]', params['providers']))  # noqa: E501
            collection_formats['providers[]'] = 'multi'  # noqa: E501

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
            ['application/javascript'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/spaces/{sid}/views/{view_name}', 'PATCH',
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

    def update_view_reduce_function(self, body, sid, view_name, **kwargs):  # noqa: E501
        """Update view reduce function  # noqa: E501

        This method replaces the existing view reduce function code with the request body.  The reduce functions are defined as JavaScript functions which are executed on the database backend.  This operation requires `space_manage_views` privilege.  ***Example cURL requests***  **Update space view** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/$VIEW_NAME/reduce \\ -H \"Content-Type: application/javascript\" -d \"@./my_improved_reduce_fun.js\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_view_reduce_function(body, sid, view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: The view reduce function. (required)
        :param str sid: Space Id in which view exist.  (required)
        :param str view_name: Name of the view. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_view_reduce_function_with_http_info(body, sid, view_name, **kwargs)  # noqa: E501
        else:
            (data) = self.update_view_reduce_function_with_http_info(body, sid, view_name, **kwargs)  # noqa: E501
            return data

    def update_view_reduce_function_with_http_info(self, body, sid, view_name, **kwargs):  # noqa: E501
        """Update view reduce function  # noqa: E501

        This method replaces the existing view reduce function code with the request body.  The reduce functions are defined as JavaScript functions which are executed on the database backend.  This operation requires `space_manage_views` privilege.  ***Example cURL requests***  **Update space view** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/$VIEW_NAME/reduce \\ -H \"Content-Type: application/javascript\" -d \"@./my_improved_reduce_fun.js\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_view_reduce_function_with_http_info(body, sid, view_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: The view reduce function. (required)
        :param str sid: Space Id in which view exist.  (required)
        :param str view_name: Name of the view. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'sid', 'view_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_view_reduce_function" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_view_reduce_function`")  # noqa: E501
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `update_view_reduce_function`")  # noqa: E501
        # verify the required parameter 'view_name' is set
        if ('view_name' not in params or
                params['view_name'] is None):
            raise ValueError("Missing the required parameter `view_name` when calling `update_view_reduce_function`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sid' in params:
            path_params['sid'] = params['sid']  # noqa: E501
        if 'view_name' in params:
            path_params['view_name'] = params['view_name']  # noqa: E501

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
            ['application/javascript'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/spaces/{sid}/views/{view_name}/reduce', 'PUT',
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
