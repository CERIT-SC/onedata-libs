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


class TokenApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def confine_token(self, body, **kwargs):  # noqa: E501
        """Confine a token  # noqa: E501

        Confines (restricts) a token provided in serialized form with given caveats. Returns the confined token. Does not verify the token.  This operation has public access.  ***Example cURL requests***  **Confine a token** ```bash curl -d '{   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaW\",   \"caveats\": [{\"type\": \"time\", \"validUntil\": 1571147494}] }' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/tokens/confine ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.confine_token(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TokensConfineBody body: The token to be confined and caveats. (required)
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.confine_token_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.confine_token_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def confine_token_with_http_info(self, body, **kwargs):  # noqa: E501
        """Confine a token  # noqa: E501

        Confines (restricts) a token provided in serialized form with given caveats. Returns the confined token. Does not verify the token.  This operation has public access.  ***Example cURL requests***  **Confine a token** ```bash curl -d '{   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaW\",   \"caveats\": [{\"type\": \"time\", \"validUntil\": 1571147494}] }' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/tokens/confine ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.confine_token_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TokensConfineBody body: The token to be confined and caveats. (required)
        :return: InlineResponse20012
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
                    " to method confine_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `confine_token`")  # noqa: E501

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
            '/tokens/confine', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_named_token_for_current_provider(self, body, **kwargs):  # noqa: E501
        """Create named token for current provider  # noqa: E501

        Creates a new named token for the provider. The token name must be unique for the provider.  This operation can be invoked on behalf of the current provider only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create named token for current provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X POST -d '{\"name\": \"new-token\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/provider/tokens/named ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_named_token_for_current_provider(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NamedTokenCreateRequest body: Properties of the new named token. (required)
        :return: NamedTokenCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_named_token_for_current_provider_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_named_token_for_current_provider_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_named_token_for_current_provider_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create named token for current provider  # noqa: E501

        Creates a new named token for the provider. The token name must be unique for the provider.  This operation can be invoked on behalf of the current provider only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create named token for current provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X POST -d '{\"name\": \"new-token\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/provider/tokens/named ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_named_token_for_current_provider_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NamedTokenCreateRequest body: Properties of the new named token. (required)
        :return: NamedTokenCreateResponse
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
                    " to method create_named_token_for_current_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_named_token_for_current_provider`")  # noqa: E501

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
            '/provider/tokens/named', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NamedTokenCreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_named_token_for_current_user(self, body, **kwargs):  # noqa: E501
        """Create named token for current user  # noqa: E501

        Creates a new named token for the user. The token name must be unique for the user.  In case of invite tokens, invite / add member privileges are required in the target entity to create a token. For example, `space_add_group` in the space when creating a `groupJoinSpace` invite token.  This operation can be invoked on behalf of the current user only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create named token for current user** ```bash curl -u username:password -X POST -d '{\"name\": \"new-token-1\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/user/tokens/named ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_named_token_for_current_user(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NamedTokenCreateRequest body: Properties of the new named token. (required)
        :return: NamedTokenCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_named_token_for_current_user_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_named_token_for_current_user_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_named_token_for_current_user_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create named token for current user  # noqa: E501

        Creates a new named token for the user. The token name must be unique for the user.  In case of invite tokens, invite / add member privileges are required in the target entity to create a token. For example, `space_add_group` in the space when creating a `groupJoinSpace` invite token.  This operation can be invoked on behalf of the current user only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create named token for current user** ```bash curl -u username:password -X POST -d '{\"name\": \"new-token-1\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/user/tokens/named ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_named_token_for_current_user_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NamedTokenCreateRequest body: Properties of the new named token. (required)
        :return: NamedTokenCreateResponse
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
                    " to method create_named_token_for_current_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_named_token_for_current_user`")  # noqa: E501

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
            '/user/tokens/named', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NamedTokenCreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_named_token_for_provider(self, body, id, **kwargs):  # noqa: E501
        """Create named token for a provider  # noqa: E501

        Creates a new named token for specific provider. The token name must be unique for the provider.  This operation is available for the subject provider (`id`), or the provider's cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create named token for a provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X POST -d '{\"name\": \"new-token\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/tokens/named/ ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_named_token_for_provider(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NamedTokenCreateRequest body: Properties of the new named token. (required)
        :param str id: Provider Id (required)
        :return: NamedTokenCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_named_token_for_provider_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_named_token_for_provider_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def create_named_token_for_provider_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Create named token for a provider  # noqa: E501

        Creates a new named token for specific provider. The token name must be unique for the provider.  This operation is available for the subject provider (`id`), or the provider's cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create named token for a provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X POST -d '{\"name\": \"new-token\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/tokens/named/ ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_named_token_for_provider_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NamedTokenCreateRequest body: Properties of the new named token. (required)
        :param str id: Provider Id (required)
        :return: NamedTokenCreateResponse
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
                    " to method create_named_token_for_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_named_token_for_provider`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_named_token_for_provider`")  # noqa: E501

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
            '/providers/{id}/tokens/named', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NamedTokenCreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_named_token_for_user(self, body, id, **kwargs):  # noqa: E501
        """Create named token for a user  # noqa: E501

        Creates a new named token for specific user. The token name must be unique for the user.  In case of invite tokens, invite / add member privileges are required in the target entity to create a token. For example, `space_add_group` in the space when creating a `groupJoinSpace` invite token.  This operation is available for the token owner (subject), otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create named token for a user** ```bash curl -u username:password -X POST -d '{\"name\": \"new-token-1\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/tokens/named ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_named_token_for_user(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NamedTokenCreateRequest body: Properties of the new named token. (required)
        :param str id: User Id (required)
        :return: NamedTokenCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_named_token_for_user_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_named_token_for_user_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def create_named_token_for_user_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Create named token for a user  # noqa: E501

        Creates a new named token for specific user. The token name must be unique for the user.  In case of invite tokens, invite / add member privileges are required in the target entity to create a token. For example, `space_add_group` in the space when creating a `groupJoinSpace` invite token.  This operation is available for the token owner (subject), otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create named token for a user** ```bash curl -u username:password -X POST -d '{\"name\": \"new-token-1\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/tokens/named ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_named_token_for_user_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NamedTokenCreateRequest body: Properties of the new named token. (required)
        :param str id: User Id (required)
        :return: NamedTokenCreateResponse
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
                    " to method create_named_token_for_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_named_token_for_user`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_named_token_for_user`")  # noqa: E501

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
            '/users/{id}/tokens/named', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NamedTokenCreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_temporary_token_for_current_provider(self, body, **kwargs):  # noqa: E501
        """Create temporary token for current provider  # noqa: E501

        Creates a new temporary token for the provider. Temporary tokens must be confined with a time caveat and are not persisted (cannot be retrieved, listed, revoked, updated or deleted). However, it is possible to revoke all existing temporary tokens of the provider: [see more](#operation/revoke_all_temporary_tokens_of_current_provider)).  This operation can be invoked on behalf of the current provider only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create temporary token for current provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X POST \\ -d '{\"type\": {\"accessToken\":{}}, \"caveats\": [{\"type\": \"time\", \"validUntil\": 1571147494}]}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/provider/tokens/temporary ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_temporary_token_for_current_provider(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TemporaryTokenCreateRequest body: Properties of the new temporary token. (required)
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_temporary_token_for_current_provider_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_temporary_token_for_current_provider_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_temporary_token_for_current_provider_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create temporary token for current provider  # noqa: E501

        Creates a new temporary token for the provider. Temporary tokens must be confined with a time caveat and are not persisted (cannot be retrieved, listed, revoked, updated or deleted). However, it is possible to revoke all existing temporary tokens of the provider: [see more](#operation/revoke_all_temporary_tokens_of_current_provider)).  This operation can be invoked on behalf of the current provider only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create temporary token for current provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X POST \\ -d '{\"type\": {\"accessToken\":{}}, \"caveats\": [{\"type\": \"time\", \"validUntil\": 1571147494}]}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/provider/tokens/temporary ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_temporary_token_for_current_provider_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TemporaryTokenCreateRequest body: Properties of the new temporary token. (required)
        :return: InlineResponse20012
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
                    " to method create_temporary_token_for_current_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_temporary_token_for_current_provider`")  # noqa: E501

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
            '/provider/tokens/temporary', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_temporary_token_for_current_user(self, body, **kwargs):  # noqa: E501
        """Create temporary token for current user  # noqa: E501

        Creates a new temporary token for the user. Temporary tokens must be confined with a time caveat and are not persisted (cannot be retrieved, listed, revoked, updated or deleted). However, it is possible to revoke all existing temporary tokens of the user: [see more](#operation/revoke_all_temporary_tokens_of_current_user)).  In case of invite tokens, invite / add member privileges are required in the target entity to create a token. For example, `space_add_group` in the space when creating a `groupJoinSpace` invite token.  This operation can be invoked on behalf of the current user only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create temporary token for current user** ```bash curl -u username:password -X POST \\ -d '{\"type\": {\"accessToken\":{}}, \"caveats\": [{\"type\": \"time\", \"validUntil\": 1571147494}]}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/user/tokens/temporary ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_temporary_token_for_current_user(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TemporaryTokenCreateRequest body: Properties of the new temporary token. (required)
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_temporary_token_for_current_user_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_temporary_token_for_current_user_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_temporary_token_for_current_user_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create temporary token for current user  # noqa: E501

        Creates a new temporary token for the user. Temporary tokens must be confined with a time caveat and are not persisted (cannot be retrieved, listed, revoked, updated or deleted). However, it is possible to revoke all existing temporary tokens of the user: [see more](#operation/revoke_all_temporary_tokens_of_current_user)).  In case of invite tokens, invite / add member privileges are required in the target entity to create a token. For example, `space_add_group` in the space when creating a `groupJoinSpace` invite token.  This operation can be invoked on behalf of the current user only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create temporary token for current user** ```bash curl -u username:password -X POST \\ -d '{\"type\": {\"accessToken\":{}}, \"caveats\": [{\"type\": \"time\", \"validUntil\": 1571147494}]}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/user/tokens/temporary ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_temporary_token_for_current_user_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TemporaryTokenCreateRequest body: Properties of the new temporary token. (required)
        :return: InlineResponse20012
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
                    " to method create_temporary_token_for_current_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_temporary_token_for_current_user`")  # noqa: E501

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
            '/user/tokens/temporary', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_temporary_token_for_provider(self, body, id, **kwargs):  # noqa: E501
        """Create temporary token for a provider  # noqa: E501

        Creates a new temporary token for specific provider. Temporary tokens must be confined with a time caveat and are not persisted (cannot be retrieved, listed, revoked, updated or deleted). However, it is possible to revoke all existing temporary tokens of the provider: [see more](#operation/revoke_all_temporary_tokens_of_provider)).  This operation is available for the subject provider (`id`), or the provider's cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create temporary token for a provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X POST \\ -d '{\"type\": {\"accessToken\":{}}, \"caveats\": [{\"type\": \"time\", \"validUntil\": 1571147494}]}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/tokens/temporary ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_temporary_token_for_provider(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TemporaryTokenCreateRequest body: Properties of the new temporary token. (required)
        :param str id: Provider Id (required)
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_temporary_token_for_provider_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_temporary_token_for_provider_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def create_temporary_token_for_provider_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Create temporary token for a provider  # noqa: E501

        Creates a new temporary token for specific provider. Temporary tokens must be confined with a time caveat and are not persisted (cannot be retrieved, listed, revoked, updated or deleted). However, it is possible to revoke all existing temporary tokens of the provider: [see more](#operation/revoke_all_temporary_tokens_of_provider)).  This operation is available for the subject provider (`id`), or the provider's cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create temporary token for a provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X POST \\ -d '{\"type\": {\"accessToken\":{}}, \"caveats\": [{\"type\": \"time\", \"validUntil\": 1571147494}]}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/tokens/temporary ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_temporary_token_for_provider_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TemporaryTokenCreateRequest body: Properties of the new temporary token. (required)
        :param str id: Provider Id (required)
        :return: InlineResponse20012
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
                    " to method create_temporary_token_for_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_temporary_token_for_provider`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_temporary_token_for_provider`")  # noqa: E501

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
            '/providers/{id}/tokens/temporary', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_temporary_token_for_user(self, body, id, **kwargs):  # noqa: E501
        """Create temporary token for a user  # noqa: E501

        Creates a new temporary token for specific user. Temporary tokens must be confined with a time caveat and are not persisted (cannot be retrieved, listed, revoked, updated or deleted). However, it is possible to revoke all existing temporary tokens of the user: [see more](#operation/revoke_all_temporary_tokens_of_user)).  In case of invite tokens, invite / add member privileges are required in the target entity to create a token. For example, `space_add_group` in the space when creating a `groupJoinSpace` invite token.  This operation is available for the currently authorized user, otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create temporary token for a user** ```bash curl -u username:password -X POST \\ -d '{\"type\": {\"accessToken\":{}}, \"caveats\": [{\"type\": \"time\", \"validUntil\": 1571147494}]}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/tokens/temporary ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_temporary_token_for_user(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TemporaryTokenCreateRequest body: Properties of the new temporary token. (required)
        :param str id: User Id (required)
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_temporary_token_for_user_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_temporary_token_for_user_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def create_temporary_token_for_user_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Create temporary token for a user  # noqa: E501

        Creates a new temporary token for specific user. Temporary tokens must be confined with a time caveat and are not persisted (cannot be retrieved, listed, revoked, updated or deleted). However, it is possible to revoke all existing temporary tokens of the user: [see more](#operation/revoke_all_temporary_tokens_of_user)).  In case of invite tokens, invite / add member privileges are required in the target entity to create a token. For example, `space_add_group` in the space when creating a `groupJoinSpace` invite token.  This operation is available for the currently authorized user, otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Create temporary token for a user** ```bash curl -u username:password -X POST \\ -d '{\"type\": {\"accessToken\":{}}, \"caveats\": [{\"type\": \"time\", \"validUntil\": 1571147494}]}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/tokens/temporary ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_temporary_token_for_user_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TemporaryTokenCreateRequest body: Properties of the new temporary token. (required)
        :param str id: User Id (required)
        :return: InlineResponse20012
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
                    " to method create_temporary_token_for_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_temporary_token_for_user`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_temporary_token_for_user`")  # noqa: E501

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
            '/users/{id}/tokens/temporary', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_named_token(self, id, **kwargs):  # noqa: E501
        """Delete named token  # noqa: E501

        Deletes a specific named token.  This operation is available for the token owner (subject), or (in case of provider tokens) cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Delete named token** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/tokens/named/$TOKEN_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_named_token(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Token Id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_named_token_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_named_token_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_named_token_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete named token  # noqa: E501

        Deletes a specific named token.  This operation is available for the token owner (subject), or (in case of provider tokens) cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Delete named token** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/tokens/named/$TOKEN_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_named_token_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Token Id (required)
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
                    " to method delete_named_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_named_token`")  # noqa: E501

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
            '/tokens/named/{id}', 'DELETE',
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

    def delete_named_tokens_of_current_provider(self, **kwargs):  # noqa: E501
        """Delete named tokens of current provider  # noqa: E501

        Deletes all provider's named tokens.  This operation can be invoked on behalf of the current provider only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Delete named tokens of current provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/provider/tokens/named ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_named_tokens_of_current_provider(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_named_tokens_of_current_provider_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_named_tokens_of_current_provider_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_named_tokens_of_current_provider_with_http_info(self, **kwargs):  # noqa: E501
        """Delete named tokens of current provider  # noqa: E501

        Deletes all provider's named tokens.  This operation can be invoked on behalf of the current provider only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Delete named tokens of current provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/provider/tokens/named ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_named_tokens_of_current_provider_with_http_info(async_req=True)
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
                    " to method delete_named_tokens_of_current_provider" % key
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
            '/provider/tokens/named', 'DELETE',
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

    def delete_named_tokens_of_current_user(self, **kwargs):  # noqa: E501
        """Delete named tokens of current user  # noqa: E501

        Deletes all user's named tokens.  This operation can be invoked on behalf of the current user only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Delete named tokens of current user** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/tokens/named ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_named_tokens_of_current_user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_named_tokens_of_current_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_named_tokens_of_current_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_named_tokens_of_current_user_with_http_info(self, **kwargs):  # noqa: E501
        """Delete named tokens of current user  # noqa: E501

        Deletes all user's named tokens.  This operation can be invoked on behalf of the current user only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Delete named tokens of current user** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/tokens/named ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_named_tokens_of_current_user_with_http_info(async_req=True)
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
                    " to method delete_named_tokens_of_current_user" % key
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
            '/user/tokens/named', 'DELETE',
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

    def delete_named_tokens_of_provider(self, id, **kwargs):  # noqa: E501
        """Delete named tokens of a provider  # noqa: E501

        Deletes all named tokens belonging to a specific provider.  This operation is available for the subject provider (`id`), or the provider's cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Delete named tokens of a provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/tokens/named ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_named_tokens_of_provider(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_named_tokens_of_provider_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_named_tokens_of_provider_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_named_tokens_of_provider_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete named tokens of a provider  # noqa: E501

        Deletes all named tokens belonging to a specific provider.  This operation is available for the subject provider (`id`), or the provider's cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Delete named tokens of a provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/tokens/named ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_named_tokens_of_provider_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id (required)
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
                    " to method delete_named_tokens_of_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_named_tokens_of_provider`")  # noqa: E501

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
            '/providers/{id}/tokens/named', 'DELETE',
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

    def delete_named_tokens_of_user(self, id, **kwargs):  # noqa: E501
        """Delete named tokens of a user  # noqa: E501

        Deletes all named tokens belonging to a specific user.  This operation is available for the currently authorized user, otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Delete named tokens of a user** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/tokens/named ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_named_tokens_of_user(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_named_tokens_of_user_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_named_tokens_of_user_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_named_tokens_of_user_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete named tokens of a user  # noqa: E501

        Deletes all named tokens belonging to a specific user.  This operation is available for the currently authorized user, otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Delete named tokens of a user** ```bash curl -u username:password -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/tokens/named ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_named_tokens_of_user_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id (required)
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
                    " to method delete_named_tokens_of_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_named_tokens_of_user`")  # noqa: E501

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
            '/users/{id}/tokens/named', 'DELETE',
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

    def examine_token(self, body, **kwargs):  # noqa: E501
        """Examine a token  # noqa: E501

        Examines a token provided in serialized form. Returns all the information that can be inferred from the token. Does not verify the token.  This operation has public access.  ***Example cURL requests***  **Examine a token** ```bash curl -d '{\"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaW\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/tokens/examine ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.examine_token(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TokensExamineBody body: The token to be examined (encapsulated in an object). (required)
        :return: ExaminedToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.examine_token_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.examine_token_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def examine_token_with_http_info(self, body, **kwargs):  # noqa: E501
        """Examine a token  # noqa: E501

        Examines a token provided in serialized form. Returns all the information that can be inferred from the token. Does not verify the token.  This operation has public access.  ***Example cURL requests***  **Examine a token** ```bash curl -d '{\"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaW\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/tokens/examine ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.examine_token_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TokensExamineBody body: The token to be examined (encapsulated in an object). (required)
        :return: ExaminedToken
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
                    " to method examine_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `examine_token`")  # noqa: E501

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
            '/tokens/examine', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExaminedToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_named_token(self, id, **kwargs):  # noqa: E501
        """Get named token  # noqa: E501

        Returns the information about a specific named token.  This operation is available for the token owner (subject), or (in case of provider tokens) cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Get named token** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/tokens/named/$TOKEN_ID {   \"id\": \"2b5d0dd5aa6443a69277b5ce0544fec2\",   \"name\": \"my-token-1\",   \"subject\": {     \"type\": \"user\",     \"id\": \"1b510f18b3b05611871c0acdffa9aed4\"   },   \"type\": {     \"inviteToken\": {       \"inviteType\": \"userJoinCluster\",       \"clusterId\": \"fb73f7ceff5abd995357abbe01c812ce\"     }   },   \"caveats\": [     {       \"type\": \"time\",       \"validUntil\": 1571147494     },     {       \"type\": \"ip\",       \"whitelist\": [         \"189.34.15.0/8\",         \"127.0.0.0/24\",         \"167.73.12.17\"       ]     }   ],   \"metadata\": {     \"creationTime\": 1564721024,     \"usageLimit\": 15,     \"usageCount\": 3,     \"privileges\": [       \"space_view\",       \"space_read_data\",       \"space_view_views\",       \"space_view_statistics\"     ],     \"custom\": {       \"jobName\": \"experiment-15\",       \"vm\": \"worker156.cloud.local\"     }   },   \"revoked\": false,   \"token\": \"MDAxNWxvY2F0aW9uIG9uZXpvbmUKMDAzYmlkZW50aWZpZXIgOEhmSEFSSGdrbHFCa1pWSTR\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_named_token(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Token Id (required)
        :return: NamedToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_named_token_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_named_token_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_named_token_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get named token  # noqa: E501

        Returns the information about a specific named token.  This operation is available for the token owner (subject), or (in case of provider tokens) cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Get named token** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/tokens/named/$TOKEN_ID {   \"id\": \"2b5d0dd5aa6443a69277b5ce0544fec2\",   \"name\": \"my-token-1\",   \"subject\": {     \"type\": \"user\",     \"id\": \"1b510f18b3b05611871c0acdffa9aed4\"   },   \"type\": {     \"inviteToken\": {       \"inviteType\": \"userJoinCluster\",       \"clusterId\": \"fb73f7ceff5abd995357abbe01c812ce\"     }   },   \"caveats\": [     {       \"type\": \"time\",       \"validUntil\": 1571147494     },     {       \"type\": \"ip\",       \"whitelist\": [         \"189.34.15.0/8\",         \"127.0.0.0/24\",         \"167.73.12.17\"       ]     }   ],   \"metadata\": {     \"creationTime\": 1564721024,     \"usageLimit\": 15,     \"usageCount\": 3,     \"privileges\": [       \"space_view\",       \"space_read_data\",       \"space_view_views\",       \"space_view_statistics\"     ],     \"custom\": {       \"jobName\": \"experiment-15\",       \"vm\": \"worker156.cloud.local\"     }   },   \"revoked\": false,   \"token\": \"MDAxNWxvY2F0aW9uIG9uZXpvbmUKMDAzYmlkZW50aWZpZXIgOEhmSEFSSGdrbHFCa1pWSTR\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_named_token_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Token Id (required)
        :return: NamedToken
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
                    " to method get_named_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_named_token`")  # noqa: E501

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
            '/tokens/named/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NamedToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_named_token_of_current_provider_by_name(self, name, **kwargs):  # noqa: E501
        """Get named token of current provider by name  # noqa: E501

        Returns the information about a provider's named token by token name.  This operation can be invoked on behalf of the current provider only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Get named token of current provider by name** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/provider/tokens/named/name/my-token-1 {   \"id\": \"2b5d0dd5aa6443a69277b5ce0544fec2\",   \"name\": \"my-token-1\",   \"subject\": {     \"type\": \"provider\",     \"id\": \"6ebe7ac282e0188b5336b5d8cfa564d5\"   },   \"type\": {     \"inviteToken\": {       \"inviteType\": \"userJoinCluster\",       \"clusterId\": \"fb73f7ceff5abd995357abbe01c812ce\"     }   },   \"caveats\": [     {       \"type\": \"time\",       \"validUntil\": 1571147494     },     {       \"type\": \"ip\",       \"whitelist\": [         \"189.34.15.0/8\",         \"127.0.0.0/24\",         \"167.73.12.17\"       ]     }   ],   \"metadata\": {     \"creationTime\": 1564721024,     \"usageLimit\": 15,     \"usageCount\": 3,     \"privileges\": [       \"space_view\",       \"space_read_data\",       \"space_view_views\",       \"space_view_statistics\"     ],     \"custom\": {       \"jobName\": \"experiment-15\",       \"vm\": \"worker156.cloud.local\"     }   },   \"revoked\": false,   \"token\": \"MDAxNWxvY2F0aW9uIG9uZXpvbmUKMDAzYmlkZW50aWZpZXIgOEhmSEFSSGdrbHFCa1pWSTR\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_named_token_of_current_provider_by_name(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Token name (required)
        :return: NamedToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_named_token_of_current_provider_by_name_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_named_token_of_current_provider_by_name_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def get_named_token_of_current_provider_by_name_with_http_info(self, name, **kwargs):  # noqa: E501
        """Get named token of current provider by name  # noqa: E501

        Returns the information about a provider's named token by token name.  This operation can be invoked on behalf of the current provider only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Get named token of current provider by name** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/provider/tokens/named/name/my-token-1 {   \"id\": \"2b5d0dd5aa6443a69277b5ce0544fec2\",   \"name\": \"my-token-1\",   \"subject\": {     \"type\": \"provider\",     \"id\": \"6ebe7ac282e0188b5336b5d8cfa564d5\"   },   \"type\": {     \"inviteToken\": {       \"inviteType\": \"userJoinCluster\",       \"clusterId\": \"fb73f7ceff5abd995357abbe01c812ce\"     }   },   \"caveats\": [     {       \"type\": \"time\",       \"validUntil\": 1571147494     },     {       \"type\": \"ip\",       \"whitelist\": [         \"189.34.15.0/8\",         \"127.0.0.0/24\",         \"167.73.12.17\"       ]     }   ],   \"metadata\": {     \"creationTime\": 1564721024,     \"usageLimit\": 15,     \"usageCount\": 3,     \"privileges\": [       \"space_view\",       \"space_read_data\",       \"space_view_views\",       \"space_view_statistics\"     ],     \"custom\": {       \"jobName\": \"experiment-15\",       \"vm\": \"worker156.cloud.local\"     }   },   \"revoked\": false,   \"token\": \"MDAxNWxvY2F0aW9uIG9uZXpvbmUKMDAzYmlkZW50aWZpZXIgOEhmSEFSSGdrbHFCa1pWSTR\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_named_token_of_current_provider_by_name_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Token name (required)
        :return: NamedToken
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_named_token_of_current_provider_by_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_named_token_of_current_provider_by_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

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
            '/provider/tokens/named/name/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NamedToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_named_token_of_current_user_by_name(self, name, **kwargs):  # noqa: E501
        """Get named token of current user by name  # noqa: E501

        Returns the information about a user's named token by token name.  This operation can be invoked on behalf of the current user only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Get named token of current user by name** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/tokens/named/name/my-token-1 {   \"id\": \"2b5d0dd5aa6443a69277b5ce0544fec2\",   \"name\": \"my-token-1\",   \"subject\": {     \"type\": \"user\",     \"id\": \"c26bab23d12f7389c3c311caf9c15902\"   },   \"type\": {     \"inviteToken\": {       \"inviteType\": \"userJoinCluster\",       \"clusterId\": \"fb73f7ceff5abd995357abbe01c812ce\"     }   },   \"caveats\": [     {       \"type\": \"time\",       \"validUntil\": 1571147494     },     {       \"type\": \"ip\",       \"whitelist\": [         \"189.34.15.0/8\",         \"127.0.0.0/24\",         \"167.73.12.17\"       ]     }   ],   \"metadata\": {     \"creationTime\": 1564721024,     \"usageLimit\": 15,     \"usageCount\": 3,     \"privileges\": [       \"space_view\",       \"space_read_data\",       \"space_view_views\",       \"space_view_statistics\"     ],     \"custom\": {       \"jobName\": \"experiment-15\",       \"vm\": \"worker156.cloud.local\"     }   },   \"revoked\": false,   \"token\": \"MDAxNWxvY2F0aW9uIG9uZXpvbmUKMDAzYmlkZW50aWZpZXIgOEhmSEFSSGdrbHFCa1pWSTR\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_named_token_of_current_user_by_name(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Token name (required)
        :return: NamedToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_named_token_of_current_user_by_name_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_named_token_of_current_user_by_name_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def get_named_token_of_current_user_by_name_with_http_info(self, name, **kwargs):  # noqa: E501
        """Get named token of current user by name  # noqa: E501

        Returns the information about a user's named token by token name.  This operation can be invoked on behalf of the current user only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Get named token of current user by name** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/tokens/named/name/my-token-1 {   \"id\": \"2b5d0dd5aa6443a69277b5ce0544fec2\",   \"name\": \"my-token-1\",   \"subject\": {     \"type\": \"user\",     \"id\": \"c26bab23d12f7389c3c311caf9c15902\"   },   \"type\": {     \"inviteToken\": {       \"inviteType\": \"userJoinCluster\",       \"clusterId\": \"fb73f7ceff5abd995357abbe01c812ce\"     }   },   \"caveats\": [     {       \"type\": \"time\",       \"validUntil\": 1571147494     },     {       \"type\": \"ip\",       \"whitelist\": [         \"189.34.15.0/8\",         \"127.0.0.0/24\",         \"167.73.12.17\"       ]     }   ],   \"metadata\": {     \"creationTime\": 1564721024,     \"usageLimit\": 15,     \"usageCount\": 3,     \"privileges\": [       \"space_view\",       \"space_read_data\",       \"space_view_views\",       \"space_view_statistics\"     ],     \"custom\": {       \"jobName\": \"experiment-15\",       \"vm\": \"worker156.cloud.local\"     }   },   \"revoked\": false,   \"token\": \"MDAxNWxvY2F0aW9uIG9uZXpvbmUKMDAzYmlkZW50aWZpZXIgOEhmSEFSSGdrbHFCa1pWSTR\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_named_token_of_current_user_by_name_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Token name (required)
        :return: NamedToken
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_named_token_of_current_user_by_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_named_token_of_current_user_by_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

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
            '/user/tokens/named/name/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NamedToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_named_token_of_provider_by_name(self, id, name, **kwargs):  # noqa: E501
        """Get named token of a provider by name  # noqa: E501

        Returns the information about a specific provider's named token by token name.  This operation is available for the subject provider (`id`), or the provider's cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Get named token of a provider by name** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/tokens/named/name/my-token-1 {   \"id\": \"2b5d0dd5aa6443a69277b5ce0544fec2\",   \"name\": \"my-token-1\",   \"subject\": {     \"type\": \"provider\",     \"id\": \"6ebe7ac282e0188b5336b5d8cfa564d5\"   },   \"type\": {     \"inviteToken\": {       \"inviteType\": \"userJoinCluster\",       \"clusterId\": \"fb73f7ceff5abd995357abbe01c812ce\"     }   },   \"caveats\": [     {       \"type\": \"time\",       \"validUntil\": 1571147494     },     {       \"type\": \"ip\",       \"whitelist\": [         \"189.34.15.0/8\",         \"127.0.0.0/24\",         \"167.73.12.17\"       ]     }   ],   \"metadata\": {     \"creationTime\": 1564721024,     \"usageLimit\": 15,     \"usageCount\": 3,     \"privileges\": [       \"space_view\",       \"space_read_data\",       \"space_view_views\",       \"space_view_statistics\"     ],     \"custom\": {       \"jobName\": \"experiment-15\",       \"vm\": \"worker156.cloud.local\"     }   },   \"revoked\": false,   \"token\": \"MDAxNWxvY2F0aW9uIG9uZXpvbmUKMDAzYmlkZW50aWZpZXIgOEhmSEFSSGdrbHFCa1pWSTR\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_named_token_of_provider_by_name(id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id (required)
        :param str name: Token name (required)
        :return: NamedToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_named_token_of_provider_by_name_with_http_info(id, name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_named_token_of_provider_by_name_with_http_info(id, name, **kwargs)  # noqa: E501
            return data

    def get_named_token_of_provider_by_name_with_http_info(self, id, name, **kwargs):  # noqa: E501
        """Get named token of a provider by name  # noqa: E501

        Returns the information about a specific provider's named token by token name.  This operation is available for the subject provider (`id`), or the provider's cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Get named token of a provider by name** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/tokens/named/name/my-token-1 {   \"id\": \"2b5d0dd5aa6443a69277b5ce0544fec2\",   \"name\": \"my-token-1\",   \"subject\": {     \"type\": \"provider\",     \"id\": \"6ebe7ac282e0188b5336b5d8cfa564d5\"   },   \"type\": {     \"inviteToken\": {       \"inviteType\": \"userJoinCluster\",       \"clusterId\": \"fb73f7ceff5abd995357abbe01c812ce\"     }   },   \"caveats\": [     {       \"type\": \"time\",       \"validUntil\": 1571147494     },     {       \"type\": \"ip\",       \"whitelist\": [         \"189.34.15.0/8\",         \"127.0.0.0/24\",         \"167.73.12.17\"       ]     }   ],   \"metadata\": {     \"creationTime\": 1564721024,     \"usageLimit\": 15,     \"usageCount\": 3,     \"privileges\": [       \"space_view\",       \"space_read_data\",       \"space_view_views\",       \"space_view_statistics\"     ],     \"custom\": {       \"jobName\": \"experiment-15\",       \"vm\": \"worker156.cloud.local\"     }   },   \"revoked\": false,   \"token\": \"MDAxNWxvY2F0aW9uIG9uZXpvbmUKMDAzYmlkZW50aWZpZXIgOEhmSEFSSGdrbHFCa1pWSTR\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_named_token_of_provider_by_name_with_http_info(id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id (required)
        :param str name: Token name (required)
        :return: NamedToken
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_named_token_of_provider_by_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_named_token_of_provider_by_name`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_named_token_of_provider_by_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

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
            '/providers/{id}/tokens/named/name/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NamedToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_named_token_of_user_by_name(self, id, name, **kwargs):  # noqa: E501
        """Get named token of a user by name  # noqa: E501

        Returns the information about a specific user's named token by token name.  This operation is available for the token owner (subject), otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Get named token of a user by name** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/tokens/named/name/my-token-1 {   \"id\": \"2b5d0dd5aa6443a69277b5ce0544fec2\",   \"name\": \"my-token-1\",   \"subject\": {     \"type\": \"user\",     \"id\": \"c26bab23d12f7389c3c311caf9c15902\"   },   \"type\": {     \"inviteToken\": {       \"inviteType\": \"userJoinCluster\",       \"clusterId\": \"fb73f7ceff5abd995357abbe01c812ce\"     }   },   \"caveats\": [     {       \"type\": \"time\",       \"validUntil\": 1571147494     },     {       \"type\": \"ip\",       \"whitelist\": [         \"189.34.15.0/8\",         \"127.0.0.0/24\",         \"167.73.12.17\"       ]     }   ],   \"metadata\": {     \"creationTime\": 1564721024,     \"usageLimit\": 15,     \"usageCount\": 3,     \"privileges\": [       \"space_view\",       \"space_read_data\",       \"space_view_views\",       \"space_view_statistics\"     ],     \"custom\": {       \"jobName\": \"experiment-15\",       \"vm\": \"worker156.cloud.local\"     }   },   \"revoked\": false,   \"token\": \"MDAxNWxvY2F0aW9uIG9uZXpvbmUKMDAzYmlkZW50aWZpZXIgOEhmSEFSSGdrbHFCa1pWSTR\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_named_token_of_user_by_name(id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id (required)
        :param str name: Token name (required)
        :return: NamedToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_named_token_of_user_by_name_with_http_info(id, name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_named_token_of_user_by_name_with_http_info(id, name, **kwargs)  # noqa: E501
            return data

    def get_named_token_of_user_by_name_with_http_info(self, id, name, **kwargs):  # noqa: E501
        """Get named token of a user by name  # noqa: E501

        Returns the information about a specific user's named token by token name.  This operation is available for the token owner (subject), otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Get named token of a user by name** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/tokens/named/name/my-token-1 {   \"id\": \"2b5d0dd5aa6443a69277b5ce0544fec2\",   \"name\": \"my-token-1\",   \"subject\": {     \"type\": \"user\",     \"id\": \"c26bab23d12f7389c3c311caf9c15902\"   },   \"type\": {     \"inviteToken\": {       \"inviteType\": \"userJoinCluster\",       \"clusterId\": \"fb73f7ceff5abd995357abbe01c812ce\"     }   },   \"caveats\": [     {       \"type\": \"time\",       \"validUntil\": 1571147494     },     {       \"type\": \"ip\",       \"whitelist\": [         \"189.34.15.0/8\",         \"127.0.0.0/24\",         \"167.73.12.17\"       ]     }   ],   \"metadata\": {     \"creationTime\": 1564721024,     \"usageLimit\": 15,     \"usageCount\": 3,     \"privileges\": [       \"space_view\",       \"space_read_data\",       \"space_view_views\",       \"space_view_statistics\"     ],     \"custom\": {       \"jobName\": \"experiment-15\",       \"vm\": \"worker156.cloud.local\"     }   },   \"revoked\": false,   \"token\": \"MDAxNWxvY2F0aW9uIG9uZXpvbmUKMDAzYmlkZW50aWZpZXIgOEhmSEFSSGdrbHFCa1pWSTR\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_named_token_of_user_by_name_with_http_info(id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id (required)
        :param str name: Token name (required)
        :return: NamedToken
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_named_token_of_user_by_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_named_token_of_user_by_name`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_named_token_of_user_by_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

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
            '/users/{id}/tokens/named/name/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NamedToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_named_token_status(self, id, **kwargs):  # noqa: E501
        """Get named token status  # noqa: E501

        Returns the status of a specific named token - information if the token is currently revoked.  This operation is available for: * the token owner (subject) * in case of user tokens - a provider that supports the user * in case of provider tokens - the provider cluster member * admins with `oz_tokens_manage` privilege.  ***Example cURL requests***  **Get named token status** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/tokens/named/$TOKEN_ID/status {   \"revoked\": false } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_named_token_status(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Token Id (required)
        :return: NamedTokenStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_named_token_status_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_named_token_status_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_named_token_status_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get named token status  # noqa: E501

        Returns the status of a specific named token - information if the token is currently revoked.  This operation is available for: * the token owner (subject) * in case of user tokens - a provider that supports the user * in case of provider tokens - the provider cluster member * admins with `oz_tokens_manage` privilege.  ***Example cURL requests***  **Get named token status** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/tokens/named/$TOKEN_ID/status {   \"revoked\": false } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_named_token_status_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Token Id (required)
        :return: NamedTokenStatus
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
                    " to method get_named_token_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_named_token_status`")  # noqa: E501

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
            '/tokens/named/{id}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NamedTokenStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_temporary_token_generation_of_current_provider(self, **kwargs):  # noqa: E501
        """Get temporary token generation of current provider  # noqa: E501

        Returns the generation of temporary tokens of the provider. The generation is an increasing number that denotes the generation of shared token secret - if the secret changes (temporary tokens are revoked), the generation is incremented.  This operation can be invoked on behalf of the current provider only.  ***Example cURL requests***  **Get temporary token generation of current provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/provider/tokens/temporary  {   \"generation\": 3 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_temporary_token_generation_of_current_provider(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: TemporaryTokenGeneration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_temporary_token_generation_of_current_provider_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_temporary_token_generation_of_current_provider_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_temporary_token_generation_of_current_provider_with_http_info(self, **kwargs):  # noqa: E501
        """Get temporary token generation of current provider  # noqa: E501

        Returns the generation of temporary tokens of the provider. The generation is an increasing number that denotes the generation of shared token secret - if the secret changes (temporary tokens are revoked), the generation is incremented.  This operation can be invoked on behalf of the current provider only.  ***Example cURL requests***  **Get temporary token generation of current provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/provider/tokens/temporary  {   \"generation\": 3 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_temporary_token_generation_of_current_provider_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: TemporaryTokenGeneration
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
                    " to method get_temporary_token_generation_of_current_provider" % key
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
            '/provider/tokens/temporary', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TemporaryTokenGeneration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_temporary_token_generation_of_current_user(self, **kwargs):  # noqa: E501
        """Get temporary token generation of current user  # noqa: E501

        Returns the generation of temporary tokens of the user. The generation is an increasing number that denotes the generation of shared token secret - if the secret changes (temporary tokens are revoked), the generation is incremented.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get temporary token generation of current user** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/tokens/temporary  {   \"generation\": 3 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_temporary_token_generation_of_current_user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: TemporaryTokenGeneration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_temporary_token_generation_of_current_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_temporary_token_generation_of_current_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_temporary_token_generation_of_current_user_with_http_info(self, **kwargs):  # noqa: E501
        """Get temporary token generation of current user  # noqa: E501

        Returns the generation of temporary tokens of the user. The generation is an increasing number that denotes the generation of shared token secret - if the secret changes (temporary tokens are revoked), the generation is incremented.  This operation can be invoked on behalf of the current user only.  ***Example cURL requests***  **Get temporary token generation of current user** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/tokens/temporary  {   \"generation\": 3 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_temporary_token_generation_of_current_user_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: TemporaryTokenGeneration
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
                    " to method get_temporary_token_generation_of_current_user" % key
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
            '/user/tokens/temporary', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TemporaryTokenGeneration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_temporary_token_generation_of_provider(self, id, **kwargs):  # noqa: E501
        """Get temporary token generation of a provider  # noqa: E501

        Returns the generation of temporary tokens of a specific provider. The generation is an increasing number that denotes the generation of shared token secret - if the secret changes (temporary tokens are revoked), the generation is incremented.  This operation is available for the subject provider (`id`), or the provider's cluster member. Otherwise requires `oz_tokens_manage` admin privilege.  ***Example cURL requests***  **Get temporary token generation of a provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/tokens/temporary  {   \"generation\": 3 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_temporary_token_generation_of_provider(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id (required)
        :return: TemporaryTokenGeneration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_temporary_token_generation_of_provider_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_temporary_token_generation_of_provider_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_temporary_token_generation_of_provider_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get temporary token generation of a provider  # noqa: E501

        Returns the generation of temporary tokens of a specific provider. The generation is an increasing number that denotes the generation of shared token secret - if the secret changes (temporary tokens are revoked), the generation is incremented.  This operation is available for the subject provider (`id`), or the provider's cluster member. Otherwise requires `oz_tokens_manage` admin privilege.  ***Example cURL requests***  **Get temporary token generation of a provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/tokens/temporary  {   \"generation\": 3 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_temporary_token_generation_of_provider_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id (required)
        :return: TemporaryTokenGeneration
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
                    " to method get_temporary_token_generation_of_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_temporary_token_generation_of_provider`")  # noqa: E501

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
            '/providers/{id}/tokens/temporary', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TemporaryTokenGeneration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_temporary_token_generation_of_user(self, id, **kwargs):  # noqa: E501
        """Get temporary token generation of a user  # noqa: E501

        Returns the generation of temporary tokens of a specific user. The generation is an increasing number that denotes the generation of shared token secret - if the secret changes (temporary tokens are revoked), the generation is incremented.  This operation is available for the currently authorized user and provider that supports the user, otherwise requires `oz_tokens_manage` admin privilege.  ***Example cURL requests***  **Get temporary token generation of a user** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/tokens/temporary  {   \"generation\": 3 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_temporary_token_generation_of_user(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id (required)
        :return: TemporaryTokenGeneration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_temporary_token_generation_of_user_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_temporary_token_generation_of_user_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_temporary_token_generation_of_user_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get temporary token generation of a user  # noqa: E501

        Returns the generation of temporary tokens of a specific user. The generation is an increasing number that denotes the generation of shared token secret - if the secret changes (temporary tokens are revoked), the generation is incremented.  This operation is available for the currently authorized user and provider that supports the user, otherwise requires `oz_tokens_manage` admin privilege.  ***Example cURL requests***  **Get temporary token generation of a user** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/tokens/temporary  {   \"generation\": 3 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_temporary_token_generation_of_user_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id (required)
        :return: TemporaryTokenGeneration
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
                    " to method get_temporary_token_generation_of_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_temporary_token_generation_of_user`")  # noqa: E501

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
            '/users/{id}/tokens/temporary', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TemporaryTokenGeneration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_all_named_tokens(self, **kwargs):  # noqa: E501
        """List all named tokens  # noqa: E501

        Returns the list of all tokens in the system. The results include ids of users' and providers' named tokens - temporary tokens are not included as they are not persisted in the system.  Requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **List all named tokens** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/tokens  {   \"tokens\": [     \"2b5d0dd5aa6443a69277b5ce0544fec2\",     \"818bf8d4404c2bcee2b47f024f6c0890\",     \"4a5e5dabcd55e03f1e9237eeca2548ff\",     \"81336b59656653a481d1e65168f3f213\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_all_named_tokens(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Tokens
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_all_named_tokens_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_all_named_tokens_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_all_named_tokens_with_http_info(self, **kwargs):  # noqa: E501
        """List all named tokens  # noqa: E501

        Returns the list of all tokens in the system. The results include ids of users' and providers' named tokens - temporary tokens are not included as they are not persisted in the system.  Requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **List all named tokens** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/tokens  {   \"tokens\": [     \"2b5d0dd5aa6443a69277b5ce0544fec2\",     \"818bf8d4404c2bcee2b47f024f6c0890\",     \"4a5e5dabcd55e03f1e9237eeca2548ff\",     \"81336b59656653a481d1e65168f3f213\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_all_named_tokens_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Tokens
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
                    " to method list_all_named_tokens" % key
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
            '/tokens/named', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Tokens',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_named_tokens_of_current_provider(self, **kwargs):  # noqa: E501
        """List named tokens of current provider  # noqa: E501

        Returns the list of provider's named tokens.  This operation can be invoked on behalf of the current provider only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **List named tokens of current provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/provider/tokens/named  {   \"tokens\": [     \"2b5d0dd5aa6443a69277b5ce0544fec2\",     \"818bf8d4404c2bcee2b47f024f6c0890\",     \"4a5e5dabcd55e03f1e9237eeca2548ff\",     \"81336b59656653a481d1e65168f3f213\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_named_tokens_of_current_provider(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Tokens
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_named_tokens_of_current_provider_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_named_tokens_of_current_provider_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_named_tokens_of_current_provider_with_http_info(self, **kwargs):  # noqa: E501
        """List named tokens of current provider  # noqa: E501

        Returns the list of provider's named tokens.  This operation can be invoked on behalf of the current provider only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **List named tokens of current provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/provider/tokens/named  {   \"tokens\": [     \"2b5d0dd5aa6443a69277b5ce0544fec2\",     \"818bf8d4404c2bcee2b47f024f6c0890\",     \"4a5e5dabcd55e03f1e9237eeca2548ff\",     \"81336b59656653a481d1e65168f3f213\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_named_tokens_of_current_provider_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Tokens
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
                    " to method list_named_tokens_of_current_provider" % key
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
            '/provider/tokens/named', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Tokens',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_named_tokens_of_current_user(self, **kwargs):  # noqa: E501
        """List named tokens of current user  # noqa: E501

        Returns the list of user's named tokens.  This operation can be invoked on behalf of the current user only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **List named tokens of current user** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/tokens/named  {   \"tokens\": [     \"2b5d0dd5aa6443a69277b5ce0544fec2\",     \"818bf8d4404c2bcee2b47f024f6c0890\",     \"4a5e5dabcd55e03f1e9237eeca2548ff\",     \"81336b59656653a481d1e65168f3f213\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_named_tokens_of_current_user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Tokens
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_named_tokens_of_current_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_named_tokens_of_current_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_named_tokens_of_current_user_with_http_info(self, **kwargs):  # noqa: E501
        """List named tokens of current user  # noqa: E501

        Returns the list of user's named tokens.  This operation can be invoked on behalf of the current user only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **List named tokens of current user** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/user/tokens/named  {   \"tokens\": [     \"2b5d0dd5aa6443a69277b5ce0544fec2\",     \"818bf8d4404c2bcee2b47f024f6c0890\",     \"4a5e5dabcd55e03f1e9237eeca2548ff\",     \"81336b59656653a481d1e65168f3f213\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_named_tokens_of_current_user_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Tokens
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
                    " to method list_named_tokens_of_current_user" % key
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
            '/user/tokens/named', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Tokens',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_named_tokens_of_provider(self, id, **kwargs):  # noqa: E501
        """List named tokens of a provider  # noqa: E501

        Returns the list of specific provider's named tokens.  This operation is available for the subject provider (`id`), or the provider's cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **List named tokens of a provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/tokens/named  {   \"tokens\": [     \"2b5d0dd5aa6443a69277b5ce0544fec2\",     \"818bf8d4404c2bcee2b47f024f6c0890\",     \"4a5e5dabcd55e03f1e9237eeca2548ff\",     \"81336b59656653a481d1e65168f3f213\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_named_tokens_of_provider(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id (required)
        :return: Tokens
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_named_tokens_of_provider_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_named_tokens_of_provider_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_named_tokens_of_provider_with_http_info(self, id, **kwargs):  # noqa: E501
        """List named tokens of a provider  # noqa: E501

        Returns the list of specific provider's named tokens.  This operation is available for the subject provider (`id`), or the provider's cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **List named tokens of a provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X GET \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/tokens/named  {   \"tokens\": [     \"2b5d0dd5aa6443a69277b5ce0544fec2\",     \"818bf8d4404c2bcee2b47f024f6c0890\",     \"4a5e5dabcd55e03f1e9237eeca2548ff\",     \"81336b59656653a481d1e65168f3f213\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_named_tokens_of_provider_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id (required)
        :return: Tokens
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
                    " to method list_named_tokens_of_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_named_tokens_of_provider`")  # noqa: E501

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
            '/providers/{id}/tokens/named', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Tokens',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_named_tokens_of_user(self, id, **kwargs):  # noqa: E501
        """List named tokens of a user  # noqa: E501

        Returns the list of specific user's named tokens.  This operation is available for the currently authorized user, otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **List named tokens of a user** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/tokens/named  {   \"tokens\": [     \"2b5d0dd5aa6443a69277b5ce0544fec2\",     \"818bf8d4404c2bcee2b47f024f6c0890\",     \"4a5e5dabcd55e03f1e9237eeca2548ff\",     \"81336b59656653a481d1e65168f3f213\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_named_tokens_of_user(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id (required)
        :return: Tokens
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_named_tokens_of_user_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_named_tokens_of_user_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_named_tokens_of_user_with_http_info(self, id, **kwargs):  # noqa: E501
        """List named tokens of a user  # noqa: E501

        Returns the list of specific user's named tokens.  This operation is available for the currently authorized user, otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **List named tokens of a user** ```bash curl -u username:password -X GET \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/tokens/named  {   \"tokens\": [     \"2b5d0dd5aa6443a69277b5ce0544fec2\",     \"818bf8d4404c2bcee2b47f024f6c0890\",     \"4a5e5dabcd55e03f1e9237eeca2548ff\",     \"81336b59656653a481d1e65168f3f213\"   ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_named_tokens_of_user_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id (required)
        :return: Tokens
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
                    " to method list_named_tokens_of_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_named_tokens_of_user`")  # noqa: E501

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
            '/users/{id}/tokens/named', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Tokens',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_named_token(self, body, id, **kwargs):  # noqa: E501
        """Modify named token  # noqa: E501

        Modifies a specific named token. Supports renaming the token, toggling the revoked flag and modifying the metadata.  This operation is available for the token owner (subject), or (in case of provider tokens) cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Modify named token** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"revoked\": true}' \\ https://$ZONE_HOST/api/v3/onezone/tokens/named/$TOKEN_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_named_token(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NamedTokenUpdateRequest body: Named token update request (required)
        :param str id: Token Id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_named_token_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_named_token_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def modify_named_token_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Modify named token  # noqa: E501

        Modifies a specific named token. Supports renaming the token, toggling the revoked flag and modifying the metadata.  This operation is available for the token owner (subject), or (in case of provider tokens) cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Modify named token** ```bash curl -u username:password -H \"Content-type: application/json\" \\ -X PATCH -d '{\"revoked\": true}' \\ https://$ZONE_HOST/api/v3/onezone/tokens/named/$TOKEN_ID ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_named_token_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NamedTokenUpdateRequest body: Named token update request (required)
        :param str id: Token Id (required)
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
                    " to method modify_named_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `modify_named_token`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `modify_named_token`")  # noqa: E501

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
            '/tokens/named/{id}', 'PATCH',
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

    def revoke_all_temporary_tokens_of_current_provider(self, **kwargs):  # noqa: E501
        """Revoke all temporary tokens of current provider  # noqa: E501

        Immediately revokes (invalidates) all temporary tokens belonging to the provider. The operation cannot be undone.  This operation can be invoked on behalf of the current provider only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Revoke all temporary tokens of current provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/provider/tokens/temporary ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revoke_all_temporary_tokens_of_current_provider(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.revoke_all_temporary_tokens_of_current_provider_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.revoke_all_temporary_tokens_of_current_provider_with_http_info(**kwargs)  # noqa: E501
            return data

    def revoke_all_temporary_tokens_of_current_provider_with_http_info(self, **kwargs):  # noqa: E501
        """Revoke all temporary tokens of current provider  # noqa: E501

        Immediately revokes (invalidates) all temporary tokens belonging to the provider. The operation cannot be undone.  This operation can be invoked on behalf of the current provider only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Revoke all temporary tokens of current provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/provider/tokens/temporary ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revoke_all_temporary_tokens_of_current_provider_with_http_info(async_req=True)
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
                    " to method revoke_all_temporary_tokens_of_current_provider" % key
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
            '/provider/tokens/temporary', 'DELETE',
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

    def revoke_all_temporary_tokens_of_current_user(self, **kwargs):  # noqa: E501
        """Revoke all temporary tokens of current user  # noqa: E501

        Immediately revokes (invalidates) all temporary tokens belonging to the user. The operation cannot be undone.  This operation can be invoked on behalf of the current user only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Revoke all temporary tokens of current user** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/tokens/temporary ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revoke_all_temporary_tokens_of_current_user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.revoke_all_temporary_tokens_of_current_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.revoke_all_temporary_tokens_of_current_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def revoke_all_temporary_tokens_of_current_user_with_http_info(self, **kwargs):  # noqa: E501
        """Revoke all temporary tokens of current user  # noqa: E501

        Immediately revokes (invalidates) all temporary tokens belonging to the user. The operation cannot be undone.  This operation can be invoked on behalf of the current user only.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Revoke all temporary tokens of current user** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/user/tokens/temporary ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revoke_all_temporary_tokens_of_current_user_with_http_info(async_req=True)
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
                    " to method revoke_all_temporary_tokens_of_current_user" % key
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
            '/user/tokens/temporary', 'DELETE',
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

    def revoke_all_temporary_tokens_of_provider(self, id, **kwargs):  # noqa: E501
        """Revoke all temporary tokens of a provider  # noqa: E501

        Immediately revokes (invalidates) all temporary tokens belonging to a specific provider. The operation cannot be undone.  This operation is available for the subject provider (`id`), or the provider's cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Revoke all temporary tokens of a provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/tokens/temporary ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revoke_all_temporary_tokens_of_provider(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.revoke_all_temporary_tokens_of_provider_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.revoke_all_temporary_tokens_of_provider_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def revoke_all_temporary_tokens_of_provider_with_http_info(self, id, **kwargs):  # noqa: E501
        """Revoke all temporary tokens of a provider  # noqa: E501

        Immediately revokes (invalidates) all temporary tokens belonging to a specific provider. The operation cannot be undone.  This operation is available for the subject provider (`id`), or the provider's cluster member with `cluster_update` privilege. Otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Revoke all temporary tokens of a provider** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/providers/$PROVIDER_ID/tokens/temporary ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revoke_all_temporary_tokens_of_provider_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Provider Id (required)
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
                    " to method revoke_all_temporary_tokens_of_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `revoke_all_temporary_tokens_of_provider`")  # noqa: E501

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
            '/providers/{id}/tokens/temporary', 'DELETE',
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

    def revoke_all_temporary_tokens_of_user(self, id, **kwargs):  # noqa: E501
        """Revoke all temporary tokens of a user  # noqa: E501

        Immediately revokes (invalidates) all temporary tokens belonging to a specific user. The operation cannot be undone.  This operation is available for the currently authorized user, otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Revoke all temporary tokens of a user** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/tokens/temporary ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revoke_all_temporary_tokens_of_user(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.revoke_all_temporary_tokens_of_user_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.revoke_all_temporary_tokens_of_user_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def revoke_all_temporary_tokens_of_user_with_http_info(self, id, **kwargs):  # noqa: E501
        """Revoke all temporary tokens of a user  # noqa: E501

        Immediately revokes (invalidates) all temporary tokens belonging to a specific user. The operation cannot be undone.  This operation is available for the currently authorized user, otherwise requires `oz_tokens_manage` admin privilege.  You can learn more about named and temporary tokens [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[named-and-temporary-tokens].html).  ***Example cURL requests***  **Revoke all temporary tokens of a user** ```bash curl -H \"x-auth-token: $TOKEN\" -X DELETE \\ https://$ZONE_HOST/api/v3/onezone/users/$USER_ID/tokens/temporary ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revoke_all_temporary_tokens_of_user_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: User Id (required)
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
                    " to method revoke_all_temporary_tokens_of_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `revoke_all_temporary_tokens_of_user`")  # noqa: E501

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
            '/users/{id}/tokens/temporary', 'DELETE',
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

    def verify_access_token(self, **kwargs):  # noqa: E501
        """Verify an access token  # noqa: E501

        Verifies an [access token](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[access-tokens].html) provided in serialized form. Upon success, returns the token's subject.  Optionally, contextual information that may be required to verify token caveats can be provided in the request body:  * IP address of the token bearer - defaults to the requesting client's IP, * identity token of the service which is handling the request - defaults to `null`, * consumer's identity token - consumer defaults to the authenticated client   if valid token credentials are sent with this request, or `null` otherwise, * interface to which the token bearer has connected - defaults to `null` (undefined interface), * information if data access caveats should be allowed in the token - defaults to `false`.  If the token cannot be positively verified, HTTP code 4xx is returned with an error describing the reason of failure.  This operation has public access.  ***Example cURL requests***  **Verify an access token** ```bash curl -d '{\"token\": \"MDAxNmxvY2F00aW9uIHZ2...\", \"peerIp\": \"38.190.241.12\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/tokens/verify_access_token  {   \"subject\": {     \"type\": \"user\",     \"id\": \"1b510f18b3b05611871c0acdffa9aed4\"   },   \"ttl\": 3600 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_access_token(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VerifyAccessTokenRequest body: The token to be verified and optionally peer's IP address.
        :return: VerifyTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.verify_access_token_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.verify_access_token_with_http_info(**kwargs)  # noqa: E501
            return data

    def verify_access_token_with_http_info(self, **kwargs):  # noqa: E501
        """Verify an access token  # noqa: E501

        Verifies an [access token](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[access-tokens].html) provided in serialized form. Upon success, returns the token's subject.  Optionally, contextual information that may be required to verify token caveats can be provided in the request body:  * IP address of the token bearer - defaults to the requesting client's IP, * identity token of the service which is handling the request - defaults to `null`, * consumer's identity token - consumer defaults to the authenticated client   if valid token credentials are sent with this request, or `null` otherwise, * interface to which the token bearer has connected - defaults to `null` (undefined interface), * information if data access caveats should be allowed in the token - defaults to `false`.  If the token cannot be positively verified, HTTP code 4xx is returned with an error describing the reason of failure.  This operation has public access.  ***Example cURL requests***  **Verify an access token** ```bash curl -d '{\"token\": \"MDAxNmxvY2F00aW9uIHZ2...\", \"peerIp\": \"38.190.241.12\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/tokens/verify_access_token  {   \"subject\": {     \"type\": \"user\",     \"id\": \"1b510f18b3b05611871c0acdffa9aed4\"   },   \"ttl\": 3600 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_access_token_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VerifyAccessTokenRequest body: The token to be verified and optionally peer's IP address.
        :return: VerifyTokenResponse
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
                    " to method verify_access_token" % key
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
            '/tokens/verify_access_token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VerifyTokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def verify_identity_token(self, body, **kwargs):  # noqa: E501
        """Verify an identity token  # noqa: E501

        Verifies an [identity token](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[identity-tokens].html) provided in serialized form. Identity token is a token that carries proof of identity, but does not carry authorization to perform any operations in the system. Upon success, returns the token's subject.  Optionally, contextual information that may be required to verify token caveats can be provided in the request body:  * IP address of the token bearer - defaults to the requesting client's IP, * consumer's identity token - consumer defaults to the authenticated client   if valid token credentials are sent with this request, or `null` otherwise, * interface to which the token bearer has connected - defaults to `null` (undefined interface).  If the token cannot be positively verified, HTTP code 4xx is returned with an error describing the reason of failure.  This operation has public access.  ***Example cURL requests***  **Verify an identity token** ```bash curl -d '{\"token\": \"MDAxNmxvY2F00aW9uIHZ2...\", \"peerIp\": \"38.190.241.12\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/tokens/verify_identity_token  {   \"subject\": {     \"type\": \"user\",     \"id\": \"1b510f18b3b05611871c0acdffa9aed4\"   },   \"ttl\": 3600 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_identity_token(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VerifyIdentityTokenRequest body: The token to be verified and optionally peer's IP address. (required)
        :return: VerifyTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.verify_identity_token_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.verify_identity_token_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def verify_identity_token_with_http_info(self, body, **kwargs):  # noqa: E501
        """Verify an identity token  # noqa: E501

        Verifies an [identity token](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[identity-tokens].html) provided in serialized form. Identity token is a token that carries proof of identity, but does not carry authorization to perform any operations in the system. Upon success, returns the token's subject.  Optionally, contextual information that may be required to verify token caveats can be provided in the request body:  * IP address of the token bearer - defaults to the requesting client's IP, * consumer's identity token - consumer defaults to the authenticated client   if valid token credentials are sent with this request, or `null` otherwise, * interface to which the token bearer has connected - defaults to `null` (undefined interface).  If the token cannot be positively verified, HTTP code 4xx is returned with an error describing the reason of failure.  This operation has public access.  ***Example cURL requests***  **Verify an identity token** ```bash curl -d '{\"token\": \"MDAxNmxvY2F00aW9uIHZ2...\", \"peerIp\": \"38.190.241.12\"}' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/tokens/verify_identity_token  {   \"subject\": {     \"type\": \"user\",     \"id\": \"1b510f18b3b05611871c0acdffa9aed4\"   },   \"ttl\": 3600 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_identity_token_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VerifyIdentityTokenRequest body: The token to be verified and optionally peer's IP address. (required)
        :return: VerifyTokenResponse
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
                    " to method verify_identity_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `verify_identity_token`")  # noqa: E501

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
            '/tokens/verify_identity_token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VerifyTokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def verify_invite_token(self, body, **kwargs):  # noqa: E501
        """Verify an invite token  # noqa: E501

        Verifies an [invite token](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[invite-tokens].html) provided in serialized form. Upon success, returns the token's subject. Does not check if the token can be effectively consumed (only if prerequisites are satisfied - the token itself is valid).  Optionally, contextual information that may be required to verify token caveats can be provided in the request body:  * IP address of the token bearer - defaults to the requesting client's IP, * consumer's identity token - consumer defaults to the authenticated client   if valid token credentials are sent with this request, or `null` otherwise, * expected invite token type, which will cause verification to fail if it   does not match the actual token type. If not specified, the procedure will   check if given token is an invite token of any type.  If the token cannot be positively verified, HTTP code 4xx is returned with an error describing the reason of failure.  This operation has public access.  ***Example cURL requests***  **Verify an invite token** ```bash curl -d '{   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaW\",   \"peerIp\": \"38.190.241.12\",   \"expectedInviteType\": \"userJoinGroup\" }' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/tokens/verify_invite_token  {   \"subject\": {     \"type\": \"user\",     \"id\": \"1b510f18b3b05611871c0acdffa9aed4\"   },   \"ttl\": 3600 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_invite_token(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VerifyInviteTokenRequest body: The token to be verified and optional parameters. (required)
        :return: VerifyTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.verify_invite_token_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.verify_invite_token_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def verify_invite_token_with_http_info(self, body, **kwargs):  # noqa: E501
        """Verify an invite token  # noqa: E501

        Verifies an [invite token](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[invite-tokens].html) provided in serialized form. Upon success, returns the token's subject. Does not check if the token can be effectively consumed (only if prerequisites are satisfied - the token itself is valid).  Optionally, contextual information that may be required to verify token caveats can be provided in the request body:  * IP address of the token bearer - defaults to the requesting client's IP, * consumer's identity token - consumer defaults to the authenticated client   if valid token credentials are sent with this request, or `null` otherwise, * expected invite token type, which will cause verification to fail if it   does not match the actual token type. If not specified, the procedure will   check if given token is an invite token of any type.  If the token cannot be positively verified, HTTP code 4xx is returned with an error describing the reason of failure.  This operation has public access.  ***Example cURL requests***  **Verify an invite token** ```bash curl -d '{   \"token\": \"MDAxNmxvY2F00aW9uIHJlZ2lzdHJ5CjAwM2JpZGVudGlmaW\",   \"peerIp\": \"38.190.241.12\",   \"expectedInviteType\": \"userJoinGroup\" }' \\ -H 'Content-type: application/json' \\ https://$ZONE_HOST/api/v3/onezone/tokens/verify_invite_token  {   \"subject\": {     \"type\": \"user\",     \"id\": \"1b510f18b3b05611871c0acdffa9aed4\"   },   \"ttl\": 3600 } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_invite_token_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VerifyInviteTokenRequest body: The token to be verified and optional parameters. (required)
        :return: VerifyTokenResponse
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
                    " to method verify_invite_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `verify_invite_token`")  # noqa: E501

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
            '/tokens/verify_invite_token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VerifyTokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
