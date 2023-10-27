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


class ClusterApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_cluster_user(self, id, uid, **kwargs):  # noqa: E501
        """Add user to cluster  # noqa: E501

        Adds user {uid} as member of cluster {id}. Optionally, privileges can be passed in the request body, otherwise default privileges will be set for the user in this cluster.  This operation can only be invoked by the user {uid} to add himself to the cluster (if he is not a member already) and requires `cluster_add_user` privilege in the cluster. If `privileges` are specified in the request, `cluster_set_privileges` privilege is also required.  Administrators having the `oz_clusters_add_relationships` and `oz_users_add_relationships` admin privileges can add any user to any cluster, though `oz_clusters_set_privileges` privilege is required if `privileges` are specified in the request.  ***Example cURL requests***  **Add user to cluster** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_cluster_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :param str uid: User Id. (required)
        :param UsersUidBody5 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_cluster_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.add_cluster_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def add_cluster_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Add user to cluster  # noqa: E501

        Adds user {uid} as member of cluster {id}. Optionally, privileges can be passed in the request body, otherwise default privileges will be set for the user in this cluster.  This operation can only be invoked by the user {uid} to add himself to the cluster (if he is not a member already) and requires `cluster_add_user` privilege in the cluster. If `privileges` are specified in the request, `cluster_set_privileges` privilege is also required.  Administrators having the `oz_clusters_add_relationships` and `oz_users_add_relationships` admin privileges can add any user to any cluster, though `oz_clusters_set_privileges` privilege is required if `privileges` are specified in the request.  ***Example cURL requests***  **Add user to cluster** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_cluster_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :param str uid: User Id. (required)
        :param UsersUidBody5 body:
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
                    " to method add_cluster_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_cluster_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `add_cluster_user`")  # noqa: E501

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
            '/clusters/{id}/users/{uid}', 'PUT',
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

    def add_group_to_cluster(self, id, gid, **kwargs):  # noqa: E501
        """Add group to cluster  # noqa: E501

        Adds group {gid} as member of cluster {id}. Optionally, privileges can be passed in the request body, otherwise default privileges will be set for the group in this cluster.  This operation requires `cluster_add_group` privilege in the cluster and `group_add_cluster` privilege in the group. If `privileges` are specified in the request, `cluster_set_privileges` privilege is also required.  For administrator who does not belong to the group / cluster, `oz_groups_add_relationships` and `oz_clusters_add_relationships` privileges are required, and `oz_clusters_set_privileges` if `privileges` are specified in the request.  ***Example cURL requests***  **Add group to cluster** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\  https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_group_to_cluster(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :param str gid: Group Id. (required)
        :param GroupsGidBody4 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_group_to_cluster_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.add_group_to_cluster_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def add_group_to_cluster_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Add group to cluster  # noqa: E501

        Adds group {gid} as member of cluster {id}. Optionally, privileges can be passed in the request body, otherwise default privileges will be set for the group in this cluster.  This operation requires `cluster_add_group` privilege in the cluster and `group_add_cluster` privilege in the group. If `privileges` are specified in the request, `cluster_set_privileges` privilege is also required.  For administrator who does not belong to the group / cluster, `oz_groups_add_relationships` and `oz_clusters_add_relationships` privileges are required, and `oz_clusters_set_privileges` if `privileges` are specified in the request.  ***Example cURL requests***  **Add group to cluster** ```bash curl -u username:password -H \"Content-type: application/json\" -X PUT \\  https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_group_to_cluster_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :param str gid: Group Id. (required)
        :param GroupsGidBody4 body:
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
                    " to method add_group_to_cluster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_group_to_cluster`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `add_group_to_cluster`")  # noqa: E501

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
            '/clusters/{id}/groups/{gid}', 'PUT',
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

    def create_cluster_group(self, body, id, **kwargs):  # noqa: E501
        """Create group in cluster  # noqa: E501

        Creates a new group belonging to the cluster of {id}.  This operation requires `cluster_add_group` privilege. For administrator who does not belong to this group `oz_clusters_add_relationships` and `oz_groups_create` privileges are required.  ***Example cURL requests***  **Create group in cluster** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_cluster_group(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupCreateRequest body: Group properties. (required)
        :param str id: Cluster Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_cluster_group_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_cluster_group_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def create_cluster_group_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Create group in cluster  # noqa: E501

        Creates a new group belonging to the cluster of {id}.  This operation requires `cluster_add_group` privilege. For administrator who does not belong to this group `oz_clusters_add_relationships` and `oz_groups_create` privileges are required.  ***Example cURL requests***  **Create group in cluster** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_cluster_group_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupCreateRequest body: Group properties. (required)
        :param str id: Cluster Id. (required)
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
                    " to method create_cluster_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_cluster_group`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_cluster_group`")  # noqa: E501

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
            '/clusters/{id}/groups', 'POST',
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

    def create_cluster_group_invite_token(self, id, **kwargs):  # noqa: E501
        """Create cluster invite token for group  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token allowing to add a group to a specific cluster.  This operation requires `cluster_add_group` privilege or `oz_clusters_add_relationships` admin privilege.  ***Example cURL requests***  **Create cluster invitation token for group** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups/token  {   \"token\": \"MDAxNmxvY0cGUgKWsjcpnrLE00RtOd2F00cGUgKWsjcpnrLE00RtOdhmnQycSICwMsugo\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_cluster_group_invite_token(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :return: ClusterInviteToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_cluster_group_invite_token_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_cluster_group_invite_token_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def create_cluster_group_invite_token_with_http_info(self, id, **kwargs):  # noqa: E501
        """Create cluster invite token for group  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token allowing to add a group to a specific cluster.  This operation requires `cluster_add_group` privilege or `oz_clusters_add_relationships` admin privilege.  ***Example cURL requests***  **Create cluster invitation token for group** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups/token  {   \"token\": \"MDAxNmxvY0cGUgKWsjcpnrLE00RtOd2F00cGUgKWsjcpnrLE00RtOdhmnQycSICwMsugo\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_cluster_group_invite_token_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :return: ClusterInviteToken
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
                    " to method create_cluster_group_invite_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_cluster_group_invite_token`")  # noqa: E501

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
            '/clusters/{id}/groups/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClusterInviteToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_cluster_user_invite_token(self, id, **kwargs):  # noqa: E501
        """Create cluster user invite token  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token allowing new user to join a cluster.  This operation requires `cluster_add_user` privilege. For administrators who do not have to be members of this cluster, `oz_clusters_add_relationships` privilege is required.  ***Example cURL requests***  **Create cluster user invite token** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/users/token  {   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaWVyIG00zcEJ2UDVuOHhkQUNhdk9hbTlyNnIwNldPSzVhc\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_cluster_user_invite_token(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :return: ClusterInviteToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_cluster_user_invite_token_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_cluster_user_invite_token_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def create_cluster_user_invite_token_with_http_info(self, id, **kwargs):  # noqa: E501
        """Create cluster user invite token  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token allowing new user to join a cluster.  This operation requires `cluster_add_user` privilege. For administrators who do not have to be members of this cluster, `oz_clusters_add_relationships` privilege is required.  ***Example cURL requests***  **Create cluster user invite token** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/users/token  {   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaWVyIG00zcEJ2UDVuOHhkQUNhdk9hbTlyNnIwNldPSzVhc\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_cluster_user_invite_token_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :return: ClusterInviteToken
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
                    " to method create_cluster_user_invite_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_cluster_user_invite_token`")  # noqa: E501

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
            '/clusters/{id}/users/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClusterInviteToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_cluster(self, id, **kwargs):  # noqa: E501
        """Get cluster details  # noqa: E501

        Returns the details about a specific cluster.  This operation requires membership in the cluster or `oz_clusters_view` admin privilege.  ***Example cURL requests***  **Get cluster details** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID  {   \"clusterId\": \"f8d843beda24e54545455ecc0f4b8886\",   \"type\": \"oneprovider\",   \"workerVersion\": {     \"release\": \"21.02.3\",     \"build\": \"1-gfabf02d\",     \"gui\": \"129c549fbe9b3e730c3d9910492228566e39e1236945766a74381405cc57fb04\"   },   \"onepanelVersion\": {     \"release\": \"21.02.3\",     \"build\": \"3-89fc6bad\",     \"gui\": \"68e7e1472adb719ddf2d88908775091dfb10e5d0b916f06125ea1af4056044e3\"   },   \"online\": true,   \"onepanelProxy\": false,   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cluster(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :return: Cluster
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_cluster_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cluster_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_cluster_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get cluster details  # noqa: E501

        Returns the details about a specific cluster.  This operation requires membership in the cluster or `oz_clusters_view` admin privilege.  ***Example cURL requests***  **Get cluster details** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID  {   \"clusterId\": \"f8d843beda24e54545455ecc0f4b8886\",   \"type\": \"oneprovider\",   \"workerVersion\": {     \"release\": \"21.02.3\",     \"build\": \"1-gfabf02d\",     \"gui\": \"129c549fbe9b3e730c3d9910492228566e39e1236945766a74381405cc57fb04\"   },   \"onepanelVersion\": {     \"release\": \"21.02.3\",     \"build\": \"3-89fc6bad\",     \"gui\": \"68e7e1472adb719ddf2d88908775091dfb10e5d0b916f06125ea1af4056044e3\"   },   \"online\": true,   \"onepanelProxy\": false,   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cluster_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :return: Cluster
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
                    " to method get_cluster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_cluster`")  # noqa: E501

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
            '/clusters/{id}', 'GET',
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

    def get_cluster_effective_group(self, id, gid, **kwargs):  # noqa: E501
        """Get cluster's effective group details  # noqa: E501

        Returns details about a specific effective group in a cluster.  This operation requires `cluster_view` privilege or `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get effective cluster group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_groups/$GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_groupX\",   \"type\": \"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cluster_effective_group(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :param str gid: Group Id. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_cluster_effective_group_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cluster_effective_group_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def get_cluster_effective_group_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Get cluster's effective group details  # noqa: E501

        Returns details about a specific effective group in a cluster.  This operation requires `cluster_view` privilege or `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get effective cluster group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_groups/$GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_groupX\",   \"type\": \"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cluster_effective_group_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
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
                    " to method get_cluster_effective_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_cluster_effective_group`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `get_cluster_effective_group`")  # noqa: E501

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
            '/clusters/{id}/effective_groups/{gid}', 'GET',
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

    def get_cluster_effective_user(self, id, uid, **kwargs):  # noqa: E501
        """Get cluster's effective user details  # noqa: E501

        Returns details about a specific effective user in a cluster.  This operation requires `cluster_view` privilege or `oz_users_view` admin privilege.  ***Example cURL requests***  **Get effective cluster user details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_users/$USER_ID  {   \"userId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"fullName\" : \"John Doe\",   \"username\" : \"jodoe\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cluster_effective_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :param str uid: User Id. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_cluster_effective_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cluster_effective_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def get_cluster_effective_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Get cluster's effective user details  # noqa: E501

        Returns details about a specific effective user in a cluster.  This operation requires `cluster_view` privilege or `oz_users_view` admin privilege.  ***Example cURL requests***  **Get effective cluster user details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_users/$USER_ID  {   \"userId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"fullName\" : \"John Doe\",   \"username\" : \"jodoe\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cluster_effective_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
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
                    " to method get_cluster_effective_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_cluster_effective_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_cluster_effective_user`")  # noqa: E501

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
            '/clusters/{id}/effective_users/{uid}', 'GET',
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

    def get_cluster_group(self, id, gid, **kwargs):  # noqa: E501
        """Get cluster group details  # noqa: E501

        Returns details about a specific group in a cluster.  This operation requires `cluster_view` privilege. For administrators who do not have to be members of this cluster, `oz_groups_view` privilege is required.  ***Example cURL requests***  **Get cluster group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups/$GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_groupX\",   \"type\": \"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cluster_group(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :param str gid: Group Id. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_cluster_group_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cluster_group_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def get_cluster_group_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Get cluster group details  # noqa: E501

        Returns details about a specific group in a cluster.  This operation requires `cluster_view` privilege. For administrators who do not have to be members of this cluster, `oz_groups_view` privilege is required.  ***Example cURL requests***  **Get cluster group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups/$GROUP_ID  {   \"groupId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"name\": \"new_groupX\",   \"type\": \"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cluster_group_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
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
                    " to method get_cluster_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_cluster_group`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `get_cluster_group`")  # noqa: E501

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
            '/clusters/{id}/groups/{gid}', 'GET',
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

    def get_cluster_user(self, id, uid, **kwargs):  # noqa: E501
        """Get cluster's user details  # noqa: E501

        Returns basic information about a specific user in a cluster.  This operation requires `cluster_view` privilege. For administrators who do not have to be members of this cluster, `oz_users_view` privilege is required.  ***Example cURL requests***  **Get cluster user data** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cluster_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :param str uid: User Id. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_cluster_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cluster_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def get_cluster_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Get cluster's user details  # noqa: E501

        Returns basic information about a specific user in a cluster.  This operation requires `cluster_view` privilege. For administrators who do not have to be members of this cluster, `oz_users_view` privilege is required.  ***Example cURL requests***  **Get cluster user data** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cluster_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
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
                    " to method get_cluster_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_cluster_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_cluster_user`")  # noqa: E501

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
            '/clusters/{id}/users/{uid}', 'GET',
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

    def get_effective_group_cluster_membership_intermediaries(self, id, gid, **kwargs):  # noqa: E501
        """Get effective group's cluster membership intermediaries  # noqa: E501

        Returns the effective group's (`{gid}`) cluster membership intermediaries - entities from which the group inherits membership in the cluster (`{id}`). Special keyword `\"self\"` in entity id indicates that the group (`{gid}`) has a direct membership in the cluster (`{id}`).  This operation requires any of the following authentication: * as user who is an effective member of the group (`{gid}`), * as user who has `cluster_view` privilege in the cluster (`{id}`), * as user who has `oz_clusters_view` admin privilege.  ***Example cURL requests***  **Get effective group's cluster membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_groups/$GROUP_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"cluster\", \"id\": \"self\"}   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_group_cluster_membership_intermediaries(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :param str gid: Group Id. (required)
        :return: MembershipIntermediaries
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_group_cluster_membership_intermediaries_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_group_cluster_membership_intermediaries_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def get_effective_group_cluster_membership_intermediaries_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Get effective group's cluster membership intermediaries  # noqa: E501

        Returns the effective group's (`{gid}`) cluster membership intermediaries - entities from which the group inherits membership in the cluster (`{id}`). Special keyword `\"self\"` in entity id indicates that the group (`{gid}`) has a direct membership in the cluster (`{id}`).  This operation requires any of the following authentication: * as user who is an effective member of the group (`{gid}`), * as user who has `cluster_view` privilege in the cluster (`{id}`), * as user who has `oz_clusters_view` admin privilege.  ***Example cURL requests***  **Get effective group's cluster membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_groups/$GROUP_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"cluster\", \"id\": \"self\"}   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_group_cluster_membership_intermediaries_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
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
                    " to method get_effective_group_cluster_membership_intermediaries" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_group_cluster_membership_intermediaries`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `get_effective_group_cluster_membership_intermediaries`")  # noqa: E501

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
            '/clusters/{id}/effective_groups/{gid}/membership', 'GET',
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

    def get_effective_user_cluster_membership_intermediaries(self, id, uid, **kwargs):  # noqa: E501
        """Get effective user's cluster membership intermediaries  # noqa: E501

        Returns the effective user's (`{uid}`) cluster membership intermediaries - entities from which the user inherits membership in the cluster (`{id}`). Special keyword `\"self\"` in entity id indicates that the user (`{uid}`) has a direct membership in the cluster (`{id}`).  This operation requires any of the following authentication: * as user (`{uid}`) who is an effective member of the cluster (`{id}`), * as user who has `cluster_view` privilege in the cluster (`{id}`), * as user who has `oz_clusters_view` admin privilege.  ***Example cURL requests***  **Get effective user's cluster membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_users/$USER_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"cluster\", \"id\": \"self\"}   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_user_cluster_membership_intermediaries(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :param str uid: User Id. (required)
        :return: MembershipIntermediaries
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_user_cluster_membership_intermediaries_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_user_cluster_membership_intermediaries_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def get_effective_user_cluster_membership_intermediaries_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Get effective user's cluster membership intermediaries  # noqa: E501

        Returns the effective user's (`{uid}`) cluster membership intermediaries - entities from which the user inherits membership in the cluster (`{id}`). Special keyword `\"self\"` in entity id indicates that the user (`{uid}`) has a direct membership in the cluster (`{id}`).  This operation requires any of the following authentication: * as user (`{uid}`) who is an effective member of the cluster (`{id}`), * as user who has `cluster_view` privilege in the cluster (`{id}`), * as user who has `oz_clusters_view` admin privilege.  ***Example cURL requests***  **Get effective user's cluster membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_users/$USER_ID/membership  {   \"intermediaries\": [     {\"type\": \"group\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"group\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"},     {\"type\": \"cluster\", \"id\": \"self\"}   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_user_cluster_membership_intermediaries_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
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
                    " to method get_effective_user_cluster_membership_intermediaries" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_user_cluster_membership_intermediaries`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_effective_user_cluster_membership_intermediaries`")  # noqa: E501

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
            '/clusters/{id}/effective_users/{uid}/membership', 'GET',
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

    def list_cluster_effective_groups(self, id, **kwargs):  # noqa: E501
        """List cluster's effective groups  # noqa: E501

        Returns the list of effective groups belonging to a specific cluster.  This operation requires `cluster_view` privilege or `oz_clusters_list_relationships` admin privilege.  ***Example cURL requests***  **Get cluster effective groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_groups  {   \"groups\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_cluster_effective_groups(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :return: Groups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_cluster_effective_groups_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_cluster_effective_groups_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_cluster_effective_groups_with_http_info(self, id, **kwargs):  # noqa: E501
        """List cluster's effective groups  # noqa: E501

        Returns the list of effective groups belonging to a specific cluster.  This operation requires `cluster_view` privilege or `oz_clusters_list_relationships` admin privilege.  ***Example cURL requests***  **Get cluster effective groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_groups  {   \"groups\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_cluster_effective_groups_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
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
                    " to method list_cluster_effective_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_cluster_effective_groups`")  # noqa: E501

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
            '/clusters/{id}/effective_groups', 'GET',
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

    def list_cluster_effective_users(self, id, **kwargs):  # noqa: E501
        """List cluster's effective users  # noqa: E501

        Returns the list of effective users belonging to a specific cluster.  This operation requires `cluster_view` privilege or `oz_clusters_list_relationships` admin privilege.  ***Example cURL requests***  **Get cluster effective users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_users  {   \"users\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_cluster_effective_users(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_cluster_effective_users_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_cluster_effective_users_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_cluster_effective_users_with_http_info(self, id, **kwargs):  # noqa: E501
        """List cluster's effective users  # noqa: E501

        Returns the list of effective users belonging to a specific cluster.  This operation requires `cluster_view` privilege or `oz_clusters_list_relationships` admin privilege.  ***Example cURL requests***  **Get cluster effective users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_users  {   \"users\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_cluster_effective_users_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
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
                    " to method list_cluster_effective_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_cluster_effective_users`")  # noqa: E501

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
            '/clusters/{id}/effective_users', 'GET',
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

    def list_cluster_groups(self, id, **kwargs):  # noqa: E501
        """List cluster's groups  # noqa: E501

        Returns the list of groups belonging to a specific cluster.  This operation requires `cluster_view` privilege. For administrator who does not belong to this cluster `oz_clusters_list_relationships` privilege is required.  ***Example cURL requests***  **Get cluster groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups  {   \"groups\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_cluster_groups(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :return: Groups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_cluster_groups_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_cluster_groups_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_cluster_groups_with_http_info(self, id, **kwargs):  # noqa: E501
        """List cluster's groups  # noqa: E501

        Returns the list of groups belonging to a specific cluster.  This operation requires `cluster_view` privilege. For administrator who does not belong to this cluster `oz_clusters_list_relationships` privilege is required.  ***Example cURL requests***  **Get cluster groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups  {   \"groups\": [     \"f1c8b1a37aa7447b22eb65a742d40524\",     \"8e1cea0b379e3683257c32f896d55115\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_cluster_groups_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
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
                    " to method list_cluster_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_cluster_groups`")  # noqa: E501

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
            '/clusters/{id}/groups', 'GET',
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

    def list_cluster_privileges(self, **kwargs):  # noqa: E501
        """List all cluster privileges  # noqa: E501

        Returns list of all possible cluster privileges.  This endpoint does not require authentication.  ***Example cURL requests***  **Get list of all cluster privileges** ```bash curl https://$ZONE_HOST/api/v3/onezone/clusters/privileges  {   \"admin\": [     \"cluster_view\",     \"cluster_update\",     \"cluster_delete\",     \"cluster_view_privileges\",     \"cluster_set_privileges\",     \"cluster_add_user\",     \"cluster_remove_user\",     \"cluster_add_group\",     \"cluster_remove_group\"   ],   \"manager\": [     \"cluster_view\",     \"cluster_add_user\",     \"cluster_remove_user\",     \"cluster_add_group\",     \"cluster_remove_group\"   ],   \"member\": [     \"cluster_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_cluster_privileges(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20019
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_cluster_privileges_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_cluster_privileges_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_cluster_privileges_with_http_info(self, **kwargs):  # noqa: E501
        """List all cluster privileges  # noqa: E501

        Returns list of all possible cluster privileges.  This endpoint does not require authentication.  ***Example cURL requests***  **Get list of all cluster privileges** ```bash curl https://$ZONE_HOST/api/v3/onezone/clusters/privileges  {   \"admin\": [     \"cluster_view\",     \"cluster_update\",     \"cluster_delete\",     \"cluster_view_privileges\",     \"cluster_set_privileges\",     \"cluster_add_user\",     \"cluster_remove_user\",     \"cluster_add_group\",     \"cluster_remove_group\"   ],   \"manager\": [     \"cluster_view\",     \"cluster_add_user\",     \"cluster_remove_user\",     \"cluster_add_group\",     \"cluster_remove_group\"   ],   \"member\": [     \"cluster_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_cluster_privileges_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20019
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
                    " to method list_cluster_privileges" % key
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
            '/clusters/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20019',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_cluster_users(self, id, **kwargs):  # noqa: E501
        """List cluster's users  # noqa: E501

        Returns the list of users belonging to a specific cluster.  This operation requires `cluster_view` privilege. For administrators who do not have to be members of this cluster, `oz_clusters_list_relationships` privilege is required.  ***Example cURL requests***  **Get cluster users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/users  {   \"users\": [     \"a5b469a2b0516b662a49da74d6d7d7bc\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_cluster_users(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_cluster_users_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_cluster_users_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_cluster_users_with_http_info(self, id, **kwargs):  # noqa: E501
        """List cluster's users  # noqa: E501

        Returns the list of users belonging to a specific cluster.  This operation requires `cluster_view` privilege. For administrators who do not have to be members of this cluster, `oz_clusters_list_relationships` privilege is required.  ***Example cURL requests***  **Get cluster users** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/users  {   \"users\": [     \"a5b469a2b0516b662a49da74d6d7d7bc\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_cluster_users_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
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
                    " to method list_cluster_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_cluster_users`")  # noqa: E501

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
            '/clusters/{id}/users', 'GET',
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

    def list_effective_group_cluster_privileges(self, id, gid, **kwargs):  # noqa: E501
        """List effective group's cluster privileges  # noqa: E501

        Returns the list of effective group's (`{gid}`) privileges in a cluster (`{id}`).  Effective privileges are a sum of group's privileges and privileges inherited from its parent group memberships.  This operation requires `cluster_view_privileges` privilege or `oz_clusters_view_privileges` admin privilege.  ***Example cURL requests***  **List effective groups's privileges in a cluster** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_groups/$GROUP_ID/privileges  {   \"privileges\": [     \"cluster_view\",     \"cluster_update\",     \"cluster_delete\",     \"cluster_view_privileges\",     \"cluster_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_cluster_privileges(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :param str gid: Group Id. (required)
        :return: InlineResponse20020
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_group_cluster_privileges_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_group_cluster_privileges_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def list_effective_group_cluster_privileges_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """List effective group's cluster privileges  # noqa: E501

        Returns the list of effective group's (`{gid}`) privileges in a cluster (`{id}`).  Effective privileges are a sum of group's privileges and privileges inherited from its parent group memberships.  This operation requires `cluster_view_privileges` privilege or `oz_clusters_view_privileges` admin privilege.  ***Example cURL requests***  **List effective groups's privileges in a cluster** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_groups/$GROUP_ID/privileges  {   \"privileges\": [     \"cluster_view\",     \"cluster_update\",     \"cluster_delete\",     \"cluster_view_privileges\",     \"cluster_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_group_cluster_privileges_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :param str gid: Group Id. (required)
        :return: InlineResponse20020
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
                    " to method list_effective_group_cluster_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_group_cluster_privileges`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `list_effective_group_cluster_privileges`")  # noqa: E501

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
            '/clusters/{id}/effective_groups/{gid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20020',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_effective_user_cluster_privileges(self, id, uid, **kwargs):  # noqa: E501
        """List effective user's cluster privileges  # noqa: E501

        Returns the list of effective user's (`{uid}`) privileges in a cluster (`{id}`).  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation requires `cluster_view_privileges` privilege or `oz_clusters_view_privileges` admin privilege.  ***Example cURL requests***  **List effective user's privileges in a cluster** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_users/$USER_ID/privileges  {   \"privileges\": [     \"cluster_view\",     \"cluster_update\",     \"cluster_delete\",     \"cluster_view_privileges\",     \"cluster_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_user_cluster_privileges(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :param str uid: User Id. (required)
        :return: InlineResponse20020
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_user_cluster_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_user_cluster_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def list_effective_user_cluster_privileges_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """List effective user's cluster privileges  # noqa: E501

        Returns the list of effective user's (`{uid}`) privileges in a cluster (`{id}`).  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation requires `cluster_view_privileges` privilege or `oz_clusters_view_privileges` admin privilege.  ***Example cURL requests***  **List effective user's privileges in a cluster** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/effective_users/$USER_ID/privileges  {   \"privileges\": [     \"cluster_view\",     \"cluster_update\",     \"cluster_delete\",     \"cluster_view_privileges\",     \"cluster_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_user_cluster_privileges_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :param str uid: User Id. (required)
        :return: InlineResponse20020
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
                    " to method list_effective_user_cluster_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_user_cluster_privileges`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `list_effective_user_cluster_privileges`")  # noqa: E501

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
            '/clusters/{id}/effective_users/{uid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20020',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_group_cluster_privileges(self, id, gid, **kwargs):  # noqa: E501
        """List group's cluster privileges  # noqa: E501

        Returns the list of group's (`{gid}`) privileges in a cluster (`{id}`).  This operation requires `cluster_view_privileges` privilege or `oz_clusters_view_privileges` admin privilege.  ***Example cURL requests***  **List groups's privileges in a cluster** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups/$GROUP_ID/privileges  {   \"privileges\": [     \"cluster_view\",     \"cluster_update\",     \"cluster_delete\",     \"cluster_view_privileges\",     \"cluster_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_cluster_privileges(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :param str gid: Group Id. (required)
        :return: InlineResponse20020
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_group_cluster_privileges_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_group_cluster_privileges_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def list_group_cluster_privileges_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """List group's cluster privileges  # noqa: E501

        Returns the list of group's (`{gid}`) privileges in a cluster (`{id}`).  This operation requires `cluster_view_privileges` privilege or `oz_clusters_view_privileges` admin privilege.  ***Example cURL requests***  **List groups's privileges in a cluster** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups/$GROUP_ID/privileges  {   \"privileges\": [     \"cluster_view\",     \"cluster_update\",     \"cluster_delete\",     \"cluster_view_privileges\",     \"cluster_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_cluster_privileges_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :param str gid: Group Id. (required)
        :return: InlineResponse20020
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
                    " to method list_group_cluster_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_group_cluster_privileges`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `list_group_cluster_privileges`")  # noqa: E501

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
            '/clusters/{id}/groups/{gid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20020',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_user_cluster_privileges(self, id, uid, **kwargs):  # noqa: E501
        """List user's cluster privileges  # noqa: E501

        Returns the list of user's (`{uid}`) privileges in a cluster (`{id}`).  This operation requires `cluster_view_privileges` privilege. For administrators who do not have to be members of this cluster, `oz_clusters_view_privileges` privilege is required.  ***Example cURL requests***  **List user's privileges in a cluster** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/users/$USER_ID/privileges  {   \"privileges\": [     \"cluster_view\",     \"cluster_update\",     \"cluster_delete\",     \"cluster_view_privileges\",     \"cluster_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_cluster_privileges(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :param str uid: User Id. (required)
        :return: InlineResponse20020
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_cluster_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_user_cluster_privileges_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def list_user_cluster_privileges_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """List user's cluster privileges  # noqa: E501

        Returns the list of user's (`{uid}`) privileges in a cluster (`{id}`).  This operation requires `cluster_view_privileges` privilege. For administrators who do not have to be members of this cluster, `oz_clusters_view_privileges` privilege is required.  ***Example cURL requests***  **List user's privileges in a cluster** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/users/$USER_ID/privileges  {   \"privileges\": [     \"cluster_view\",     \"cluster_update\",     \"cluster_delete\",     \"cluster_view_privileges\",     \"cluster_set_privileges\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_cluster_privileges_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :param str uid: User Id. (required)
        :return: InlineResponse20020
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
                    " to method list_user_cluster_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_user_cluster_privileges`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `list_user_cluster_privileges`")  # noqa: E501

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
            '/clusters/{id}/users/{uid}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20020',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_cluster(self, body, id, **kwargs):  # noqa: E501
        """Modify cluster details  # noqa: E501

        Updates the details about a cluster.  This operation requires `cluster_update` privilege or `oz_clusters_update` admin privilege.  ***Example cURL requests***  **Change cluster name** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"name\": \"new_cluster12\"}' \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_cluster(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ClusterUpdateRequest body: Cluster data. (required)
        :param str id: Cluster Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_cluster_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_cluster_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def modify_cluster_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Modify cluster details  # noqa: E501

        Updates the details about a cluster.  This operation requires `cluster_update` privilege or `oz_clusters_update` admin privilege.  ***Example cURL requests***  **Change cluster name** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"name\": \"new_cluster12\"}' \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_cluster_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ClusterUpdateRequest body: Cluster data. (required)
        :param str id: Cluster Id. (required)
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
                    " to method modify_cluster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `modify_cluster`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `modify_cluster`")  # noqa: E501

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
            '/clusters/{id}', 'PATCH',
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

    def oz_clusters_list(self, **kwargs):  # noqa: E501
        """List all clusters  # noqa: E501

        Returns the list of all clusters managed by the Onezone service.  This operation requires `oz_clusters_list` admin privilege.  ***Example cURL requests***  **List all clusters** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters  {   \"clusters\": [     \"S0Y9FSe9TFJFFzzLtBEs8\",     \"IkHBv8CoAFmbFU4fj26\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oz_clusters_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Clusters
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.oz_clusters_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.oz_clusters_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def oz_clusters_list_with_http_info(self, **kwargs):  # noqa: E501
        """List all clusters  # noqa: E501

        Returns the list of all clusters managed by the Onezone service.  This operation requires `oz_clusters_list` admin privilege.  ***Example cURL requests***  **List all clusters** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/clusters  {   \"clusters\": [     \"S0Y9FSe9TFJFFzzLtBEs8\",     \"IkHBv8CoAFmbFU4fj26\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oz_clusters_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Clusters
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
                    " to method oz_clusters_list" % key
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
            '/clusters', 'GET',
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

    def remove_cluster_group(self, id, gid, **kwargs):  # noqa: E501
        """Remove group from cluster  # noqa: E501

        Removes a specific group from cluster.  For regular users, who belong to this cluster it requires `cluster_remove_group` privilege to remove a group from this cluster.  For administrators, who are not members of this cluster, `oz_clusters_remove_relationships` privilege is required.  ***Example cURL requests***  **Get cluster group details** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_cluster_group(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :param str gid: Group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_cluster_group_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_cluster_group_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def remove_cluster_group_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Remove group from cluster  # noqa: E501

        Removes a specific group from cluster.  For regular users, who belong to this cluster it requires `cluster_remove_group` privilege to remove a group from this cluster.  For administrators, who are not members of this cluster, `oz_clusters_remove_relationships` privilege is required.  ***Example cURL requests***  **Get cluster group details** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_cluster_group_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
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
                    " to method remove_cluster_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_cluster_group`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `remove_cluster_group`")  # noqa: E501

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
            '/clusters/{id}/groups/{gid}', 'DELETE',
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

    def remove_cluster_user(self, id, uid, **kwargs):  # noqa: E501
        """Remove user from cluster  # noqa: E501

        Removes user from specific cluster.  This operation requires `cluster_remove_user` privilege in the cluster or `oz_clusters_remove_relationships` and `oz_users_remove_relationships` admin privileges.  ***Example cURL requests***  **Get cluster user data** ```bash curl -u admin:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_cluster_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
        :param str uid: User Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_cluster_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_cluster_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def remove_cluster_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Remove user from cluster  # noqa: E501

        Removes user from specific cluster.  This operation requires `cluster_remove_user` privilege in the cluster or `oz_clusters_remove_relationships` and `oz_users_remove_relationships` admin privileges.  ***Example cURL requests***  **Get cluster user data** ```bash curl -u admin:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_cluster_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Cluster Id. (required)
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
                    " to method remove_cluster_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_cluster_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `remove_cluster_user`")  # noqa: E501

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
            '/clusters/{id}/users/{uid}', 'DELETE',
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

    def update_group_cluster_privileges(self, body, id, gid, **kwargs):  # noqa: E501
        """Update group's privileges in a cluster  # noqa: E501

        Updates group's (`{gid}`) privileges in a cluster (`{id}`).  This operation requires `cluster_set_privileges` privilege or `oz_clusters_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update group's privileges in a cluster** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"cluster_view\", \"cluster_update\"], \"revoke\": [\"cluster_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups/$GROUP_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_group_cluster_privileges(body, id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ClusterPrivilegesUpdate body: Cluster privileges update request. (required)
        :param str id: Cluster Id. (required)
        :param str gid: Group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_group_cluster_privileges_with_http_info(body, id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_group_cluster_privileges_with_http_info(body, id, gid, **kwargs)  # noqa: E501
            return data

    def update_group_cluster_privileges_with_http_info(self, body, id, gid, **kwargs):  # noqa: E501
        """Update group's privileges in a cluster  # noqa: E501

        Updates group's (`{gid}`) privileges in a cluster (`{id}`).  This operation requires `cluster_set_privileges` privilege or `oz_clusters_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update group's privileges in a cluster** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"cluster_view\", \"cluster_update\"], \"revoke\": [\"cluster_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/groups/$GROUP_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_group_cluster_privileges_with_http_info(body, id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ClusterPrivilegesUpdate body: Cluster privileges update request. (required)
        :param str id: Cluster Id. (required)
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
                    " to method update_group_cluster_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_group_cluster_privileges`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_group_cluster_privileges`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `update_group_cluster_privileges`")  # noqa: E501

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
            '/clusters/{id}/groups/{gid}/privileges', 'PATCH',
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

    def update_user_cluster_privileges(self, body, id, uid, **kwargs):  # noqa: E501
        """Update user's cluster privileges  # noqa: E501

        Updates user's (`{uid}`) privileges in a cluster (`{id}`).  This operation requires `cluster_set_privileges` privilege. For administrators who do not have to be members of this cluster, `oz_clusters_set_privileges` privilege is required.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update user's privileges in a cluster** ```bash curl -u admin:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"cluster_view\", \"cluster_update\"], \"revoke\": [\"cluster_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/users/$USER_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_cluster_privileges(body, id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ClusterPrivilegesUpdate body: Cluster privileges update request. (required)
        :param str id: Cluster Id. (required)
        :param str uid: User Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_user_cluster_privileges_with_http_info(body, id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_user_cluster_privileges_with_http_info(body, id, uid, **kwargs)  # noqa: E501
            return data

    def update_user_cluster_privileges_with_http_info(self, body, id, uid, **kwargs):  # noqa: E501
        """Update user's cluster privileges  # noqa: E501

        Updates user's (`{uid}`) privileges in a cluster (`{id}`).  This operation requires `cluster_set_privileges` privilege. For administrators who do not have to be members of this cluster, `oz_clusters_set_privileges` privilege is required.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Update user's privileges in a cluster** ```bash curl -u admin:password -X PATCH -H \"Content-type: application/json\" \\ -d '{\"grant\": [\"cluster_view\", \"cluster_update\"], \"revoke\": [\"cluster_delete\"]}' \\ https://$ZONE_HOST/api/v3/onezone/clusters/$CLUSTER_ID/users/$USER_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_cluster_privileges_with_http_info(body, id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ClusterPrivilegesUpdate body: Cluster privileges update request. (required)
        :param str id: Cluster Id. (required)
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
                    " to method update_user_cluster_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_user_cluster_privileges`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_user_cluster_privileges`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `update_user_cluster_privileges`")  # noqa: E501

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
            '/clusters/{id}/users/{uid}/privileges', 'PATCH',
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
