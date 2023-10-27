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


class GroupApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_child_group(self, id, cid, **kwargs):  # noqa: E501
        """Add child group  # noqa: E501

        Adds group {cid} as child group of group {id}. Optional privileges can be passed in the request body, otherwise default privileges will be set for the child group in this group.  This operation requires `group_add_child` privilege in the parent group and `group_add_parent` privilege in the child group. If `privileges` are specified in the request, `group_set_privileges` privilege is also required.  For administrator who does not belong to those groups, `oz_groups_add_relationships` privilege is required, and `oz_groups_set_privileges` if `privileges` are specified in the request.  ***Example cURL requests***  **Add child group** ```bash curl -u username:password -X PUT \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/children/$CHILD_GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_child_group(id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str cid: Child group Id. (required)
        :param ChildrenCidBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_child_group_with_http_info(id, cid, **kwargs)  # noqa: E501
        else:
            (data) = self.add_child_group_with_http_info(id, cid, **kwargs)  # noqa: E501
            return data

    def add_child_group_with_http_info(self, id, cid, **kwargs):  # noqa: E501
        """Add child group  # noqa: E501

        Adds group {cid} as child group of group {id}. Optional privileges can be passed in the request body, otherwise default privileges will be set for the child group in this group.  This operation requires `group_add_child` privilege in the parent group and `group_add_parent` privilege in the child group. If `privileges` are specified in the request, `group_set_privileges` privilege is also required.  For administrator who does not belong to those groups, `oz_groups_add_relationships` privilege is required, and `oz_groups_set_privileges` if `privileges` are specified in the request.  ***Example cURL requests***  **Add child group** ```bash curl -u username:password -X PUT \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/children/$CHILD_GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_child_group_with_http_info(id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str cid: Child group Id. (required)
        :param ChildrenCidBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'cid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_child_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_child_group`")  # noqa: E501
        # verify the required parameter 'cid' is set
        if ('cid' not in params or
                params['cid'] is None):
            raise ValueError("Missing the required parameter `cid` when calling `add_child_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'cid' in params:
            path_params['cid'] = params['cid']  # noqa: E501

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
            '/groups/{id}/children/{cid}', 'PUT',
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

    def add_group_handle_service(self, body, id, **kwargs):  # noqa: E501
        """Create a new handle service for given group.  # noqa: E501

        Creates a new handle service for group.  This operation requires `group_create_handle_service` privilege and `oz_handle_services_create` admin privilege. For administrator who does not belong to this group `oz_handle_services_create` and `oz_groups_add_relationships` privileges are required.  ***Example cURL requests***  **Add group handle services** ```bash curl -u username:password -X POST -H \"Content-type: application/json\" \\ -d '{ ... }' https://$ZONE_HOST/api/v3/onezone/groups/4ebd9efd1e67f6c18695db1d762a914a/handle_services ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_group_handle_service(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HandleServiceCreateRequest body: (required)
        :param str id: Group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_group_handle_service_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.add_group_handle_service_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def add_group_handle_service_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Create a new handle service for given group.  # noqa: E501

        Creates a new handle service for group.  This operation requires `group_create_handle_service` privilege and `oz_handle_services_create` admin privilege. For administrator who does not belong to this group `oz_handle_services_create` and `oz_groups_add_relationships` privileges are required.  ***Example cURL requests***  **Add group handle services** ```bash curl -u username:password -X POST -H \"Content-type: application/json\" \\ -d '{ ... }' https://$ZONE_HOST/api/v3/onezone/groups/4ebd9efd1e67f6c18695db1d762a914a/handle_services ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_group_handle_service_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HandleServiceCreateRequest body: (required)
        :param str id: Group Id. (required)
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
                    " to method add_group_handle_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_group_handle_service`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_group_handle_service`")  # noqa: E501

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
            '/groups/{id}/handle_services', 'POST',
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

    def add_group_user(self, id, uid, **kwargs):  # noqa: E501
        """Add user to group  # noqa: E501

        Adds user {uid} as member of group {id}. Optional privileges can be passed in the request body, otherwise default privileges will be set for the user in this group.  This operation can only be invoked by the user {uid} to add himself to the group (if he is not a member already) and requires `group_add_user` privilege in the group. If `privileges` are specified in the request, `group_set_privileges` privilege is also required.  Administrators having the `oz_groups_add_relationships` and `oz_users_add_relationships` admin privileges can add any user to any group, though `oz_groups_set_privileges` privilege is required if `privileges` are specified in the request.  ***Example cURL requests***  **Generate user group invite token** ```bash curl -u admin:password -X PUT \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_group_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str uid: User Id. (required)
        :param UsersUidBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_group_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.add_group_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def add_group_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Add user to group  # noqa: E501

        Adds user {uid} as member of group {id}. Optional privileges can be passed in the request body, otherwise default privileges will be set for the user in this group.  This operation can only be invoked by the user {uid} to add himself to the group (if he is not a member already) and requires `group_add_user` privilege in the group. If `privileges` are specified in the request, `group_set_privileges` privilege is also required.  Administrators having the `oz_groups_add_relationships` and `oz_users_add_relationships` admin privileges can add any user to any group, though `oz_groups_set_privileges` privilege is required if `privileges` are specified in the request.  ***Example cURL requests***  **Generate user group invite token** ```bash curl -u admin:password -X PUT \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_group_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str uid: User Id. (required)
        :param UsersUidBody body:
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
                    " to method add_group_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_group_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `add_group_user`")  # noqa: E501

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
            '/groups/{id}/users/{uid}', 'PUT',
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

    def create_child_group(self, body, id, **kwargs):  # noqa: E501
        """Create child group  # noqa: E501

        Creates a new child group belonging to the group of {id}.  This operation requires `group_add_child` privilege. For administrator who does not belong to this group `oz_groups_add_relationships` and `oz_groups_create` privileges are required.  ***Example cURL requests***  **Create child group** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/children ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_child_group(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupCreateRequest body: Group properties. (required)
        :param str id: Group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_child_group_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_child_group_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def create_child_group_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Create child group  # noqa: E501

        Creates a new child group belonging to the group of {id}.  This operation requires `group_add_child` privilege. For administrator who does not belong to this group `oz_groups_add_relationships` and `oz_groups_create` privileges are required.  ***Example cURL requests***  **Create child group** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/children ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_child_group_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupCreateRequest body: Group properties. (required)
        :param str id: Group Id. (required)
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
                    " to method create_child_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_child_group`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_child_group`")  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{id}/children', 'POST',
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

    def create_child_group_token(self, id, **kwargs):  # noqa: E501
        """Create child group invitation token  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token that can be used to add a group as child group of group with {id}.  This operation requires `group_add_child` privilege. For administrator who does not belong to this group `oz_groups_add_relationships` privilege is required.  ***Example cURL requests***  **Create invitation token for child group** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID  {   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaWVyIZdrenY00SX\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_child_group_token(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: GroupInviteToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_child_group_token_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_child_group_token_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def create_child_group_token_with_http_info(self, id, **kwargs):  # noqa: E501
        """Create child group invitation token  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token that can be used to add a group as child group of group with {id}.  This operation requires `group_add_child` privilege. For administrator who does not belong to this group `oz_groups_add_relationships` privilege is required.  ***Example cURL requests***  **Create invitation token for child group** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID  {   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaWVyIZdrenY00SX\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_child_group_token_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: GroupInviteToken
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
                    " to method create_child_group_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_child_group_token`")  # noqa: E501

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
            '/groups/{id}/children/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GroupInviteToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_group(self, body, **kwargs):  # noqa: E501
        """Create new group  # noqa: E501

        Creates a new group.  This operation requires `oz_groups_create` privilege.    See also:   [Create a new group for the current user](#operation/create_group_for_user)   [Create a new parent group for given group](#operation/create_parent_group)    ***Example cURL requests***  **Create new group of type `team`** ```bash  curl -u username:password -H \"Content-type: application/json\" \\  -X POST -d '{ \"name\":\"new_group\" , \"type\":\"team\" }' \\  https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_group(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupCreateRequest body: Group properties. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_group_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_group_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_group_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create new group  # noqa: E501

        Creates a new group.  This operation requires `oz_groups_create` privilege.    See also:   [Create a new group for the current user](#operation/create_group_for_user)   [Create a new parent group for given group](#operation/create_parent_group)    ***Example cURL requests***  **Create new group of type `team`** ```bash  curl -u username:password -H \"Content-type: application/json\" \\  -X POST -d '{ \"name\":\"new_group\" , \"type\":\"team\" }' \\  https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_group_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupCreateRequest body: Group properties. (required)
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
                    " to method create_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_group`")  # noqa: E501

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
            '/groups', 'POST',
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

    def create_group_handle(self, body, id, **kwargs):  # noqa: E501
        """Create a new handle for given group  # noqa: E501

        Creates a new handle on behalf of a group.  This operation requires `group_create_handle` privilege in the group and `handle_service_register_handle` privilege in the handle service specified in the `handleServiceId` field.   For administrator who does not belong to this group `oz_groups_add_relationships` and `oz_handles_create` privilege is required.   ***Example cURL requests***  **Create new group handle** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"handleServiceId\": \"ddb06ed993bae95f2f430664fff122f7\", \"resourceType\": \"Share\", \"resourceId\": \"4fa683cbda8d8f686d15d42720af431d\", \"metadata\": \"<?xml version=\\'1.0\\'?>...\" }' https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/handles ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_group_handle(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HandleRegistrationRequest body: New handle parameters. (required)
        :param str id: Group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_group_handle_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_group_handle_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def create_group_handle_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Create a new handle for given group  # noqa: E501

        Creates a new handle on behalf of a group.  This operation requires `group_create_handle` privilege in the group and `handle_service_register_handle` privilege in the handle service specified in the `handleServiceId` field.   For administrator who does not belong to this group `oz_groups_add_relationships` and `oz_handles_create` privilege is required.   ***Example cURL requests***  **Create new group handle** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"handleServiceId\": \"ddb06ed993bae95f2f430664fff122f7\", \"resourceType\": \"Share\", \"resourceId\": \"4fa683cbda8d8f686d15d42720af431d\", \"metadata\": \"<?xml version=\\'1.0\\'?>...\" }' https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/handles ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_group_handle_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HandleRegistrationRequest body: New handle parameters. (required)
        :param str id: Group Id. (required)
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
                    " to method create_group_handle" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_group_handle`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_group_handle`")  # noqa: E501

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
            '/groups/{id}/handles', 'POST',
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

    def create_harvester_for_group(self, body, id, **kwargs):  # noqa: E501
        """Create a new harvester for given group  # noqa: E501

        Creates a new harvester for a specific group.  This operation requires `group_add_harvester` privilege. For administrator who does not belong to this group `oz_groups_add_relationships` and `oz_harvesters_create` privileges are required.  ***Example cURL requests***  **Create new harvester for group** ```bash curl -u admin:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"name\" : \"new_harvester\", \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\", \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\"  \\ \"config\" : { \"typeMapping\": [ { \"id\": 0, \"name\": \"Type 1\" }, { \"id\": 1, \"name\": \"Type 1\" } ],              \"externalHelpLink\": \"http://example.com/some_help_page\",              \"refreshDataTimeout\": 1000 }, \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/harvesters ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_harvester_for_group(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HarvesterCreateRequest body: Harvester properties. (required)
        :param str id: Group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_harvester_for_group_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_harvester_for_group_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def create_harvester_for_group_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Create a new harvester for given group  # noqa: E501

        Creates a new harvester for a specific group.  This operation requires `group_add_harvester` privilege. For administrator who does not belong to this group `oz_groups_add_relationships` and `oz_harvesters_create` privileges are required.  ***Example cURL requests***  **Create new harvester for group** ```bash curl -u admin:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"name\" : \"new_harvester\", \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\", \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\"  \\ \"config\" : { \"typeMapping\": [ { \"id\": 0, \"name\": \"Type 1\" }, { \"id\": 1, \"name\": \"Type 1\" } ],              \"externalHelpLink\": \"http://example.com/some_help_page\",              \"refreshDataTimeout\": 1000 }, \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/harvesters ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_harvester_for_group_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HarvesterCreateRequest body: Harvester properties. (required)
        :param str id: Group Id. (required)
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
                    " to method create_harvester_for_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_harvester_for_group`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_harvester_for_group`")  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{id}/harvesters', 'POST',
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

    def create_parent_group(self, body, id, **kwargs):  # noqa: E501
        """Create a new parent group for given group  # noqa: E501

        Creates a new group for the current group. The group automatically becomes a member of this group.  This operation requires `group_add_parent` privilege. For administrator who does not belong to this group `oz_groups_add_relationships` and `oz_groups_create` privileges are required.  ***Example cURL requests***  **Create new group** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"name\" : \"test_group\" , \"type\" : \"team\" }' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/parents ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_parent_group(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Group body: New group parameters. (required)
        :param str id: Group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_parent_group_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_parent_group_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def create_parent_group_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Create a new parent group for given group  # noqa: E501

        Creates a new group for the current group. The group automatically becomes a member of this group.  This operation requires `group_add_parent` privilege. For administrator who does not belong to this group `oz_groups_add_relationships` and `oz_groups_create` privileges are required.  ***Example cURL requests***  **Create new group** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"name\" : \"test_group\" , \"type\" : \"team\" }' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/parents ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_parent_group_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Group body: New group parameters. (required)
        :param str id: Group Id. (required)
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
                    " to method create_parent_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_parent_group`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_parent_group`")  # noqa: E501

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
            '/groups/{id}/parents', 'POST',
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

    def create_space_for_group(self, id, **kwargs):  # noqa: E501
        """Create a new space for given group  # noqa: E501

        Creates a new space for a specific group.  This operation requires `group_add_space` privilege. For administrator who does not belong to this group `oz_groups_add_relationships` and `oz_spaces_create` privileges are required.  ***Example cURL requests***  **Create new space for group** ```bash curl -u admin:password -H \"Content-type: application/json\" \\ -X POST -d '{\"name\": \"new_space\"}' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/spaces ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_space_for_group(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param IdSpacesBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_space_for_group_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_space_for_group_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def create_space_for_group_with_http_info(self, id, **kwargs):  # noqa: E501
        """Create a new space for given group  # noqa: E501

        Creates a new space for a specific group.  This operation requires `group_add_space` privilege. For administrator who does not belong to this group `oz_groups_add_relationships` and `oz_spaces_create` privileges are required.  ***Example cURL requests***  **Create new space for group** ```bash curl -u admin:password -H \"Content-type: application/json\" \\ -X POST -d '{\"name\": \"new_space\"}' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/spaces ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_space_for_group_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param IdSpacesBody body:
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
                    " to method create_space_for_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_space_for_group`")  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{id}/spaces', 'POST',
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

    def create_user_group_invite_token(self, id, **kwargs):  # noqa: E501
        """Create user invite token for group  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token allowing new user to join the group.  This operation requires `group_add_user` privilege. For administrator who does not belong to this group `oz_groups_add_relationships` privilege is required.  ***Example cURL requests***  **Generate user group invite token** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/users/token  {   \"token\": \"MDAxNmxvY2F00aW9uIHJlZlFTUbnZpdGVthHo8xmai4RqqBO2MZM00mrYGgo\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_group_invite_token(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: GroupInviteToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_user_group_invite_token_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_user_group_invite_token_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def create_user_group_invite_token_with_http_info(self, id, **kwargs):  # noqa: E501
        """Create user invite token for group  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token allowing new user to join the group.  This operation requires `group_add_user` privilege. For administrator who does not belong to this group `oz_groups_add_relationships` privilege is required.  ***Example cURL requests***  **Generate user group invite token** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/users/token  {   \"token\": \"MDAxNmxvY2F00aW9uIHJlZlFTUbnZpdGVthHo8xmai4RqqBO2MZM00mrYGgo\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_group_invite_token_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: GroupInviteToken
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
                    " to method create_user_group_invite_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_user_group_invite_token`")  # noqa: E501

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
            '/groups/{id}/users/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GroupInviteToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_child_group(self, id, cid, **kwargs):  # noqa: E501
        """Get child group details  # noqa: E501

        Returns information about a specific child group.  This operation requires `group_view` privilege. For administrator who does not belong to this group  `oz_groups_view` privilege is required.  ***Example cURL requests***  **Get child group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/children/$CHILD_GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_group1\",   \"type\": \"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_child_group(id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str cid: Child group Id. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_child_group_with_http_info(id, cid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_child_group_with_http_info(id, cid, **kwargs)  # noqa: E501
            return data

    def get_child_group_with_http_info(self, id, cid, **kwargs):  # noqa: E501
        """Get child group details  # noqa: E501

        Returns information about a specific child group.  This operation requires `group_view` privilege. For administrator who does not belong to this group  `oz_groups_view` privilege is required.  ***Example cURL requests***  **Get child group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/children/$CHILD_GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_group1\",   \"type\": \"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_child_group_with_http_info(id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str cid: Child group Id. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'cid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_child_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_child_group`")  # noqa: E501
        # verify the required parameter 'cid' is set
        if ('cid' not in params or
                params['cid'] is None):
            raise ValueError("Missing the required parameter `cid` when calling `get_child_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'cid' in params:
            path_params['cid'] = params['cid']  # noqa: E501

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
            '/groups/{id}/children/{cid}', 'GET',
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

    def get_effective_child_group(self, id, cid, **kwargs):  # noqa: E501
        """Get effective child group details  # noqa: E501

        Returns information about a specific effective child group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_view` privilege is required.  ***Example cURL requests***  **Get effective child details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_children/$CHILD_GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_group1\",   \"type\": \"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_child_group(id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str cid: Effective child group Id. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_child_group_with_http_info(id, cid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_child_group_with_http_info(id, cid, **kwargs)  # noqa: E501
            return data

    def get_effective_child_group_with_http_info(self, id, cid, **kwargs):  # noqa: E501
        """Get effective child group details  # noqa: E501

        Returns information about a specific effective child group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_view` privilege is required.  ***Example cURL requests***  **Get effective child details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_children/$CHILD_GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_group1\",   \"type\": \"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_child_group_with_http_info(id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str cid: Effective child group Id. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'cid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_effective_child_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_child_group`")  # noqa: E501
        # verify the required parameter 'cid' is set
        if ('cid' not in params or
                params['cid'] is None):
            raise ValueError("Missing the required parameter `cid` when calling `get_effective_child_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'cid' in params:
            path_params['cid'] = params['cid']  # noqa: E501

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
            '/groups/{id}/effective_children/{cid}', 'GET',
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

    def get_effective_child_group_membership_intermediaries(self, id, cid, **kwargs):  # noqa: E501
        """Get effective child's group membership intermediaries  # noqa: E501

        Returns the effective child's (`{cid}`) group membership intermediaries - entities from which the child inherits access to the group (`{id}`). Special keyword `\"self\"` in entity id indicates that the child (`{cid}`) has a direct access to the group (`{id}`).  This operation requires any of the following authentication: * as user who is an effective member of the child group (`{cid}`), * as user who has `group_view` privilege in the group (`{id}`), * as user who has `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get effective child's group membership intermediaries** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_children/$CHILD_GROUP_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"group\", \"id\": \"self\"}   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_child_group_membership_intermediaries(id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str cid: Child Id. (required)
        :return: MembershipIntermediaries
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_child_group_membership_intermediaries_with_http_info(id, cid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_child_group_membership_intermediaries_with_http_info(id, cid, **kwargs)  # noqa: E501
            return data

    def get_effective_child_group_membership_intermediaries_with_http_info(self, id, cid, **kwargs):  # noqa: E501
        """Get effective child's group membership intermediaries  # noqa: E501

        Returns the effective child's (`{cid}`) group membership intermediaries - entities from which the child inherits access to the group (`{id}`). Special keyword `\"self\"` in entity id indicates that the child (`{cid}`) has a direct access to the group (`{id}`).  This operation requires any of the following authentication: * as user who is an effective member of the child group (`{cid}`), * as user who has `group_view` privilege in the group (`{id}`), * as user who has `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get effective child's group membership intermediaries** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_children/$CHILD_GROUP_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"group\", \"id\": \"self\"}   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_child_group_membership_intermediaries_with_http_info(id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str cid: Child Id. (required)
        :return: MembershipIntermediaries
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'cid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_effective_child_group_membership_intermediaries" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_child_group_membership_intermediaries`")  # noqa: E501
        # verify the required parameter 'cid' is set
        if ('cid' not in params or
                params['cid'] is None):
            raise ValueError("Missing the required parameter `cid` when calling `get_effective_child_group_membership_intermediaries`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'cid' in params:
            path_params['cid'] = params['cid']  # noqa: E501

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
            '/groups/{id}/effective_children/{cid}/membership', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MembershipIntermediaries',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_effective_children_groups(self, id, **kwargs):  # noqa: E501
        """Get effective child groups  # noqa: E501

        Returns the list of effective child groups of a specific group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get effective child groups** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_children  {   \"groups\": [] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_children_groups(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Groups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_children_groups_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_children_groups_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_effective_children_groups_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get effective child groups  # noqa: E501

        Returns the list of effective child groups of a specific group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get effective child groups** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_children  {   \"groups\": [] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_children_groups_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
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
                    " to method get_effective_children_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_children_groups`")  # noqa: E501

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
            '/groups/{id}/effective_children', 'GET',
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

    def get_effective_group_handle(self, id, hid, **kwargs):  # noqa: E501
        """Get effective group handle details  # noqa: E501

        Returns the details of a specific effective handle.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_handles_view` privilege is required.  ***Example cURL requests***  **Get effective handle details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_handles/$HANDLE_ID  {   \"publicHandle\": \"10.5072/w95Zlng\",   \"handleId\": \"95b663a6467c72ab1256865efef9e387\",   \"handleServiceId\": \"97c27230017cd54c1220189e357322c4\",   \"resourceType\": \"Share\",   \"resourceId\": \"d6ee1aecf03b23f09756d6a49e435455\",   \"metadata\": \"<?xml version=\\\"1.0\\\"?>       <!DOCTYPE rdf:RDF SYSTEM \\\\\"http://dublincore.org/2000/12/01-dcmes-xml-dtd.dtd\\\">       <rdf:RDF xmlns:rdf=\\\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\\\"                xmlns:dc=\\\"http://purl.org/dc/elements/1.1/\\\">         <rdf:Description rdf:about=\\\"http://example.com/resouces/1\\\">           <dc:title>Example Resource</dc:title>           <dc:creator>John Doe</dc:creator>           <dc:publisher>MIT</dc:publisher>           <dc:date>2000-06-06</dc:date>         </rdf:Description>       </rdf:RDF>\",   \"timestamp\": \"1997-07-16T19:20\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_group_handle(id, hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str hid: Handle Id. (required)
        :return: Handle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_group_handle_with_http_info(id, hid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_group_handle_with_http_info(id, hid, **kwargs)  # noqa: E501
            return data

    def get_effective_group_handle_with_http_info(self, id, hid, **kwargs):  # noqa: E501
        """Get effective group handle details  # noqa: E501

        Returns the details of a specific effective handle.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_handles_view` privilege is required.  ***Example cURL requests***  **Get effective handle details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_handles/$HANDLE_ID  {   \"publicHandle\": \"10.5072/w95Zlng\",   \"handleId\": \"95b663a6467c72ab1256865efef9e387\",   \"handleServiceId\": \"97c27230017cd54c1220189e357322c4\",   \"resourceType\": \"Share\",   \"resourceId\": \"d6ee1aecf03b23f09756d6a49e435455\",   \"metadata\": \"<?xml version=\\\"1.0\\\"?>       <!DOCTYPE rdf:RDF SYSTEM \\\\\"http://dublincore.org/2000/12/01-dcmes-xml-dtd.dtd\\\">       <rdf:RDF xmlns:rdf=\\\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\\\"                xmlns:dc=\\\"http://purl.org/dc/elements/1.1/\\\">         <rdf:Description rdf:about=\\\"http://example.com/resouces/1\\\">           <dc:title>Example Resource</dc:title>           <dc:creator>John Doe</dc:creator>           <dc:publisher>MIT</dc:publisher>           <dc:date>2000-06-06</dc:date>         </rdf:Description>       </rdf:RDF>\",   \"timestamp\": \"1997-07-16T19:20\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_group_handle_with_http_info(id, hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
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
                    " to method get_effective_group_handle" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_group_handle`")  # noqa: E501
        # verify the required parameter 'hid' is set
        if ('hid' not in params or
                params['hid'] is None):
            raise ValueError("Missing the required parameter `hid` when calling `get_effective_group_handle`")  # noqa: E501

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
            '/groups/{id}/effective_handles/{hid}', 'GET',
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

    def get_effective_group_harvester(self, id, hid, **kwargs):  # noqa: E501
        """Get effective group harvester details  # noqa: E501

        Returns information about a specific effective harvester to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_harvesters_view` privilege is required.  ***Example cURL requests***  **Get group's harvester details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_harvesters/$HARVESTER_ID  {   \"harvesterId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_harvester1\",   \"public\" : true,   \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\",   \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_group_harvester(id, hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str hid: Effective harvester Id. (required)
        :return: Harvester
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_group_harvester_with_http_info(id, hid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_group_harvester_with_http_info(id, hid, **kwargs)  # noqa: E501
            return data

    def get_effective_group_harvester_with_http_info(self, id, hid, **kwargs):  # noqa: E501
        """Get effective group harvester details  # noqa: E501

        Returns information about a specific effective harvester to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_harvesters_view` privilege is required.  ***Example cURL requests***  **Get group's harvester details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_harvesters/$HARVESTER_ID  {   \"harvesterId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_harvester1\",   \"public\" : true,   \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\",   \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_group_harvester_with_http_info(id, hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str hid: Effective harvester Id. (required)
        :return: Harvester
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
                    " to method get_effective_group_harvester" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_group_harvester`")  # noqa: E501
        # verify the required parameter 'hid' is set
        if ('hid' not in params or
                params['hid'] is None):
            raise ValueError("Missing the required parameter `hid` when calling `get_effective_group_harvester`")  # noqa: E501

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
            '/groups/{id}/effective_harvesters/{hid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Harvester',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_effective_group_space(self, id, sid, **kwargs):  # noqa: E501
        """Get effective group space details  # noqa: E501

        Returns information about a specific effective space to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_spaces_view` privilege is required.  ***Example cURL requests***  **Get group's space details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_spaces/$SPACE_ID  {   \"spaceId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_space1\",   \"providers\": {     \"296ebe3c20e9666dc489b647f8647f12\" : 5368709120   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebfc1a770c3\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_group_space(id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str sid: Effective space Id. (required)
        :return: Space
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_group_space_with_http_info(id, sid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_group_space_with_http_info(id, sid, **kwargs)  # noqa: E501
            return data

    def get_effective_group_space_with_http_info(self, id, sid, **kwargs):  # noqa: E501
        """Get effective group space details  # noqa: E501

        Returns information about a specific effective space to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_spaces_view` privilege is required.  ***Example cURL requests***  **Get group's space details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_spaces/$SPACE_ID  {   \"spaceId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_space1\",   \"providers\": {     \"296ebe3c20e9666dc489b647f8647f12\" : 5368709120   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebfc1a770c3\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_group_space_with_http_info(id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str sid: Effective space Id. (required)
        :return: Space
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'sid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_effective_group_space" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_group_space`")  # noqa: E501
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `get_effective_group_space`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
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
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{id}/effective_spaces/{sid}', 'GET',
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

    def get_effective_group_user(self, id, uid, **kwargs):  # noqa: E501
        """Get effective group user details  # noqa: E501

        Returns information about a specific effective group user.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_users_view` privilege is required.  ***Example cURL requests***  **Get group user details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\", } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_group_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str uid: User Id. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_group_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_group_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def get_effective_group_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Get effective group user details  # noqa: E501

        Returns information about a specific effective group user.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_users_view` privilege is required.  ***Example cURL requests***  **Get group user details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\", } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_group_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str uid: User Id. (required)
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
                    " to method get_effective_group_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_group_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_effective_group_user`")  # noqa: E501

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
            '/groups/{id}/effective_users/{uid}', 'GET',
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

    def get_effective_parent_group(self, id, pid, **kwargs):  # noqa: E501
        """Get effective parent group details  # noqa: E501

        Returns details about a specific effective parent group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_view` privilege is required.  ***Example cURL requests***  **Get effective parent group details** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_parents/$PARENT_GROUP_ID  {   \"groupId\": \"9OqgExw00RwaU2MXT51\",   \"name\": \"Group1\",   \"type\": \"organization\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_parent_group(id, pid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str pid: Effective parent group Id. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_parent_group_with_http_info(id, pid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_parent_group_with_http_info(id, pid, **kwargs)  # noqa: E501
            return data

    def get_effective_parent_group_with_http_info(self, id, pid, **kwargs):  # noqa: E501
        """Get effective parent group details  # noqa: E501

        Returns details about a specific effective parent group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_view` privilege is required.  ***Example cURL requests***  **Get effective parent group details** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_parents/$PARENT_GROUP_ID  {   \"groupId\": \"9OqgExw00RwaU2MXT51\",   \"name\": \"Group1\",   \"type\": \"organization\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_parent_group_with_http_info(id, pid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str pid: Effective parent group Id. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'pid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_effective_parent_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_parent_group`")  # noqa: E501
        # verify the required parameter 'pid' is set
        if ('pid' not in params or
                params['pid'] is None):
            raise ValueError("Missing the required parameter `pid` when calling `get_effective_parent_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'pid' in params:
            path_params['pid'] = params['pid']  # noqa: E501

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
            '/groups/{id}/effective_parents/{pid}', 'GET',
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

    def get_effective_user_group_membership_intermediaries(self, id, uid, **kwargs):  # noqa: E501
        """Get effective user's group membership intermediaries  # noqa: E501

        Returns the effective user's (`{uid}`) group membership intermediaries - entities from which the user inherits access to the group (`{id}`). Special keyword `\"self\"` in entity id indicates that the user (`{uid}`) has a direct access to the group (`{id}`).  This operation requires any of the following authentication: * as user (`{uid}`) who is an effective member of the group (`{id}`), * as user who has `group_view` privilege in the group (`{id}`), * as user who has `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get effective user's group membership intermediaries** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_users/$USER_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"group\", \"id\": \"self\"}   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_user_group_membership_intermediaries(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str uid: User Id. (required)
        :return: MembershipIntermediaries
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_user_group_membership_intermediaries_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_user_group_membership_intermediaries_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def get_effective_user_group_membership_intermediaries_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Get effective user's group membership intermediaries  # noqa: E501

        Returns the effective user's (`{uid}`) group membership intermediaries - entities from which the user inherits access to the group (`{id}`). Special keyword `\"self\"` in entity id indicates that the user (`{uid}`) has a direct access to the group (`{id}`).  This operation requires any of the following authentication: * as user (`{uid}`) who is an effective member of the group (`{id}`), * as user who has `group_view` privilege in the group (`{id}`), * as user who has `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get effective user's group membership intermediaries** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_users/$USER_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"group\", \"id\": \"self\"}   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_user_group_membership_intermediaries_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str uid: User Id. (required)
        :return: MembershipIntermediaries
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
                    " to method get_effective_user_group_membership_intermediaries" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_user_group_membership_intermediaries`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_effective_user_group_membership_intermediaries`")  # noqa: E501

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
            '/groups/{id}/effective_users/{uid}/membership', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MembershipIntermediaries',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_group(self, id, **kwargs):  # noqa: E501
        """Get group details  # noqa: E501

        Returns the information about a specific group.  This operation requires membership in the group or `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID  {   \"groupId\": \"a4d3bc73aada63052310652d421609f1\",   \"name\": \"Test group\",   \"type\": \"team\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_group_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_group_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_group_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get group details  # noqa: E501

        Returns the information about a specific group.  This operation requires membership in the group or `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID  {   \"groupId\": \"a4d3bc73aada63052310652d421609f1\",   \"name\": \"Test group\",   \"type\": \"team\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Group
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
                    " to method get_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_group`")  # noqa: E501

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
            '/groups/{id}', 'GET',
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

    def get_group_cluster(self, id, cid, **kwargs):  # noqa: E501
        """Get group's cluster details  # noqa: E501

        Returns the details of a specific group's cluster.  This operation can be invoked on behalf of the current group only.  ***Example cURL requests***  **Get group's cluster details** ```bash curl -u groupname:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/group/clusters/$CLUSTER_ID  {   \"clusterId\": \"f8d843beda24e54545455ecc0f4b8886\",   \"type\": \"oneprovider\",   \"workerVersion\": {     \"release\": \"21.02.3\",     \"build\": \"1-gfabf02d\",     \"gui\": \"129c549fbe9b3e730c3d9910492228566e39e1236945766a74381405cc57fb04\"   },   \"onepanelVersion\": {     \"release\": \"21.02.3\",     \"build\": \"3-89fc6bad\",     \"gui\": \"68e7e1472adb719ddf2d88908775091dfb10e5d0b916f06125ea1af4056044e3\"   },   \"online\": true,   \"onepanelProxy\": false,   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_cluster(id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str cid: Cluster Id. (required)
        :return: Cluster
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_group_cluster_with_http_info(id, cid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_group_cluster_with_http_info(id, cid, **kwargs)  # noqa: E501
            return data

    def get_group_cluster_with_http_info(self, id, cid, **kwargs):  # noqa: E501
        """Get group's cluster details  # noqa: E501

        Returns the details of a specific group's cluster.  This operation can be invoked on behalf of the current group only.  ***Example cURL requests***  **Get group's cluster details** ```bash curl -u groupname:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/group/clusters/$CLUSTER_ID  {   \"clusterId\": \"f8d843beda24e54545455ecc0f4b8886\",   \"type\": \"oneprovider\",   \"workerVersion\": {     \"release\": \"21.02.3\",     \"build\": \"1-gfabf02d\",     \"gui\": \"129c549fbe9b3e730c3d9910492228566e39e1236945766a74381405cc57fb04\"   },   \"onepanelVersion\": {     \"release\": \"21.02.3\",     \"build\": \"3-89fc6bad\",     \"gui\": \"68e7e1472adb719ddf2d88908775091dfb10e5d0b916f06125ea1af4056044e3\"   },   \"online\": true,   \"onepanelProxy\": false,   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_cluster_with_http_info(id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str cid: Cluster Id. (required)
        :return: Cluster
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'cid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_group_cluster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_group_cluster`")  # noqa: E501
        # verify the required parameter 'cid' is set
        if ('cid' not in params or
                params['cid'] is None):
            raise ValueError("Missing the required parameter `cid` when calling `get_group_cluster`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'cid' in params:
            path_params['cid'] = params['cid']  # noqa: E501

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
            '/groups/{id}/clusters/{cid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Cluster',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_group_effective_cluster(self, id, cid, **kwargs):  # noqa: E501
        """Get group's effective cluster details  # noqa: E501

        Returns information about a specific effective cluster to which the group belongs.  This operation can be invoked on behalf of the current group only.  ***Example cURL requests***  **Get group's effective cluster details** ```bash curl -u groupname:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/group/clusters/$CLUSTER_ID  {   \"clusterId\": \"f8d843beda24e54545455ecc0f4b8886\",   \"type\": \"oneprovider\",   \"workerVersion\": {     \"release\": \"21.02.3\",     \"build\": \"1-gfabf02d\",     \"gui\": \"129c549fbe9b3e730c3d9910492228566e39e1236945766a74381405cc57fb04\"   },   \"onepanelVersion\": {     \"release\": \"21.02.3\",     \"build\": \"3-89fc6bad\",     \"gui\": \"68e7e1472adb719ddf2d88908775091dfb10e5d0b916f06125ea1af4056044e3\"   },   \"online\": true,   \"onepanelProxy\": false,   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_effective_cluster(id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str cid: Cluster Id. (required)
        :return: Cluster
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_group_effective_cluster_with_http_info(id, cid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_group_effective_cluster_with_http_info(id, cid, **kwargs)  # noqa: E501
            return data

    def get_group_effective_cluster_with_http_info(self, id, cid, **kwargs):  # noqa: E501
        """Get group's effective cluster details  # noqa: E501

        Returns information about a specific effective cluster to which the group belongs.  This operation can be invoked on behalf of the current group only.  ***Example cURL requests***  **Get group's effective cluster details** ```bash curl -u groupname:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/group/clusters/$CLUSTER_ID  {   \"clusterId\": \"f8d843beda24e54545455ecc0f4b8886\",   \"type\": \"oneprovider\",   \"workerVersion\": {     \"release\": \"21.02.3\",     \"build\": \"1-gfabf02d\",     \"gui\": \"129c549fbe9b3e730c3d9910492228566e39e1236945766a74381405cc57fb04\"   },   \"onepanelVersion\": {     \"release\": \"21.02.3\",     \"build\": \"3-89fc6bad\",     \"gui\": \"68e7e1472adb719ddf2d88908775091dfb10e5d0b916f06125ea1af4056044e3\"   },   \"online\": true,   \"onepanelProxy\": false,   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_effective_cluster_with_http_info(id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str cid: Cluster Id. (required)
        :return: Cluster
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'cid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_group_effective_cluster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_group_effective_cluster`")  # noqa: E501
        # verify the required parameter 'cid' is set
        if ('cid' not in params or
                params['cid'] is None):
            raise ValueError("Missing the required parameter `cid` when calling `get_group_effective_cluster`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'cid' in params:
            path_params['cid'] = params['cid']  # noqa: E501

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
            '/groups/{id}/effective_clusters/{cid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Cluster',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_group_effective_handle_service(self, id, hsid, **kwargs):  # noqa: E501
        """Get effective group handle service details  # noqa: E501

        Returns the details of a specific effective handle service.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_handle_services_view` privilege is required.  ***Example cURL requests***  **Get effective handle service details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_handle_services/$HANDLE_SERVICE_ID  {   \"handleServiceId\": \"0fe7c8a20ffdf07480c46f084bc3b8d5\",   \"name\": \"MyCommunity Handle service\",   \"proxyEndpoint\": \"https://localhost:17000/handle_proxy\",   \"serviceProperties\": {     \"allowTemplateOverride\": false,     \"doiEndpoint\": \"/doi\",     \"host\": \"https://mds.test.datacite.org\",     \"identifierTemplate\": \"{{space.name}}-{{space.guid}}\",     \"mediaEndpoint\": \"/media\",     \"metadataEndpoint\": \"/metadata\",     \"password\": \"pa$$word\",     \"prefix\": 10.5072,     \"type\": \"DOI\",     \"username\": \"alice\"   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_effective_handle_service(id, hsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str hsid: Handle service Id. (required)
        :return: HandleService
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_group_effective_handle_service_with_http_info(id, hsid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_group_effective_handle_service_with_http_info(id, hsid, **kwargs)  # noqa: E501
            return data

    def get_group_effective_handle_service_with_http_info(self, id, hsid, **kwargs):  # noqa: E501
        """Get effective group handle service details  # noqa: E501

        Returns the details of a specific effective handle service.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_handle_services_view` privilege is required.  ***Example cURL requests***  **Get effective handle service details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_handle_services/$HANDLE_SERVICE_ID  {   \"handleServiceId\": \"0fe7c8a20ffdf07480c46f084bc3b8d5\",   \"name\": \"MyCommunity Handle service\",   \"proxyEndpoint\": \"https://localhost:17000/handle_proxy\",   \"serviceProperties\": {     \"allowTemplateOverride\": false,     \"doiEndpoint\": \"/doi\",     \"host\": \"https://mds.test.datacite.org\",     \"identifierTemplate\": \"{{space.name}}-{{space.guid}}\",     \"mediaEndpoint\": \"/media\",     \"metadataEndpoint\": \"/metadata\",     \"password\": \"pa$$word\",     \"prefix\": 10.5072,     \"type\": \"DOI\",     \"username\": \"alice\"   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_effective_handle_service_with_http_info(id, hsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str hsid: Handle service Id. (required)
        :return: HandleService
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'hsid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_group_effective_handle_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_group_effective_handle_service`")  # noqa: E501
        # verify the required parameter 'hsid' is set
        if ('hsid' not in params or
                params['hsid'] is None):
            raise ValueError("Missing the required parameter `hsid` when calling `get_group_effective_handle_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'hsid' in params:
            path_params['hsid'] = params['hsid']  # noqa: E501

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
            '/groups/{id}/effective_handle_services/{hsid}', 'GET',
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

    def get_group_effective_provider(self, id, pid, **kwargs):  # noqa: E501
        """Get group's effective provider details  # noqa: E501

        Returns information about a specific effective provider for the group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_providers_view` privilege is required.  ***Example cURL requests***  **Get group's effective provider details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_providers/$PROVIDER_ID  {   \"providerId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"name\": \"Example provider\",   \"domain\": \"provider1.example.com\",   \"latitude\": 50.0647,   \"longitude\": 19.945,   \"clusterId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"online\": true,   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_effective_provider(id, pid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str pid: Effective provider Id. (required)
        :return: ProviderDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_group_effective_provider_with_http_info(id, pid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_group_effective_provider_with_http_info(id, pid, **kwargs)  # noqa: E501
            return data

    def get_group_effective_provider_with_http_info(self, id, pid, **kwargs):  # noqa: E501
        """Get group's effective provider details  # noqa: E501

        Returns information about a specific effective provider for the group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_providers_view` privilege is required.  ***Example cURL requests***  **Get group's effective provider details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_providers/$PROVIDER_ID  {   \"providerId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"name\": \"Example provider\",   \"domain\": \"provider1.example.com\",   \"latitude\": 50.0647,   \"longitude\": 19.945,   \"clusterId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"online\": true,   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_effective_provider_with_http_info(id, pid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str pid: Effective provider Id. (required)
        :return: ProviderDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'pid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_group_effective_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_group_effective_provider`")  # noqa: E501
        # verify the required parameter 'pid' is set
        if ('pid' not in params or
                params['pid'] is None):
            raise ValueError("Missing the required parameter `pid` when calling `get_group_effective_provider`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'pid' in params:
            path_params['pid'] = params['pid']  # noqa: E501

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
            '/groups/{id}/effective_providers/{pid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProviderDetails',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_group_handle(self, id, hid, **kwargs):  # noqa: E501
        """Get group handle details  # noqa: E501

        Returns the details of a specific handle.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_handles_view` privilege is required.  ***Example cURL requests***  **Get handle details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/handles/$HANDLE_ID  {   \"publicHandle\": \"10.5072/w95Zlng\",   \"handleId\": \"95b663a6467c72ab1256865efef9e387\",   \"handleServiceId\": \"97c27230017cd54c1220189e357322c4\",   \"resourceType\": \"Share\",   \"resourceId\": \"d6ee1aecf03b23f09756d6a49e435455\",   \"metadata\": \"<?xml version=\\\"1.0\\\"?>       <!DOCTYPE rdf:RDF SYSTEM \\\\\"http://dublincore.org/2000/12/01-dcmes-xml-dtd.dtd\\\">       <rdf:RDF xmlns:rdf=\\\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\\\"                xmlns:dc=\\\"http://purl.org/dc/elements/1.1/\\\">         <rdf:Description rdf:about=\\\"http://example.com/resouces/1\\\">           <dc:title>Example Resource</dc:title>           <dc:creator>John Doe</dc:creator>           <dc:publisher>MIT</dc:publisher>           <dc:date>2000-06-06</dc:date>         </rdf:Description>       </rdf:RDF>\",   \"timestamp\": \"1997-07-16T19:20\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_handle(id, hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str hid: Handle Id. (required)
        :return: Handle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_group_handle_with_http_info(id, hid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_group_handle_with_http_info(id, hid, **kwargs)  # noqa: E501
            return data

    def get_group_handle_with_http_info(self, id, hid, **kwargs):  # noqa: E501
        """Get group handle details  # noqa: E501

        Returns the details of a specific handle.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_handles_view` privilege is required.  ***Example cURL requests***  **Get handle details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/handles/$HANDLE_ID  {   \"publicHandle\": \"10.5072/w95Zlng\",   \"handleId\": \"95b663a6467c72ab1256865efef9e387\",   \"handleServiceId\": \"97c27230017cd54c1220189e357322c4\",   \"resourceType\": \"Share\",   \"resourceId\": \"d6ee1aecf03b23f09756d6a49e435455\",   \"metadata\": \"<?xml version=\\\"1.0\\\"?>       <!DOCTYPE rdf:RDF SYSTEM \\\\\"http://dublincore.org/2000/12/01-dcmes-xml-dtd.dtd\\\">       <rdf:RDF xmlns:rdf=\\\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\\\"                xmlns:dc=\\\"http://purl.org/dc/elements/1.1/\\\">         <rdf:Description rdf:about=\\\"http://example.com/resouces/1\\\">           <dc:title>Example Resource</dc:title>           <dc:creator>John Doe</dc:creator>           <dc:publisher>MIT</dc:publisher>           <dc:date>2000-06-06</dc:date>         </rdf:Description>       </rdf:RDF>\",   \"timestamp\": \"1997-07-16T19:20\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_handle_with_http_info(id, hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
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
                    " to method get_group_handle" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_group_handle`")  # noqa: E501
        # verify the required parameter 'hid' is set
        if ('hid' not in params or
                params['hid'] is None):
            raise ValueError("Missing the required parameter `hid` when calling `get_group_handle`")  # noqa: E501

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
            '/groups/{id}/handles/{hid}', 'GET',
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

    def get_group_handle_service(self, id, hsid, **kwargs):  # noqa: E501
        """Get group handle service details  # noqa: E501

        Returns the details of a specific handle service.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_handle_services_view` privilege is required.  ***Example cURL requests***  **Get handle service details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/handle_services/$HANDLE_SERVICE_ID  {   \"name\": \"MyCommunity Handle service\",   \"handleServiceId\": \"0fe7c8a20ffdf07480c46f084bc3b8d5\",   \"proxyEndpoint\": \"https://localhost:17000/handle_proxy\",   \"serviceProperties\": {     \"allowTemplateOverride\": false,     \"doiEndpoint\": \"/doi\",     \"host\": \"https://mds.test.datacite.org\",     \"identifierTemplate\": \"{{space.name}}-{{space.guid}}\",     \"mediaEndpoint\": \"/media\",     \"metadataEndpoint\": \"/metadata\",     \"password\": \"pa$$word\",     \"prefix\": 10.5072,     \"type\": \"DOI\",     \"username\": \"alice\"   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_handle_service(id, hsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str hsid: Handle service Id. (required)
        :return: HandleService
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_group_handle_service_with_http_info(id, hsid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_group_handle_service_with_http_info(id, hsid, **kwargs)  # noqa: E501
            return data

    def get_group_handle_service_with_http_info(self, id, hsid, **kwargs):  # noqa: E501
        """Get group handle service details  # noqa: E501

        Returns the details of a specific handle service.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_handle_services_view` privilege is required.  ***Example cURL requests***  **Get handle service details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/handle_services/$HANDLE_SERVICE_ID  {   \"name\": \"MyCommunity Handle service\",   \"handleServiceId\": \"0fe7c8a20ffdf07480c46f084bc3b8d5\",   \"proxyEndpoint\": \"https://localhost:17000/handle_proxy\",   \"serviceProperties\": {     \"allowTemplateOverride\": false,     \"doiEndpoint\": \"/doi\",     \"host\": \"https://mds.test.datacite.org\",     \"identifierTemplate\": \"{{space.name}}-{{space.guid}}\",     \"mediaEndpoint\": \"/media\",     \"metadataEndpoint\": \"/metadata\",     \"password\": \"pa$$word\",     \"prefix\": 10.5072,     \"type\": \"DOI\",     \"username\": \"alice\"   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_handle_service_with_http_info(id, hsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str hsid: Handle service Id. (required)
        :return: HandleService
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'hsid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_group_handle_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_group_handle_service`")  # noqa: E501
        # verify the required parameter 'hsid' is set
        if ('hsid' not in params or
                params['hsid'] is None):
            raise ValueError("Missing the required parameter `hsid` when calling `get_group_handle_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'hsid' in params:
            path_params['hsid'] = params['hsid']  # noqa: E501

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
            '/groups/{id}/handle_services/{hsid}', 'GET',
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

    def get_group_harvester(self, id, hid, **kwargs):  # noqa: E501
        """Get group's harvester details  # noqa: E501

        Returns information about a specific harvester to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_harvesters_view` privilege is required.  ***Example cURL requests***  **Get group's harvester details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/harvesters/$HARVESTER_ID  {   \"harvesterId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_harvester1\",   \"public\" : true,   \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\",   \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_harvester(id, hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str hid: Harvester Id. (required)
        :return: Harvester
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_group_harvester_with_http_info(id, hid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_group_harvester_with_http_info(id, hid, **kwargs)  # noqa: E501
            return data

    def get_group_harvester_with_http_info(self, id, hid, **kwargs):  # noqa: E501
        """Get group's harvester details  # noqa: E501

        Returns information about a specific harvester to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_harvesters_view` privilege is required.  ***Example cURL requests***  **Get group's harvester details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/harvesters/$HARVESTER_ID  {   \"harvesterId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_harvester1\",   \"public\" : true,   \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\",   \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_harvester_with_http_info(id, hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str hid: Harvester Id. (required)
        :return: Harvester
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
                    " to method get_group_harvester" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_group_harvester`")  # noqa: E501
        # verify the required parameter 'hid' is set
        if ('hid' not in params or
                params['hid'] is None):
            raise ValueError("Missing the required parameter `hid` when calling `get_group_harvester`")  # noqa: E501

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
            '/groups/{id}/harvesters/{hid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Harvester',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_group_space(self, id, sid, **kwargs):  # noqa: E501
        """Get group's space details  # noqa: E501

        Returns information about a specific space to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_spaces_view` privilege is required.  ***Example cURL requests***  **Get group's space details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/spaces/$SPACE_ID  {   \"spaceId\": \"7e1af0c5f0bfdfe9d2e7edb731247f5f\",   \"name\": \"Personal space\",   \"providers\": {     \"296ebe3c20e9666dc489b647f8647f12\" : 5368709120   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebfc1a770c3\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_space(id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str sid: Space Id. (required)
        :return: Space
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_group_space_with_http_info(id, sid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_group_space_with_http_info(id, sid, **kwargs)  # noqa: E501
            return data

    def get_group_space_with_http_info(self, id, sid, **kwargs):  # noqa: E501
        """Get group's space details  # noqa: E501

        Returns information about a specific space to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_spaces_view` privilege is required.  ***Example cURL requests***  **Get group's space details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/spaces/$SPACE_ID  {   \"spaceId\": \"7e1af0c5f0bfdfe9d2e7edb731247f5f\",   \"name\": \"Personal space\",   \"providers\": {     \"296ebe3c20e9666dc489b647f8647f12\" : 5368709120   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebfc1a770c3\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_space_with_http_info(id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str sid: Space Id. (required)
        :return: Space
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'sid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_group_space" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_group_space`")  # noqa: E501
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `get_group_space`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
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
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{id}/spaces/{sid}', 'GET',
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

    def get_group_spaces_in_effective_provider(self, id, pid, **kwargs):  # noqa: E501
        """Get group's spaces that are supported by given effective provider  # noqa: E501

        Returns the list of group's spaces that are supported by given effective provider.  This operation requires `group_view` privilege.  ***Example cURL requests***  **Get groups's spaces supported by effective provider** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_providers/$PROVIDER_ID/spaces  {   \"spaces\": [     \"6825604b0eb6a47b8b7a04b6369eb24d\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_spaces_in_effective_provider(id, pid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str pid: Effective provider Id. (required)
        :return: ProviderDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_group_spaces_in_effective_provider_with_http_info(id, pid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_group_spaces_in_effective_provider_with_http_info(id, pid, **kwargs)  # noqa: E501
            return data

    def get_group_spaces_in_effective_provider_with_http_info(self, id, pid, **kwargs):  # noqa: E501
        """Get group's spaces that are supported by given effective provider  # noqa: E501

        Returns the list of group's spaces that are supported by given effective provider.  This operation requires `group_view` privilege.  ***Example cURL requests***  **Get groups's spaces supported by effective provider** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_providers/$PROVIDER_ID/spaces  {   \"spaces\": [     \"6825604b0eb6a47b8b7a04b6369eb24d\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_spaces_in_effective_provider_with_http_info(id, pid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str pid: Effective provider Id. (required)
        :return: ProviderDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'pid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_group_spaces_in_effective_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_group_spaces_in_effective_provider`")  # noqa: E501
        # verify the required parameter 'pid' is set
        if ('pid' not in params or
                params['pid'] is None):
            raise ValueError("Missing the required parameter `pid` when calling `get_group_spaces_in_effective_provider`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'pid' in params:
            path_params['pid'] = params['pid']  # noqa: E501

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
            '/groups/{id}/effective_providers/{pid}/spaces', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProviderDetails',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_group_user(self, id, uid, **kwargs):  # noqa: E501
        """Get group user details  # noqa: E501

        Returns basic information about a user {uid} in group {id}.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_users_view` privilege is required.  ***Example cURL requests***  **Generate user group invite token** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\", } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str uid: User Id. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_group_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_group_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def get_group_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Get group user details  # noqa: E501

        Returns basic information about a user {uid} in group {id}.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_users_view` privilege is required.  ***Example cURL requests***  **Generate user group invite token** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\", } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str uid: User Id. (required)
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
                    " to method get_group_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_group_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_group_user`")  # noqa: E501

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
            '/groups/{id}/users/{uid}', 'GET',
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

    def get_parent_group(self, id, pid, **kwargs):  # noqa: E501
        """Get parent group details  # noqa: E501

        Returns details about a specific parent group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_view` privilege is required.  ***Example cURL requests***  **Get parent group details** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/parents/$PARENT_GROUP_ID  {   \"groupId\": \"9OqgExw00RwaU2MXT51\",   \"name\": \"Group1\",   \"type\": \"organization\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_parent_group(id, pid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str pid: Parent group Id. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_parent_group_with_http_info(id, pid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_parent_group_with_http_info(id, pid, **kwargs)  # noqa: E501
            return data

    def get_parent_group_with_http_info(self, id, pid, **kwargs):  # noqa: E501
        """Get parent group details  # noqa: E501

        Returns details about a specific parent group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_view` privilege is required.  ***Example cURL requests***  **Get parent group details** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/parents/$PARENT_GROUP_ID  {   \"groupId\": \"9OqgExw00RwaU2MXT51\",   \"name\": \"Group1\",   \"type\": \"organization\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_parent_group_with_http_info(id, pid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str pid: Parent group Id. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'pid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_parent_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_parent_group`")  # noqa: E501
        # verify the required parameter 'pid' is set
        if ('pid' not in params or
                params['pid'] is None):
            raise ValueError("Missing the required parameter `pid` when calling `get_parent_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'pid' in params:
            path_params['pid'] = params['pid']  # noqa: E501

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
            '/groups/{id}/parents/{pid}', 'GET',
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

    def group_join_cluster(self, body, id, **kwargs):  # noqa: E501
        """Join group to a cluster  # noqa: E501

        Join an existing cluster using an inivitation token.  ***Example cURL requests***  **Join group to an existing cluster** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"token\" : \"MDAxNmxvY2F00aW9uRVM2TVo5UlZ5cGFjZV9jcmLciFsOgyUkPI3f02le6PM01IX8go\" }'  \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/clusters/join ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_join_cluster(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ClusterInviteToken body: Token for joining a cluster. (required)
        :param str id: Group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.group_join_cluster_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.group_join_cluster_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def group_join_cluster_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Join group to a cluster  # noqa: E501

        Join an existing cluster using an inivitation token.  ***Example cURL requests***  **Join group to an existing cluster** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"token\" : \"MDAxNmxvY2F00aW9uRVM2TVo5UlZ5cGFjZV9jcmLciFsOgyUkPI3f02le6PM01IX8go\" }'  \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/clusters/join ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_join_cluster_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ClusterInviteToken body: Token for joining a cluster. (required)
        :param str id: Group Id. (required)
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
                    " to method group_join_cluster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `group_join_cluster`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `group_join_cluster`")  # noqa: E501

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
            '/groups/{id}/clusters/join', 'POST',
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

    def group_join_harvester(self, id, **kwargs):  # noqa: E501
        """Join harvester by group  # noqa: E501

        Joins the group to an existing harvester based on provided harvester invitation token.  This operation requires `group_add_harvester` privilege. For administrator who does not belong to this group `oz_harvesters_add_relationships` and `oz_groups_add_relationships` privilege is required.  ***Example cURL requests***  **Join group's harvester** ```bash curl -u admin:password -H \"Content-type: application/json\" \\ -d '{\"token\":\"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVuJ3l02U1JXzstRdK00ZHbso02rRcG8bJLAo\"}' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/harvesters/join ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_join_harvester(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param HarvesterInviteToken body: Harvester join token.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.group_join_harvester_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.group_join_harvester_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def group_join_harvester_with_http_info(self, id, **kwargs):  # noqa: E501
        """Join harvester by group  # noqa: E501

        Joins the group to an existing harvester based on provided harvester invitation token.  This operation requires `group_add_harvester` privilege. For administrator who does not belong to this group `oz_harvesters_add_relationships` and `oz_groups_add_relationships` privilege is required.  ***Example cURL requests***  **Join group's harvester** ```bash curl -u admin:password -H \"Content-type: application/json\" \\ -d '{\"token\":\"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVuJ3l02U1JXzstRdK00ZHbso02rRcG8bJLAo\"}' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/harvesters/join ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_join_harvester_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param HarvesterInviteToken body: Harvester join token.
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
                    " to method group_join_harvester" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `group_join_harvester`")  # noqa: E501

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
            '/groups/{id}/harvesters/join', 'POST',
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

    def group_join_space(self, id, **kwargs):  # noqa: E501
        """Join space by group  # noqa: E501

        Joins the group to an existing space based on provided space invitation token.  This operation requires `group_add_space` privilege. For administrator who does not belong to this group `oz_spaces_add_relationships` and `oz_groups_add_relationships` privilege is required.  ***Example cURL requests***  **Join group's space** ```bash curl -u admin:password -H \"Content-type: application/json\" \\ -d '{\"token\":\"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVuJ3l02U1JXzstRdK00ZHbso02rRcG8bJLAo\"}' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/spaces/join ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_join_space(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param SpaceInviteToken body: Space join token.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.group_join_space_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.group_join_space_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def group_join_space_with_http_info(self, id, **kwargs):  # noqa: E501
        """Join space by group  # noqa: E501

        Joins the group to an existing space based on provided space invitation token.  This operation requires `group_add_space` privilege. For administrator who does not belong to this group `oz_spaces_add_relationships` and `oz_groups_add_relationships` privilege is required.  ***Example cURL requests***  **Join group's space** ```bash curl -u admin:password -H \"Content-type: application/json\" \\ -d '{\"token\":\"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVuJ3l02U1JXzstRdK00ZHbso02rRcG8bJLAo\"}' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/spaces/join ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_join_space_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param SpaceInviteToken body: Space join token.
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
                    " to method group_join_space" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `group_join_space`")  # noqa: E501

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
            '/groups/{id}/spaces/join', 'POST',
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

    def group_leave_cluster(self, id, cid, **kwargs):  # noqa: E501
        """Leave cluster  # noqa: E501

        Removes the groups membership in a specific cluster.  ***Example cURL requests***  **Group leave cluster** ```bash curl -u groupname:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/clusters/$CLUSTER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_leave_cluster(id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str cid: Cluster Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.group_leave_cluster_with_http_info(id, cid, **kwargs)  # noqa: E501
        else:
            (data) = self.group_leave_cluster_with_http_info(id, cid, **kwargs)  # noqa: E501
            return data

    def group_leave_cluster_with_http_info(self, id, cid, **kwargs):  # noqa: E501
        """Leave cluster  # noqa: E501

        Removes the groups membership in a specific cluster.  ***Example cURL requests***  **Group leave cluster** ```bash curl -u groupname:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/clusters/$CLUSTER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_leave_cluster_with_http_info(id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str cid: Cluster Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'cid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method group_leave_cluster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `group_leave_cluster`")  # noqa: E501
        # verify the required parameter 'cid' is set
        if ('cid' not in params or
                params['cid'] is None):
            raise ValueError("Missing the required parameter `cid` when calling `group_leave_cluster`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'cid' in params:
            path_params['cid'] = params['cid']  # noqa: E501

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
            '/groups/{id}/clusters/{cid}', 'DELETE',
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

    def group_leave_handle(self, id, hid, **kwargs):  # noqa: E501
        """Group leave handle  # noqa: E501

        Removes the group's ownership or access to a specific handle.  This operation requires `group_leave_handle` privilege. For administrator who does not belong to this group `oz_groups_remove_relationships` and `oz_handles_remove_relationships` privileges are required.  ***Example cURL requests***  **Delete user space** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/handles/$HANDLE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_leave_handle(id, hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str hid: Handle Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.group_leave_handle_with_http_info(id, hid, **kwargs)  # noqa: E501
        else:
            (data) = self.group_leave_handle_with_http_info(id, hid, **kwargs)  # noqa: E501
            return data

    def group_leave_handle_with_http_info(self, id, hid, **kwargs):  # noqa: E501
        """Group leave handle  # noqa: E501

        Removes the group's ownership or access to a specific handle.  This operation requires `group_leave_handle` privilege. For administrator who does not belong to this group `oz_groups_remove_relationships` and `oz_handles_remove_relationships` privileges are required.  ***Example cURL requests***  **Delete user space** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/handles/$HANDLE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_leave_handle_with_http_info(id, hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str hid: Handle Id. (required)
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
                    " to method group_leave_handle" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `group_leave_handle`")  # noqa: E501
        # verify the required parameter 'hid' is set
        if ('hid' not in params or
                params['hid'] is None):
            raise ValueError("Missing the required parameter `hid` when calling `group_leave_handle`")  # noqa: E501

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
            '/groups/{id}/handles/{hid}', 'DELETE',
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

    def group_leave_handle_service(self, id, hsid, **kwargs):  # noqa: E501
        """Group leave handle service  # noqa: E501

        Removes the group's ownership or access to a specific handle service.  This operation requires `group_leave_handle_service` privilege. For administrator who does not belong to this group `oz_groups_remove_relationships` and `oz_handle_services_remove_relationships` privilege is required.  ***Example cURL requests***  **Delete user handle service** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/handle_services/$HANDLE_SERVICE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_leave_handle_service(id, hsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str hsid: Handle service Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.group_leave_handle_service_with_http_info(id, hsid, **kwargs)  # noqa: E501
        else:
            (data) = self.group_leave_handle_service_with_http_info(id, hsid, **kwargs)  # noqa: E501
            return data

    def group_leave_handle_service_with_http_info(self, id, hsid, **kwargs):  # noqa: E501
        """Group leave handle service  # noqa: E501

        Removes the group's ownership or access to a specific handle service.  This operation requires `group_leave_handle_service` privilege. For administrator who does not belong to this group `oz_groups_remove_relationships` and `oz_handle_services_remove_relationships` privilege is required.  ***Example cURL requests***  **Delete user handle service** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/handle_services/$HANDLE_SERVICE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.group_leave_handle_service_with_http_info(id, hsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str hsid: Handle service Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'hsid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method group_leave_handle_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `group_leave_handle_service`")  # noqa: E501
        # verify the required parameter 'hsid' is set
        if ('hsid' not in params or
                params['hsid'] is None):
            raise ValueError("Missing the required parameter `hsid` when calling `group_leave_handle_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'hsid' in params:
            path_params['hsid'] = params['hsid']  # noqa: E501

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
            '/groups/{id}/handle_services/{hsid}', 'DELETE',
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

    def join_parent_group(self, id, **kwargs):  # noqa: E501
        """Join parent group  # noqa: E501

        Adds given group as a child group of a specific group based on provided token.  The parent group to which the group will be added is identified from the token (the token is issued in the context of a group).  This operation requires `group_add_parent` privilege. For administrator who does not belong to this group `oz_groups_add_relationships` privilege is required.  ***Example cURL requests***  **Join parent group**  ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d  '{\"token\":\"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaW\"}'  \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/parents/join ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.join_parent_group(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param GroupInviteToken body: Group join token.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.join_parent_group_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.join_parent_group_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def join_parent_group_with_http_info(self, id, **kwargs):  # noqa: E501
        """Join parent group  # noqa: E501

        Adds given group as a child group of a specific group based on provided token.  The parent group to which the group will be added is identified from the token (the token is issued in the context of a group).  This operation requires `group_add_parent` privilege. For administrator who does not belong to this group `oz_groups_add_relationships` privilege is required.  ***Example cURL requests***  **Join parent group**  ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d  '{\"token\":\"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaW\"}'  \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/parents/join ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.join_parent_group_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param GroupInviteToken body: Group join token.
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
                    " to method join_parent_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `join_parent_group`")  # noqa: E501

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
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{id}/parents/join', 'POST',
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

    def leave_parent_group(self, id, pid, **kwargs):  # noqa: E501
        """Leave parent group  # noqa: E501

        Removes the group access to a specific parent group.  This operation requires `group_leave_parent` privilege. For administrator who does not belong to this group `oz_groups_remove_relationships` privilege is required.  ***Example cURL requests***  **Leave parent group as group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/parents/$PARENT_GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.leave_parent_group(id, pid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str pid: Parent group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.leave_parent_group_with_http_info(id, pid, **kwargs)  # noqa: E501
        else:
            (data) = self.leave_parent_group_with_http_info(id, pid, **kwargs)  # noqa: E501
            return data

    def leave_parent_group_with_http_info(self, id, pid, **kwargs):  # noqa: E501
        """Leave parent group  # noqa: E501

        Removes the group access to a specific parent group.  This operation requires `group_leave_parent` privilege. For administrator who does not belong to this group `oz_groups_remove_relationships` privilege is required.  ***Example cURL requests***  **Leave parent group as group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/parents/$PARENT_GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.leave_parent_group_with_http_info(id, pid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str pid: Parent group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'pid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method leave_parent_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `leave_parent_group`")  # noqa: E501
        # verify the required parameter 'pid' is set
        if ('pid' not in params or
                params['pid'] is None):
            raise ValueError("Missing the required parameter `pid` when calling `leave_parent_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'pid' in params:
            path_params['pid'] = params['pid']  # noqa: E501

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
            '/groups/{id}/parents/{pid}', 'DELETE',
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

    def list_child_group_privileges(self, id, cid, **kwargs):  # noqa: E501
        """List child's group privileges  # noqa: E501

        Returns the list of child group's (`{cid}`) privileges in a group (`{id}`).  This operation requires `group_view_privileges` privilege. For administrator who does not belong to this group `oz_groups_view_privileges` privilege is required.  ***Example cURL requests***  **List child group's privileges in a group** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/children/$CHILD_GROUP_ID/privileges  {   \"privileges\": [     \"group_view\",     \"group_update\",     \"group_delete\",     \"group_view_privileges\",     \"group_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_child_group_privileges(id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str cid: Child group Id. (required)
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_child_group_privileges_with_http_info(id, cid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_child_group_privileges_with_http_info(id, cid, **kwargs)  # noqa: E501
            return data

    def list_child_group_privileges_with_http_info(self, id, cid, **kwargs):  # noqa: E501
        """List child's group privileges  # noqa: E501

        Returns the list of child group's (`{cid}`) privileges in a group (`{id}`).  This operation requires `group_view_privileges` privilege. For administrator who does not belong to this group `oz_groups_view_privileges` privilege is required.  ***Example cURL requests***  **List child group's privileges in a group** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/children/$CHILD_GROUP_ID/privileges  {   \"privileges\": [     \"group_view\",     \"group_update\",     \"group_delete\",     \"group_view_privileges\",     \"group_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_child_group_privileges_with_http_info(id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str cid: Child group Id. (required)
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'cid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_child_group_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_child_group_privileges`")  # noqa: E501
        # verify the required parameter 'cid' is set
        if ('cid' not in params or
                params['cid'] is None):
            raise ValueError("Missing the required parameter `cid` when calling `list_child_group_privileges`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'cid' in params:
            path_params['cid'] = params['cid']  # noqa: E501

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
            '/groups/{id}/children/{cid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_child_groups(self, id, **kwargs):  # noqa: E501
        """Get child groups  # noqa: E501

        Returns the list of child groups of a specific group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get child groups** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/children  {   \"groups\": [] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_child_groups(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Groups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_child_groups_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_child_groups_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_child_groups_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get child groups  # noqa: E501

        Returns the list of child groups of a specific group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get child groups** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/children  {   \"groups\": [] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_child_groups_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
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
                    " to method list_child_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_child_groups`")  # noqa: E501

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
            '/groups/{id}/children', 'GET',
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

    def list_effective_child_group_privileges(self, id, cid, **kwargs):  # noqa: E501
        """List effective child's group privileges  # noqa: E501

        Returns the list of effective child group's (`{cid}`) privileges in a group (`{id}`).  Effective privileges are a sum of child group's privileges and privileges inherited from its parent group memberships.  This operation requires `group_view_privileges` privilege. For administrator who does not belong to this group `oz_groups_view_privileges` privilege is required.  ***Example cURL requests***  **List effective child group's privileges in a group** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_children/$CHILD_GROUP_ID/privileges  {   \"privileges\": [     \"group_view\",     \"group_update\",     \"group_delete\",     \"group_view_privileges\",     \"group_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_child_group_privileges(id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str cid: Effective child group Id. (required)
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_child_group_privileges_with_http_info(id, cid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_child_group_privileges_with_http_info(id, cid, **kwargs)  # noqa: E501
            return data

    def list_effective_child_group_privileges_with_http_info(self, id, cid, **kwargs):  # noqa: E501
        """List effective child's group privileges  # noqa: E501

        Returns the list of effective child group's (`{cid}`) privileges in a group (`{id}`).  Effective privileges are a sum of child group's privileges and privileges inherited from its parent group memberships.  This operation requires `group_view_privileges` privilege. For administrator who does not belong to this group `oz_groups_view_privileges` privilege is required.  ***Example cURL requests***  **List effective child group's privileges in a group** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_children/$CHILD_GROUP_ID/privileges  {   \"privileges\": [     \"group_view\",     \"group_update\",     \"group_delete\",     \"group_view_privileges\",     \"group_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_child_group_privileges_with_http_info(id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str cid: Effective child group Id. (required)
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'cid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_effective_child_group_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_child_group_privileges`")  # noqa: E501
        # verify the required parameter 'cid' is set
        if ('cid' not in params or
                params['cid'] is None):
            raise ValueError("Missing the required parameter `cid` when calling `list_effective_child_group_privileges`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'cid' in params:
            path_params['cid'] = params['cid']  # noqa: E501

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
            '/groups/{id}/effective_children/{cid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_effective_group_handle_services(self, id, **kwargs):  # noqa: E501
        """List effective group handle services  # noqa: E501

        Returns the list of registered group effective handle services.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group effective handle services** ```bash curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_handle_services  {   \"handle_services\": [     \"95b663a6467c72ab1256865efef9e387\",     \"67222da37f90559bcca1f85edd745e5c\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_handle_services(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: HandleServices
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_group_handle_services_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_group_handle_services_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_effective_group_handle_services_with_http_info(self, id, **kwargs):  # noqa: E501
        """List effective group handle services  # noqa: E501

        Returns the list of registered group effective handle services.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group effective handle services** ```bash curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_handle_services  {   \"handle_services\": [     \"95b663a6467c72ab1256865efef9e387\",     \"67222da37f90559bcca1f85edd745e5c\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_handle_services_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: HandleServices
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
                    " to method list_effective_group_handle_services" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_group_handle_services`")  # noqa: E501

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
            '/groups/{id}/effective_handle_services', 'GET',
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

    def list_effective_group_handles(self, id, **kwargs):  # noqa: E501
        """List effective group handles  # noqa: E501

        Returns the list of effective groups' handles.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **List effective group handles** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_handles  {   \"handles\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_handles(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Handles
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_group_handles_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_group_handles_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_effective_group_handles_with_http_info(self, id, **kwargs):  # noqa: E501
        """List effective group handles  # noqa: E501

        Returns the list of effective groups' handles.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **List effective group handles** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_handles  {   \"handles\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_handles_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
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
                    " to method list_effective_group_handles" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_group_handles`")  # noqa: E501

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
            '/groups/{id}/effective_handles', 'GET',
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

    def list_effective_group_harvesters(self, id, **kwargs):  # noqa: E501
        """List effective group's harvesters  # noqa: E501

        Returns the effective list of harvesters to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group effective harvesters** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_harvesters  {   \"harvesters\": [     \"GVC8lKEasj4q253sptVqF8HwUpk8jrwxKOe45uzLFX2\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_harvesters(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Harvesters
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_group_harvesters_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_group_harvesters_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_effective_group_harvesters_with_http_info(self, id, **kwargs):  # noqa: E501
        """List effective group's harvesters  # noqa: E501

        Returns the effective list of harvesters to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group effective harvesters** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_harvesters  {   \"harvesters\": [     \"GVC8lKEasj4q253sptVqF8HwUpk8jrwxKOe45uzLFX2\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_harvesters_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Harvesters
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
                    " to method list_effective_group_harvesters" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_group_harvesters`")  # noqa: E501

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
            '/groups/{id}/effective_harvesters', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Harvesters',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_effective_group_providers(self, id, **kwargs):  # noqa: E501
        """List effective group's providers  # noqa: E501

        Returns the list of effective providers supporting group spaces.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group effective providers** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_providers ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_providers(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Providers
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_group_providers_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_group_providers_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_effective_group_providers_with_http_info(self, id, **kwargs):  # noqa: E501
        """List effective group's providers  # noqa: E501

        Returns the list of effective providers supporting group spaces.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group effective providers** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_providers ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_providers_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Providers
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
                    " to method list_effective_group_providers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_group_providers`")  # noqa: E501

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
            '/groups/{id}/effective_providers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Providers',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_effective_group_spaces(self, id, **kwargs):  # noqa: E501
        """List effective group's spaces  # noqa: E501

        Returns the list of effective spaces to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group effective spaces** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_spaces  {   \"spaces\": [     \"GVC8lKEasj4q253sptVqF8HwUpk8jrwxKOe45uzLFX2\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_spaces(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Spaces
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_group_spaces_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_group_spaces_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_effective_group_spaces_with_http_info(self, id, **kwargs):  # noqa: E501
        """List effective group's spaces  # noqa: E501

        Returns the list of effective spaces to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group effective spaces** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_spaces  {   \"spaces\": [     \"GVC8lKEasj4q253sptVqF8HwUpk8jrwxKOe45uzLFX2\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_spaces_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Spaces
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
                    " to method list_effective_group_spaces" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_group_spaces`")  # noqa: E501

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
            '/groups/{id}/effective_spaces', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Spaces',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_effective_group_users(self, id, **kwargs):  # noqa: E501
        """List effective group users  # noqa: E501

        Returns the list of effective group users, which includes both who directly belong to the group, as well as users who belong to the group indirectly through its parent groups.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get effective group users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_users  {   \"users\":  [     \"lb0NvUXIVguzjQ3dBOXAyd1c11fWKB5dKJDQ6YvB7a0\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_users(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_group_users_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_group_users_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_effective_group_users_with_http_info(self, id, **kwargs):  # noqa: E501
        """List effective group users  # noqa: E501

        Returns the list of effective group users, which includes both who directly belong to the group, as well as users who belong to the group indirectly through its parent groups.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get effective group users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_users  {   \"users\":  [     \"lb0NvUXIVguzjQ3dBOXAyd1c11fWKB5dKJDQ6YvB7a0\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_users_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
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
                    " to method list_effective_group_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_group_users`")  # noqa: E501

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
            '/groups/{id}/effective_users', 'GET',
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

    def list_effective_parent_groups(self, id, **kwargs):  # noqa: E501
        """List effective parent groups  # noqa: E501

        Returns the effective parent groups of a specific group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get effective parent groups** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_parents  {   \"groups\": [] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_parent_groups(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Groups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_parent_groups_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_parent_groups_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_effective_parent_groups_with_http_info(self, id, **kwargs):  # noqa: E501
        """List effective parent groups  # noqa: E501

        Returns the effective parent groups of a specific group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get effective parent groups** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_parents  {   \"groups\": [] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_parent_groups_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
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
                    " to method list_effective_parent_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_parent_groups`")  # noqa: E501

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
            '/groups/{id}/effective_parents', 'GET',
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

    def list_effective_user_group_privileges(self, id, uid, **kwargs):  # noqa: E501
        """List effective user's group privileges  # noqa: E501

        Returns the list of effective user's (`{uid}`) privileges in a group (`{id}`).  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation requires `group_view_privileges` privilege. For administrator who does not belong to this group `oz_groups_view_privileges` privilege is required.  ***Example cURL requests***  **List effective user's privileges in a group** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_users/$USER_ID/privileges  {   \"privileges\": [     \"group_view\",     \"group_update\",     \"group_delete\",     \"group_view_privileges\",     \"group_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_user_group_privileges(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str uid: User Id. (required)
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_user_group_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_user_group_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def list_effective_user_group_privileges_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """List effective user's group privileges  # noqa: E501

        Returns the list of effective user's (`{uid}`) privileges in a group (`{id}`).  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation requires `group_view_privileges` privilege. For administrator who does not belong to this group `oz_groups_view_privileges` privilege is required.  ***Example cURL requests***  **List effective user's privileges in a group** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_users/$USER_ID/privileges  {   \"privileges\": [     \"group_view\",     \"group_update\",     \"group_delete\",     \"group_view_privileges\",     \"group_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_user_group_privileges_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str uid: User Id. (required)
        :return: InlineResponse2005
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
                    " to method list_effective_user_group_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_user_group_privileges`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `list_effective_user_group_privileges`")  # noqa: E501

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
            '/groups/{id}/effective_users/{uid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_group_admin_privileges(self, id, **kwargs):  # noqa: E501
        """List group's admin privileges  # noqa: E501

        Returns the list of group's (`{id}`) admin privileges in Onezone.  This operation requires `oz_view_privileges` admin privilege.  ***Example cURL requests***  **List group's admin privileges in Onezone** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/privileges  {   \"privileges\": [     \"oz_view_privileges\",     \"oz_users_list\",     \"oz_users_view\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handles_list\",     \"oz_handles_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_admin_privileges(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_group_admin_privileges_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_group_admin_privileges_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_group_admin_privileges_with_http_info(self, id, **kwargs):  # noqa: E501
        """List group's admin privileges  # noqa: E501

        Returns the list of group's (`{id}`) admin privileges in Onezone.  This operation requires `oz_view_privileges` admin privilege.  ***Example cURL requests***  **List group's admin privileges in Onezone** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/privileges  {   \"privileges\": [     \"oz_view_privileges\",     \"oz_users_list\",     \"oz_users_view\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handles_list\",     \"oz_handles_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_admin_privileges_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: InlineResponse2001
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
                    " to method list_group_admin_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_group_admin_privileges`")  # noqa: E501

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
            '/groups/{id}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_group_clusters(self, id, **kwargs):  # noqa: E501
        """List group's clusters  # noqa: E501

        Returns the list of clusters to which the group has access.  ***Example cURL requests***  **Get group's clusters** ```bash curl -u groupname:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/group/GVC8lKEasj4q253sptVqF8HwUpk8j/clusters  {   \"clusters\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_clusters(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Clusters
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_group_clusters_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_group_clusters_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_group_clusters_with_http_info(self, id, **kwargs):  # noqa: E501
        """List group's clusters  # noqa: E501

        Returns the list of clusters to which the group has access.  ***Example cURL requests***  **Get group's clusters** ```bash curl -u groupname:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/group/GVC8lKEasj4q253sptVqF8HwUpk8j/clusters  {   \"clusters\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_clusters_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Clusters
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
                    " to method list_group_clusters" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_group_clusters`")  # noqa: E501

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
            '/groups/{id}/clusters', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Clusters',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_group_effective_admin_privileges(self, id, **kwargs):  # noqa: E501
        """List group's effective admin privileges  # noqa: E501

        Returns the list of group's (`{id}`) effective admin privileges in Onezone.  Effective privileges are a sum of group's privileges and privileges inherited from its parent group memberships.  This operation requires `oz_view_privileges` admin privilege.  ***Example cURL requests***  **List group's effective admin privileges in Onezone** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_privileges  {   \"privileges\": [     \"oz_view_privileges\",     \"oz_users_list\",     \"oz_users_view\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handles_list\",     \"oz_handles_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_effective_admin_privileges(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_group_effective_admin_privileges_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_group_effective_admin_privileges_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_group_effective_admin_privileges_with_http_info(self, id, **kwargs):  # noqa: E501
        """List group's effective admin privileges  # noqa: E501

        Returns the list of group's (`{id}`) effective admin privileges in Onezone.  Effective privileges are a sum of group's privileges and privileges inherited from its parent group memberships.  This operation requires `oz_view_privileges` admin privilege.  ***Example cURL requests***  **List group's effective admin privileges in Onezone** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_privileges  {   \"privileges\": [     \"oz_view_privileges\",     \"oz_users_list\",     \"oz_users_view\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handles_list\",     \"oz_handles_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_effective_admin_privileges_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: InlineResponse2001
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
                    " to method list_group_effective_admin_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_group_effective_admin_privileges`")  # noqa: E501

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
            '/groups/{id}/effective_privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_group_effective_clusters(self, id, **kwargs):  # noqa: E501
        """List group's effective clusters  # noqa: E501

        Returns the list of effective clusters to which the group has access.  ***Example cURL requests***  **Get group's effective clusters** ```bash curl -u groupname:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_clusters  {   \"clusters\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_effective_clusters(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Clusters
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_group_effective_clusters_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_group_effective_clusters_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_group_effective_clusters_with_http_info(self, id, **kwargs):  # noqa: E501
        """List group's effective clusters  # noqa: E501

        Returns the list of effective clusters to which the group has access.  ***Example cURL requests***  **Get group's effective clusters** ```bash curl -u groupname:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/effective_clusters  {   \"clusters\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_effective_clusters_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Clusters
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
                    " to method list_group_effective_clusters" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_group_effective_clusters`")  # noqa: E501

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
            '/groups/{id}/effective_clusters', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Clusters',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_group_handle_services(self, id, **kwargs):  # noqa: E501
        """List group handle services  # noqa: E501

        Returns the list of registered group handle services.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group handle services** ```bash curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/handle_services  {   \"handle_services\": [     \"0fe7c8a20ffdf07480c46f084bc3b8d5\",     \"302da048de67e2ea05f0af1d0fe7c8a2\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_handle_services(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: HandleServices
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_group_handle_services_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_group_handle_services_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_group_handle_services_with_http_info(self, id, **kwargs):  # noqa: E501
        """List group handle services  # noqa: E501

        Returns the list of registered group handle services.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group handle services** ```bash curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/handle_services  {   \"handle_services\": [     \"0fe7c8a20ffdf07480c46f084bc3b8d5\",     \"302da048de67e2ea05f0af1d0fe7c8a2\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_handle_services_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: HandleServices
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
                    " to method list_group_handle_services" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_group_handle_services`")  # noqa: E501

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
            '/groups/{id}/handle_services', 'GET',
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

    def list_group_handles(self, id, **kwargs):  # noqa: E501
        """List group handles  # noqa: E501

        Returns the list of groups handles.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group handles** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/handles  {   \"handles\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_handles(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Handles
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_group_handles_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_group_handles_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_group_handles_with_http_info(self, id, **kwargs):  # noqa: E501
        """List group handles  # noqa: E501

        Returns the list of groups handles.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group handles** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/handles  {   \"handles\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_handles_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
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
                    " to method list_group_handles" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_group_handles`")  # noqa: E501

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
            '/groups/{id}/handles', 'GET',
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

    def list_group_harvesters(self, id, **kwargs):  # noqa: E501
        """List group's harvesters  # noqa: E501

        Returns the list of harvesters to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group harvesters** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/harvesters  {   \"harvesters\": [     \"GVC8lKEasj4q253sptVqF8HwUpk8jrwxKOe45uzLFX2\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_harvesters(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Harvesters
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_group_harvesters_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_group_harvesters_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_group_harvesters_with_http_info(self, id, **kwargs):  # noqa: E501
        """List group's harvesters  # noqa: E501

        Returns the list of harvesters to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group harvesters** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/harvesters  {   \"harvesters\": [     \"GVC8lKEasj4q253sptVqF8HwUpk8jrwxKOe45uzLFX2\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_harvesters_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Harvesters
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
                    " to method list_group_harvesters" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_group_harvesters`")  # noqa: E501

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
            '/groups/{id}/harvesters', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Harvesters',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_group_privileges(self, **kwargs):  # noqa: E501
        """List all group privileges  # noqa: E501

        Returns list of all possible group privileges.  This endpoint does not require authentication.  ***Example cURL requests***  **Get list of all group privileges** ```bash curl https://$ZONE_HOST/api/v3/onezone/groups/privileges  {   \"admin\": [     \"group_view\",     \"group_update\",     \"group_delete\",     \"group_view_privileges\",     \"group_set_privileges\",     \"group_add_parent\",     \"group_leave_parent\",     \"group_add_child\",     \"group_remove_child\",     \"group_add_user\",     \"group_remove_user\",     \"group_add_space\",     \"group_leave_space\",     \"group_create_handle_service\",     \"group_leave_handle_service\",     \"group_create_handle\",     \"group_leave_handle\",     \"group_add_harvester\",     \"group_remove_harvester\"   ],   \"manager\": [     \"group_view\",     \"group_view_privileges\",     \"group_add_parent\",     \"group_leave_parent\",     \"group_add_child\",     \"group_remove_child\",     \"group_add_user\",     \"group_remove_user\",     \"group_add_harvester\",     \"group_remove_harvester\"   ],   \"member\": [     \"group_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_privileges(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_group_privileges_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_group_privileges_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_group_privileges_with_http_info(self, **kwargs):  # noqa: E501
        """List all group privileges  # noqa: E501

        Returns list of all possible group privileges.  This endpoint does not require authentication.  ***Example cURL requests***  **Get list of all group privileges** ```bash curl https://$ZONE_HOST/api/v3/onezone/groups/privileges  {   \"admin\": [     \"group_view\",     \"group_update\",     \"group_delete\",     \"group_view_privileges\",     \"group_set_privileges\",     \"group_add_parent\",     \"group_leave_parent\",     \"group_add_child\",     \"group_remove_child\",     \"group_add_user\",     \"group_remove_user\",     \"group_add_space\",     \"group_leave_space\",     \"group_create_handle_service\",     \"group_leave_handle_service\",     \"group_create_handle\",     \"group_leave_handle\",     \"group_add_harvester\",     \"group_remove_harvester\"   ],   \"manager\": [     \"group_view\",     \"group_view_privileges\",     \"group_add_parent\",     \"group_leave_parent\",     \"group_add_child\",     \"group_remove_child\",     \"group_add_user\",     \"group_remove_user\",     \"group_add_harvester\",     \"group_remove_harvester\"   ],   \"member\": [     \"group_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_privileges_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2004
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
                    " to method list_group_privileges" % key
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
            '/groups/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_group_spaces(self, id, **kwargs):  # noqa: E501
        """List group's spaces  # noqa: E501

        Returns the list of spaces to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group spaces** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/spaces  {   \"spaces\": [     \"GVC8lKEasj4q253sptVqF8HwUpk8jrwxKOe45uzLFX2\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_spaces(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Spaces
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_group_spaces_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_group_spaces_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_group_spaces_with_http_info(self, id, **kwargs):  # noqa: E501
        """List group's spaces  # noqa: E501

        Returns the list of spaces to which the group has access.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group spaces** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/spaces  {   \"spaces\": [     \"GVC8lKEasj4q253sptVqF8HwUpk8jrwxKOe45uzLFX2\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_spaces_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Spaces
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
                    " to method list_group_spaces" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_group_spaces`")  # noqa: E501

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
            '/groups/{id}/spaces', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Spaces',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_group_users(self, id, **kwargs):  # noqa: E501
        """List group users  # noqa: E501

        Returns the list of users belonging to a specific group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/users  {   \"users\": [     \"a5b469a2b0516b662a49da74d6d7d7bc\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_users(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_group_users_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_group_users_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_group_users_with_http_info(self, id, **kwargs):  # noqa: E501
        """List group users  # noqa: E501

        Returns the list of users belonging to a specific group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get group users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/users  {   \"users\": [     \"a5b469a2b0516b662a49da74d6d7d7bc\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_users_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
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
                    " to method list_group_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_group_users`")  # noqa: E501

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
            '/groups/{id}/users', 'GET',
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

    def list_groups(self, **kwargs):  # noqa: E501
        """List all groups  # noqa: E501

        Returns the list of all groups in the system.  Requires `oz_groups_list` admin privilege.  ***Example cURL requests***  **List all groups in the system** ```bash  curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/groups ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_groups(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Groups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_groups_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_groups_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_groups_with_http_info(self, **kwargs):  # noqa: E501
        """List all groups  # noqa: E501

        Returns the list of all groups in the system.  Requires `oz_groups_list` admin privilege.  ***Example cURL requests***  **List all groups in the system** ```bash  curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/groups ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_groups_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Groups
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
                    " to method list_groups" % key
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
            '/groups', 'GET',
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

    def list_parent_groups(self, id, **kwargs):  # noqa: E501
        """List parent groups  # noqa: E501

        Returns the parent groups of a specific group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get parent groups** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/parents  {   \"groups\": [] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_parent_groups(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: Groups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_parent_groups_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_parent_groups_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_parent_groups_with_http_info(self, id, **kwargs):  # noqa: E501
        """List parent groups  # noqa: E501

        Returns the parent groups of a specific group.  This operation requires `group_view` privilege. For administrator who does not belong to this group `oz_groups_list_relationships` privilege is required.  ***Example cURL requests***  **Get parent groups** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/parents  {   \"groups\": [] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_parent_groups_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
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
                    " to method list_parent_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_parent_groups`")  # noqa: E501

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
            '/groups/{id}/parents', 'GET',
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

    def list_user_group_privileges(self, id, uid, **kwargs):  # noqa: E501
        """List user's group privileges  # noqa: E501

        Returns the list of user's (`{uid}`) privileges in a group (`{id}`).  This operation requires `group_view_privileges` privilege. For administrator who does not belong to this group `oz_groups_view_privileges` privilege is required.  ***Example cURL requests***  **List user's privileges in a group** ```bash curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/users/$USER_ID/privileges  {   \"privileges\": [     \"group_view\",     \"group_update\",     \"group_delete\",     \"group_view_privileges\",     \"group_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_group_privileges(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str uid: User Id. (required)
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_group_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_user_group_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def list_user_group_privileges_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """List user's group privileges  # noqa: E501

        Returns the list of user's (`{uid}`) privileges in a group (`{id}`).  This operation requires `group_view_privileges` privilege. For administrator who does not belong to this group `oz_groups_view_privileges` privilege is required.  ***Example cURL requests***  **List user's privileges in a group** ```bash curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/users/$USER_ID/privileges  {   \"privileges\": [     \"group_view\",     \"group_update\",     \"group_delete\",     \"group_view_privileges\",     \"group_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_group_privileges_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str uid: User Id. (required)
        :return: InlineResponse2005
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
                    " to method list_user_group_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_user_group_privileges`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `list_user_group_privileges`")  # noqa: E501

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
            '/groups/{id}/users/{uid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_group(self, body, id, **kwargs):  # noqa: E501
        """Modify group details  # noqa: E501

        Updates the details about a group.  This operation requires `group_update` privilege. For administrator who does not belong to this group `oz_groups_update` privilege is required.  ***Example cURL requests***  **Modify group name** ```bash curl -u admin:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"name\": \"new_group_name\"}' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_group(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupUpdateRequest body: Group parameters (required)
        :param str id: Group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_group_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_group_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def modify_group_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Modify group details  # noqa: E501

        Updates the details about a group.  This operation requires `group_update` privilege. For administrator who does not belong to this group `oz_groups_update` privilege is required.  ***Example cURL requests***  **Modify group name** ```bash curl -u admin:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"name\": \"new_group_name\"}' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_group_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupUpdateRequest body: Group parameters (required)
        :param str id: Group Id. (required)
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
                    " to method modify_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `modify_group`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `modify_group`")  # noqa: E501

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
            '/groups/{id}', 'PATCH',
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

    def remove_child_group(self, id, cid, **kwargs):  # noqa: E501
        """Remove child group  # noqa: E501

        Removes a specific child with {cid} from parent group with {id}.  This operation requires `group_remove_child` privilege. For administrator who does not belong to this group `oz_groups_remove_relationships` privilege is required.  ***Example cURL requests***  **Remove child group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/children/$CHILD_GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_child_group(id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str cid: Child group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_child_group_with_http_info(id, cid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_child_group_with_http_info(id, cid, **kwargs)  # noqa: E501
            return data

    def remove_child_group_with_http_info(self, id, cid, **kwargs):  # noqa: E501
        """Remove child group  # noqa: E501

        Removes a specific child with {cid} from parent group with {id}.  This operation requires `group_remove_child` privilege. For administrator who does not belong to this group `oz_groups_remove_relationships` privilege is required.  ***Example cURL requests***  **Remove child group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/children/$CHILD_GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_child_group_with_http_info(id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str cid: Child group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'cid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_child_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_child_group`")  # noqa: E501
        # verify the required parameter 'cid' is set
        if ('cid' not in params or
                params['cid'] is None):
            raise ValueError("Missing the required parameter `cid` when calling `remove_child_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'cid' in params:
            path_params['cid'] = params['cid']  # noqa: E501

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
            '/groups/{id}/children/{cid}', 'DELETE',
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

    def remove_group(self, id, **kwargs):  # noqa: E501
        """Remove group  # noqa: E501

        Removes a specific group.  This operation requires `group_delete` privilege. For administrator who does not belong to this group `oz_groups_delete` privilege is required.  ***Example cURL requests***  **Remove group** ```bash curl -u admin:password -X DELETE  \\ https://$ZONE_HOST/api/v3/onezone/user/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_group(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_group_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_group_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def remove_group_with_http_info(self, id, **kwargs):  # noqa: E501
        """Remove group  # noqa: E501

        Removes a specific group.  This operation requires `group_delete` privilege. For administrator who does not belong to this group `oz_groups_delete` privilege is required.  ***Example cURL requests***  **Remove group** ```bash curl -u admin:password -X DELETE  \\ https://$ZONE_HOST/api/v3/onezone/user/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_group_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
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
                    " to method remove_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_group`")  # noqa: E501

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
            '/groups/{id}', 'DELETE',
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

    def remove_group_admin_privileges(self, id, **kwargs):  # noqa: E501
        """Remove group's admin privileges  # noqa: E501

        Removes all group's (`{id}`) admin privileges in Onezone.  This operation requires `oz_set_privileges` admin privilege.  ***Example cURL requests***  **Remove all group's admin privileges in Onezone** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_group_admin_privileges(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_group_admin_privileges_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_group_admin_privileges_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def remove_group_admin_privileges_with_http_info(self, id, **kwargs):  # noqa: E501
        """Remove group's admin privileges  # noqa: E501

        Removes all group's (`{id}`) admin privileges in Onezone.  This operation requires `oz_set_privileges` admin privilege.  ***Example cURL requests***  **Remove all group's admin privileges in Onezone** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_group_admin_privileges_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
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
                    " to method remove_group_admin_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_group_admin_privileges`")  # noqa: E501

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
            '/groups/{id}/privileges', 'DELETE',
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

    def remove_group_from_harvester(self, id, hid, **kwargs):  # noqa: E501
        """Remove group from harvester  # noqa: E501

        Removes the group {id} from harvester {hid} (the group will no longer have access to harvester).  This operation requires `group_leave_harvester` privilege. For administrator who does not belong to this group `oz_groups_remove_relationships` and `oz_harvesters_remove_relationships` privileges are required.  ***Example cURL requests***  **Remove harvester from group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/harvesters/$HARVESTER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_group_from_harvester(id, hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str hid: Harvester Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_group_from_harvester_with_http_info(id, hid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_group_from_harvester_with_http_info(id, hid, **kwargs)  # noqa: E501
            return data

    def remove_group_from_harvester_with_http_info(self, id, hid, **kwargs):  # noqa: E501
        """Remove group from harvester  # noqa: E501

        Removes the group {id} from harvester {hid} (the group will no longer have access to harvester).  This operation requires `group_leave_harvester` privilege. For administrator who does not belong to this group `oz_groups_remove_relationships` and `oz_harvesters_remove_relationships` privileges are required.  ***Example cURL requests***  **Remove harvester from group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/harvesters/$HARVESTER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_group_from_harvester_with_http_info(id, hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str hid: Harvester Id. (required)
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
                    " to method remove_group_from_harvester" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_group_from_harvester`")  # noqa: E501
        # verify the required parameter 'hid' is set
        if ('hid' not in params or
                params['hid'] is None):
            raise ValueError("Missing the required parameter `hid` when calling `remove_group_from_harvester`")  # noqa: E501

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
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{id}/harvesters/{hid}', 'DELETE',
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

    def remove_group_from_space(self, id, sid, **kwargs):  # noqa: E501
        """Remove group from space  # noqa: E501

        Removes the group {id} from space {sid} (the group will no longer have access to space).  This operation requires `group_leave_space` privilege. For administrator who does not belong to this group `oz_groups_remove_relationships` and `oz_spaces_remove_relationships` privileges are required.  ***Example cURL requests***  **Remove space from group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/spaces/$SPACE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_group_from_space(id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str sid: Space Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_group_from_space_with_http_info(id, sid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_group_from_space_with_http_info(id, sid, **kwargs)  # noqa: E501
            return data

    def remove_group_from_space_with_http_info(self, id, sid, **kwargs):  # noqa: E501
        """Remove group from space  # noqa: E501

        Removes the group {id} from space {sid} (the group will no longer have access to space).  This operation requires `group_leave_space` privilege. For administrator who does not belong to this group `oz_groups_remove_relationships` and `oz_spaces_remove_relationships` privileges are required.  ***Example cURL requests***  **Remove space from group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/spaces/$SPACE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_group_from_space_with_http_info(id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str sid: Space Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'sid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_group_from_space" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_group_from_space`")  # noqa: E501
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `remove_group_from_space`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'sid' in params:
            path_params['sid'] = params['sid']  # noqa: E501

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
            '/groups/{id}/spaces/{sid}', 'DELETE',
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

    def remove_group_user(self, id, uid, **kwargs):  # noqa: E501
        """Remove user from group  # noqa: E501

        Removes the user {uid} from a group {id} (the user will no longer have access to spaces accessible to the group).  This operation requires `group_remove_user` privilege. For administrator who does not belong to this group `oz_groups_remove_relationships` and `oz_users_remove_relationships` privileges are required.  ***Example cURL requests***  **Remove user from group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_group_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str uid: User Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_group_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_group_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def remove_group_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Remove user from group  # noqa: E501

        Removes the user {uid} from a group {id} (the user will no longer have access to spaces accessible to the group).  This operation requires `group_remove_user` privilege. For administrator who does not belong to this group `oz_groups_remove_relationships` and `oz_users_remove_relationships` privileges are required.  ***Example cURL requests***  **Remove user from group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_group_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Group Id. (required)
        :param str uid: User Id. (required)
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
                    " to method remove_group_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_group_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `remove_group_user`")  # noqa: E501

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
            '/groups/{id}/users/{uid}', 'DELETE',
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

    def update_child_group_privileges(self, body, id, cid, **kwargs):  # noqa: E501
        """Update child's group privileges  # noqa: E501

        Updates child group's (`{cid}`) privileges in a group (`{id}`).  This operation requires `group_set_privileges` privilege. For administrator who does not belong to this group `oz_groups_set_privileges` privilege is required.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update child group's privileges in a group** ```bash curl -u username:password -H \"Content-type: application/json\" -X PATCH \\ -d '{\"grant\": [\"group_view\", \"group_update\"], \"revoke\": [\"group_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/children/$CHILD_GROUP_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_child_group_privileges(body, id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupPrivilegesUpdate body: Group privileges update request. (required)
        :param str id: Group Id. (required)
        :param str cid: Child group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_child_group_privileges_with_http_info(body, id, cid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_child_group_privileges_with_http_info(body, id, cid, **kwargs)  # noqa: E501
            return data

    def update_child_group_privileges_with_http_info(self, body, id, cid, **kwargs):  # noqa: E501
        """Update child's group privileges  # noqa: E501

        Updates child group's (`{cid}`) privileges in a group (`{id}`).  This operation requires `group_set_privileges` privilege. For administrator who does not belong to this group `oz_groups_set_privileges` privilege is required.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update child group's privileges in a group** ```bash curl -u username:password -H \"Content-type: application/json\" -X PATCH \\ -d '{\"grant\": [\"group_view\", \"group_update\"], \"revoke\": [\"group_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/children/$CHILD_GROUP_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_child_group_privileges_with_http_info(body, id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupPrivilegesUpdate body: Group privileges update request. (required)
        :param str id: Group Id. (required)
        :param str cid: Child group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id', 'cid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_child_group_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_child_group_privileges`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_child_group_privileges`")  # noqa: E501
        # verify the required parameter 'cid' is set
        if ('cid' not in params or
                params['cid'] is None):
            raise ValueError("Missing the required parameter `cid` when calling `update_child_group_privileges`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'cid' in params:
            path_params['cid'] = params['cid']  # noqa: E501

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
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{id}/children/{cid}/privileges', 'PATCH',
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

    def update_group_admin_privileges(self, body, id, **kwargs):  # noqa: E501
        """Update group's admin privileges  # noqa: E501

        Updates group's (`{id}`) admin privileges in Onezone.  This operation requires `oz_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update group's admin privileges in Onezone** ```bash curl -H \"Content-type: application/json\" -X PATCH \\ -d '{\"grant\": [\"oz_spaces_list\"], \"revoke\": [\"oz_groups_update\"]}' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_group_admin_privileges(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AdminPrivilegesUpdate body: admin privileges update request. (required)
        :param str id: Group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_group_admin_privileges_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_group_admin_privileges_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def update_group_admin_privileges_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Update group's admin privileges  # noqa: E501

        Updates group's (`{id}`) admin privileges in Onezone.  This operation requires `oz_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update group's admin privileges in Onezone** ```bash curl -H \"Content-type: application/json\" -X PATCH \\ -d '{\"grant\": [\"oz_spaces_list\"], \"revoke\": [\"oz_groups_update\"]}' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_group_admin_privileges_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AdminPrivilegesUpdate body: admin privileges update request. (required)
        :param str id: Group Id. (required)
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
                    " to method update_group_admin_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_group_admin_privileges`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_group_admin_privileges`")  # noqa: E501

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
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{id}/privileges', 'PATCH',
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

    def update_user_group_privileges(self, body, id, uid, **kwargs):  # noqa: E501
        """Update user's group privileges  # noqa: E501

        Updates user's (`{uid}`) privileges in a group (`{id}`).  This operation requires `group_set_privileges` privilege. For administrator who does not belong to this group `oz_groups_set_privileges` privilege is required.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update user's privileges in a group** ```bash curl -H \"Content-type: application/json\" -X PATCH \\ -d '{\"grant\": [\"group_view\", \"group_update\"], \"revoke\": [\"group_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/users/$USER_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_group_privileges(body, id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupPrivilegesUpdate body: Group privileges update request. (required)
        :param str id: Group Id. (required)
        :param str uid: User Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_user_group_privileges_with_http_info(body, id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_user_group_privileges_with_http_info(body, id, uid, **kwargs)  # noqa: E501
            return data

    def update_user_group_privileges_with_http_info(self, body, id, uid, **kwargs):  # noqa: E501
        """Update user's group privileges  # noqa: E501

        Updates user's (`{uid}`) privileges in a group (`{id}`).  This operation requires `group_set_privileges` privilege. For administrator who does not belong to this group `oz_groups_set_privileges` privilege is required.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update user's privileges in a group** ```bash curl -H \"Content-type: application/json\" -X PATCH \\ -d '{\"grant\": [\"group_view\", \"group_update\"], \"revoke\": [\"group_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/groups/$GROUP_ID/users/$USER_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_group_privileges_with_http_info(body, id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupPrivilegesUpdate body: Group privileges update request. (required)
        :param str id: Group Id. (required)
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
                    " to method update_user_group_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_user_group_privileges`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_user_group_privileges`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `update_user_group_privileges`")  # noqa: E501

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
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{id}/users/{uid}/privileges', 'PATCH',
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
