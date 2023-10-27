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


class HandleApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_handle_group(self, id, gid, **kwargs):  # noqa: E501
        """Add handle group  # noqa: E501

        Allows to add a group to a handle.  This operation requires `handle_update` privilege or `oz_handles_add_relationships` and `oz_groups_add_relationships` admin privilege.  ***Example cURL requests***  **Add handle group** ```bash curl -u username:password -X PUT \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_handle_group(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str gid: The Id of the group to add to handle. (required)
        :param GroupsGidBody2 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_handle_group_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.add_handle_group_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def add_handle_group_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Add handle group  # noqa: E501

        Allows to add a group to a handle.  This operation requires `handle_update` privilege or `oz_handles_add_relationships` and `oz_groups_add_relationships` admin privilege.  ***Example cURL requests***  **Add handle group** ```bash curl -u username:password -X PUT \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_handle_group_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str gid: The Id of the group to add to handle. (required)
        :param GroupsGidBody2 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'gid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_handle_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_handle_group`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `add_handle_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'gid' in params:
            path_params['gid'] = params['gid']  # noqa: E501

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
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/handles/{id}/groups/{gid}', 'PUT',
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

    def add_handle_user(self, id, uid, **kwargs):  # noqa: E501
        """Add handle user  # noqa: E501

        Allows to add a user to a handle.  This operation requires `handle_update` privilege or `oz_handles_add_relationships` and `oz_users_add_relationships` admin privilege.  ***Example cURL requests***  **Add handle user** ```bash curl -u username:password -X PUT \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_handle_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str uid: The Id of the user to add to handle. (required)
        :param UsersUidBody3 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_handle_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.add_handle_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def add_handle_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Add handle user  # noqa: E501

        Allows to add a user to a handle.  This operation requires `handle_update` privilege or `oz_handles_add_relationships` and `oz_users_add_relationships` admin privilege.  ***Example cURL requests***  **Add handle user** ```bash curl -u username:password -X PUT \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_handle_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str uid: The Id of the user to add to handle. (required)
        :param UsersUidBody3 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'uid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_handle_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_handle_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `add_handle_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501

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
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/handles/{id}/users/{uid}', 'PUT',
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

    def get_effective_handle_group(self, id, gid, **kwargs):  # noqa: E501
        """Get effective handle group  # noqa: E501

        Returns the details of an effective group with access to handle.  This operation requires `handle_view` privilege or `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get effective handle group** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/effective_groups/$GROUP_ID  {   \"groupId\":\"HwUpk8jrwxKOe45uzLFX2GVa8lKEasj4q253sptVqF8\",   \"name\":\"Group name\",   \"type\":\"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_handle_group(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str gid: The Id of the group to add to handle. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_handle_group_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_handle_group_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def get_effective_handle_group_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Get effective handle group  # noqa: E501

        Returns the details of an effective group with access to handle.  This operation requires `handle_view` privilege or `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get effective handle group** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/effective_groups/$GROUP_ID  {   \"groupId\":\"HwUpk8jrwxKOe45uzLFX2GVa8lKEasj4q253sptVqF8\",   \"name\":\"Group name\",   \"type\":\"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_handle_group_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str gid: The Id of the group to add to handle. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'gid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_effective_handle_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_handle_group`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `get_effective_handle_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'gid' in params:
            path_params['gid'] = params['gid']  # noqa: E501

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
            '/handles/{id}/effective_groups/{gid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Group',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_effective_handle_user(self, id, uid, **kwargs):  # noqa: E501
        """Get effective handle user  # noqa: E501

        Returns effective handle user details.  This operation requires `handle_view` privilege or `oz_users_view` admin privilege.  ***Example cURL requests***  **Add handle user** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/effective_users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_handle_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str uid: The Id of the user to add to handle. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_handle_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_handle_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def get_effective_handle_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Get effective handle user  # noqa: E501

        Returns effective handle user details.  This operation requires `handle_view` privilege or `oz_users_view` admin privilege.  ***Example cURL requests***  **Add handle user** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/effective_users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_handle_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str uid: The Id of the user to add to handle. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_effective_handle_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_handle_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_effective_handle_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501

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
            '/handles/{id}/effective_users/{uid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_handle(self, id, **kwargs):  # noqa: E501
        """Get handle  # noqa: E501

        Returns the details of a specific handle.  This operation requires `handle_view` privilege or `oz_handles_view` admin privilege.  ***Example cURL requests***  **Get handle** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID  {   \"publicHandle\": \"10.5072/w95Zlng\",   \"handleId\": \"95b663a6467c72ab1256865efef9e387\",   \"handleServiceId\": \"97c27230017cd54c1220189e357322c4\",   \"resourceType\": \"Share\",   \"resourceId\": \"d6ee1aecf03b23f09756d6a49e435455\",   \"metadata\": \"<?xml version=\\\"1.0\\\"?>       <!DOCTYPE rdf:RDF SYSTEM \\\\\"http://dublincore.org/2000/12/01-dcmes-xml-dtd.dtd\\\">       <rdf:RDF xmlns:rdf=\\\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\\\"                xmlns:dc=\\\"http://purl.org/dc/elements/1.1/\\\">         <rdf:Description rdf:about=\\\"http://example.com/resouces/1\\\">           <dc:title>Example Resource</dc:title>           <dc:creator>John Doe</dc:creator>           <dc:publisher>MIT</dc:publisher>           <dc:date>2000-06-06</dc:date>         </rdf:Description>       </rdf:RDF>\",   \"timestamp\": \"1997-07-16T19:20\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_handle(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The handle Id. (required)
        :return: Handle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_handle_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_handle_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_handle_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get handle  # noqa: E501

        Returns the details of a specific handle.  This operation requires `handle_view` privilege or `oz_handles_view` admin privilege.  ***Example cURL requests***  **Get handle** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID  {   \"publicHandle\": \"10.5072/w95Zlng\",   \"handleId\": \"95b663a6467c72ab1256865efef9e387\",   \"handleServiceId\": \"97c27230017cd54c1220189e357322c4\",   \"resourceType\": \"Share\",   \"resourceId\": \"d6ee1aecf03b23f09756d6a49e435455\",   \"metadata\": \"<?xml version=\\\"1.0\\\"?>       <!DOCTYPE rdf:RDF SYSTEM \\\\\"http://dublincore.org/2000/12/01-dcmes-xml-dtd.dtd\\\">       <rdf:RDF xmlns:rdf=\\\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\\\"                xmlns:dc=\\\"http://purl.org/dc/elements/1.1/\\\">         <rdf:Description rdf:about=\\\"http://example.com/resouces/1\\\">           <dc:title>Example Resource</dc:title>           <dc:creator>John Doe</dc:creator>           <dc:publisher>MIT</dc:publisher>           <dc:date>2000-06-06</dc:date>         </rdf:Description>       </rdf:RDF>\",   \"timestamp\": \"1997-07-16T19:20\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_handle_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The handle Id. (required)
        :return: Handle
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
                    " to method get_handle" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_handle`")  # noqa: E501

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
            '/handles/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Handle',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_handle_group(self, id, gid, **kwargs):  # noqa: E501
        """Get handle group  # noqa: E501

        Returns the details of a group with access to handle.  This operation requires `handle_view` privilege or `oz_groups_view` admin privilege.  ***Example cURL requests***  **Add handle group** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/groups/$GROUP_ID  {   \"groupId\":\"HwUpk8jrwxKOe45uzLFX2GVa8lKEasj4q253sptVqF8\",   \"name\":\"Group name\",   \"type\":\"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_handle_group(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str gid: The Id of the group to add to handle. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_handle_group_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_handle_group_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def get_handle_group_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Get handle group  # noqa: E501

        Returns the details of a group with access to handle.  This operation requires `handle_view` privilege or `oz_groups_view` admin privilege.  ***Example cURL requests***  **Add handle group** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/groups/$GROUP_ID  {   \"groupId\":\"HwUpk8jrwxKOe45uzLFX2GVa8lKEasj4q253sptVqF8\",   \"name\":\"Group name\",   \"type\":\"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_handle_group_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str gid: The Id of the group to add to handle. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'gid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_handle_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_handle_group`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `get_handle_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'gid' in params:
            path_params['gid'] = params['gid']  # noqa: E501

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
            '/handles/{id}/groups/{gid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Group',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_handle_user(self, id, uid, **kwargs):  # noqa: E501
        """Get handle user  # noqa: E501

        Allows to add a user to a handle.  This operation requires `handle_view` privilege or `oz_users_view` admin privilege.  ***Example cURL requests***  **Get handle user** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_handle_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str uid: The Id of the user to add to handle. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_handle_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_handle_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def get_handle_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Get handle user  # noqa: E501

        Allows to add a user to a handle.  This operation requires `handle_view` privilege or `oz_users_view` admin privilege.  ***Example cURL requests***  **Get handle user** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_handle_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str uid: The Id of the user to add to handle. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_handle_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_handle_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_handle_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501

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
            '/handles/{id}/users/{uid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_public_handle_details(self, id, **kwargs):  # noqa: E501
        """Get public handle details  # noqa: E501

        Returns the publicly available details of a specific handle. This endpoint is available for anyone knowing the handle Id, without authentication.  ***Example cURL requests***  **Get public handle details** ```bash curl -X GET https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/public  {   \"handleId\": \"95b663a6467c72ab1256865efef9e387\",   \"publicHandle\": \"10.5072/w95Zlng\",   \"resourceType\": \"Share\",   \"resourceId\": \"d6ee1aecf03b23f09756d6a49e435455\",   \"metadata\": \"<?xml version=\\\"1.0\\\"?>       <!DOCTYPE rdf:RDF SYSTEM \\\\\"http://dublincore.org/2000/12/01-dcmes-xml-dtd.dtd\\\">       <rdf:RDF xmlns:rdf=\\\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\\\"                xmlns:dc=\\\"http://purl.org/dc/elements/1.1/\\\">         <rdf:Description rdf:about=\\\"http://example.com/resouces/1\\\">           <dc:title>Example Resource</dc:title>           <dc:creator>John Doe</dc:creator>           <dc:publisher>MIT</dc:publisher>           <dc:date>2000-06-06</dc:date>         </rdf:Description>       </rdf:RDF>\",   \"timestamp\": \"1997-07-16T19:20\",   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_public_handle_details(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The handle Id. (required)
        :return: Handle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_public_handle_details_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_public_handle_details_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_public_handle_details_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get public handle details  # noqa: E501

        Returns the publicly available details of a specific handle. This endpoint is available for anyone knowing the handle Id, without authentication.  ***Example cURL requests***  **Get public handle details** ```bash curl -X GET https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/public  {   \"handleId\": \"95b663a6467c72ab1256865efef9e387\",   \"publicHandle\": \"10.5072/w95Zlng\",   \"resourceType\": \"Share\",   \"resourceId\": \"d6ee1aecf03b23f09756d6a49e435455\",   \"metadata\": \"<?xml version=\\\"1.0\\\"?>       <!DOCTYPE rdf:RDF SYSTEM \\\\\"http://dublincore.org/2000/12/01-dcmes-xml-dtd.dtd\\\">       <rdf:RDF xmlns:rdf=\\\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\\\"                xmlns:dc=\\\"http://purl.org/dc/elements/1.1/\\\">         <rdf:Description rdf:about=\\\"http://example.com/resouces/1\\\">           <dc:title>Example Resource</dc:title>           <dc:creator>John Doe</dc:creator>           <dc:publisher>MIT</dc:publisher>           <dc:date>2000-06-06</dc:date>         </rdf:Description>       </rdf:RDF>\",   \"timestamp\": \"1997-07-16T19:20\",   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_public_handle_details_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The handle Id. (required)
        :return: Handle
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
                    " to method get_public_handle_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_public_handle_details`")  # noqa: E501

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
            '/handles/{id}/public', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Handle',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def handle_service_register_handle(self, body, **kwargs):  # noqa: E501
        """Register handle  # noqa: E501

        Allows to register a new handle identifier, using a specific handle service.  The handle service must be registered in Onedata separately.  See also:   [Create a new handle for the current user](#operation/create_user_handle)   [Create a new handle for given group](#operation/create_group_handle)    This operation requires `handle_service_register_handle` privilege, which needs to be assigned to a specific handle service or `oz_handles_create` admin privilege.  ***Example cURL requests***  **Register handle** ```bash curl -u username:password -X POST -H \"Content-type: application/json\" \\ -d '{ \"handleServiceId\": \"ddb06ed993bae95f2f430664fff122f7\", \"resourceType\": \"Share\", \"resourceId\": \"4fa683cbda8d8f686d15d42720af431d\", \"metadata\": \"<?xml version=\\'1.0\\'?>...\" }' \\ https://$ZONE_HOST/api/v3/onezone/handles ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_service_register_handle(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HandleRegistrationRequest body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.handle_service_register_handle_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.handle_service_register_handle_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def handle_service_register_handle_with_http_info(self, body, **kwargs):  # noqa: E501
        """Register handle  # noqa: E501

        Allows to register a new handle identifier, using a specific handle service.  The handle service must be registered in Onedata separately.  See also:   [Create a new handle for the current user](#operation/create_user_handle)   [Create a new handle for given group](#operation/create_group_handle)    This operation requires `handle_service_register_handle` privilege, which needs to be assigned to a specific handle service or `oz_handles_create` admin privilege.  ***Example cURL requests***  **Register handle** ```bash curl -u username:password -X POST -H \"Content-type: application/json\" \\ -d '{ \"handleServiceId\": \"ddb06ed993bae95f2f430664fff122f7\", \"resourceType\": \"Share\", \"resourceId\": \"4fa683cbda8d8f686d15d42720af431d\", \"metadata\": \"<?xml version=\\'1.0\\'?>...\" }' \\ https://$ZONE_HOST/api/v3/onezone/handles ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_service_register_handle_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HandleRegistrationRequest body: (required)
        :return: None
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
                    " to method handle_service_register_handle" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `handle_service_register_handle`")  # noqa: E501

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
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/handles', 'POST',
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

    def handle_update(self, body, id, **kwargs):  # noqa: E501
        """Modify handle  # noqa: E501

        Allows to update a registered handle, currently it only allows to modify the handle metadata property.  This operation requires `handle_update` privilege or `oz_handles_update` admin privilege.  ***Example cURL requests***  **Modify handle resource** ```bash curl -u username:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"metadata\": \"<?xml...\"}' \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_update(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HandlesIdBody body: (required)
        :param str id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.handle_update_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.handle_update_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def handle_update_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Modify handle  # noqa: E501

        Allows to update a registered handle, currently it only allows to modify the handle metadata property.  This operation requires `handle_update` privilege or `oz_handles_update` admin privilege.  ***Example cURL requests***  **Modify handle resource** ```bash curl -u username:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"metadata\": \"<?xml...\"}' \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_update_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HandlesIdBody body: (required)
        :param str id: (required)
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
                    " to method handle_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `handle_update`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `handle_update`")  # noqa: E501

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
            '/handles/{id}', 'PATCH',
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

    def list_effective_group_handle_privileges(self, id, gid, **kwargs):  # noqa: E501
        """List effective group's handle privileges  # noqa: E501

        Returns the list of effective group's (`{gid}`) privileges in a handle (`{id}`).  Effective privileges are a sum of group's privileges and privileges inherited from its parent group memberships.  This operation requires `handle_view` privilege or `oz_handles_view_privileges` admin privilege.  ***Example cURL requests***  **List effective group's privileges in a handle** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/effective_groups/$GROUP_ID/privileges  {   \"privileges\": [     \"handle_delete\",     \"handle_update\",     \"handle_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_handle_privileges(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str gid: Group Id. (required)
        :return: InlineResponse20016
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_group_handle_privileges_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_group_handle_privileges_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def list_effective_group_handle_privileges_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """List effective group's handle privileges  # noqa: E501

        Returns the list of effective group's (`{gid}`) privileges in a handle (`{id}`).  Effective privileges are a sum of group's privileges and privileges inherited from its parent group memberships.  This operation requires `handle_view` privilege or `oz_handles_view_privileges` admin privilege.  ***Example cURL requests***  **List effective group's privileges in a handle** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/effective_groups/$GROUP_ID/privileges  {   \"privileges\": [     \"handle_delete\",     \"handle_update\",     \"handle_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_handle_privileges_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str gid: Group Id. (required)
        :return: InlineResponse20016
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'gid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_effective_group_handle_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_group_handle_privileges`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `list_effective_group_handle_privileges`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'gid' in params:
            path_params['gid'] = params['gid']  # noqa: E501

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
            '/handles/{id}/effective_groups/{gid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20016',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_effective_handle_groups(self, id, **kwargs):  # noqa: E501
        """Get effective handle groups  # noqa: E501

        Returns effective groups with access to a handle instance.  This operation requires `handle_view` privilege or `oz_handles_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/effective_groups  {   \"groups\": [     \"16969b9d4d1f1457b7c1d061022f6b96\",     \"a6c6e47cc477aa4d3f8c61ce71df9850\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_handle_groups(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :return: Groups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_handle_groups_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_handle_groups_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_effective_handle_groups_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get effective handle groups  # noqa: E501

        Returns effective groups with access to a handle instance.  This operation requires `handle_view` privilege or `oz_handles_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/effective_groups  {   \"groups\": [     \"16969b9d4d1f1457b7c1d061022f6b96\",     \"a6c6e47cc477aa4d3f8c61ce71df9850\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_handle_groups_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :return: Groups
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
                    " to method list_effective_handle_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_handle_groups`")  # noqa: E501

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
            '/handles/{id}/effective_groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Groups',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_effective_handle_users(self, id, **kwargs):  # noqa: E501
        """List effective handle users  # noqa: E501

        Returns effective list of users with access to a handle instance.  This operation requires `handle_view` privilege or `oz_handles_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/effective_users  {   \"users\": [     \"5bcd19ea6b3e308347fd12ccefc96b09\",     \"cef7eb7463ed17acd3ffd9bc53b796ea\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_handle_users(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_handle_users_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_handle_users_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_effective_handle_users_with_http_info(self, id, **kwargs):  # noqa: E501
        """List effective handle users  # noqa: E501

        Returns effective list of users with access to a handle instance.  This operation requires `handle_view` privilege or `oz_handles_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/effective_users  {   \"users\": [     \"5bcd19ea6b3e308347fd12ccefc96b09\",     \"cef7eb7463ed17acd3ffd9bc53b796ea\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_handle_users_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :return: Users
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
                    " to method list_effective_handle_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_handle_users`")  # noqa: E501

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
            '/handles/{id}/effective_users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Users',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_effective_user_handle_privileges(self, id, uid, **kwargs):  # noqa: E501
        """List effective user's handle privileges  # noqa: E501

        Returns the list of effective user's (`{uid}`) privileges in a handle (`{id}`).  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation requires `handle_view` privilege or `oz_handles_view_privileges` admin privilege.  ***Example cURL requests***  **List effective user's privileges in a handle** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/effective_users/$USER_ID/privileges  {   \"privileges\": [     \"handle_delete\",     \"handle_update\",     \"handle_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_user_handle_privileges(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str uid: User Id. (required)
        :return: InlineResponse20016
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_user_handle_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_user_handle_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def list_effective_user_handle_privileges_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """List effective user's handle privileges  # noqa: E501

        Returns the list of effective user's (`{uid}`) privileges in a handle (`{id}`).  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation requires `handle_view` privilege or `oz_handles_view_privileges` admin privilege.  ***Example cURL requests***  **List effective user's privileges in a handle** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/effective_users/$USER_ID/privileges  {   \"privileges\": [     \"handle_delete\",     \"handle_update\",     \"handle_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_user_handle_privileges_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str uid: User Id. (required)
        :return: InlineResponse20016
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_effective_user_handle_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_user_handle_privileges`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `list_effective_user_handle_privileges`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501

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
            '/handles/{id}/effective_users/{uid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20016',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_group_handle_privileges(self, id, gid, **kwargs):  # noqa: E501
        """List group's handle privileges  # noqa: E501

        Returns the list of group's (`{gid}`) privileges in a handle (`{id}`).  This operation requires `handle_view` privilege or `oz_handles_view_privileges` admin privilege.  ***Example cURL requests***  **List group's privileges in a handle** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/groups/$GROUP_ID/privileges  {   \"privileges\": [     \"handle_delete\",     \"handle_update\",     \"handle_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_handle_privileges(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str gid: Group Id. (required)
        :return: InlineResponse20016
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_group_handle_privileges_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_group_handle_privileges_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def list_group_handle_privileges_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """List group's handle privileges  # noqa: E501

        Returns the list of group's (`{gid}`) privileges in a handle (`{id}`).  This operation requires `handle_view` privilege or `oz_handles_view_privileges` admin privilege.  ***Example cURL requests***  **List group's privileges in a handle** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/groups/$GROUP_ID/privileges  {   \"privileges\": [     \"handle_delete\",     \"handle_update\",     \"handle_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_handle_privileges_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str gid: Group Id. (required)
        :return: InlineResponse20016
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'gid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_group_handle_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_group_handle_privileges`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `list_group_handle_privileges`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'gid' in params:
            path_params['gid'] = params['gid']  # noqa: E501

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
            '/handles/{id}/groups/{gid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20016',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_handle_groups(self, id, **kwargs):  # noqa: E501
        """List handle groups  # noqa: E501

        Returns all groups with access to a handle instance  This operation requires `handle_view` privilege or `oz_handles_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/groups  {   \"groups\": [     \"16969b9d4d1f1457b7c1d061022f6b96\",     \"a6c6e47cc477aa4d3f8c61ce71df9850\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_handle_groups(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :return: Groups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_handle_groups_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_handle_groups_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_handle_groups_with_http_info(self, id, **kwargs):  # noqa: E501
        """List handle groups  # noqa: E501

        Returns all groups with access to a handle instance  This operation requires `handle_view` privilege or `oz_handles_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/groups  {   \"groups\": [     \"16969b9d4d1f1457b7c1d061022f6b96\",     \"a6c6e47cc477aa4d3f8c61ce71df9850\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_handle_groups_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :return: Groups
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
                    " to method list_handle_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_handle_groups`")  # noqa: E501

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
            '/handles/{id}/groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Groups',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_handle_privileges(self, **kwargs):  # noqa: E501
        """List all handle privileges  # noqa: E501

        Returns list of all possible handle privileges.  This endpoint does not require authentication.  ***Example cURL requests***  **Get list of all handle privileges** ```bash curl https://$ZONE_HOST/api/v3/onezone/handles/privileges  {   \"admin\": [     \"handle_view\",     \"handle_update\",     \"handle_delete\"   ],   \"member\": [     \"handle_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_handle_privileges(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20015
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_handle_privileges_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_handle_privileges_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_handle_privileges_with_http_info(self, **kwargs):  # noqa: E501
        """List all handle privileges  # noqa: E501

        Returns list of all possible handle privileges.  This endpoint does not require authentication.  ***Example cURL requests***  **Get list of all handle privileges** ```bash curl https://$ZONE_HOST/api/v3/onezone/handles/privileges  {   \"admin\": [     \"handle_view\",     \"handle_update\",     \"handle_delete\"   ],   \"member\": [     \"handle_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_handle_privileges_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20015
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
                    " to method list_handle_privileges" % key
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
            '/handles/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20015',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_handle_users(self, id, **kwargs):  # noqa: E501
        """List handle users  # noqa: E501

        Returns all users with access to a handle instance  This operation requires `handle_view` privilege or `oz_handles_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/users  {   \"users\": [     \"5bcd19ea6b3e308347fd12ccefc96b09\",     \"cef7eb7463ed17acd3ffd9bc53b796ea\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_handle_users(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_handle_users_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_handle_users_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_handle_users_with_http_info(self, id, **kwargs):  # noqa: E501
        """List handle users  # noqa: E501

        Returns all users with access to a handle instance  This operation requires `handle_view` privilege or `oz_handles_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/users  {   \"users\": [     \"5bcd19ea6b3e308347fd12ccefc96b09\",     \"cef7eb7463ed17acd3ffd9bc53b796ea\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_handle_users_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :return: Users
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
                    " to method list_handle_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_handle_users`")  # noqa: E501

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
            '/handles/{id}/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Users',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_handles(self, **kwargs):  # noqa: E501
        """List handles  # noqa: E501

        Returns the list of Ids of all handles registered in Onezone.  This operation requires `oz_handles_list` admin privilege.  ***Example cURL requests***  **Get handles** ```bash curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/handles  {   \"handles\": [     \"0fe7c8a20ffdf07480c46f084bc3b8d5\",     \"302da048de67e2ea05f0af1d0fe7c8a2\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_handles(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Handles
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_handles_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_handles_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_handles_with_http_info(self, **kwargs):  # noqa: E501
        """List handles  # noqa: E501

        Returns the list of Ids of all handles registered in Onezone.  This operation requires `oz_handles_list` admin privilege.  ***Example cURL requests***  **Get handles** ```bash curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/handles  {   \"handles\": [     \"0fe7c8a20ffdf07480c46f084bc3b8d5\",     \"302da048de67e2ea05f0af1d0fe7c8a2\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_handles_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Handles
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
                    " to method list_handles" % key
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
            '/handles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Handles',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_user_handle_privileges(self, id, uid, **kwargs):  # noqa: E501
        """List user handle privileges  # noqa: E501

        Returns the list of user's (`{uid}`) privileges in a handle (`{id}`).  This operation requires `handle_view` privilege or `oz_handles_view_privileges` admin privilege.  ***Example cURL requests***  **List handle user privileges** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/users/$USER_ID/privileges  {   \"privileges\": [     \"handle_delete\",     \"handle_update\",     \"handle_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_handle_privileges(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str uid: User Id. (required)
        :return: InlineResponse20016
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_handle_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_user_handle_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def list_user_handle_privileges_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """List user handle privileges  # noqa: E501

        Returns the list of user's (`{uid}`) privileges in a handle (`{id}`).  This operation requires `handle_view` privilege or `oz_handles_view_privileges` admin privilege.  ***Example cURL requests***  **List handle user privileges** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/users/$USER_ID/privileges  {   \"privileges\": [     \"handle_delete\",     \"handle_update\",     \"handle_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_handle_privileges_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str uid: User Id. (required)
        :return: InlineResponse20016
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_user_handle_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_user_handle_privileges`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `list_user_handle_privileges`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501

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
            '/handles/{id}/users/{uid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20016',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_handle(self, id, **kwargs):  # noqa: E501
        """Unregister handle  # noqa: E501

        Allows to unregister a registered handle.  This operation requires `handle_delete` privilege or `oz_handles_delete` admin privilege.  ***Example cURL requests***  **Unregister handle** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_handle(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_handle_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_handle_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def remove_handle_with_http_info(self, id, **kwargs):  # noqa: E501
        """Unregister handle  # noqa: E501

        Allows to unregister a registered handle.  This operation requires `handle_delete` privilege or `oz_handles_delete` admin privilege.  ***Example cURL requests***  **Unregister handle** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_handle_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
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
                    " to method remove_handle" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_handle`")  # noqa: E501

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
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/handles/{id}', 'DELETE',
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

    def remove_handle_group(self, id, gid, **kwargs):  # noqa: E501
        """Remove handle group  # noqa: E501

        Allows to remove a group from access to a handle.  This operation requires `handle_update` privilege or `oz_handles_remove_relationships` and `oz_groups_remove_relationships` admin privilege.  ***Example cURL requests***  **Remove handle service group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_handle_group(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str gid: The Id of the group to remove from handle. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_handle_group_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_handle_group_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def remove_handle_group_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Remove handle group  # noqa: E501

        Allows to remove a group from access to a handle.  This operation requires `handle_update` privilege or `oz_handles_remove_relationships` and `oz_groups_remove_relationships` admin privilege.  ***Example cURL requests***  **Remove handle service group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_handle_group_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str gid: The Id of the group to remove from handle. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'gid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_handle_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_handle_group`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `remove_handle_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'gid' in params:
            path_params['gid'] = params['gid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/handles/{id}/groups/{gid}', 'DELETE',
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

    def remove_handle_user(self, id, uid, **kwargs):  # noqa: E501
        """Remove handle user  # noqa: E501

        Allows to revoke users access to a handle.  This operation requires `handle_update` privilege or `oz_handles_remove_relationships` and `oz_users_remove_relationships` admin privilege.  ***Example cURL requests***  **Remove handle service user** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_handle_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str uid: The Id of the user to remove from handle. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_handle_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_handle_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def remove_handle_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Remove handle user  # noqa: E501

        Allows to revoke users access to a handle.  This operation requires `handle_update` privilege or `oz_handles_remove_relationships` and `oz_users_remove_relationships` admin privilege.  ***Example cURL requests***  **Remove handle service user** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_handle_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle Id. (required)
        :param str uid: The Id of the user to remove from handle. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_handle_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_handle_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `remove_handle_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/handles/{id}/users/{uid}', 'DELETE',
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

    def update_group_handle_privileges(self, body, id, gid, **kwargs):  # noqa: E501
        """Update handle groups privileges  # noqa: E501

        Updates group's (`{gid}`) privileges in a handle (`{id}`).  This operation requires `handle_update` privilege or `oz_handles_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update group's privileges in a handle** ```bash curl -u username:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"handle_view\"], \"revoke\": [\"handle_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/groups/$GROUP_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_group_handle_privileges(body, id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HandlePrivilegesUpdate body: Handle privileges update request. (required)
        :param str id: Handle Id. (required)
        :param str gid: Group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_group_handle_privileges_with_http_info(body, id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_group_handle_privileges_with_http_info(body, id, gid, **kwargs)  # noqa: E501
            return data

    def update_group_handle_privileges_with_http_info(self, body, id, gid, **kwargs):  # noqa: E501
        """Update handle groups privileges  # noqa: E501

        Updates group's (`{gid}`) privileges in a handle (`{id}`).  This operation requires `handle_update` privilege or `oz_handles_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update group's privileges in a handle** ```bash curl -u username:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"handle_view\"], \"revoke\": [\"handle_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/groups/$GROUP_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_group_handle_privileges_with_http_info(body, id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HandlePrivilegesUpdate body: Handle privileges update request. (required)
        :param str id: Handle Id. (required)
        :param str gid: Group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id', 'gid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_group_handle_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_group_handle_privileges`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_group_handle_privileges`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `update_group_handle_privileges`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'gid' in params:
            path_params['gid'] = params['gid']  # noqa: E501

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
            '/handles/{id}/groups/{gid}/privileges', 'PATCH',
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

    def update_handle_user_privileges(self, body, id, uid, **kwargs):  # noqa: E501
        """Update user handle privileges  # noqa: E501

        Updates user's (`{uid}`) privileges in a handle (`{id}`).  This operation requires `handle_update` privilege or `oz_handles_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update group's privileges in a handle** ```bash curl -u username:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"handle_view\"], \"revoke\": [\"handle_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/users/$USER_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_handle_user_privileges(body, id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HandlePrivilegesUpdate body: Handle privileges update request. (required)
        :param str id: Handle Id. (required)
        :param str uid: User Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_handle_user_privileges_with_http_info(body, id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_handle_user_privileges_with_http_info(body, id, uid, **kwargs)  # noqa: E501
            return data

    def update_handle_user_privileges_with_http_info(self, body, id, uid, **kwargs):  # noqa: E501
        """Update user handle privileges  # noqa: E501

        Updates user's (`{uid}`) privileges in a handle (`{id}`).  This operation requires `handle_update` privilege or `oz_handles_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update group's privileges in a handle** ```bash curl -u username:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"handle_view\"], \"revoke\": [\"handle_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/handles/$HANDLE_ID/users/$USER_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_handle_user_privileges_with_http_info(body, id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HandlePrivilegesUpdate body: Handle privileges update request. (required)
        :param str id: Handle Id. (required)
        :param str uid: User Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id', 'uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_handle_user_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_handle_user_privileges`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_handle_user_privileges`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `update_handle_user_privileges`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501

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
            '/handles/{id}/users/{uid}/privileges', 'PATCH',
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
