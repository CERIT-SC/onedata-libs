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
from onepanel_client.models.storage_modify_details import StorageModifyDetails  # noqa: F401,E501

class HTTPModify(StorageModifyDetails):
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
        'endpoint': 'str',
        'verify_server_certificate': 'bool',
        'credentials_type': 'str',
        'credentials': 'str',
        'authorization_header': 'str',
        'connection_pool_size': 'int',
        'max_requests_per_session': 'int',
        'file_mode': 'str'
    }
    if hasattr(StorageModifyDetails, "swagger_types"):
        swagger_types.update(StorageModifyDetails.swagger_types)

    attribute_map = {
        'type': 'type',
        'endpoint': 'endpoint',
        'verify_server_certificate': 'verifyServerCertificate',
        'credentials_type': 'credentialsType',
        'credentials': 'credentials',
        'authorization_header': 'authorizationHeader',
        'connection_pool_size': 'connectionPoolSize',
        'max_requests_per_session': 'maxRequestsPerSession',
        'file_mode': 'fileMode'
    }
    if hasattr(StorageModifyDetails, "attribute_map"):
        attribute_map.update(StorageModifyDetails.attribute_map)

    def __init__(self, type=None, endpoint=None, verify_server_certificate=None, credentials_type=None, credentials=None, authorization_header=None, connection_pool_size=None, max_requests_per_session=None, file_mode=None, *args, **kwargs):  # noqa: E501
        """HTTPModify - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._endpoint = None
        self._verify_server_certificate = None
        self._credentials_type = None
        self._credentials = None
        self._authorization_header = None
        self._connection_pool_size = None
        self._max_requests_per_session = None
        self._file_mode = None
        self.discriminator = None
        self.type = type
        if endpoint is not None:
            self.endpoint = endpoint
        if verify_server_certificate is not None:
            self.verify_server_certificate = verify_server_certificate
        if credentials_type is not None:
            self.credentials_type = credentials_type
        if credentials is not None:
            self.credentials = credentials
        if authorization_header is not None:
            self.authorization_header = authorization_header
        if connection_pool_size is not None:
            self.connection_pool_size = connection_pool_size
        if max_requests_per_session is not None:
            self.max_requests_per_session = max_requests_per_session
        if file_mode is not None:
            self.file_mode = file_mode
        StorageModifyDetails.__init__(self, *args, **kwargs)

    @property
    def type(self):
        """Gets the type of this HTTPModify.  # noqa: E501

        The type of storage.  `type = \"http\"`  Any [HTTP](https://tools.ietf.org/html/rfc7231) or HTTPS compatible server. Supported only with Readonly option enabled and in manual import mode.   # noqa: E501

        :return: The type of this HTTPModify.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HTTPModify.

        The type of storage.  `type = \"http\"`  Any [HTTP](https://tools.ietf.org/html/rfc7231) or HTTPS compatible server. Supported only with Readonly option enabled and in manual import mode.   # noqa: E501

        :param type: The type of this HTTPModify.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["http"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def endpoint(self):
        """Gets the endpoint of this HTTPModify.  # noqa: E501

        Full URL of the HTTP server, including scheme (http or https) and path.   # noqa: E501

        :return: The endpoint of this HTTPModify.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this HTTPModify.

        Full URL of the HTTP server, including scheme (http or https) and path.   # noqa: E501

        :param endpoint: The endpoint of this HTTPModify.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def verify_server_certificate(self):
        """Gets the verify_server_certificate of this HTTPModify.  # noqa: E501

        Determines whether Oneprovider should verify the certificate of the HTTP server.   # noqa: E501

        :return: The verify_server_certificate of this HTTPModify.  # noqa: E501
        :rtype: bool
        """
        return self._verify_server_certificate

    @verify_server_certificate.setter
    def verify_server_certificate(self, verify_server_certificate):
        """Sets the verify_server_certificate of this HTTPModify.

        Determines whether Oneprovider should verify the certificate of the HTTP server.   # noqa: E501

        :param verify_server_certificate: The verify_server_certificate of this HTTPModify.  # noqa: E501
        :type: bool
        """

        self._verify_server_certificate = verify_server_certificate

    @property
    def credentials_type(self):
        """Gets the credentials_type of this HTTPModify.  # noqa: E501

        Determines the types of credentials provided in the credentials field.   # noqa: E501

        :return: The credentials_type of this HTTPModify.  # noqa: E501
        :rtype: str
        """
        return self._credentials_type

    @credentials_type.setter
    def credentials_type(self, credentials_type):
        """Sets the credentials_type of this HTTPModify.

        Determines the types of credentials provided in the credentials field.   # noqa: E501

        :param credentials_type: The credentials_type of this HTTPModify.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "basic", "token"]  # noqa: E501
        if credentials_type not in allowed_values:
            raise ValueError(
                "Invalid value for `credentials_type` ({0}), must be one of {1}"  # noqa: E501
                .format(credentials_type, allowed_values)
            )

        self._credentials_type = credentials_type

    @property
    def credentials(self):
        """Gets the credentials of this HTTPModify.  # noqa: E501

        The credentials to authenticate with the HTTP server. `basic` credentials should be provided in the form `username:password`, for `token` just the token. For `none` this field is ignored.   # noqa: E501

        :return: The credentials of this HTTPModify.  # noqa: E501
        :rtype: str
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this HTTPModify.

        The credentials to authenticate with the HTTP server. `basic` credentials should be provided in the form `username:password`, for `token` just the token. For `none` this field is ignored.   # noqa: E501

        :param credentials: The credentials of this HTTPModify.  # noqa: E501
        :type: str
        """

        self._credentials = credentials

    @property
    def authorization_header(self):
        """Gets the authorization_header of this HTTPModify.  # noqa: E501

        The authorization header to be used for passing the access token. This field can contain any prefix that should be added to the header value. Default is `Authorization: Bearer {}`. The token will placed where `{}` is provided.   # noqa: E501

        :return: The authorization_header of this HTTPModify.  # noqa: E501
        :rtype: str
        """
        return self._authorization_header

    @authorization_header.setter
    def authorization_header(self, authorization_header):
        """Sets the authorization_header of this HTTPModify.

        The authorization header to be used for passing the access token. This field can contain any prefix that should be added to the header value. Default is `Authorization: Bearer {}`. The token will placed where `{}` is provided.   # noqa: E501

        :param authorization_header: The authorization_header of this HTTPModify.  # noqa: E501
        :type: str
        """

        self._authorization_header = authorization_header

    @property
    def connection_pool_size(self):
        """Gets the connection_pool_size of this HTTPModify.  # noqa: E501

        Defines the maximum number of parallel connections for a single HTTP storage.   # noqa: E501

        :return: The connection_pool_size of this HTTPModify.  # noqa: E501
        :rtype: int
        """
        return self._connection_pool_size

    @connection_pool_size.setter
    def connection_pool_size(self, connection_pool_size):
        """Sets the connection_pool_size of this HTTPModify.

        Defines the maximum number of parallel connections for a single HTTP storage.   # noqa: E501

        :param connection_pool_size: The connection_pool_size of this HTTPModify.  # noqa: E501
        :type: int
        """

        self._connection_pool_size = connection_pool_size

    @property
    def max_requests_per_session(self):
        """Gets the max_requests_per_session of this HTTPModify.  # noqa: E501

        Defines the maximum number of requests performed in a single HTTP session. After the limit is reached, 'Connection: close' header is sent to the server. When set to 0 (default), number of requests per session is unlimited, unless imposed by the server.   # noqa: E501

        :return: The max_requests_per_session of this HTTPModify.  # noqa: E501
        :rtype: int
        """
        return self._max_requests_per_session

    @max_requests_per_session.setter
    def max_requests_per_session(self, max_requests_per_session):
        """Sets the max_requests_per_session of this HTTPModify.

        Defines the maximum number of requests performed in a single HTTP session. After the limit is reached, 'Connection: close' header is sent to the server. When set to 0 (default), number of requests per session is unlimited, unless imposed by the server.   # noqa: E501

        :param max_requests_per_session: The max_requests_per_session of this HTTPModify.  # noqa: E501
        :type: int
        """

        self._max_requests_per_session = max_requests_per_session

    @property
    def file_mode(self):
        """Gets the file_mode of this HTTPModify.  # noqa: E501

        Defines the file permissions, which files imported from HTTP storage will have in Onedata. Values should be provided in octal format e.g. `0664`.   # noqa: E501

        :return: The file_mode of this HTTPModify.  # noqa: E501
        :rtype: str
        """
        return self._file_mode

    @file_mode.setter
    def file_mode(self, file_mode):
        """Sets the file_mode of this HTTPModify.

        Defines the file permissions, which files imported from HTTP storage will have in Onedata. Values should be provided in octal format e.g. `0664`.   # noqa: E501

        :param file_mode: The file_mode of this HTTPModify.  # noqa: E501
        :type: str
        """

        self._file_mode = file_mode

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
        if issubclass(HTTPModify, dict):
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
        if not isinstance(other, HTTPModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other