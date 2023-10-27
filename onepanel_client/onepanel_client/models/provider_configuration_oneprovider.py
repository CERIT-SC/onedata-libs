# coding: utf-8

"""
    Onepanel

    # Overview  This is the RESTful API definition of **Onepanel** component of Onedata data management system [onedata.org](http://onedata.org).  > This API is defined using [Swagger](http://swagger.io/), the JSON specification can be used to automatically generate client libraries -   [swagger.json](../../../swagger/onepanel/swagger.json).  This API allows control and configuration of local Onedata deployment, in particular full control over the **Onezone** and **Oneprovider** services and their distribution and monitoring on the local resources.  The API is grouped into 3 categories of operations:   * **Onepanel** - for common operations   * **Oneprovider** - for Oneprovider specific administrative operations   * **Onezone** - for Onezone specific administrative operations  Each of these components is composed of the following services:   * **Worker services** - these are available under `/zone/workers` and     `/provider/workers` paths,   * **Databases services** - each Onedata component stores it's metadata in a     Couchbase backend, which can be distributed on any number of nodes, these     are available under `/zone/databases` and `/provider/databases` paths,   * **Cluster manager services** - this is a service which controls other     deployed processes in one site, these are availables under these are     available under `/zone/managers` and `/provider/managers` paths.  **Onezone** and **Oneprovider** components are composed of 3 types of services: **managers**, **databases** and **workers**.  Using this API each of these components can be deployed, configured, started and stopped on a specified host in the local site, in the context of either **Onezone** or **Oneprovider** service.  All paths listed in this documentation are relative to the base Onepanel REST API which is `/api/v3/onepanel`, so complete URL for a request to Onepanel service is:  ``` http://HOSTNAME:PORT/api/v3/onepanel/... ```  ## Authentication  ### Token authentication  The recommended, safest way of authenticating requests to Onepanel API is using the **Onedata access tokens**. The token should be present in `X-Auth-Token` or `Authorization: Bearer` header. See [Onezone documentation](/#/home/api/latest/onezone?anchor=section/Overview/Authentication-and-authorization) for detailed explanation of the token concepts.  Curl examples: ```bash curl -H \"X-Auth-Token: $TOKEN\" [...] curl -H \"Authorization: Bearer $TOKEN\" [...] curl -H \"Macaroon: $TOKEN\" [...]   # DEPRECATED ```   ### Passphrase authentication  The token authentication dependes on the Onezone service. In special cases - during Onezone deployment or its outage - it is necessary to use the local **emergency passphrase**.  The passphrase should be provided in a Basic authentication header with username `onepanel`. For curl users this means ```bash curl -u onepanel:TheEmergencyPassphrase ```  The passphrase can also be sent without any username, as the whole content of base64-encoded string in Basic authorization header, e.g. ```bash curl -H \"Authorization: Basic $(echo -n TheEmergencyPassphrase | base64)\" ```  The passphrase is set during deployment. It can be changed in the Onepanel GUI or with an API request: ```bash curl -X PUT 'https://$PANEL_HOST:9443/api/v3/onepanel/emergency_passphrase' \\ -u onepanel:TheEmergencyPassphrase -H 'Content-Type: application/json' \\ -d '{\"currentPassphrase\": \"TheEmergencyPassphrase\", \"newPassphrase\": \"TheNewPassphrase\"}' ```  ## API structure  The Onepanel API is structured to reflect that it can either be used to control **Onezone** or **Oneprovider** deployment, each Onedata component deployment has a separate Onepanel instance. In order to make the API calls explicit, **Onezone** or **Oneprovider** specific requests have different paths, i.e.:   * Onezone specific operations start with `/api/v3/onepanel/zone/`   * Oneprovider specific operations start with `/api/v3/onepanel/provider/`   * Common operations paths include `/api/v3/onepanel/users`,     `/api/v3/onepanel/hosts` and `/api/v3/onepanel/tasks`  The overall configuration of each component can be controlled by updating `/api/v3/onepanel/zone/configuration` and `/api/v3/onepanel/provider/configuration` resources.  ## Examples  Below are some example requests to Onepanel using cURL:  **Add storage resource to provider** ```bash curl -X POST -u onepanel:Passphrase1 -k -vvv -H \"content-type: application/json\" \\ -d '{\"NFS\": {\"type\": \"posix\", \"mountPoint\": \"/mnt/vfs\"}}' \\ https://172.17.0.4:9443/api/v3/onepanel/provider/storages ```  **Add a new Onezone worker** ```bash curl -X POST -u onepanel:Passphrase1 -k -vvv -H \"content-type: application/json\" \\ -d '{\"hosts\": [\"node1.p1.1.dev\"]}' \\ https://172.17.0.4:9443/api/v3/onepanel/zone/workers ```   # noqa: E501

    OpenAPI spec version: 21.02.3
    Contact: info@onedata.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProviderConfigurationOneprovider(object):
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
        'register': 'bool',
        'token_provision_method': 'str',
        'token': 'str',
        'token_file': 'str',
        'name': 'str',
        'subdomain_delegation': 'bool',
        'subdomain': 'str',
        'lets_encrypt_enabled': 'bool',
        'domain': 'str',
        'geo_longitude': 'float',
        'geo_latitude': 'float',
        'admin_email': 'str'
    }

    attribute_map = {
        'register': 'register',
        'token_provision_method': 'tokenProvisionMethod',
        'token': 'token',
        'token_file': 'tokenFile',
        'name': 'name',
        'subdomain_delegation': 'subdomainDelegation',
        'subdomain': 'subdomain',
        'lets_encrypt_enabled': 'letsEncryptEnabled',
        'domain': 'domain',
        'geo_longitude': 'geoLongitude',
        'geo_latitude': 'geoLatitude',
        'admin_email': 'adminEmail'
    }

    def __init__(self, register=None, token_provision_method='inline', token=None, token_file=None, name=None, subdomain_delegation=False, subdomain=None, lets_encrypt_enabled=False, domain=None, geo_longitude=None, geo_latitude=None, admin_email=None):  # noqa: E501
        """ProviderConfigurationOneprovider - a model defined in Swagger"""  # noqa: E501
        self._register = None
        self._token_provision_method = None
        self._token = None
        self._token_file = None
        self._name = None
        self._subdomain_delegation = None
        self._subdomain = None
        self._lets_encrypt_enabled = None
        self._domain = None
        self._geo_longitude = None
        self._geo_latitude = None
        self._admin_email = None
        self.discriminator = None
        self.register = register
        if token_provision_method is not None:
            self.token_provision_method = token_provision_method
        if token is not None:
            self.token = token
        if token_file is not None:
            self.token_file = token_file
        self.name = name
        if subdomain_delegation is not None:
            self.subdomain_delegation = subdomain_delegation
        if subdomain is not None:
            self.subdomain = subdomain
        if lets_encrypt_enabled is not None:
            self.lets_encrypt_enabled = lets_encrypt_enabled
        if domain is not None:
            self.domain = domain
        if geo_longitude is not None:
            self.geo_longitude = geo_longitude
        if geo_latitude is not None:
            self.geo_latitude = geo_latitude
        self.admin_email = admin_email

    @property
    def register(self):
        """Gets the register of this ProviderConfigurationOneprovider.  # noqa: E501

        Defines whether the provider should be registered in a zone.  # noqa: E501

        :return: The register of this ProviderConfigurationOneprovider.  # noqa: E501
        :rtype: bool
        """
        return self._register

    @register.setter
    def register(self, register):
        """Sets the register of this ProviderConfigurationOneprovider.

        Defines whether the provider should be registered in a zone.  # noqa: E501

        :param register: The register of this ProviderConfigurationOneprovider.  # noqa: E501
        :type: bool
        """
        if register is None:
            raise ValueError("Invalid value for `register`, must not be `None`")  # noqa: E501

        self._register = register

    @property
    def token_provision_method(self):
        """Gets the token_provision_method of this ProviderConfigurationOneprovider.  # noqa: E501

        Indicates how the Oneprovider registration token will be provided: * `\"inline\"` - the registration token must be placed in the **token**   field (consult for more information). * `\"fromFile\"` - the registration token will be read from given file,   specified in the **tokenFile** field (consult for more information).   # noqa: E501

        :return: The token_provision_method of this ProviderConfigurationOneprovider.  # noqa: E501
        :rtype: str
        """
        return self._token_provision_method

    @token_provision_method.setter
    def token_provision_method(self, token_provision_method):
        """Sets the token_provision_method of this ProviderConfigurationOneprovider.

        Indicates how the Oneprovider registration token will be provided: * `\"inline\"` - the registration token must be placed in the **token**   field (consult for more information). * `\"fromFile\"` - the registration token will be read from given file,   specified in the **tokenFile** field (consult for more information).   # noqa: E501

        :param token_provision_method: The token_provision_method of this ProviderConfigurationOneprovider.  # noqa: E501
        :type: str
        """
        allowed_values = ["inline", "fromFile"]  # noqa: E501
        if token_provision_method not in allowed_values:
            raise ValueError(
                "Invalid value for `token_provision_method` ({0}), must be one of {1}"  # noqa: E501
                .format(token_provision_method, allowed_values)
            )

        self._token_provision_method = token_provision_method

    @property
    def token(self):
        """Gets the token of this ProviderConfigurationOneprovider.  # noqa: E501

        Registration token obtained from Onezone. This token identifies the Onezone service where the Oneprovider will be registered and authorizes the registration request. Required when the `tokenProvisionMethod` is set to `\"inline\"`.   # noqa: E501

        :return: The token of this ProviderConfigurationOneprovider.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this ProviderConfigurationOneprovider.

        Registration token obtained from Onezone. This token identifies the Onezone service where the Oneprovider will be registered and authorizes the registration request. Required when the `tokenProvisionMethod` is set to `\"inline\"`.   # noqa: E501

        :param token: The token of this ProviderConfigurationOneprovider.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def token_file(self):
        """Gets the token_file of this ProviderConfigurationOneprovider.  # noqa: E501

        Absolute path to the file containing the Oneprovider registration token. The token (and nothing else) should be placed in the file as plaintext. The file does not have to pre-exist - it may be created after this request is made (Onepanel will wait for the file to appear for some time). Required when the `tokenProvisionMethod` is set to `\"fromFile\"`.   # noqa: E501

        :return: The token_file of this ProviderConfigurationOneprovider.  # noqa: E501
        :rtype: str
        """
        return self._token_file

    @token_file.setter
    def token_file(self, token_file):
        """Sets the token_file of this ProviderConfigurationOneprovider.

        Absolute path to the file containing the Oneprovider registration token. The token (and nothing else) should be placed in the file as plaintext. The file does not have to pre-exist - it may be created after this request is made (Onepanel will wait for the file to appear for some time). Required when the `tokenProvisionMethod` is set to `\"fromFile\"`.   # noqa: E501

        :param token_file: The token_file of this ProviderConfigurationOneprovider.  # noqa: E501
        :type: str
        """

        self._token_file = token_file

    @property
    def name(self):
        """Gets the name of this ProviderConfigurationOneprovider.  # noqa: E501

        The name under which the provider will be registered in a zone.  # noqa: E501

        :return: The name of this ProviderConfigurationOneprovider.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProviderConfigurationOneprovider.

        The name under which the provider will be registered in a zone.  # noqa: E501

        :param name: The name of this ProviderConfigurationOneprovider.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def subdomain_delegation(self):
        """Gets the subdomain_delegation of this ProviderConfigurationOneprovider.  # noqa: E501

        If enabled, the storage provider will be assigned a subdomain in onezone's domain and 'subdomain' property must be provided. If disabled, 'domain' property should be provided.   # noqa: E501

        :return: The subdomain_delegation of this ProviderConfigurationOneprovider.  # noqa: E501
        :rtype: bool
        """
        return self._subdomain_delegation

    @subdomain_delegation.setter
    def subdomain_delegation(self, subdomain_delegation):
        """Sets the subdomain_delegation of this ProviderConfigurationOneprovider.

        If enabled, the storage provider will be assigned a subdomain in onezone's domain and 'subdomain' property must be provided. If disabled, 'domain' property should be provided.   # noqa: E501

        :param subdomain_delegation: The subdomain_delegation of this ProviderConfigurationOneprovider.  # noqa: E501
        :type: bool
        """

        self._subdomain_delegation = subdomain_delegation

    @property
    def subdomain(self):
        """Gets the subdomain of this ProviderConfigurationOneprovider.  # noqa: E501

        Unique subdomain in onezone's domain for the provider. Required if subdomain delegation is enabled.   # noqa: E501

        :return: The subdomain of this ProviderConfigurationOneprovider.  # noqa: E501
        :rtype: str
        """
        return self._subdomain

    @subdomain.setter
    def subdomain(self, subdomain):
        """Sets the subdomain of this ProviderConfigurationOneprovider.

        Unique subdomain in onezone's domain for the provider. Required if subdomain delegation is enabled.   # noqa: E501

        :param subdomain: The subdomain of this ProviderConfigurationOneprovider.  # noqa: E501
        :type: str
        """

        self._subdomain = subdomain

    @property
    def lets_encrypt_enabled(self):
        """Gets the lets_encrypt_enabled of this ProviderConfigurationOneprovider.  # noqa: E501

        If enabled the provider will use Let's Encrypt service to obtain SSL certificates. Otherwise certificates must be manually provided. This option cannot be enabled if subdomainDelegation is false. By enabling this option you agree to the Let's Encrypt Subscriber Agreement.   # noqa: E501

        :return: The lets_encrypt_enabled of this ProviderConfigurationOneprovider.  # noqa: E501
        :rtype: bool
        """
        return self._lets_encrypt_enabled

    @lets_encrypt_enabled.setter
    def lets_encrypt_enabled(self, lets_encrypt_enabled):
        """Sets the lets_encrypt_enabled of this ProviderConfigurationOneprovider.

        If enabled the provider will use Let's Encrypt service to obtain SSL certificates. Otherwise certificates must be manually provided. This option cannot be enabled if subdomainDelegation is false. By enabling this option you agree to the Let's Encrypt Subscriber Agreement.   # noqa: E501

        :param lets_encrypt_enabled: The lets_encrypt_enabled of this ProviderConfigurationOneprovider.  # noqa: E501
        :type: bool
        """

        self._lets_encrypt_enabled = lets_encrypt_enabled

    @property
    def domain(self):
        """Gets the domain of this ProviderConfigurationOneprovider.  # noqa: E501

        The fully qualified domain name of the provider or its IP address (only for single-node deployments or clusters with a reverse proxy). Required if subdomain delegation is disabled.   # noqa: E501

        :return: The domain of this ProviderConfigurationOneprovider.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ProviderConfigurationOneprovider.

        The fully qualified domain name of the provider or its IP address (only for single-node deployments or clusters with a reverse proxy). Required if subdomain delegation is disabled.   # noqa: E501

        :param domain: The domain of this ProviderConfigurationOneprovider.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def geo_longitude(self):
        """Gets the geo_longitude of this ProviderConfigurationOneprovider.  # noqa: E501

        The geographical longitude of the provider.  # noqa: E501

        :return: The geo_longitude of this ProviderConfigurationOneprovider.  # noqa: E501
        :rtype: float
        """
        return self._geo_longitude

    @geo_longitude.setter
    def geo_longitude(self, geo_longitude):
        """Sets the geo_longitude of this ProviderConfigurationOneprovider.

        The geographical longitude of the provider.  # noqa: E501

        :param geo_longitude: The geo_longitude of this ProviderConfigurationOneprovider.  # noqa: E501
        :type: float
        """

        self._geo_longitude = geo_longitude

    @property
    def geo_latitude(self):
        """Gets the geo_latitude of this ProviderConfigurationOneprovider.  # noqa: E501

        The geographical latitude of the provider.  # noqa: E501

        :return: The geo_latitude of this ProviderConfigurationOneprovider.  # noqa: E501
        :rtype: float
        """
        return self._geo_latitude

    @geo_latitude.setter
    def geo_latitude(self, geo_latitude):
        """Sets the geo_latitude of this ProviderConfigurationOneprovider.

        The geographical latitude of the provider.  # noqa: E501

        :param geo_latitude: The geo_latitude of this ProviderConfigurationOneprovider.  # noqa: E501
        :type: float
        """

        self._geo_latitude = geo_latitude

    @property
    def admin_email(self):
        """Gets the admin_email of this ProviderConfigurationOneprovider.  # noqa: E501

        Email address of the oneprovider administrator.  # noqa: E501

        :return: The admin_email of this ProviderConfigurationOneprovider.  # noqa: E501
        :rtype: str
        """
        return self._admin_email

    @admin_email.setter
    def admin_email(self, admin_email):
        """Sets the admin_email of this ProviderConfigurationOneprovider.

        Email address of the oneprovider administrator.  # noqa: E501

        :param admin_email: The admin_email of this ProviderConfigurationOneprovider.  # noqa: E501
        :type: str
        """
        if admin_email is None:
            raise ValueError("Invalid value for `admin_email`, must not be `None`")  # noqa: E501

        self._admin_email = admin_email

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
        if issubclass(ProviderConfigurationOneprovider, dict):
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
        if not isinstance(other, ProviderConfigurationOneprovider):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
