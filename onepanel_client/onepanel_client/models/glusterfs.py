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
from onepanel_client.models.storage_get_details import StorageGetDetails  # noqa: F401,E501

class Glusterfs(StorageGetDetails):
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
        'timeout': 'int',
        'skip_storage_detection': 'bool',
        'luma_feed': 'str',
        'luma_feed_url': 'str',
        'luma_feed_api_key': 'str',
        'qos_parameters': 'dict(str, str)',
        'imported_storage': 'bool',
        'archive_storage': 'bool',
        'readonly': 'bool',
        'volume': 'str',
        'hostname': 'str',
        'port': 'int',
        'transport': 'str',
        'mount_point': 'str',
        'xlator_options': 'str',
        'storage_path_type': 'str'
    }
    if hasattr(StorageGetDetails, "swagger_types"):
        swagger_types.update(StorageGetDetails.swagger_types)

    attribute_map = {
        'type': 'type',
        'timeout': 'timeout',
        'skip_storage_detection': 'skipStorageDetection',
        'luma_feed': 'lumaFeed',
        'luma_feed_url': 'lumaFeedUrl',
        'luma_feed_api_key': 'lumaFeedApiKey',
        'qos_parameters': 'qosParameters',
        'imported_storage': 'importedStorage',
        'archive_storage': 'archiveStorage',
        'readonly': 'readonly',
        'volume': 'volume',
        'hostname': 'hostname',
        'port': 'port',
        'transport': 'transport',
        'mount_point': 'mountPoint',
        'xlator_options': 'xlatorOptions',
        'storage_path_type': 'storagePathType'
    }
    if hasattr(StorageGetDetails, "attribute_map"):
        attribute_map.update(StorageGetDetails.attribute_map)

    def __init__(self, type=None, timeout=None, skip_storage_detection=False, luma_feed='auto', luma_feed_url=None, luma_feed_api_key=None, qos_parameters=None, imported_storage=False, archive_storage=False, readonly=False, volume=None, hostname=None, port=None, transport='tcp', mount_point='', xlator_options='', storage_path_type='canonical', *args, **kwargs):  # noqa: E501
        """Glusterfs - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._timeout = None
        self._skip_storage_detection = None
        self._luma_feed = None
        self._luma_feed_url = None
        self._luma_feed_api_key = None
        self._qos_parameters = None
        self._imported_storage = None
        self._archive_storage = None
        self._readonly = None
        self._volume = None
        self._hostname = None
        self._port = None
        self._transport = None
        self._mount_point = None
        self._xlator_options = None
        self._storage_path_type = None
        self.discriminator = None
        self.type = type
        if timeout is not None:
            self.timeout = timeout
        if skip_storage_detection is not None:
            self.skip_storage_detection = skip_storage_detection
        if luma_feed is not None:
            self.luma_feed = luma_feed
        if luma_feed_url is not None:
            self.luma_feed_url = luma_feed_url
        if luma_feed_api_key is not None:
            self.luma_feed_api_key = luma_feed_api_key
        if qos_parameters is not None:
            self.qos_parameters = qos_parameters
        if imported_storage is not None:
            self.imported_storage = imported_storage
        if archive_storage is not None:
            self.archive_storage = archive_storage
        if readonly is not None:
            self.readonly = readonly
        self.volume = volume
        self.hostname = hostname
        if port is not None:
            self.port = port
        if transport is not None:
            self.transport = transport
        if mount_point is not None:
            self.mount_point = mount_point
        if xlator_options is not None:
            self.xlator_options = xlator_options
        if storage_path_type is not None:
            self.storage_path_type = storage_path_type
        StorageGetDetails.__init__(self, *args, **kwargs)

    @property
    def type(self):
        """Gets the type of this Glusterfs.  # noqa: E501

        The type of storage.  `type = \"glusterfs\"`  [GlusterFS](https://www.gluster.org/) volume directly attached to the Oneprovider.   # noqa: E501

        :return: The type of this Glusterfs.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Glusterfs.

        The type of storage.  `type = \"glusterfs\"`  [GlusterFS](https://www.gluster.org/) volume directly attached to the Oneprovider.   # noqa: E501

        :param type: The type of this Glusterfs.  # noqa: E501
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
    def timeout(self):
        """Gets the timeout of this Glusterfs.  # noqa: E501

        Storage operation timeout in milliseconds.  # noqa: E501

        :return: The timeout of this Glusterfs.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this Glusterfs.

        Storage operation timeout in milliseconds.  # noqa: E501

        :param timeout: The timeout of this Glusterfs.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def skip_storage_detection(self):
        """Gets the skip_storage_detection of this Glusterfs.  # noqa: E501

        If true, detecting whether storage is directly accessible by the Oneclient will not be performed. This option should be set to true on readonly storages.   # noqa: E501

        :return: The skip_storage_detection of this Glusterfs.  # noqa: E501
        :rtype: bool
        """
        return self._skip_storage_detection

    @skip_storage_detection.setter
    def skip_storage_detection(self, skip_storage_detection):
        """Sets the skip_storage_detection of this Glusterfs.

        If true, detecting whether storage is directly accessible by the Oneclient will not be performed. This option should be set to true on readonly storages.   # noqa: E501

        :param skip_storage_detection: The skip_storage_detection of this Glusterfs.  # noqa: E501
        :type: bool
        """

        self._skip_storage_detection = skip_storage_detection

    @property
    def luma_feed(self):
        """Gets the luma_feed of this Glusterfs.  # noqa: E501

        Type of feed for LUMA DB. Feed is a source of user/group mappings used to populate the LUMA DB. For more info please read: https://onedata.org/#/home/documentation/doc/administering_onedata/luma.html   # noqa: E501

        :return: The luma_feed of this Glusterfs.  # noqa: E501
        :rtype: str
        """
        return self._luma_feed

    @luma_feed.setter
    def luma_feed(self, luma_feed):
        """Sets the luma_feed of this Glusterfs.

        Type of feed for LUMA DB. Feed is a source of user/group mappings used to populate the LUMA DB. For more info please read: https://onedata.org/#/home/documentation/doc/administering_onedata/luma.html   # noqa: E501

        :param luma_feed: The luma_feed of this Glusterfs.  # noqa: E501
        :type: str
        """
        allowed_values = ["auto", "local", "external"]  # noqa: E501
        if luma_feed not in allowed_values:
            raise ValueError(
                "Invalid value for `luma_feed` ({0}), must be one of {1}"  # noqa: E501
                .format(luma_feed, allowed_values)
            )

        self._luma_feed = luma_feed

    @property
    def luma_feed_url(self):
        """Gets the luma_feed_url of this Glusterfs.  # noqa: E501

        URL of external feed for LUMA DB. Relevant only if lumaFeed equals `external`.  # noqa: E501

        :return: The luma_feed_url of this Glusterfs.  # noqa: E501
        :rtype: str
        """
        return self._luma_feed_url

    @luma_feed_url.setter
    def luma_feed_url(self, luma_feed_url):
        """Sets the luma_feed_url of this Glusterfs.

        URL of external feed for LUMA DB. Relevant only if lumaFeed equals `external`.  # noqa: E501

        :param luma_feed_url: The luma_feed_url of this Glusterfs.  # noqa: E501
        :type: str
        """

        self._luma_feed_url = luma_feed_url

    @property
    def luma_feed_api_key(self):
        """Gets the luma_feed_api_key of this Glusterfs.  # noqa: E501

        API key checked by external service used as feed for LUMA DB. Relevant only if lumaFeed equals `external`.   # noqa: E501

        :return: The luma_feed_api_key of this Glusterfs.  # noqa: E501
        :rtype: str
        """
        return self._luma_feed_api_key

    @luma_feed_api_key.setter
    def luma_feed_api_key(self, luma_feed_api_key):
        """Sets the luma_feed_api_key of this Glusterfs.

        API key checked by external service used as feed for LUMA DB. Relevant only if lumaFeed equals `external`.   # noqa: E501

        :param luma_feed_api_key: The luma_feed_api_key of this Glusterfs.  # noqa: E501
        :type: str
        """

        self._luma_feed_api_key = luma_feed_api_key

    @property
    def qos_parameters(self):
        """Gets the qos_parameters of this Glusterfs.  # noqa: E501

        Map with key-value pairs used for describing storage QoS parameters.  # noqa: E501

        :return: The qos_parameters of this Glusterfs.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._qos_parameters

    @qos_parameters.setter
    def qos_parameters(self, qos_parameters):
        """Sets the qos_parameters of this Glusterfs.

        Map with key-value pairs used for describing storage QoS parameters.  # noqa: E501

        :param qos_parameters: The qos_parameters of this Glusterfs.  # noqa: E501
        :type: dict(str, str)
        """

        self._qos_parameters = qos_parameters

    @property
    def imported_storage(self):
        """Gets the imported_storage of this Glusterfs.  # noqa: E501

        Defines whether storage contains existing data to be imported.   # noqa: E501

        :return: The imported_storage of this Glusterfs.  # noqa: E501
        :rtype: bool
        """
        return self._imported_storage

    @imported_storage.setter
    def imported_storage(self, imported_storage):
        """Sets the imported_storage of this Glusterfs.

        Defines whether storage contains existing data to be imported.   # noqa: E501

        :param imported_storage: The imported_storage of this Glusterfs.  # noqa: E501
        :type: bool
        """

        self._imported_storage = imported_storage

    @property
    def archive_storage(self):
        """Gets the archive_storage of this Glusterfs.  # noqa: E501

        Defines whether storage supports long-term dataset archiving.   # noqa: E501

        :return: The archive_storage of this Glusterfs.  # noqa: E501
        :rtype: bool
        """
        return self._archive_storage

    @archive_storage.setter
    def archive_storage(self, archive_storage):
        """Sets the archive_storage of this Glusterfs.

        Defines whether storage supports long-term dataset archiving.   # noqa: E501

        :param archive_storage: The archive_storage of this Glusterfs.  # noqa: E501
        :type: bool
        """

        self._archive_storage = archive_storage

    @property
    def readonly(self):
        """Gets the readonly of this Glusterfs.  # noqa: E501

        Defines whether the storage is readonly. If enabled, Oneprovider will block any operation that writes, modifies or deletes data on the storage. Such storage can only be used to import data into the space. Mandatory to ensure proper behaviour if the backend storage is actually configured as readonly. This option is available only for imported storages.   # noqa: E501

        :return: The readonly of this Glusterfs.  # noqa: E501
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        """Sets the readonly of this Glusterfs.

        Defines whether the storage is readonly. If enabled, Oneprovider will block any operation that writes, modifies or deletes data on the storage. Such storage can only be used to import data into the space. Mandatory to ensure proper behaviour if the backend storage is actually configured as readonly. This option is available only for imported storages.   # noqa: E501

        :param readonly: The readonly of this Glusterfs.  # noqa: E501
        :type: bool
        """

        self._readonly = readonly

    @property
    def volume(self):
        """Gets the volume of this Glusterfs.  # noqa: E501

        The name of the volume to use as a storage backend.  # noqa: E501

        :return: The volume of this Glusterfs.  # noqa: E501
        :rtype: str
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this Glusterfs.

        The name of the volume to use as a storage backend.  # noqa: E501

        :param volume: The volume of this Glusterfs.  # noqa: E501
        :type: str
        """
        if volume is None:
            raise ValueError("Invalid value for `volume`, must not be `None`")  # noqa: E501

        self._volume = volume

    @property
    def hostname(self):
        """Gets the hostname of this Glusterfs.  # noqa: E501

        The hostname (IP address or FQDN) of GlusterFS volume server.  # noqa: E501

        :return: The hostname of this Glusterfs.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this Glusterfs.

        The hostname (IP address or FQDN) of GlusterFS volume server.  # noqa: E501

        :param hostname: The hostname of this Glusterfs.  # noqa: E501
        :type: str
        """
        if hostname is None:
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501

        self._hostname = hostname

    @property
    def port(self):
        """Gets the port of this Glusterfs.  # noqa: E501

        The GlusterFS port on volume server.  # noqa: E501

        :return: The port of this Glusterfs.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this Glusterfs.

        The GlusterFS port on volume server.  # noqa: E501

        :param port: The port of this Glusterfs.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def transport(self):
        """Gets the transport of this Glusterfs.  # noqa: E501

        The transport protocol to use to connect to the volume server.  # noqa: E501

        :return: The transport of this Glusterfs.  # noqa: E501
        :rtype: str
        """
        return self._transport

    @transport.setter
    def transport(self, transport):
        """Sets the transport of this Glusterfs.

        The transport protocol to use to connect to the volume server.  # noqa: E501

        :param transport: The transport of this Glusterfs.  # noqa: E501
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
        """Gets the mount_point of this Glusterfs.  # noqa: E501

        Relative mountpoint within the volume which should be used by Oneprovider.  # noqa: E501

        :return: The mount_point of this Glusterfs.  # noqa: E501
        :rtype: str
        """
        return self._mount_point

    @mount_point.setter
    def mount_point(self, mount_point):
        """Sets the mount_point of this Glusterfs.

        Relative mountpoint within the volume which should be used by Oneprovider.  # noqa: E501

        :param mount_point: The mount_point of this Glusterfs.  # noqa: E501
        :type: str
        """

        self._mount_point = mount_point

    @property
    def xlator_options(self):
        """Gets the xlator_options of this Glusterfs.  # noqa: E501

        Volume specific GlusterFS translator options, in the format:   TRANSLATOR1.OPTION1=VALUE1;TRANSLATOR2.OPTION2=VALUE2;...   # noqa: E501

        :return: The xlator_options of this Glusterfs.  # noqa: E501
        :rtype: str
        """
        return self._xlator_options

    @xlator_options.setter
    def xlator_options(self, xlator_options):
        """Sets the xlator_options of this Glusterfs.

        Volume specific GlusterFS translator options, in the format:   TRANSLATOR1.OPTION1=VALUE1;TRANSLATOR2.OPTION2=VALUE2;...   # noqa: E501

        :param xlator_options: The xlator_options of this Glusterfs.  # noqa: E501
        :type: str
        """

        self._xlator_options = xlator_options

    @property
    def storage_path_type(self):
        """Gets the storage_path_type of this Glusterfs.  # noqa: E501

        Determines how the logical file paths will be mapped on the storage. 'canonical' paths reflect the logical file names and directory structure, however each rename operation will require renaming the files on the storage. 'flat' paths are based on unique file UUID's and do not require on-storage rename when logical file name is changed. **Note that 'flat' paths are not allowed on this type of storage.**   # noqa: E501

        :return: The storage_path_type of this Glusterfs.  # noqa: E501
        :rtype: str
        """
        return self._storage_path_type

    @storage_path_type.setter
    def storage_path_type(self, storage_path_type):
        """Sets the storage_path_type of this Glusterfs.

        Determines how the logical file paths will be mapped on the storage. 'canonical' paths reflect the logical file names and directory structure, however each rename operation will require renaming the files on the storage. 'flat' paths are based on unique file UUID's and do not require on-storage rename when logical file name is changed. **Note that 'flat' paths are not allowed on this type of storage.**   # noqa: E501

        :param storage_path_type: The storage_path_type of this Glusterfs.  # noqa: E501
        :type: str
        """
        allowed_values = ["canonical"]  # noqa: E501
        if storage_path_type not in allowed_values:
            raise ValueError(
                "Invalid value for `storage_path_type` ({0}), must be one of {1}"  # noqa: E501
                .format(storage_path_type, allowed_values)
            )

        self._storage_path_type = storage_path_type

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
        if issubclass(Glusterfs, dict):
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
        if not isinstance(other, Glusterfs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other