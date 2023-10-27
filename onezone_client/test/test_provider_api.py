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
from onezone_client.api.provider_api import ProviderApi  # noqa: E501
from onezone_client.rest import ApiException


class TestProviderApi(unittest.TestCase):
    """ProviderApi unit test stubs"""

    def setUp(self):
        self.api = ProviderApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_current_time(self):
        """Test case for check_current_time

        Show current clock time  # noqa: E501
        """
        pass

    def test_check_my_ip(self):
        """Test case for check_my_ip

        Show client IP address  # noqa: E501
        """
        pass

    def test_get_current_provider_details(self):
        """Test case for get_current_provider_details

        Get current provider details  # noqa: E501
        """
        pass

    def test_get_current_provider_domain_config(self):
        """Test case for get_current_provider_domain_config

        Get current provider's domain config  # noqa: E501
        """
        pass

    def test_get_effective_group_provider_membership_intermediaries(self):
        """Test case for get_effective_group_provider_membership_intermediaries

        Get effective group's provider membership intermediaries  # noqa: E501
        """
        pass

    def test_get_effective_provider_group(self):
        """Test case for get_effective_provider_group

        Get group of provider  # noqa: E501
        """
        pass

    def test_get_effective_provider_user(self):
        """Test case for get_effective_provider_user

        Get effective user of provider  # noqa: E501
        """
        pass

    def test_get_effective_user_provider_membership_intermediaries(self):
        """Test case for get_effective_user_provider_membership_intermediaries

        Get effective user's provider membership intermediaries  # noqa: E501
        """
        pass

    def test_get_provider_details(self):
        """Test case for get_provider_details

        Get provider details  # noqa: E501
        """
        pass

    def test_get_provider_domain_config(self):
        """Test case for get_provider_domain_config

        Get provider's domain config  # noqa: E501
        """
        pass

    def test_get_provider_space(self):
        """Test case for get_provider_space

        Get space supported by provider  # noqa: E501
        """
        pass

    def test_get_supported_space(self):
        """Test case for get_supported_space

        Get space details by provider  # noqa: E501
        """
        pass

    def test_list_current_provider_supported_spaces(self):
        """Test case for list_current_provider_supported_spaces

        List current provider's supported spaces  # noqa: E501
        """
        pass

    def test_list_effective_provider_groups(self):
        """Test case for list_effective_provider_groups

        List effective groups of provider  # noqa: E501
        """
        pass

    def test_list_effective_provider_users(self):
        """Test case for list_effective_provider_users

        List effective users of provider  # noqa: E501
        """
        pass

    def test_list_provider_supported_spaces(self):
        """Test case for list_provider_supported_spaces

        List provider's supported spaces  # noqa: E501
        """
        pass

    def test_map_idp_group(self):
        """Test case for map_idp_group

        Map IdP group to Onezone group  # noqa: E501
        """
        pass

    def test_map_idp_user(self):
        """Test case for map_idp_user

        Map IdP user to Onezone user  # noqa: E501
        """
        pass

    def test_modify_provider(self):
        """Test case for modify_provider

        Modify provider details  # noqa: E501
        """
        pass

    def test_modify_supported_space(self):
        """Test case for modify_supported_space

        Modify supported space  # noqa: E501
        """
        pass

    def test_oz_providers_list(self):
        """Test case for oz_providers_list

        List providers  # noqa: E501
        """
        pass

    def test_register_provider(self):
        """Test case for register_provider

        Register provider  # noqa: E501
        """
        pass

    def test_remove_provider(self):
        """Test case for remove_provider

        Remove provider  # noqa: E501
        """
        pass

    def test_remove_space_support(self):
        """Test case for remove_space_support

        Remove space support  # noqa: E501
        """
        pass

    def test_unregister_provider(self):
        """Test case for unregister_provider

        Unregister provider  # noqa: E501
        """
        pass

    def test_verify_provider_identity(self):
        """Test case for verify_provider_identity

        Verify the identity of given provider  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
