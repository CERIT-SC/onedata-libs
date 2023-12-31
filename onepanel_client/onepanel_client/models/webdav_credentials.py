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
from onepanel_client.models.luma_storage_credentials import LumaStorageCredentials  # noqa: F401,E501

class WebdavCredentials(LumaStorageCredentials):
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
        'type': 'str',
        'credentials_type': 'str',
        'credentials': 'str',
        'oauth2_id_p': 'str',
        'onedata_access_token': 'str'
    }
    if hasattr(LumaStorageCredentials, "swagger_types"):
        swagger_types.update(LumaStorageCredentials.swagger_types)

    attribute_map = {
        'type': 'type',
        'credentials_type': 'credentialsType',
        'credentials': 'credentials',
        'oauth2_id_p': 'oauth2IdP',
        'onedata_access_token': 'onedataAccessToken'
    }
    if hasattr(LumaStorageCredentials, "attribute_map"):
        attribute_map.update(LumaStorageCredentials.attribute_map)

    def __init__(self, type=None, credentials_type='none', credentials=None, oauth2_id_p=None, onedata_access_token=None, *args, **kwargs):  # noqa: E501
        """WebdavCredentials - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._credentials_type = None
        self._credentials = None
        self._oauth2_id_p = None
        self._onedata_access_token = None
        self.discriminator = None
        self.type = type
        if credentials_type is not None:
            self.credentials_type = credentials_type
        if credentials is not None:
            self.credentials = credentials
        if oauth2_id_p is not None:
            self.oauth2_id_p = oauth2_id_p
        if onedata_access_token is not None:
            self.onedata_access_token = onedata_access_token
        LumaStorageCredentials.__init__(self, *args, **kwargs)

    @property
    def type(self):
        """Gets the type of this WebdavCredentials.  # noqa: E501

        Type of the storage. Must be given explicitly and must match the actual type of subject storage - this redundancy is needed due to limitations of OpenAPI polymorphism.   # noqa: E501

        :return: The type of this WebdavCredentials.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WebdavCredentials.

        Type of the storage. Must be given explicitly and must match the actual type of subject storage - this redundancy is needed due to limitations of OpenAPI polymorphism.   # noqa: E501

        :param type: The type of this WebdavCredentials.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["webdav"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def credentials_type(self):
        """Gets the credentials_type of this WebdavCredentials.  # noqa: E501

        Determines the types of credentials provided in the credentials field.   # noqa: E501

        :return: The credentials_type of this WebdavCredentials.  # noqa: E501
        :rtype: str
        """
        return self._credentials_type

    @credentials_type.setter
    def credentials_type(self, credentials_type):
        """Sets the credentials_type of this WebdavCredentials.

        Determines the types of credentials provided in the credentials field.   # noqa: E501

        :param credentials_type: The credentials_type of this WebdavCredentials.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "basic", "token", "oauth2"]  # noqa: E501
        if credentials_type not in allowed_values:
            raise ValueError(
                "Invalid value for `credentials_type` ({0}), must be one of {1}"  # noqa: E501
                .format(credentials_type, allowed_values)
            )

        self._credentials_type = credentials_type

    @property
    def credentials(self):
        """Gets the credentials of this WebdavCredentials.  # noqa: E501

        The credentials to authenticate with the WebDAV server. `basic` credentials should be provided in the form `username:password`, for `token` just the token. In case of `oauth2`, this field should contain the username for the WebDAV, while the token will be obtained and refreshed automatically in the background. For `none` this field is ignored.   # noqa: E501

        :return: The credentials of this WebdavCredentials.  # noqa: E501
        :rtype: str
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this WebdavCredentials.

        The credentials to authenticate with the WebDAV server. `basic` credentials should be provided in the form `username:password`, for `token` just the token. In case of `oauth2`, this field should contain the username for the WebDAV, while the token will be obtained and refreshed automatically in the background. For `none` this field is ignored.   # noqa: E501

        :param credentials: The credentials of this WebdavCredentials.  # noqa: E501
        :type: str
        """

        self._credentials = credentials

    @property
    def oauth2_id_p(self):
        """Gets the oauth2_id_p of this WebdavCredentials.  # noqa: E501

        In case `oauth2` credential type is selected and Onezone is configured with support for multiple external IdP's, this field must contain the name of the IdP which authenticates requests to the WebDAV endpoint. If Onezone has only one external IdP, it will be selected automatically.   # noqa: E501

        :return: The oauth2_id_p of this WebdavCredentials.  # noqa: E501
        :rtype: str
        """
        return self._oauth2_id_p

    @oauth2_id_p.setter
    def oauth2_id_p(self, oauth2_id_p):
        """Sets the oauth2_id_p of this WebdavCredentials.

        In case `oauth2` credential type is selected and Onezone is configured with support for multiple external IdP's, this field must contain the name of the IdP which authenticates requests to the WebDAV endpoint. If Onezone has only one external IdP, it will be selected automatically.   # noqa: E501

        :param oauth2_id_p: The oauth2_id_p of this WebdavCredentials.  # noqa: E501
        :type: str
        """

        self._oauth2_id_p = oauth2_id_p

    @property
    def onedata_access_token(self):
        """Gets the onedata_access_token of this WebdavCredentials.  # noqa: E501

        When registering storage with feed of LUMA DB set to`auto` and with `oauth2` external IdP, this field must contain a valid Onedata access token of the user on whose behalf the WebDAV storage will be accessed by all users with access to any space supported by this storage.   # noqa: E501

        :return: The onedata_access_token of this WebdavCredentials.  # noqa: E501
        :rtype: str
        """
        return self._onedata_access_token

    @onedata_access_token.setter
    def onedata_access_token(self, onedata_access_token):
        """Sets the onedata_access_token of this WebdavCredentials.

        When registering storage with feed of LUMA DB set to`auto` and with `oauth2` external IdP, this field must contain a valid Onedata access token of the user on whose behalf the WebDAV storage will be accessed by all users with access to any space supported by this storage.   # noqa: E501

        :param onedata_access_token: The onedata_access_token of this WebdavCredentials.  # noqa: E501
        :type: str
        """

        self._onedata_access_token = onedata_access_token

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
        if issubclass(WebdavCredentials, dict):
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
        if not isinstance(other, WebdavCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
