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

class Configuration(object):
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
        'name': 'str',
        'domain': 'str',
        'version': 'str',
        'build': 'str',
        'subdomain_delegation_supported': 'bool',
        'compatible_oneprovider_versions': 'list[str]',
        'compatibility_registry_revision': 'int',
        'supported_id_ps': 'list[ConfigurationSupportedIdPs]',
        'available_space_tags': 'dict(str, list[str])'
    }

    attribute_map = {
        'name': 'name',
        'domain': 'domain',
        'version': 'version',
        'build': 'build',
        'subdomain_delegation_supported': 'subdomainDelegationSupported',
        'compatible_oneprovider_versions': 'compatibleOneproviderVersions',
        'compatibility_registry_revision': 'compatibilityRegistryRevision',
        'supported_id_ps': 'supportedIdPs',
        'available_space_tags': 'availableSpaceTags'
    }

    def __init__(self, name=None, domain=None, version=None, build=None, subdomain_delegation_supported=None, compatible_oneprovider_versions=None, compatibility_registry_revision=None, supported_id_ps=None, available_space_tags=None):  # noqa: E501
        """Configuration - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._domain = None
        self._version = None
        self._build = None
        self._subdomain_delegation_supported = None
        self._compatible_oneprovider_versions = None
        self._compatibility_registry_revision = None
        self._supported_id_ps = None
        self._available_space_tags = None
        self.discriminator = None
        self.name = name
        self.domain = domain
        self.version = version
        self.build = build
        self.subdomain_delegation_supported = subdomain_delegation_supported
        self.compatible_oneprovider_versions = compatible_oneprovider_versions
        self.compatibility_registry_revision = compatibility_registry_revision
        self.supported_id_ps = supported_id_ps
        self.available_space_tags = available_space_tags

    @property
    def name(self):
        """Gets the name of this Configuration.  # noqa: E501

        Onezone's name  # noqa: E501

        :return: The name of this Configuration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Configuration.

        Onezone's name  # noqa: E501

        :param name: The name of this Configuration.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def domain(self):
        """Gets the domain of this Configuration.  # noqa: E501

        Onezone's cluster domain  # noqa: E501

        :return: The domain of this Configuration.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Configuration.

        Onezone's cluster domain  # noqa: E501

        :param domain: The domain of this Configuration.  # noqa: E501
        :type: str
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def version(self):
        """Gets the version of this Configuration.  # noqa: E501

        Version of this Onezone service  # noqa: E501

        :return: The version of this Configuration.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Configuration.

        Version of this Onezone service  # noqa: E501

        :param version: The version of this Configuration.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def build(self):
        """Gets the build of this Configuration.  # noqa: E501

        Build number of this Onezone service  # noqa: E501

        :return: The build of this Configuration.  # noqa: E501
        :rtype: str
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this Configuration.

        Build number of this Onezone service  # noqa: E501

        :param build: The build of this Configuration.  # noqa: E501
        :type: str
        """
        if build is None:
            raise ValueError("Invalid value for `build`, must not be `None`")  # noqa: E501

        self._build = build

    @property
    def subdomain_delegation_supported(self):
        """Gets the subdomain_delegation_supported of this Configuration.  # noqa: E501

        If true, registering Oneproviders are allowed to request subdomains of the Onezone domain for use as their domains.  # noqa: E501

        :return: The subdomain_delegation_supported of this Configuration.  # noqa: E501
        :rtype: bool
        """
        return self._subdomain_delegation_supported

    @subdomain_delegation_supported.setter
    def subdomain_delegation_supported(self, subdomain_delegation_supported):
        """Sets the subdomain_delegation_supported of this Configuration.

        If true, registering Oneproviders are allowed to request subdomains of the Onezone domain for use as their domains.  # noqa: E501

        :param subdomain_delegation_supported: The subdomain_delegation_supported of this Configuration.  # noqa: E501
        :type: bool
        """
        if subdomain_delegation_supported is None:
            raise ValueError("Invalid value for `subdomain_delegation_supported`, must not be `None`")  # noqa: E501

        self._subdomain_delegation_supported = subdomain_delegation_supported

    @property
    def compatible_oneprovider_versions(self):
        """Gets the compatible_oneprovider_versions of this Configuration.  # noqa: E501

        List of compatible Oneprovider versions  # noqa: E501

        :return: The compatible_oneprovider_versions of this Configuration.  # noqa: E501
        :rtype: list[str]
        """
        return self._compatible_oneprovider_versions

    @compatible_oneprovider_versions.setter
    def compatible_oneprovider_versions(self, compatible_oneprovider_versions):
        """Sets the compatible_oneprovider_versions of this Configuration.

        List of compatible Oneprovider versions  # noqa: E501

        :param compatible_oneprovider_versions: The compatible_oneprovider_versions of this Configuration.  # noqa: E501
        :type: list[str]
        """
        if compatible_oneprovider_versions is None:
            raise ValueError("Invalid value for `compatible_oneprovider_versions`, must not be `None`")  # noqa: E501

        self._compatible_oneprovider_versions = compatible_oneprovider_versions

    @property
    def compatibility_registry_revision(self):
        """Gets the compatibility_registry_revision of this Configuration.  # noqa: E501

        Revision of the compatibility registry enforced by this Onezone service  # noqa: E501

        :return: The compatibility_registry_revision of this Configuration.  # noqa: E501
        :rtype: int
        """
        return self._compatibility_registry_revision

    @compatibility_registry_revision.setter
    def compatibility_registry_revision(self, compatibility_registry_revision):
        """Sets the compatibility_registry_revision of this Configuration.

        Revision of the compatibility registry enforced by this Onezone service  # noqa: E501

        :param compatibility_registry_revision: The compatibility_registry_revision of this Configuration.  # noqa: E501
        :type: int
        """
        if compatibility_registry_revision is None:
            raise ValueError("Invalid value for `compatibility_registry_revision`, must not be `None`")  # noqa: E501

        self._compatibility_registry_revision = compatibility_registry_revision

    @property
    def supported_id_ps(self):
        """Gets the supported_id_ps of this Configuration.  # noqa: E501

        List of IdPs supported by Onezone  # noqa: E501

        :return: The supported_id_ps of this Configuration.  # noqa: E501
        :rtype: list[ConfigurationSupportedIdPs]
        """
        return self._supported_id_ps

    @supported_id_ps.setter
    def supported_id_ps(self, supported_id_ps):
        """Sets the supported_id_ps of this Configuration.

        List of IdPs supported by Onezone  # noqa: E501

        :param supported_id_ps: The supported_id_ps of this Configuration.  # noqa: E501
        :type: list[ConfigurationSupportedIdPs]
        """
        if supported_id_ps is None:
            raise ValueError("Invalid value for `supported_id_ps`, must not be `None`")  # noqa: E501

        self._supported_id_ps = supported_id_ps

    @property
    def available_space_tags(self):
        """Gets the available_space_tags of this Configuration.  # noqa: E501

        A map of tag categories and corresponding available tags for each category.  Space tag is a short keyword or phrase that helps to understand the purpose of a space. Tag categories and available tags are arbitrary strings configured by the Onezone admin.   # noqa: E501

        :return: The available_space_tags of this Configuration.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._available_space_tags

    @available_space_tags.setter
    def available_space_tags(self, available_space_tags):
        """Sets the available_space_tags of this Configuration.

        A map of tag categories and corresponding available tags for each category.  Space tag is a short keyword or phrase that helps to understand the purpose of a space. Tag categories and available tags are arbitrary strings configured by the Onezone admin.   # noqa: E501

        :param available_space_tags: The available_space_tags of this Configuration.  # noqa: E501
        :type: dict(str, list[str])
        """
        if available_space_tags is None:
            raise ValueError("Invalid value for `available_space_tags`, must not be `None`")  # noqa: E501

        self._available_space_tags = available_space_tags

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
        if issubclass(Configuration, dict):
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
        if not isinstance(other, Configuration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
