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


class ProviderApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def check_current_time(self, **kwargs):  # noqa: E501
        """Show current clock time  # noqa: E501

        Returns current clock time of this Onezone instance, in milliseconds since epoch.  This operation has public access.  ***Example cURL requests***  **Check provider IP** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET https://onezone.example.com/api/v3/onezone/provider/public/get_current_time ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_current_time(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.check_current_time_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.check_current_time_with_http_info(**kwargs)  # noqa: E501
            return data

    def check_current_time_with_http_info(self, **kwargs):  # noqa: E501
        """Show current clock time  # noqa: E501

        Returns current clock time of this Onezone instance, in milliseconds since epoch.  This operation has public access.  ***Example cURL requests***  **Check provider IP** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET https://onezone.example.com/api/v3/onezone/provider/public/get_current_time ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_current_time_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: int
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
                    " to method check_current_time" % key
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
            '/provider/public/get_current_time', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def check_my_ip(self, **kwargs):  # noqa: E501
        """Show client IP address  # noqa: E501

        Returns the IP of the request peer. Will return the external IP (as seen by the Onezone).  This operation has public access.  ***Example cURL requests***  **Check provider IP** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET https://onezone.example.com/api/v3/onezone/provider/public/check_my_ip ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_my_ip(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.check_my_ip_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.check_my_ip_with_http_info(**kwargs)  # noqa: E501
            return data

    def check_my_ip_with_http_info(self, **kwargs):  # noqa: E501
        """Show client IP address  # noqa: E501

        Returns the IP of the request peer. Will return the external IP (as seen by the Onezone).  This operation has public access.  ***Example cURL requests***  **Check provider IP** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET https://onezone.example.com/api/v3/onezone/provider/public/check_my_ip ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_my_ip_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
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
                    " to method check_my_ip" % key
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
            '/provider/public/check_my_ip', 'GET',
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

    def get_current_provider_details(self, **kwargs):  # noqa: E501
        """Get current provider details  # noqa: E501

        Returns information about the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Get information about provider** ```bash curl -H \"x-auth-token: $TOKEN\" https://$ZONE_HOST/api/v3/onezone/provider  {   \"providerId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"name\": \"Example provider\",   \"domain\": \"provider1.example.com\",   \"latitude\": 50.0647,   \"longitude\": 19.945,   \"clusterId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"online\": true,   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_provider_details(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ProviderDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_current_provider_details_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_current_provider_details_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_current_provider_details_with_http_info(self, **kwargs):  # noqa: E501
        """Get current provider details  # noqa: E501

        Returns information about the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Get information about provider** ```bash curl -H \"x-auth-token: $TOKEN\" https://$ZONE_HOST/api/v3/onezone/provider  {   \"providerId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"name\": \"Example provider\",   \"domain\": \"provider1.example.com\",   \"latitude\": 50.0647,   \"longitude\": 19.945,   \"clusterId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"online\": true,   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_provider_details_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ProviderDetails
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
                    " to method get_current_provider_details" % key
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
            '/provider', 'GET',
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

    def get_current_provider_domain_config(self, **kwargs):  # noqa: E501
        """Get current provider's domain config  # noqa: E501

        Returns the domain config of the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Get provider's domain config** ```bash curl -sS -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/provider/domain_config  {   \"subdomainDelegation\": true,   \"domain\": \"provider1.onezone.example.com\",   \"subdomain\": \"provider1\",   \"ipList\": [\"172.17.0.1\", \"172.17.0.2\", \"172.17.0.3\"] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_provider_domain_config(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ProviderDomainConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_current_provider_domain_config_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_current_provider_domain_config_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_current_provider_domain_config_with_http_info(self, **kwargs):  # noqa: E501
        """Get current provider's domain config  # noqa: E501

        Returns the domain config of the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Get provider's domain config** ```bash curl -sS -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/provider/domain_config  {   \"subdomainDelegation\": true,   \"domain\": \"provider1.onezone.example.com\",   \"subdomain\": \"provider1\",   \"ipList\": [\"172.17.0.1\", \"172.17.0.2\", \"172.17.0.3\"] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_provider_domain_config_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ProviderDomainConfig
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
                    " to method get_current_provider_domain_config" % key
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
            '/provider/domain_config', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProviderDomainConfig',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_effective_group_provider_membership_intermediaries(self, id, gid, **kwargs):  # noqa: E501
        """Get effective group's provider membership intermediaries  # noqa: E501

        Returns the effective group's (`{gid}`) provider membership intermediaries - spaces from which the group inherits access to the provider (`{id}`).  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user (`{uid}`) who is an effective member of the group (`{gid}`), * as user who has `oz_providers_view` admin privilege.  ***Example cURL requests***  **Get effective group's provider membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/effective_groups/$GROUP_ID/membership  {   \"intermediaries\": [     {\"type\": \"space\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"space\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"}   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_group_provider_membership_intermediaries(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
        :param str gid: Group Id. (required)
        :return: MembershipIntermediaries
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_group_provider_membership_intermediaries_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_group_provider_membership_intermediaries_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def get_effective_group_provider_membership_intermediaries_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Get effective group's provider membership intermediaries  # noqa: E501

        Returns the effective group's (`{gid}`) provider membership intermediaries - spaces from which the group inherits access to the provider (`{id}`).  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user (`{uid}`) who is an effective member of the group (`{gid}`), * as user who has `oz_providers_view` admin privilege.  ***Example cURL requests***  **Get effective group's provider membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/effective_groups/$GROUP_ID/membership  {   \"intermediaries\": [     {\"type\": \"space\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"space\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"}   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_group_provider_membership_intermediaries_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
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
                    " to method get_effective_group_provider_membership_intermediaries" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_group_provider_membership_intermediaries`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `get_effective_group_provider_membership_intermediaries`")  # noqa: E501

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
            '/providers/{id}/effective_groups/{gid}/membership', 'GET',
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

    def get_effective_provider_group(self, id, gid, **kwargs):  # noqa: E501
        """Get group of provider  # noqa: E501

        Returns the details of an effective group of a specific provider.  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user who has `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get group of a provider** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/groups/$GROUP_ID  {   \"groupId\":\"051f1a51d80c664b0d9528d81ee56a93\",   \"name\":\"new_group\",   \"type\":\"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_provider_group(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
        :param str gid: Group Id. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_provider_group_with_http_info(id, gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_provider_group_with_http_info(id, gid, **kwargs)  # noqa: E501
            return data

    def get_effective_provider_group_with_http_info(self, id, gid, **kwargs):  # noqa: E501
        """Get group of provider  # noqa: E501

        Returns the details of an effective group of a specific provider.  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user who has `oz_groups_view` admin privilege.  ***Example cURL requests***  **Get group of a provider** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/groups/$GROUP_ID  {   \"groupId\":\"051f1a51d80c664b0d9528d81ee56a93\",   \"name\":\"new_group\",   \"type\":\"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_provider_group_with_http_info(id, gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
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
                    " to method get_effective_provider_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_provider_group`")  # noqa: E501
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `get_effective_provider_group`")  # noqa: E501

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
            '/providers/{id}/effective_groups/{gid}', 'GET',
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

    def get_effective_provider_user(self, id, uid, **kwargs):  # noqa: E501
        """Get effective user of provider  # noqa: E501

        Returns the details of an effective user of a specific provider. This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user who has `oz_users_view` admin privilege.  ***Example cURL requests***  **Get effective user of a provider** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/effective_users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\",    \"emails\" : [],    \"linkedAccounts\" : [] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_provider_user(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
        :param str uid: User Id. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_provider_user_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_provider_user_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def get_effective_provider_user_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Get effective user of provider  # noqa: E501

        Returns the details of an effective user of a specific provider. This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user who has `oz_users_view` admin privilege.  ***Example cURL requests***  **Get effective user of a provider** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/effective_users/$USER_ID  {    \"userId\" : \"f1c8b1a37aa7447b22eb65a742d40524\",    \"fullName\" : \"John Doe\",    \"username\" : \"jodoe\",    \"emails\" : [],    \"linkedAccounts\" : [] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_provider_user_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
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
                    " to method get_effective_provider_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_provider_user`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_effective_provider_user`")  # noqa: E501

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
            '/providers/{id}/effective_users/{uid}', 'GET',
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

    def get_effective_user_provider_membership_intermediaries(self, id, uid, **kwargs):  # noqa: E501
        """Get effective user's provider membership intermediaries  # noqa: E501

        Returns the effective user's (`{uid}`) provider membership intermediaries - spaces from which the user inherits access to the provider (`{id}`).  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user (`{uid}`) who is an effective member of the provider (`{id}`), * as user who has `oz_providers_view` admin privilege.  ***Example cURL requests***  **Get effective user's provider membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/effective_users/$USER_ID/membership  {   \"intermediaries\": [     {\"type\": \"space\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"space\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"}   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_user_provider_membership_intermediaries(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
        :param str uid: User Id. (required)
        :return: MembershipIntermediaries
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_user_provider_membership_intermediaries_with_http_info(id, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_user_provider_membership_intermediaries_with_http_info(id, uid, **kwargs)  # noqa: E501
            return data

    def get_effective_user_provider_membership_intermediaries_with_http_info(self, id, uid, **kwargs):  # noqa: E501
        """Get effective user's provider membership intermediaries  # noqa: E501

        Returns the effective user's (`{uid}`) provider membership intermediaries - spaces from which the user inherits access to the provider (`{id}`).  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user (`{uid}`) who is an effective member of the provider (`{id}`), * as user who has `oz_providers_view` admin privilege.  ***Example cURL requests***  **Get effective user's provider membership intermediaries** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/effective_users/$USER_ID/membership  {   \"intermediaries\": [     {\"type\": \"space\", \"id\": \"95527367966a95639e93a88718450b36\"},     {\"type\": \"space\", \"id\": \"2ef3de15fd49b3d6420f58428a6ad219\"}   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_user_provider_membership_intermediaries_with_http_info(id, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
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
                    " to method get_effective_user_provider_membership_intermediaries" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_effective_user_provider_membership_intermediaries`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_effective_user_provider_membership_intermediaries`")  # noqa: E501

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
            '/providers/{id}/effective_users/{uid}/membership', 'GET',
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

    def get_provider_details(self, id, **kwargs):  # noqa: E501
        """Get provider details  # noqa: E501

        Returns the information about a specific Oneprovider service that is registered in Onezone.  This operation requires any of the following authentication: * as any provider (providers are allowed to view each other's data), * as user who is an effective member in a space supported by the subject provider, * as user who has `oz_providers_view` admin privilege.  ***Example cURL requests***  **Get specific provider details** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID  {   \"providerId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"name\": \"Example provider\",   \"domain\": \"provider1.example.com\",   \"latitude\": 50.0647,   \"longitude\": 19.945,   \"clusterId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"online\": true,   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_provider_details(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
        :return: ProviderDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_provider_details_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_provider_details_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_provider_details_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get provider details  # noqa: E501

        Returns the information about a specific Oneprovider service that is registered in Onezone.  This operation requires any of the following authentication: * as any provider (providers are allowed to view each other's data), * as user who is an effective member in a space supported by the subject provider, * as user who has `oz_providers_view` admin privilege.  ***Example cURL requests***  **Get specific provider details** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID  {   \"providerId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"name\": \"Example provider\",   \"domain\": \"provider1.example.com\",   \"latitude\": 50.0647,   \"longitude\": 19.945,   \"clusterId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"online\": true,   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_provider_details_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
        :return: ProviderDetails
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
                    " to method get_provider_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_provider_details`")  # noqa: E501

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
            '/providers/{id}', 'GET',
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

    def get_provider_domain_config(self, id, **kwargs):  # noqa: E501
        """Get provider's domain config  # noqa: E501

        Returns the domain config of specific provider.  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user who has `oz_providers_view` admin privilege.  ***Example cURL requests***  **Get provider's domain config** ```bash curl -sS -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/domain_config  {   \"subdomainDelegation\": true,   \"domain\": \"provider1.onezone.example.com\",   \"subdomain\": \"provider1\",   \"ipList\": [\"172.17.0.1\", \"172.17.0.2\", \"172.17.0.3\"] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_provider_domain_config(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
        :return: ProviderDomainConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_provider_domain_config_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_provider_domain_config_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_provider_domain_config_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get provider's domain config  # noqa: E501

        Returns the domain config of specific provider.  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user who has `oz_providers_view` admin privilege.  ***Example cURL requests***  **Get provider's domain config** ```bash curl -sS -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/domain_config  {   \"subdomainDelegation\": true,   \"domain\": \"provider1.onezone.example.com\",   \"subdomain\": \"provider1\",   \"ipList\": [\"172.17.0.1\", \"172.17.0.2\", \"172.17.0.3\"] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_provider_domain_config_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
        :return: ProviderDomainConfig
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
                    " to method get_provider_domain_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_provider_domain_config`")  # noqa: E501

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
            '/providers/{id}/domain_config', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProviderDomainConfig',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_provider_space(self, id, sid, **kwargs):  # noqa: E501
        """Get space supported by provider  # noqa: E501

        Returns the details of space supported by a specific provider.  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user who has `oz_spaces_view` admin privilege.  ***Example cURL requests***  **Get space supported by provider** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/spaces/$SPACE_ID  {   \"spaceId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_space1\",   \"providers\": {     \"296ebe3c20e9666dc489b647f8647f12\" : 5368709120   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebfc1a770c3\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_provider_space(id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
        :param str sid: Space Id. (required)
        :return: Space
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_provider_space_with_http_info(id, sid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_provider_space_with_http_info(id, sid, **kwargs)  # noqa: E501
            return data

    def get_provider_space_with_http_info(self, id, sid, **kwargs):  # noqa: E501
        """Get space supported by provider  # noqa: E501

        Returns the details of space supported by a specific provider.  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user who has `oz_spaces_view` admin privilege.  ***Example cURL requests***  **Get space supported by provider** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/spaces/$SPACE_ID  {   \"spaceId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_space1\",   \"providers\": {     \"296ebe3c20e9666dc489b647f8647f12\" : 5368709120   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebfc1a770c3\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_provider_space_with_http_info(id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
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
                    " to method get_provider_space" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_provider_space`")  # noqa: E501
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `get_provider_space`")  # noqa: E501

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
            '/providers/{id}/spaces/{sid}', 'GET',
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

    def get_supported_space(self, sid, **kwargs):  # noqa: E501
        """Get space details by provider  # noqa: E501

        Returns information about a specific space supported by the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Get space details** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/provider/spaces/$SPACE_ID  {   \"spaceId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_space1\",   \"providers\": {     \"296ebe3c20e9666dc489b647f8647f12\" : 5368709120   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebfc1a770c3\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_supported_space(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id. (required)
        :return: Space
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_supported_space_with_http_info(sid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_supported_space_with_http_info(sid, **kwargs)  # noqa: E501
            return data

    def get_supported_space_with_http_info(self, sid, **kwargs):  # noqa: E501
        """Get space details by provider  # noqa: E501

        Returns information about a specific space supported by the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Get space details** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/provider/spaces/$SPACE_ID  {   \"spaceId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_space1\",   \"providers\": {     \"296ebe3c20e9666dc489b647f8647f12\" : 5368709120   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebfc1a770c3\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_supported_space_with_http_info(sid, async_req=True)
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
                    " to method get_supported_space" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `get_supported_space`")  # noqa: E501

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
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/provider/spaces/{sid}', 'GET',
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

    def list_current_provider_supported_spaces(self, **kwargs):  # noqa: E501
        """List current provider's supported spaces  # noqa: E501

        Returns the list of spaces managed by the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Get spaces supported by provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET https://$ZONE_HOST/api/v3/onezone/provider/spaces  {   \"spaces\": [     \"1ad4551e2c127fac3850374eeb2dfec4\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_current_provider_supported_spaces(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Spaces
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_current_provider_supported_spaces_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_current_provider_supported_spaces_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_current_provider_supported_spaces_with_http_info(self, **kwargs):  # noqa: E501
        """List current provider's supported spaces  # noqa: E501

        Returns the list of spaces managed by the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Get spaces supported by provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET https://$ZONE_HOST/api/v3/onezone/provider/spaces  {   \"spaces\": [     \"1ad4551e2c127fac3850374eeb2dfec4\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_current_provider_supported_spaces_with_http_info(async_req=True)
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
                    " to method list_current_provider_supported_spaces" % key
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
            '/provider/spaces', 'GET',
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

    def list_effective_provider_groups(self, id, **kwargs):  # noqa: E501
        """List effective groups of provider  # noqa: E501

        Returns the list of effective groups of a specific provider.  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user who has `oz_providers_list_relationships` admin privilege.  ***Example cURL requests***  **List groups of a provider** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/groups  {   \"groups\": [     \"1ad4551e2c127fac3850374eeb2dfec4\",     \"a6c6e47cc477aa4d3f8c61ce71df9850\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_provider_groups(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
        :return: Groups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_provider_groups_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_provider_groups_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_effective_provider_groups_with_http_info(self, id, **kwargs):  # noqa: E501
        """List effective groups of provider  # noqa: E501

        Returns the list of effective groups of a specific provider.  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user who has `oz_providers_list_relationships` admin privilege.  ***Example cURL requests***  **List groups of a provider** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/groups  {   \"groups\": [     \"1ad4551e2c127fac3850374eeb2dfec4\",     \"a6c6e47cc477aa4d3f8c61ce71df9850\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_provider_groups_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
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
                    " to method list_effective_provider_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_provider_groups`")  # noqa: E501

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
            '/providers/{id}/effective_groups', 'GET',
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

    def list_effective_provider_users(self, id, **kwargs):  # noqa: E501
        """List effective users of provider  # noqa: E501

        Returns the list of effective users of a specific provider.  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user who has `oz_providers_list_relationships` admin privilege.  ***Example cURL requests***  **List effective users of a provider** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/users  {   \"users\": [     \"1ad4551e2c127fac3850374eeb2dfec4\",     \"a6c6e47cc477aa4d3f8c61ce71df9850\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_provider_users(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_provider_users_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_provider_users_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_effective_provider_users_with_http_info(self, id, **kwargs):  # noqa: E501
        """List effective users of provider  # noqa: E501

        Returns the list of effective users of a specific provider.  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user who has `oz_providers_list_relationships` admin privilege.  ***Example cURL requests***  **List effective users of a provider** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/users  {   \"users\": [     \"1ad4551e2c127fac3850374eeb2dfec4\",     \"a6c6e47cc477aa4d3f8c61ce71df9850\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_provider_users_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
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
                    " to method list_effective_provider_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_effective_provider_users`")  # noqa: E501

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
            '/providers/{id}/effective_users', 'GET',
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

    def list_provider_supported_spaces(self, id, **kwargs):  # noqa: E501
        """List provider's supported spaces  # noqa: E501

        Returns the list of spaces supported by specific provider.  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user who has `oz_providers_list_relationships` admin privilege.  ***Example cURL requests***  **List spaces supported by provider** ```bash curlsS -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/spaces  {   \"spaces\": [     \"1ad4551e2c127fac3850374eeb2dfec4\",     \"a6c6e47cc477aa4d3f8c61ce71df9850\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_provider_supported_spaces(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
        :return: Spaces
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_provider_supported_spaces_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_provider_supported_spaces_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_provider_supported_spaces_with_http_info(self, id, **kwargs):  # noqa: E501
        """List provider's supported spaces  # noqa: E501

        Returns the list of spaces supported by specific provider.  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `cluster_view` privilege in the cluster corresponding to   the subject provider, * as user who has `oz_providers_list_relationships` admin privilege.  ***Example cURL requests***  **List spaces supported by provider** ```bash curlsS -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/spaces  {   \"spaces\": [     \"1ad4551e2c127fac3850374eeb2dfec4\",     \"a6c6e47cc477aa4d3f8c61ce71df9850\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_provider_supported_spaces_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
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
                    " to method list_provider_supported_spaces" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_provider_supported_spaces`")  # noqa: E501

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
            '/providers/{id}/spaces', 'GET',
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

    def map_idp_group(self, body, **kwargs):  # noqa: E501
        """Map IdP group to Onezone group  # noqa: E501

        Maps external IdP group Id into internal group Id in Onezone. The IdP must have group mapping enabled.  The group does not have to exist in Onezone or the IdP - this method merely transforms the Id using a deterministic procedure. It can be used to predict the group Id in Onezone before it is created.  This operation has public access.  ***Example cURL requests***  **Map IdP group to Onezone group** ```bash curl -H 'Content-type: application/json' \\ -d '{\"idp\": \"elixir\", \"groupId\": \"elixir:members\"}' \\ -X POST https://onezone.example.com/api/v3/onezone/provider/public/map_idp_group  {   \"groupId\": \"302da048de67e2ea05f0af1d0fe7c8a2\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.map_idp_group(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PublicMapIdpGroupBody body: Mapping parameters (required)
        :return: InlineResponse20011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.map_idp_group_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.map_idp_group_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def map_idp_group_with_http_info(self, body, **kwargs):  # noqa: E501
        """Map IdP group to Onezone group  # noqa: E501

        Maps external IdP group Id into internal group Id in Onezone. The IdP must have group mapping enabled.  The group does not have to exist in Onezone or the IdP - this method merely transforms the Id using a deterministic procedure. It can be used to predict the group Id in Onezone before it is created.  This operation has public access.  ***Example cURL requests***  **Map IdP group to Onezone group** ```bash curl -H 'Content-type: application/json' \\ -d '{\"idp\": \"elixir\", \"groupId\": \"elixir:members\"}' \\ -X POST https://onezone.example.com/api/v3/onezone/provider/public/map_idp_group  {   \"groupId\": \"302da048de67e2ea05f0af1d0fe7c8a2\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.map_idp_group_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PublicMapIdpGroupBody body: Mapping parameters (required)
        :return: InlineResponse20011
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
                    " to method map_idp_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `map_idp_group`")  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/provider/public/map_idp_group', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20011',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def map_idp_user(self, body, **kwargs):  # noqa: E501
        """Map IdP user to Onezone user  # noqa: E501

        Maps external IdP user id into internal user id in Onezone.  The user does not have to exist in Onezone or the IdP - this method merely transforms the Id using a deterministic procedure. It can be used to predict the user Id in Onezone before it is created.  This operation has public access.  ***Example cURL requests***  **Map IdP user to Onezone user** ```bash curl -H 'Content-type: application/json' \\ -d '{\"idp\": \"elixir\", \"userId\": \"dqs1ew2afn9q28rnweu8fb23r9jqwtfg\"}' \\ -X POST https://onezone.example.com/api/v3/onezone/provider/public/map_idp_user  {   \"userId\": \"0fe7c8a20ffdf07480c46f084bc3b8d5\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.map_idp_user(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PublicMapIdpUserBody body: Mapping parameters (required)
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.map_idp_user_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.map_idp_user_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def map_idp_user_with_http_info(self, body, **kwargs):  # noqa: E501
        """Map IdP user to Onezone user  # noqa: E501

        Maps external IdP user id into internal user id in Onezone.  The user does not have to exist in Onezone or the IdP - this method merely transforms the Id using a deterministic procedure. It can be used to predict the user Id in Onezone before it is created.  This operation has public access.  ***Example cURL requests***  **Map IdP user to Onezone user** ```bash curl -H 'Content-type: application/json' \\ -d '{\"idp\": \"elixir\", \"userId\": \"dqs1ew2afn9q28rnweu8fb23r9jqwtfg\"}' \\ -X POST https://onezone.example.com/api/v3/onezone/provider/public/map_idp_user  {   \"userId\": \"0fe7c8a20ffdf07480c46f084bc3b8d5\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.map_idp_user_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PublicMapIdpUserBody body: Mapping parameters (required)
        :return: InlineResponse20010
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
                    " to method map_idp_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `map_idp_user`")  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/provider/public/map_idp_user', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20010',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_provider(self, body, **kwargs):  # noqa: E501
        """Modify provider details  # noqa: E501

        Updates information about the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Update provider geo location** ```bash curl -H \"x-auth-token: $TOKEN\" -H \"Content-type: application/json\" -X PATCH \\ -d '{\"latitude\": 50.068968,\"longitude\": 20.909444}'  \\ https://$ZONE_HOST/api/v3/onezone/provider ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_provider(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProviderUpdateRequest body: Provider data. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_provider_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_provider_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def modify_provider_with_http_info(self, body, **kwargs):  # noqa: E501
        """Modify provider details  # noqa: E501

        Updates information about the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Update provider geo location** ```bash curl -H \"x-auth-token: $TOKEN\" -H \"Content-type: application/json\" -X PATCH \\ -d '{\"latitude\": 50.068968,\"longitude\": 20.909444}'  \\ https://$ZONE_HOST/api/v3/onezone/provider ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_provider_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProviderUpdateRequest body: Provider data. (required)
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
                    " to method modify_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `modify_provider`")  # noqa: E501

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
            '/provider', 'PATCH',
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

    def modify_supported_space(self, sid, **kwargs):  # noqa: E501
        """Modify supported space  # noqa: E501

        Modifies the support size of a space supported by the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Change supported size** ```bash curl -H \"x-auth-token: $TOKEN\" -H \"Content-type: application/json\" \\ -X PATCH -d '{\"size\": 1024000}' \\ https://$ZONE_HOST/api/v3/onezone/provider/spaces/$SPACE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_supported_space(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_supported_space_with_http_info(sid, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_supported_space_with_http_info(sid, **kwargs)  # noqa: E501
            return data

    def modify_supported_space_with_http_info(self, sid, **kwargs):  # noqa: E501
        """Modify supported space  # noqa: E501

        Modifies the support size of a space supported by the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Change supported size** ```bash curl -H \"x-auth-token: $TOKEN\" -H \"Content-type: application/json\" \\ -X PATCH -d '{\"size\": 1024000}' \\ https://$ZONE_HOST/api/v3/onezone/provider/spaces/$SPACE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_supported_space_with_http_info(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id. (required)
        :return: None
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
                    " to method modify_supported_space" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `modify_supported_space`")  # noqa: E501

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
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/provider/spaces/{sid}', 'PATCH',
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

    def oz_providers_list(self, **kwargs):  # noqa: E501
        """List providers  # noqa: E501

        Returns the list of providers registered in the Onezone service.  This operation requires `oz_providers_list` admin privilege.  ***Example cURL requests***  **Get list of providers** ```bash curl -Ssk -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers  {   \"providers\": [     \"WEavnRE7c49EU2sjF0Rz7l_kpiA1IBrwbDxNfH87Plc\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oz_providers_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Providers
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.oz_providers_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.oz_providers_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def oz_providers_list_with_http_info(self, **kwargs):  # noqa: E501
        """List providers  # noqa: E501

        Returns the list of providers registered in the Onezone service.  This operation requires `oz_providers_list` admin privilege.  ***Example cURL requests***  **Get list of providers** ```bash curl -Ssk -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/providers  {   \"providers\": [     \"WEavnRE7c49EU2sjF0Rz7l_kpiA1IBrwbDxNfH87Plc\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oz_providers_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Providers
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
                    " to method oz_providers_list" % key
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
            '/providers', 'GET',
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

    def register_provider(self, body, **kwargs):  # noqa: E501
        """Register provider  # noqa: E501

        Registers a Oneprovider in Onezone service. Upon success, a new cluster is created, with the registering user linked to it. The cluster Id is the same as Oneprovider Id.  Requires a valid provider registration token - see:   * [Create provider registration token for self](#operation/user_create_provider_registration_token_for_self)   * [Create provider registration token for a user](#operation/user_create_provider_registration_token)  This operation has public access.  ***Example cURL requests***  **Register provider** ```bash curl -H \"Content-type: application/json\" -X POST -d '{   \"token\" : \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaW...\",   \"name\" : \"My provider\",   \"adminEmail\" : \"person@example.com\",   \"subdomainDelegation\" : \"false\",   \"domain\" : \"my-provider.example.com\",   \"latitude\" : \"50.0647\",   \"longitude\" : \"19.9450\", }' \\ https://$ZONE_HOST/api/v3/onezone/providers ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register_provider(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProviderRegistrationRequest body: Provider reqistration request. (required)
        :return: ProviderRegistrationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.register_provider_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.register_provider_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def register_provider_with_http_info(self, body, **kwargs):  # noqa: E501
        """Register provider  # noqa: E501

        Registers a Oneprovider in Onezone service. Upon success, a new cluster is created, with the registering user linked to it. The cluster Id is the same as Oneprovider Id.  Requires a valid provider registration token - see:   * [Create provider registration token for self](#operation/user_create_provider_registration_token_for_self)   * [Create provider registration token for a user](#operation/user_create_provider_registration_token)  This operation has public access.  ***Example cURL requests***  **Register provider** ```bash curl -H \"Content-type: application/json\" -X POST -d '{   \"token\" : \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaW...\",   \"name\" : \"My provider\",   \"adminEmail\" : \"person@example.com\",   \"subdomainDelegation\" : \"false\",   \"domain\" : \"my-provider.example.com\",   \"latitude\" : \"50.0647\",   \"longitude\" : \"19.9450\", }' \\ https://$ZONE_HOST/api/v3/onezone/providers ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register_provider_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProviderRegistrationRequest body: Provider reqistration request. (required)
        :return: ProviderRegistrationResponse
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
                    " to method register_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `register_provider`")  # noqa: E501

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
            '/providers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProviderRegistrationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_provider(self, id, **kwargs):  # noqa: E501
        """Remove provider  # noqa: E501

        Removes (unregisters) given Oneprovider from Onezone.  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `oz_providers_delete` admin privilege.  ***Example cURL requests***  **Get specific provider details** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_provider(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_provider_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_provider_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def remove_provider_with_http_info(self, id, **kwargs):  # noqa: E501
        """Remove provider  # noqa: E501

        Removes (unregisters) given Oneprovider from Onezone.  This operation requires any of the following authentication: * as the subject provider (`{id}`), * as user who has `oz_providers_delete` admin privilege.  ***Example cURL requests***  **Get specific provider details** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE  \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_provider_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id. (required)
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
                    " to method remove_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_provider`")  # noqa: E501

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
            '/providers/{id}', 'DELETE',
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

    def remove_space_support(self, sid, **kwargs):  # noqa: E501
        """Remove space support  # noqa: E501

        Revokes support for a space supported by the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Revoke space support** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/provider/spaces/$SPACE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_space_support(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_space_support_with_http_info(sid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_space_support_with_http_info(sid, **kwargs)  # noqa: E501
            return data

    def remove_space_support_with_http_info(self, sid, **kwargs):  # noqa: E501
        """Remove space support  # noqa: E501

        Revokes support for a space supported by the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Revoke space support** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/provider/spaces/$SPACE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_space_support_with_http_info(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id. (required)
        :return: None
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
                    " to method remove_space_support" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `remove_space_support`")  # noqa: E501

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
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/provider/spaces/{sid}', 'DELETE',
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

    def unregister_provider(self, **kwargs):  # noqa: E501
        """Unregister provider  # noqa: E501

        Allows Oneprovider service to unregister from Onezone - concerns the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Unregister provider from Onezone** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE  \\ https://$ZONE_HOST/api/v3/onezone/provider ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unregister_provider(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.unregister_provider_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.unregister_provider_with_http_info(**kwargs)  # noqa: E501
            return data

    def unregister_provider_with_http_info(self, **kwargs):  # noqa: E501
        """Unregister provider  # noqa: E501

        Allows Oneprovider service to unregister from Onezone - concerns the Oneprovider that performed the request.  This operation requires provider authentication - see [provider auth token](#section/Overview/Authentication-and-authorization).  ***Example cURL requests***  **Unregister provider from Onezone** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE  \\ https://$ZONE_HOST/api/v3/onezone/provider ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unregister_provider_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
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
                    " to method unregister_provider" % key
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
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/provider', 'DELETE',
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

    def verify_provider_identity(self, body, **kwargs):  # noqa: E501
        """Verify the identity of given provider  # noqa: E501

        Verifies the identity of given provider based on its identity token.  This operation has public access.  ***Example cURL requests***  **Check provider IP** ```bash curl -H \"X-Auth-Token: $TOKEN\" -H \"Content-type: application/json\" \\ -d '{\"providerId\": \"f3a3fbcc6e85e1b7829e4901a8e1809\", \"token\": \"JKAxNWxvY2F0aW9uIG9uZXp...\"}' \\ -X POST https://onezone.example.com/api/v3/onezone/provider/public/verify_provider_identity ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_provider_identity(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PublicVerifyProviderIdentityBody body: Identity parameters (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.verify_provider_identity_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.verify_provider_identity_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def verify_provider_identity_with_http_info(self, body, **kwargs):  # noqa: E501
        """Verify the identity of given provider  # noqa: E501

        Verifies the identity of given provider based on its identity token.  This operation has public access.  ***Example cURL requests***  **Check provider IP** ```bash curl -H \"X-Auth-Token: $TOKEN\" -H \"Content-type: application/json\" \\ -d '{\"providerId\": \"f3a3fbcc6e85e1b7829e4901a8e1809\", \"token\": \"JKAxNWxvY2F0aW9uIG9uZXp...\"}' \\ -X POST https://onezone.example.com/api/v3/onezone/provider/public/verify_provider_identity ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_provider_identity_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PublicVerifyProviderIdentityBody body: Identity parameters (required)
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
                    " to method verify_provider_identity" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `verify_provider_identity`")  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/provider/public/verify_provider_identity', 'POST',
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
