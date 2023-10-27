# coding: utf-8

"""
    Onezone

    # Overview This is the RESTful API definition of Onezone component of Onedata data management system [onedata.org](http://onedata.org).  > This API is defined using [Swagger](http://swagger.io/), the JSON specification can be used to automatically generate client libraries - [swagger.json](../../../swagger/onezone/swagger.json).  This API allows control and configuration of local Onezone service deployment, in particular management of users, groups, spaces, shares, providers, handle services, handles and clusters.  ## Authentication and authorization To be able to use this API, the REST client must authenticate with the Onezone service and posses required authorization, which is determined based on client's privileges and relations in the system.  There are essentially three types of REST clients depending on the authentication:   * **users** - can authenticate using an access token or basic credentials   (only for users originating from Onezone's onepanel). Examples:   ```bash   curl -H \"x-auth-token: $TOKEN\" [...]   curl -H \"authorization: Bearer $TOKEN\" [...]   curl -u \"username:password\" [...]   curl -H \"macaroon: $TOKEN\" [...]   # DEPRECATED   ```   > `$TOKEN` can ba a Onedata access token, obtained via Onezone GUI or API, in the form   `MDAxNWxvY2F00aW9...`. If authority delegation for given IdP is enabled,   it is possible to provide an access token from the IdP, which must be prefixed   properly (depending on the configuration), e.g.: `github/GST5aasdA...`.    * **Oneproviders** - can authenticate using the provider root token,   which was assigned during registration in Onezone. It can be found in   `/etc/op_worker/provider_root_token.txt`. It is used just like a user   access token, for example:   ```bash   curl -H \"x-auth-token: $TOKEN\" [...]   curl -H \"authorization: Bearer $TOKEN\" [...]   curl -H \"macaroon: $TOKEN\" [...]   # DEPRECATED   ```   > Please mind that the provider root token is highly confidential and must   be kept secret (similarly to a private RSA key).    * **anonymous** - there is a small subset of operations that do not require     any authentication and are publicly available (look for information about     public availability in the endpoint descriptions).  The authorization of the client is determined based on existing relations and privileges in the system. In most cases, the rules below can be roughly applied:   * users and providers can access and modify their own data   * users can perform operations in groups, spaces, handle services, handles     and clusters depending on their privileges in subject entity - the required     privileges are listed in the description of each operation   * users can be given special admin privileges (fine-grained) that allow to     access and modify all entities in the system - see certain operations for     details.  Authentication and Authorization errors have the following meaning:   * HTTP 401 UNAUTHORIZED - the client could not be authenticated   * HTTP 403 FORBIDDEN - the client was authenticated, but is not permitted to     perform the action  ## Effective users and effective groups and spaces Onedata supports creation of arbitrary nested group and space membership tree structures. In order to determine if a given user belongs to the group directly or indirectly by belonging to a subgroup of a group, separate API calls are provided for getting information about group users (direct group members) and effective users (indirect group members).  ## API structure The API is divided into several categories, corresponding to entities in Onedata:  **Space management** The space management operations of this API provide means for accessing information about spaces and their management.  **Share management** The share management operations of this API provide means for accessing information about shares and their management.  **Group management** The group management operations allow creation of user groups, assigning their authorization rights, adding and removing users from groups.  **User management** The user management methods allow creation of users, managing their authorization credentials as well as space and group membership.  **Provider management** Provider specific calls allow getting global information about the spaces managed by the provider, and some administrative operations which can be used for monitoring or accounting.  **Handle service management** The handle service management operations of this API provide means for accessing information about handle services and their management.  **Handle API** Onezone provides extensive support for integration with Handle system registration services, including support for DOI and PID identifier assignment services. The API provides methods for adding new Handle services to the system, managing which users can use which registration services and complete API for registering identifiers to users' data sets which are made public.  **Cluster management** Operations for managing Onezone / Oneprovider clusters and their members - users and groups that can access the Onepanel interfaces (REST or GUI) of a cluster.   ## Using the API Onezone API is quite complex and thus it might be difficult to quickly figure out how to perform specific action, however the following guidelines might be useful:   * Operations performed by a regular users on their resources are grouped under     `/user` path (**USER** group in the menu)   * Operations performed by administrators of specific resources (e.g. groups,     spaces, shares) start with specific resource (e.g. `/groups`)   * By default the operations which list resource membership     (e.g. `/spaces/SPACE_ID/groups/`) will list explicit resource membership.     To get list of effective resource membership (i.e. including indirect     membership), special paths are provided     (e.g. `/spaces/SPACE_ID/effective_groups/`)  Furthermore, we have prepared a command-line client environment based on Docker which gives easy access to each of Onedata services via command-line clients, with pre-configured shell with full help on the APIs and autocomplete for operations and attributes.  ``` docker run -it onedata/rest-cli:21.02.3 ```  Below you can find some tutorials which show how to use this API in practice:   * [User oriented tutorial](https://onedata.org/#/home/documentation/doc/using_onedata/using_onedata_from_cli.html)   * [Administrator oriented tutorial](https://onedata.org/#/home/documentation/doc/administering_onedata/administering_onedata_from_cli.html)   ## Examples  **Generate new authentication token** ```bash curl -u user:password -X POST -H 'Content-type: application/json' -d '{}' \\ https://$ONEZONE_HOST/api/v3/onezone/user/client_tokens ```  **Get user details** ```bash curl -H 'X-Auth-Token: $TOKEN' -X GET \\ https://$ONEZONE_HOST/api/v3/onezone/user ```  **Get user details using an access token from github** ```bash curl -H 'X-Auth-Token: github/ijaAVWq3j9234jA9gPoR9agFja89t9UiPf8tiueSdx' -X GET \\ https://$ONEZONE_HOST/api/v3/onezone/user ``` > Note that GitHub IdP must be properly configured for the example to work: > * authority delegation must be enabled > * tokenPrefix must be set to \"github/\" > > You can learn more in > [the documentation](https://onedata.org/#/home/documentation/doc/administering_onedata/openid_saml_configuration/openid_saml_configuration_19_02[authority-delegation].html).   # noqa: E501

    OpenAPI spec version: 21.02.3
    Contact: info@onedata.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from onezone_client.api_client import ApiClient


class ShareApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_public_share_details(self, id, **kwargs):  # noqa: E501
        """Get public share details  # noqa: E501

        Returns the publicly available details of a specific share. This endpoint is available for anyone knowing the share Id, without authentication.  ***Example cURL requests***  **Get public share details** ```bash curl -X GET https://$ZONE_HOST/api/v3/onezone/shares/$SHARE_ID/public  {   \"shareId\": \"1f4b762b1380946e73aeca574c77f14c\",   \"name\": \"Experiment XYZ\",   \"description\": \"# Experiment XYZ\\nThis collection contains results from Experiment XYZ.\",   \"publicUrl\": \"https://example.com/shares/1f4b762b1380946e73aeca574c77f14c\",   \"publicRestUrl\": \"https://example.com/api/v3/onezone/shares/1f4b762b1380946e73aeca574c77f14c/public\",   \"fileType\": \"dir\",   \"rootFileId\": \"00000000006CB663736861726547756964233339643236366165646365\\   6266666164353939663761373734313235363166342336656331613534313362366634653\\   2623031613563383561386664373937653223316634623736326231333830393436653733\\   6165636135373463373766313463\",   \"handleId\" \"70570c0ebcd081835ca29560708fd98f\",   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_public_share_details(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Share Id. (required)
        :return: Share
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_public_share_details_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_public_share_details_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_public_share_details_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get public share details  # noqa: E501

        Returns the publicly available details of a specific share. This endpoint is available for anyone knowing the share Id, without authentication.  ***Example cURL requests***  **Get public share details** ```bash curl -X GET https://$ZONE_HOST/api/v3/onezone/shares/$SHARE_ID/public  {   \"shareId\": \"1f4b762b1380946e73aeca574c77f14c\",   \"name\": \"Experiment XYZ\",   \"description\": \"# Experiment XYZ\\nThis collection contains results from Experiment XYZ.\",   \"publicUrl\": \"https://example.com/shares/1f4b762b1380946e73aeca574c77f14c\",   \"publicRestUrl\": \"https://example.com/api/v3/onezone/shares/1f4b762b1380946e73aeca574c77f14c/public\",   \"fileType\": \"dir\",   \"rootFileId\": \"00000000006CB663736861726547756964233339643236366165646365\\   6266666164353939663761373734313235363166342336656331613534313362366634653\\   2623031613563383561386664373937653223316634623736326231333830393436653733\\   6165636135373463373766313463\",   \"handleId\" \"70570c0ebcd081835ca29560708fd98f\",   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_public_share_details_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Share Id. (required)
        :return: Share
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
                    " to method get_public_share_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_public_share_details`")  # noqa: E501

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
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/shares/{id}/public', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Share',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_share(self, id, **kwargs):  # noqa: E501
        """Get share details  # noqa: E501

        Returns the private details about a specific share.  NOTE: Only Oneprovider API supports creating / deleting shares and is preferred for all share operations. Onezone API is limited to retrieving and modifying share details.  This operation requires `space_view` privilege in space where share is created or `oz_shares_view` admin privilege.  ***Example cURL requests***  **Get share details** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/shares/$SHARE_ID  {   \"shareId\": \"1f4b762b1380946e73aeca574c77f14c\",   \"name\": \"Experiment XYZ\",   \"description\": \"# Experiment XYZ\\nThis collection contains results from Experiment XYZ.\",   \"publicUrl\": \"https://example.com/shares/1f4b762b1380946e73aeca574c77f14c\",   \"publicRestUrl\": \"https://example.com/api/v3/onezone/shares/1f4b762b1380946e73aeca574c77f14c/public\",   \"fileType\": \"dir\",   \"rootFileId\": \"00000000006CB663736861726547756964233339643236366165646365\\   6266666164353939663761373734313235363166342336656331613534313362366634653\\   2623031613563383561386664373937653223316634623736326231333830393436653733\\   6165636135373463373766313463\",   \"spaceId\": \"6ec1a5413b6f4e2b01a5c85a8fd797e2\",   \"handleId\" \"70570c0ebcd081835ca29560708fd98f\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_share(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Share Id. (required)
        :return: Share
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_share_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_share_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_share_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get share details  # noqa: E501

        Returns the private details about a specific share.  NOTE: Only Oneprovider API supports creating / deleting shares and is preferred for all share operations. Onezone API is limited to retrieving and modifying share details.  This operation requires `space_view` privilege in space where share is created or `oz_shares_view` admin privilege.  ***Example cURL requests***  **Get share details** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/shares/$SHARE_ID  {   \"shareId\": \"1f4b762b1380946e73aeca574c77f14c\",   \"name\": \"Experiment XYZ\",   \"description\": \"# Experiment XYZ\\nThis collection contains results from Experiment XYZ.\",   \"publicUrl\": \"https://example.com/shares/1f4b762b1380946e73aeca574c77f14c\",   \"publicRestUrl\": \"https://example.com/api/v3/onezone/shares/1f4b762b1380946e73aeca574c77f14c/public\",   \"fileType\": \"dir\",   \"rootFileId\": \"00000000006CB663736861726547756964233339643236366165646365\\   6266666164353939663761373734313235363166342336656331613534313362366634653\\   2623031613563383561386664373937653223316634623736326231333830393436653733\\   6165636135373463373766313463\",   \"spaceId\": \"6ec1a5413b6f4e2b01a5c85a8fd797e2\",   \"handleId\" \"70570c0ebcd081835ca29560708fd98f\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_share_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Share Id. (required)
        :return: Share
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
                    " to method get_share" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_share`")  # noqa: E501

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
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/shares/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Share',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_shared_data(self, file_id, subpath, **kwargs):  # noqa: E501
        """Get shared file or directory data  # noqa: E501

        This endpoint can be used to fetch publicly available information and content of a shared file or directory knowing its Id, without any authentication. It redirects to the corresponding REST endpoint in one of the supporting Oneproviders. The Oneprovider is chosen dynamically and may change in time, so the redirection URL should not be cached.  The endpoint accepts only identifiers of shared files/directories and will reject requests if a containing share is deleted. The shared file/directory Id can be acquired either by fetching public share details or by listing a shared directory.  The provided query string (if any) is preserved during redirection - consult corresponding Oneprovider REST endpoints for possible options.  Currently, publicly available operations are: * `{...}/$FILE_ID/content` - download file or directory content   (see Oneprovider [REST endpoint](https://onedata.org/#/home/api/latest/oneprovider?anchor=operation/download_file_content))  * `{...}/$FILE_ID/children` - list directory files and subdirectories   (see Oneprovider [REST endpoint](https://onedata.org/#/home/api/latest/oneprovider?anchor=operation/list_children))  * `{...}/$FILE_ID` - get basic attributes of a file or directory   (see Oneprovider [REST endpoint](https://onedata.org/#/home/api/latest/oneprovider?anchor=operation/get_attrs))  * `{...}/$FILE_ID/metadata/xattrs` - get custom extended attributes (xattrs) associated with a file or directory   (see Oneprovider [REST endpoint](https://onedata.org/#/home/api/latest/oneprovider?anchor=operation/get_xattrs))  * `{...}/$FILE_ID/metadata/json` - get custom JSON metadata associated with a file or directory   (see Oneprovider [REST endpoint](https://onedata.org/#/home/api/latest/oneprovider?anchor=operation/get_json_metadata))  * `{...}/$FILE_ID/metadata/rdf` - get custom RDF metadata associated with a file or directory   (see Oneprovider [REST endpoint](https://onedata.org/#/home/api/latest/oneprovider?anchor=operation/get_rdf_metadata))  The endpoint will return `503 Service Unavailable` when there is no suitable Oneprovider to handle the request and `501 Not Implemented` when all available Oneproviders are in versions older than `20.02.*`. If an invalid subpath is requested, the target Oneprovider will respond with a proper error.  ***Example cURL requests***  **Get shared file or directory data** ```bash curl -v -X GET https://$ZONE_HOST/api/v3/onezone/shares/data/$FILE_ID/content  < HTTP/1.1 307 Temporary Redirect < location: https://provider.example.com/api/v3/oneprovider/data/$FILE_ID/content  # -------------------------------------------------------------------------------  curl -v -X GET https://$ZONE_HOST/api/v3/onezone/shares/data/$FILE_ID/children?limit=3  < HTTP/1.1 307 Temporary Redirect < location: https://provider.example.com/api/v3/oneprovider/data/$FILE_ID/children?limit=3  # -------------------------------------------------------------------------------  # automatically follow redirects with -L option, request a byte range curl -L -X GET https://$ZONE_HOST/api/v3/onezone/shares/data/$FILE_ID/content \\ -H \"Range: bytes=5-8\"  fghi ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_shared_data(file_id, subpath, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file_id: Shared file/directory Id. (required)
        :param str subpath: Subpath corresponding to desired [Oneprovider REST API](https://onedata.org/#/home/api/latest/oneprovider?anchor=tag/Basic-File-Operations) operation.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_shared_data_with_http_info(file_id, subpath, **kwargs)  # noqa: E501
        else:
            (data) = self.get_shared_data_with_http_info(file_id, subpath, **kwargs)  # noqa: E501
            return data

    def get_shared_data_with_http_info(self, file_id, subpath, **kwargs):  # noqa: E501
        """Get shared file or directory data  # noqa: E501

        This endpoint can be used to fetch publicly available information and content of a shared file or directory knowing its Id, without any authentication. It redirects to the corresponding REST endpoint in one of the supporting Oneproviders. The Oneprovider is chosen dynamically and may change in time, so the redirection URL should not be cached.  The endpoint accepts only identifiers of shared files/directories and will reject requests if a containing share is deleted. The shared file/directory Id can be acquired either by fetching public share details or by listing a shared directory.  The provided query string (if any) is preserved during redirection - consult corresponding Oneprovider REST endpoints for possible options.  Currently, publicly available operations are: * `{...}/$FILE_ID/content` - download file or directory content   (see Oneprovider [REST endpoint](https://onedata.org/#/home/api/latest/oneprovider?anchor=operation/download_file_content))  * `{...}/$FILE_ID/children` - list directory files and subdirectories   (see Oneprovider [REST endpoint](https://onedata.org/#/home/api/latest/oneprovider?anchor=operation/list_children))  * `{...}/$FILE_ID` - get basic attributes of a file or directory   (see Oneprovider [REST endpoint](https://onedata.org/#/home/api/latest/oneprovider?anchor=operation/get_attrs))  * `{...}/$FILE_ID/metadata/xattrs` - get custom extended attributes (xattrs) associated with a file or directory   (see Oneprovider [REST endpoint](https://onedata.org/#/home/api/latest/oneprovider?anchor=operation/get_xattrs))  * `{...}/$FILE_ID/metadata/json` - get custom JSON metadata associated with a file or directory   (see Oneprovider [REST endpoint](https://onedata.org/#/home/api/latest/oneprovider?anchor=operation/get_json_metadata))  * `{...}/$FILE_ID/metadata/rdf` - get custom RDF metadata associated with a file or directory   (see Oneprovider [REST endpoint](https://onedata.org/#/home/api/latest/oneprovider?anchor=operation/get_rdf_metadata))  The endpoint will return `503 Service Unavailable` when there is no suitable Oneprovider to handle the request and `501 Not Implemented` when all available Oneproviders are in versions older than `20.02.*`. If an invalid subpath is requested, the target Oneprovider will respond with a proper error.  ***Example cURL requests***  **Get shared file or directory data** ```bash curl -v -X GET https://$ZONE_HOST/api/v3/onezone/shares/data/$FILE_ID/content  < HTTP/1.1 307 Temporary Redirect < location: https://provider.example.com/api/v3/oneprovider/data/$FILE_ID/content  # -------------------------------------------------------------------------------  curl -v -X GET https://$ZONE_HOST/api/v3/onezone/shares/data/$FILE_ID/children?limit=3  < HTTP/1.1 307 Temporary Redirect < location: https://provider.example.com/api/v3/oneprovider/data/$FILE_ID/children?limit=3  # -------------------------------------------------------------------------------  # automatically follow redirects with -L option, request a byte range curl -L -X GET https://$ZONE_HOST/api/v3/onezone/shares/data/$FILE_ID/content \\ -H \"Range: bytes=5-8\"  fghi ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_shared_data_with_http_info(file_id, subpath, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file_id: Shared file/directory Id. (required)
        :param str subpath: Subpath corresponding to desired [Oneprovider REST API](https://onedata.org/#/home/api/latest/oneprovider?anchor=tag/Basic-File-Operations) operation.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_id', 'subpath']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_shared_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_id' is set
        if ('file_id' not in params or
                params['file_id'] is None):
            raise ValueError("Missing the required parameter `file_id` when calling `get_shared_data`")  # noqa: E501
        # verify the required parameter 'subpath' is set
        if ('subpath' not in params or
                params['subpath'] is None):
            raise ValueError("Missing the required parameter `subpath` when calling `get_shared_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'file_id' in params:
            path_params['file_id'] = params['file_id']  # noqa: E501
        if 'subpath' in params:
            path_params['subpath'] = params['subpath']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/shares/data/{file_id}/{subpath}', 'GET',
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

    def list_shares(self, **kwargs):  # noqa: E501
        """List all shares  # noqa: E501

        Returns the list of all shares managed by the Onezone service.  NOTE: Only Oneprovider API supports creating / deleting shares and is preferred for all share operations. Onezone API is limited to retrieving and modifying share details.  This operation requires admin privilege `oz_shares_list`.  ***Example cURL requests***  **Get shares** ```bash curl -u admin:password -X GET https://$ZONE_HOST/api/v3/onezone/shares  {   \"shares\": [     \"303884afb761d91a7362b2841647bc08\",     \"32919d6a51bac9b040c7cb7961fdccf3\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_shares(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Shares
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_shares_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_shares_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_shares_with_http_info(self, **kwargs):  # noqa: E501
        """List all shares  # noqa: E501

        Returns the list of all shares managed by the Onezone service.  NOTE: Only Oneprovider API supports creating / deleting shares and is preferred for all share operations. Onezone API is limited to retrieving and modifying share details.  This operation requires admin privilege `oz_shares_list`.  ***Example cURL requests***  **Get shares** ```bash curl -u admin:password -X GET https://$ZONE_HOST/api/v3/onezone/shares  {   \"shares\": [     \"303884afb761d91a7362b2841647bc08\",     \"32919d6a51bac9b040c7cb7961fdccf3\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_shares_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Shares
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
                    " to method list_shares" % key
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
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/shares', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Shares',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_share(self, body, id, **kwargs):  # noqa: E501
        """Modify share details  # noqa: E501

        Updates the share details - name or description.  NOTE: Only Oneprovider API supports creating / deleting shares and is preferred for all share operations. Onezone API is limited to retrieving and modifying share details.  This operation requires privilege `space_manage_shares` in space in which the share was created or `oz_shares_update` admin privilege.  ***Example cURL requests***  **Modify share details** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"name\": \"NewShareName\", \"description\": \"# New description\"}' \\ https://$ZONE_HOST/api/v3/onezone/shares/$SHARE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_share(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SharesIdBody body: New share details (required)
        :param str id: Space Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_share_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_share_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def modify_share_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Modify share details  # noqa: E501

        Updates the share details - name or description.  NOTE: Only Oneprovider API supports creating / deleting shares and is preferred for all share operations. Onezone API is limited to retrieving and modifying share details.  This operation requires privilege `space_manage_shares` in space in which the share was created or `oz_shares_update` admin privilege.  ***Example cURL requests***  **Modify share details** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"name\": \"NewShareName\", \"description\": \"# New description\"}' \\ https://$ZONE_HOST/api/v3/onezone/shares/$SHARE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_share_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SharesIdBody body: New share details (required)
        :param str id: Space Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_share" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `modify_share`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `modify_share`")  # noqa: E501

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
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/shares/{id}', 'PATCH',
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
