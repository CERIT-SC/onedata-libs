# coding: utf-8

"""
    Onezone

    # Overview This is the RESTful API definition of Onezone component of Onedata data management system [onedata.org](http://onedata.org).  > This API is defined using [Swagger](http://swagger.io/), the JSON specification can be used to automatically generate client libraries - [swagger.json](../../../swagger/onezone/swagger.json).  This API allows control and configuration of local Onezone service deployment, in particular management of users, groups, spaces, shares, providers, handle services, handles and clusters.  ## Authentication and authorization To be able to use this API, the REST client must authenticate with the Onezone service and posses required authorization, which is determined based on client's privileges and relations in the system.  There are essentially three types of REST clients depending on the authentication:   * **users** - can authenticate using an access token or basic credentials   (only for users originating from Onezone's onepanel). Examples:   ```bash   curl -H \"x-auth-token: $TOKEN\" [...]   curl -H \"authorization: Bearer $TOKEN\" [...]   curl -u \"username:password\" [...]   curl -H \"macaroon: $TOKEN\" [...]   # DEPRECATED   ```   > `$TOKEN` can ba a Onedata access token, obtained via Onezone GUI or API, in the form   `MDAxNWxvY2F00aW9...`. If authority delegation for given IdP is enabled,   it is possible to provide an access token from the IdP, which must be prefixed   properly (depending on the configuration), e.g.: `github/GST5aasdA...`.    * **Oneproviders** - can authenticate using the provider root token,   which was assigned during registration in Onezone. It can be found in   `/etc/op_worker/provider_root_token.txt`. It is used just like a user   access token, for example:   ```bash   curl -H \"x-auth-token: $TOKEN\" [...]   curl -H \"authorization: Bearer $TOKEN\" [...]   curl -H \"macaroon: $TOKEN\" [...]   # DEPRECATED   ```   > Please mind that the provider root token is highly confidential and must   be kept secret (similarly to a private RSA key).    * **anonymous** - there is a small subset of operations that do not require     any authentication and are publicly available (look for information about     public availability in the endpoint descriptions).  The authorization of the client is determined based on existing relations and privileges in the system. In most cases, the rules below can be roughly applied:   * users and providers can access and modify their own data   * users can perform operations in groups, spaces, handle services, handles     and clusters depending on their privileges in subject entity - the required     privileges are listed in the description of each operation   * users can be given special admin privileges (fine-grained) that allow to     access and modify all entities in the system - see certain operations for     details.  Authentication and Authorization errors have the following meaning:   * HTTP 401 UNAUTHORIZED - the client could not be authenticated   * HTTP 403 FORBIDDEN - the client was authenticated, but is not permitted to     perform the action  ## Effective users and effective groups and spaces Onedata supports creation of arbitrary nested group and space membership tree structures. In order to determine if a given user belongs to the group directly or indirectly by belonging to a subgroup of a group, separate API calls are provided for getting information about group users (direct group members) and effective users (indirect group members).  ## API structure The API is divided into several categories, corresponding to entities in Onedata:  **Space management** The space management operations of this API provide means for accessing information about spaces and their management.  **Share management** The share management operations of this API provide means for accessing information about shares and their management.  **Group management** The group management operations allow creation of user groups, assigning their authorization rights, adding and removing users from groups.  **User management** The user management methods allow creation of users, managing their authorization credentials as well as space and group membership.  **Provider management** Provider specific calls allow getting global information about the spaces managed by the provider, and some administrative operations which can be used for monitoring or accounting.  **Handle service management** The handle service management operations of this API provide means for accessing information about handle services and their management.  **Handle API** Onezone provides extensive support for integration with Handle system registration services, including support for DOI and PID identifier assignment services. The API provides methods for adding new Handle services to the system, managing which users can use which registration services and complete API for registering identifiers to users' data sets which are made public.  **Cluster management** Operations for managing Onezone / Oneprovider clusters and their members - users and groups that can access the Onepanel interfaces (REST or GUI) of a cluster.   ## Using the API Onezone API is quite complex and thus it might be difficult to quickly figure out how to perform specific action, however the following guidelines might be useful:   * Operations performed by a regular users on their resources are grouped under     `/user` path (**USER** group in the menu)   * Operations performed by administrators of specific resources (e.g. groups,     spaces, shares) start with specific resource (e.g. `/groups`)   * By default the operations which list resource membership     (e.g. `/spaces/SPACE_ID/groups/`) will list explicit resource membership.     To get list of effective resource membership (i.e. including indirect     membership), special paths are provided     (e.g. `/spaces/SPACE_ID/effective_groups/`)  Furthermore, we have prepared a command-line client environment based on Docker which gives easy access to each of Onedata services via command-line clients, with pre-configured shell with full help on the APIs and autocomplete for operations and attributes.  ``` docker run -it onedata/rest-cli:21.02.3 ```  Below you can find some tutorials which show how to use this API in practice:   * [User oriented tutorial](https://onedata.org/#/home/documentation/doc/using_onedata/using_onedata_from_cli.html)   * [Administrator oriented tutorial](https://onedata.org/#/home/documentation/doc/administering_onedata/administering_onedata_from_cli.html)   ## Examples  **Generate new authentication token** ```bash curl -u user:password -X POST -H 'Content-type: application/json' -d '{}' \\ https://$ONEZONE_HOST/api/v3/onezone/user/client_tokens ```  **Get user details** ```bash curl -H 'X-Auth-Token: $TOKEN' -X GET \\ https://$ONEZONE_HOST/api/v3/onezone/user ```  **Get user details using an access token from github** ```bash curl -H 'X-Auth-Token: github/ijaAVWq3j9234jA9gPoR9agFja89t9UiPf8tiueSdx' -X GET \\ https://$ONEZONE_HOST/api/v3/onezone/user ``` > Note that GitHub IdP must be properly configured for the example to work: > * authority delegation must be enabled > * tokenPrefix must be set to \"github/\" > > You can learn more in > [the documentation](https://onedata.org/#/home/documentation/doc/administering_onedata/openid_saml_configuration/openid_saml_configuration_19_02[authority-delegation].html).   # noqa: E501

    OpenAPI spec version: 21.02.3
    Contact: info@onedata.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserProtectedInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'user_id': 'str',
        'full_name': 'str',
        'username': 'str',
        'linked_accounts': 'list[LinkedAccount]',
        'emails': 'list[str]',
        'basic_auth_enabled': 'bool',
        'blocked': 'bool',
        'creation_time': 'Timestamp'
    }

    attribute_map = {
        'user_id': 'userId',
        'full_name': 'fullName',
        'username': 'username',
        'linked_accounts': 'linkedAccounts',
        'emails': 'emails',
        'basic_auth_enabled': 'basicAuthEnabled',
        'blocked': 'blocked',
        'creation_time': 'creationTime'
    }

    def __init__(self, user_id=None, full_name=None, username=None, linked_accounts=None, emails=None, basic_auth_enabled=None, blocked=None, creation_time=None):  # noqa: E501
        """UserProtectedInfo - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._full_name = None
        self._username = None
        self._linked_accounts = None
        self._emails = None
        self._basic_auth_enabled = None
        self._blocked = None
        self._creation_time = None
        self.discriminator = None
        self.user_id = user_id
        self.full_name = full_name
        self.username = username
        self.linked_accounts = linked_accounts
        self.emails = emails
        self.basic_auth_enabled = basic_auth_enabled
        self.blocked = blocked
        self.creation_time = creation_time

    @property
    def user_id(self):
        """Gets the user_id of this UserProtectedInfo.  # noqa: E501

        Unique user Id.  # noqa: E501

        :return: The user_id of this UserProtectedInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserProtectedInfo.

        Unique user Id.  # noqa: E501

        :param user_id: The user_id of this UserProtectedInfo.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def full_name(self):
        """Gets the full_name of this UserProtectedInfo.  # noqa: E501

        User's full name (given names + surname).  # noqa: E501

        :return: The full_name of this UserProtectedInfo.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this UserProtectedInfo.

        User's full name (given names + surname).  # noqa: E501

        :param full_name: The full_name of this UserProtectedInfo.  # noqa: E501
        :type: str
        """
        if full_name is None:
            raise ValueError("Invalid value for `full_name`, must not be `None`")  # noqa: E501

        self._full_name = full_name

    @property
    def username(self):
        """Gets the username of this UserProtectedInfo.  # noqa: E501

        User's human-readable identifier, unique across the system. Makes it easier to identify the user and can be used for signing in with password.   # noqa: E501

        :return: The username of this UserProtectedInfo.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserProtectedInfo.

        User's human-readable identifier, unique across the system. Makes it easier to identify the user and can be used for signing in with password.   # noqa: E501

        :param username: The username of this UserProtectedInfo.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def linked_accounts(self):
        """Gets the linked_accounts of this UserProtectedInfo.  # noqa: E501

        The list of accounts linked to this user.  # noqa: E501

        :return: The linked_accounts of this UserProtectedInfo.  # noqa: E501
        :rtype: list[LinkedAccount]
        """
        return self._linked_accounts

    @linked_accounts.setter
    def linked_accounts(self, linked_accounts):
        """Sets the linked_accounts of this UserProtectedInfo.

        The list of accounts linked to this user.  # noqa: E501

        :param linked_accounts: The linked_accounts of this UserProtectedInfo.  # noqa: E501
        :type: list[LinkedAccount]
        """
        if linked_accounts is None:
            raise ValueError("Invalid value for `linked_accounts`, must not be `None`")  # noqa: E501

        self._linked_accounts = linked_accounts

    @property
    def emails(self):
        """Gets the emails of this UserProtectedInfo.  # noqa: E501


        :return: The emails of this UserProtectedInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this UserProtectedInfo.


        :param emails: The emails of this UserProtectedInfo.  # noqa: E501
        :type: list[str]
        """
        if emails is None:
            raise ValueError("Invalid value for `emails`, must not be `None`")  # noqa: E501

        self._emails = emails

    @property
    def basic_auth_enabled(self):
        """Gets the basic_auth_enabled of this UserProtectedInfo.  # noqa: E501

        Denotes if this user is allowed to authenticate with username & password.  # noqa: E501

        :return: The basic_auth_enabled of this UserProtectedInfo.  # noqa: E501
        :rtype: bool
        """
        return self._basic_auth_enabled

    @basic_auth_enabled.setter
    def basic_auth_enabled(self, basic_auth_enabled):
        """Sets the basic_auth_enabled of this UserProtectedInfo.

        Denotes if this user is allowed to authenticate with username & password.  # noqa: E501

        :param basic_auth_enabled: The basic_auth_enabled of this UserProtectedInfo.  # noqa: E501
        :type: bool
        """
        if basic_auth_enabled is None:
            raise ValueError("Invalid value for `basic_auth_enabled`, must not be `None`")  # noqa: E501

        self._basic_auth_enabled = basic_auth_enabled

    @property
    def blocked(self):
        """Gets the blocked of this UserProtectedInfo.  # noqa: E501

        Denotes if this user's account has been blocked by the administrators.  # noqa: E501

        :return: The blocked of this UserProtectedInfo.  # noqa: E501
        :rtype: bool
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked):
        """Sets the blocked of this UserProtectedInfo.

        Denotes if this user's account has been blocked by the administrators.  # noqa: E501

        :param blocked: The blocked of this UserProtectedInfo.  # noqa: E501
        :type: bool
        """
        if blocked is None:
            raise ValueError("Invalid value for `blocked`, must not be `None`")  # noqa: E501

        self._blocked = blocked

    @property
    def creation_time(self):
        """Gets the creation_time of this UserProtectedInfo.  # noqa: E501


        :return: The creation_time of this UserProtectedInfo.  # noqa: E501
        :rtype: Timestamp
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this UserProtectedInfo.


        :param creation_time: The creation_time of this UserProtectedInfo.  # noqa: E501
        :type: Timestamp
        """
        if creation_time is None:
            raise ValueError("Invalid value for `creation_time`, must not be `None`")  # noqa: E501

        self._creation_time = creation_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UserProtectedInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserProtectedInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
