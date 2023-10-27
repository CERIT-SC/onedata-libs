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

class GlusterfsModify(StorageModifyDetails):
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
        'volume': 'str',
        'hostname': 'str',
        'port': 'int',
        'transport': 'str',
        'mount_point': 'str',
        'xlator_options': 'str'
    }
    if hasattr(StorageModifyDetails, "swagger_types"):
        swagger_types.update(StorageModifyDetails.swagger_types)

    attribute_map = {
        'type': 'type',
        'volume': 'volume',
        'hostname': 'hostname',
        'port': 'port',
        'transport': 'transport',
        'mount_point': 'mountPoint',
        'xlator_options': 'xlatorOptions'
    }
    if hasattr(StorageModifyDetails, "attribute_map"):
        attribute_map.update(StorageModifyDetails.attribute_map)

    def __init__(self, type=None, volume=None, hostname=None, port=None, transport=None, mount_point=None, xlator_options=None, *args, **kwargs):  # noqa: E501
        """GlusterfsModify - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._volume = None
        self._hostname = None
        self._port = None
        self._transport = None
        self._mount_point = None
        self._xlator_options = None
        self.discriminator = None
        self.type = type
        if volume is not None:
            self.volume = volume
        if hostname is not None:
            self.hostname = hostname
        if port is not None:
            self.port = port
        if transport is not None:
            self.transport = transport
        if mount_point is not None:
            self.mount_point = mount_point
        if xlator_options is not None:
            self.xlator_options = xlator_options
        StorageModifyDetails.__init__(self, *args, **kwargs)

    @property
    def type(self):
        """Gets the type of this GlusterfsModify.  # noqa: E501

        The type of storage.  `type = \"glusterfs\"`  [GlusterFS](https://www.gluster.org/) volume directly attached to the Oneprovider.   # noqa: E501

        :return: The type of this GlusterfsModify.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GlusterfsModify.

        The type of storage.  `type = \"glusterfs\"`  [GlusterFS](https://www.gluster.org/) volume directly attached to the Oneprovider.   # noqa: E501

        :param type: The type of this GlusterfsModify.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["glusterfs"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def volume(self):
        """Gets the volume of this GlusterfsModify.  # noqa: E501

        The name of the volume to use as a storage backend.  # noqa: E501

        :return: The volume of this GlusterfsModify.  # noqa: E501
        :rtype: str
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this GlusterfsModify.

        The name of the volume to use as a storage backend.  # noqa: E501

        :param volume: The volume of this GlusterfsModify.  # noqa: E501
        :type: str
        """

        self._volume = volume

    @property
    def hostname(self):
        """Gets the hostname of this GlusterfsModify.  # noqa: E501

        The hostname (IP address or FQDN) of GlusterFS volume server.  # noqa: E501

        :return: The hostname of this GlusterfsModify.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this GlusterfsModify.

        The hostname (IP address or FQDN) of GlusterFS volume server.  # noqa: E501

        :param hostname: The hostname of this GlusterfsModify.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def port(self):
        """Gets the port of this GlusterfsModify.  # noqa: E501

        The GlusterFS port on volume server.  # noqa: E501

        :return: The port of this GlusterfsModify.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this GlusterfsModify.

        The GlusterFS port on volume server.  # noqa: E501

        :param port: The port of this GlusterfsModify.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def transport(self):
        """Gets the transport of this GlusterfsModify.  # noqa: E501

        The transport protocol to use to connect to the volume server.  # noqa: E501

        :return: The transport of this GlusterfsModify.  # noqa: E501
        :rtype: str
        """
        return self._transport

    @transport.setter
    def transport(self, transport):
        """Sets the transport of this GlusterfsModify.

        The transport protocol to use to connect to the volume server.  # noqa: E501

        :param transport: The transport of this GlusterfsModify.  # noqa: E501
        :type: str
        """
        allowed_values = ["tcp", "rdma", "socket"]  # noqa: E501
        if transport not in allowed_values:
            raise ValueError(
                "Invalid value for `transport` ({0}), must be one of {1}"  # noqa: E501
                .format(transport, allowed_values)
            )

        self._transport = transport

    @property
    def mount_point(self):
        """Gets the mount_point of this GlusterfsModify.  # noqa: E501

        Relative mountpoint within the volume which should be used by Oneprovider.  # noqa: E501

        :return: The mount_point of this GlusterfsModify.  # noqa: E501
        :rtype: str
        """
        return self._mount_point

    @mount_point.setter
    def mount_point(self, mount_point):
        """Sets the mount_point of this GlusterfsModify.

        Relative mountpoint within the volume which should be used by Oneprovider.  # noqa: E501

        :param mount_point: The mount_point of this GlusterfsModify.  # noqa: E501
        :type: str
        """

        self._mount_point = mount_point

    @property
    def xlator_options(self):
        """Gets the xlator_options of this GlusterfsModify.  # noqa: E501

        Volume specific GlusterFS translator options, in the format:   TRANSLATOR1.OPTION1=VALUE1;TRANSLATOR2.OPTION2=VALUE2;...   # noqa: E501

        :return: The xlator_options of this GlusterfsModify.  # noqa: E501
        :rtype: str
        """
        return self._xlator_options

    @xlator_options.setter
    def xlator_options(self, xlator_options):
        """Sets the xlator_options of this GlusterfsModify.

        Volume specific GlusterFS translator options, in the format:   TRANSLATOR1.OPTION1=VALUE1;TRANSLATOR2.OPTION2=VALUE2;...   # noqa: E501

        :param xlator_options: The xlator_options of this GlusterfsModify.  # noqa: E501
        :type: str
        """

        self._xlator_options = xlator_options

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
        if issubclass(GlusterfsModify, dict):
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
        if not isinstance(other, GlusterfsModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
