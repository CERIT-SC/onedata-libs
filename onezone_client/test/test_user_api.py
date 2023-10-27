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
from onezone_client.api.user_api import UserApi  # noqa: E501
from onezone_client.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_acquire_idp_access_token(self):
        """Test case for acquire_idp_access_token

        Acquire IdP access token  # noqa: E501
        """
        pass

    def test_add_user_handle_service(self):
        """Test case for add_user_handle_service

        Create a new handle service for the current user  # noqa: E501
        """
        pass

    def test_change_user_basic_auth_settings(self):
        """Test case for change_user_basic_auth_settings

        Change user's basic auth settings  # noqa: E501
        """
        pass

    def test_change_user_password(self):
        """Test case for change_user_password

        Change user's password  # noqa: E501
        """
        pass

    def test_create_client_token(self):
        """Test case for create_client_token

        Generate user access token  # noqa: E501
        """
        pass

    def test_create_provider_registration_token_for_current_user(self):
        """Test case for create_provider_registration_token_for_current_user

        Create provider registration token for current user  # noqa: E501
        """
        pass

    def test_create_provider_registration_token_for_user(self):
        """Test case for create_provider_registration_token_for_user

        Create provider registration token for a user  # noqa: E501
        """
        pass

    def test_create_user(self):
        """Test case for create_user

        Create new user  # noqa: E501
        """
        pass

    def test_create_user_group(self):
        """Test case for create_user_group

        Create a new group for the current user  # noqa: E501
        """
        pass

    def test_create_user_handle(self):
        """Test case for create_user_handle

        Create a new handle for the current user  # noqa: E501
        """
        pass

    def test_create_user_harvester(self):
        """Test case for create_user_harvester

        Create a new harvester for the current user  # noqa: E501
        """
        pass

    def test_create_user_space(self):
        """Test case for create_user_space

        Create a new space for the current user  # noqa: E501
        """
        pass

    def test_get_current_user(self):
        """Test case for get_current_user

        Get current user details  # noqa: E501
        """
        pass

    def test_get_effective_user_harvester(self):
        """Test case for get_effective_user_harvester

        Get effective harvester details  # noqa: E501
        """
        pass

    def test_get_effective_user_space(self):
        """Test case for get_effective_user_space

        Get effective space details  # noqa: E501
        """
        pass

    def test_get_space_membership_requests(self):
        """Test case for get_space_membership_requests

        Get summary of space membership requests  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get user details  # noqa: E501
        """
        pass

    def test_get_user_cluster(self):
        """Test case for get_user_cluster

        Get user's cluster details  # noqa: E501
        """
        pass

    def test_get_user_effective_cluster(self):
        """Test case for get_user_effective_cluster

        Get user's effective cluster details  # noqa: E501
        """
        pass

    def test_get_user_effective_group(self):
        """Test case for get_user_effective_group

        Get effective group details  # noqa: E501
        """
        pass

    def test_get_user_effective_handle(self):
        """Test case for get_user_effective_handle

        Get effective handle details  # noqa: E501
        """
        pass

    def test_get_user_effective_handle_service(self):
        """Test case for get_user_effective_handle_service

        Get effective handle service details  # noqa: E501
        """
        pass

    def test_get_user_effective_provider(self):
        """Test case for get_user_effective_provider

        Get user's effective provider details  # noqa: E501
        """
        pass

    def test_get_user_group(self):
        """Test case for get_user_group

        Get group details  # noqa: E501
        """
        pass

    def test_get_user_handle(self):
        """Test case for get_user_handle

        Get handle details  # noqa: E501
        """
        pass

    def test_get_user_handle_service(self):
        """Test case for get_user_handle_service

        Get user handle service details  # noqa: E501
        """
        pass

    def test_get_user_harvester(self):
        """Test case for get_user_harvester

        Get harvester details  # noqa: E501
        """
        pass

    def test_get_user_space(self):
        """Test case for get_user_space

        Get space details  # noqa: E501
        """
        pass

    def test_get_user_space_alias(self):
        """Test case for get_user_space_alias

        Get user space alias  # noqa: E501
        """
        pass

    def test_get_user_spaces_in_effective_provider(self):
        """Test case for get_user_spaces_in_effective_provider

        Get user's spaces that are supported by given effective provider  # noqa: E501
        """
        pass

    def test_join_group(self):
        """Test case for join_group

        Join group  # noqa: E501
        """
        pass

    def test_join_harvester(self):
        """Test case for join_harvester

        Join harvester  # noqa: E501
        """
        pass

    def test_join_space(self):
        """Test case for join_space

        Join space  # noqa: E501
        """
        pass

    def test_leave_group(self):
        """Test case for leave_group

        Leave group  # noqa: E501
        """
        pass

    def test_leave_handle_service(self):
        """Test case for leave_handle_service

        Leave handle service  # noqa: E501
        """
        pass

    def test_leave_space(self):
        """Test case for leave_space

        Leave space  # noqa: E501
        """
        pass

    def test_list_client_tokens(self):
        """Test case for list_client_tokens

        List user access tokens  # noqa: E501
        """
        pass

    def test_list_current_user_admin_privileges(self):
        """Test case for list_current_user_admin_privileges

        List current user privileges  # noqa: E501
        """
        pass

    def test_list_current_user_effective_admin_privileges(self):
        """Test case for list_current_user_effective_admin_privileges

        List current user effective privileges  # noqa: E501
        """
        pass

    def test_list_effective_user_groups(self):
        """Test case for list_effective_user_groups

        List effective user groups  # noqa: E501
        """
        pass

    def test_list_effective_user_harvesters(self):
        """Test case for list_effective_user_harvesters

        List effective user harvesters  # noqa: E501
        """
        pass

    def test_list_effective_user_providers(self):
        """Test case for list_effective_user_providers

        List user effective providers  # noqa: E501
        """
        pass

    def test_list_effective_user_spaces(self):
        """Test case for list_effective_user_spaces

        List effective user spaces  # noqa: E501
        """
        pass

    def test_list_user_admin_privileges(self):
        """Test case for list_user_admin_privileges

        List user admin privileges  # noqa: E501
        """
        pass

    def test_list_user_clusters(self):
        """Test case for list_user_clusters

        List user's clusters  # noqa: E501
        """
        pass

    def test_list_user_effective_admin_privileges(self):
        """Test case for list_user_effective_admin_privileges

        List user's effective admin privileges  # noqa: E501
        """
        pass

    def test_list_user_effective_clusters(self):
        """Test case for list_user_effective_clusters

        List user's effective clusters  # noqa: E501
        """
        pass

    def test_list_user_effective_handle_services(self):
        """Test case for list_user_effective_handle_services

        List user effective handle services  # noqa: E501
        """
        pass

    def test_list_user_effective_handles(self):
        """Test case for list_user_effective_handles

        Get user effective handles  # noqa: E501
        """
        pass

    def test_list_user_groups(self):
        """Test case for list_user_groups

        List user groups  # noqa: E501
        """
        pass

    def test_list_user_handle_services(self):
        """Test case for list_user_handle_services

        List user handle services  # noqa: E501
        """
        pass

    def test_list_user_handles(self):
        """Test case for list_user_handles

        List user handles  # noqa: E501
        """
        pass

    def test_list_user_harvesters(self):
        """Test case for list_user_harvesters

        List user harvesters  # noqa: E501
        """
        pass

    def test_list_user_spaces(self):
        """Test case for list_user_spaces

        List user spaces  # noqa: E501
        """
        pass

    def test_modify_current_user(self):
        """Test case for modify_current_user

        Modify current user  # noqa: E501
        """
        pass

    def test_oz_users_list(self):
        """Test case for oz_users_list

        List all users  # noqa: E501
        """
        pass

    def test_remove_client_token(self):
        """Test case for remove_client_token

        Delete access token  # noqa: E501
        """
        pass

    def test_remove_current_user(self):
        """Test case for remove_current_user

        Remove current user  # noqa: E501
        """
        pass

    def test_remove_current_user_admin_privileges(self):
        """Test case for remove_current_user_admin_privileges

        Remove current user's admin privileges  # noqa: E501
        """
        pass

    def test_remove_user(self):
        """Test case for remove_user

        Remove user  # noqa: E501
        """
        pass

    def test_remove_user_admin_privileges(self):
        """Test case for remove_user_admin_privileges

        Remove user's admin privileges  # noqa: E501
        """
        pass

    def test_remove_user_handle(self):
        """Test case for remove_user_handle

        Leave handle  # noqa: E501
        """
        pass

    def test_remove_user_space_alias(self):
        """Test case for remove_user_space_alias

        Remove space alias  # noqa: E501
        """
        pass

    def test_set_user_space_alias(self):
        """Test case for set_user_space_alias

        Set user space alias  # noqa: E501
        """
        pass

    def test_toggle_user_access_block(self):
        """Test case for toggle_user_access_block

        Block or unblock user access  # noqa: E501
        """
        pass

    def test_update_current_user_admin_privileges(self):
        """Test case for update_current_user_admin_privileges

        Update current user's admin privileges  # noqa: E501
        """
        pass

    def test_update_user_admin_privileges(self):
        """Test case for update_user_admin_privileges

        Update user's admin privileges  # noqa: E501
        """
        pass

    def test_user_join_cluster(self):
        """Test case for user_join_cluster

        Join cluster  # noqa: E501
        """
        pass

    def test_user_leave_cluster(self):
        """Test case for user_leave_cluster

        Leave cluster  # noqa: E501
        """
        pass

    def test_user_leave_harvester(self):
        """Test case for user_leave_harvester

        Leave harvester  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
