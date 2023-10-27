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

class VerifyInviteTokenRequest(object):
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
        'token': 'SerializedToken',
        'peer_ip': 'str',
        'consumer_token': 'SerializedToken',
        'expected_invite_type': 'str'
    }

    attribute_map = {
        'token': 'token',
        'peer_ip': 'peerIp',
        'consumer_token': 'consumerToken',
        'expected_invite_type': 'expectedInviteType'
    }

    def __init__(self, token=None, peer_ip=None, consumer_token=None, expected_invite_type=None):  # noqa: E501
        """VerifyInviteTokenRequest - a model defined in Swagger"""  # noqa: E501
        self._token = None
        self._peer_ip = None
        self._consumer_token = None
        self._expected_invite_type = None
        self.discriminator = None
        self.token = token
        if peer_ip is not None:
            self.peer_ip = peer_ip
        if consumer_token is not None:
            self.consumer_token = consumer_token
        if expected_invite_type is not None:
            self.expected_invite_type = expected_invite_type

    @property
    def token(self):
        """Gets the token of this VerifyInviteTokenRequest.  # noqa: E501


        :return: The token of this VerifyInviteTokenRequest.  # noqa: E501
        :rtype: SerializedToken
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this VerifyInviteTokenRequest.


        :param token: The token of this VerifyInviteTokenRequest.  # noqa: E501
        :type: SerializedToken
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def peer_ip(self):
        """Gets the peer_ip of this VerifyInviteTokenRequest.  # noqa: E501

        The IP address of the token bearer.  # noqa: E501

        :return: The peer_ip of this VerifyInviteTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._peer_ip

    @peer_ip.setter
    def peer_ip(self, peer_ip):
        """Sets the peer_ip of this VerifyInviteTokenRequest.

        The IP address of the token bearer.  # noqa: E501

        :param peer_ip: The peer_ip of this VerifyInviteTokenRequest.  # noqa: E501
        :type: str
        """

        self._peer_ip = peer_ip

    @property
    def consumer_token(self):
        """Gets the consumer_token of this VerifyInviteTokenRequest.  # noqa: E501


        :return: The consumer_token of this VerifyInviteTokenRequest.  # noqa: E501
        :rtype: SerializedToken
        """
        return self._consumer_token

    @consumer_token.setter
    def consumer_token(self, consumer_token):
        """Sets the consumer_token of this VerifyInviteTokenRequest.


        :param consumer_token: The consumer_token of this VerifyInviteTokenRequest.  # noqa: E501
        :type: SerializedToken
        """

        self._consumer_token = consumer_token

    @property
    def expected_invite_type(self):
        """Gets the expected_invite_type of this VerifyInviteTokenRequest.  # noqa: E501

        Expected type of the invite token - verification will not succeed if it does not match the actual invite token type.   # noqa: E501

        :return: The expected_invite_type of this VerifyInviteTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._expected_invite_type

    @expected_invite_type.setter
    def expected_invite_type(self, expected_invite_type):
        """Sets the expected_invite_type of this VerifyInviteTokenRequest.

        Expected type of the invite token - verification will not succeed if it does not match the actual invite token type.   # noqa: E501

        :param expected_invite_type: The expected_invite_type of this VerifyInviteTokenRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["userJoinGroup", "groupJoinGroup", "userJoinSpace", "groupJoinSpace", "supportSpace", "harvesterJoinSpace", "registerOneprovider", "userJoinCluster", "groupJoinCluster", "userJoinHarvester", "groupJoinHarvester", "spaceJoinHarvester"]  # noqa: E501
        if expected_invite_type not in allowed_values:
            raise ValueError(
                "Invalid value for `expected_invite_type` ({0}), must be one of {1}"  # noqa: E501
                .format(expected_invite_type, allowed_values)
            )

        self._expected_invite_type = expected_invite_type

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
        if issubclass(VerifyInviteTokenRequest, dict):
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
        if not isinstance(other, VerifyInviteTokenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
