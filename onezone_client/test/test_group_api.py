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
from onezone_client.api.group_api import GroupApi  # noqa: E501
from onezone_client.rest import ApiException


class TestGroupApi(unittest.TestCase):
    """GroupApi unit test stubs"""

    def setUp(self):
        self.api = GroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_child_group(self):
        """Test case for add_child_group

        Add child group  # noqa: E501
        """
        pass

    def test_add_group_handle_service(self):
        """Test case for add_group_handle_service

        Create a new handle service for given group.  # noqa: E501
        """
        pass

    def test_add_group_user(self):
        """Test case for add_group_user

        Add user to group  # noqa: E501
        """
        pass

    def test_create_child_group(self):
        """Test case for create_child_group

        Create child group  # noqa: E501
        """
        pass

    def test_create_child_group_token(self):
        """Test case for create_child_group_token

        Create child group invitation token  # noqa: E501
        """
        pass

    def test_create_group(self):
        """Test case for create_group

        Create new group  # noqa: E501
        """
        pass

    def test_create_group_handle(self):
        """Test case for create_group_handle

        Create a new handle for given group  # noqa: E501
        """
        pass

    def test_create_harvester_for_group(self):
        """Test case for create_harvester_for_group

        Create a new harvester for given group  # noqa: E501
        """
        pass

    def test_create_parent_group(self):
        """Test case for create_parent_group

        Create a new parent group for given group  # noqa: E501
        """
        pass

    def test_create_space_for_group(self):
        """Test case for create_space_for_group

        Create a new space for given group  # noqa: E501
        """
        pass

    def test_create_user_group_invite_token(self):
        """Test case for create_user_group_invite_token

        Create user invite token for group  # noqa: E501
        """
        pass

    def test_get_child_group(self):
        """Test case for get_child_group

        Get child group details  # noqa: E501
        """
        pass

    def test_get_effective_child_group(self):
        """Test case for get_effective_child_group

        Get effective child group details  # noqa: E501
        """
        pass

    def test_get_effective_child_group_membership_intermediaries(self):
        """Test case for get_effective_child_group_membership_intermediaries

        Get effective child's group membership intermediaries  # noqa: E501
        """
        pass

    def test_get_effective_children_groups(self):
        """Test case for get_effective_children_groups

        Get effective child groups  # noqa: E501
        """
        pass

    def test_get_effective_group_handle(self):
        """Test case for get_effective_group_handle

        Get effective group handle details  # noqa: E501
        """
        pass

    def test_get_effective_group_harvester(self):
        """Test case for get_effective_group_harvester

        Get effective group harvester details  # noqa: E501
        """
        pass

    def test_get_effective_group_space(self):
        """Test case for get_effective_group_space

        Get effective group space details  # noqa: E501
        """
        pass

    def test_get_effective_group_user(self):
        """Test case for get_effective_group_user

        Get effective group user details  # noqa: E501
        """
        pass

    def test_get_effective_parent_group(self):
        """Test case for get_effective_parent_group

        Get effective parent group details  # noqa: E501
        """
        pass

    def test_get_effective_user_group_membership_intermediaries(self):
        """Test case for get_effective_user_group_membership_intermediaries

        Get effective user's group membership intermediaries  # noqa: E501
        """
        pass

    def test_get_group(self):
        """Test case for get_group

        Get group details  # noqa: E501
        """
        pass

    def test_get_group_cluster(self):
        """Test case for get_group_cluster

        Get group's cluster details  # noqa: E501
        """
        pass

    def test_get_group_effective_cluster(self):
        """Test case for get_group_effective_cluster

        Get group's effective cluster details  # noqa: E501
        """
        pass

    def test_get_group_effective_handle_service(self):
        """Test case for get_group_effective_handle_service

        Get effective group handle service details  # noqa: E501
        """
        pass

    def test_get_group_effective_provider(self):
        """Test case for get_group_effective_provider

        Get group's effective provider details  # noqa: E501
        """
        pass

    def test_get_group_handle(self):
        """Test case for get_group_handle

        Get group handle details  # noqa: E501
        """
        pass

    def test_get_group_handle_service(self):
        """Test case for get_group_handle_service

        Get group handle service details  # noqa: E501
        """
        pass

    def test_get_group_harvester(self):
        """Test case for get_group_harvester

        Get group's harvester details  # noqa: E501
        """
        pass

    def test_get_group_space(self):
        """Test case for get_group_space

        Get group's space details  # noqa: E501
        """
        pass

    def test_get_group_spaces_in_effective_provider(self):
        """Test case for get_group_spaces_in_effective_provider

        Get group's spaces that are supported by given effective provider  # noqa: E501
        """
        pass

    def test_get_group_user(self):
        """Test case for get_group_user

        Get group user details  # noqa: E501
        """
        pass

    def test_get_parent_group(self):
        """Test case for get_parent_group

        Get parent group details  # noqa: E501
        """
        pass

    def test_group_join_cluster(self):
        """Test case for group_join_cluster

        Join group to a cluster  # noqa: E501
        """
        pass

    def test_group_join_harvester(self):
        """Test case for group_join_harvester

        Join harvester by group  # noqa: E501
        """
        pass

    def test_group_join_space(self):
        """Test case for group_join_space

        Join space by group  # noqa: E501
        """
        pass

    def test_group_leave_cluster(self):
        """Test case for group_leave_cluster

        Leave cluster  # noqa: E501
        """
        pass

    def test_group_leave_handle(self):
        """Test case for group_leave_handle

        Group leave handle  # noqa: E501
        """
        pass

    def test_group_leave_handle_service(self):
        """Test case for group_leave_handle_service

        Group leave handle service  # noqa: E501
        """
        pass

    def test_join_parent_group(self):
        """Test case for join_parent_group

        Join parent group  # noqa: E501
        """
        pass

    def test_leave_parent_group(self):
        """Test case for leave_parent_group

        Leave parent group  # noqa: E501
        """
        pass

    def test_list_child_group_privileges(self):
        """Test case for list_child_group_privileges

        List child's group privileges  # noqa: E501
        """
        pass

    def test_list_child_groups(self):
        """Test case for list_child_groups

        Get child groups  # noqa: E501
        """
        pass

    def test_list_effective_child_group_privileges(self):
        """Test case for list_effective_child_group_privileges

        List effective child's group privileges  # noqa: E501
        """
        pass

    def test_list_effective_group_handle_services(self):
        """Test case for list_effective_group_handle_services

        List effective group handle services  # noqa: E501
        """
        pass

    def test_list_effective_group_handles(self):
        """Test case for list_effective_group_handles

        List effective group handles  # noqa: E501
        """
        pass

    def test_list_effective_group_harvesters(self):
        """Test case for list_effective_group_harvesters

        List effective group's harvesters  # noqa: E501
        """
        pass

    def test_list_effective_group_providers(self):
        """Test case for list_effective_group_providers

        List effective group's providers  # noqa: E501
        """
        pass

    def test_list_effective_group_spaces(self):
        """Test case for list_effective_group_spaces

        List effective group's spaces  # noqa: E501
        """
        pass

    def test_list_effective_group_users(self):
        """Test case for list_effective_group_users

        List effective group users  # noqa: E501
        """
        pass

    def test_list_effective_parent_groups(self):
        """Test case for list_effective_parent_groups

        List effective parent groups  # noqa: E501
        """
        pass

    def test_list_effective_user_group_privileges(self):
        """Test case for list_effective_user_group_privileges

        List effective user's group privileges  # noqa: E501
        """
        pass

    def test_list_group_admin_privileges(self):
        """Test case for list_group_admin_privileges

        List group's admin privileges  # noqa: E501
        """
        pass

    def test_list_group_clusters(self):
        """Test case for list_group_clusters

        List group's clusters  # noqa: E501
        """
        pass

    def test_list_group_effective_admin_privileges(self):
        """Test case for list_group_effective_admin_privileges

        List group's effective admin privileges  # noqa: E501
        """
        pass

    def test_list_group_effective_clusters(self):
        """Test case for list_group_effective_clusters

        List group's effective clusters  # noqa: E501
        """
        pass

    def test_list_group_handle_services(self):
        """Test case for list_group_handle_services

        List group handle services  # noqa: E501
        """
        pass

    def test_list_group_handles(self):
        """Test case for list_group_handles

        List group handles  # noqa: E501
        """
        pass

    def test_list_group_harvesters(self):
        """Test case for list_group_harvesters

        List group's harvesters  # noqa: E501
        """
        pass

    def test_list_group_privileges(self):
        """Test case for list_group_privileges

        List all group privileges  # noqa: E501
        """
        pass

    def test_list_group_spaces(self):
        """Test case for list_group_spaces

        List group's spaces  # noqa: E501
        """
        pass

    def test_list_group_users(self):
        """Test case for list_group_users

        List group users  # noqa: E501
        """
        pass

    def test_list_groups(self):
        """Test case for list_groups

        List all groups  # noqa: E501
        """
        pass

    def test_list_parent_groups(self):
        """Test case for list_parent_groups

        List parent groups  # noqa: E501
        """
        pass

    def test_list_user_group_privileges(self):
        """Test case for list_user_group_privileges

        List user's group privileges  # noqa: E501
        """
        pass

    def test_modify_group(self):
        """Test case for modify_group

        Modify group details  # noqa: E501
        """
        pass

    def test_remove_child_group(self):
        """Test case for remove_child_group

        Remove child group  # noqa: E501
        """
        pass

    def test_remove_group(self):
        """Test case for remove_group

        Remove group  # noqa: E501
        """
        pass

    def test_remove_group_admin_privileges(self):
        """Test case for remove_group_admin_privileges

        Remove group's admin privileges  # noqa: E501
        """
        pass

    def test_remove_group_from_harvester(self):
        """Test case for remove_group_from_harvester

        Remove group from harvester  # noqa: E501
        """
        pass

    def test_remove_group_from_space(self):
        """Test case for remove_group_from_space

        Remove group from space  # noqa: E501
        """
        pass

    def test_remove_group_user(self):
        """Test case for remove_group_user

        Remove user from group  # noqa: E501
        """
        pass

    def test_update_child_group_privileges(self):
        """Test case for update_child_group_privileges

        Update child's group privileges  # noqa: E501
        """
        pass

    def test_update_group_admin_privileges(self):
        """Test case for update_group_admin_privileges

        Update group's admin privileges  # noqa: E501
        """
        pass

    def test_update_user_group_privileges(self):
        """Test case for update_user_group_privileges

        Update user's group privileges  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
