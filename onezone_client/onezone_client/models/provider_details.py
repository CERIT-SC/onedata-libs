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

class ProviderDetails(object):
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
        'provider_id': 'str',
        'name': 'str',
        'domain': 'str',
        'latitude': 'float',
        'longitude': 'float',
        'cluster_id': 'str',
        'online': 'bool',
        'creation_time': 'Timestamp'
    }

    attribute_map = {
        'provider_id': 'providerId',
        'name': 'name',
        'domain': 'domain',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'cluster_id': 'clusterId',
        'online': 'online',
        'creation_time': 'creationTime'
    }

    def __init__(self, provider_id=None, name=None, domain=None, latitude=None, longitude=None, cluster_id=None, online=None, creation_time=None):  # noqa: E501
        """ProviderDetails - a model defined in Swagger"""  # noqa: E501
        self._provider_id = None
        self._name = None
        self._domain = None
        self._latitude = None
        self._longitude = None
        self._cluster_id = None
        self._online = None
        self._creation_time = None
        self.discriminator = None
        self.provider_id = provider_id
        self.name = name
        self.domain = domain
        self.latitude = latitude
        self.longitude = longitude
        self.cluster_id = cluster_id
        self.online = online
        self.creation_time = creation_time

    @property
    def provider_id(self):
        """Gets the provider_id of this ProviderDetails.  # noqa: E501

        The Oneprovider Id.  # noqa: E501

        :return: The provider_id of this ProviderDetails.  # noqa: E501
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this ProviderDetails.

        The Oneprovider Id.  # noqa: E501

        :param provider_id: The provider_id of this ProviderDetails.  # noqa: E501
        :type: str
        """
        if provider_id is None:
            raise ValueError("Invalid value for `provider_id`, must not be `None`")  # noqa: E501

        self._provider_id = provider_id

    @property
    def name(self):
        """Gets the name of this ProviderDetails.  # noqa: E501

        Oneprovider name.  # noqa: E501

        :return: The name of this ProviderDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProviderDetails.

        Oneprovider name.  # noqa: E501

        :param name: The name of this ProviderDetails.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def domain(self):
        """Gets the domain of this ProviderDetails.  # noqa: E501

        The fully qualified domain name of the Oneprovider or its IP address (only for single-node deployments or clusters with a reverse proxy).   # noqa: E501

        :return: The domain of this ProviderDetails.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ProviderDetails.

        The fully qualified domain name of the Oneprovider or its IP address (only for single-node deployments or clusters with a reverse proxy).   # noqa: E501

        :param domain: The domain of this ProviderDetails.  # noqa: E501
        :type: str
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def latitude(self):
        """Gets the latitude of this ProviderDetails.  # noqa: E501

        The geographical latitude of the Oneprovider's data center location.  # noqa: E501

        :return: The latitude of this ProviderDetails.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this ProviderDetails.

        The geographical latitude of the Oneprovider's data center location.  # noqa: E501

        :param latitude: The latitude of this ProviderDetails.  # noqa: E501
        :type: float
        """
        if latitude is None:
            raise ValueError("Invalid value for `latitude`, must not be `None`")  # noqa: E501

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this ProviderDetails.  # noqa: E501

        The geographical longitude of the Oneprovider's data center location.  # noqa: E501

        :return: The longitude of this ProviderDetails.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this ProviderDetails.

        The geographical longitude of the Oneprovider's data center location.  # noqa: E501

        :param longitude: The longitude of this ProviderDetails.  # noqa: E501
        :type: float
        """
        if longitude is None:
            raise ValueError("Invalid value for `longitude`, must not be `None`")  # noqa: E501

        self._longitude = longitude

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ProviderDetails.  # noqa: E501

        The Id of the corresponding Oneprovider cluster.  # noqa: E501

        :return: The cluster_id of this ProviderDetails.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ProviderDetails.

        The Id of the corresponding Oneprovider cluster.  # noqa: E501

        :param cluster_id: The cluster_id of this ProviderDetails.  # noqa: E501
        :type: str
        """
        if cluster_id is None:
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def online(self):
        """Gets the online of this ProviderDetails.  # noqa: E501

        True if this Oneprovider is online - connected to Onezone.  # noqa: E501

        :return: The online of this ProviderDetails.  # noqa: E501
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this ProviderDetails.

        True if this Oneprovider is online - connected to Onezone.  # noqa: E501

        :param online: The online of this ProviderDetails.  # noqa: E501
        :type: bool
        """
        if online is None:
            raise ValueError("Invalid value for `online`, must not be `None`")  # noqa: E501

        self._online = online

    @property
    def creation_time(self):
        """Gets the creation_time of this ProviderDetails.  # noqa: E501


        :return: The creation_time of this ProviderDetails.  # noqa: E501
        :rtype: Timestamp
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this ProviderDetails.


        :param creation_time: The creation_time of this ProviderDetails.  # noqa: E501
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
        if issubclass(ProviderDetails, dict):
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
        if not isinstance(other, ProviderDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
