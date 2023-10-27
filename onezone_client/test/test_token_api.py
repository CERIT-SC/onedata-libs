# coding: utf-8

"""
    Onezone

    # Overview This is the RESTful API definition of Onezone component of Onedata data management system [onedata.org](http://onedata.org).  > This API is defined using [Swagger](http://swagger.io/), the JSON specification can be used to automatically generate client libraries - [swagger.json](../../../swagger/onezone/swagger.json).  This API allows control and configuration of local Onezone service deployment, in particular management of users, groups, spaces, shares, providers, handle services, handles and clusters.  ## Authentication and authorization To be able to use this API, the REST client must authenticate with the Onezone service and posses required authorization, which is determined based on client's privileges and relations in the system.  There are essentially three types of REST clients depending on the authentication:   * **users** - can authenticate using an access token or basic credentials   (only for users originating from Onezone's onepanel). Examples:   ```bash   curl -H \"x-auth-token: $TOKEN\" [...]   curl -H \"authorization: Bearer $TOKEN\" [...]   curl -u \"username:password\" [...]   curl -H \"macaroon: $TOKEN\" [...]   # DEPRECATED   ```   > `$TOKEN` can ba a Onedata access token, obtained via Onezone GUI or API, in the form   `MDAxNWxvY2F00aW9...`. If authority delegation for given IdP is enabled,   it is possible to provide an access token from the IdP, which must be prefixed   properly (depending on the configuration), e.g.: `github/GST5aasdA...`.    * **Oneproviders** - can authenticate using the provider root token,   which was assigned during registration in Onezone. It can be found in   `/etc/op_worker/provider_root_token.txt`. It is used just like a user   access token, for example:   ```bash   curl -H \"x-auth-token: $TOKEN\" [...]   curl -H \"authorization: Bearer $TOKEN\" [...]   curl -H \"macaroon: $TOKEN\" [...]   # DEPRECATED   ```   > Please mind that the provider root token is highly confidential and must   be kept secret (similarly to a private RSA key).    * **anonymous** - there is a small subset of operations that do not require     any authentication and are publicly available (look for information about     public availability in the endpoint descriptions).  The authorization of the client is determined based on existing relations and privileges in the system. In most cases, the rules below can be roughly applied:   * users and providers can access and modify their own data   * users can perform operations in groups, spaces, handle services, handles     and clusters depending on their privileges in subject entity - the required     privileges are listed in the description of each operation   * users can be given special admin privileges (fine-grained) that allow to     access and modify all entities in the system - see certain operations for     details.  Authentication and Authorization errors have the following meaning:   * HTTP 401 UNAUTHORIZED - the client could not be authenticated   * HTTP 403 FORBIDDEN - the client was authenticated, but is not permitted to     perform the action  ## Effective users and effective groups and spaces Onedata supports creation of arbitrary nested group and space membership tree structures. In order to determine if a given user belongs to the group directly or indirectly by belonging to a subgroup of a group, separate API calls are provided for getting information about group users (direct group members) and effective users (indirect group members).  ## API structure The API is divided into several categories, corresponding to entities in Onedata:  **Space management** The space management operations of this API provide means for accessing information about spaces and their management.  **Share management** The share management operations of this API provide means for accessing information about shares and their management.  **Group management** The group management operations allow creation of user groups, assigning their authorization rights, adding and removing users from groups.  **User management** The user management methods allow creation of users, managing their authorization credentials as well as space and group membership.  **Provider management** Provider specific calls allow getting global information about the spaces managed by the provider, and some administrative operations which can be used for monitoring or accounting.  **Handle service management** The handle service management operations of this API provide means for accessing information about handle services and their management.  **Handle API** Onezone provides extensive support for integration with Handle system registration services, including support for DOI and PID identifier assignment services. The API provides methods for adding new Handle services to the system, managing which users can use which registration services and complete API for registering identifiers to users' data sets which are made public.  **Cluster management** Operations for managing Onezone / Oneprovider clusters and their members - users and groups that can access the Onepanel interfaces (REST or GUI) of a cluster.   ## Using the API Onezone API is quite complex and thus it might be difficult to quickly figure out how to perform specific action, however the following guidelines might be useful:   * Operations performed by a regular users on their resources are grouped under     `/user` path (**USER** group in the menu)   * Operations performed by administrators of specific resources (e.g. groups,     spaces, shares) start with specific resource (e.g. `/groups`)   * By default the operations which list resource membership     (e.g. `/spaces/SPACE_ID/groups/`) will list explicit resource membership.     To get list of effective resource membership (i.e. including indirect     membership), special paths are provided     (e.g. `/spaces/SPACE_ID/effective_groups/`)  Furthermore, we have prepared a command-line client environment based on Docker which gives easy access to each of Onedata services via command-line clients, with pre-configured shell with full help on the APIs and autocomplete for operations and attributes.  ``` docker run -it onedata/rest-cli:21.02.3 ```  Below you can find some tutorials which show how to use this API in practice:   * [User oriented tutorial](https://onedata.org/#/home/documentation/doc/using_onedata/using_onedata_from_cli.html)   * [Administrator oriented tutorial](https://onedata.org/#/home/documentation/doc/administering_onedata/administering_onedata_from_cli.html)   ## Examples  **Generate new authentication token** ```bash curl -u user:password -X POST -H 'Content-type: application/json' -d '{}' \\ https://$ONEZONE_HOST/api/v3/onezone/user/client_tokens ```  **Get user details** ```bash curl -H 'X-Auth-Token: $TOKEN' -X GET \\ https://$ONEZONE_HOST/api/v3/onezone/user ```  **Get user details using an access token from github** ```bash curl -H 'X-Auth-Token: github/ijaAVWq3j9234jA9gPoR9agFja89t9UiPf8tiueSdx' -X GET \\ https://$ONEZONE_HOST/api/v3/onezone/user ``` > Note that GitHub IdP must be properly configured for the example to work: > * authority delegation must be enabled > * tokenPrefix must be set to \"github/\" > > You can learn more in > [the documentation](https://onedata.org/#/home/documentation/doc/administering_onedata/openid_saml_configuration/openid_saml_configuration_19_02[authority-delegation].html).   # noqa: E501

    OpenAPI spec version: 21.02.3
    Contact: info@onedata.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import onezone_client
from onezone_client.api.token_api import TokenApi  # noqa: E501
from onezone_client.rest import ApiException


class TestTokenApi(unittest.TestCase):
    """TokenApi unit test stubs"""

    def setUp(self):
        self.api = TokenApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_confine_token(self):
        """Test case for confine_token

        Confine a token  # noqa: E501
        """
        pass

    def test_create_named_token_for_current_provider(self):
        """Test case for create_named_token_for_current_provider

        Create named token for current provider  # noqa: E501
        """
        pass

    def test_create_named_token_for_current_user(self):
        """Test case for create_named_token_for_current_user

        Create named token for current user  # noqa: E501
        """
        pass

    def test_create_named_token_for_provider(self):
        """Test case for create_named_token_for_provider

        Create named token for a provider  # noqa: E501
        """
        pass

    def test_create_named_token_for_user(self):
        """Test case for create_named_token_for_user

        Create named token for a user  # noqa: E501
        """
        pass

    def test_create_temporary_token_for_current_provider(self):
        """Test case for create_temporary_token_for_current_provider

        Create temporary token for current provider  # noqa: E501
        """
        pass

    def test_create_temporary_token_for_current_user(self):
        """Test case for create_temporary_token_for_current_user

        Create temporary token for current user  # noqa: E501
        """
        pass

    def test_create_temporary_token_for_provider(self):
        """Test case for create_temporary_token_for_provider

        Create temporary token for a provider  # noqa: E501
        """
        pass

    def test_create_temporary_token_for_user(self):
        """Test case for create_temporary_token_for_user

        Create temporary token for a user  # noqa: E501
        """
        pass

    def test_delete_named_token(self):
        """Test case for delete_named_token

        Delete named token  # noqa: E501
        """
        pass

    def test_delete_named_tokens_of_current_provider(self):
        """Test case for delete_named_tokens_of_current_provider

        Delete named tokens of current provider  # noqa: E501
        """
        pass

    def test_delete_named_tokens_of_current_user(self):
        """Test case for delete_named_tokens_of_current_user

        Delete named tokens of current user  # noqa: E501
        """
        pass

    def test_delete_named_tokens_of_provider(self):
        """Test case for delete_named_tokens_of_provider

        Delete named tokens of a provider  # noqa: E501
        """
        pass

    def test_delete_named_tokens_of_user(self):
        """Test case for delete_named_tokens_of_user

        Delete named tokens of a user  # noqa: E501
        """
        pass

    def test_examine_token(self):
        """Test case for examine_token

        Examine a token  # noqa: E501
        """
        pass

    def test_get_named_token(self):
        """Test case for get_named_token

        Get named token  # noqa: E501
        """
        pass

    def test_get_named_token_of_current_provider_by_name(self):
        """Test case for get_named_token_of_current_provider_by_name

        Get named token of current provider by name  # noqa: E501
        """
        pass

    def test_get_named_token_of_current_user_by_name(self):
        """Test case for get_named_token_of_current_user_by_name

        Get named token of current user by name  # noqa: E501
        """
        pass

    def test_get_named_token_of_provider_by_name(self):
        """Test case for get_named_token_of_provider_by_name

        Get named token of a provider by name  # noqa: E501
        """
        pass

    def test_get_named_token_of_user_by_name(self):
        """Test case for get_named_token_of_user_by_name

        Get named token of a user by name  # noqa: E501
        """
        pass

    def test_get_named_token_status(self):
        """Test case for get_named_token_status

        Get named token status  # noqa: E501
        """
        pass

    def test_get_temporary_token_generation_of_current_provider(self):
        """Test case for get_temporary_token_generation_of_current_provider

        Get temporary token generation of current provider  # noqa: E501
        """
        pass

    def test_get_temporary_token_generation_of_current_user(self):
        """Test case for get_temporary_token_generation_of_current_user

        Get temporary token generation of current user  # noqa: E501
        """
        pass

    def test_get_temporary_token_generation_of_provider(self):
        """Test case for get_temporary_token_generation_of_provider

        Get temporary token generation of a provider  # noqa: E501
        """
        pass

    def test_get_temporary_token_generation_of_user(self):
        """Test case for get_temporary_token_generation_of_user

        Get temporary token generation of a user  # noqa: E501
        """
        pass

    def test_list_all_named_tokens(self):
        """Test case for list_all_named_tokens

        List all named tokens  # noqa: E501
        """
        pass

    def test_list_named_tokens_of_current_provider(self):
        """Test case for list_named_tokens_of_current_provider

        List named tokens of current provider  # noqa: E501
        """
        pass

    def test_list_named_tokens_of_current_user(self):
        """Test case for list_named_tokens_of_current_user

        List named tokens of current user  # noqa: E501
        """
        pass

    def test_list_named_tokens_of_provider(self):
        """Test case for list_named_tokens_of_provider

        List named tokens of a provider  # noqa: E501
        """
        pass

    def test_list_named_tokens_of_user(self):
        """Test case for list_named_tokens_of_user

        List named tokens of a user  # noqa: E501
        """
        pass

    def test_modify_named_token(self):
        """Test case for modify_named_token

        Modify named token  # noqa: E501
        """
        pass

    def test_revoke_all_temporary_tokens_of_current_provider(self):
        """Test case for revoke_all_temporary_tokens_of_current_provider

        Revoke all temporary tokens of current provider  # noqa: E501
        """
        pass

    def test_revoke_all_temporary_tokens_of_current_user(self):
        """Test case for revoke_all_temporary_tokens_of_current_user

        Revoke all temporary tokens of current user  # noqa: E501
        """
        pass

    def test_revoke_all_temporary_tokens_of_provider(self):
        """Test case for revoke_all_temporary_tokens_of_provider

        Revoke all temporary tokens of a provider  # noqa: E501
        """
        pass

    def test_revoke_all_temporary_tokens_of_user(self):
        """Test case for revoke_all_temporary_tokens_of_user

        Revoke all temporary tokens of a user  # noqa: E501
        """
        pass

    def test_verify_access_token(self):
        """Test case for verify_access_token

        Verify an access token  # noqa: E501
        """
        pass

    def test_verify_identity_token(self):
        """Test case for verify_identity_token

        Verify an identity token  # noqa: E501
        """
        pass

    def test_verify_invite_token(self):
        """Test case for verify_invite_token

        Verify an invite token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
