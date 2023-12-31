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

class WebCert(object):
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
        'lets_encrypt': 'bool',
        'expiration_time': 'str',
        'creation_time': 'str',
        'status': 'str',
        'paths': 'WebCertPaths',
        'domain': 'str',
        'issuer': 'str',
        'last_renewal_success': 'str',
        'last_renewal_failure': 'str'
    }

    attribute_map = {
        'lets_encrypt': 'letsEncrypt',
        'expiration_time': 'expirationTime',
        'creation_time': 'creationTime',
        'status': 'status',
        'paths': 'paths',
        'domain': 'domain',
        'issuer': 'issuer',
        'last_renewal_success': 'lastRenewalSuccess',
        'last_renewal_failure': 'lastRenewalFailure'
    }

    def __init__(self, lets_encrypt=None, expiration_time=None, creation_time=None, status=None, paths=None, domain=None, issuer=None, last_renewal_success=None, last_renewal_failure=None):  # noqa: E501
        """WebCert - a model defined in Swagger"""  # noqa: E501
        self._lets_encrypt = None
        self._expiration_time = None
        self._creation_time = None
        self._status = None
        self._paths = None
        self._domain = None
        self._issuer = None
        self._last_renewal_success = None
        self._last_renewal_failure = None
        self.discriminator = None
        self.lets_encrypt = lets_encrypt
        self.expiration_time = expiration_time
        self.creation_time = creation_time
        self.status = status
        self.paths = paths
        self.domain = domain
        self.issuer = issuer
        if last_renewal_success is not None:
            self.last_renewal_success = last_renewal_success
        if last_renewal_failure is not None:
            self.last_renewal_failure = last_renewal_failure

    @property
    def lets_encrypt(self):
        """Gets the lets_encrypt of this WebCert.  # noqa: E501

        If true, the certificate is obtained from Let's Encrypt service and renewed automatically. Otherwise, the certificate management is up to the administrator.   # noqa: E501

        :return: The lets_encrypt of this WebCert.  # noqa: E501
        :rtype: bool
        """
        return self._lets_encrypt

    @lets_encrypt.setter
    def lets_encrypt(self, lets_encrypt):
        """Sets the lets_encrypt of this WebCert.

        If true, the certificate is obtained from Let's Encrypt service and renewed automatically. Otherwise, the certificate management is up to the administrator.   # noqa: E501

        :param lets_encrypt: The lets_encrypt of this WebCert.  # noqa: E501
        :type: bool
        """
        if lets_encrypt is None:
            raise ValueError("Invalid value for `lets_encrypt`, must not be `None`")  # noqa: E501

        self._lets_encrypt = lets_encrypt

    @property
    def expiration_time(self):
        """Gets the expiration_time of this WebCert.  # noqa: E501

        Installed certificate's expiration time in ISO 8601 format.   # noqa: E501

        :return: The expiration_time of this WebCert.  # noqa: E501
        :rtype: str
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """Sets the expiration_time of this WebCert.

        Installed certificate's expiration time in ISO 8601 format.   # noqa: E501

        :param expiration_time: The expiration_time of this WebCert.  # noqa: E501
        :type: str
        """
        if expiration_time is None:
            raise ValueError("Invalid value for `expiration_time`, must not be `None`")  # noqa: E501

        self._expiration_time = expiration_time

    @property
    def creation_time(self):
        """Gets the creation_time of this WebCert.  # noqa: E501

        Installed certificate's creation time in ISO 8601 format.   # noqa: E501

        :return: The creation_time of this WebCert.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this WebCert.

        Installed certificate's creation time in ISO 8601 format.   # noqa: E501

        :param creation_time: The creation_time of this WebCert.  # noqa: E501
        :type: str
        """
        if creation_time is None:
            raise ValueError("Invalid value for `creation_time`, must not be `None`")  # noqa: E501

        self._creation_time = creation_time

    @property
    def status(self):
        """Gets the status of this WebCert.  # noqa: E501

        Describes certificate validity status.  # noqa: E501

        :return: The status of this WebCert.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WebCert.

        Describes certificate validity status.  # noqa: E501

        :param status: The status of this WebCert.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["valid", "near_expiration", "expired", "domain_mismatch", "regenerating", "unknown"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def paths(self):
        """Gets the paths of this WebCert.  # noqa: E501


        :return: The paths of this WebCert.  # noqa: E501
        :rtype: WebCertPaths
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this WebCert.


        :param paths: The paths of this WebCert.  # noqa: E501
        :type: WebCertPaths
        """
        if paths is None:
            raise ValueError("Invalid value for `paths`, must not be `None`")  # noqa: E501

        self._paths = paths

    @property
    def domain(self):
        """Gets the domain of this WebCert.  # noqa: E501

        The domain (Common Name) for which current certificate was issued.   # noqa: E501

        :return: The domain of this WebCert.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this WebCert.

        The domain (Common Name) for which current certificate was issued.   # noqa: E501

        :param domain: The domain of this WebCert.  # noqa: E501
        :type: str
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def issuer(self):
        """Gets the issuer of this WebCert.  # noqa: E501

        Issuer value of the current certificate.   # noqa: E501

        :return: The issuer of this WebCert.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this WebCert.

        Issuer value of the current certificate.   # noqa: E501

        :param issuer: The issuer of this WebCert.  # noqa: E501
        :type: str
        """
        if issuer is None:
            raise ValueError("Invalid value for `issuer`, must not be `None`")  # noqa: E501

        self._issuer = issuer

    @property
    def last_renewal_success(self):
        """Gets the last_renewal_success of this WebCert.  # noqa: E501

        Date and time in ISO 8601 format. Represents last successful Let's Encrypt certification. If there are no successful attempts its value is null. This property is omitted if letsEncrypt is off.   # noqa: E501

        :return: The last_renewal_success of this WebCert.  # noqa: E501
        :rtype: str
        """
        return self._last_renewal_success

    @last_renewal_success.setter
    def last_renewal_success(self, last_renewal_success):
        """Sets the last_renewal_success of this WebCert.

        Date and time in ISO 8601 format. Represents last successful Let's Encrypt certification. If there are no successful attempts its value is null. This property is omitted if letsEncrypt is off.   # noqa: E501

        :param last_renewal_success: The last_renewal_success of this WebCert.  # noqa: E501
        :type: str
        """

        self._last_renewal_success = last_renewal_success

    @property
    def last_renewal_failure(self):
        """Gets the last_renewal_failure of this WebCert.  # noqa: E501

        Date and time in ISO 8601 format. Represents last unsuccessful Let's Encrypt certification. If there are no successful attempts its value is null. This property is omitted if letsEncrypt is off.   # noqa: E501

        :return: The last_renewal_failure of this WebCert.  # noqa: E501
        :rtype: str
        """
        return self._last_renewal_failure

    @last_renewal_failure.setter
    def last_renewal_failure(self, last_renewal_failure):
        """Sets the last_renewal_failure of this WebCert.

        Date and time in ISO 8601 format. Represents last unsuccessful Let's Encrypt certification. If there are no successful attempts its value is null. This property is omitted if letsEncrypt is off.   # noqa: E501

        :param last_renewal_failure: The last_renewal_failure of this WebCert.  # noqa: E501
        :type: str
        """

        self._last_renewal_failure = last_renewal_failure

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
        if issubclass(WebCert, dict):
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
        if not isinstance(other, WebCert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
