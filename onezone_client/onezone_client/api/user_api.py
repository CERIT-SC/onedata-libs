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


class UserApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def acquire_idp_access_token(self, idp, **kwargs):  # noqa: E501
        """Acquire IdP access token  # noqa: E501

        Acquires an access token issued by given IdP for the current user. This operation requires that the IdP is configured to support offline access - issues refresh tokens upon user's login to Onezone, which are later used to acquire new access tokens when they expire. Offline access can be configured by the Onezone admin.  The user must first log in to Onezone using given IdP, otherwise the operation will return a 404 error.  This operation can be invoked on behalf of current user only.  ***Example cURL requests***  **Acquire IdP access token** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/user/idp_access_token/github ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.acquire_idp_access_token(idp, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str idp: IdP identifier. (required)
        :return: IdPAccessToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.acquire_idp_access_token_with_http_info(idp, **kwargs)  # noqa: E501
        else:
            (data) = self.acquire_idp_access_token_with_http_info(idp, **kwargs)  # noqa: E501
            return data

    def acquire_idp_access_token_with_http_info(self, idp, **kwargs):  # noqa: E501
        """Acquire IdP access token  # noqa: E501

        Acquires an access token issued by given IdP for the current user. This operation requires that the IdP is configured to support offline access - issues refresh tokens upon user's login to Onezone, which are later used to acquire new access tokens when they expire. Offline access can be configured by the Onezone admin.  The user must first log in to Onezone using given IdP, otherwise the operation will return a 404 error.  This operation can be invoked on behalf of current user only.  ***Example cURL requests***  **Acquire IdP access token** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/user/idp_access_token/github ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.acquire_idp_access_token_with_http_info(idp, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str idp: IdP identifier. (required)
        :return: IdPAccessToken
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['idp']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method acquire_idp_access_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'idp' is set
        if ('idp' not in params or
                params['idp'] is None):
            raise ValueError("Missing the required parameter `idp` when calling `acquire_idp_access_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'idp' in params:
            path_params['idp'] = params['idp']  # noqa: E501

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
            '/user/idp_access_token/{idp}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdPAccessToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def add_user_handle_service(self, body, **kwargs):  # noqa: E501
        """Create a new handle service for the current user  # noqa: E501

        Allows to register a new handle service.  This operation can be invoked on behalf of the current user only and requires `oz_handle_service_create` admin privilege.  ***Example cURL requests***  **Add user handle services** ```bash curl -u username:password -X POST -H \"Content-type: application/json\" \\ -d '{ ... }' https://$ZONE_HOST/api/v3/onezone/user/handle_services ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_user_handle_service(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HandleService body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_user_handle_service_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_user_handle_service_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def add_user_handle_service_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new handle service for the current user  # noqa: E501

        Allows to register a new handle service.  This operation can be invoked on behalf of the current user only and requires `oz_handle_service_create` admin privilege.  ***Example cURL requests***  **Add user handle services** ```bash curl -u username:password -X POST -H \"Content-type: application/json\" \\ -d '{ ... }' https://$ZONE_HOST/api/v3/onezone/user/handle_services ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_user_handle_service_with_http_info(body, async_req=True)
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
                    " to method add_user_handle_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_user_handle_service`")  # noqa: E501

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
            '/user/handle_services', 'POST',
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

    def change_user_basic_auth_settings(self, body, id, **kwargs):  # noqa: E501
        """Change user's basic auth settings  # noqa: E501

        Changes user's basic auth settings - the ability to authenticate with username & password, and/or the password itself.  This operation requires `oz_users_manage_passwords` admin privilege.  ***Example cURL requests***  **Change user's basic auth settings** ```bash curl -u admin:password -H \"Content-type: application/json\" -X PATCH  \\ -d '{\"basicAuthEnabled\": true, \"newPassword\": \"password123\"}' \\ https://$ZONE_HOST/api/v3/onezone/users/c5cb69ce45940468596ed16310a45e49/basic_auth ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_user_basic_auth_settings(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserBasicAuthSettingsUpdate body: User basic auth settings update request. (required)
        :param str id: User Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.change_user_basic_auth_settings_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.change_user_basic_auth_settings_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def change_user_basic_auth_settings_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Change user's basic auth settings  # noqa: E501

        Changes user's basic auth settings - the ability to authenticate with username & password, and/or the password itself.  This operation requires `oz_users_manage_passwords` admin privilege.  ***Example cURL requests***  **Change user's basic auth settings** ```bash curl -u admin:password -H \"Content-type: application/json\" -X PATCH  \\ -d '{\"basicAuthEnabled\": true, \"newPassword\": \"password123\"}' \\ https://$ZONE_HOST/api/v3/onezone/users/c5cb69ce45940468596ed16310a45e49/basic_auth ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_user_basic_auth_settings_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserBasicAuthSettingsUpdate body: User basic auth settings update request. (required)
        :param str id: User Id. (required)
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
                    " to method change_user_basic_auth_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `change_user_basic_auth_settings`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `change_user_basic_auth_settings`")  # noqa: E501

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
            '/users/{id}/basic_auth', 'PATCH',
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

    def change_user_password(self, body, **kwargs):  # noqa: E501
        """Change user's password  # noqa: E501

        Changes user's password, the old password must be given.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Change user's password** ```bash curl -u username:password -H \"Content-type: application/json\" -X PATCH  \\ -d '{\"oldPassword\": \"password\", \"newPassword\": \"password123\"}' \\ https://$ZONE_HOST/api/v3/onezone/user/password ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_user_password(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserPasswordUpdate body: User password update request. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.change_user_password_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.change_user_password_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def change_user_password_with_http_info(self, body, **kwargs):  # noqa: E501
        """Change user's password  # noqa: E501

        Changes user's password, the old password must be given.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Change user's password** ```bash curl -u username:password -H \"Content-type: application/json\" -X PATCH  \\ -d '{\"oldPassword\": \"password\", \"newPassword\": \"password123\"}' \\ https://$ZONE_HOST/api/v3/onezone/user/password ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_user_password_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserPasswordUpdate body: User password update request. (required)
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
                    " to method change_user_password" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `change_user_password`")  # noqa: E501

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
            '/user/password', 'PATCH',
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

    def create_client_token(self, **kwargs):  # noqa: E501
        """Generate user access token  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use [this one](#operation/create_named_token_for_current_user).  Creates new user token. The token is returned in the response body.  This operation can be invoked on behalf of currently authenticated user only.  ***Example cURL requests***  **Generate user token** ```bash curl -u username:password -X POST -d '' -H 'content-type: application/json' \\   https://$ZONE_HOST/api/v3/onezone/user/client_tokens  {   \"token\": \"MDAxNWxvY2F00aW9uIG9uZXpvbmUKMDAzYmlkZW500aWZpZXIgSlVxNGFLVkJSTXVFN3FLbHNQVHlNX00lLeHpYZXNWdVFSMGNfMldpOXFZNAowMDFhY2lkIHRpbWUgPCAxNTIyMzU4MzMzCjAwMmZzaWduYXR1cmUgv02ByyOA9802H02rPMB7Y9mIhDVAjYDmjAUjtrMs13znukK\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_client_token(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ClientToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_client_token_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_client_token_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_client_token_with_http_info(self, **kwargs):  # noqa: E501
        """Generate user access token  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use [this one](#operation/create_named_token_for_current_user).  Creates new user token. The token is returned in the response body.  This operation can be invoked on behalf of currently authenticated user only.  ***Example cURL requests***  **Generate user token** ```bash curl -u username:password -X POST -d '' -H 'content-type: application/json' \\   https://$ZONE_HOST/api/v3/onezone/user/client_tokens  {   \"token\": \"MDAxNWxvY2F00aW9uIG9uZXpvbmUKMDAzYmlkZW500aWZpZXIgSlVxNGFLVkJSTXVFN3FLbHNQVHlNX00lLeHpYZXNWdVFSMGNfMldpOXFZNAowMDFhY2lkIHRpbWUgPCAxNTIyMzU4MzMzCjAwMmZzaWduYXR1cmUgv02ByyOA9802H02rPMB7Y9mIhDVAjYDmjAUjtrMs13znukK\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_client_token_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ClientToken
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
                    " to method create_client_token" % key
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
            '/user/client_tokens', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClientToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_provider_registration_token_for_current_user(self, **kwargs):  # noqa: E501
        """Create provider registration token for current user  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token for the current user allowing him to register a new provider in Onezone. After the registration, the user's account will be automatically linked to the new Oneprovider cluster (granting him access to Oneprovider's onepanel).  This operation can be invoked on behalf of the current user only.  If registration policy in Onezone is configured as `open`, any user can generate the token for himself. In case of `restricted` policy, this operation requires `oz_providers_invite` privilege.  ***Example cURL requests***  **Create provider registration token for current user** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/user/clusters/$CLUSTER_ID  {   \"token\": [     \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaW-0Y8\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_provider_registration_token_for_current_user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ProviderRegistrationToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_provider_registration_token_for_current_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_provider_registration_token_for_current_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_provider_registration_token_for_current_user_with_http_info(self, **kwargs):  # noqa: E501
        """Create provider registration token for current user  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token for the current user allowing him to register a new provider in Onezone. After the registration, the user's account will be automatically linked to the new Oneprovider cluster (granting him access to Oneprovider's onepanel).  This operation can be invoked on behalf of the current user only.  If registration policy in Onezone is configured as `open`, any user can generate the token for himself. In case of `restricted` policy, this operation requires `oz_providers_invite` privilege.  ***Example cURL requests***  **Create provider registration token for current user** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/user/clusters/$CLUSTER_ID  {   \"token\": [     \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaW-0Y8\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_provider_registration_token_for_current_user_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ProviderRegistrationToken
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
                    " to method create_provider_registration_token_for_current_user" % key
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
            '/user/clusters/provider_registration_token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProviderRegistrationToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_provider_registration_token_for_user(self, id, **kwargs):  # noqa: E501
        """Create provider registration token for a user  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token for a specific user allowing him to register a new provider in Onezone. After the registration, the user's account will be automatically linked to the new Oneprovider cluster (granting him access to Oneprovider's onepanel).  If registration policy in Onezone is configured as `open`, any user can generate the token for himself. In case of `restricted` policy or issuing the token for another user, this operation requires `oz_providers_invite` privilege.  ***Example cURL requests***  **Create provider registration token for a user** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/clusters/$CLUSTER_ID  {   \"token\": [     \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaW-0Y8\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_provider_registration_token_for_user(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id. (required)
        :return: ProviderRegistrationToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_provider_registration_token_for_user_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_provider_registration_token_for_user_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def create_provider_registration_token_for_user_with_http_info(self, id, **kwargs):  # noqa: E501
        """Create provider registration token for a user  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use one of: * [create named token](#operation/create_named_token_for_current_user) * [create temporary token](#operation/create_temporary_token_for_current_user)  Creates a token for a specific user allowing him to register a new provider in Onezone. After the registration, the user's account will be automatically linked to the new Oneprovider cluster (granting him access to Oneprovider's onepanel).  If registration policy in Onezone is configured as `open`, any user can generate the token for himself. In case of `restricted` policy or issuing the token for another user, this operation requires `oz_providers_invite` privilege.  ***Example cURL requests***  **Create provider registration token for a user** ```bash curl -u username:password -X POST \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/clusters/$CLUSTER_ID  {   \"token\": [     \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaW-0Y8\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_provider_registration_token_for_user_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id. (required)
        :return: ProviderRegistrationToken
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
                    " to method create_provider_registration_token_for_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_provider_registration_token_for_user`")  # noqa: E501

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
            '/users/{id}/clusters/provider_registration_token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProviderRegistrationToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_user(self, body, **kwargs):  # noqa: E501
        """Create new user  # noqa: E501

        Creates a new user.  This operation requires `oz_users_create` admin privilege.  ***Example cURL requests***  **Create new user** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"username\" : \"new_user\", \"password\": \"lS1c6FD2mxB2ff\" }' \\ https://$ZONE_HOST/api/v3/onezone/users ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserCreateRequest body: User name. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_user_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_user_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_user_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create new user  # noqa: E501

        Creates a new user.  This operation requires `oz_users_create` admin privilege.  ***Example cURL requests***  **Create new user** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"username\" : \"new_user\", \"password\": \"lS1c6FD2mxB2ff\" }' \\ https://$ZONE_HOST/api/v3/onezone/users ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserCreateRequest body: User name. (required)
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
                    " to method create_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_user`")  # noqa: E501

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
            '/users', 'POST',
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

    def create_user_group(self, body, **kwargs):  # noqa: E501
        """Create a new group for the current user  # noqa: E501

        Creates a new group for the current user. The user automatically becomes a member of this group.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Create new group** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"name\" : \"test_group\" , \"type\" : \"team\" }' \\ https://$ZONE_HOST/api/v3/onezone/user/groups ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_group(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Group body: New group parameters. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_user_group_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_user_group_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_user_group_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new group for the current user  # noqa: E501

        Creates a new group for the current user. The user automatically becomes a member of this group.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Create new group** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"name\" : \"test_group\" , \"type\" : \"team\" }' \\ https://$ZONE_HOST/api/v3/onezone/user/groups ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_group_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Group body: New group parameters. (required)
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
                    " to method create_user_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_user_group`")  # noqa: E501

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
            '/user/groups', 'POST',
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

    def create_user_handle(self, body, **kwargs):  # noqa: E501
        """Create a new handle for the current user  # noqa: E501

        Creates a new handle as current user.  This operation can be invoked on behalf of the current user only and requires 'handle_service_register_handle' privilege in the handle service where the new handle is to be registered  ***Example cURL requests***  **Create new user handle** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"handleServiceId\": \"ddb06ed993bae95f2f430664fff122f7\", \"resourceType\": \"Share\", \"resourceId\": \"4fa683cbda8d8f686d15d42720af431d\", \"metadata\": \"<?xml version=\\'1.0\\'?>...\" }' https://$ZONE_HOST/api/v3/onezone/user/handles ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_handle(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HandleRegistrationRequest body: New handle parameters. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_user_handle_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_user_handle_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_user_handle_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new handle for the current user  # noqa: E501

        Creates a new handle as current user.  This operation can be invoked on behalf of the current user only and requires 'handle_service_register_handle' privilege in the handle service where the new handle is to be registered  ***Example cURL requests***  **Create new user handle** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"handleServiceId\": \"ddb06ed993bae95f2f430664fff122f7\", \"resourceType\": \"Share\", \"resourceId\": \"4fa683cbda8d8f686d15d42720af431d\", \"metadata\": \"<?xml version=\\'1.0\\'?>...\" }' https://$ZONE_HOST/api/v3/onezone/user/handles ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_handle_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HandleRegistrationRequest body: New handle parameters. (required)
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
                    " to method create_user_handle" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_user_handle`")  # noqa: E501

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
            '/user/handles', 'POST',
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

    def create_user_harvester(self, body, **kwargs):  # noqa: E501
        """Create a new harvester for the current user  # noqa: E501

        Creates a new harvester as current user. The user automaticaly becomes the harvesters' member.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Create new user harvester** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -X POST -d '{ \"name\" : \"new_harvester\", \"endpoint\" : \"example.elastic.com:9200\", \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\"  \\ \"config\" : { \"typeMapping\": [ { \"id\": 0, \"name\": \"Type 1\" }, { \"id\": 1, \"name\": \"Type 1\" } ],              \"externalHelpLink\": \"http://example.com/some_help_page\",              \"refreshDataTimeout\": 1000 }, \\ https://$ZONE_HOST/api/v3/onezone/user/harvesters ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_harvester(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HarvesterCreateRequest body: New harvester parameters. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_user_harvester_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_user_harvester_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_user_harvester_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new harvester for the current user  # noqa: E501

        Creates a new harvester as current user. The user automaticaly becomes the harvesters' member.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Create new user harvester** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -X POST -d '{ \"name\" : \"new_harvester\", \"endpoint\" : \"example.elastic.com:9200\", \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\"  \\ \"config\" : { \"typeMapping\": [ { \"id\": 0, \"name\": \"Type 1\" }, { \"id\": 1, \"name\": \"Type 1\" } ],              \"externalHelpLink\": \"http://example.com/some_help_page\",              \"refreshDataTimeout\": 1000 }, \\ https://$ZONE_HOST/api/v3/onezone/user/harvesters ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_harvester_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HarvesterCreateRequest body: New harvester parameters. (required)
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
                    " to method create_user_harvester" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_user_harvester`")  # noqa: E501

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
            '/user/harvesters', 'POST',
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

    def create_user_space(self, body, **kwargs):  # noqa: E501
        """Create a new space for the current user  # noqa: E501

        Creates a new space as current user. The user automaticaly becomes the spaces' member.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Create new user space** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"name\" : \"test_space\"}' https://$ZONE_HOST/api/v3/onezone/user/spaces ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_space(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SpaceCreateRequest body: New space parameters. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # kwargs['_return_http_data_only'] = True
        kwargs['_return_http_data_only'] = False
        if kwargs.get('async_req'):
            return self.create_user_space_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_user_space_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_user_space_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new space for the current user  # noqa: E501

        Creates a new space as current user. The user automaticaly becomes the spaces' member.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Create new user space** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"name\" : \"test_space\"}' https://$ZONE_HOST/api/v3/onezone/user/spaces ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_space_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SpaceCreateRequest body: New space parameters. (required)
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
                    " to method create_user_space" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_user_space`")  # noqa: E501

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
            '/user/spaces', 'POST',
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

    def get_current_user(self, **kwargs):  # noqa: E501
        """Get current user details  # noqa: E501

        Returns details about currently authenticated user.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user details** ```bash curl -u admin:password -X GET https://$ZONE_HOST/api/v3/onezone/user  {   \"userId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"fullName\": \"Rudolf Lingens\",   \"username\": \"r.lingens\",   \"linkedAccounts\": [     {       \"idp\": \"github\",       \"subjectId\": \"1978f5775ae2dc16730418bf3fc81764\"     },     {       \"idp\": \"elixir\",       \"subjectId\": \"38bf3fc2f4c16730481764bd775ae2d1\"     }   ],   \"emails\": [     \"rudolf.lingens@example.com\",     \"john.doe@example.com\"   ],   \"basicAuthEnabled\": false,   \"blocked\": false,   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UserProtectedInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_current_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_current_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_current_user_with_http_info(self, **kwargs):  # noqa: E501
        """Get current user details  # noqa: E501

        Returns details about currently authenticated user.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user details** ```bash curl -u admin:password -X GET https://$ZONE_HOST/api/v3/onezone/user  {   \"userId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"fullName\": \"Rudolf Lingens\",   \"username\": \"r.lingens\",   \"linkedAccounts\": [     {       \"idp\": \"github\",       \"subjectId\": \"1978f5775ae2dc16730418bf3fc81764\"     },     {       \"idp\": \"elixir\",       \"subjectId\": \"38bf3fc2f4c16730481764bd775ae2d1\"     }   ],   \"emails\": [     \"rudolf.lingens@example.com\",     \"john.doe@example.com\"   ],   \"basicAuthEnabled\": false,   \"blocked\": false,   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_user_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UserProtectedInfo
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
                    " to method get_current_user" % key
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
            '/user', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserProtectedInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_effective_user_harvester(self, hid, **kwargs):  # noqa: E501
        """Get effective harvester details  # noqa: E501

        Returns information about a specific effective harvester to which the user has access.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective harvester** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_harvesters/$HARVESTER_ID  {   \"harvesterId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_harvester1\",   \"public\" : true,   \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\",   \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_user_harvester(hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hid: Harvester Id. (required)
        :return: Harvester
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_user_harvester_with_http_info(hid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_user_harvester_with_http_info(hid, **kwargs)  # noqa: E501
            return data

    def get_effective_user_harvester_with_http_info(self, hid, **kwargs):  # noqa: E501
        """Get effective harvester details  # noqa: E501

        Returns information about a specific effective harvester to which the user has access.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective harvester** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_harvesters/$HARVESTER_ID  {   \"harvesterId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_harvester1\",   \"public\" : true,   \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\",   \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_user_harvester_with_http_info(hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hid: Harvester Id. (required)
        :return: Harvester
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_effective_user_harvester" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hid' is set
        if ('hid' not in params or
                params['hid'] is None):
            raise ValueError("Missing the required parameter `hid` when calling `get_effective_user_harvester`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/user/effective_harvesters/{hid}', 'GET',
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

    def get_effective_user_space(self, sid, **kwargs):  # noqa: E501
        """Get effective space details  # noqa: E501

        Returns information about a specific effective space to which the user has access.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective space** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_spaces/$SPACE_ID  {   \"spaceId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_space1\",   \"providers\": {     \"296ebe3c20e9666dc489b647f8647f12\" : 5368709120   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebfc1a770c3\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_user_space(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id. (required)
        :return: Space
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_effective_user_space_with_http_info(sid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_effective_user_space_with_http_info(sid, **kwargs)  # noqa: E501
            return data

    def get_effective_user_space_with_http_info(self, sid, **kwargs):  # noqa: E501
        """Get effective space details  # noqa: E501

        Returns information about a specific effective space to which the user has access.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective space** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_spaces/$SPACE_ID  {   \"spaceId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_space1\",   \"providers\": {     \"296ebe3c20e9666dc489b647f8647f12\" : 5368709120   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebfc1a770c3\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_effective_user_space_with_http_info(sid, async_req=True)
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
                    " to method get_effective_user_space" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `get_effective_user_space`")  # noqa: E501

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
            '/user/effective_spaces/{sid}', 'GET',
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

    def get_space_membership_requests(self, **kwargs):  # noqa: E501
        """Get summary of space membership requests  # noqa: E501

        Returns the summary of user's space membership requests.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get summary of space membership requests** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/space_membership_requests  {   \"pending\": {     \"715f5cf924cf8f69899a4ee8bbce8120\": {       \"requestId\": \"585110fde9d1a52c93f8eb22c0614e47\",       \"contactEmail\": \"user@example.com\",       \"lastActivity\": 1563819329     },     \"6db7e3095d8aedf5c145ef576339b10d\": {       \"requestId\": \"97216a666edd09945880a0785ad66a7b\",       \"contactEmail\": \"user@example.com\",       \"lastActivity\": 1563819923     }   },   \"rejected\": {      \"ee7aa1c60642646b9a5d1962dcd02b89\": {       \"requestId\": \"8467b1458989b8454a2faa8b5a45df7b\",       \"contactEmail\": \"user@example.com\",       \"lastActivity\": 1563823164     }   } } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_membership_requests(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: SpaceMembershipRequests
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_space_membership_requests_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_space_membership_requests_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_space_membership_requests_with_http_info(self, **kwargs):  # noqa: E501
        """Get summary of space membership requests  # noqa: E501

        Returns the summary of user's space membership requests.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get summary of space membership requests** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/space_membership_requests  {   \"pending\": {     \"715f5cf924cf8f69899a4ee8bbce8120\": {       \"requestId\": \"585110fde9d1a52c93f8eb22c0614e47\",       \"contactEmail\": \"user@example.com\",       \"lastActivity\": 1563819329     },     \"6db7e3095d8aedf5c145ef576339b10d\": {       \"requestId\": \"97216a666edd09945880a0785ad66a7b\",       \"contactEmail\": \"user@example.com\",       \"lastActivity\": 1563819923     }   },   \"rejected\": {      \"ee7aa1c60642646b9a5d1962dcd02b89\": {       \"requestId\": \"8467b1458989b8454a2faa8b5a45df7b\",       \"contactEmail\": \"user@example.com\",       \"lastActivity\": 1563823164     }   } } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_membership_requests_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: SpaceMembershipRequests
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
                    " to method get_space_membership_requests" % key
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
            '/user/space_membership_requests', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SpaceMembershipRequests',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user(self, id, **kwargs):  # noqa: E501
        """Get user details  # noqa: E501

        Returns the information about a specific user.  This operation requires `oz_users_view` admin privilege.  ***Example cURL requests***  **Get user details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID  {   \"userId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"fullName\": \"Rudolf Lingens\",   \"username\": \"r.lingens\",   \"linkedAccounts\": [     {       \"idp\": \"github\",       \"subjectId\": \"1978f5775ae2dc16730418bf3fc81764\"     },     {       \"idp\": \"elixir\",       \"subjectId\": \"38bf3fc2f4c16730481764bd775ae2d1\"     }   ],   \"emails\": [     \"rudolf.lingens@example.com\",     \"john.doe@example.com\"   ],   \"basicAuthEnabled\": false,   \"blocked\": false,   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id. (required)
        :return: UserProtectedInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_user_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get user details  # noqa: E501

        Returns the information about a specific user.  This operation requires `oz_users_view` admin privilege.  ***Example cURL requests***  **Get user details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID  {   \"userId\": \"f1c8b1a37aa7447b22eb65a742d40524\",   \"fullName\": \"Rudolf Lingens\",   \"username\": \"r.lingens\",   \"linkedAccounts\": [     {       \"idp\": \"github\",       \"subjectId\": \"1978f5775ae2dc16730418bf3fc81764\"     },     {       \"idp\": \"elixir\",       \"subjectId\": \"38bf3fc2f4c16730481764bd775ae2d1\"     }   ],   \"emails\": [     \"rudolf.lingens@example.com\",     \"john.doe@example.com\"   ],   \"basicAuthEnabled\": false,   \"blocked\": false,   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id. (required)
        :return: UserProtectedInfo
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
                    " to method get_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_user`")  # noqa: E501

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
            '/users/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserProtectedInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_cluster(self, cid, **kwargs):  # noqa: E501
        """Get user's cluster details  # noqa: E501

        Returns the details of a specific user's cluster.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user's cluster details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/clusters/$CLUSTER_ID  {   \"clusterId\": \"f8d843beda24e54545455ecc0f4b8886\",   \"type\": \"oneprovider\",   \"workerVersion\": {     \"release\": \"21.02.3\",     \"build\": \"1-gfabf02d\",     \"gui\": \"129c549fbe9b3e730c3d9910492228566e39e1236945766a74381405cc57fb04\"   },   \"onepanelVersion\": {     \"release\": \"21.02.3\",     \"build\": \"3-89fc6bad\",     \"gui\": \"68e7e1472adb719ddf2d88908775091dfb10e5d0b916f06125ea1af4056044e3\"   },   \"online\": true,   \"onepanelProxy\": false,   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_cluster(cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cid: Cluster Id. (required)
        :return: Cluster
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_cluster_with_http_info(cid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_cluster_with_http_info(cid, **kwargs)  # noqa: E501
            return data

    def get_user_cluster_with_http_info(self, cid, **kwargs):  # noqa: E501
        """Get user's cluster details  # noqa: E501

        Returns the details of a specific user's cluster.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user's cluster details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/clusters/$CLUSTER_ID  {   \"clusterId\": \"f8d843beda24e54545455ecc0f4b8886\",   \"type\": \"oneprovider\",   \"workerVersion\": {     \"release\": \"21.02.3\",     \"build\": \"1-gfabf02d\",     \"gui\": \"129c549fbe9b3e730c3d9910492228566e39e1236945766a74381405cc57fb04\"   },   \"onepanelVersion\": {     \"release\": \"21.02.3\",     \"build\": \"3-89fc6bad\",     \"gui\": \"68e7e1472adb719ddf2d88908775091dfb10e5d0b916f06125ea1af4056044e3\"   },   \"online\": true,   \"onepanelProxy\": false,   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_cluster_with_http_info(cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cid: Cluster Id. (required)
        :return: Cluster
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_cluster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cid' is set
        if ('cid' not in params or
                params['cid'] is None):
            raise ValueError("Missing the required parameter `cid` when calling `get_user_cluster`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/user/clusters/{cid}', 'GET',
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

    def get_user_effective_cluster(self, cid, **kwargs):  # noqa: E501
        """Get user's effective cluster details  # noqa: E501

        Returns information about a specific user's effective cluster.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user's effective cluster details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/clusters/$CLUSTER_ID  {   \"clusterId\": \"f8d843beda24e54545455ecc0f4b8886\",   \"type\": \"oneprovider\",   \"workerVersion\": {     \"release\": \"21.02.3\",     \"build\": \"1-gfabf02d\",     \"gui\": \"129c549fbe9b3e730c3d9910492228566e39e1236945766a74381405cc57fb04\"   },   \"onepanelVersion\": {     \"release\": \"21.02.3\",     \"build\": \"3-89fc6bad\",     \"gui\": \"68e7e1472adb719ddf2d88908775091dfb10e5d0b916f06125ea1af4056044e3\"   },   \"online\": true,   \"onepanelProxy\": false,   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_effective_cluster(cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cid: Cluster Id. (required)
        :return: Cluster
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_effective_cluster_with_http_info(cid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_effective_cluster_with_http_info(cid, **kwargs)  # noqa: E501
            return data

    def get_user_effective_cluster_with_http_info(self, cid, **kwargs):  # noqa: E501
        """Get user's effective cluster details  # noqa: E501

        Returns information about a specific user's effective cluster.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user's effective cluster details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/clusters/$CLUSTER_ID  {   \"clusterId\": \"f8d843beda24e54545455ecc0f4b8886\",   \"type\": \"oneprovider\",   \"workerVersion\": {     \"release\": \"21.02.3\",     \"build\": \"1-gfabf02d\",     \"gui\": \"129c549fbe9b3e730c3d9910492228566e39e1236945766a74381405cc57fb04\"   },   \"onepanelVersion\": {     \"release\": \"21.02.3\",     \"build\": \"3-89fc6bad\",     \"gui\": \"68e7e1472adb719ddf2d88908775091dfb10e5d0b916f06125ea1af4056044e3\"   },   \"online\": true,   \"onepanelProxy\": false,   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_effective_cluster_with_http_info(cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cid: Cluster Id. (required)
        :return: Cluster
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_effective_cluster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cid' is set
        if ('cid' not in params or
                params['cid'] is None):
            raise ValueError("Missing the required parameter `cid` when calling `get_user_effective_cluster`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/user/effective_clusters/{cid}', 'GET',
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

    def get_user_effective_group(self, gid, **kwargs):  # noqa: E501
        """Get effective group details  # noqa: E501

        Returns information about a specific effective group to which the user has access.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user's effective group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_groups/$GROUP_ID  {   \"groupId\": \"59fec3bd894eef1cdae81623f477e370\",   \"name\": \"admins\",   \"type\": \"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_effective_group(gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gid: Group Id. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_effective_group_with_http_info(gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_effective_group_with_http_info(gid, **kwargs)  # noqa: E501
            return data

    def get_user_effective_group_with_http_info(self, gid, **kwargs):  # noqa: E501
        """Get effective group details  # noqa: E501

        Returns information about a specific effective group to which the user has access.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user's effective group details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_groups/$GROUP_ID  {   \"groupId\": \"59fec3bd894eef1cdae81623f477e370\",   \"name\": \"admins\",   \"type\": \"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_effective_group_with_http_info(gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gid: Group Id. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_effective_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `get_user_effective_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/user/effective_groups/{gid}', 'GET',
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

    def get_user_effective_handle(self, hid, **kwargs):  # noqa: E501
        """Get effective handle details  # noqa: E501

        Returns information about a specific effective handle to which the user has access.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective handle** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_handles/$HANDLE_ID  {   \"publicHandle\": \"10.5072/w95Zlng\",   \"handleId\": \"95b663a6467c72ab1256865efef9e387\",   \"handleServiceId\": \"97c27230017cd54c1220189e357322c4\",   \"resourceType\": \"Share\",   \"resourceId\": \"d6ee1aecf03b23f09756d6a49e435455\",   \"metadata\": \"<?xml version=\\\"1.0\\\"?>       <!DOCTYPE rdf:RDF SYSTEM \\\\\"http://dublincore.org/2000/12/01-dcmes-xml-dtd.dtd\\\">       <rdf:RDF xmlns:rdf=\\\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\\\"                xmlns:dc=\\\"http://purl.org/dc/elements/1.1/\\\">         <rdf:Description rdf:about=\\\"http://example.com/resouces/1\\\">           <dc:title>Example Resource</dc:title>           <dc:creator>John Doe</dc:creator>           <dc:publisher>MIT</dc:publisher>           <dc:date>2000-06-06</dc:date>         </rdf:Description>       </rdf:RDF>\",   \"timestamp\": \"1997-07-16T19:20\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_effective_handle(hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hid: Handle Id. (required)
        :return: Handle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_effective_handle_with_http_info(hid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_effective_handle_with_http_info(hid, **kwargs)  # noqa: E501
            return data

    def get_user_effective_handle_with_http_info(self, hid, **kwargs):  # noqa: E501
        """Get effective handle details  # noqa: E501

        Returns information about a specific effective handle to which the user has access.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective handle** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_handles/$HANDLE_ID  {   \"publicHandle\": \"10.5072/w95Zlng\",   \"handleId\": \"95b663a6467c72ab1256865efef9e387\",   \"handleServiceId\": \"97c27230017cd54c1220189e357322c4\",   \"resourceType\": \"Share\",   \"resourceId\": \"d6ee1aecf03b23f09756d6a49e435455\",   \"metadata\": \"<?xml version=\\\"1.0\\\"?>       <!DOCTYPE rdf:RDF SYSTEM \\\\\"http://dublincore.org/2000/12/01-dcmes-xml-dtd.dtd\\\">       <rdf:RDF xmlns:rdf=\\\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\\\"                xmlns:dc=\\\"http://purl.org/dc/elements/1.1/\\\">         <rdf:Description rdf:about=\\\"http://example.com/resouces/1\\\">           <dc:title>Example Resource</dc:title>           <dc:creator>John Doe</dc:creator>           <dc:publisher>MIT</dc:publisher>           <dc:date>2000-06-06</dc:date>         </rdf:Description>       </rdf:RDF>\",   \"timestamp\": \"1997-07-16T19:20\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_effective_handle_with_http_info(hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hid: Handle Id. (required)
        :return: Handle
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_effective_handle" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hid' is set
        if ('hid' not in params or
                params['hid'] is None):
            raise ValueError("Missing the required parameter `hid` when calling `get_user_effective_handle`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/user/effective_handles/{hid}', 'GET',
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

    def get_user_effective_handle_service(self, hsid, **kwargs):  # noqa: E501
        """Get effective handle service details  # noqa: E501

        Returns information about a specific effective handle service for the user.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective handle service** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_handle_services/$HANDLE_SERVICE_ID  {     \"name\": \"MyCommunity Handle service\",     \"proxyEndpoint\": \"https://localhost:17000/handle_proxy\",     \"serviceProperties\": {         \"allowTemplateOverride\": false,         \"doiEndpoint\": \"/doi\",         \"host\": \"https://mds.test.datacite.org\",         \"identifierTemplate\": \"{{space.name}}-{{space.guid}}\",         \"mediaEndpoint\": \"/media\",         \"metadataEndpoint\": \"/metadata\",         \"password\": \"pa$$word\",         \"prefix\": 10.5072,         \"type\": \"DOI\",         \"username\": \"alice\"     } } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_effective_handle_service(hsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hsid: Handle service Id. (required)
        :return: HandleService
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_effective_handle_service_with_http_info(hsid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_effective_handle_service_with_http_info(hsid, **kwargs)  # noqa: E501
            return data

    def get_user_effective_handle_service_with_http_info(self, hsid, **kwargs):  # noqa: E501
        """Get effective handle service details  # noqa: E501

        Returns information about a specific effective handle service for the user.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective handle service** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_handle_services/$HANDLE_SERVICE_ID  {     \"name\": \"MyCommunity Handle service\",     \"proxyEndpoint\": \"https://localhost:17000/handle_proxy\",     \"serviceProperties\": {         \"allowTemplateOverride\": false,         \"doiEndpoint\": \"/doi\",         \"host\": \"https://mds.test.datacite.org\",         \"identifierTemplate\": \"{{space.name}}-{{space.guid}}\",         \"mediaEndpoint\": \"/media\",         \"metadataEndpoint\": \"/metadata\",         \"password\": \"pa$$word\",         \"prefix\": 10.5072,         \"type\": \"DOI\",         \"username\": \"alice\"     } } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_effective_handle_service_with_http_info(hsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hsid: Handle service Id. (required)
        :return: HandleService
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hsid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_effective_handle_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hsid' is set
        if ('hsid' not in params or
                params['hsid'] is None):
            raise ValueError("Missing the required parameter `hsid` when calling `get_user_effective_handle_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/user/effective_handle_services/{hsid}', 'GET',
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

    def get_user_effective_provider(self, pid, **kwargs):  # noqa: E501
        """Get user's effective provider details  # noqa: E501

        Returns information about a specific effective provider for the user.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective provider** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_providers/$PROVIDER_ID  {   \"providerId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"name\": \"Example provider\",   \"domain\": \"provider1.example.com\",   \"latitude\": 50.0647,   \"longitude\": 19.945,   \"clusterId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"online\": true,   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_effective_provider(pid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pid: Provider Id. (required)
        :return: ProviderDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_effective_provider_with_http_info(pid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_effective_provider_with_http_info(pid, **kwargs)  # noqa: E501
            return data

    def get_user_effective_provider_with_http_info(self, pid, **kwargs):  # noqa: E501
        """Get user's effective provider details  # noqa: E501

        Returns information about a specific effective provider for the user.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective provider** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_providers/$PROVIDER_ID  {   \"providerId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"name\": \"Example provider\",   \"domain\": \"provider1.example.com\",   \"latitude\": 50.0647,   \"longitude\": 19.945,   \"clusterId\": \"6b9bc70630547d925861a27e1f050dfe\",   \"online\": true,   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_effective_provider_with_http_info(pid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pid: Provider Id. (required)
        :return: ProviderDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_effective_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pid' is set
        if ('pid' not in params or
                params['pid'] is None):
            raise ValueError("Missing the required parameter `pid` when calling `get_user_effective_provider`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/user/effective_providers/{pid}', 'GET',
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

    def get_user_group(self, gid, **kwargs):  # noqa: E501
        """Get group details  # noqa: E501

        Returns information about a specific group to which the user has access.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/groups/$GROUP_ID  {   \"groupId\": \"59fec3bd894eef1cdae81623f477e370\",   \"name\": \"admins\",   \"type\": \"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_group(gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gid: Group Id. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_group_with_http_info(gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_group_with_http_info(gid, **kwargs)  # noqa: E501
            return data

    def get_user_group_with_http_info(self, gid, **kwargs):  # noqa: E501
        """Get group details  # noqa: E501

        Returns information about a specific group to which the user has access.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user groups** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/groups/$GROUP_ID  {   \"groupId\": \"59fec3bd894eef1cdae81623f477e370\",   \"name\": \"admins\",   \"type\": \"team\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_group_with_http_info(gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gid: Group Id. (required)
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `get_user_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/user/groups/{gid}', 'GET',
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

    def get_user_handle(self, hid, **kwargs):  # noqa: E501
        """Get handle details  # noqa: E501

        Returns the details of a specific handle.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get handle details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/handles/$HANDLE_ID  {   \"publicHandle\": \"10.5072/w95Zlng\",   \"handleId\": \"95b663a6467c72ab1256865efef9e387\",   \"handleServiceId\": \"97c27230017cd54c1220189e357322c4\",   \"resourceType\": \"Share\",   \"resourceId\": \"d6ee1aecf03b23f09756d6a49e435455\",   \"metadata\": \"<?xml version=\\\"1.0\\\"?>       <!DOCTYPE rdf:RDF SYSTEM \\\\\"http://dublincore.org/2000/12/01-dcmes-xml-dtd.dtd\\\">       <rdf:RDF xmlns:rdf=\\\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\\\"                xmlns:dc=\\\"http://purl.org/dc/elements/1.1/\\\">         <rdf:Description rdf:about=\\\"http://example.com/resouces/1\\\">           <dc:title>Example Resource</dc:title>           <dc:creator>John Doe</dc:creator>           <dc:publisher>MIT</dc:publisher>           <dc:date>2000-06-06</dc:date>         </rdf:Description>       </rdf:RDF>\",   \"timestamp\": \"1997-07-16T19:20\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_handle(hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hid: Handle Id. (required)
        :return: Handle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_handle_with_http_info(hid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_handle_with_http_info(hid, **kwargs)  # noqa: E501
            return data

    def get_user_handle_with_http_info(self, hid, **kwargs):  # noqa: E501
        """Get handle details  # noqa: E501

        Returns the details of a specific handle.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get handle details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/handles/$HANDLE_ID  {   \"publicHandle\": \"10.5072/w95Zlng\",   \"handleId\": \"95b663a6467c72ab1256865efef9e387\",   \"handleServiceId\": \"97c27230017cd54c1220189e357322c4\",   \"resourceType\": \"Share\",   \"resourceId\": \"d6ee1aecf03b23f09756d6a49e435455\",   \"metadata\": \"<?xml version=\\\"1.0\\\"?>       <!DOCTYPE rdf:RDF SYSTEM \\\\\"http://dublincore.org/2000/12/01-dcmes-xml-dtd.dtd\\\">       <rdf:RDF xmlns:rdf=\\\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\\\"                xmlns:dc=\\\"http://purl.org/dc/elements/1.1/\\\">         <rdf:Description rdf:about=\\\"http://example.com/resouces/1\\\">           <dc:title>Example Resource</dc:title>           <dc:creator>John Doe</dc:creator>           <dc:publisher>MIT</dc:publisher>           <dc:date>2000-06-06</dc:date>         </rdf:Description>       </rdf:RDF>\",   \"timestamp\": \"1997-07-16T19:20\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_handle_with_http_info(hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hid: Handle Id. (required)
        :return: Handle
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_handle" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hid' is set
        if ('hid' not in params or
                params['hid'] is None):
            raise ValueError("Missing the required parameter `hid` when calling `get_user_handle`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/user/handles/{hid}', 'GET',
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

    def get_user_handle_service(self, hsid, **kwargs):  # noqa: E501
        """Get user handle service details  # noqa: E501

        Returns the details of a specific handle service.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get handle service details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/handle_services/$HANDLE_SERVICE_ID  {     \"name\": \"MyCommunity Handle service\",     \"proxyEndpoint\": \"https://localhost:17000/handle_proxy\",     \"serviceProperties\": {         \"allowTemplateOverride\": false,         \"doiEndpoint\": \"/doi\",         \"host\": \"https://mds.test.datacite.org\",         \"identifierTemplate\": \"{{space.name}}-{{space.guid}}\",         \"mediaEndpoint\": \"/media\",         \"metadataEndpoint\": \"/metadata\",         \"password\": \"pa$$word\",         \"prefix\": 10.5072,         \"type\": \"DOI\",         \"username\": \"alice\"     } } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_handle_service(hsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hsid: Handle service Id. (required)
        :return: HandleService
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_handle_service_with_http_info(hsid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_handle_service_with_http_info(hsid, **kwargs)  # noqa: E501
            return data

    def get_user_handle_service_with_http_info(self, hsid, **kwargs):  # noqa: E501
        """Get user handle service details  # noqa: E501

        Returns the details of a specific handle service.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get handle service details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/handle_services/$HANDLE_SERVICE_ID  {     \"name\": \"MyCommunity Handle service\",     \"proxyEndpoint\": \"https://localhost:17000/handle_proxy\",     \"serviceProperties\": {         \"allowTemplateOverride\": false,         \"doiEndpoint\": \"/doi\",         \"host\": \"https://mds.test.datacite.org\",         \"identifierTemplate\": \"{{space.name}}-{{space.guid}}\",         \"mediaEndpoint\": \"/media\",         \"metadataEndpoint\": \"/metadata\",         \"password\": \"pa$$word\",         \"prefix\": 10.5072,         \"type\": \"DOI\",         \"username\": \"alice\"     } } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_handle_service_with_http_info(hsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hsid: Handle service Id. (required)
        :return: HandleService
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hsid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_handle_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hsid' is set
        if ('hsid' not in params or
                params['hsid'] is None):
            raise ValueError("Missing the required parameter `hsid` when calling `get_user_handle_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/user/handle_services/{hsid}', 'GET',
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

    def get_user_harvester(self, hid, **kwargs):  # noqa: E501
        """Get harvester details  # noqa: E501

        Returns the details of a specific harvester.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get harvester details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/harvesters/$HARVESTER_ID  {   \"harvesterId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_harvester1\",   \"public\" : true,   \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\",   \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_harvester(hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hid: Harvester Id. (required)
        :return: Harvester
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_harvester_with_http_info(hid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_harvester_with_http_info(hid, **kwargs)  # noqa: E501
            return data

    def get_user_harvester_with_http_info(self, hid, **kwargs):  # noqa: E501
        """Get harvester details  # noqa: E501

        Returns the details of a specific harvester.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get harvester details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/harvesters/$HARVESTER_ID  {   \"harvesterId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_harvester1\",   \"public\" : true,   \"harvestingBackendType\" : \"elasticsearch_harvesting_backend\",   \"harvestingBackendEndpoint\" : \"example.elastic.com:9200\",   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebf\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_harvester_with_http_info(hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hid: Harvester Id. (required)
        :return: Harvester
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_harvester" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hid' is set
        if ('hid' not in params or
                params['hid'] is None):
            raise ValueError("Missing the required parameter `hid` when calling `get_user_harvester`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/user/harvesters/{hid}', 'GET',
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

    def get_user_space(self, sid, **kwargs):  # noqa: E501
        """Get space details  # noqa: E501

        Returns the details of a specific space.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get space details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/spaces/$SPACE_ID  {   \"spaceId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_space1\",   \"providers\": {     \"296ebe3c20e9666dc489b647f8647f12\" : 5368709120   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebfc1a770c3\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_space(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id. (required)
        :return: Space
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_space_with_http_info(sid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_space_with_http_info(sid, **kwargs)  # noqa: E501
            return data

    def get_user_space_with_http_info(self, sid, **kwargs):  # noqa: E501
        """Get space details  # noqa: E501

        Returns the details of a specific space.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get space details** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/spaces/$SPACE_ID  {   \"spaceId\": \"2c0160248ba9a66f45da751ca459535a\",   \"name\": \"new_space1\",   \"providers\": {     \"296ebe3c20e9666dc489b647f8647f12\" : 5368709120   },   \"creator\": {     \"type\": \"user\",     \"id\": \"7434b256e71e1052e0d5e3e9da657ebfc1a770c3\"   },   \"creationTime\": 1576152793 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_space_with_http_info(sid, async_req=True)
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
                    " to method get_user_space" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `get_user_space`")  # noqa: E501

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
            '/user/spaces/{sid}', 'GET',
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

    def get_user_space_alias(self, sid, **kwargs):  # noqa: E501
        """Get user space alias  # noqa: E501

        Returns the alias (user defined name) for a specific space. Will return 404 NOT FOUND if no alias is defined for the space.  NOTE: Space aliases are not yet implemented - setting an alias is possible but will have no effect.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get space alias** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/spaces/$SPACE_ID/alias  {   \"alias\": \"Test space 2\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_space_alias(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id. (required)
        :return: SpaceAlias
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_space_alias_with_http_info(sid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_space_alias_with_http_info(sid, **kwargs)  # noqa: E501
            return data

    def get_user_space_alias_with_http_info(self, sid, **kwargs):  # noqa: E501
        """Get user space alias  # noqa: E501

        Returns the alias (user defined name) for a specific space. Will return 404 NOT FOUND if no alias is defined for the space.  NOTE: Space aliases are not yet implemented - setting an alias is possible but will have no effect.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get space alias** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/spaces/$SPACE_ID/alias  {   \"alias\": \"Test space 2\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_space_alias_with_http_info(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id. (required)
        :return: SpaceAlias
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
                    " to method get_user_space_alias" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `get_user_space_alias`")  # noqa: E501

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
            '/user/spaces/{sid}/alias', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SpaceAlias',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_spaces_in_effective_provider(self, pid, **kwargs):  # noqa: E501
        """Get user's spaces that are supported by given effective provider  # noqa: E501

        Returns the list of user's spaces that are supported by given effective provider.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user's spaces supported by effective provider** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_providers/$PROVIDER_ID/spaces  {   \"spaces\": [     \"6825604b0eb6a47b8b7a04b6369eb24d\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_spaces_in_effective_provider(pid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pid: Provider Id. (required)
        :return: Spaces
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_spaces_in_effective_provider_with_http_info(pid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_spaces_in_effective_provider_with_http_info(pid, **kwargs)  # noqa: E501
            return data

    def get_user_spaces_in_effective_provider_with_http_info(self, pid, **kwargs):  # noqa: E501
        """Get user's spaces that are supported by given effective provider  # noqa: E501

        Returns the list of user's spaces that are supported by given effective provider.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user's spaces supported by effective provider** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_providers/$PROVIDER_ID/spaces  {   \"spaces\": [     \"6825604b0eb6a47b8b7a04b6369eb24d\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_spaces_in_effective_provider_with_http_info(pid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pid: Provider Id. (required)
        :return: Spaces
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_spaces_in_effective_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pid' is set
        if ('pid' not in params or
                params['pid'] is None):
            raise ValueError("Missing the required parameter `pid` when calling `get_user_spaces_in_effective_provider`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/user/effective_providers/{pid}/spaces', 'GET',
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

    def join_group(self, body, **kwargs):  # noqa: E501
        """Join group  # noqa: E501

        Join existing group using an invitation token.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Join group**  ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"token\": \"9ef3973a007d616cb6b3e95829dec18a\" }' \\ https://$ZONE_HOST/api/v3/onezone/user/groups/join ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.join_group(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupInviteToken body: Token for joining a group. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.join_group_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.join_group_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def join_group_with_http_info(self, body, **kwargs):  # noqa: E501
        """Join group  # noqa: E501

        Join existing group using an invitation token.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Join group**  ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X POST -d '{ \"token\": \"9ef3973a007d616cb6b3e95829dec18a\" }' \\ https://$ZONE_HOST/api/v3/onezone/user/groups/join ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.join_group_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupInviteToken body: Token for joining a group. (required)
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
                    " to method join_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `join_group`")  # noqa: E501

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
            '/user/groups/join', 'POST',
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

    def join_harvester(self, body, **kwargs):  # noqa: E501
        """Join harvester  # noqa: E501

        Join existing harvester using invitation token.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Join existing harvester** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"token\" : \"MDAxNmxvY2F00aW9uRVM2TVo5UlZ5cGFjZV9jcmLciFsOgyUkPI3f02le6PM01IX8go\" }'  \\ https://$ZONE_HOST/api/v3/onezone/user/harvesters/join ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.join_harvester(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HarvesterInviteToken body: Token for joining a harvester. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.join_harvester_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.join_harvester_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def join_harvester_with_http_info(self, body, **kwargs):  # noqa: E501
        """Join harvester  # noqa: E501

        Join existing harvester using invitation token.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Join existing harvester** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"token\" : \"MDAxNmxvY2F00aW9uRVM2TVo5UlZ5cGFjZV9jcmLciFsOgyUkPI3f02le6PM01IX8go\" }'  \\ https://$ZONE_HOST/api/v3/onezone/user/harvesters/join ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.join_harvester_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HarvesterInviteToken body: Token for joining a harvester. (required)
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
                    " to method join_harvester" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `join_harvester`")  # noqa: E501

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
            '/user/harvesters/join', 'POST',
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

    def join_space(self, body, **kwargs):  # noqa: E501
        """Join space  # noqa: E501

        Join existing space using an invitation token.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Join an existing space** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"token\" : \"MDAxNmxvY2F00aW9uRVM2TVo5UlZ5cGFjZV9jcmLciFsOgyUkPI3f02le6PM01IX8go\" }'  \\ https://$ZONE_HOST/api/v3/onezone/user/spaces/join ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.join_space(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SpaceInviteToken body: Token for joining a space. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.join_space_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.join_space_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def join_space_with_http_info(self, body, **kwargs):  # noqa: E501
        """Join space  # noqa: E501

        Join existing space using an invitation token.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Join an existing space** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"token\" : \"MDAxNmxvY2F00aW9uRVM2TVo5UlZ5cGFjZV9jcmLciFsOgyUkPI3f02le6PM01IX8go\" }'  \\ https://$ZONE_HOST/api/v3/onezone/user/spaces/join ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.join_space_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SpaceInviteToken body: Token for joining a space. (required)
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
                    " to method join_space" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `join_space`")  # noqa: E501

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
            '/user/spaces/join', 'POST',
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

    def leave_group(self, gid, **kwargs):  # noqa: E501
        """Leave group  # noqa: E501

        Removes the current user from a specific group.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Leave group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.leave_group(gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gid: Group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.leave_group_with_http_info(gid, **kwargs)  # noqa: E501
        else:
            (data) = self.leave_group_with_http_info(gid, **kwargs)  # noqa: E501
            return data

    def leave_group_with_http_info(self, gid, **kwargs):  # noqa: E501
        """Leave group  # noqa: E501

        Removes the current user from a specific group.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Leave group** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/groups/$GROUP_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.leave_group_with_http_info(gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gid: Group Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method leave_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gid' is set
        if ('gid' not in params or
                params['gid'] is None):
            raise ValueError("Missing the required parameter `gid` when calling `leave_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/user/groups/{gid}', 'DELETE',
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

    def leave_handle_service(self, hsid, **kwargs):  # noqa: E501
        """Leave handle service  # noqa: E501

        Removes the user's ownership or access to a specific handle service.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Delete user handle service** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/handle_services/$HANDLE_SERVICE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.leave_handle_service(hsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hsid: Handle service Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.leave_handle_service_with_http_info(hsid, **kwargs)  # noqa: E501
        else:
            (data) = self.leave_handle_service_with_http_info(hsid, **kwargs)  # noqa: E501
            return data

    def leave_handle_service_with_http_info(self, hsid, **kwargs):  # noqa: E501
        """Leave handle service  # noqa: E501

        Removes the user's ownership or access to a specific handle service.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Delete user handle service** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/handle_services/$HANDLE_SERVICE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.leave_handle_service_with_http_info(hsid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hsid: Handle service Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hsid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method leave_handle_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hsid' is set
        if ('hsid' not in params or
                params['hsid'] is None):
            raise ValueError("Missing the required parameter `hsid` when calling `leave_handle_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/user/handle_services/{hsid}', 'DELETE',
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

    def leave_space(self, sid, **kwargs):  # noqa: E501
        """Leave space  # noqa: E501

        Removes the user's ownership or access to a specific space.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Delete user space** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/spaces/$SPACE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.leave_space(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.leave_space_with_http_info(sid, **kwargs)  # noqa: E501
        else:
            (data) = self.leave_space_with_http_info(sid, **kwargs)  # noqa: E501
            return data

    def leave_space_with_http_info(self, sid, **kwargs):  # noqa: E501
        """Leave space  # noqa: E501

        Removes the user's ownership or access to a specific space.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Delete user space** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/spaces/$SPACE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.leave_space_with_http_info(sid, async_req=True)
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
                    " to method leave_space" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `leave_space`")  # noqa: E501

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
            '/user/spaces/{sid}', 'DELETE',
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

    def list_client_tokens(self, **kwargs):  # noqa: E501
        """List user access tokens  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use [this one](#operation/list_named_tokens_of_current_user).  Returns the list of user tokens.  This operation can be invoked on behalf of currently authenticated user only.  ***Example cURL requests***  **Get user tokens** ```bash curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/user/client_tokens  {   \"tokens: [      \"12da582337ff25cc86db30580b20d3cd\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_client_tokens(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ClientTokens
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_client_tokens_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_client_tokens_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_client_tokens_with_http_info(self, **kwargs):  # noqa: E501
        """List user access tokens  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use [this one](#operation/list_named_tokens_of_current_user).  Returns the list of user tokens.  This operation can be invoked on behalf of currently authenticated user only.  ***Example cURL requests***  **Get user tokens** ```bash curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/user/client_tokens  {   \"tokens: [      \"12da582337ff25cc86db30580b20d3cd\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_client_tokens_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ClientTokens
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
                    " to method list_client_tokens" % key
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
            '/user/client_tokens', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClientTokens',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_current_user_admin_privileges(self, **kwargs):  # noqa: E501
        """List current user privileges  # noqa: E501

        Returns the list of currently authenticated user's admin privileges in Onezone.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **List current user's admin privileges in Onezone** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/user/privileges  {   \"privileges\": [     \"oz_view_privileges\",     \"oz_users_list\",     \"oz_users_view\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handles_list\",     \"oz_handles_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_current_user_admin_privileges(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_current_user_admin_privileges_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_current_user_admin_privileges_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_current_user_admin_privileges_with_http_info(self, **kwargs):  # noqa: E501
        """List current user privileges  # noqa: E501

        Returns the list of currently authenticated user's admin privileges in Onezone.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **List current user's admin privileges in Onezone** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/user/privileges  {   \"privileges\": [     \"oz_view_privileges\",     \"oz_users_list\",     \"oz_users_view\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handles_list\",     \"oz_handles_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_current_user_admin_privileges_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2001
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
                    " to method list_current_user_admin_privileges" % key
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
            '/user/privileges', 'GET',
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

    def list_current_user_effective_admin_privileges(self, **kwargs):  # noqa: E501
        """List current user effective privileges  # noqa: E501

        Returns the list of currently authenticated user's admin privileges in Onezone.  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **List user's effective admin privileges in Onezone** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/user/effective_privileges  {   \"privileges\": [     \"oz_view_privileges\",     \"oz_users_list\",     \"oz_users_view\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handles_list\",     \"oz_handles_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_current_user_effective_admin_privileges(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_current_user_effective_admin_privileges_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_current_user_effective_admin_privileges_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_current_user_effective_admin_privileges_with_http_info(self, **kwargs):  # noqa: E501
        """List current user effective privileges  # noqa: E501

        Returns the list of currently authenticated user's admin privileges in Onezone.  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **List user's effective admin privileges in Onezone** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/user/effective_privileges  {   \"privileges\": [     \"oz_view_privileges\",     \"oz_users_list\",     \"oz_users_view\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handles_list\",     \"oz_handles_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_current_user_effective_admin_privileges_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2001
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
                    " to method list_current_user_effective_admin_privileges" % key
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
            '/user/effective_privileges', 'GET',
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

    def list_effective_user_groups(self, **kwargs):  # noqa: E501
        """List effective user groups  # noqa: E501

        Returns the list of user's effective groups.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective groups** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_groups  {   \"groups\": [     \"admins\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_user_groups(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Groups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_user_groups_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_user_groups_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_effective_user_groups_with_http_info(self, **kwargs):  # noqa: E501
        """List effective user groups  # noqa: E501

        Returns the list of user's effective groups.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective groups** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_groups  {   \"groups\": [     \"admins\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_user_groups_with_http_info(async_req=True)
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
                    " to method list_effective_user_groups" % key
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
            '/user/effective_groups', 'GET',
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

    def list_effective_user_harvesters(self, **kwargs):  # noqa: E501
        """List effective user harvesters  # noqa: E501

        Returns the list of user's effective harvesters.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective harvesters** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_harvesters  {   \"harvesters\": [     \"40090ed592dc7975d2a9cd6bbe6c9a67\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_user_harvesters(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Harvesters
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_user_harvesters_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_user_harvesters_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_effective_user_harvesters_with_http_info(self, **kwargs):  # noqa: E501
        """List effective user harvesters  # noqa: E501

        Returns the list of user's effective harvesters.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective harvesters** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_harvesters  {   \"harvesters\": [     \"40090ed592dc7975d2a9cd6bbe6c9a67\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_user_harvesters_with_http_info(async_req=True)
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
                    " to method list_effective_user_harvesters" % key
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
            '/user/effective_harvesters', 'GET',
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

    def list_effective_user_providers(self, **kwargs):  # noqa: E501
        """List user effective providers  # noqa: E501

        Returns the list of user's effective providers.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective providers** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_providers  {   \"providers\": [     \"LKJASHGDFKLJHASKLJDH\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_user_providers(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Providers
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_user_providers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_user_providers_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_effective_user_providers_with_http_info(self, **kwargs):  # noqa: E501
        """List user effective providers  # noqa: E501

        Returns the list of user's effective providers.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective providers** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_providers  {   \"providers\": [     \"LKJASHGDFKLJHASKLJDH\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_user_providers_with_http_info(async_req=True)
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
                    " to method list_effective_user_providers" % key
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
            '/user/effective_providers', 'GET',
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

    def list_effective_user_spaces(self, **kwargs):  # noqa: E501
        """List effective user spaces  # noqa: E501

        Returns the list of user's effective spaces.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective spaces** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_spaces  {   \"spaces\": [     \"40090ed592dc7975d2a9cd6bbe6c9a67\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_user_spaces(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Spaces
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_effective_user_spaces_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_effective_user_spaces_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_effective_user_spaces_with_http_info(self, **kwargs):  # noqa: E501
        """List effective user spaces  # noqa: E501

        Returns the list of user's effective spaces.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective spaces** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_spaces  {   \"spaces\": [     \"40090ed592dc7975d2a9cd6bbe6c9a67\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_effective_user_spaces_with_http_info(async_req=True)
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
                    " to method list_effective_user_spaces" % key
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
            '/user/effective_spaces', 'GET',
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

    def list_user_admin_privileges(self, id, **kwargs):  # noqa: E501
        """List user admin privileges  # noqa: E501

        Returns the list of user's (`{id}`) admin privileges in Onezone.  This operation requires `oz_view_privileges` admin privilege.  ***Example cURL requests***  **List user's admin privileges in Onezone** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/privileges  {   \"privileges\": [     \"oz_view_privileges\",     \"oz_users_list\",     \"oz_users_view\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handles_list\",     \"oz_handles_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_admin_privileges(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id. (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_admin_privileges_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_user_admin_privileges_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_user_admin_privileges_with_http_info(self, id, **kwargs):  # noqa: E501
        """List user admin privileges  # noqa: E501

        Returns the list of user's (`{id}`) admin privileges in Onezone.  This operation requires `oz_view_privileges` admin privilege.  ***Example cURL requests***  **List user's admin privileges in Onezone** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/privileges  {   \"privileges\": [     \"oz_view_privileges\",     \"oz_users_list\",     \"oz_users_view\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handles_list\",     \"oz_handles_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_admin_privileges_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id. (required)
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
                    " to method list_user_admin_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_user_admin_privileges`")  # noqa: E501

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
            '/users/{id}/privileges', 'GET',
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

    def list_user_clusters(self, **kwargs):  # noqa: E501
        """List user's clusters  # noqa: E501

        Returns the list of user's clusters.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user's clusters** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/clusters  {   \"clusters\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_clusters(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Clusters
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_clusters_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_user_clusters_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_user_clusters_with_http_info(self, **kwargs):  # noqa: E501
        """List user's clusters  # noqa: E501

        Returns the list of user's clusters.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user's clusters** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/clusters  {   \"clusters\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_clusters_with_http_info(async_req=True)
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
                    " to method list_user_clusters" % key
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
            '/user/clusters', 'GET',
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

    def list_user_effective_admin_privileges(self, id, **kwargs):  # noqa: E501
        """List user's effective admin privileges  # noqa: E501

        Returns the list of user's (`{id}`) admin privileges in Onezone.  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation requires `oz_view_privileges` admin privilege.  ***Example cURL requests***  **List user's effective admin privileges in Onezone** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/effective_privileges   {   \"privileges\": [     \"oz_view_privileges\",     \"oz_users_list\",     \"oz_users_view\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handles_list\",     \"oz_handles_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_effective_admin_privileges(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id. (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_effective_admin_privileges_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_user_effective_admin_privileges_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_user_effective_admin_privileges_with_http_info(self, id, **kwargs):  # noqa: E501
        """List user's effective admin privileges  # noqa: E501

        Returns the list of user's (`{id}`) admin privileges in Onezone.  Effective privileges are a sum of user's privileges and privileges inherited from his group memberships.  This operation requires `oz_view_privileges` admin privilege.  ***Example cURL requests***  **List user's effective admin privileges in Onezone** ```bash curl -u username:password -X GET  \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/effective_privileges   {   \"privileges\": [     \"oz_view_privileges\",     \"oz_users_list\",     \"oz_users_view\",     \"oz_groups_list\",     \"oz_groups_view\",     \"oz_spaces_list\",     \"oz_spaces_view\",     \"oz_shares_list\",     \"oz_shares_view\",     \"oz_providers_list\",     \"oz_providers_view\",     \"oz_handle_services_list\",     \"oz_handle_services_view\",     \"oz_handles_list\",     \"oz_handles_view\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_effective_admin_privileges_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id. (required)
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
                    " to method list_user_effective_admin_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_user_effective_admin_privileges`")  # noqa: E501

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
            '/users/{id}/effective_privileges', 'GET',
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

    def list_user_effective_clusters(self, **kwargs):  # noqa: E501
        """List user's effective clusters  # noqa: E501

        Returns the list of user's effective clusters.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user's effective clusters** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_clusters  {   \"clusters\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_effective_clusters(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Clusters
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_effective_clusters_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_user_effective_clusters_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_user_effective_clusters_with_http_info(self, **kwargs):  # noqa: E501
        """List user's effective clusters  # noqa: E501

        Returns the list of user's effective clusters.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user's effective clusters** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_clusters  {   \"clusters\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_effective_clusters_with_http_info(async_req=True)
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
                    " to method list_user_effective_clusters" % key
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
            '/user/effective_clusters', 'GET',
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

    def list_user_effective_handle_services(self, **kwargs):  # noqa: E501
        """List user effective handle services  # noqa: E501

        Returns the list of user's effective handle services.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective handle services** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_handle_services  {   \"handle_services\": [     \"LKJASHGDFKLJHASKLJDH\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_effective_handle_services(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: HandleServices
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_effective_handle_services_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_user_effective_handle_services_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_user_effective_handle_services_with_http_info(self, **kwargs):  # noqa: E501
        """List user effective handle services  # noqa: E501

        Returns the list of user's effective handle services.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective handle services** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_handle_services  {   \"handle_services\": [     \"LKJASHGDFKLJHASKLJDH\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_effective_handle_services_with_http_info(async_req=True)
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
                    " to method list_user_effective_handle_services" % key
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
            '/user/effective_handle_services', 'GET',
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

    def list_user_effective_handles(self, **kwargs):  # noqa: E501
        """Get user effective handles  # noqa: E501

        Returns the list of user's effective handles.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective handles** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_handles  {   \"handles\": [     \"8f8304077af3a834f0d484cd673073f0\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_effective_handles(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Handles
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_effective_handles_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_user_effective_handles_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_user_effective_handles_with_http_info(self, **kwargs):  # noqa: E501
        """Get user effective handles  # noqa: E501

        Returns the list of user's effective handles.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user effective handles** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/effective_handles  {   \"handles\": [     \"8f8304077af3a834f0d484cd673073f0\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_effective_handles_with_http_info(async_req=True)
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
                    " to method list_user_effective_handles" % key
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
            '/user/effective_handles', 'GET',
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

    def list_user_groups(self, **kwargs):  # noqa: E501
        """List user groups  # noqa: E501

        Returns the list of user's groups.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user groups** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/groups  {   \"groups\": [     \"13c6bf68ed88dd01f396571f976b148d\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_groups(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Groups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_groups_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_user_groups_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_user_groups_with_http_info(self, **kwargs):  # noqa: E501
        """List user groups  # noqa: E501

        Returns the list of user's groups.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user groups** ```bash curl -u admin:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/groups  {   \"groups\": [     \"13c6bf68ed88dd01f396571f976b148d\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_groups_with_http_info(async_req=True)
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
                    " to method list_user_groups" % key
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
            '/user/groups', 'GET',
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

    def list_user_handle_services(self, **kwargs):  # noqa: E501
        """List user handle services  # noqa: E501

        Returns the list of registered user handle services.  ***Example cURL requests***  **Get user handle services** ```bash curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/user/handle_services  {   \"handle_services\": [     \"0fe7c8a20ffdf07480c46f084bc3b8d5\",     \"302da048de67e2ea05f0af1d0fe7c8a2\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_handle_services(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: HandleServices
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_handle_services_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_user_handle_services_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_user_handle_services_with_http_info(self, **kwargs):  # noqa: E501
        """List user handle services  # noqa: E501

        Returns the list of registered user handle services.  ***Example cURL requests***  **Get user handle services** ```bash curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/user/handle_services  {   \"handle_services\": [     \"0fe7c8a20ffdf07480c46f084bc3b8d5\",     \"302da048de67e2ea05f0af1d0fe7c8a2\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_handle_services_with_http_info(async_req=True)
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
                    " to method list_user_handle_services" % key
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
            '/user/handle_services', 'GET',
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

    def list_user_handles(self, **kwargs):  # noqa: E501
        """List user handles  # noqa: E501

        Returns the list of users' handles.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user handles** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/handles  {   \"handles\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_handles(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Handles
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_handles_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_user_handles_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_user_handles_with_http_info(self, **kwargs):  # noqa: E501
        """List user handles  # noqa: E501

        Returns the list of users' handles.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user handles** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/handles  {   \"handles\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_handles_with_http_info(async_req=True)
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
                    " to method list_user_handles" % key
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
            '/user/handles', 'GET',
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

    def list_user_harvesters(self, **kwargs):  # noqa: E501
        """List user harvesters  # noqa: E501

        Returns the list of users' harvesters.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user harvesters** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/harvesters  {   \"harvesters\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_harvesters(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_harvesters_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_user_harvesters_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_user_harvesters_with_http_info(self, **kwargs):  # noqa: E501
        """List user harvesters  # noqa: E501

        Returns the list of users' harvesters.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user harvesters** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/harvesters  {   \"harvesters\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_harvesters_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2003
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
                    " to method list_user_harvesters" % key
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
            '/user/harvesters', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_user_spaces(self, **kwargs):  # noqa: E501
        """List user spaces  # noqa: E501

        Returns the list of users' spaces.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user spaces** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/spaces  {   \"spaces\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_spaces(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_spaces_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_user_spaces_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_user_spaces_with_http_info(self, **kwargs):  # noqa: E501
        """List user spaces  # noqa: E501

        Returns the list of users' spaces.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get user spaces** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/spaces  {   \"spaces\": [     \"c45fb16186931e6c2b44648cedd6b878ed1f6931\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_spaces_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2002
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
                    " to method list_user_spaces" % key
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
            '/user/spaces', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_current_user(self, body, **kwargs):  # noqa: E501
        """Modify current user  # noqa: E501

        Modifies user account details based on information provided in the request body.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Change user fullName** ```bash curl -u username:password -H \"Content-type: application/json\" -X PATCH  \\ -d '{\"fullName\": \"John Doe\"}' \\ https://$ZONE_HOST/api/v3/onezone/user ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_current_user(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserUpdateRequest body: User data. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_current_user_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_current_user_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def modify_current_user_with_http_info(self, body, **kwargs):  # noqa: E501
        """Modify current user  # noqa: E501

        Modifies user account details based on information provided in the request body.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Change user fullName** ```bash curl -u username:password -H \"Content-type: application/json\" -X PATCH  \\ -d '{\"fullName\": \"John Doe\"}' \\ https://$ZONE_HOST/api/v3/onezone/user ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_current_user_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserUpdateRequest body: User data. (required)
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
                    " to method modify_current_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `modify_current_user`")  # noqa: E501

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
            '/user', 'PATCH',
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

    def oz_users_list(self, **kwargs):  # noqa: E501
        """List all users  # noqa: E501

        Returns the list of all users in the system.  Requires `oz_users_list` admin privilege.  ***Example cURL requests***  **List all users in the system** ```bash  curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/users ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oz_users_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.oz_users_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.oz_users_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def oz_users_list_with_http_info(self, **kwargs):  # noqa: E501
        """List all users  # noqa: E501

        Returns the list of all users in the system.  Requires `oz_users_list` admin privilege.  ***Example cURL requests***  **List all users in the system** ```bash  curl -u username:password -X GET https://$ZONE_HOST/api/v3/onezone/users ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oz_users_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Users
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
                    " to method oz_users_list" % key
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
            '/users', 'GET',
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

    def remove_client_token(self, tid, **kwargs):  # noqa: E501
        """Delete access token  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use [this one](#operation/delete_named_token_of_current_user).  Removes a specific access token.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Delete user access token** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/client_tokens/PMPs42mROSS7Rg7z7BwU9JYpSof4SvIW5v14uQY8X08 ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_client_token(tid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tid: Token. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_client_token_with_http_info(tid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_client_token_with_http_info(tid, **kwargs)  # noqa: E501
            return data

    def remove_client_token_with_http_info(self, tid, **kwargs):  # noqa: E501
        """Delete access token  # noqa: E501

        This enpoint is deprecated and will be removed in future release, please use [this one](#operation/delete_named_token_of_current_user).  Removes a specific access token.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Delete user access token** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/client_tokens/PMPs42mROSS7Rg7z7BwU9JYpSof4SvIW5v14uQY8X08 ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_client_token_with_http_info(tid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tid: Token. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_client_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tid' is set
        if ('tid' not in params or
                params['tid'] is None):
            raise ValueError("Missing the required parameter `tid` when calling `remove_client_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tid' in params:
            path_params['tid'] = params['tid']  # noqa: E501

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
            '/user/client_tokens/{tid}', 'DELETE',
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

    def remove_current_user(self, **kwargs):  # noqa: E501
        """Remove current user  # noqa: E501

        Removes the account of currently authenticated user.  ***Example cURL requests***  **Remove user account** ```bash curl -u username:password -X DELETE  \\ https://$ZONE_HOST/api/v3/onezone/user ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_current_user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_current_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.remove_current_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def remove_current_user_with_http_info(self, **kwargs):  # noqa: E501
        """Remove current user  # noqa: E501

        Removes the account of currently authenticated user.  ***Example cURL requests***  **Remove user account** ```bash curl -u username:password -X DELETE  \\ https://$ZONE_HOST/api/v3/onezone/user ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_current_user_with_http_info(async_req=True)
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
                    " to method remove_current_user" % key
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
            '/user', 'DELETE',
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

    def remove_current_user_admin_privileges(self, **kwargs):  # noqa: E501
        """Remove current user's admin privileges  # noqa: E501

        Removes all currently authenticated user's admin privileges in Onezone.  This operation can be invoked on behalf of the current user only and requires `oz_set_privileges` admin privilege.  ***Example cURL requests***  **Remove all user's admin privileges in Onezone** ```bash curl -u username:password  -X DELETE  \\ https://$ZONE_HOST/api/v3/onezone/users/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_current_user_admin_privileges(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_current_user_admin_privileges_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.remove_current_user_admin_privileges_with_http_info(**kwargs)  # noqa: E501
            return data

    def remove_current_user_admin_privileges_with_http_info(self, **kwargs):  # noqa: E501
        """Remove current user's admin privileges  # noqa: E501

        Removes all currently authenticated user's admin privileges in Onezone.  This operation can be invoked on behalf of the current user only and requires `oz_set_privileges` admin privilege.  ***Example cURL requests***  **Remove all user's admin privileges in Onezone** ```bash curl -u username:password  -X DELETE  \\ https://$ZONE_HOST/api/v3/onezone/users/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_current_user_admin_privileges_with_http_info(async_req=True)
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
                    " to method remove_current_user_admin_privileges" % key
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
            '/user/privileges', 'DELETE',
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

    def remove_user(self, id, **kwargs):  # noqa: E501
        """Remove user  # noqa: E501

        Removes a specific user.  This operation requires `oz_users_delete` admin privilege.  ***Example cURL requests***  **Remove user** ```bash curl -u admin:password -X DELETE  \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_user(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_user_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_user_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def remove_user_with_http_info(self, id, **kwargs):  # noqa: E501
        """Remove user  # noqa: E501

        Removes a specific user.  This operation requires `oz_users_delete` admin privilege.  ***Example cURL requests***  **Remove user** ```bash curl -u admin:password -X DELETE  \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_user_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id. (required)
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
                    " to method remove_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_user`")  # noqa: E501

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
            '/users/{id}', 'DELETE',
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

    def remove_user_admin_privileges(self, id, **kwargs):  # noqa: E501
        """Remove user's admin privileges  # noqa: E501

        Removes all user's (`{id}`) admin privileges in Onezone.  This operation requires `oz_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Removes all user's admin privileges in Onezone** ```bash curl -u username:password -X DELETE  \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_user_admin_privileges(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_user_admin_privileges_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_user_admin_privileges_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def remove_user_admin_privileges_with_http_info(self, id, **kwargs):  # noqa: E501
        """Remove user's admin privileges  # noqa: E501

        Removes all user's (`{id}`) admin privileges in Onezone.  This operation requires `oz_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Removes all user's admin privileges in Onezone** ```bash curl -u username:password -X DELETE  \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_user_admin_privileges_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id. (required)
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
                    " to method remove_user_admin_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_user_admin_privileges`")  # noqa: E501

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
            '/users/{id}/privileges', 'DELETE',
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

    def remove_user_handle(self, hid, **kwargs):  # noqa: E501
        """Leave handle  # noqa: E501

        Removes the user's ownership or access to a specific space.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Delete user space** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/handles/$HANDLE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_user_handle(hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hid: Handle Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_user_handle_with_http_info(hid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_user_handle_with_http_info(hid, **kwargs)  # noqa: E501
            return data

    def remove_user_handle_with_http_info(self, hid, **kwargs):  # noqa: E501
        """Leave handle  # noqa: E501

        Removes the user's ownership or access to a specific space.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Delete user space** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/handles/$HANDLE_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_user_handle_with_http_info(hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hid: Handle Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_user_handle" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hid' is set
        if ('hid' not in params or
                params['hid'] is None):
            raise ValueError("Missing the required parameter `hid` when calling `remove_user_handle`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/user/handles/{hid}', 'DELETE',
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

    def remove_user_space_alias(self, sid, **kwargs):  # noqa: E501
        """Remove space alias  # noqa: E501

        Removes the alias (user defined name) for a specific space.  NOTE: Space aliases are not yet implemented - setting an alias is possible but will have no effect.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Remove user space alias** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/spaces/$SPACE_ID/alias ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_user_space_alias(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_user_space_alias_with_http_info(sid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_user_space_alias_with_http_info(sid, **kwargs)  # noqa: E501
            return data

    def remove_user_space_alias_with_http_info(self, sid, **kwargs):  # noqa: E501
        """Remove space alias  # noqa: E501

        Removes the alias (user defined name) for a specific space.  NOTE: Space aliases are not yet implemented - setting an alias is possible but will have no effect.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Remove user space alias** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/spaces/$SPACE_ID/alias ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_user_space_alias_with_http_info(sid, async_req=True)
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
                    " to method remove_user_space_alias" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `remove_user_space_alias`")  # noqa: E501

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
            '/user/spaces/{sid}/alias', 'DELETE',
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

    def set_user_space_alias(self, body, sid, **kwargs):  # noqa: E501
        """Set user space alias  # noqa: E501

        Sets the alias (user defined name) for a specific space.  NOTE: Space aliases are not yet implemented - setting an alias is possible but will have no effect.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Set space alias** ```bash curl -u username:password -X PUT -d '{\"alias\": \"Space alias\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/user/spaces/$SPACE_ID/alias ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_user_space_alias(body, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SpaceAlias body: New space alias. (required)
        :param str sid: Space Id. (required)
        :return: SpaceAlias
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_user_space_alias_with_http_info(body, sid, **kwargs)  # noqa: E501
        else:
            (data) = self.set_user_space_alias_with_http_info(body, sid, **kwargs)  # noqa: E501
            return data

    def set_user_space_alias_with_http_info(self, body, sid, **kwargs):  # noqa: E501
        """Set user space alias  # noqa: E501

        Sets the alias (user defined name) for a specific space.  NOTE: Space aliases are not yet implemented - setting an alias is possible but will have no effect.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Set space alias** ```bash curl -u username:password -X PUT -d '{\"alias\": \"Space alias\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/user/spaces/$SPACE_ID/alias ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_user_space_alias_with_http_info(body, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SpaceAlias body: New space alias. (required)
        :param str sid: Space Id. (required)
        :return: SpaceAlias
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'sid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_user_space_alias" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `set_user_space_alias`")  # noqa: E501
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `set_user_space_alias`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/user/spaces/{sid}/alias', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SpaceAlias',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def toggle_user_access_block(self, body, id, **kwargs):  # noqa: E501
        """Block or unblock user access  # noqa: E501

        Allows to block or unblock access to Onedata services for a specific user.  This operation requires `oz_users_update` admin privilege.  ***Example cURL requests***  **Block or unblock user access** ```bash curl -u admin:password -X PATCH https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/access_block \\ -H \"Content-Type: application/json\" -d '{\"blocked\": true}' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.toggle_user_access_block(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserAccessBlockUpdate body: User access block modification request. (required)
        :param str id: User Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.toggle_user_access_block_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.toggle_user_access_block_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def toggle_user_access_block_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Block or unblock user access  # noqa: E501

        Allows to block or unblock access to Onedata services for a specific user.  This operation requires `oz_users_update` admin privilege.  ***Example cURL requests***  **Block or unblock user access** ```bash curl -u admin:password -X PATCH https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/access_block \\ -H \"Content-Type: application/json\" -d '{\"blocked\": true}' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.toggle_user_access_block_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserAccessBlockUpdate body: User access block modification request. (required)
        :param str id: User Id. (required)
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
                    " to method toggle_user_access_block" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `toggle_user_access_block`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `toggle_user_access_block`")  # noqa: E501

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
            '/users/{id}/access_block', 'PATCH',
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

    def update_current_user_admin_privileges(self, **kwargs):  # noqa: E501
        """Update current user's admin privileges  # noqa: E501

        Updates currently authenticated user's admin privileges in Onezone.  This operation can be invoked on behalf of the current user only and requires `oz_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Updates current user's admin privileges in Onezone** ```bash curl -u username:password -H \"Content-type: application/json\" -X PATCH \\ -d '{\"grant\": [\"oz_spaces_list\"], \"revoke\": [\"oz_groups_update\"]}' \\ https://$ZONE_HOST/api/v3/onezone/user/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_current_user_admin_privileges(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AdminPrivilegesUpdate body: User admin privileges.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_current_user_admin_privileges_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.update_current_user_admin_privileges_with_http_info(**kwargs)  # noqa: E501
            return data

    def update_current_user_admin_privileges_with_http_info(self, **kwargs):  # noqa: E501
        """Update current user's admin privileges  # noqa: E501

        Updates currently authenticated user's admin privileges in Onezone.  This operation can be invoked on behalf of the current user only and requires `oz_set_privileges` admin privilege.  The `grant` field specifies a list of privileges to be granted. The `revoke` field specifies a list of privileges to be revoked. At least one of those fields must be given.  ***Example cURL requests***  **Updates current user's admin privileges in Onezone** ```bash curl -u username:password -H \"Content-type: application/json\" -X PATCH \\ -d '{\"grant\": [\"oz_spaces_list\"], \"revoke\": [\"oz_groups_update\"]}' \\ https://$ZONE_HOST/api/v3/onezone/user/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_current_user_admin_privileges_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AdminPrivilegesUpdate body: User admin privileges.
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
                    " to method update_current_user_admin_privileges" % key
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
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/user/privileges', 'PATCH',
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

    def update_user_admin_privileges(self, id, **kwargs):  # noqa: E501
        """Update user's admin privileges  # noqa: E501

        Updates user's (`{id}`) admin privileges in Onezone.  This operation requires `oz_set_privileges` admin privilege.  ***Example cURL requests***  **Updates user's admin privileges in Onezone** ```bash curl -u username:password -H \"Content-type: application/json\" -X PATCH \\ -d '{\"grant\": [\"oz_spaces_list\"], \"revoke\": [\"oz_groups_update\"]}' \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_admin_privileges(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id. (required)
        :param AdminPrivilegesUpdate body: User admin privileges.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_user_admin_privileges_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_user_admin_privileges_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def update_user_admin_privileges_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update user's admin privileges  # noqa: E501

        Updates user's (`{id}`) admin privileges in Onezone.  This operation requires `oz_set_privileges` admin privilege.  ***Example cURL requests***  **Updates user's admin privileges in Onezone** ```bash curl -u username:password -H \"Content-type: application/json\" -X PATCH \\ -d '{\"grant\": [\"oz_spaces_list\"], \"revoke\": [\"oz_groups_update\"]}' \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/privileges ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_admin_privileges_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id. (required)
        :param AdminPrivilegesUpdate body: User admin privileges.
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
                    " to method update_user_admin_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_user_admin_privileges`")  # noqa: E501

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
            '/users/{id}/privileges', 'PATCH',
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

    def user_join_cluster(self, body, **kwargs):  # noqa: E501
        """Join cluster  # noqa: E501

        Join an existing cluster using an inivitation token.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Join an existing cluster** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"token\" : \"MDAxNmxvY2F00aW9uRVM2TVo5UlZ5cGFjZV9jcmLciFsOgyUkPI3f02le6PM01IX8go\" }'  \\ https://$ZONE_HOST/api/v3/onezone/user/clusters/join ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_join_cluster(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ClusterInviteToken body: Token for joining a cluster. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_join_cluster_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.user_join_cluster_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def user_join_cluster_with_http_info(self, body, **kwargs):  # noqa: E501
        """Join cluster  # noqa: E501

        Join an existing cluster using an inivitation token.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Join an existing cluster** ```bash curl -u admin:password -H \"Content-type: application/json\" -X POST \\ -d '{ \"token\" : \"MDAxNmxvY2F00aW9uRVM2TVo5UlZ5cGFjZV9jcmLciFsOgyUkPI3f02le6PM01IX8go\" }'  \\ https://$ZONE_HOST/api/v3/onezone/user/clusters/join ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_join_cluster_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ClusterInviteToken body: Token for joining a cluster. (required)
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
                    " to method user_join_cluster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `user_join_cluster`")  # noqa: E501

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
            '/user/clusters/join', 'POST',
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

    def user_leave_cluster(self, cid, **kwargs):  # noqa: E501
        """Leave cluster  # noqa: E501

        Removes the users membership in a specific cluster.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **User leave cluster** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/clusters/$CLUSTER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_leave_cluster(cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cid: Cluster Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_leave_cluster_with_http_info(cid, **kwargs)  # noqa: E501
        else:
            (data) = self.user_leave_cluster_with_http_info(cid, **kwargs)  # noqa: E501
            return data

    def user_leave_cluster_with_http_info(self, cid, **kwargs):  # noqa: E501
        """Leave cluster  # noqa: E501

        Removes the users membership in a specific cluster.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **User leave cluster** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/clusters/$CLUSTER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_leave_cluster_with_http_info(cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cid: Cluster Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_leave_cluster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cid' is set
        if ('cid' not in params or
                params['cid'] is None):
            raise ValueError("Missing the required parameter `cid` when calling `user_leave_cluster`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/user/clusters/{cid}', 'DELETE',
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

    def user_leave_harvester(self, hid, **kwargs):  # noqa: E501
        """Leave harvester  # noqa: E501

        Removes the users ownership or access to a specific harvester.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Delete user harvester** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/harvesters/$HARVESTER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_leave_harvester(hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hid: Harvester Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_leave_harvester_with_http_info(hid, **kwargs)  # noqa: E501
        else:
            (data) = self.user_leave_harvester_with_http_info(hid, **kwargs)  # noqa: E501
            return data

    def user_leave_harvester_with_http_info(self, hid, **kwargs):  # noqa: E501
        """Leave harvester  # noqa: E501

        Removes the users ownership or access to a specific harvester.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Delete user harvester** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/harvesters/$HARVESTER_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_leave_harvester_with_http_info(hid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hid: Harvester Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_leave_harvester" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hid' is set
        if ('hid' not in params or
                params['hid'] is None):
            raise ValueError("Missing the required parameter `hid` when calling `user_leave_harvester`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/user/harvesters/{hid}', 'DELETE',
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
