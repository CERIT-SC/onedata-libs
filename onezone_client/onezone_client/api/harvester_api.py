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


class HarvesterApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_group_to_harvester(self, id, gid, **kwargs):  # noqa: E501
        """Add group to harvester  # noqa: E501

        Adds group {gid} as member of harvester {id}. Optional privileges can be passed in the request body, otherwise default privileges will be set for the group in this harvester.  This operation requires `harvester_add_group` privilege in the harvester and `group_add_harvester` privilege in the group. If `privileges` are specified in the request, `harvester_set_privileges` privilege is also required.  For administrator who does not belong to the group / harvester, `oz_groups_add_relationships` and `oz_harvesters_add_relationships` privileges are required, and `oz_harvesters_set_privileges` if `privileges` are specified in the request.  ***Example cURL requests***  **Add group to harvester** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\  https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_group_to_harvester(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str gid: Group Id. (required)
        :param GroupsGidBody3 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_group_to_harvester_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.add_group_to_harvester_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def add_group_to_harvester_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Add group to harvester  # noqa: E501

        Adds group {gid} as member of harvester {id}. Optional privileges can be passed in the request body, otherwise default privileges will be set for the group in this harvester.  This operation requires `harvester_add_group` privilege in the harvester and `group_add_harvester` privilege in the group. If `privileges` are specified in the request, `harvester_set_privileges` privilege is also required.  For administrator who does not belong to the group / harvester, `oz_groups_add_relationships` and `oz_harvesters_add_relationships` privileges are required, and `oz_harvesters_set_privileges` if `privileges` are specified in the request.  ***Example cURL requests***  **Add group to harvester** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\  https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_group_to_harvester_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str gid: Group Id. (required)
        :param GroupsGidBody3 body:
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
                    " to method add_group_to_harvester" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_group_to_harvester`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `add_group_to_harvester`")  # noqa: E501

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
            '/harvesters/{id}/groups/{gid}', 'PUT',
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

    def add_harvester_user(self, id, uid, **kwargs):  # noqa: E501
        """Add user to harvester  # noqa: E501

        Adds user {uid} as member of harvester {id}. Optional privileges can be passed in the request body, otherwise default privileges will be set for the user in this harvester.  This operation can only be invoked by the user {uid} to add himself to the harvester (if he is not a member already) and requires `harvester_invite_user` privilege in the harvester. If `privileges` are specified in the request, `harvester_set_privileges` privilege is also required.  Administrators having the `oz_harvesters_add_relationships` and `oz_users_add_relationships` admin privileges can add any user to any harvester, though `oz_harvesters_set_privileges` privilege is required if `privileges` are specified in the request.  ***Example cURL requests***  **Add user to harvester** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_harvester_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str uid: User Id. (required)
        :param UsersUidBody4 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_harvester_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.add_harvester_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def add_harvester_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Add user to harvester  # noqa: E501

        Adds user {uid} as member of harvester {id}. Optional privileges can be passed in the request body, otherwise default privileges will be set for the user in this harvester.  This operation can only be invoked by the user {uid} to add himself to the harvester (if he is not a member already) and requires `harvester_invite_user` privilege in the harvester. If `privileges` are specified in the request, `harvester_set_privileges` privilege is also required.  Administrators having the `oz_harvesters_add_relationships` and `oz_users_add_relationships` admin privileges can add any user to any harvester, though `oz_harvesters_set_privileges` privilege is required if `privileges` are specified in the request.  ***Example cURL requests***  **Add user to harvester** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_harvester_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str uid: User Id. (required)
        :param UsersUidBody4 body:
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
                    " to method add_harvester_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_harvester_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `add_harvester_user`")  # noqa: E501

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
            '/harvesters/{id}/users/{uid}', 'PUT',
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

    def add_space_to_harvester(self, id, sid, **kwargs):  # noqa: E501
        """Add space to harvester  # noqa: E501

        Adds space {sid} as member of harvester {id}.  This operation requires `harvester_add_space` privilege in the harvester and `space_add_harvester` privilege in the space.  For administrator who does not belong to the space / harvester, `oz_spaces_add_relationships` and `oz_harvesters_add_relationships` privileges are required.  ***Example cURL requests***  **Add space to harvester** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\  https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/spaces/$SPACE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_space_to_harvester(id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str sid: Space Id. (required)
        :param list[str] body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_space_to_harvester_with_http_info(id, sid, **kwargs)  # noqa: E501
        else:
            (data) = self.add_space_to_harvester_with_http_info(id, sid, **kwargs)  # noqa: E501
            return data

    def add_space_to_harvester_with_http_info(self, id, sid, **kwargs):  # noqa: E501
        """Add space to harvester  # noqa: E501

        Adds space {sid} as member of harvester {id}.  This operation requires `harvester_add_space` privilege in the harvester and `space_add_harvester` privilege in the space.  For administrator who does not belong to the space / harvester, `oz_spaces_add_relationships` and `oz_harvesters_add_relationships` privileges are required.  ***Example cURL requests***  **Add space to harvester** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\  https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/spaces/$SPACE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_space_to_harvester_with_http_info(id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str sid: Space Id. (required)
        :param list[str] body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'sid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_space_to_harvester" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_space_to_harvester`")  # noqa: E501
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `add_space_to_harvester`")  # noqa: E501

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
            '/harvesters/{id}/spaces/{sid}', 'PUT',
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

    def create_harvester(self, body, **kwargs):  # noqa: E501
        """Create new harvester  # noqa: E501

        Creates new harvester.  This operation requires `oz_harvesters_create` admin privilege.  See also:   [Create a new harvester for the current user](#operation/create_user_harvester)   [Create a new harvester for given group](#operation/create_harvester_for_group)    ***Example cURL requests***  **Create new harvester** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"name\" : \"new_harvester\", \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\", \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\"  \\ \"guiPluginConfig\" : { \"typeMapping\": [ { \"id\": 0, \"name\": \"Type 1\" }, { \"id\": 1, \"name\": \"Type 1\" } ],                        \"externalHelpLink\": \"http://example.com/some_help_page\",                        \"refreshDataTimeout\": 1000 }                     }' \\ https://$ZONE_HOST/api/v3/onezone/harvesters ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_harvester(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HarvesterCreateRequest body: Harvester properties. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_harvester_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_harvester_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_harvester_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create new harvester  # noqa: E501

        Creates new harvester.  This operation requires `oz_harvesters_create` admin privilege.  See also:   [Create a new harvester for the current user](#operation/create_user_harvester)   [Create a new harvester for given group](#operation/create_harvester_for_group)    ***Example cURL requests***  **Create new harvester** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"name\" : \"new_harvester\", \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\", \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\"  \\ \"guiPluginConfig\" : { \"typeMapping\": [ { \"id\": 0, \"name\": \"Type 1\" }, { \"id\": 1, \"name\": \"Type 1\" } ],                        \"externalHelpLink\": \"http://example.com/some_help_page\",                        \"refreshDataTimeout\": 1000 }                     }' \\ https://$ZONE_HOST/api/v3/onezone/harvesters ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_harvester_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HarvesterCreateRequest body: Harvester properties. (required)
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
                    " to method create_harvester" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_harvester`")  # noqa: E501

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
            '/harvesters', 'POST',
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

    def create_harvester_group(self, body, id, **kwargs):  # noqa: E501
        """Create group in harvester  # noqa: E501

        Creates a new group belonging to the harvester of {id}.  This operation requires `harvester_add_group` privilege. For administrator who does not belong to this group `oz_harvesters_add_relationships` and `oz_groups_create` privileges are required.  ***Example cURL requests***  **Create group in harvester** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_harvester_group(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupCreateRequest body: Group properties. (required)
        :param str id: Harvester Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_harvester_group_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_harvester_group_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def create_harvester_group_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Create group in harvester  # noqa: E501

        Creates a new group belonging to the harvester of {id}.  This operation requires `harvester_add_group` privilege. For administrator who does not belong to this group `oz_harvesters_add_relationships` and `oz_groups_create` privileges are required.  ***Example cURL requests***  **Create group in harvester** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_harvester_group_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupCreateRequest body: Group properties. (required)
        :param str id: Harvester Id. (required)
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
                    " to method create_harvester_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_harvester_group`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_harvester_group`")  # noqa: E501

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
            '/harvesters/{id}/groups', 'POST',
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

    def create_harvester_group_token(self, id, **kwargs):  # noqa: E501
        """Create harvester invite token for group  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token allowing to add a group to a specific harvester.  This operation requires `harvester_add_group` privilege or `oz_harvesters_add_relationships` admin privilege.  ***Example cURL requests***  **Create harvester invitation token for group** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups/token  {   \"token\": \"MDAxNmxvY0cGUgKWsjcpnrLE00RtOd2F00cGUgKWsjcpnrLE00RtOdhmnQycSICwMsugo\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_harvester_group_token(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :return: HarvesterInviteToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_harvester_group_token_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_harvester_group_token_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def create_harvester_group_token_with_http_info(self, id, **kwargs):  # noqa: E501
        """Create harvester invite token for group  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token allowing to add a group to a specific harvester.  This operation requires `harvester_add_group` privilege or `oz_harvesters_add_relationships` admin privilege.  ***Example cURL requests***  **Create harvester invitation token for group** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups/token  {   \"token\": \"MDAxNmxvY0cGUgKWsjcpnrLE00RtOd2F00cGUgKWsjcpnrLE00RtOdhmnQycSICwMsugo\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_harvester_group_token_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :return: HarvesterInviteToken
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
                    " to method create_harvester_group_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_harvester_group_token`")  # noqa: E501

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
            '/harvesters/{id}/groups/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HarvesterInviteToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_harvester_index(self, body, id, **kwargs):  # noqa: E501
        """Create new index in harvester  # noqa: E501

        Creates new index in given harvester.  This operation requires `oz_harvesters_update` admin privilege.  ***Example cURL requests***  **Create new index in harvester** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"name\" : \"My study index\", \"guiPluginName\" : \"study\"}\\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_harvester_index(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HarvesterIndexCreateRequest body: Index properties. (required)
        :param str id: Harvester Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_harvester_index_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_harvester_index_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def create_harvester_index_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Create new index in harvester  # noqa: E501

        Creates new index in given harvester.  This operation requires `oz_harvesters_update` admin privilege.  ***Example cURL requests***  **Create new index in harvester** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"name\" : \"My study index\", \"guiPluginName\" : \"study\"}\\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_harvester_index_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HarvesterIndexCreateRequest body: Index properties. (required)
        :param str id: Harvester Id. (required)
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
                    " to method create_harvester_index" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_harvester_index`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_harvester_index`")  # noqa: E501

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
            '/harvesters/{id}/indices', 'POST',
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

    def create_harvester_invite_space_token(self, id, **kwargs):  # noqa: E501
        """Create harvester invite token for space  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token which can be can be consumed to add a space to a harvester.  This operation requires `harvester_invite_space` privilege or `oz_harvesters_add_relationships` admin privilege.  ***Example cURL requests***  **Create harvester invite space token** ```bash curl -u admin:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/spaces/token  {   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaWVyIHZjUGlIcGkweGZta1ZOdEp00eUNINVNvR2001Wl\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_harvester_invite_space_token(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :return: HarvesterInviteToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_harvester_invite_space_token_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_harvester_invite_space_token_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def create_harvester_invite_space_token_with_http_info(self, id, **kwargs):  # noqa: E501
        """Create harvester invite token for space  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token which can be can be consumed to add a space to a harvester.  This operation requires `harvester_invite_space` privilege or `oz_harvesters_add_relationships` admin privilege.  ***Example cURL requests***  **Create harvester invite space token** ```bash curl -u admin:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/spaces/token  {   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaWVyIHZjUGlIcGkweGZta1ZOdEp00eUNINVNvR2001Wl\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_harvester_invite_space_token_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :return: HarvesterInviteToken
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
                    " to method create_harvester_invite_space_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_harvester_invite_space_token`")  # noqa: E501

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
            '/harvesters/{id}/spaces/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HarvesterInviteToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_harvester_user_invite_token(self, id, **kwargs):  # noqa: E501
        """Create harvester user invite token  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token allowing new user to join a harvester.  This operation requires `harvester_invite_user` privilege. For administrators who do not have to be members of this harvester, `oz_harvesters_add_relationships` privilege is required.  ***Example cURL requests***  **Create harvester user invite token** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/users/token  {   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaWVyIG00zcEJ2UDVuOHhkQUNhdk9hbTlyNnIwNldPSzVhc\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_harvester_user_invite_token(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :return: HarvesterInviteToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_harvester_user_invite_token_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_harvester_user_invite_token_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def create_harvester_user_invite_token_with_http_info(self, id, **kwargs):  # noqa: E501
        """Create harvester user invite token  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token allowing new user to join a harvester.  This operation requires `harvester_invite_user` privilege. For administrators who do not have to be members of this harvester, `oz_harvesters_add_relationships` privilege is required.  ***Example cURL requests***  **Create harvester user invite token** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/users/token  {   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaWVyIG00zcEJ2UDVuOHhkQUNhdk9hbTlyNnIwNldPSzVhc\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_harvester_user_invite_token_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :return: HarvesterInviteToken
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
                    " to method create_harvester_user_invite_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_harvester_user_invite_token`")  # noqa: E501

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
            '/harvesters/{id}/users/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HarvesterInviteToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_effective_group_harvester_membership_intermediaries(self, id, gid, **kwargs):  # noqa: E501
        """Get effective group's harvester membership intermediaries  # noqa: E501

        Returns the effective group's (`{gid}`) harvester membership intermediaries - entities from which the group inherits access to the harvester (`{id}`). Special keyword `\"self\"` in entity id indicates that the group (`{gid}`) has a direct access to the harvester (`{id}`).  This operation requires any of the following authorization: * as user who is an effective member of the group (`{gid}`) * as user who has `harvester_view` privilege in the harvester (`{id}`) * as user who has `oz_harvesters_view` admin privilege.  ***Example cURL requests***  **Get effective group's harvester membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_groups/$GROUP_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"harvester\", \"id\": \"self\"}   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_group_harvester_membership_intermediaries(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str gid: Group Id. (required)
        :return: MembershipIntermediaries
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_group_harvester_membership_intermediaries_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_group_harvester_membership_intermediaries_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def get_effective_group_harvester_membership_intermediaries_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Get effective group's harvester membership intermediaries  # noqa: E501

        Returns the effective group's (`{gid}`) harvester membership intermediaries - entities from which the group inherits access to the harvester (`{id}`). Special keyword `\"self\"` in entity id indicates that the group (`{gid}`) has a direct access to the harvester (`{id}`).  This operation requires any of the following authorization: * as user who is an effective member of the group (`{gid}`) * as user who has `harvester_view` privilege in the harvester (`{id}`) * as user who has `oz_harvesters_view` admin privilege.  ***Example cURL requests***  **Get effective group's harvester membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_groups/$GROUP_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"harvester\", \"id\": \"self\"}   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_group_harvester_membership_intermediaries_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
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
                    " to method get_effective_group_harvester_membership_intermediaries" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_group_harvester_membership_intermediaries`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `get_effective_group_harvester_membership_intermediaries`")  # noqa: E501

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
            '/harvesters/{id}/effective_groups/{gid}/membership', 'GET',
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

    def get_effective_harvester_group(self, id, gid, **kwargs):  # noqa: E501
        """Get effective harvester group details  # noqa: E501

        Returns details about a specific effective group in a harvester.  This operation requires `harvester_view` privilege or `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get effective harvester group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_groups/$GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_groupX\",   \"type\": \"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_harvester_group(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str gid: Group Id. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_harvester_group_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_harvester_group_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def get_effective_harvester_group_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Get effective harvester group details  # noqa: E501

        Returns details about a specific effective group in a harvester.  This operation requires `harvester_view` privilege or `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get effective harvester group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_groups/$GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_groupX\",   \"type\": \"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_harvester_group_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
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
                    " to method get_effective_harvester_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_harvester_group`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `get_effective_harvester_group`")  # noqa: E501

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
            '/harvesters/{id}/effective_groups/{gid}', 'GET',
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

    def get_effective_harvester_user(self, id, uid, **kwargs):  # noqa: E501
        """Get effective harvester user details  # noqa: E501

        Returns details about a specific effective user in a harvester.  This operation requires `harvester_view` privilege or `oz_users_view` admin privilege.  ***Example cURL requests***  **Get effective harvester user details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_users/$USER_ID  {   \"userId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"username\" : \"jodoe\",   \"fullName\" : \"John Doe\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_harvester_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str uid: User Id. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_harvester_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_harvester_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def get_effective_harvester_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Get effective harvester user details  # noqa: E501

        Returns details about a specific effective user in a harvester.  This operation requires `harvester_view` privilege or `oz_users_view` admin privilege.  ***Example cURL requests***  **Get effective harvester user details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_users/$USER_ID  {   \"userId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"username\" : \"jodoe\",   \"fullName\" : \"John Doe\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_harvester_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
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
                    " to method get_effective_harvester_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_harvester_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_effective_harvester_user`")  # noqa: E501

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
            '/harvesters/{id}/effective_users/{uid}', 'GET',
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

    def get_effective_user_harvester_membership_intermediaries(self, id, uid, **kwargs):  # noqa: E501
        """Get effective user's harvester membership intermediaries  # noqa: E501

        Returns the effective user's (`{uid}`) harvester membership intermediaries - entities from which the user inherits access to the harvester (`{id}`). Special keyword `\"self\"` in entity id indicates that the user (`{uid}`) has a direct access to the harvester (`{id}`).  This operation requires any of the following authorization: * as user (`{uid}`) who is an effective member of the harvester (`{id}`) * as user who has `harvester_view` privilege in the harvester (`{id}`) * as user who has `oz_harvesters_view` admin privilege.  ***Example cURL requests***  **Get effective user's harvester membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_users/$USER_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"harvester\", \"id\": \"self\"}   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_user_harvester_membership_intermediaries(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str uid: User Id. (required)
        :return: MembershipIntermediaries
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_user_harvester_membership_intermediaries_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_user_harvester_membership_intermediaries_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def get_effective_user_harvester_membership_intermediaries_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Get effective user's harvester membership intermediaries  # noqa: E501

        Returns the effective user's (`{uid}`) harvester membership intermediaries - entities from which the user inherits access to the harvester (`{id}`). Special keyword `\"self\"` in entity id indicates that the user (`{uid}`) has a direct access to the harvester (`{id}`).  This operation requires any of the following authorization: * as user (`{uid}`) who is an effective member of the harvester (`{id}`) * as user who has `harvester_view` privilege in the harvester (`{id}`) * as user who has `oz_harvesters_view` admin privilege.  ***Example cURL requests***  **Get effective user's harvester membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_users/$USER_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"harvester\", \"id\": \"self\"}   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_user_harvester_membership_intermediaries_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
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
                    " to method get_effective_user_harvester_membership_intermediaries" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_user_harvester_membership_intermediaries`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_effective_user_harvester_membership_intermediaries`")  # noqa: E501

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
            '/harvesters/{id}/effective_users/{uid}/membership', 'GET',
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

    def get_harvester(self, id, **kwargs):  # noqa: E501
        """Get harvester details  # noqa: E501

        Returns the details about a specific harvester.  If called by user who is not member of the harvester, requires `oz_harvesters_view` admin privilege.  ***Example cURL requests***  **Get harvester details** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID  {   \"harvesterId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_harvester1\",   \"public\" : true,   \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\",   \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_harvester(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :return: Harvester
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_harvester_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_harvester_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_harvester_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get harvester details  # noqa: E501

        Returns the details about a specific harvester.  If called by user who is not member of the harvester, requires `oz_harvesters_view` admin privilege.  ***Example cURL requests***  **Get harvester details** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID  {   \"harvesterId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_harvester1\",   \"public\" : true,   \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\",   \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_harvester_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :return: Harvester
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
                    " to method get_harvester" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_harvester`")  # noqa: E501

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
            '/harvesters/{id}', 'GET',
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

    def get_harvester_config(self, id, **kwargs):  # noqa: E501
        """Get harvester configuration  # noqa: E501

        Returns JSON configuration for harvester GUI plugin.  If called by user who is not member of the harvester, requires `oz_harvesters_view` admin privilege.  ***Example cURL requests***  **Get harvester details** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/config  {   \"config\" : {     \"typeMapping\": [ { \"id\": 0, \"name\": \"Type 1\" }, { \"id\": 1, \"name\": \"Type 1\" } ],     \"externalHelpLink\": \"http://example.com/some_help_page\",     \"refreshDataTimeout\": 1000   } } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_harvester_config(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :return: HarvesterGuiPluginConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_harvester_config_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_harvester_config_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_harvester_config_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get harvester configuration  # noqa: E501

        Returns JSON configuration for harvester GUI plugin.  If called by user who is not member of the harvester, requires `oz_harvesters_view` admin privilege.  ***Example cURL requests***  **Get harvester details** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/config  {   \"config\" : {     \"typeMapping\": [ { \"id\": 0, \"name\": \"Type 1\" }, { \"id\": 1, \"name\": \"Type 1\" } ],     \"externalHelpLink\": \"http://example.com/some_help_page\",     \"refreshDataTimeout\": 1000   } } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_harvester_config_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :return: HarvesterGuiPluginConfig
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
                    " to method get_harvester_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_harvester_config`")  # noqa: E501

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
            '/harvesters/{id}/gui_plugin_config', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HarvesterGuiPluginConfig',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_harvester_group(self, id, gid, **kwargs):  # noqa: E501
        """Get harvester's group details  # noqa: E501

        Returns details about a specific group in a harvester.  This operation requires `harvester_view` privilege. For administrators who do not have to be members of this harvester, `oz_groups_view` privilege is required.  ***Example cURL requests***  **Get harvester group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups/$GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_groupX\",   \"type\": \"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_harvester_group(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str gid: Group Id. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_harvester_group_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_harvester_group_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def get_harvester_group_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Get harvester's group details  # noqa: E501

        Returns details about a specific group in a harvester.  This operation requires `harvester_view` privilege. For administrators who do not have to be members of this harvester, `oz_groups_view` privilege is required.  ***Example cURL requests***  **Get harvester group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups/$GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_groupX\",   \"type\": \"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_harvester_group_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
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
                    " to method get_harvester_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_harvester_group`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `get_harvester_group`")  # noqa: E501

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
            '/harvesters/{id}/groups/{gid}', 'GET',
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

    def get_harvester_index(self, id, idx, **kwargs):  # noqa: E501
        """Get harvester index details  # noqa: E501

        Returns details about a specific index in the harvester.  For users who are members of harvester it requires `harvester_view`. For administrators who do not have to be members of this harvester, `oz_harvesters_view` privilege is required.  ***Example cURL requests***  **Get harvester space details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices/$INDEX_ID  {   \"indexId\": \"H8ez0CwDZ7JMYRWn1ipmBpgJHPXzIXj0-upGkf9tk\",   \"name\": \"My study index\"   \"guiPluginName\": \"study\"   \"schema\": \"{ \\\"mappings\\\": { \\\"properties\\\": { \\\"foo\\\": { \\\"type\\\": \\\"keyword\\\" } } } }\"   \"includeMetadata\": [\"json\", \"xattrs\"]   \"includeFileDetails\": [\"fileName\", \"metadataExistenceFlags\"]   \"includeRejectionReason\": false   \"retryOnRejection\": true } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_harvester_index(id, idx, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str idx: Index Id. (required)
        :return: HarvesterIndex
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_harvester_index_with_http_info(id, idx, **kwargs)  # noqa: E501
        else:
            (data) = self.get_harvester_index_with_http_info(id, idx, **kwargs)  # noqa: E501
            return data

    def get_harvester_index_with_http_info(self, id, idx, **kwargs):  # noqa: E501
        """Get harvester index details  # noqa: E501

        Returns details about a specific index in the harvester.  For users who are members of harvester it requires `harvester_view`. For administrators who do not have to be members of this harvester, `oz_harvesters_view` privilege is required.  ***Example cURL requests***  **Get harvester space details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices/$INDEX_ID  {   \"indexId\": \"H8ez0CwDZ7JMYRWn1ipmBpgJHPXzIXj0-upGkf9tk\",   \"name\": \"My study index\"   \"guiPluginName\": \"study\"   \"schema\": \"{ \\\"mappings\\\": { \\\"properties\\\": { \\\"foo\\\": { \\\"type\\\": \\\"keyword\\\" } } } }\"   \"includeMetadata\": [\"json\", \"xattrs\"]   \"includeFileDetails\": [\"fileName\", \"metadataExistenceFlags\"]   \"includeRejectionReason\": false   \"retryOnRejection\": true } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_harvester_index_with_http_info(id, idx, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str idx: Index Id. (required)
        :return: HarvesterIndex
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'idx']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_harvester_index" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_harvester_index`")  # noqa: E501
        # verify the required parameter 'idx' is set
        if ('idx' not in params or
                params['idx'] is None):
            raise ValueError("Missing the required parameter `idx` when calling `get_harvester_index`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'idx' in params:
            path_params['idx'] = params['idx']  # noqa: E501

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
            '/harvesters/{id}/indices/{idx}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HarvesterIndex',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_harvester_index_stats(self, id, idx, **kwargs):  # noqa: E501
        """Get harvester index stats  # noqa: E501

        Returns details about harvesting stats of a specific index in the harvester.  For users who are members of harvester it requires `harvester_view`. For administrators who do not have to be members of this harvester, `oz_harvesters_view` privilege is required.  ***Example cURL requests***  **Get harvester index stats** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices/$INDEX_ID  {   $SPACE_ID1 : {     $PROVIDER_ID1 : {       \"currentSeq\" : 5,       \"maxSeq\" : 8,       \"error\" : null,       \"lastUpdate\" : 1557928576,       \"archival\" : false     },     $PROVIDER_ID2 : {       \"currentSeq\" : 8,       \"maxSeq\" : 13,       \"error\" : \"Service unavailable: temporary failure.\",       \"lastUpdate\" : 1557928576,       \"archival\" : false     }   },   $SPACE_ID2 : {     $PROVIDER_ID1 : {       \"currentSeq\" : 13,       \"maxSeq\" : 21,       \"error\" : null,       \"lastUpdate\" : 1557928576,       \"archival\" : false     },     $PROVIDER_ID3 : {       \"currentSeq\" : 21,       \"maxSeq\" : 34,       \"error\" : null,       \"lastUpdate\" : 1557928576,       \"archival\" : true     }   } } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_harvester_index_stats(id, idx, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str idx: Index Id. (required)
        :return: HarvesterIndexStatsDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_harvester_index_stats_with_http_info(id, idx, **kwargs)  # noqa: E501
        else:
            (data) = self.get_harvester_index_stats_with_http_info(id, idx, **kwargs)  # noqa: E501
            return data

    def get_harvester_index_stats_with_http_info(self, id, idx, **kwargs):  # noqa: E501
        """Get harvester index stats  # noqa: E501

        Returns details about harvesting stats of a specific index in the harvester.  For users who are members of harvester it requires `harvester_view`. For administrators who do not have to be members of this harvester, `oz_harvesters_view` privilege is required.  ***Example cURL requests***  **Get harvester index stats** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices/$INDEX_ID  {   $SPACE_ID1 : {     $PROVIDER_ID1 : {       \"currentSeq\" : 5,       \"maxSeq\" : 8,       \"error\" : null,       \"lastUpdate\" : 1557928576,       \"archival\" : false     },     $PROVIDER_ID2 : {       \"currentSeq\" : 8,       \"maxSeq\" : 13,       \"error\" : \"Service unavailable: temporary failure.\",       \"lastUpdate\" : 1557928576,       \"archival\" : false     }   },   $SPACE_ID2 : {     $PROVIDER_ID1 : {       \"currentSeq\" : 13,       \"maxSeq\" : 21,       \"error\" : null,       \"lastUpdate\" : 1557928576,       \"archival\" : false     },     $PROVIDER_ID3 : {       \"currentSeq\" : 21,       \"maxSeq\" : 34,       \"error\" : null,       \"lastUpdate\" : 1557928576,       \"archival\" : true     }   } } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_harvester_index_stats_with_http_info(id, idx, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str idx: Index Id. (required)
        :return: HarvesterIndexStatsDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'idx']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_harvester_index_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_harvester_index_stats`")  # noqa: E501
        # verify the required parameter 'idx' is set
        if ('idx' not in params or
                params['idx'] is None):
            raise ValueError("Missing the required parameter `idx` when calling `get_harvester_index_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'idx' in params:
            path_params['idx'] = params['idx']  # noqa: E501

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
            '/harvesters/{id}/indices/{idx}/stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HarvesterIndexStatsDetails',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_harvester_space(self, id, sid, **kwargs):  # noqa: E501
        """Get harvester space details  # noqa: E501

        Returns details about a specific space in the harvester.  For users who are members of harvester it requires `harvester_view`. For administrators who do not have to be members of this harvester, `oz_spaces_view` privilege is required.  ***Example cURL requests***  **Get harvester space details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/spaces/$SPACE_ID  {   \"spaceId\": \"H8ez0CwDZ7JMYRWn1ipmBpgJHPXzIXj0-upGkf9tk\",   \"name\": \"example\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_harvester_space(id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str sid: Space Id. (required)
        :return: Space
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_harvester_space_with_http_info(id, sid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_harvester_space_with_http_info(id, sid, **kwargs)  # noqa: E501
            return data

    def get_harvester_space_with_http_info(self, id, sid, **kwargs):  # noqa: E501
        """Get harvester space details  # noqa: E501

        Returns details about a specific space in the harvester.  For users who are members of harvester it requires `harvester_view`. For administrators who do not have to be members of this harvester, `oz_spaces_view` privilege is required.  ***Example cURL requests***  **Get harvester space details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/spaces/$SPACE_ID  {   \"spaceId\": \"H8ez0CwDZ7JMYRWn1ipmBpgJHPXzIXj0-upGkf9tk\",   \"name\": \"example\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_harvester_space_with_http_info(id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
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
                    " to method get_harvester_space" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_harvester_space`")  # noqa: E501
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `get_harvester_space`")  # noqa: E501

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
            '/harvesters/{id}/spaces/{sid}', 'GET',
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

    def get_harvester_user(self, id, uid, **kwargs):  # noqa: E501
        """Get harvester user details  # noqa: E501

        Returns basic information about a specific user in a harvester.  This operation requires `harvester_view` privilege. For administrators who do not have to be members of this harvester, `oz_users_view` privilege is required.  ***Example cURL requests***  **Get harvester user data** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_harvester_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str uid: User Id. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_harvester_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_harvester_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def get_harvester_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Get harvester user details  # noqa: E501

        Returns basic information about a specific user in a harvester.  This operation requires `harvester_view` privilege. For administrators who do not have to be members of this harvester, `oz_users_view` privilege is required.  ***Example cURL requests***  **Get harvester user data** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_harvester_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
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
                    " to method get_harvester_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_harvester_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_harvester_user`")  # noqa: E501

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
            '/harvesters/{id}/users/{uid}', 'GET',
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

    def harvester_join_space(self, id, **kwargs):  # noqa: E501
        """Join harvester to a space  # noqa: E501

        Joins the harvester to an existing space based on provided `harvesterJoinSpace` invitation token (the space becomes a metadata source for the harvester).  This operation requires `harvester_add_space` privilege. For administrator who does not belong to this space `oz_harvesters_add_relationships` and `oz_spaces_add_relationships` privilege is required.  ***Example cURL requests***  **Join harvester to a space** ```bash curl -u admin:password -H \"Content-type: application/json\" \\ -d '{\"token\":\"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVuJ3l02U1JXzstRdK00ZHbso02rRcG8bJLAo\"}' \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/spaces/join ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.harvester_join_space(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param SpaceInviteToken body: harvesterJoinSpace invite token.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.harvester_join_space_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.harvester_join_space_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def harvester_join_space_with_http_info(self, id, **kwargs):  # noqa: E501
        """Join harvester to a space  # noqa: E501

        Joins the harvester to an existing space based on provided `harvesterJoinSpace` invitation token (the space becomes a metadata source for the harvester).  This operation requires `harvester_add_space` privilege. For administrator who does not belong to this space `oz_harvesters_add_relationships` and `oz_spaces_add_relationships` privilege is required.  ***Example cURL requests***  **Join harvester to a space** ```bash curl -u admin:password -H \"Content-type: application/json\" \\ -d '{\"token\":\"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVuJ3l02U1JXzstRdK00ZHbso02rRcG8bJLAo\"}' \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/spaces/join ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.harvester_join_space_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param SpaceInviteToken body: harvesterJoinSpace invite token.
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
                    " to method harvester_join_space" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `harvester_join_space`")  # noqa: E501

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
            '/harvesters/{id}/spaces/join', 'POST',
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

    def list_effective_group_harvester_privileges(self, id, gid, **kwargs):  # noqa: E501
        """List effective group's harvester privileges  # noqa: E501

        Returns the list of effective group's (`{gid}`) privileges in a harvester (`{id}`).  Effective privileges are a sum of group's privileges and privileges inherited from its parent group memberships.  This operation requires `harvester_view_privileges` privilege or `oz_harvesters_view_privileges` admin privilege.  ***Example cURL requests***  **List effective groups's privileges in a harvester** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_groups/$GROUP_ID/privileges  {   \"privileges\": [     \"harvester_view\",     \"harvester_update\",     \"harvester_delete\",     \"harvester_view_privileges\",     \"harvester_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_harvester_privileges(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str gid: Group Id. (required)
        :return: InlineResponse20018
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_group_harvester_privileges_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_group_harvester_privileges_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def list_effective_group_harvester_privileges_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """List effective group's harvester privileges  # noqa: E501

        Returns the list of effective group's (`{gid}`) privileges in a harvester (`{id}`).  Effective privileges are a sum of group's privileges and privileges inherited from its parent group memberships.  This operation requires `harvester_view_privileges` privilege or `oz_harvesters_view_privileges` admin privilege.  ***Example cURL requests***  **List effective groups's privileges in a harvester** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_groups/$GROUP_ID/privileges  {   \"privileges\": [     \"harvester_view\",     \"harvester_update\",     \"harvester_delete\",     \"harvester_view_privileges\",     \"harvester_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_harvester_privileges_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str gid: Group Id. (required)
        :return: InlineResponse20018
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
                    " to method list_effective_group_harvester_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_group_harvester_privileges`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `list_effective_group_harvester_privileges`")  # noqa: E501

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
            '/harvesters/{id}/effective_groups/{gid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20018',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_effective_harvester_groups(self, id, **kwargs):  # noqa: E501
        """List effective harvester groups  # noqa: E501

        Returns the effective list of groups belonging to a specific harvester.  This operation requires `harvester_view` privilege or `oz_harvesters_list_relationships` admin privilege.  ***Example cURL requests***  **Get harvester effective groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_groups  {   \"groups\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_harvester_groups(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :return: Groups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_harvester_groups_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_harvester_groups_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_effective_harvester_groups_with_http_info(self, id, **kwargs):  # noqa: E501
        """List effective harvester groups  # noqa: E501

        Returns the effective list of groups belonging to a specific harvester.  This operation requires `harvester_view` privilege or `oz_harvesters_list_relationships` admin privilege.  ***Example cURL requests***  **Get harvester effective groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_groups  {   \"groups\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_harvester_groups_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
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
                    " to method list_effective_harvester_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_harvester_groups`")  # noqa: E501

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
            '/harvesters/{id}/effective_groups', 'GET',
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

    def list_effective_harvester_users(self, id, **kwargs):  # noqa: E501
        """List effective harvester users  # noqa: E501

        Returns the effective list of users belonging to a specific harvester.  This operation requires `harvester_view` privilege or `oz_harvesters_list_relationships` admin privilege.  ***Example cURL requests***  **Get harvester effective users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_users  {   \"users\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_harvester_users(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_harvester_users_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_harvester_users_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_effective_harvester_users_with_http_info(self, id, **kwargs):  # noqa: E501
        """List effective harvester users  # noqa: E501

        Returns the effective list of users belonging to a specific harvester.  This operation requires `harvester_view` privilege or `oz_harvesters_list_relationships` admin privilege.  ***Example cURL requests***  **Get harvester effective users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_users  {   \"users\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_harvester_users_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
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
                    " to method list_effective_harvester_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_harvester_users`")  # noqa: E501

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
            '/harvesters/{id}/effective_users', 'GET',
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

    def list_effective_user_harvester_privileges(self, id, uid, **kwargs):  # noqa: E501
        """List effective user's harvester privileges  # noqa: E501

        Returns the list of effective user's (`{uid}`) privileges in a harvester (`{id}`).  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation requires `harvester_view_privileges` privilege or `oz_harvesters_view_privileges` admin privilege.  ***Example cURL requests***  **List effective user's privileges in a harvester** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_users/$USER_ID/privileges  {   \"privileges\": [     \"harvester_view\",     \"harvester_update\",     \"harvester_delete\",     \"harvester_view_privileges\",     \"harvester_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_user_harvester_privileges(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str uid: User Id. (required)
        :return: InlineResponse20018
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_user_harvester_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_user_harvester_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def list_effective_user_harvester_privileges_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """List effective user's harvester privileges  # noqa: E501

        Returns the list of effective user's (`{uid}`) privileges in a harvester (`{id}`).  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation requires `harvester_view_privileges` privilege or `oz_harvesters_view_privileges` admin privilege.  ***Example cURL requests***  **List effective user's privileges in a harvester** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/effective_users/$USER_ID/privileges  {   \"privileges\": [     \"harvester_view\",     \"harvester_update\",     \"harvester_delete\",     \"harvester_view_privileges\",     \"harvester_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_user_harvester_privileges_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str uid: User Id. (required)
        :return: InlineResponse20018
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
                    " to method list_effective_user_harvester_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_user_harvester_privileges`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `list_effective_user_harvester_privileges`")  # noqa: E501

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
            '/harvesters/{id}/effective_users/{uid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20018',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_group_harvester_privileges(self, id, gid, **kwargs):  # noqa: E501
        """List group's harvester privileges  # noqa: E501

        Returns the list of group's (`{gid}`) privileges in a harvester (`{id}`).  This operation requires `harvester_view_privileges` privilege or `oz_harvesters_view_privileges` admin privilege.  ***Example cURL requests***  **List groups's privileges in a harvester** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups/$GROUP_ID/privileges  {   \"privileges\": [     \"harvester_view\",     \"harvester_update\",     \"harvester_delete\",     \"harvester_view_privileges\",     \"harvester_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_harvester_privileges(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str gid: Group Id. (required)
        :return: InlineResponse20018
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_group_harvester_privileges_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_group_harvester_privileges_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def list_group_harvester_privileges_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """List group's harvester privileges  # noqa: E501

        Returns the list of group's (`{gid}`) privileges in a harvester (`{id}`).  This operation requires `harvester_view_privileges` privilege or `oz_harvesters_view_privileges` admin privilege.  ***Example cURL requests***  **List groups's privileges in a harvester** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups/$GROUP_ID/privileges  {   \"privileges\": [     \"harvester_view\",     \"harvester_update\",     \"harvester_delete\",     \"harvester_view_privileges\",     \"harvester_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_harvester_privileges_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str gid: Group Id. (required)
        :return: InlineResponse20018
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
                    " to method list_group_harvester_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_group_harvester_privileges`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `list_group_harvester_privileges`")  # noqa: E501

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
            '/harvesters/{id}/groups/{gid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20018',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_harvester_groups(self, id, **kwargs):  # noqa: E501
        """List harvester groups  # noqa: E501

        Returns the list of groups belonging to a specific harvester.  This operation requires `harvester_view` privilege in the harvester.  For administrator who does not belong to the harvester, `oz_harvesters_list_relationships` privilege is required.  ***Example cURL requests***  **Get harvester groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups  {   \"groups\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_harvester_groups(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :return: Groups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_harvester_groups_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_harvester_groups_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_harvester_groups_with_http_info(self, id, **kwargs):  # noqa: E501
        """List harvester groups  # noqa: E501

        Returns the list of groups belonging to a specific harvester.  This operation requires `harvester_view` privilege in the harvester.  For administrator who does not belong to the harvester, `oz_harvesters_list_relationships` privilege is required.  ***Example cURL requests***  **Get harvester groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups  {   \"groups\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_harvester_groups_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
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
                    " to method list_harvester_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_harvester_groups`")  # noqa: E501

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
            '/harvesters/{id}/groups', 'GET',
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

    def list_harvester_indices(self, id, **kwargs):  # noqa: E501
        """List harvester indices  # noqa: E501

        Returns the list of indices in specific harvester.  For users who are members of harvester it requires `harvester_view`.  For administrators who do not have to be members of this harvester, `oz_harvesters_view` privilege is required.  ***Example cURL requests***  **Get harvester index** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices  {   \"indices\": [     \"MDAxNmxvYZjUGlIcGkweGZta1ZOdEp00eUNINVNvR2001Wl\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_harvester_indices(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :return: HarvesterIndices
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_harvester_indices_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_harvester_indices_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_harvester_indices_with_http_info(self, id, **kwargs):  # noqa: E501
        """List harvester indices  # noqa: E501

        Returns the list of indices in specific harvester.  For users who are members of harvester it requires `harvester_view`.  For administrators who do not have to be members of this harvester, `oz_harvesters_view` privilege is required.  ***Example cURL requests***  **Get harvester index** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices  {   \"indices\": [     \"MDAxNmxvYZjUGlIcGkweGZta1ZOdEp00eUNINVNvR2001Wl\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_harvester_indices_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :return: HarvesterIndices
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
                    " to method list_harvester_indices" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_harvester_indices`")  # noqa: E501

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
            '/harvesters/{id}/indices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HarvesterIndices',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_harvester_privileges(self, **kwargs):  # noqa: E501
        """List all harvester privileges  # noqa: E501

        Returns list of all possible harvester privileges.  This endpoint does not require authentication.  ***Example cURL requests***  **Get list of all harvester privileges** ```bash curl https://$ZONE_HOST/api/v3/onezone/harvesters/privileges  {   \"admin\": [     \"harvester_view\",     \"harvester_update\",     \"harvester_delete\",     \"harvester_view_privileges\",     \"harvester_set_privileges\",     \"harvester_add_user\",     \"harvester_remove_user\",     \"harvester_add_group\",     \"harvester_remove_group\",     \"harvester_add_space\",     \"harvester_remove_space\"   ],   \"manager\": [     \"harvester_view\",     \"harvester_add_user\",     \"harvester_remove_user\",     \"harvester_add_group\",     \"harvester_remove_group\",     \"harvester_add_space\",     \"harvester_remove_space\"   ],   \"member\": [     \"harvester_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_harvester_privileges(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20017
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_harvester_privileges_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_harvester_privileges_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_harvester_privileges_with_http_info(self, **kwargs):  # noqa: E501
        """List all harvester privileges  # noqa: E501

        Returns list of all possible harvester privileges.  This endpoint does not require authentication.  ***Example cURL requests***  **Get list of all harvester privileges** ```bash curl https://$ZONE_HOST/api/v3/onezone/harvesters/privileges  {   \"admin\": [     \"harvester_view\",     \"harvester_update\",     \"harvester_delete\",     \"harvester_view_privileges\",     \"harvester_set_privileges\",     \"harvester_add_user\",     \"harvester_remove_user\",     \"harvester_add_group\",     \"harvester_remove_group\",     \"harvester_add_space\",     \"harvester_remove_space\"   ],   \"manager\": [     \"harvester_view\",     \"harvester_add_user\",     \"harvester_remove_user\",     \"harvester_add_group\",     \"harvester_remove_group\",     \"harvester_add_space\",     \"harvester_remove_space\"   ],   \"member\": [     \"harvester_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_harvester_privileges_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20017
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
                    " to method list_harvester_privileges" % key
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
            '/harvesters/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20017',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_harvester_spaces(self, id, **kwargs):  # noqa: E501
        """List harvester spaces  # noqa: E501

        Returns the list of spaces in specific harvester.  For users who are members of harvester it requires `harvester_view`.  For administrators who do not have to be members of this harvester, `oz_harvesters_list_relationships` privilege is required.  ***Example cURL requests***  **List harvester spaces** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/spaces  {   \"spaces\": [     \"MDAxNmxvYZjUGlIcGkweGZta1ZOdEp00eUNINVNvR2001Wl\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_harvester_spaces(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :return: Spaces
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_harvester_spaces_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_harvester_spaces_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_harvester_spaces_with_http_info(self, id, **kwargs):  # noqa: E501
        """List harvester spaces  # noqa: E501

        Returns the list of spaces in specific harvester.  For users who are members of harvester it requires `harvester_view`.  For administrators who do not have to be members of this harvester, `oz_harvesters_list_relationships` privilege is required.  ***Example cURL requests***  **List harvester spaces** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/spaces  {   \"spaces\": [     \"MDAxNmxvYZjUGlIcGkweGZta1ZOdEp00eUNINVNvR2001Wl\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_harvester_spaces_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
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
                    " to method list_harvester_spaces" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_harvester_spaces`")  # noqa: E501

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
            '/harvesters/{id}/spaces', 'GET',
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

    def list_harvester_users(self, id, **kwargs):  # noqa: E501
        """List harvester users  # noqa: E501

        Returns the list of users belonging to a specific harvester.  This operation requires `harvester_view` privilege. For administrators who do not have to be members of this harvester, `oz_harvesters_list_relationships` privilege is required.  ***Example cURL requests***  **Get harvester users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/users  {   \"users\": [     \"a5b469a2b0516b662a49da74d6d7d7bc\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_harvester_users(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_harvester_users_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_harvester_users_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_harvester_users_with_http_info(self, id, **kwargs):  # noqa: E501
        """List harvester users  # noqa: E501

        Returns the list of users belonging to a specific harvester.  This operation requires `harvester_view` privilege. For administrators who do not have to be members of this harvester, `oz_harvesters_list_relationships` privilege is required.  ***Example cURL requests***  **Get harvester users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/users  {   \"users\": [     \"a5b469a2b0516b662a49da74d6d7d7bc\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_harvester_users_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
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
                    " to method list_harvester_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_harvester_users`")  # noqa: E501

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
            '/harvesters/{id}/users', 'GET',
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

    def list_user_harvester_privileges(self, id, uid, **kwargs):  # noqa: E501
        """List user's harvester privileges  # noqa: E501

        Returns the list of user's (`{uid}`) privileges in a harvester (`{id}`).  This operation requires `harvester_view_privileges` privilege. For administrators who do not have to be members of this harvester, `oz_harvesters_view_privileges` privilege is required.  ***Example cURL requests***  **List user's privileges in a harvester** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/users/$USER_ID/privileges  {   \"privileges\": [     \"harvester_view\",     \"harvester_update\",     \"harvester_delete\",     \"harvester_view_privileges\",     \"harvester_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_harvester_privileges(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str uid: User Id. (required)
        :return: InlineResponse20018
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_harvester_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_user_harvester_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def list_user_harvester_privileges_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """List user's harvester privileges  # noqa: E501

        Returns the list of user's (`{uid}`) privileges in a harvester (`{id}`).  This operation requires `harvester_view_privileges` privilege. For administrators who do not have to be members of this harvester, `oz_harvesters_view_privileges` privilege is required.  ***Example cURL requests***  **List user's privileges in a harvester** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/users/$USER_ID/privileges  {   \"privileges\": [     \"harvester_view\",     \"harvester_update\",     \"harvester_delete\",     \"harvester_view_privileges\",     \"harvester_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_harvester_privileges_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str uid: User Id. (required)
        :return: InlineResponse20018
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
                    " to method list_user_harvester_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_user_harvester_privileges`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `list_user_harvester_privileges`")  # noqa: E501

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
            '/harvesters/{id}/users/{uid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20018',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_harvester(self, body, id, **kwargs):  # noqa: E501
        """Modify harvester details  # noqa: E501

        Updates the details about a harvester.  This operation requires `harvester_update` privilege or `oz_harvesters_update` admin privilege.  ***Example cURL requests***  **Change harvester name** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"name\": \"new_harvester12\"}' \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_harvester(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HarvesterUpdateRequest body: Harvester parameters (required)
        :param str id: Harvester Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_harvester_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_harvester_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def modify_harvester_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Modify harvester details  # noqa: E501

        Updates the details about a harvester.  This operation requires `harvester_update` privilege or `oz_harvesters_update` admin privilege.  ***Example cURL requests***  **Change harvester name** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"name\": \"new_harvester12\"}' \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_harvester_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HarvesterUpdateRequest body: Harvester parameters (required)
        :param str id: Harvester Id. (required)
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
                    " to method modify_harvester" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `modify_harvester`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `modify_harvester`")  # noqa: E501

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
            '/harvesters/{id}', 'PATCH',
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

    def modify_harvester_config(self, body, id, **kwargs):  # noqa: E501
        """Modify harvester configuration  # noqa: E501

        Updates harvester GUI plugin configuration.  This operation requires `harvester_update` privilege or `oz_harvesters_update` admin privilege.  ***Example cURL requests***  **Change harvester name** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"config\": {}}' \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/config ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_harvester_config(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HarvesterGuiPluginConfig body: New harvester config (required)
        :param str id: Harvester Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_harvester_config_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_harvester_config_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def modify_harvester_config_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Modify harvester configuration  # noqa: E501

        Updates harvester GUI plugin configuration.  This operation requires `harvester_update` privilege or `oz_harvesters_update` admin privilege.  ***Example cURL requests***  **Change harvester name** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"config\": {}}' \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/config ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_harvester_config_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HarvesterGuiPluginConfig body: New harvester config (required)
        :param str id: Harvester Id. (required)
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
                    " to method modify_harvester_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `modify_harvester_config`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `modify_harvester_config`")  # noqa: E501

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
            '/harvesters/{id}/gui_plugin_config', 'PATCH',
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

    def modify_harvester_index(self, body, id, idx, **kwargs):  # noqa: E501
        """Modify harvester index  # noqa: E501

        Modifies harvester index.  This operation requires `harvester_update` privilege or `oz_harvesters_update` admin privilege.  ***Example cURL requests***  **Change harvester name** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"name\" : \"new_name\", \"guiPluginName\" : \"new_gui_plugin_name\"}' \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices/$INDEX_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_harvester_index(body, id, idx, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IndicesIdxBody body: The new data of the index. (required)
        :param str id: Harvester Id. (required)
        :param str idx: Index Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_harvester_index_with_http_info(body, id, idx, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_harvester_index_with_http_info(body, id, idx, **kwargs)  # noqa: E501
            return data

    def modify_harvester_index_with_http_info(self, body, id, idx, **kwargs):  # noqa: E501
        """Modify harvester index  # noqa: E501

        Modifies harvester index.  This operation requires `harvester_update` privilege or `oz_harvesters_update` admin privilege.  ***Example cURL requests***  **Change harvester name** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"name\" : \"new_name\", \"guiPluginName\" : \"new_gui_plugin_name\"}' \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices/$INDEX_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_harvester_index_with_http_info(body, id, idx, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IndicesIdxBody body: The new data of the index. (required)
        :param str id: Harvester Id. (required)
        :param str idx: Index Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id', 'idx']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_harvester_index" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `modify_harvester_index`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `modify_harvester_index`")  # noqa: E501
        # verify the required parameter 'idx' is set
        if ('idx' not in params or
                params['idx'] is None):
            raise ValueError("Missing the required parameter `idx` when calling `modify_harvester_index`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'idx' in params:
            path_params['idx'] = params['idx']  # noqa: E501

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
            '/harvesters/{id}/indices/{idx}', 'PATCH',
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

    def oz_harvesters_list(self, **kwargs):  # noqa: E501
        """List all harvesters  # noqa: E501

        Returns the list of all harvesters managed by the Onezone service.  This operation requires `oz_harvesters_list` admin privilege.  ***Example cURL requests***  **List all harvesters** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters  {   \"harvesters\": [     \"S0Y9FSe9TFJFFzzLtBEs8\",     \"IkHBv8CoAFmbFU4fj26\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oz_harvesters_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Harvesters
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.oz_harvesters_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.oz_harvesters_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def oz_harvesters_list_with_http_info(self, **kwargs):  # noqa: E501
        """List all harvesters  # noqa: E501

        Returns the list of all harvesters managed by the Onezone service.  This operation requires `oz_harvesters_list` admin privilege.  ***Example cURL requests***  **List all harvesters** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/harvesters  {   \"harvesters\": [     \"S0Y9FSe9TFJFFzzLtBEs8\",     \"IkHBv8CoAFmbFU4fj26\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oz_harvesters_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Harvesters
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
                    " to method oz_harvesters_list" % key
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
            '/harvesters', 'GET',
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

    def query_harvester_index(self, body, id, idx, **kwargs):  # noqa: E501
        """Query harvester index  # noqa: E501

        Performs query to index {idx} in harvester {id}.  This operation does not require any privileges when the harvester is public  otherwise being member of the harvester is required. For administrators who do not have to be members of this harvester, `oz_harvesters_view` privilege is required.  Request body and response depend on selected `harvester_plugin`. Below examples are for `elasticsearch_plugin`.  ***Example cURL requests***  **query harvester index** ```bash curl -u username:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"method\" : \"get\", \"path\" : \"resource_id\"}'  https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices/$INDEX_ID/query ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_harvester_index(body, id, idx, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HarvesterQuery body: (required)
        :param str id: Harvester Id. (required)
        :param str idx: Index Id. (required)
        :return: HarvesterQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.query_harvester_index_with_http_info(body, id, idx, **kwargs)  # noqa: E501
        else:
            (data) = self.query_harvester_index_with_http_info(body, id, idx, **kwargs)  # noqa: E501
            return data

    def query_harvester_index_with_http_info(self, body, id, idx, **kwargs):  # noqa: E501
        """Query harvester index  # noqa: E501

        Performs query to index {idx} in harvester {id}.  This operation does not require any privileges when the harvester is public  otherwise being member of the harvester is required. For administrators who do not have to be members of this harvester, `oz_harvesters_view` privilege is required.  Request body and response depend on selected `harvester_plugin`. Below examples are for `elasticsearch_plugin`.  ***Example cURL requests***  **query harvester index** ```bash curl -u username:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"method\" : \"get\", \"path\" : \"resource_id\"}'  https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices/$INDEX_ID/query ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_harvester_index_with_http_info(body, id, idx, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HarvesterQuery body: (required)
        :param str id: Harvester Id. (required)
        :param str idx: Index Id. (required)
        :return: HarvesterQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id', 'idx']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_harvester_index" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `query_harvester_index`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `query_harvester_index`")  # noqa: E501
        # verify the required parameter 'idx' is set
        if ('idx' not in params or
                params['idx'] is None):
            raise ValueError("Missing the required parameter `idx` when calling `query_harvester_index`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'idx' in params:
            path_params['idx'] = params['idx']  # noqa: E501

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
            '/harvesters/{id}/indices/{idx}/query', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HarvesterQueryResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_harvested_index_metadata(self, id, idx, **kwargs):  # noqa: E501
        """Remove harvested index metadata  # noqa: E501

        Schedules removal of all harvested metadata in given index.\\ See also: [Remove index](#operation/remove_harvester_index)  This operation requires `harvester_update` privilege or `oz_harvesters_update` admin privilege.  ***Example cURL requests***  **Remove harvested index metadata** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices/$INDEX_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_harvested_index_metadata(id, idx, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str idx: Index Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_harvested_index_metadata_with_http_info(id, idx, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_harvested_index_metadata_with_http_info(id, idx, **kwargs)  # noqa: E501
            return data

    def remove_harvested_index_metadata_with_http_info(self, id, idx, **kwargs):  # noqa: E501
        """Remove harvested index metadata  # noqa: E501

        Schedules removal of all harvested metadata in given index.\\ See also: [Remove index](#operation/remove_harvester_index)  This operation requires `harvester_update` privilege or `oz_harvesters_update` admin privilege.  ***Example cURL requests***  **Remove harvested index metadata** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices/$INDEX_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_harvested_index_metadata_with_http_info(id, idx, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str idx: Index Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'idx']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_harvested_index_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_harvested_index_metadata`")  # noqa: E501
        # verify the required parameter 'idx' is set
        if ('idx' not in params or
                params['idx'] is None):
            raise ValueError("Missing the required parameter `idx` when calling `remove_harvested_index_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'idx' in params:
            path_params['idx'] = params['idx']  # noqa: E501

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
            '/harvesters/{id}/indices/{idx}/metadata', 'DELETE',
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

    def remove_harvested_metadata(self, id, **kwargs):  # noqa: E501
        """Remove harvested metadata  # noqa: E501

        Schedules removal of harvested metadata in all indices in given harvester.\\ See also: [Remove harvester](#operation/remove_harvester)  This operation requires `harvester_delete` privilege or `oz_harvesters_delete` admin privilege.  ***Example cURL requests***  **Remove harvested metadata** ```bash curl -u admin:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_harvested_metadata(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_harvested_metadata_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_harvested_metadata_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def remove_harvested_metadata_with_http_info(self, id, **kwargs):  # noqa: E501
        """Remove harvested metadata  # noqa: E501

        Schedules removal of harvested metadata in all indices in given harvester.\\ See also: [Remove harvester](#operation/remove_harvester)  This operation requires `harvester_delete` privilege or `oz_harvesters_delete` admin privilege.  ***Example cURL requests***  **Remove harvested metadata** ```bash curl -u admin:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_harvested_metadata_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
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
                    " to method remove_harvested_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_harvested_metadata`")  # noqa: E501

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
            '/harvesters/{id}/metadata', 'DELETE',
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

    def remove_harvester(self, id, **kwargs):  # noqa: E501
        """Remove harvester  # noqa: E501

        Removes a specific harvester. **It will be no longer possible to access harvested data through onezone service**.\\ If you wish to remove harvested metadata see:  [Remove harvested data](#operation/remove_harvested_data)  This operation requires `harvester_delete` privilege or `oz_harvesters_delete` admin privilege.  ***Example cURL requests***  **Remove harvester** ```bash curl -u admin:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_harvester(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_harvester_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_harvester_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def remove_harvester_with_http_info(self, id, **kwargs):  # noqa: E501
        """Remove harvester  # noqa: E501

        Removes a specific harvester. **It will be no longer possible to access harvested data through onezone service**.\\ If you wish to remove harvested metadata see:  [Remove harvested data](#operation/remove_harvested_data)  This operation requires `harvester_delete` privilege or `oz_harvesters_delete` admin privilege.  ***Example cURL requests***  **Remove harvester** ```bash curl -u admin:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_harvester_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
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
                    " to method remove_harvester" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_harvester`")  # noqa: E501

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
            '/harvesters/{id}', 'DELETE',
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

    def remove_harvester_group(self, id, gid, **kwargs):  # noqa: E501
        """Remove group from harvester  # noqa: E501

        Removes a specific group from harvester.  For regular users, who belong to this harvester it requires `harvester_remove_group` privilege to remove a group from this harvester.  For administrators, who are not members of this harvester, `oz_harvesters_remove_relationships` privilege is required.  ***Example cURL requests***  **Get harvester group details** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_harvester_group(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str gid: Group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_harvester_group_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_harvester_group_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def remove_harvester_group_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Remove group from harvester  # noqa: E501

        Removes a specific group from harvester.  For regular users, who belong to this harvester it requires `harvester_remove_group` privilege to remove a group from this harvester.  For administrators, who are not members of this harvester, `oz_harvesters_remove_relationships` privilege is required.  ***Example cURL requests***  **Get harvester group details** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_harvester_group_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
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
                    " to method remove_harvester_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_harvester_group`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `remove_harvester_group`")  # noqa: E501

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
            '/harvesters/{id}/groups/{gid}', 'DELETE',
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

    def remove_harvester_index(self, id, idx, **kwargs):  # noqa: E501
        """Remove harvester index  # noqa: E501

        Removes index from a specific harvester. **It will be no longer possible to access harvested data through onezone service**.\\ If you wish to remove harvested metadata see: [Remove harvested metadata in index](#operation/remove_harvested_index_data)  This operation requires `harvester_update` privilege or `oz_harvesters_update` admin privilege.  ***Example cURL requests***  **Remove harvester index** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices/$INDEX_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_harvester_index(id, idx, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str idx: Index Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_harvester_index_with_http_info(id, idx, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_harvester_index_with_http_info(id, idx, **kwargs)  # noqa: E501
            return data

    def remove_harvester_index_with_http_info(self, id, idx, **kwargs):  # noqa: E501
        """Remove harvester index  # noqa: E501

        Removes index from a specific harvester. **It will be no longer possible to access harvested data through onezone service**.\\ If you wish to remove harvested metadata see: [Remove harvested metadata in index](#operation/remove_harvested_index_data)  This operation requires `harvester_update` privilege or `oz_harvesters_update` admin privilege.  ***Example cURL requests***  **Remove harvester index** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/indices/$INDEX_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_harvester_index_with_http_info(id, idx, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str idx: Index Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'idx']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_harvester_index" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_harvester_index`")  # noqa: E501
        # verify the required parameter 'idx' is set
        if ('idx' not in params or
                params['idx'] is None):
            raise ValueError("Missing the required parameter `idx` when calling `remove_harvester_index`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'idx' in params:
            path_params['idx'] = params['idx']  # noqa: E501

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
            '/harvesters/{id}/indices/{idx}', 'DELETE',
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

    def remove_harvester_space(self, id, sid, **kwargs):  # noqa: E501
        """Remove harvester space  # noqa: E501

        Removes space from a specific harvester.  This operation requires `harvester_remove_space` privilege or `oz_harvesters_remove_relationships` admin privilege.  ***Example cURL requests***  **Remove harvester space** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/spaces/$SPACE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_harvester_space(id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str sid: Space Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_harvester_space_with_http_info(id, sid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_harvester_space_with_http_info(id, sid, **kwargs)  # noqa: E501
            return data

    def remove_harvester_space_with_http_info(self, id, sid, **kwargs):  # noqa: E501
        """Remove harvester space  # noqa: E501

        Removes space from a specific harvester.  This operation requires `harvester_remove_space` privilege or `oz_harvesters_remove_relationships` admin privilege.  ***Example cURL requests***  **Remove harvester space** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/spaces/$SPACE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_harvester_space_with_http_info(id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
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
                    " to method remove_harvester_space" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_harvester_space`")  # noqa: E501
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `remove_harvester_space`")  # noqa: E501

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
            '/harvesters/{id}/spaces/{sid}', 'DELETE',
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

    def remove_harvester_user(self, id, uid, **kwargs):  # noqa: E501
        """Remove user from harvester  # noqa: E501

        Removes user from specific harvester.  This operation requires `harvester_remove_user` or requires `oz_harvesters_add_relationships` and `oz_users_add_relationships` admin privilege.  ***Example cURL requests***  **Get harvester user data** ```bash curl -u admin:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_harvester_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
        :param str uid: User Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_harvester_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_harvester_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def remove_harvester_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Remove user from harvester  # noqa: E501

        Removes user from specific harvester.  This operation requires `harvester_remove_user` or requires `oz_harvesters_add_relationships` and `oz_users_add_relationships` admin privilege.  ***Example cURL requests***  **Get harvester user data** ```bash curl -u admin:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_harvester_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Harvester Id. (required)
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
                    " to method remove_harvester_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_harvester_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `remove_harvester_user`")  # noqa: E501

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
            '/harvesters/{id}/users/{uid}', 'DELETE',
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

    def update_group_harvester_privileges(self, body, id, gid, **kwargs):  # noqa: E501
        """Update group privileges to harvester  # noqa: E501

        Updates group's (`{gid}`) privileges in a harvester (`{id}`).  This operation requires `harvester_set_privileges` privilege or `oz_harvesters_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update group's privileges in a harvester** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"harvester_view\", \"harvester_update\"], \"revoke\": [\"harvester_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups/$GROUP_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_group_harvester_privileges(body, id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HarvesterPrivilegesUpdate body: Harvester privileges update request. (required)
        :param str id: Harvester Id. (required)
        :param str gid: Group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_group_harvester_privileges_with_http_info(body, id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_group_harvester_privileges_with_http_info(body, id, gid, **kwargs)  # noqa: E501
            return data

    def update_group_harvester_privileges_with_http_info(self, body, id, gid, **kwargs):  # noqa: E501
        """Update group privileges to harvester  # noqa: E501

        Updates group's (`{gid}`) privileges in a harvester (`{id}`).  This operation requires `harvester_set_privileges` privilege or `oz_harvesters_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update group's privileges in a harvester** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"harvester_view\", \"harvester_update\"], \"revoke\": [\"harvester_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/groups/$GROUP_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_group_harvester_privileges_with_http_info(body, id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HarvesterPrivilegesUpdate body: Harvester privileges update request. (required)
        :param str id: Harvester Id. (required)
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
                    " to method update_group_harvester_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_group_harvester_privileges`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_group_harvester_privileges`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `update_group_harvester_privileges`")  # noqa: E501

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
            '/harvesters/{id}/groups/{gid}/privileges', 'PATCH',
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

    def update_user_harvester_privileges(self, body, id, uid, **kwargs):  # noqa: E501
        """Update user's harvester privileges  # noqa: E501

        Updates user's (`{uid}`) privileges in a harvester (`{id}`).  This operation requires `harvester_set_privileges` privilege. For administrators who do not have to be members of this harvester, `oz_harvesters_set_privileges` privilege is required.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update user's privileges in a harvester** ```bash curl -u admin:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"harvester_view\", \"harvester_update\"], \"revoke\": [\"harvester_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/users/$USER_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_harvester_privileges(body, id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HarvesterPrivilegesUpdate body: Harvester privileges update request. (required)
        :param str id: Harvester Id. (required)
        :param str uid: User Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_user_harvester_privileges_with_http_info(body, id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_user_harvester_privileges_with_http_info(body, id, uid, **kwargs)  # noqa: E501
            return data

    def update_user_harvester_privileges_with_http_info(self, body, id, uid, **kwargs):  # noqa: E501
        """Update user's harvester privileges  # noqa: E501

        Updates user's (`{uid}`) privileges in a harvester (`{id}`).  This operation requires `harvester_set_privileges` privilege. For administrators who do not have to be members of this harvester, `oz_harvesters_set_privileges` privilege is required.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update user's privileges in a harvester** ```bash curl -u admin:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"harvester_view\", \"harvester_update\"], \"revoke\": [\"harvester_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/harvesters/$HARVESTER_ID/users/$USER_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_harvester_privileges_with_http_info(body, id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HarvesterPrivilegesUpdate body: Harvester privileges update request. (required)
        :param str id: Harvester Id. (required)
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
                    " to method update_user_harvester_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_user_harvester_privileges`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_user_harvester_privileges`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `update_user_harvester_privileges`")  # noqa: E501

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
            '/harvesters/{id}/users/{uid}/privileges', 'PATCH',
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
