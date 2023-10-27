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


class SpaceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_group_to_space(self, id, gid, **kwargs):  # noqa: E501
        """Add group to space  # noqa: E501

        Adds group {gid} as member of space {id}. Optional privileges can be passed in the request body, otherwise default privileges will be set for the group in this space.  This operation requires `space_add_group` privilege in the space and `group_add_space` privilege in the group. If `privileges` are specified in the request, `space_set_privileges` privilege is also required.  For administrator who does not belong to the group / space, `oz_groups_add_relationships` and `oz_spaces_add_relationships` privileges are required, and `oz_spaces_set_privileges` if `privileges` are specified in the request.  ***Example cURL requests***  **Add group to space** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\  https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_group_to_space(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str gid: Group Id. (required)
        :param GroupsGidBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_group_to_space_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.add_group_to_space_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def add_group_to_space_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Add group to space  # noqa: E501

        Adds group {gid} as member of space {id}. Optional privileges can be passed in the request body, otherwise default privileges will be set for the group in this space.  This operation requires `space_add_group` privilege in the space and `group_add_space` privilege in the group. If `privileges` are specified in the request, `space_set_privileges` privilege is also required.  For administrator who does not belong to the group / space, `oz_groups_add_relationships` and `oz_spaces_add_relationships` privileges are required, and `oz_spaces_set_privileges` if `privileges` are specified in the request.  ***Example cURL requests***  **Add group to space** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\  https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_group_to_space_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str gid: Group Id. (required)
        :param GroupsGidBody body:
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
                    " to method add_group_to_space" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_group_to_space`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `add_group_to_space`")  # noqa: E501

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
            '/spaces/{id}/groups/{gid}', 'PUT',
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

    def add_space_owner(self, id, uid, **kwargs):  # noqa: E501
        """Add space owner  # noqa: E501

        Adds user `{uid}` as an owner of space `{id}`. Ownership can only be granted to effective members of the space - if the desired user is not a member, they have to be added to the space first. If the new owner is only an indirect member (via a group), he is automatically added as a direct member when granted ownership.  Space owners are members of the space (users) that have absolute power regarding the space API and files (analogical to \"root\", but in the scope of one space). Being an owner means that user privileges are essentially ignored and all API operations are allowed.  This operation requires any of the following authentication: * as user who is currently an owner of the space (`{id}`), * as user who has `oz_spaces_set_privileges` admin privilege.  ***Example cURL requests***  **Add space space owner** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/owners/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_space_owner(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str uid: User Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_space_owner_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.add_space_owner_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def add_space_owner_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Add space owner  # noqa: E501

        Adds user `{uid}` as an owner of space `{id}`. Ownership can only be granted to effective members of the space - if the desired user is not a member, they have to be added to the space first. If the new owner is only an indirect member (via a group), he is automatically added as a direct member when granted ownership.  Space owners are members of the space (users) that have absolute power regarding the space API and files (analogical to \"root\", but in the scope of one space). Being an owner means that user privileges are essentially ignored and all API operations are allowed.  This operation requires any of the following authentication: * as user who is currently an owner of the space (`{id}`), * as user who has `oz_spaces_set_privileges` admin privilege.  ***Example cURL requests***  **Add space space owner** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/owners/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_space_owner_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
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
                    " to method add_space_owner" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_space_owner`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `add_space_owner`")  # noqa: E501

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
            '/spaces/{id}/owners/{uid}', 'PUT',
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

    def add_space_user(self, id, uid, **kwargs):  # noqa: E501
        """Add user to space  # noqa: E501

        Adds user {uid} as member of space {id}. Optional privileges can be passed in the request body, otherwise default privileges will be set for the user in this space.  This operation can only be invoked by the user {uid} to add himself to the space (if he is not a member already) and requires `space_add_user` privilege in the space. If `privileges` are specified in the request, `space_set_privileges` privilege is also required.  Administrators having the `oz_spaces_add_relationships` and `oz_users_add_relationships` admin privileges can add any user to any space, though `oz_spaces_set_privileges` privilege is required if `privileges` are specified in the request.  ***Example cURL requests***  **Add user to space** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_space_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str uid: User Id. (required)
        :param UsersUidBody1 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_space_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.add_space_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def add_space_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Add user to space  # noqa: E501

        Adds user {uid} as member of space {id}. Optional privileges can be passed in the request body, otherwise default privileges will be set for the user in this space.  This operation can only be invoked by the user {uid} to add himself to the space (if he is not a member already) and requires `space_add_user` privilege in the space. If `privileges` are specified in the request, `space_set_privileges` privilege is also required.  Administrators having the `oz_spaces_add_relationships` and `oz_users_add_relationships` admin privileges can add any user to any space, though `oz_spaces_set_privileges` privilege is required if `privileges` are specified in the request.  ***Example cURL requests***  **Add user to space** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_space_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str uid: User Id. (required)
        :param UsersUidBody1 body:
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
                    " to method add_space_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_space_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `add_space_user`")  # noqa: E501

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
            '/spaces/{id}/users/{uid}', 'PUT',
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

    def cease_support_by_provider(self, id, pid, **kwargs):  # noqa: E501
        """Ceases space support by provider  # noqa: E501

        Ceases the space's support from given provider. WARNING: this will cause irreversible data loss if the data located in given space on given provider is not replicated beforehand.  This operation requires `space_remove_support` privilege or `oz_spaces_remove_relationships` admin privilege.  ***Example cURL requests***  **Remove space support** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/providers/$PROVIDER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cease_support_by_provider(id, pid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str pid: Provider Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cease_support_by_provider_with_http_info(id, pid, **kwargs)  # noqa: E501
        else:
            (data) = self.cease_support_by_provider_with_http_info(id, pid, **kwargs)  # noqa: E501
            return data

    def cease_support_by_provider_with_http_info(self, id, pid, **kwargs):  # noqa: E501
        """Ceases space support by provider  # noqa: E501

        Ceases the space's support from given provider. WARNING: this will cause irreversible data loss if the data located in given space on given provider is not replicated beforehand.  This operation requires `space_remove_support` privilege or `oz_spaces_remove_relationships` admin privilege.  ***Example cURL requests***  **Remove space support** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/providers/$PROVIDER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cease_support_by_provider_with_http_info(id, pid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str pid: Provider Id. (required)
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
                    " to method cease_support_by_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `cease_support_by_provider`")  # noqa: E501
        # verify the required parameter 'pid' is set
        if ('pid' not in params or
                params['pid'] is None):
            raise ValueError("Missing the required parameter `pid` when calling `cease_support_by_provider`")  # noqa: E501

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
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/spaces/{id}/providers/{pid}', 'DELETE',
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

    def create_space(self, **kwargs):  # noqa: E501
        """Create new space  # noqa: E501

        Creates new space.  This operation requires `oz_spaces_create` admin privilege.  See also:   [Create a new space for the current user](#operation/create_user_space)   [Create a new space for given group](#operation/create_space_for_group)    ***Example cURL requests***  **Create new space** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"name\" : \"new_space\" }' \\ https://$ZONE_HOST/api/v3/onezone/spaces ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_space(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SpacesBody body: Space creation data.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_space_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_space_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_space_with_http_info(self, **kwargs):  # noqa: E501
        """Create new space  # noqa: E501

        Creates new space.  This operation requires `oz_spaces_create` admin privilege.  See also:   [Create a new space for the current user](#operation/create_user_space)   [Create a new space for given group](#operation/create_space_for_group)    ***Example cURL requests***  **Create new space** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"name\" : \"new_space\" }' \\ https://$ZONE_HOST/api/v3/onezone/spaces ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_space_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SpacesBody body: Space creation data.
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
                    " to method create_space" % key
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
            '/spaces', 'POST',
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

    def create_space_group(self, body, id, **kwargs):  # noqa: E501
        """Create group in space  # noqa: E501

        Creates a new group belonging to the space of {id}.  This operation requires `space_add_group` privilege. For administrator who does not belong to this group `oz_spaces_add_relationships` and `oz_groups_create` privileges are required.  ***Example cURL requests***  **Create group in space** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_space_group(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupCreateRequest body: Group properties. (required)
        :param str id: Space Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_space_group_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_space_group_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def create_space_group_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Create group in space  # noqa: E501

        Creates a new group belonging to the space of {id}.  This operation requires `space_add_group` privilege. For administrator who does not belong to this group `oz_spaces_add_relationships` and `oz_groups_create` privileges are required.  ***Example cURL requests***  **Create group in space** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_space_group_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupCreateRequest body: Group properties. (required)
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
                    " to method create_space_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_space_group`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_space_group`")  # noqa: E501

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
            '/spaces/{id}/groups', 'POST',
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

    def create_space_group_token(self, id, **kwargs):  # noqa: E501
        """Create space invite token for group  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user).  Creates a token allowing to add a group to a specific space.  This operation requires `space_add_group` privilege or `oz_spaces_add_relationships` admin privilege.  ***Example cURL requests***  **Create space invitation token for group** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups/token  {   \"token\": \"MDAxNmxvY0cGUgKWsjcpnrLE00RtOd2F00cGUgKWsjcpnrLE00RtOdhmnQycSICwMsugo\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_space_group_token(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :return: SpaceInviteToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_space_group_token_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_space_group_token_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def create_space_group_token_with_http_info(self, id, **kwargs):  # noqa: E501
        """Create space invite token for group  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user).  Creates a token allowing to add a group to a specific space.  This operation requires `space_add_group` privilege or `oz_spaces_add_relationships` admin privilege.  ***Example cURL requests***  **Create space invitation token for group** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups/token  {   \"token\": \"MDAxNmxvY0cGUgKWsjcpnrLE00RtOd2F00cGUgKWsjcpnrLE00RtOdhmnQycSICwMsugo\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_space_group_token_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :return: SpaceInviteToken
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
                    " to method create_space_group_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_space_group_token`")  # noqa: E501

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
            '/spaces/{id}/groups/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SpaceInviteToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_space_support_token(self, id, **kwargs):  # noqa: E501
        """Create space support token  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user).  Creates a token which can be submitted to a selected provider in order to add storage support for the space.  This operation requires `space_add_support` privilege or `oz_spaces_add_relationships` admin privilege.  ***Example cURL requests***  **Create space support token** ```bash curl -u admin:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/providers/token  {   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaWVyIHZjUGlIcGkweGZta1ZOdEp00eUNINVNvR2001Wl\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_space_support_token(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :return: SpaceSupportToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_space_support_token_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_space_support_token_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def create_space_support_token_with_http_info(self, id, **kwargs):  # noqa: E501
        """Create space support token  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user).  Creates a token which can be submitted to a selected provider in order to add storage support for the space.  This operation requires `space_add_support` privilege or `oz_spaces_add_relationships` admin privilege.  ***Example cURL requests***  **Create space support token** ```bash curl -u admin:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/providers/token  {   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaWVyIHZjUGlIcGkweGZta1ZOdEp00eUNINVNvR2001Wl\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_space_support_token_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :return: SpaceSupportToken
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
                    " to method create_space_support_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_space_support_token`")  # noqa: E501

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
            '/spaces/{id}/providers/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SpaceSupportToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_space_user_invite_token(self, id, **kwargs):  # noqa: E501
        """Create space user invite token  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token allowing new user to join a space.  This operation requires `space_add_user` privilege. For administrators who do not have to be members of this space, `oz_spaces_add_relationships` privilege is required.  ***Example cURL requests***  **Create space user invite token** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/users/token  {   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaWVyIG00zcEJ2UDVuOHhkQUNhdk9hbTlyNnIwNldPSzVhc\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_space_user_invite_token(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :return: SpaceInviteToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_space_user_invite_token_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_space_user_invite_token_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def create_space_user_invite_token_with_http_info(self, id, **kwargs):  # noqa: E501
        """Create space user invite token  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token allowing new user to join a space.  This operation requires `space_add_user` privilege. For administrators who do not have to be members of this space, `oz_spaces_add_relationships` privilege is required.  ***Example cURL requests***  **Create space user invite token** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/users/token  {   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaWVyIG00zcEJ2UDVuOHhkQUNhdk9hbTlyNnIwNldPSzVhc\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_space_user_invite_token_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :return: SpaceInviteToken
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
                    " to method create_space_user_invite_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_space_user_invite_token`")  # noqa: E501

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
            '/spaces/{id}/users/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SpaceInviteToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_effective_group_space_membership_intermediaries(self, id, gid, **kwargs):  # noqa: E501
        """Get effective group's space membership intermediaries  # noqa: E501

        Returns the effective group's (`{gid}`) space membership intermediaries - entities from which the group inherits access to the space (`{id}`). Special keyword `\"self\"` in entity id indicates that the group (`{gid}`) has a direct access to the space (`{id}`).  This operation requires any of the following authentication: * as user who is an effective member of the group (`{gid}`), * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space, * as user who has `oz_spaces_view` admin privilege.  ***Example cURL requests***  **Get effective group's space membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_groups/$GROUP_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"space\", \"id\": \"self\"}   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_group_space_membership_intermediaries(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str gid: Group Id. (required)
        :return: MembershipIntermediaries
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_group_space_membership_intermediaries_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_group_space_membership_intermediaries_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def get_effective_group_space_membership_intermediaries_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Get effective group's space membership intermediaries  # noqa: E501

        Returns the effective group's (`{gid}`) space membership intermediaries - entities from which the group inherits access to the space (`{id}`). Special keyword `\"self\"` in entity id indicates that the group (`{gid}`) has a direct access to the space (`{id}`).  This operation requires any of the following authentication: * as user who is an effective member of the group (`{gid}`), * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space, * as user who has `oz_spaces_view` admin privilege.  ***Example cURL requests***  **Get effective group's space membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_groups/$GROUP_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"space\", \"id\": \"self\"}   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_group_space_membership_intermediaries_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str gid: Group Id. (required)
        :return: MembershipIntermediaries
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
                    " to method get_effective_group_space_membership_intermediaries" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_group_space_membership_intermediaries`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `get_effective_group_space_membership_intermediaries`")  # noqa: E501

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
            '/spaces/{id}/effective_groups/{gid}/membership', 'GET',
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

    def get_effective_space_group(self, id, gid, **kwargs):  # noqa: E501
        """Get effective space group details  # noqa: E501

        Returns details about a specific effective group in a space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get effective space group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_groups/$GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_groupX\",   \"type\": \"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_space_group(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str gid: Group Id. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_space_group_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_space_group_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def get_effective_space_group_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Get effective space group details  # noqa: E501

        Returns details about a specific effective group in a space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get effective space group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_groups/$GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_groupX\",   \"type\": \"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_space_group_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str gid: Group Id. (required)
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
                    " to method get_effective_space_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_space_group`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `get_effective_space_group`")  # noqa: E501

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
            '/spaces/{id}/effective_groups/{gid}', 'GET',
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

    def get_effective_space_user(self, id, uid, **kwargs):  # noqa: E501
        """Get effective space user details  # noqa: E501

        Returns details about a specific effective user in a space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_users_view` admin privilege.  ***Example cURL requests***  **Get effective space user details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_users/$USER_ID  {   \"userId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"fullName\" : \"John Doe\",   \"username\" : \"jodoe\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_space_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str uid: User Id. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_space_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_space_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def get_effective_space_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Get effective space user details  # noqa: E501

        Returns details about a specific effective user in a space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_users_view` admin privilege.  ***Example cURL requests***  **Get effective space user details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_users/$USER_ID  {   \"userId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"fullName\" : \"John Doe\",   \"username\" : \"jodoe\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_space_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
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
                    " to method get_effective_space_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_space_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_effective_space_user`")  # noqa: E501

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
            '/spaces/{id}/effective_users/{uid}', 'GET',
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

    def get_effective_user_space_membership_intermediaries(self, id, uid, **kwargs):  # noqa: E501
        """Get effective user's space membership intermediaries  # noqa: E501

        Returns the effective user's (`{uid}`) space membership intermediaries - entities from which the user inherits access to the space (`{id}`). Special keyword `\"self\"` in entity id indicates that the user (`{uid}`) has a direct access to the space (`{id}`).  This operation requires any of the following authentication: * as user (`{uid}`) who is an effective member of the space (`{id}`), * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_view` admin privilege.  ***Example cURL requests***  **Get effective user's space membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_users/$USER_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"space\", \"id\": \"self\"}   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_user_space_membership_intermediaries(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str uid: User Id. (required)
        :return: MembershipIntermediaries
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_user_space_membership_intermediaries_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_user_space_membership_intermediaries_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def get_effective_user_space_membership_intermediaries_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Get effective user's space membership intermediaries  # noqa: E501

        Returns the effective user's (`{uid}`) space membership intermediaries - entities from which the user inherits access to the space (`{id}`). Special keyword `\"self\"` in entity id indicates that the user (`{uid}`) has a direct access to the space (`{id}`).  This operation requires any of the following authentication: * as user (`{uid}`) who is an effective member of the space (`{id}`), * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_view` admin privilege.  ***Example cURL requests***  **Get effective user's space membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_users/$USER_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"space\", \"id\": \"self\"}   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_user_space_membership_intermediaries_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
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
                    " to method get_effective_user_space_membership_intermediaries" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_user_space_membership_intermediaries`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_effective_user_space_membership_intermediaries`")  # noqa: E501

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
            '/spaces/{id}/effective_users/{uid}/membership', 'GET',
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

    def get_membership_requester_info(self, id, rid, **kwargs):  # noqa: E501
        """Get membership requester info  # noqa: E501

        Get requester info for a specific space membership request made via the Marketplace.  This operation requires privilege `space_manage_in_marketplace` or `oz_spaces_view` admin privilege.  ***Example cURL requests***  **Get space membership requester info** ```bash curl -u admin:password -H \"Content-type: application/json\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/marketplace/$SPACE_ID/request/$REQUEST_ID/requester_info  {   \"userId\": \"585110fde9d1a52c93f8eb22c0614e47\",   \"fullName\": \"Joe Joester\",   \"username\": \"JoJo\",   \"contactEmail\": user@example.com } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_membership_requester_info(id, rid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str rid: Space membership request Id. (required)
        :return: SpaceMembershipRequesterInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_membership_requester_info_with_http_info(id, rid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_membership_requester_info_with_http_info(id, rid, **kwargs)  # noqa: E501
            return data

    def get_membership_requester_info_with_http_info(self, id, rid, **kwargs):  # noqa: E501
        """Get membership requester info  # noqa: E501

        Get requester info for a specific space membership request made via the Marketplace.  This operation requires privilege `space_manage_in_marketplace` or `oz_spaces_view` admin privilege.  ***Example cURL requests***  **Get space membership requester info** ```bash curl -u admin:password -H \"Content-type: application/json\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/marketplace/$SPACE_ID/request/$REQUEST_ID/requester_info  {   \"userId\": \"585110fde9d1a52c93f8eb22c0614e47\",   \"fullName\": \"Joe Joester\",   \"username\": \"JoJo\",   \"contactEmail\": user@example.com } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_membership_requester_info_with_http_info(id, rid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str rid: Space membership request Id. (required)
        :return: SpaceMembershipRequesterInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'rid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_membership_requester_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_membership_requester_info`")  # noqa: E501
        # verify the required parameter 'rid' is set
        if ('rid' not in params or
                params['rid'] is None):
            raise ValueError("Missing the required parameter `rid` when calling `get_membership_requester_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'rid' in params:
            path_params['rid'] = params['rid']  # noqa: E501

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
            '/spaces/marketplace/{id}/request/{rid}/requester_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SpaceMembershipRequesterInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_space(self, id, **kwargs):  # noqa: E501
        """Get space details  # noqa: E501

        Returns the details about a specific space.  This operation requires any of the following authentication: * as user who is an effective member of the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_view` admin privilege.  ***Example cURL requests***  **Get space details** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID  {   \"spaceId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"My Private space\",   \"description\": \"My Private data\",   \"organizationName\": \"\",   \"tags\": [\"images\", \"sport\"],   \"advertisedInMarketplace\": false,   \"marketplaceContactEmail\": \"\",   \"providers\": {     \"296ebe3c20e9666dc489b647f8647f12\": 5368709120,     \"dcf12429647c204896eebe3b6f686967\": 14400000   },   \"supportParametersRegistry\": {     \"296ebe3c20e9666dc489b647f8647f12\": {       \"accountingEnabled\": false,       \"dirStatsServiceEnabled\": true,       \"dirStatsServiceStatus\": \"enabled\"     },     \"dcf12429647c204896eebe3b6f686967\": {       \"accountingEnabled\": false,       \"dirStatsServiceEnabled\": false,       \"dirStatsServiceStatus\": \"stopping\"     }   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebfc1a770c3\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :return: Space
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_space_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_space_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_space_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get space details  # noqa: E501

        Returns the details about a specific space.  This operation requires any of the following authentication: * as user who is an effective member of the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_view` admin privilege.  ***Example cURL requests***  **Get space details** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID  {   \"spaceId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"My Private space\",   \"description\": \"My Private data\",   \"organizationName\": \"\",   \"tags\": [\"images\", \"sport\"],   \"advertisedInMarketplace\": false,   \"marketplaceContactEmail\": \"\",   \"providers\": {     \"296ebe3c20e9666dc489b647f8647f12\": 5368709120,     \"dcf12429647c204896eebe3b6f686967\": 14400000   },   \"supportParametersRegistry\": {     \"296ebe3c20e9666dc489b647f8647f12\": {       \"accountingEnabled\": false,       \"dirStatsServiceEnabled\": true,       \"dirStatsServiceStatus\": \"enabled\"     },     \"dcf12429647c204896eebe3b6f686967\": {       \"accountingEnabled\": false,       \"dirStatsServiceEnabled\": false,       \"dirStatsServiceStatus\": \"stopping\"     }   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebfc1a770c3\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :return: Space
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
                    " to method get_space" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_space`")  # noqa: E501

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
            '/spaces/{id}', 'GET',
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

    def get_space_data_in_marketplace(self, id, **kwargs):  # noqa: E501
        """Get space details in the Marketplace  # noqa: E501

        Returns the Marketplace related details about a specific space.  This operation can be performed by any user, but only for spaces advertised in the Marketplace.  ***Example cURL requests***  **Get space details in the Marketplace** ```bash curl -H \"x-auth-token: $TOKEN\" -H \\ https://$ZONE_HOST/api/v3/onezone/spaces/marketplace/$SPACE_ID  {   \"name\": \"Meteo dataset\",   \"index\": \"Meteo dataset@2c0160248ba9a66f45da751ca459535a\",   \"description\": \"This dataset contains meteorological data for major Polish cities in years 2012-2014.\",   \"organizationName\": \"ACK Cyfronet AGH\",   \"tags\": [\"archival\", \"big-data\", \"open-data\", \"environment\"],   \"providerNames\": [\"krakow\", \"paris\"],   \"totalSupportSize\": 30500000000,   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_data_in_marketplace(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :return: SpaceMarketplaceData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_space_data_in_marketplace_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_space_data_in_marketplace_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_space_data_in_marketplace_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get space details in the Marketplace  # noqa: E501

        Returns the Marketplace related details about a specific space.  This operation can be performed by any user, but only for spaces advertised in the Marketplace.  ***Example cURL requests***  **Get space details in the Marketplace** ```bash curl -H \"x-auth-token: $TOKEN\" -H \\ https://$ZONE_HOST/api/v3/onezone/spaces/marketplace/$SPACE_ID  {   \"name\": \"Meteo dataset\",   \"index\": \"Meteo dataset@2c0160248ba9a66f45da751ca459535a\",   \"description\": \"This dataset contains meteorological data for major Polish cities in years 2012-2014.\",   \"organizationName\": \"ACK Cyfronet AGH\",   \"tags\": [\"archival\", \"big-data\", \"open-data\", \"environment\"],   \"providerNames\": [\"krakow\", \"paris\"],   \"totalSupportSize\": 30500000000,   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_data_in_marketplace_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :return: SpaceMarketplaceData
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
                    " to method get_space_data_in_marketplace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_space_data_in_marketplace`")  # noqa: E501

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
            '/spaces/marketplace/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SpaceMarketplaceData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_space_group(self, id, gid, **kwargs):  # noqa: E501
        """Get space's group details  # noqa: E501

        Returns details about a specific group in a space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get space group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups/$GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_groupX\",   \"type\": \"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_group(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str gid: Group Id. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_space_group_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_space_group_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def get_space_group_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Get space's group details  # noqa: E501

        Returns details about a specific group in a space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get space group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups/$GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_groupX\",   \"type\": \"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_group_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str gid: Group Id. (required)
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
                    " to method get_space_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_space_group`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `get_space_group`")  # noqa: E501

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
            '/spaces/{id}/groups/{gid}', 'GET',
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

    def get_space_harvester(self, id, hid, **kwargs):  # noqa: E501
        """Get harvester details  # noqa: E501

        Returns details about a specific harvester in a space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_harvesters_view` admin privilege.  ***Example cURL requests***  **Get space harvester details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/harvesters/$HARVESTER_ID  {   \"harvesterId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_harvester1\",   \"public\" : true,   \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\",   \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_harvester(id, hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str hid: Harvester Id. (required)
        :return: Harvester
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_space_harvester_with_http_info(id, hid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_space_harvester_with_http_info(id, hid, **kwargs)  # noqa: E501
            return data

    def get_space_harvester_with_http_info(self, id, hid, **kwargs):  # noqa: E501
        """Get harvester details  # noqa: E501

        Returns details about a specific harvester in a space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_harvesters_view` admin privilege.  ***Example cURL requests***  **Get space harvester details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/harvesters/$HARVESTER_ID  {   \"harvesterId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_harvester1\",   \"public\" : true,   \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\",   \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_harvester_with_http_info(id, hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
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
                    " to method get_space_harvester" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_space_harvester`")  # noqa: E501
        # verify the required parameter 'hid' is set
        if ('hid' not in params or
                params['hid'] is None):
            raise ValueError("Missing the required parameter `hid` when calling `get_space_harvester`")  # noqa: E501

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
            '/spaces/{id}/harvesters/{hid}', 'GET',
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

    def get_space_provider(self, id, pid, **kwargs):  # noqa: E501
        """Get space provider details  # noqa: E501

        Returns details about a specific provider supporting the space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_providers_view` admin privilege.  ***Example cURL requests***  **Get space provider details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/providers/$PROVIDER_ID  {   \"providerId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"name\": \"Example provider\",   \"domain\": \"provider1.example.com\",   \"latitude\": 50.0647,   \"longitude\": 19.945,   \"clusterId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"online\": true,   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_provider(id, pid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str pid: Provider Id. (required)
        :return: ProviderDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_space_provider_with_http_info(id, pid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_space_provider_with_http_info(id, pid, **kwargs)  # noqa: E501
            return data

    def get_space_provider_with_http_info(self, id, pid, **kwargs):  # noqa: E501
        """Get space provider details  # noqa: E501

        Returns details about a specific provider supporting the space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_providers_view` admin privilege.  ***Example cURL requests***  **Get space provider details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/providers/$PROVIDER_ID  {   \"providerId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"name\": \"Example provider\",   \"domain\": \"provider1.example.com\",   \"latitude\": 50.0647,   \"longitude\": 19.945,   \"clusterId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"online\": true,   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_provider_with_http_info(id, pid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str pid: Provider Id. (required)
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
                    " to method get_space_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_space_provider`")  # noqa: E501
        # verify the required parameter 'pid' is set
        if ('pid' not in params or
                params['pid'] is None):
            raise ValueError("Missing the required parameter `pid` when calling `get_space_provider`")  # noqa: E501

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
            '/spaces/{id}/providers/{pid}', 'GET',
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

    def get_space_share(self, id, sid, **kwargs):  # noqa: E501
        """Get space share  # noqa: E501

        Returns the details about a share from specific space.  NOTE: Only Oneprovider API supports creating / deleting shares and is preferred for all share operations. Onezone API is limited to retrieving and modifying share details.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_shares_view` admin privilege.  ***Example cURL requests***  **Get space share** ```bash curl -u username:password -H \"Content-type: application/json\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/shares/$SHARE_ID  {   \"shareId\": \"1f4b762b1380946e73aeca574c77f14c\",   \"name\": \"Experiment XYZ\",   \"description\": \"# Experiment XYZ\\nThis collection contains results from Experiment XYZ.\",   \"publicUrl\": \"https://example.com/shares/1f4b762b1380946e73aeca574c77f14c\",   \"publicRestUrl\": \"https://example.com/api/v3/onezone/shares/1f4b762b1380946e73aeca574c77f14c/public\",   \"fileType\": \"dir\",   \"rootFileId\": \"00000000006CB663736861726547756964233339643236366165646365\\   6266666164353939663761373734313235363166342336656331613534313362366634653\\   2623031613563383561386664373937653223316634623736326231333830393436653733\\   6165636135373463373766313463\",   \"spaceId\": \"6ec1a5413b6f4e2b01a5c85a8fd797e2\",   \"handleId\" \"70570c0ebcd081835ca29560708fd98f\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_share(id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str sid: Share Id. (required)
        :return: Share
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_space_share_with_http_info(id, sid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_space_share_with_http_info(id, sid, **kwargs)  # noqa: E501
            return data

    def get_space_share_with_http_info(self, id, sid, **kwargs):  # noqa: E501
        """Get space share  # noqa: E501

        Returns the details about a share from specific space.  NOTE: Only Oneprovider API supports creating / deleting shares and is preferred for all share operations. Onezone API is limited to retrieving and modifying share details.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_shares_view` admin privilege.  ***Example cURL requests***  **Get space share** ```bash curl -u username:password -H \"Content-type: application/json\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/shares/$SHARE_ID  {   \"shareId\": \"1f4b762b1380946e73aeca574c77f14c\",   \"name\": \"Experiment XYZ\",   \"description\": \"# Experiment XYZ\\nThis collection contains results from Experiment XYZ.\",   \"publicUrl\": \"https://example.com/shares/1f4b762b1380946e73aeca574c77f14c\",   \"publicRestUrl\": \"https://example.com/api/v3/onezone/shares/1f4b762b1380946e73aeca574c77f14c/public\",   \"fileType\": \"dir\",   \"rootFileId\": \"00000000006CB663736861726547756964233339643236366165646365\\   6266666164353939663761373734313235363166342336656331613534313362366634653\\   2623031613563383561386664373937653223316634623736326231333830393436653733\\   6165636135373463373766313463\",   \"spaceId\": \"6ec1a5413b6f4e2b01a5c85a8fd797e2\",   \"handleId\" \"70570c0ebcd081835ca29560708fd98f\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_share_with_http_info(id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str sid: Share Id. (required)
        :return: Share
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
                    " to method get_space_share" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_space_share`")  # noqa: E501
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `get_space_share`")  # noqa: E501

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
            '/spaces/{id}/shares/{sid}', 'GET',
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

    def get_space_user(self, id, uid, **kwargs):  # noqa: E501
        """Get space user details  # noqa: E501

        Returns basic information about a specific user in a space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_users_view` admin privilege.  ***Example cURL requests***  **Get space user data** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str uid: User Id. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_space_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_space_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def get_space_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Get space user details  # noqa: E501

        Returns basic information about a specific user in a space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_users_view` admin privilege.  ***Example cURL requests***  **Get space user data** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
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
                    " to method get_space_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_space_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_space_user`")  # noqa: E501

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
            '/spaces/{id}/users/{uid}', 'GET',
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

    def list_effective_group_space_privileges(self, id, gid, **kwargs):  # noqa: E501
        """List effective group's space privileges  # noqa: E501

        Returns the list of effective group's (`{gid}`) privileges in a space (`{id}`).  Effective privileges are a sum of group's privileges and privileges inherited from its parent group memberships.  This operation requires any of the following authentication: * as user who has `space_view_privileges` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_groups_view_privileges` admin privilege.  ***Example cURL requests***  **List effective groups's privileges in a space** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_groups/$GROUP_ID/privileges  {   \"privileges\": [     \"space_view\",     \"space_update\",     \"space_delete\",     \"space_view_privileges\",     \"space_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_space_privileges(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str gid: Group Id. (required)
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_group_space_privileges_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_group_space_privileges_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def list_effective_group_space_privileges_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """List effective group's space privileges  # noqa: E501

        Returns the list of effective group's (`{gid}`) privileges in a space (`{id}`).  Effective privileges are a sum of group's privileges and privileges inherited from its parent group memberships.  This operation requires any of the following authentication: * as user who has `space_view_privileges` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_groups_view_privileges` admin privilege.  ***Example cURL requests***  **List effective groups's privileges in a space** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_groups/$GROUP_ID/privileges  {   \"privileges\": [     \"space_view\",     \"space_update\",     \"space_delete\",     \"space_view_privileges\",     \"space_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_space_privileges_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str gid: Group Id. (required)
        :return: InlineResponse2009
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
                    " to method list_effective_group_space_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_group_space_privileges`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `list_effective_group_space_privileges`")  # noqa: E501

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
            '/spaces/{id}/effective_groups/{gid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2009',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_effective_space_groups(self, id, **kwargs):  # noqa: E501
        """List effective space groups  # noqa: E501

        Returns the list of effective groups belonging to a specific space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_list_relationships` admin privilege.  ***Example cURL requests***  **Get space effective groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_groups  {   \"groups\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_space_groups(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :return: Groups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_space_groups_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_space_groups_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_effective_space_groups_with_http_info(self, id, **kwargs):  # noqa: E501
        """List effective space groups  # noqa: E501

        Returns the list of effective groups belonging to a specific space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_list_relationships` admin privilege.  ***Example cURL requests***  **Get space effective groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_groups  {   \"groups\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_space_groups_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
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
                    " to method list_effective_space_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_space_groups`")  # noqa: E501

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
            '/spaces/{id}/effective_groups', 'GET',
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

    def list_effective_space_users(self, id, **kwargs):  # noqa: E501
        """List effective space users  # noqa: E501

        Returns the list of effective users belonging to a specific space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_list_relationships` admin privilege.  ***Example cURL requests***  **Get space effective users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_users  {   \"users\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_space_users(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_space_users_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_space_users_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_effective_space_users_with_http_info(self, id, **kwargs):  # noqa: E501
        """List effective space users  # noqa: E501

        Returns the list of effective users belonging to a specific space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_list_relationships` admin privilege.  ***Example cURL requests***  **Get space effective users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_users  {   \"users\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_space_users_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
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
                    " to method list_effective_space_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_space_users`")  # noqa: E501

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
            '/spaces/{id}/effective_users', 'GET',
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

    def list_effective_user_space_privileges(self, id, uid, **kwargs):  # noqa: E501
        """List effective user's space privileges  # noqa: E501

        Returns the list of effective user's (`{uid}`) privileges in a space (`{id}`).  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation requires any of the following authentication: * as user who has `space_view_privileges` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_users_view_privileges` admin privilege.  ***Example cURL requests***  **List effective user's privileges in a space** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_users/$USER_ID/privileges  {   \"privileges\": [     \"space_view\",     \"space_update\",     \"space_delete\",     \"space_view_privileges\",     \"space_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_user_space_privileges(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str uid: User Id. (required)
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_user_space_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_user_space_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def list_effective_user_space_privileges_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """List effective user's space privileges  # noqa: E501

        Returns the list of effective user's (`{uid}`) privileges in a space (`{id}`).  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation requires any of the following authentication: * as user who has `space_view_privileges` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_users_view_privileges` admin privilege.  ***Example cURL requests***  **List effective user's privileges in a space** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/effective_users/$USER_ID/privileges  {   \"privileges\": [     \"space_view\",     \"space_update\",     \"space_delete\",     \"space_view_privileges\",     \"space_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_user_space_privileges_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str uid: User Id. (required)
        :return: InlineResponse2009
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
                    " to method list_effective_user_space_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_user_space_privileges`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `list_effective_user_space_privileges`")  # noqa: E501

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
            '/spaces/{id}/effective_users/{uid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2009',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_group_space_privileges(self, id, gid, **kwargs):  # noqa: E501
        """List group's space privileges  # noqa: E501

        Returns the list of group's (`{gid}`) privileges in a space (`{id}`).  This operation requires any of the following authentication: * as user who has `space_view_privileges` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_view_privileges` admin privilege.  ***Example cURL requests***  **List groups's privileges in a space** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups/$GROUP_ID/privileges  {   \"privileges\": [     \"space_view\",     \"space_update\",     \"space_delete\",     \"space_view_privileges\",     \"space_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_space_privileges(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str gid: Group Id. (required)
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_group_space_privileges_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_group_space_privileges_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def list_group_space_privileges_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """List group's space privileges  # noqa: E501

        Returns the list of group's (`{gid}`) privileges in a space (`{id}`).  This operation requires any of the following authentication: * as user who has `space_view_privileges` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_view_privileges` admin privilege.  ***Example cURL requests***  **List groups's privileges in a space** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups/$GROUP_ID/privileges  {   \"privileges\": [     \"space_view\",     \"space_update\",     \"space_delete\",     \"space_view_privileges\",     \"space_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_space_privileges_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str gid: Group Id. (required)
        :return: InlineResponse2009
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
                    " to method list_group_space_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_group_space_privileges`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `list_group_space_privileges`")  # noqa: E501

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
            '/spaces/{id}/groups/{gid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2009',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_marketplace(self, **kwargs):  # noqa: E501
        """List the Space Marketplace  # noqa: E501

        List spaces advertised in the Marketplace.  ***Example cURL requests***  **List spaces advertised in the Marketplace** ```bash curl -H \"x-auth-token: $TOKEN\" -H \"Content-type: application/json\" \\ -X POST -d '{ \"limit\" : 2 }' \\ https://$ZONE_HOST/api/v3/onezone/spaces/marketplace/list  {   \"spaces\": [     {       \"spaceId\": \"d6ee1aecf03b23f09756d6a49e435455\",        \"index\": \"aqua@d6ee1aecf03b23f09756d6a49e435455\"     },     {       \"spaceId\": \"3b23a49e1aecf06d6555d6e4354f097e\",        \"index\": \"terra@3b23a49e1aecf06d6555d6e4354f097e\"     }   ],   \"isLast\": false,   \"nextPageToken\": \"UkdseU1qWTBNak16TXpNNU5qUXpNak0yTXpZMk1UWTFOalEyTXpZMU5qSTJOalky\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_marketplace(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MarketplaceListBody body: Space Marketplace listing options.
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_marketplace_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_marketplace_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_marketplace_with_http_info(self, **kwargs):  # noqa: E501
        """List the Space Marketplace  # noqa: E501

        List spaces advertised in the Marketplace.  ***Example cURL requests***  **List spaces advertised in the Marketplace** ```bash curl -H \"x-auth-token: $TOKEN\" -H \"Content-type: application/json\" \\ -X POST -d '{ \"limit\" : 2 }' \\ https://$ZONE_HOST/api/v3/onezone/spaces/marketplace/list  {   \"spaces\": [     {       \"spaceId\": \"d6ee1aecf03b23f09756d6a49e435455\",        \"index\": \"aqua@d6ee1aecf03b23f09756d6a49e435455\"     },     {       \"spaceId\": \"3b23a49e1aecf06d6555d6e4354f097e\",        \"index\": \"terra@3b23a49e1aecf06d6555d6e4354f097e\"     }   ],   \"isLast\": false,   \"nextPageToken\": \"UkdseU1qWTBNak16TXpNNU5qUXpNak0yTXpZMk1UWTFOalEyTXpZMU5qSTJOalky\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_marketplace_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MarketplaceListBody body: Space Marketplace listing options.
        :return: InlineResponse2007
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
                    " to method list_marketplace" % key
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
            '/spaces/marketplace/list', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2007',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_space_groups(self, id, **kwargs):  # noqa: E501
        """List space groups  # noqa: E501

        Returns the list of groups belonging to a specific space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_list_relationships` admin privilege.  ***Example cURL requests***  **Get space groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups  {   \"groups\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_space_groups(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :return: Groups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_space_groups_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_space_groups_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_space_groups_with_http_info(self, id, **kwargs):  # noqa: E501
        """List space groups  # noqa: E501

        Returns the list of groups belonging to a specific space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_list_relationships` admin privilege.  ***Example cURL requests***  **Get space groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups  {   \"groups\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_space_groups_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
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
                    " to method list_space_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_space_groups`")  # noqa: E501

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
            '/spaces/{id}/groups', 'GET',
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

    def list_space_harvesters(self, id, **kwargs):  # noqa: E501
        """List space harvesters  # noqa: E501

        Returns the list of harvesters of a specific space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_list_relationships` admin privilege.  ***Example cURL requests***  **Get space harvesters** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/harvesters  {   \"harvesters\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_space_harvesters(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :return: Harvesters
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_space_harvesters_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_space_harvesters_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_space_harvesters_with_http_info(self, id, **kwargs):  # noqa: E501
        """List space harvesters  # noqa: E501

        Returns the list of harvesters of a specific space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_list_relationships` admin privilege.  ***Example cURL requests***  **Get space harvesters** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/harvesters  {   \"harvesters\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_space_harvesters_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
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
                    " to method list_space_harvesters" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_space_harvesters`")  # noqa: E501

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
            '/spaces/{id}/harvesters', 'GET',
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

    def list_space_owners(self, id, **kwargs):  # noqa: E501
        """List space owners  # noqa: E501

        Returns the list of owners of a specific space.  Space owners are members (users) of the space that have absolute power regarding the space API and files (analogical to \"root\", but in the scope of one space). Being an owner means that user privileges are essentially ignored and all API operations are allowed.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_view` admin privilege.  ***Example cURL requests***  **Get space owners** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/owners  {   \"users\": [     \"a5b469a2b0516b662a49da74d6d7d7bc\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_space_owners(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_space_owners_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_space_owners_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_space_owners_with_http_info(self, id, **kwargs):  # noqa: E501
        """List space owners  # noqa: E501

        Returns the list of owners of a specific space.  Space owners are members (users) of the space that have absolute power regarding the space API and files (analogical to \"root\", but in the scope of one space). Being an owner means that user privileges are essentially ignored and all API operations are allowed.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_view` admin privilege.  ***Example cURL requests***  **Get space owners** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/owners  {   \"users\": [     \"a5b469a2b0516b662a49da74d6d7d7bc\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_space_owners_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
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
                    " to method list_space_owners" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_space_owners`")  # noqa: E501

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
            '/spaces/{id}/owners', 'GET',
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

    def list_space_privileges(self, **kwargs):  # noqa: E501
        """List all space privileges  # noqa: E501

        Returns list of all possible space privileges.  This endpoint does not require authentication.  ***Example cURL requests***  **Get list of all space privileges** ```bash curl https://$ZONE_HOST/api/v3/onezone/spaces/privileges  {   \"admin\": [     \"space_view\",     \"space_update\",     \"space_delete\",     \"space_view_privileges\",     \"space_set_privileges\",     \"space_read_data\",     \"space_write_data\",     \"space_register_files\",     \"space_manage_shares\",     \"space_view_views\",     \"space_manage_views\",     \"space_query_views\",     \"space_view_statistics\",     \"space_view_changes_stream\",     \"space_view_transfers\",     \"space_schedule_replication\",     \"space_cancel_replication\",     \"space_schedule_eviction\",     \"space_cancel_eviction\",     \"space_view_qos\",     \"space_manage_qos\",     \"space_add_user\",     \"space_remove_user\",     \"space_add_group\",     \"space_remove_group\",     \"space_add_provider\",     \"space_remove_provider\",     \"space_add_harvester\",     \"space_remove_harvester\"   ],   \"manager\": [     \"space_view\",     \"space_view_privileges\",     \"space_read_data\",     \"space_write_data\",     \"space_register_files\",     \"space_manage_shares\",     \"space_view_views\",     \"space_query_views\",     \"space_view_statistics\",     \"space_view_changes_stream\",     \"space_view_transfers\",     \"space_schedule_replication\",     \"space_view_qos\",     \"space_add_user\",     \"space_remove_user\",     \"space_add_group\",     \"space_remove_group\",     \"space_add_harvester\",     \"space_remove_harvester\"   ],   \"member\": [     \"space_view\",     \"space_read_data\",     \"space_write_data\",     \"space_view_transfers\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_space_privileges(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_space_privileges_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_space_privileges_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_space_privileges_with_http_info(self, **kwargs):  # noqa: E501
        """List all space privileges  # noqa: E501

        Returns list of all possible space privileges.  This endpoint does not require authentication.  ***Example cURL requests***  **Get list of all space privileges** ```bash curl https://$ZONE_HOST/api/v3/onezone/spaces/privileges  {   \"admin\": [     \"space_view\",     \"space_update\",     \"space_delete\",     \"space_view_privileges\",     \"space_set_privileges\",     \"space_read_data\",     \"space_write_data\",     \"space_register_files\",     \"space_manage_shares\",     \"space_view_views\",     \"space_manage_views\",     \"space_query_views\",     \"space_view_statistics\",     \"space_view_changes_stream\",     \"space_view_transfers\",     \"space_schedule_replication\",     \"space_cancel_replication\",     \"space_schedule_eviction\",     \"space_cancel_eviction\",     \"space_view_qos\",     \"space_manage_qos\",     \"space_add_user\",     \"space_remove_user\",     \"space_add_group\",     \"space_remove_group\",     \"space_add_provider\",     \"space_remove_provider\",     \"space_add_harvester\",     \"space_remove_harvester\"   ],   \"manager\": [     \"space_view\",     \"space_view_privileges\",     \"space_read_data\",     \"space_write_data\",     \"space_register_files\",     \"space_manage_shares\",     \"space_view_views\",     \"space_query_views\",     \"space_view_statistics\",     \"space_view_changes_stream\",     \"space_view_transfers\",     \"space_schedule_replication\",     \"space_view_qos\",     \"space_add_user\",     \"space_remove_user\",     \"space_add_group\",     \"space_remove_group\",     \"space_add_harvester\",     \"space_remove_harvester\"   ],   \"member\": [     \"space_view\",     \"space_read_data\",     \"space_write_data\",     \"space_view_transfers\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_space_privileges_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2006
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
                    " to method list_space_privileges" % key
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
            '/spaces/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2006',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_space_providers(self, id, **kwargs):  # noqa: E501
        """List space providers  # noqa: E501

        Returns the list of providers supporting specific space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_list_relationships` admin privilege.  ***Example cURL requests***  **Get space support token** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/providers  {   \"providers\": [     \"MDAxNmxvYZjUGlIcGkweGZta1ZOdEp00eUNINVNvR2001Wl\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_space_providers(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :return: Providers
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_space_providers_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_space_providers_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_space_providers_with_http_info(self, id, **kwargs):  # noqa: E501
        """List space providers  # noqa: E501

        Returns the list of providers supporting specific space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_list_relationships` admin privilege.  ***Example cURL requests***  **Get space support token** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/providers  {   \"providers\": [     \"MDAxNmxvYZjUGlIcGkweGZta1ZOdEp00eUNINVNvR2001Wl\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_space_providers_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
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
                    " to method list_space_providers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_space_providers`")  # noqa: E501

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
            '/spaces/{id}/providers', 'GET',
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

    def list_space_shares(self, id, **kwargs):  # noqa: E501
        """List space shares  # noqa: E501

        Returns the list of shares from specific space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_list_relationships` admin privilege.  ***Example cURL requests***  **List space shares** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/shares  {   \"shares\": [     \"MDAxNmxvYZjUGlIcGkweGZta1ZOdEp00eUNINVNvR2001Wl\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_space_shares(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :return: Shares
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_space_shares_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_space_shares_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_space_shares_with_http_info(self, id, **kwargs):  # noqa: E501
        """List space shares  # noqa: E501

        Returns the list of shares from specific space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_list_relationships` admin privilege.  ***Example cURL requests***  **List space shares** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/shares  {   \"shares\": [     \"MDAxNmxvYZjUGlIcGkweGZta1ZOdEp00eUNINVNvR2001Wl\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_space_shares_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :return: Shares
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
                    " to method list_space_shares" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_space_shares`")  # noqa: E501

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
            '/spaces/{id}/shares', 'GET',
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

    def list_space_users(self, id, **kwargs):  # noqa: E501
        """List space users  # noqa: E501

        Returns the list of users belonging to a specific space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_list_relationships` admin privilege.  ***Example cURL requests***  **Get space users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/users  {   \"users\": [     \"a5b469a2b0516b662a49da74d6d7d7bc\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_space_users(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_space_users_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_space_users_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_space_users_with_http_info(self, id, **kwargs):  # noqa: E501
        """List space users  # noqa: E501

        Returns the list of users belonging to a specific space.  This operation requires any of the following authentication: * as user who has `space_view` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_list_relationships` admin privilege.  ***Example cURL requests***  **Get space users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/users  {   \"users\": [     \"a5b469a2b0516b662a49da74d6d7d7bc\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_space_users_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
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
                    " to method list_space_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_space_users`")  # noqa: E501

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
            '/spaces/{id}/users', 'GET',
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

    def list_spaces(self, **kwargs):  # noqa: E501
        """List all spaces  # noqa: E501

        Returns the list of all spaces managed by the Onezone service.  This operation requires `oz_spaces_list` admin privilege.  ***Example cURL requests***  **List all spaces** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces  {   \"spaces\": [     \"d6ee1aecf03b23f09756d6a49e435455\",     \"3b23a49e1aecf06d6555d6e4354f097e\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_spaces(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Spaces
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_spaces_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_spaces_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_spaces_with_http_info(self, **kwargs):  # noqa: E501
        """List all spaces  # noqa: E501

        Returns the list of all spaces managed by the Onezone service.  This operation requires `oz_spaces_list` admin privilege.  ***Example cURL requests***  **List all spaces** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces  {   \"spaces\": [     \"d6ee1aecf03b23f09756d6a49e435455\",     \"3b23a49e1aecf06d6555d6e4354f097e\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_spaces_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Spaces
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
                    " to method list_spaces" % key
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
            '/spaces', 'GET',
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

    def list_user_space_privileges(self, id, uid, **kwargs):  # noqa: E501
        """List user's space privileges  # noqa: E501

        Returns the list of user's (`{uid}`) privileges in a space (`{id}`).  This operation requires any of the following authentication: * as user who has `space_view_privileges` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_view_privileges` admin privilege.  ***Example cURL requests***  **List user's privileges in a space** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/users/$USER_ID/privileges  {   \"privileges\": [     \"space_view\",     \"space_update\",     \"space_delete\",     \"space_view_privileges\",     \"space_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_space_privileges(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str uid: User Id. (required)
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_space_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_user_space_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def list_user_space_privileges_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """List user's space privileges  # noqa: E501

        Returns the list of user's (`{uid}`) privileges in a space (`{id}`).  This operation requires any of the following authentication: * as user who has `space_view_privileges` privilege in the space (`{id}`), * as provider that supports the space (`{id}`), * as user who has `oz_spaces_view_privileges` admin privilege.  ***Example cURL requests***  **List user's privileges in a space** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/users/$USER_ID/privileges  {   \"privileges\": [     \"space_view\",     \"space_update\",     \"space_delete\",     \"space_view_privileges\",     \"space_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_space_privileges_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str uid: User Id. (required)
        :return: InlineResponse2009
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
                    " to method list_user_space_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_user_space_privileges`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `list_user_space_privileges`")  # noqa: E501

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
            '/spaces/{id}/users/{uid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2009',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_space(self, body, id, **kwargs):  # noqa: E501
        """Modify space details  # noqa: E501

        Updates the details about a space.  This operation requires `space_update` privilege or `oz_spaces_update` admin privilege.  ***Example cURL requests***  **Change space name** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"name\": \"new_space12\"}' \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_space(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SpacesIdBody body: Space parameters (required)
        :param str id: Space Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_space_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_space_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def modify_space_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Modify space details  # noqa: E501

        Updates the details about a space.  This operation requires `space_update` privilege or `oz_spaces_update` admin privilege.  ***Example cURL requests***  **Change space name** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"name\": \"new_space12\"}' \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_space_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SpacesIdBody body: Space parameters (required)
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
                    " to method modify_space" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `modify_space`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `modify_space`")  # noqa: E501

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
            '/spaces/{id}', 'PATCH',
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

    def remove_space(self, id, **kwargs):  # noqa: E501
        """Remove space  # noqa: E501

        Removes a specific space.  This operation requires `space_delete` privilege or `oz_spaces_delete` admin privilege.  ***Example cURL requests***  **Remove space** ```bash curl -u admin:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_space(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_space_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_space_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def remove_space_with_http_info(self, id, **kwargs):  # noqa: E501
        """Remove space  # noqa: E501

        Removes a specific space.  This operation requires `space_delete` privilege or `oz_spaces_delete` admin privilege.  ***Example cURL requests***  **Remove space** ```bash curl -u admin:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_space_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
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
                    " to method remove_space" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_space`")  # noqa: E501

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
            '/spaces/{id}', 'DELETE',
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

    def remove_space_from_harvester(self, id, hid, **kwargs):  # noqa: E501
        """Remove space from harvester.  # noqa: E501

        Removes the space {id} from harvester {hid} (metadata from given space will no longer be submitted to given harvester).  This operation requires `space_remove_harvester` privilege. For administrator who does not belong to this group `oz_spaces_remove_relationships` and `oz_harvesters_remove_relationships` privileges are required.  ***Example cURL requests***  **Get space harvester details** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/harvesters/$HARVESTER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_space_from_harvester(id, hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str hid: Harvester Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_space_from_harvester_with_http_info(id, hid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_space_from_harvester_with_http_info(id, hid, **kwargs)  # noqa: E501
            return data

    def remove_space_from_harvester_with_http_info(self, id, hid, **kwargs):  # noqa: E501
        """Remove space from harvester.  # noqa: E501

        Removes the space {id} from harvester {hid} (metadata from given space will no longer be submitted to given harvester).  This operation requires `space_remove_harvester` privilege. For administrator who does not belong to this group `oz_spaces_remove_relationships` and `oz_harvesters_remove_relationships` privileges are required.  ***Example cURL requests***  **Get space harvester details** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/harvesters/$HARVESTER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_space_from_harvester_with_http_info(id, hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
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
                    " to method remove_space_from_harvester" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_space_from_harvester`")  # noqa: E501
        # verify the required parameter 'hid' is set
        if ('hid' not in params or
                params['hid'] is None):
            raise ValueError("Missing the required parameter `hid` when calling `remove_space_from_harvester`")  # noqa: E501

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
            '/spaces/{id}/harvesters/{hid}', 'DELETE',
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

    def remove_space_group(self, id, gid, **kwargs):  # noqa: E501
        """Remove group from space  # noqa: E501

        Removes a specific group from space.  For regular users, who belong to this space it requires `space_remove_group` privilege to remove a group from this space.  For administrators, who are not members of this space, `oz_spaces_remove_relationships` privilege is required.  ***Example cURL requests***  **Get space group details** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_space_group(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str gid: Group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_space_group_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_space_group_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def remove_space_group_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Remove group from space  # noqa: E501

        Removes a specific group from space.  For regular users, who belong to this space it requires `space_remove_group` privilege to remove a group from this space.  For administrators, who are not members of this space, `oz_spaces_remove_relationships` privilege is required.  ***Example cURL requests***  **Get space group details** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_space_group_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str gid: Group Id. (required)
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
                    " to method remove_space_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_space_group`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `remove_space_group`")  # noqa: E501

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
            '/spaces/{id}/groups/{gid}', 'DELETE',
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

    def remove_space_owner(self, id, uid, **kwargs):  # noqa: E501
        """Remove space owner  # noqa: E501

        Removes user `{uid}` from the owners of space `{id}`. The user is not removed from the space as a member, but his ownership is revoked.  This operation will fail if the `{uid}` is the last owner of the space. First, ownership must be granted to another user so that the space has at least one owner.  This operation requires any of the following authentication: * as user who is currently an owner of the space (`{id}`), * as user who has `oz_spaces_set_privileges` admin privilege.  ***Example cURL requests***  **Remove space owner** ```bash curl -u admin:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/owners/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_space_owner(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str uid: User Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_space_owner_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_space_owner_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def remove_space_owner_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Remove space owner  # noqa: E501

        Removes user `{uid}` from the owners of space `{id}`. The user is not removed from the space as a member, but his ownership is revoked.  This operation will fail if the `{uid}` is the last owner of the space. First, ownership must be granted to another user so that the space has at least one owner.  This operation requires any of the following authentication: * as user who is currently an owner of the space (`{id}`), * as user who has `oz_spaces_set_privileges` admin privilege.  ***Example cURL requests***  **Remove space owner** ```bash curl -u admin:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/owners/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_space_owner_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
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
                    " to method remove_space_owner" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_space_owner`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `remove_space_owner`")  # noqa: E501

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
            '/spaces/{id}/owners/{uid}', 'DELETE',
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

    def remove_space_user(self, id, uid, **kwargs):  # noqa: E501
        """Remove user from space  # noqa: E501

        Removes user from specific space.  This operation requires `space_remove_user` or requires `oz_spaces_add_relationships` and `oz_users_add_relationships` admin privilege.  ***Example cURL requests***  **Remove user from space** ```bash curl -u admin:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_space_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str uid: User Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_space_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_space_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def remove_space_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Remove user from space  # noqa: E501

        Removes user from specific space.  This operation requires `space_remove_user` or requires `oz_spaces_add_relationships` and `oz_users_add_relationships` admin privilege.  ***Example cURL requests***  **Remove user from space** ```bash curl -u admin:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_space_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
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
                    " to method remove_space_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_space_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `remove_space_user`")  # noqa: E501

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
            '/spaces/{id}/users/{uid}', 'DELETE',
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

    def request_space_membership(self, body, id, **kwargs):  # noqa: E501
        """Request space membership via Marketplace  # noqa: E501

        Request space membership for a space advertised in the Marketplace as currently authenticated user.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Request space membership via Marketplace** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"contactEmail\" : \"user@example.com\"}' \\ https://$ZONE_HOST/api/v3/onezone/spaces/marketplace/$SPACE_ID/request ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_space_membership(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdRequestBody body: Space membership request body. (required)
        :param str id: Space Id. (required)
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.request_space_membership_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.request_space_membership_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def request_space_membership_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Request space membership via Marketplace  # noqa: E501

        Request space membership for a space advertised in the Marketplace as currently authenticated user.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Request space membership via Marketplace** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"contactEmail\" : \"user@example.com\"}' \\ https://$ZONE_HOST/api/v3/onezone/spaces/marketplace/$SPACE_ID/request ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_space_membership_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdRequestBody body: Space membership request body. (required)
        :param str id: Space Id. (required)
        :return: InlineResponse2008
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
                    " to method request_space_membership" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `request_space_membership`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `request_space_membership`")  # noqa: E501

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
            '/spaces/marketplace/{id}/request', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2008',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resolve_space_membership_request(self, body, id, rid, **kwargs):  # noqa: E501
        """Resolve space membership request  # noqa: E501

        Resolve space membership request made via the Marketplace.  This operation requires privilege `space_manage_in_marketplace` and, in case of positive resolution, `space_add_user` in space for which  the request was made.  ***Example cURL requests***  **Resolve space membership request** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"requestId\": \"97216a666edd09945880a0785ad66a7b\", \"decision\": \"grant\"}' \\ https://$ZONE_HOST/api/v3/onezone/spaces/marketplace/$SPACE_ID/request/$REQUEST_ID/resolve ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resolve_space_membership_request(body, id, rid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RidResolveBody body: Space membership request resolution body. (required)
        :param str id: Space Id. (required)
        :param str rid: Space membership request Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.resolve_space_membership_request_with_http_info(body, id, rid, **kwargs)  # noqa: E501
        else:
            (data) = self.resolve_space_membership_request_with_http_info(body, id, rid, **kwargs)  # noqa: E501
            return data

    def resolve_space_membership_request_with_http_info(self, body, id, rid, **kwargs):  # noqa: E501
        """Resolve space membership request  # noqa: E501

        Resolve space membership request made via the Marketplace.  This operation requires privilege `space_manage_in_marketplace` and, in case of positive resolution, `space_add_user` in space for which  the request was made.  ***Example cURL requests***  **Resolve space membership request** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"requestId\": \"97216a666edd09945880a0785ad66a7b\", \"decision\": \"grant\"}' \\ https://$ZONE_HOST/api/v3/onezone/spaces/marketplace/$SPACE_ID/request/$REQUEST_ID/resolve ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resolve_space_membership_request_with_http_info(body, id, rid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RidResolveBody body: Space membership request resolution body. (required)
        :param str id: Space Id. (required)
        :param str rid: Space membership request Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id', 'rid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resolve_space_membership_request" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `resolve_space_membership_request`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `resolve_space_membership_request`")  # noqa: E501
        # verify the required parameter 'rid' is set
        if ('rid' not in params or
                params['rid'] is None):
            raise ValueError("Missing the required parameter `rid` when calling `resolve_space_membership_request`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'rid' in params:
            path_params['rid'] = params['rid']  # noqa: E501

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
            '/spaces/marketplace/{id}/request/{rid}/resolve', 'POST',
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

    def space_join_harvester(self, id, **kwargs):  # noqa: E501
        """Join space to a harvester  # noqa: E501

        Joins the space to an existing harvester based on provided `spaceJoinHarvester` invitation token (the space becomes a metadata source for the harvester).  This operation requires `space_add_harvester` privilege. For administrator who does not belong to this space `oz_harvesters_add_relationships` and `oz_spaces_add_relationships` privilege is required.  ***Example cURL requests***  **Join space to a harvester** ```bash curl -u admin:password -H \"Content-type: application/json\" \\ -d '{\"token\":\"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVuJ3l02U1JXzstRdK00ZHbso02rRcG8bJLAo\"}' \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/harvesters/join ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.space_join_harvester(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param HarvesterInviteToken body: spaceJoinHarvester invite token.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.space_join_harvester_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.space_join_harvester_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def space_join_harvester_with_http_info(self, id, **kwargs):  # noqa: E501
        """Join space to a harvester  # noqa: E501

        Joins the space to an existing harvester based on provided `spaceJoinHarvester` invitation token (the space becomes a metadata source for the harvester).  This operation requires `space_add_harvester` privilege. For administrator who does not belong to this space `oz_harvesters_add_relationships` and `oz_spaces_add_relationships` privilege is required.  ***Example cURL requests***  **Join space to a harvester** ```bash curl -u admin:password -H \"Content-type: application/json\" \\ -d '{\"token\":\"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVuJ3l02U1JXzstRdK00ZHbso02rRcG8bJLAo\"}' \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/harvesters/join ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.space_join_harvester_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param HarvesterInviteToken body: spaceJoinHarvester invite token.
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
                    " to method space_join_harvester" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `space_join_harvester`")  # noqa: E501

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
            '/spaces/{id}/harvesters/join', 'POST',
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

    def update_group_space_privileges(self, body, id, gid, **kwargs):  # noqa: E501
        """Update group privileges to space  # noqa: E501

        Updates group's (`{gid}`) privileges in a space (`{id}`).  This operation requires `space_set_privileges` privilege or `oz_spaces_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update group's privileges in a space** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"space_view\", \"space_update\"], \"revoke\": [\"space_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups/$GROUP_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_group_space_privileges(body, id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SpacePrivilegesUpdate body: Space privileges update request. (required)
        :param str id: Space Id. (required)
        :param str gid: Group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_group_space_privileges_with_http_info(body, id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_group_space_privileges_with_http_info(body, id, gid, **kwargs)  # noqa: E501
            return data

    def update_group_space_privileges_with_http_info(self, body, id, gid, **kwargs):  # noqa: E501
        """Update group privileges to space  # noqa: E501

        Updates group's (`{gid}`) privileges in a space (`{id}`).  This operation requires `space_set_privileges` privilege or `oz_spaces_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update group's privileges in a space** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"space_view\", \"space_update\"], \"revoke\": [\"space_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/groups/$GROUP_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_group_space_privileges_with_http_info(body, id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SpacePrivilegesUpdate body: Space privileges update request. (required)
        :param str id: Space Id. (required)
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
                    " to method update_group_space_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_group_space_privileges`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_group_space_privileges`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `update_group_space_privileges`")  # noqa: E501

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
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/spaces/{id}/groups/{gid}/privileges', 'PATCH',
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

    def update_support_parameters_of_provider(self, id, pid, **kwargs):  # noqa: E501
        """Update space support parameters of provider  # noqa: E501

        Updates space support parameters of a provider in the space.  Authorization depends on the modified parameters (see respective descriptions).  ***Example cURL requests***  **Update space support parameters of provider** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"dirStatsServiceEnabled\": true}' \\ https://$HOST/api/v3/onezone/spaces/$SPACE_ID/providers/$PROVIDER_ID/support_parameters ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_support_parameters_of_provider(id, pid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str pid: Provider Id. (required)
        :param SupportParameters body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_support_parameters_of_provider_with_http_info(id, pid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_support_parameters_of_provider_with_http_info(id, pid, **kwargs)  # noqa: E501
            return data

    def update_support_parameters_of_provider_with_http_info(self, id, pid, **kwargs):  # noqa: E501
        """Update space support parameters of provider  # noqa: E501

        Updates space support parameters of a provider in the space.  Authorization depends on the modified parameters (see respective descriptions).  ***Example cURL requests***  **Update space support parameters of provider** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"dirStatsServiceEnabled\": true}' \\ https://$HOST/api/v3/onezone/spaces/$SPACE_ID/providers/$PROVIDER_ID/support_parameters ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_support_parameters_of_provider_with_http_info(id, pid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Space Id. (required)
        :param str pid: Provider Id. (required)
        :param SupportParameters body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'pid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_support_parameters_of_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_support_parameters_of_provider`")  # noqa: E501
        # verify the required parameter 'pid' is set
        if ('pid' not in params or
                params['pid'] is None):
            raise ValueError("Missing the required parameter `pid` when calling `update_support_parameters_of_provider`")  # noqa: E501

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
            '/spaces/{id}/providers/{pid}/support_parameters', 'PATCH',
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

    def update_user_space_privileges(self, body, id, uid, **kwargs):  # noqa: E501
        """Update user's space privileges  # noqa: E501

        Updates user's (`{uid}`) privileges in a space (`{id}`).  This operation requires `space_set_privileges` privilege. For administrators who do not have to be members of this space, `oz_spaces_set_privileges` privilege is required.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update user's privileges in a space** ```bash curl -u admin:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"space_view\", \"space_update\"], \"revoke\": [\"space_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/users/$USER_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_space_privileges(body, id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SpacePrivilegesUpdate body: Space privileges update request. (required)
        :param str id: Space Id. (required)
        :param str uid: User Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_user_space_privileges_with_http_info(body, id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_user_space_privileges_with_http_info(body, id, uid, **kwargs)  # noqa: E501
            return data

    def update_user_space_privileges_with_http_info(self, body, id, uid, **kwargs):  # noqa: E501
        """Update user's space privileges  # noqa: E501

        Updates user's (`{uid}`) privileges in a space (`{id}`).  This operation requires `space_set_privileges` privilege. For administrators who do not have to be members of this space, `oz_spaces_set_privileges` privilege is required.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update user's privileges in a space** ```bash curl -u admin:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"space_view\", \"space_update\"], \"revoke\": [\"space_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/spaces/$SPACE_ID/users/$USER_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_space_privileges_with_http_info(body, id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SpacePrivilegesUpdate body: Space privileges update request. (required)
        :param str id: Space Id. (required)
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
                    " to method update_user_space_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_user_space_privileges`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_user_space_privileges`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `update_user_space_privileges`")  # noqa: E501

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
            '/spaces/{id}/users/{uid}/privileges', 'PATCH',
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
