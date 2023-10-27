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


class HandleServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_handle_service(self, body, **kwargs):  # noqa: E501
        """Add handle service  # noqa: E501

        Allows to register a new handle service.  This operation requires `oz_handle_services_create` admin privilege.  See also:   [Create a new handle service for the current user](#operation/add_user_handle_service)   [Create a new handle service for given group](#operation/add_group_handle_service)    ***Example cURL requests***  **Add handle services** ```bash curl -u username:password -X POST -H \"Content-type: application/json\" \\ -d '{ ... }' https://$ZONE_HOST/api/v3/onezone/handle_services ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_handle_service(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HandleService body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_handle_service_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_handle_service_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def add_handle_service_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add handle service  # noqa: E501

        Allows to register a new handle service.  This operation requires `oz_handle_services_create` admin privilege.  See also:   [Create a new handle service for the current user](#operation/add_user_handle_service)   [Create a new handle service for given group](#operation/add_group_handle_service)    ***Example cURL requests***  **Add handle services** ```bash curl -u username:password -X POST -H \"Content-type: application/json\" \\ -d '{ ... }' https://$ZONE_HOST/api/v3/onezone/handle_services ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_handle_service_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HandleService body: (required)
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
                    " to method add_handle_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_handle_service`")  # noqa: E501

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
            '/handle_services', 'POST',
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

    def add_handle_service_group(self, id, gid, **kwargs):  # noqa: E501
        """Add handle service group  # noqa: E501

        Allows to add a group to a handle service.  This operation requires `handle_service_update` privilege or `oz_handle_services_add_relationships` and `oz_groups_add_relationships` admin privilege.  ***Example cURL requests***  **Add handle service user** ```bash curl -u username:password -X PUT \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_handle_service_group(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str gid: The Id of the group to add to handle service. (required)
        :param GroupsGidBody1 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_handle_service_group_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.add_handle_service_group_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def add_handle_service_group_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Add handle service group  # noqa: E501

        Allows to add a group to a handle service.  This operation requires `handle_service_update` privilege or `oz_handle_services_add_relationships` and `oz_groups_add_relationships` admin privilege.  ***Example cURL requests***  **Add handle service user** ```bash curl -u username:password -X PUT \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_handle_service_group_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str gid: The Id of the group to add to handle service. (required)
        :param GroupsGidBody1 body:
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
                    " to method add_handle_service_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_handle_service_group`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `add_handle_service_group`")  # noqa: E501

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
            '/handle_services/{id}/groups/{gid}', 'PUT',
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

    def add_handle_service_user(self, id, uid, **kwargs):  # noqa: E501
        """Add handle service user  # noqa: E501

        Allows to add a user to a handle service.  This operation requires `handle_service_update` privilege or `oz_handle_services_add_relationships` and `oz_users_add_relationships` admin privilege.  ***Example cURL requests***  **Add handle service user** ```bash curl -u username:password -X PUT \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_handle_service_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str uid: The Id of the user to add to handle service. (required)
        :param UsersUidBody2 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_handle_service_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.add_handle_service_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def add_handle_service_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Add handle service user  # noqa: E501

        Allows to add a user to a handle service.  This operation requires `handle_service_update` privilege or `oz_handle_services_add_relationships` and `oz_users_add_relationships` admin privilege.  ***Example cURL requests***  **Add handle service user** ```bash curl -u username:password -X PUT \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_handle_service_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str uid: The Id of the user to add to handle service. (required)
        :param UsersUidBody2 body:
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
                    " to method add_handle_service_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_handle_service_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `add_handle_service_user`")  # noqa: E501

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
            '/handle_services/{id}/users/{uid}', 'PUT',
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

    def get_effective_handle_service_group(self, id, gid, **kwargs):  # noqa: E501
        """Get effective handle service group  # noqa: E501

        Get details of a group with effective access to handle service.  This operation requires `handle_service_view` privilege or `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get effective handle service group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/effective_groups/$GROUP_ID  {   \"groupId\":\"HwUpk8jrwxKOe45uzLFX2GVa8lKEasj4q253sptVqF8\",   \"name\":\"Group name\",   \"type\":\"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_handle_service_group(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str gid: The Id of the group to return information about. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_handle_service_group_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_handle_service_group_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def get_effective_handle_service_group_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Get effective handle service group  # noqa: E501

        Get details of a group with effective access to handle service.  This operation requires `handle_service_view` privilege or `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get effective handle service group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/effective_groups/$GROUP_ID  {   \"groupId\":\"HwUpk8jrwxKOe45uzLFX2GVa8lKEasj4q253sptVqF8\",   \"name\":\"Group name\",   \"type\":\"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_handle_service_group_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str gid: The Id of the group to return information about. (required)
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
                    " to method get_effective_handle_service_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_handle_service_group`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `get_effective_handle_service_group`")  # noqa: E501

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
            '/handle_services/{id}/effective_groups/{gid}', 'GET',
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

    def get_effective_handle_service_user(self, id, uid, **kwargs):  # noqa: E501
        """Get effective handle service user  # noqa: E501

        Allows to get a user to a handle service.  This operation requires `handle_service_view` privilege or `oz_users_view` admin privilege.  ***Example cURL requests***  **Get effective handle service user** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/effective_users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_handle_service_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str uid: The Id of the user to return information about. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_handle_service_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_handle_service_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def get_effective_handle_service_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Get effective handle service user  # noqa: E501

        Allows to get a user to a handle service.  This operation requires `handle_service_view` privilege or `oz_users_view` admin privilege.  ***Example cURL requests***  **Get effective handle service user** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/effective_users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_handle_service_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str uid: The Id of the user to return information about. (required)
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
                    " to method get_effective_handle_service_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_handle_service_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_effective_handle_service_user`")  # noqa: E501

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
            '/handle_services/{id}/effective_users/{uid}', 'GET',
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

    def get_handle_service(self, id, **kwargs):  # noqa: E501
        """Get handle service  # noqa: E501

        Returns the properties of a specific handle service.  This operation requires `oz_handle_services_view` admin privilege or handle service membership.  ***Example cURL requests***  **Get handle services** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID  {   \"handleServiceId\": \"0fe7c8a20ffdf07480c46f084bc3b8d5\",   \"name\": \"MyCommunity Handle service\",   \"proxyEndpoint\": \"https://localhost:17000/handle_proxy\",   \"serviceProperties\": {     \"allowTemplateOverride\": false,     \"doiEndpoint\": \"/doi\",     \"host\": \"https://mds.test.datacite.org\",     \"identifierTemplate\": \"{{space.name}}-{{space.guid}}\",     \"mediaEndpoint\": \"/media\",     \"metadataEndpoint\": \"/metadata\",     \"password\": \"pa$$word\",     \"prefix\": 10.5072,     \"type\": \"DOI\",     \"username\": \"alice\"   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_handle_service(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :return: HandleService
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_handle_service_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_handle_service_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_handle_service_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get handle service  # noqa: E501

        Returns the properties of a specific handle service.  This operation requires `oz_handle_services_view` admin privilege or handle service membership.  ***Example cURL requests***  **Get handle services** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID  {   \"handleServiceId\": \"0fe7c8a20ffdf07480c46f084bc3b8d5\",   \"name\": \"MyCommunity Handle service\",   \"proxyEndpoint\": \"https://localhost:17000/handle_proxy\",   \"serviceProperties\": {     \"allowTemplateOverride\": false,     \"doiEndpoint\": \"/doi\",     \"host\": \"https://mds.test.datacite.org\",     \"identifierTemplate\": \"{{space.name}}-{{space.guid}}\",     \"mediaEndpoint\": \"/media\",     \"metadataEndpoint\": \"/metadata\",     \"password\": \"pa$$word\",     \"prefix\": 10.5072,     \"type\": \"DOI\",     \"username\": \"alice\"   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_handle_service_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :return: HandleService
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
                    " to method get_handle_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_handle_service`")  # noqa: E501

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
            '/handle_services/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HandleService',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_handle_service_group(self, id, gid, **kwargs):  # noqa: E501
        """Get handle service group details  # noqa: E501

        Get details of a group with access to handle service.  This operation requires `handle_service_view` privilege or `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get group handle service** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/groups/$GROUP_ID  {   \"groupId\":\"HwUpk8jrwxKOe45uzLFX2GVa8lKEasj4q253sptVqF8\",   \"name\":\"Group name\",   \"type\":\"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_handle_service_group(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str gid: The Id of the group to return information about. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_handle_service_group_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_handle_service_group_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def get_handle_service_group_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Get handle service group details  # noqa: E501

        Get details of a group with access to handle service.  This operation requires `handle_service_view` privilege or `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get group handle service** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/groups/$GROUP_ID  {   \"groupId\":\"HwUpk8jrwxKOe45uzLFX2GVa8lKEasj4q253sptVqF8\",   \"name\":\"Group name\",   \"type\":\"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_handle_service_group_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str gid: The Id of the group to return information about. (required)
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
                    " to method get_handle_service_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_handle_service_group`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `get_handle_service_group`")  # noqa: E501

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
            '/handle_services/{id}/groups/{gid}', 'GET',
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

    def get_handle_service_handle(self, id, hid, **kwargs):  # noqa: E501
        """Get handle from handle service  # noqa: E501

        Returns the details of a specific handle registered by handle service.  This operation requires `handle_service_view` privilege or `oz_handles_view` admin privilege.  ***Example cURL requests***  **Get handle services handle** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/13c6bf68ed88dd01f396571f976b148d/handles/$HANDLE_ID  {   \"handleId\": \"95b663a6467c72ab1256865efef9e387\",   \"handleServiceId\": \"97c27230017cd54c1220189e357322c4\",   \"resourceType\": \"Share\",   \"resourceId\": \"d6ee1aecf03b23f09756d6a49e435455\",   \"metadata\": \"<?xml version=\\\"1.0\\\"?>       <!DOCTYPE rdf:RDF SYSTEM \\\\\"http://dublincore.org/2000/12/01-dcmes-xml-dtd.dtd\\\">       <rdf:RDF xmlns:rdf=\\\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\\\"                xmlns:dc=\\\"http://purl.org/dc/elements/1.1/\\\">         <rdf:Description rdf:about=\\\"http://example.com/resouces/1\\\">           <dc:title>Example Resource</dc:title>           <dc:creator>John Doe</dc:creator>           <dc:publisher>MIT</dc:publisher>           <dc:date>2000-06-06</dc:date>         </rdf:Description>       </rdf:RDF>\",   \"timestamp\": \"1997-07-16T19:20\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_handle_service_handle(id, hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str hid: Handle Id. (required)
        :return: Handle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_handle_service_handle_with_http_info(id, hid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_handle_service_handle_with_http_info(id, hid, **kwargs)  # noqa: E501
            return data

    def get_handle_service_handle_with_http_info(self, id, hid, **kwargs):  # noqa: E501
        """Get handle from handle service  # noqa: E501

        Returns the details of a specific handle registered by handle service.  This operation requires `handle_service_view` privilege or `oz_handles_view` admin privilege.  ***Example cURL requests***  **Get handle services handle** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/13c6bf68ed88dd01f396571f976b148d/handles/$HANDLE_ID  {   \"handleId\": \"95b663a6467c72ab1256865efef9e387\",   \"handleServiceId\": \"97c27230017cd54c1220189e357322c4\",   \"resourceType\": \"Share\",   \"resourceId\": \"d6ee1aecf03b23f09756d6a49e435455\",   \"metadata\": \"<?xml version=\\\"1.0\\\"?>       <!DOCTYPE rdf:RDF SYSTEM \\\\\"http://dublincore.org/2000/12/01-dcmes-xml-dtd.dtd\\\">       <rdf:RDF xmlns:rdf=\\\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\\\"                xmlns:dc=\\\"http://purl.org/dc/elements/1.1/\\\">         <rdf:Description rdf:about=\\\"http://example.com/resouces/1\\\">           <dc:title>Example Resource</dc:title>           <dc:creator>John Doe</dc:creator>           <dc:publisher>MIT</dc:publisher>           <dc:date>2000-06-06</dc:date>         </rdf:Description>       </rdf:RDF>\",   \"timestamp\": \"1997-07-16T19:20\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_handle_service_handle_with_http_info(id, hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str hid: Handle Id. (required)
        :return: Handle
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
                    " to method get_handle_service_handle" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_handle_service_handle`")  # noqa: E501
        # verify the required parameter 'hid' is set
        if ('hid' not in params or
                params['hid'] is None):
            raise ValueError("Missing the required parameter `hid` when calling `get_handle_service_handle`")  # noqa: E501

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
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/handle_services/{id}/handles/{hid}', 'GET',
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

    def get_handle_service_user(self, id, uid, **kwargs):  # noqa: E501
        """Get handle service user  # noqa: E501

        Allows to get a user to a handle service.  This operation requires `handle_service_view` privilege or `oz_users_view` admin privilege.  ***Example cURL requests***  **Add handle service user** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_handle_service_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str uid: The Id of the user to return information about. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_handle_service_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_handle_service_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def get_handle_service_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Get handle service user  # noqa: E501

        Allows to get a user to a handle service.  This operation requires `handle_service_view` privilege or `oz_users_view` admin privilege.  ***Example cURL requests***  **Add handle service user** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_handle_service_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str uid: The Id of the user to return information about. (required)
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
                    " to method get_handle_service_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_handle_service_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_handle_service_user`")  # noqa: E501

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
            '/handle_services/{id}/users/{uid}', 'GET',
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

    def handle_service_update(self, body, id, **kwargs):  # noqa: E501
        """Modify handle service  # noqa: E501

        Allows to update a registered handle service.  This operation requires `handle_service_update` privilege or `oz_handle_services_update` admin privilege.  ***Example cURL requests***  **Modify handle service password** ```bash curl -u username:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"name\": \"New handle service name\"}' \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_service_update(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HandleServiceUpdate body: (required)
        :param str id: Handle service Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.handle_service_update_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.handle_service_update_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def handle_service_update_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Modify handle service  # noqa: E501

        Allows to update a registered handle service.  This operation requires `handle_service_update` privilege or `oz_handle_services_update` admin privilege.  ***Example cURL requests***  **Modify handle service password** ```bash curl -u username:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"name\": \"New handle service name\"}' \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_service_update_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HandleServiceUpdate body: (required)
        :param str id: Handle service Id. (required)
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
                    " to method handle_service_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `handle_service_update`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `handle_service_update`")  # noqa: E501

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
            '/handle_services/{id}', 'PATCH',
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

    def list_effective_group_handle_service_privileges(self, id, gid, **kwargs):  # noqa: E501
        """List effective group's handle service privileges  # noqa: E501

        Returns the list of effective group's (`{gid}`) privileges in a handle service (`{id}`).  Effective privileges are a sum of group's privileges and privileges inherited from its parent group memberships.  This operation requires `handle_service_view` privilege or `oz_handle_services_view_privileges` admin privilege.  ***Example cURL requests***  **List effective group's privileges in a handle service** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/effective_groups/$GROUP_ID/privileges  {   \"privileges\": [     \"handle_service_register_handle\",     \"handle_service_update\",     \"handle_service_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_handle_service_privileges(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str gid: Effective group Id. (required)
        :return: InlineResponse20014
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_group_handle_service_privileges_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_group_handle_service_privileges_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def list_effective_group_handle_service_privileges_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """List effective group's handle service privileges  # noqa: E501

        Returns the list of effective group's (`{gid}`) privileges in a handle service (`{id}`).  Effective privileges are a sum of group's privileges and privileges inherited from its parent group memberships.  This operation requires `handle_service_view` privilege or `oz_handle_services_view_privileges` admin privilege.  ***Example cURL requests***  **List effective group's privileges in a handle service** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/effective_groups/$GROUP_ID/privileges  {   \"privileges\": [     \"handle_service_register_handle\",     \"handle_service_update\",     \"handle_service_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_handle_service_privileges_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str gid: Effective group Id. (required)
        :return: InlineResponse20014
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
                    " to method list_effective_group_handle_service_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_group_handle_service_privileges`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `list_effective_group_handle_service_privileges`")  # noqa: E501

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
            '/handle_services/{id}/effective_groups/{gid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20014',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_effective_handle_service_groups(self, id, **kwargs):  # noqa: E501
        """List effective handle service groups  # noqa: E501

        Returns all groups with effective access to a handle service instance  This operation requires `handle_service_view` privilege or `oz_handle_services_list_relationships` admin privilege.  ***Example cURL requests***  **Get effective handle service groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/effective_groups  {   \"groups\": [     \"9d9687a61855be21a31c34359b1fa0d4\",     \"89389b5483bb60288e6f0a7af488e710\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_handle_service_groups(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :return: Groups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_handle_service_groups_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_handle_service_groups_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_effective_handle_service_groups_with_http_info(self, id, **kwargs):  # noqa: E501
        """List effective handle service groups  # noqa: E501

        Returns all groups with effective access to a handle service instance  This operation requires `handle_service_view` privilege or `oz_handle_services_list_relationships` admin privilege.  ***Example cURL requests***  **Get effective handle service groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/effective_groups  {   \"groups\": [     \"9d9687a61855be21a31c34359b1fa0d4\",     \"89389b5483bb60288e6f0a7af488e710\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_handle_service_groups_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
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
                    " to method list_effective_handle_service_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_handle_service_groups`")  # noqa: E501

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
            '/handle_services/{id}/effective_groups', 'GET',
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

    def list_effective_handle_service_users(self, id, **kwargs):  # noqa: E501
        """Get effective handle service users  # noqa: E501

        Returns all users with access to a handle service instance  This operation requires `handle_service_view` privilege or `oz_handle_services_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle service users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/effective_users  {   \"users\": [     \"9d9687a61855be21a31c34359b1fa0d4\",     \"89389b5483bb60288e6f0a7af488e710\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_handle_service_users(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_handle_service_users_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_handle_service_users_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_effective_handle_service_users_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get effective handle service users  # noqa: E501

        Returns all users with access to a handle service instance  This operation requires `handle_service_view` privilege or `oz_handle_services_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle service users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/effective_users  {   \"users\": [     \"9d9687a61855be21a31c34359b1fa0d4\",     \"89389b5483bb60288e6f0a7af488e710\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_handle_service_users_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
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
                    " to method list_effective_handle_service_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_handle_service_users`")  # noqa: E501

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
            '/handle_services/{id}/effective_users', 'GET',
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

    def list_effective_user_handle_service_privileges(self, id, uid, **kwargs):  # noqa: E501
        """List effective user's handle service privileges  # noqa: E501

        Returns the list of effective user's (`{uid}`) privileges in a handle service (`{id}`).  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation requires `handle_service_view` privilege or `oz_handle_services_view_privileges` admin privilege.  ***Example cURL requests***  **List effective user's privileges in a handle service** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/effective_users/$USER_ID/privileges  {   \"privileges\": [     \"handle_service_register_handle\",     \"handle_service_update\",     \"handle_service_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_user_handle_service_privileges(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str uid: Effective user Id. (required)
        :return: InlineResponse20014
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_user_handle_service_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_user_handle_service_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def list_effective_user_handle_service_privileges_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """List effective user's handle service privileges  # noqa: E501

        Returns the list of effective user's (`{uid}`) privileges in a handle service (`{id}`).  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation requires `handle_service_view` privilege or `oz_handle_services_view_privileges` admin privilege.  ***Example cURL requests***  **List effective user's privileges in a handle service** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/effective_users/$USER_ID/privileges  {   \"privileges\": [     \"handle_service_register_handle\",     \"handle_service_update\",     \"handle_service_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_user_handle_service_privileges_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str uid: Effective user Id. (required)
        :return: InlineResponse20014
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
                    " to method list_effective_user_handle_service_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_user_handle_service_privileges`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `list_effective_user_handle_service_privileges`")  # noqa: E501

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
            '/handle_services/{id}/effective_users/{uid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20014',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_group_handle_service_privileges(self, id, gid, **kwargs):  # noqa: E501
        """List group's handle service privileges  # noqa: E501

        Returns the list of group's (`{gid}`) privileges in a handle service (`{id}`).  This operation requires `handle_service_view` privilege. For administrator who does not belong to this group `oz_handle_services_view_privileges` privilege is required.  ***Example cURL requests***  **List group's privileges in a handle service** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/groups/$GROUP_ID/privileges  {   \"privileges\": [     \"handle_service_register_handle\",     \"handle_service_update\",     \"handle_service_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_handle_service_privileges(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str gid: Effective group Id. (required)
        :return: InlineResponse20014
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_group_handle_service_privileges_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_group_handle_service_privileges_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def list_group_handle_service_privileges_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """List group's handle service privileges  # noqa: E501

        Returns the list of group's (`{gid}`) privileges in a handle service (`{id}`).  This operation requires `handle_service_view` privilege. For administrator who does not belong to this group `oz_handle_services_view_privileges` privilege is required.  ***Example cURL requests***  **List group's privileges in a handle service** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/groups/$GROUP_ID/privileges  {   \"privileges\": [     \"handle_service_register_handle\",     \"handle_service_update\",     \"handle_service_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_handle_service_privileges_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str gid: Effective group Id. (required)
        :return: InlineResponse20014
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
                    " to method list_group_handle_service_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_group_handle_service_privileges`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `list_group_handle_service_privileges`")  # noqa: E501

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
            '/handle_services/{id}/groups/{gid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20014',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_handle_service_groups(self, id, **kwargs):  # noqa: E501
        """List handle service groups  # noqa: E501

        Returns all groups with access to a handle service instance  This operation requires `handle_service_view` privilege or `oz_handle_services_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle service groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/groups  {   \"groups\": [     \"9d9687a61855be21a31c34359b1fa0d4\",     \"89389b5483bb60288e6f0a7af488e710\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_handle_service_groups(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :return: Groups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_handle_service_groups_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_handle_service_groups_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_handle_service_groups_with_http_info(self, id, **kwargs):  # noqa: E501
        """List handle service groups  # noqa: E501

        Returns all groups with access to a handle service instance  This operation requires `handle_service_view` privilege or `oz_handle_services_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle service groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/groups  {   \"groups\": [     \"9d9687a61855be21a31c34359b1fa0d4\",     \"89389b5483bb60288e6f0a7af488e710\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_handle_service_groups_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
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
                    " to method list_handle_service_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_handle_service_groups`")  # noqa: E501

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
            '/handle_services/{id}/groups', 'GET',
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

    def list_handle_service_privileges(self, **kwargs):  # noqa: E501
        """List all handle service privileges  # noqa: E501

        Returns list of all possible handle service privileges.  This endpoint does not require authentication.  ***Example cURL requests***  **Get list of all handle service privileges** ```bash curl https://$ZONE_HOST/api/v3/onezone/handle_services/privileges  {   \"admin\": [     \"handle_service_view\",     \"handle_service_update\",     \"handle_service_delete\",     \"handle_service_register_handle\",     \"handle_service_list_handles\"   ],   \"member\": [     \"handle_service_view\",     \"handle_service_register_handle\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_handle_service_privileges(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_handle_service_privileges_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_handle_service_privileges_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_handle_service_privileges_with_http_info(self, **kwargs):  # noqa: E501
        """List all handle service privileges  # noqa: E501

        Returns list of all possible handle service privileges.  This endpoint does not require authentication.  ***Example cURL requests***  **Get list of all handle service privileges** ```bash curl https://$ZONE_HOST/api/v3/onezone/handle_services/privileges  {   \"admin\": [     \"handle_service_view\",     \"handle_service_update\",     \"handle_service_delete\",     \"handle_service_register_handle\",     \"handle_service_list_handles\"   ],   \"member\": [     \"handle_service_view\",     \"handle_service_register_handle\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_handle_service_privileges_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20013
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
                    " to method list_handle_service_privileges" % key
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
            '/handle_services/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20013',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_handle_service_users(self, id, **kwargs):  # noqa: E501
        """Get handle service users  # noqa: E501

        Returns all users with access to a handle service instance  This operation requires `handle_service_view` privilege or `oz_handle_services_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle service users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/users  {   \"users\": [     \"9d9687a61855be21a31c34359b1fa0d4\",     \"89389b5483bb60288e6f0a7af488e710\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_handle_service_users(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_handle_service_users_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_handle_service_users_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_handle_service_users_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get handle service users  # noqa: E501

        Returns all users with access to a handle service instance  This operation requires `handle_service_view` privilege or `oz_handle_services_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle service users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/users  {   \"users\": [     \"9d9687a61855be21a31c34359b1fa0d4\",     \"89389b5483bb60288e6f0a7af488e710\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_handle_service_users_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
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
                    " to method list_handle_service_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_handle_service_users`")  # noqa: E501

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
            '/handle_services/{id}/users', 'GET',
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

    def list_handle_services(self, **kwargs):  # noqa: E501
        """List handle services  # noqa: E501

        Returns the list of registered handle services.  This operation requires `oz_handle_services_list` admin privilege.   ***Example cURL requests***  **Get handle services** ```bash curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/handle_services  {   \"handle_services\": [     \"0fe7c8a20ffdf07480c46f084bc3b8d5\",     \"302da048de67e2ea05f0af1d0fe7c8a2\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_handle_services(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: HandleServices
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_handle_services_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_handle_services_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_handle_services_with_http_info(self, **kwargs):  # noqa: E501
        """List handle services  # noqa: E501

        Returns the list of registered handle services.  This operation requires `oz_handle_services_list` admin privilege.   ***Example cURL requests***  **Get handle services** ```bash curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/handle_services  {   \"handle_services\": [     \"0fe7c8a20ffdf07480c46f084bc3b8d5\",     \"302da048de67e2ea05f0af1d0fe7c8a2\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_handle_services_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: HandleServices
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
                    " to method list_handle_services" % key
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
            '/handle_services', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HandleServices',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_handleservice_handles(self, id, **kwargs):  # noqa: E501
        """List handle service handles  # noqa: E501

        Returns the list of Ids of all handles registered by handle service.  This operation requires `handle_service_list_handles` privilege or `oz_handle_services_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle services handles** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/13c6bf68ed88dd01f396571f976b148d/handles  {   \"handles\": [     \"0fe7c8a20ffdf07480c46f084bc3b8d5\",     \"302da048de67e2ea05f0af1d0fe7c8a2\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_handleservice_handles(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :return: Handles
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_handleservice_handles_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_handleservice_handles_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_handleservice_handles_with_http_info(self, id, **kwargs):  # noqa: E501
        """List handle service handles  # noqa: E501

        Returns the list of Ids of all handles registered by handle service.  This operation requires `handle_service_list_handles` privilege or `oz_handle_services_list_relationships` admin privilege.  ***Example cURL requests***  **Get handle services handles** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/13c6bf68ed88dd01f396571f976b148d/handles  {   \"handles\": [     \"0fe7c8a20ffdf07480c46f084bc3b8d5\",     \"302da048de67e2ea05f0af1d0fe7c8a2\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_handleservice_handles_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :return: Handles
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
                    " to method list_handleservice_handles" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_handleservice_handles`")  # noqa: E501

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
            '/handle_services/{id}/handles', 'GET',
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

    def list_user_handle_service_privileges(self, id, uid, **kwargs):  # noqa: E501
        """List user's handle service privileges  # noqa: E501

        Returns the list of user's (`{uid}`) privileges in a handle service (`{id}`).  This operation requires `handle_service_view` privilege or `oz_handle_services_view_privileges` admin privilege.  ***Example cURL requests***  **List user's privileges in a handle service** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/users/$USER_ID/privileges  {   \"privileges\": [     \"handle_service_register_handle\",     \"handle_service_update\",     \"handle_service_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_handle_service_privileges(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str uid: Effective group Id. (required)
        :return: InlineResponse20014
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_handle_service_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_user_handle_service_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def list_user_handle_service_privileges_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """List user's handle service privileges  # noqa: E501

        Returns the list of user's (`{uid}`) privileges in a handle service (`{id}`).  This operation requires `handle_service_view` privilege or `oz_handle_services_view_privileges` admin privilege.  ***Example cURL requests***  **List user's privileges in a handle service** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/users/$USER_ID/privileges  {   \"privileges\": [     \"handle_service_register_handle\",     \"handle_service_update\",     \"handle_service_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_handle_service_privileges_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str uid: Effective group Id. (required)
        :return: InlineResponse20014
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
                    " to method list_user_handle_service_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_user_handle_service_privileges`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `list_user_handle_service_privileges`")  # noqa: E501

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
            '/handle_services/{id}/users/{uid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20014',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_handle_service(self, id, **kwargs):  # noqa: E501
        """Unregister handle service  # noqa: E501

        Allows to unregister a registeed handle service.  This operation requires `handle_service_delete` privilege or `oz_handle_services_delete` admin privilege.  ***Example cURL requests***  **Unregister handle service** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_handle_service(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_handle_service_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_handle_service_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def remove_handle_service_with_http_info(self, id, **kwargs):  # noqa: E501
        """Unregister handle service  # noqa: E501

        Allows to unregister a registeed handle service.  This operation requires `handle_service_delete` privilege or `oz_handle_services_delete` admin privilege.  ***Example cURL requests***  **Unregister handle service** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_handle_service_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
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
                    " to method remove_handle_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_handle_service`")  # noqa: E501

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
            '/handle_services/{id}', 'DELETE',
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

    def remove_handle_service_group(self, id, gid, **kwargs):  # noqa: E501
        """Remove handle service group  # noqa: E501

        Allows to remove a group from access to a handle service.  This operation requires `handle_service_update` privilege or `oz_handle_services_remove_relationships` and `oz_groups_remove_relationships` admin privilege.  ***Example cURL requests***  **Remove handle service group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_handle_service_group(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str gid: The Id of the group to remove from handle service. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_handle_service_group_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_handle_service_group_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def remove_handle_service_group_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Remove handle service group  # noqa: E501

        Allows to remove a group from access to a handle service.  This operation requires `handle_service_update` privilege or `oz_handle_services_remove_relationships` and `oz_groups_remove_relationships` admin privilege.  ***Example cURL requests***  **Remove handle service group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_handle_service_group_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str gid: The Id of the group to remove from handle service. (required)
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
                    " to method remove_handle_service_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_handle_service_group`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `remove_handle_service_group`")  # noqa: E501

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
            '/handle_services/{id}/groups/{gid}', 'DELETE',
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

    def remove_handle_service_user(self, id, uid, **kwargs):  # noqa: E501
        """Remove handle service user  # noqa: E501

        Allows to remove a user from access to a handle service.  This operation requires `handle_service_update` privilege or `oz_handle_services_remove_relationships` and `oz_users_remove_relationships` admin privilege.  ***Example cURL requests***  **Remove handle service user** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_handle_service_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str uid: The Id of the user to remove from handle service. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_handle_service_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_handle_service_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def remove_handle_service_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Remove handle service user  # noqa: E501

        Allows to remove a user from access to a handle service.  This operation requires `handle_service_update` privilege or `oz_handle_services_remove_relationships` and `oz_users_remove_relationships` admin privilege.  ***Example cURL requests***  **Remove handle service user** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_handle_service_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Handle service Id. (required)
        :param str uid: The Id of the user to remove from handle service. (required)
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
                    " to method remove_handle_service_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_handle_service_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `remove_handle_service_user`")  # noqa: E501

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
            '/handle_services/{id}/users/{uid}', 'DELETE',
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

    def update_group_handle_service_privileges(self, body, id, uid, **kwargs):  # noqa: E501
        """Update user's handle service privileges  # noqa: E501

        Updates user's (`{uid}`) privileges in a handle service (`{id}`).  This operation requires `handle_service_update` privilege or `oz_handle_services_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update user's privileges in a handle service** ```bash curl -u username:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"handle_service_register_handle\"], \"revoke\": [\"handle_service_update\"]}' \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/users/$USER_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_group_handle_service_privileges(body, id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: Handle service privileges update request. (required)
        :param str id: Handle service Id. (required)
        :param str uid: User Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_group_handle_service_privileges_with_http_info(body, id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_group_handle_service_privileges_with_http_info(body, id, uid, **kwargs)  # noqa: E501
            return data

    def update_group_handle_service_privileges_with_http_info(self, body, id, uid, **kwargs):  # noqa: E501
        """Update user's handle service privileges  # noqa: E501

        Updates user's (`{uid}`) privileges in a handle service (`{id}`).  This operation requires `handle_service_update` privilege or `oz_handle_services_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update user's privileges in a handle service** ```bash curl -u username:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"handle_service_register_handle\"], \"revoke\": [\"handle_service_update\"]}' \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/users/$USER_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_group_handle_service_privileges_with_http_info(body, id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: Handle service privileges update request. (required)
        :param str id: Handle service Id. (required)
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
                    " to method update_group_handle_service_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_group_handle_service_privileges`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_group_handle_service_privileges`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `update_group_handle_service_privileges`")  # noqa: E501

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
            '/handle_services/{id}/users/{uid}/privileges', 'PATCH',
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

    def update_group_handle_service_privileges_0(self, body, id, gid, **kwargs):  # noqa: E501
        """Update group's handle service privileges  # noqa: E501

        Updates group's (`{gid}`) privileges in a handle service (`{id}`).  This operation requires `handle_service_update` privilege. For administrator who does not belong to this group `oz_handle_services_set_privileges` privilege is required.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update group's privileges in a handle service** ```bash curl -u username:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"handle_service_register_handle\"], \"revoke\": [\"handle_service_update\"]}' \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/groups/$GROUP_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_group_handle_service_privileges_0(body, id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HandleServicePrivilegesUpdate body: Handle service privileges update request. (required)
        :param str id: Handle service Id. (required)
        :param str gid: Group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_group_handle_service_privileges_0_with_http_info(body, id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_group_handle_service_privileges_0_with_http_info(body, id, gid, **kwargs)  # noqa: E501
            return data

    def update_group_handle_service_privileges_0_with_http_info(self, body, id, gid, **kwargs):  # noqa: E501
        """Update group's handle service privileges  # noqa: E501

        Updates group's (`{gid}`) privileges in a handle service (`{id}`).  This operation requires `handle_service_update` privilege. For administrator who does not belong to this group `oz_handle_services_set_privileges` privilege is required.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update group's privileges in a handle service** ```bash curl -u username:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"handle_service_register_handle\"], \"revoke\": [\"handle_service_update\"]}' \\ https://$ZONE_HOST/api/v3/onezone/handle_services/$HANDLE_SERVICE_ID/groups/$GROUP_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_group_handle_service_privileges_0_with_http_info(body, id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HandleServicePrivilegesUpdate body: Handle service privileges update request. (required)
        :param str id: Handle service Id. (required)
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
                    " to method update_group_handle_service_privileges_0" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_group_handle_service_privileges_0`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_group_handle_service_privileges_0`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `update_group_handle_service_privileges_0`")  # noqa: E501

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
            '/handle_services/{id}/groups/{gid}/privileges', 'PATCH',
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
