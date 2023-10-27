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

class ProviderRegistrationRequest(object):
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
        'token': 'str',
        'name': 'str',
        'admin_email': 'str',
        'subdomain_delegation': 'bool',
        'subdomain': 'str',
        'ip_list': 'list[str]',
        'domain': 'str',
        'latitude': 'float',
        'longitude': 'float'
    }

    attribute_map = {
        'token': 'token',
        'name': 'name',
        'admin_email': 'adminEmail',
        'subdomain_delegation': 'subdomainDelegation',
        'subdomain': 'subdomain',
        'ip_list': 'ipList',
        'domain': 'domain',
        'latitude': 'latitude',
        'longitude': 'longitude'
    }

    def __init__(self, token=None, name=None, admin_email=None, subdomain_delegation=None, subdomain=None, ip_list=None, domain=None, latitude=None, longitude=None):  # noqa: E501
        """ProviderRegistrationRequest - a model defined in Swagger"""  # noqa: E501
        self._token = None
        self._name = None
        self._admin_email = None
        self._subdomain_delegation = None
        self._subdomain = None
        self._ip_list = None
        self._domain = None
        self._latitude = None
        self._longitude = None
        self.discriminator = None
        self.token = token
        self.name = name
        self.admin_email = admin_email
        self.subdomain_delegation = subdomain_delegation
        if subdomain is not None:
            self.subdomain = subdomain
        if ip_list is not None:
            self.ip_list = ip_list
        if domain is not None:
            self.domain = domain
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude

    @property
    def token(self):
        """Gets the token of this ProviderRegistrationRequest.  # noqa: E501

        Token for registering a new Oneprovider. If Onezone allows regular users to freely register Oneproviders, it can be obtained from GUI or REST API. Otherwise, only a Onezone admin can issue such token.   # noqa: E501

        :return: The token of this ProviderRegistrationRequest.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this ProviderRegistrationRequest.

        Token for registering a new Oneprovider. If Onezone allows regular users to freely register Oneproviders, it can be obtained from GUI or REST API. Otherwise, only a Onezone admin can issue such token.   # noqa: E501

        :param token: The token of this ProviderRegistrationRequest.  # noqa: E501
        :type: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def name(self):
        """Gets the name of this ProviderRegistrationRequest.  # noqa: E501

        Oneprovider name.  # noqa: E501

        :return: The name of this ProviderRegistrationRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProviderRegistrationRequest.

        Oneprovider name.  # noqa: E501

        :param name: The name of this ProviderRegistrationRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def admin_email(self):
        """Gets the admin_email of this ProviderRegistrationRequest.  # noqa: E501

        Contact email address of the Oneprovider admin.  # noqa: E501

        :return: The admin_email of this ProviderRegistrationRequest.  # noqa: E501
        :rtype: str
        """
        return self._admin_email

    @admin_email.setter
    def admin_email(self, admin_email):
        """Sets the admin_email of this ProviderRegistrationRequest.

        Contact email address of the Oneprovider admin.  # noqa: E501

        :param admin_email: The admin_email of this ProviderRegistrationRequest.  # noqa: E501
        :type: str
        """
        if admin_email is None:
            raise ValueError("Invalid value for `admin_email`, must not be `None`")  # noqa: E501

        self._admin_email = admin_email

    @property
    def subdomain_delegation(self):
        """Gets the subdomain_delegation of this ProviderRegistrationRequest.  # noqa: E501

        If enabled, the Oneprovider will be assigned a subdomain in Onezone's domain and 'subdomain', 'ipList' properties must be provided. If disabled, 'domain' property must be provided.   # noqa: E501

        :return: The subdomain_delegation of this ProviderRegistrationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._subdomain_delegation

    @subdomain_delegation.setter
    def subdomain_delegation(self, subdomain_delegation):
        """Sets the subdomain_delegation of this ProviderRegistrationRequest.

        If enabled, the Oneprovider will be assigned a subdomain in Onezone's domain and 'subdomain', 'ipList' properties must be provided. If disabled, 'domain' property must be provided.   # noqa: E501

        :param subdomain_delegation: The subdomain_delegation of this ProviderRegistrationRequest.  # noqa: E501
        :type: bool
        """
        if subdomain_delegation is None:
            raise ValueError("Invalid value for `subdomain_delegation`, must not be `None`")  # noqa: E501

        self._subdomain_delegation = subdomain_delegation

    @property
    def subdomain(self):
        """Gets the subdomain of this ProviderRegistrationRequest.  # noqa: E501

        Unique subdomain in onezone's domain for the Oneprovider. Required if subdomain delegation is enabled.   # noqa: E501

        :return: The subdomain of this ProviderRegistrationRequest.  # noqa: E501
        :rtype: str
        """
        return self._subdomain

    @subdomain.setter
    def subdomain(self, subdomain):
        """Sets the subdomain of this ProviderRegistrationRequest.

        Unique subdomain in onezone's domain for the Oneprovider. Required if subdomain delegation is enabled.   # noqa: E501

        :param subdomain: The subdomain of this ProviderRegistrationRequest.  # noqa: E501
        :type: str
        """

        self._subdomain = subdomain

    @property
    def ip_list(self):
        """Gets the ip_list of this ProviderRegistrationRequest.  # noqa: E501

        List of Oneprovider's IPv4 addresses to be advertised by Onezone's DNS. Required if subdomain delegation is enabled.   # noqa: E501

        :return: The ip_list of this ProviderRegistrationRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        """Sets the ip_list of this ProviderRegistrationRequest.

        List of Oneprovider's IPv4 addresses to be advertised by Onezone's DNS. Required if subdomain delegation is enabled.   # noqa: E501

        :param ip_list: The ip_list of this ProviderRegistrationRequest.  # noqa: E501
        :type: list[str]
        """

        self._ip_list = ip_list

    @property
    def domain(self):
        """Gets the domain of this ProviderRegistrationRequest.  # noqa: E501

        The fully qualified domain name of the Oneprovider or its IP address (only for single-node deployments or clusters with a reverse proxy). Required if subdomain delegation is disabled.   # noqa: E501

        :return: The domain of this ProviderRegistrationRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ProviderRegistrationRequest.

        The fully qualified domain name of the Oneprovider or its IP address (only for single-node deployments or clusters with a reverse proxy). Required if subdomain delegation is disabled.   # noqa: E501

        :param domain: The domain of this ProviderRegistrationRequest.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def latitude(self):
        """Gets the latitude of this ProviderRegistrationRequest.  # noqa: E501

        The geographical latitude of the Oneprovider's data center location.  # noqa: E501

        :return: The latitude of this ProviderRegistrationRequest.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this ProviderRegistrationRequest.

        The geographical latitude of the Oneprovider's data center location.  # noqa: E501

        :param latitude: The latitude of this ProviderRegistrationRequest.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this ProviderRegistrationRequest.  # noqa: E501

        The geographical longitude of the Oneprovider's data center location.  # noqa: E501

        :return: The longitude of this ProviderRegistrationRequest.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this ProviderRegistrationRequest.

        The geographical longitude of the Oneprovider's data center location.  # noqa: E501

        :param longitude: The longitude of this ProviderRegistrationRequest.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

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
        if issubclass(ProviderRegistrationRequest, dict):
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
        if not isinstance(other, ProviderRegistrationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
