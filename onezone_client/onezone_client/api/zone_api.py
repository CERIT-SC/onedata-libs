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


class ZoneApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_configuration(self, **kwargs):  # noqa: E501
        """Returns public configuration of Onezone service.  # noqa: E501

        Returns public information about the Onezone service.  This endpoint does not require authentication.  ***Example cURL requests***  **Get public information about the Onezone service** ```bash curl https://$ZONE_HOST/api/v3/onezone/configuration  {   \"name\": \"Example zone\",   \"domain\": \"zone.example.com\",   \"version\": \"21.02.3\",   \"build\": \"g52dbeca23\",   \"subdomainDelegationSupported\": true,   \"compatibleOneproviderVersions\": [       \"20.02.1\",       \"20.02.2\",       \"21.02.3\"   ],   \"compatibilityRegistryRevision\": 2022122100,   \"supportedIdPs\": [     {       \"id\": \"google\",       \"offlineAccess\": true     },     {       \"id\": \"basicAuth\",       \"offlineAccess\": false     }   ],   \"availableSpaceTags\": {     \"general\": [         \"big-data\",         \"demo\",         \"open-data\",         \"simulation\"     ],     \"domains\": [         \"agriculture\",         \"forestry\",         \"justice\",         \"science\"     ]   } } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_configuration(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Configuration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_configuration_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_configuration_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_configuration_with_http_info(self, **kwargs):  # noqa: E501
        """Returns public configuration of Onezone service.  # noqa: E501

        Returns public information about the Onezone service.  This endpoint does not require authentication.  ***Example cURL requests***  **Get public information about the Onezone service** ```bash curl https://$ZONE_HOST/api/v3/onezone/configuration  {   \"name\": \"Example zone\",   \"domain\": \"zone.example.com\",   \"version\": \"21.02.3\",   \"build\": \"g52dbeca23\",   \"subdomainDelegationSupported\": true,   \"compatibleOneproviderVersions\": [       \"20.02.1\",       \"20.02.2\",       \"21.02.3\"   ],   \"compatibilityRegistryRevision\": 2022122100,   \"supportedIdPs\": [     {       \"id\": \"google\",       \"offlineAccess\": true     },     {       \"id\": \"basicAuth\",       \"offlineAccess\": false     }   ],   \"availableSpaceTags\": {     \"general\": [         \"big-data\",         \"demo\",         \"open-data\",         \"simulation\"     ],     \"domains\": [         \"agriculture\",         \"forestry\",         \"justice\",         \"science\"     ]   } } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_configuration_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Configuration
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
                    " to method get_configuration" % key
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
            '/configuration', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Configuration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def health(self, **kwargs):  # noqa: E501
        """Check cluster health  # noqa: E501

        Returns status code indicating onezone service health status. This endpoint does not require authentication.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.health(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.health_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.health_with_http_info(**kwargs)  # noqa: E501
            return data

    def health_with_http_info(self, **kwargs):  # noqa: E501
        """Check cluster health  # noqa: E501

        Returns status code indicating onezone service health status. This endpoint does not require authentication.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.health_with_http_info(async_req=True)
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
                    " to method health" % key
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
            '/health', 'GET',
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

    def list_privileges(self, **kwargs):  # noqa: E501
        """List all admin privileges.  # noqa: E501

        Returns list of all possible Onezone admin privileges.  This endpoint does not require authentication.  ***Example cURL requests***  **Get list of all Onezone admin privileges** ```bash curl https://$ZONE_HOST/api/v3/onezone/privileges  {   \"admin\": [     \"oz_view_privileges\",     \"oz_set_privileges\",     \"oz_users_list\",     \"oz_users_view\",     \"oz_users_create\",     \"oz_users_manage_passwords\",     \"oz_users_update\",     \"oz_users_delete\",     \"oz_users_list_relationships\",     \"oz_users_add_relationships\",     \"oz_users_remove_relationships\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_groups_create\",     \"oz_groups_update\",     \"oz_groups_delete\",     \"oz_groups_view_privileges\",     \"oz_groups_set_privileges\",     \"oz_groups_list_relationships\",     \"oz_groups_add_relationships\",     \"oz_groups_remove_relationships\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_spaces_create\",     \"oz_spaces_update\",     \"oz_spaces_delete\",     \"oz_spaces_view_privileges\",     \"oz_spaces_set_privileges\",     \"oz_spaces_list_relationships\",     \"oz_spaces_add_relationships\",     \"oz_spaces_remove_relationships\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_shares_create\",     \"oz_shares_update\",     \"oz_shares_delete\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_providers_update\",     \"oz_providers_delete\",     \"oz_providers_list_relationships\",     \"oz_providers_invite\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handle_services_create\",     \"oz_handle_services_update\",     \"oz_handle_services_delete\",     \"oz_handle_services_view_privileges\",     \"oz_handle_services_set_privileges\",     \"oz_handle_services_list_relationships\",     \"oz_handle_services_add_relationships\",     \"oz_handle_services_remove_relationships\",     \"oz_handles_list\",     \"oz_handles_view\",     \"oz_handles_create\",     \"oz_handles_update\",     \"oz_handles_delete\",     \"oz_handles_view_privileges\",     \"oz_handles_set_privileges\",     \"oz_handles_list_relationships\",     \"oz_handles_add_relationships\",     \"oz_handles_remove_relationships\",     \"oz_harvesters_list\",     \"oz_harvesters_view\",     \"oz_harvesters_create\",     \"oz_harvesters_update\",     \"oz_harvesters_delete\",     \"oz_harvesters_view_privileges\",     \"oz_harvesters_set_privileges\",     \"oz_harvesters_list_relationships\",     \"oz_harvesters_add_relationships\",     \"oz_harvesters_remove_relationships\",     \"oz_clusters_list\",     \"oz_clusters_view\",     \"oz_clusters_update\",     \"oz_clusters_view_privileges\",     \"oz_clusters_set_privileges\",     \"oz_clusters_list_relationships\",     \"oz_clusters_add_relationships\",     \"oz_clusters_remove_relationships\"   ],   \"viewer\": [     \"oz_users_list\",     \"oz_users_view\",     \"oz_users_list_relationships\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_groups_list_relationships\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_spaces_list_relationships\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_providers_list_relationships\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handle_services_list_relationships\",     \"oz_handles_list\",     \"oz_handles_view\",     \"oz_handles_list_relationships\",     \"oz_harvesters_list\",     \"oz_harvesters_view\",     \"oz_harvesters_list_relationships\",     \"oz_clusters_list\",     \"oz_clusters_view\",     \"oz_clusters_list_relationships\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_privileges(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_privileges_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_privileges_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_privileges_with_http_info(self, **kwargs):  # noqa: E501
        """List all admin privileges.  # noqa: E501

        Returns list of all possible Onezone admin privileges.  This endpoint does not require authentication.  ***Example cURL requests***  **Get list of all Onezone admin privileges** ```bash curl https://$ZONE_HOST/api/v3/onezone/privileges  {   \"admin\": [     \"oz_view_privileges\",     \"oz_set_privileges\",     \"oz_users_list\",     \"oz_users_view\",     \"oz_users_create\",     \"oz_users_manage_passwords\",     \"oz_users_update\",     \"oz_users_delete\",     \"oz_users_list_relationships\",     \"oz_users_add_relationships\",     \"oz_users_remove_relationships\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_groups_create\",     \"oz_groups_update\",     \"oz_groups_delete\",     \"oz_groups_view_privileges\",     \"oz_groups_set_privileges\",     \"oz_groups_list_relationships\",     \"oz_groups_add_relationships\",     \"oz_groups_remove_relationships\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_spaces_create\",     \"oz_spaces_update\",     \"oz_spaces_delete\",     \"oz_spaces_view_privileges\",     \"oz_spaces_set_privileges\",     \"oz_spaces_list_relationships\",     \"oz_spaces_add_relationships\",     \"oz_spaces_remove_relationships\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_shares_create\",     \"oz_shares_update\",     \"oz_shares_delete\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_providers_update\",     \"oz_providers_delete\",     \"oz_providers_list_relationships\",     \"oz_providers_invite\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handle_services_create\",     \"oz_handle_services_update\",     \"oz_handle_services_delete\",     \"oz_handle_services_view_privileges\",     \"oz_handle_services_set_privileges\",     \"oz_handle_services_list_relationships\",     \"oz_handle_services_add_relationships\",     \"oz_handle_services_remove_relationships\",     \"oz_handles_list\",     \"oz_handles_view\",     \"oz_handles_create\",     \"oz_handles_update\",     \"oz_handles_delete\",     \"oz_handles_view_privileges\",     \"oz_handles_set_privileges\",     \"oz_handles_list_relationships\",     \"oz_handles_add_relationships\",     \"oz_handles_remove_relationships\",     \"oz_harvesters_list\",     \"oz_harvesters_view\",     \"oz_harvesters_create\",     \"oz_harvesters_update\",     \"oz_harvesters_delete\",     \"oz_harvesters_view_privileges\",     \"oz_harvesters_set_privileges\",     \"oz_harvesters_list_relationships\",     \"oz_harvesters_add_relationships\",     \"oz_harvesters_remove_relationships\",     \"oz_clusters_list\",     \"oz_clusters_view\",     \"oz_clusters_update\",     \"oz_clusters_view_privileges\",     \"oz_clusters_set_privileges\",     \"oz_clusters_list_relationships\",     \"oz_clusters_add_relationships\",     \"oz_clusters_remove_relationships\"   ],   \"viewer\": [     \"oz_users_list\",     \"oz_users_view\",     \"oz_users_list_relationships\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_groups_list_relationships\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_spaces_list_relationships\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_providers_list_relationships\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handle_services_list_relationships\",     \"oz_handles_list\",     \"oz_handles_view\",     \"oz_handles_list_relationships\",     \"oz_harvesters_list\",     \"oz_harvesters_view\",     \"oz_harvesters_list_relationships\",     \"oz_clusters_list\",     \"oz_clusters_view\",     \"oz_clusters_list_relationships\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_privileges_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse200
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
                    " to method list_privileges" % key
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
            '/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def test_image(self, **kwargs):  # noqa: E501
        """Get test image.  # noqa: E501

        This endpoint returns a dummy image in `.png` format. It is used internally by web applications across Onedata to check connectivity with certain services. This endpoint does not require authentication.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.test_image(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.test_image_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.test_image_with_http_info(**kwargs)  # noqa: E501
            return data

    def test_image_with_http_info(self, **kwargs):  # noqa: E501
        """Get test image.  # noqa: E501

        This endpoint returns a dummy image in `.png` format. It is used internally by web applications across Onedata to check connectivity with certain services. This endpoint does not require authentication.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.test_image_with_http_info(async_req=True)
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
                    " to method test_image" % key
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
            ['image/png'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/test_image', 'GET',
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
