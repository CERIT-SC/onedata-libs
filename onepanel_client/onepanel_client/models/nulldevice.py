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

class Nulldevice(StorageGetDetails):
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
        'latency_min': 'int',
        'latency_max': 'int',
        'timeout_probability': 'float',
        'filter': 'str',
        'storage_path_type': 'str',
        'simulated_filesystem_parameters': 'str',
        'simulated_filesystem_grow_speed': 'float',
        'enable_data_verification': 'bool'
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
        'latency_min': 'latencyMin',
        'latency_max': 'latencyMax',
        'timeout_probability': 'timeoutProbability',
        'filter': 'filter',
        'storage_path_type': 'storagePathType',
        'simulated_filesystem_parameters': 'simulatedFilesystemParameters',
        'simulated_filesystem_grow_speed': 'simulatedFilesystemGrowSpeed',
        'enable_data_verification': 'enableDataVerification'
    }
    if hasattr(StorageGetDetails, "attribute_map"):
        attribute_map.update(StorageGetDetails.attribute_map)

    def __init__(self, type=None, timeout=None, skip_storage_detection=False, luma_feed='auto', luma_feed_url=None, luma_feed_api_key=None, qos_parameters=None, imported_storage=False, archive_storage=False, readonly=False, latency_min=None, latency_max=None, timeout_probability=0.0, filter='*', storage_path_type='canonical', simulated_filesystem_parameters='', simulated_filesystem_grow_speed=0.0, enable_data_verification=False, *args, **kwargs):  # noqa: E501
        """Nulldevice - a model defined in Swagger"""  # noqa: E501
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
        self._latency_min = None
        self._latency_max = None
        self._timeout_probability = None
        self._filter = None
        self._storage_path_type = None
        self._simulated_filesystem_parameters = None
        self._simulated_filesystem_grow_speed = None
        self._enable_data_verification = None
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
        if latency_min is not None:
            self.latency_min = latency_min
        if latency_max is not None:
            self.latency_max = latency_max
        if timeout_probability is not None:
            self.timeout_probability = timeout_probability
        if filter is not None:
            self.filter = filter
        if storage_path_type is not None:
            self.storage_path_type = storage_path_type
        if simulated_filesystem_parameters is not None:
            self.simulated_filesystem_parameters = simulated_filesystem_parameters
        if simulated_filesystem_grow_speed is not None:
            self.simulated_filesystem_grow_speed = simulated_filesystem_grow_speed
        if enable_data_verification is not None:
            self.enable_data_verification = enable_data_verification
        StorageGetDetails.__init__(self, *args, **kwargs)

    @property
    def type(self):
        """Gets the type of this Nulldevice.  # noqa: E501

        The type of storage.  `type = \"nulldevice\"`  POSIX compatible storage which emulates behavior of `/dev/null` on local filesystem. Allows running various performance tests, which are not impacted by actual storage latency. Skip storage detection option is obligatory for this type of storage.   # noqa: E501

        :return: The type of this Nulldevice.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Nulldevice.

        The type of storage.  `type = \"nulldevice\"`  POSIX compatible storage which emulates behavior of `/dev/null` on local filesystem. Allows running various performance tests, which are not impacted by actual storage latency. Skip storage detection option is obligatory for this type of storage.   # noqa: E501

        :param type: The type of this Nulldevice.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["nulldevice"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def timeout(self):
        """Gets the timeout of this Nulldevice.  # noqa: E501

        Storage operation timeout in milliseconds.  # noqa: E501

        :return: The timeout of this Nulldevice.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this Nulldevice.

        Storage operation timeout in milliseconds.  # noqa: E501

        :param timeout: The timeout of this Nulldevice.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def skip_storage_detection(self):
        """Gets the skip_storage_detection of this Nulldevice.  # noqa: E501

        If true, detecting whether storage is directly accessible by the Oneclient will not be performed. This option should be set to true on readonly storages.   # noqa: E501

        :return: The skip_storage_detection of this Nulldevice.  # noqa: E501
        :rtype: bool
        """
        return self._skip_storage_detection

    @skip_storage_detection.setter
    def skip_storage_detection(self, skip_storage_detection):
        """Sets the skip_storage_detection of this Nulldevice.

        If true, detecting whether storage is directly accessible by the Oneclient will not be performed. This option should be set to true on readonly storages.   # noqa: E501

        :param skip_storage_detection: The skip_storage_detection of this Nulldevice.  # noqa: E501
        :type: bool
        """

        self._skip_storage_detection = skip_storage_detection

    @property
    def luma_feed(self):
        """Gets the luma_feed of this Nulldevice.  # noqa: E501

        Type of feed for LUMA DB. Feed is a source of user/group mappings used to populate the LUMA DB. For more info please read: https://onedata.org/#/home/documentation/doc/administering_onedata/luma.html   # noqa: E501

        :return: The luma_feed of this Nulldevice.  # noqa: E501
        :rtype: str
        """
        return self._luma_feed

    @luma_feed.setter
    def luma_feed(self, luma_feed):
        """Sets the luma_feed of this Nulldevice.

        Type of feed for LUMA DB. Feed is a source of user/group mappings used to populate the LUMA DB. For more info please read: https://onedata.org/#/home/documentation/doc/administering_onedata/luma.html   # noqa: E501

        :param luma_feed: The luma_feed of this Nulldevice.  # noqa: E501
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
        """Gets the luma_feed_url of this Nulldevice.  # noqa: E501

        URL of external feed for LUMA DB. Relevant only if lumaFeed equals `external`.  # noqa: E501

        :return: The luma_feed_url of this Nulldevice.  # noqa: E501
        :rtype: str
        """
        return self._luma_feed_url

    @luma_feed_url.setter
    def luma_feed_url(self, luma_feed_url):
        """Sets the luma_feed_url of this Nulldevice.

        URL of external feed for LUMA DB. Relevant only if lumaFeed equals `external`.  # noqa: E501

        :param luma_feed_url: The luma_feed_url of this Nulldevice.  # noqa: E501
        :type: str
        """

        self._luma_feed_url = luma_feed_url

    @property
    def luma_feed_api_key(self):
        """Gets the luma_feed_api_key of this Nulldevice.  # noqa: E501

        API key checked by external service used as feed for LUMA DB. Relevant only if lumaFeed equals `external`.   # noqa: E501

        :return: The luma_feed_api_key of this Nulldevice.  # noqa: E501
        :rtype: str
        """
        return self._luma_feed_api_key

    @luma_feed_api_key.setter
    def luma_feed_api_key(self, luma_feed_api_key):
        """Sets the luma_feed_api_key of this Nulldevice.

        API key checked by external service used as feed for LUMA DB. Relevant only if lumaFeed equals `external`.   # noqa: E501

        :param luma_feed_api_key: The luma_feed_api_key of this Nulldevice.  # noqa: E501
        :type: str
        """

        self._luma_feed_api_key = luma_feed_api_key

    @property
    def qos_parameters(self):
        """Gets the qos_parameters of this Nulldevice.  # noqa: E501

        Map with key-value pairs used for describing storage QoS parameters.  # noqa: E501

        :return: The qos_parameters of this Nulldevice.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._qos_parameters

    @qos_parameters.setter
    def qos_parameters(self, qos_parameters):
        """Sets the qos_parameters of this Nulldevice.

        Map with key-value pairs used for describing storage QoS parameters.  # noqa: E501

        :param qos_parameters: The qos_parameters of this Nulldevice.  # noqa: E501
        :type: dict(str, str)
        """

        self._qos_parameters = qos_parameters

    @property
    def imported_storage(self):
        """Gets the imported_storage of this Nulldevice.  # noqa: E501

        Defines whether storage contains existing data to be imported.   # noqa: E501

        :return: The imported_storage of this Nulldevice.  # noqa: E501
        :rtype: bool
        """
        return self._imported_storage

    @imported_storage.setter
    def imported_storage(self, imported_storage):
        """Sets the imported_storage of this Nulldevice.

        Defines whether storage contains existing data to be imported.   # noqa: E501

        :param imported_storage: The imported_storage of this Nulldevice.  # noqa: E501
        :type: bool
        """

        self._imported_storage = imported_storage

    @property
    def archive_storage(self):
        """Gets the archive_storage of this Nulldevice.  # noqa: E501

        Defines whether storage supports long-term dataset archiving.   # noqa: E501

        :return: The archive_storage of this Nulldevice.  # noqa: E501
        :rtype: bool
        """
        return self._archive_storage

    @archive_storage.setter
    def archive_storage(self, archive_storage):
        """Sets the archive_storage of this Nulldevice.

        Defines whether storage supports long-term dataset archiving.   # noqa: E501

        :param archive_storage: The archive_storage of this Nulldevice.  # noqa: E501
        :type: bool
        """

        self._archive_storage = archive_storage

    @property
    def readonly(self):
        """Gets the readonly of this Nulldevice.  # noqa: E501

        Defines whether the storage is readonly. If enabled, Oneprovider will block any operation that writes, modifies or deletes data on the storage. Such storage can only be used to import data into the space. Mandatory to ensure proper behaviour if the backend storage is actually configured as readonly. This option is available only for imported storages.   # noqa: E501

        :return: The readonly of this Nulldevice.  # noqa: E501
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        """Sets the readonly of this Nulldevice.

        Defines whether the storage is readonly. If enabled, Oneprovider will block any operation that writes, modifies or deletes data on the storage. Such storage can only be used to import data into the space. Mandatory to ensure proper behaviour if the backend storage is actually configured as readonly. This option is available only for imported storages.   # noqa: E501

        :param readonly: The readonly of this Nulldevice.  # noqa: E501
        :type: bool
        """

        self._readonly = readonly

    @property
    def latency_min(self):
        """Gets the latency_min of this Nulldevice.  # noqa: E501

        Minimum latency in milliseconds, which should be simulated for selected operations.   # noqa: E501

        :return: The latency_min of this Nulldevice.  # noqa: E501
        :rtype: int
        """
        return self._latency_min

    @latency_min.setter
    def latency_min(self, latency_min):
        """Sets the latency_min of this Nulldevice.

        Minimum latency in milliseconds, which should be simulated for selected operations.   # noqa: E501

        :param latency_min: The latency_min of this Nulldevice.  # noqa: E501
        :type: int
        """

        self._latency_min = latency_min

    @property
    def latency_max(self):
        """Gets the latency_max of this Nulldevice.  # noqa: E501

        Maximum latency in milliseconds, which should be simulated for selected operations.   # noqa: E501

        :return: The latency_max of this Nulldevice.  # noqa: E501
        :rtype: int
        """
        return self._latency_max

    @latency_max.setter
    def latency_max(self, latency_max):
        """Sets the latency_max of this Nulldevice.

        Maximum latency in milliseconds, which should be simulated for selected operations.   # noqa: E501

        :param latency_max: The latency_max of this Nulldevice.  # noqa: E501
        :type: int
        """

        self._latency_max = latency_max

    @property
    def timeout_probability(self):
        """Gets the timeout_probability of this Nulldevice.  # noqa: E501

        Probability (0.0, 1.0), with which an operation should return a timeout error.   # noqa: E501

        :return: The timeout_probability of this Nulldevice.  # noqa: E501
        :rtype: float
        """
        return self._timeout_probability

    @timeout_probability.setter
    def timeout_probability(self, timeout_probability):
        """Sets the timeout_probability of this Nulldevice.

        Probability (0.0, 1.0), with which an operation should return a timeout error.   # noqa: E501

        :param timeout_probability: The timeout_probability of this Nulldevice.  # noqa: E501
        :type: float
        """

        self._timeout_probability = timeout_probability

    @property
    def filter(self):
        """Gets the filter of this Nulldevice.  # noqa: E501

        Comma-separated list of filesystem operations, for which latency and timeout should be simulated. Empty or '*' mean all operations will be affected.   # noqa: E501

        :return: The filter of this Nulldevice.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this Nulldevice.

        Comma-separated list of filesystem operations, for which latency and timeout should be simulated. Empty or '*' mean all operations will be affected.   # noqa: E501

        :param filter: The filter of this Nulldevice.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def storage_path_type(self):
        """Gets the storage_path_type of this Nulldevice.  # noqa: E501

        Determines how the logical file paths will be mapped on the storage. 'canonical' paths reflect the logical file names and directory structure, however each rename operation will require renaming the files on the storage. 'flat' paths are based on unique file UUID's and do not require on-storage rename when logical file name is changed.   # noqa: E501

        :return: The storage_path_type of this Nulldevice.  # noqa: E501
        :rtype: str
        """
        return self._storage_path_type

    @storage_path_type.setter
    def storage_path_type(self, storage_path_type):
        """Sets the storage_path_type of this Nulldevice.

        Determines how the logical file paths will be mapped on the storage. 'canonical' paths reflect the logical file names and directory structure, however each rename operation will require renaming the files on the storage. 'flat' paths are based on unique file UUID's and do not require on-storage rename when logical file name is changed.   # noqa: E501

        :param storage_path_type: The storage_path_type of this Nulldevice.  # noqa: E501
        :type: str
        """

        self._storage_path_type = storage_path_type

    @property
    def simulated_filesystem_parameters(self):
        """Gets the simulated_filesystem_parameters of this Nulldevice.  # noqa: E501

        Specifies the parameters for a simulated null device filesystem. For example `2-2:2-2:0-1` will generate a filesystem tree which has 2 directories (`0` and `1`) and 2 files (`2` and `3`) in the root of the filesystem, each of these directories will have 2 subdirectories (`0` and `1`) and 2 files (`2` and `3`) and each of these subdirectories has only a single file (`0`). In order to specify the size of generated files, a size in bytes needs to be added as the last component of the parameter specification, for example `2-2:2-2:0-1:1048576`. Default empty string disables the simulated filesystem feature.   # noqa: E501

        :return: The simulated_filesystem_parameters of this Nulldevice.  # noqa: E501
        :rtype: str
        """
        return self._simulated_filesystem_parameters

    @simulated_filesystem_parameters.setter
    def simulated_filesystem_parameters(self, simulated_filesystem_parameters):
        """Sets the simulated_filesystem_parameters of this Nulldevice.

        Specifies the parameters for a simulated null device filesystem. For example `2-2:2-2:0-1` will generate a filesystem tree which has 2 directories (`0` and `1`) and 2 files (`2` and `3`) in the root of the filesystem, each of these directories will have 2 subdirectories (`0` and `1`) and 2 files (`2` and `3`) and each of these subdirectories has only a single file (`0`). In order to specify the size of generated files, a size in bytes needs to be added as the last component of the parameter specification, for example `2-2:2-2:0-1:1048576`. Default empty string disables the simulated filesystem feature.   # noqa: E501

        :param simulated_filesystem_parameters: The simulated_filesystem_parameters of this Nulldevice.  # noqa: E501
        :type: str
        """

        self._simulated_filesystem_parameters = simulated_filesystem_parameters

    @property
    def simulated_filesystem_grow_speed(self):
        """Gets the simulated_filesystem_grow_speed of this Nulldevice.  # noqa: E501

        Determines the simulated filesystem grow rate. Default 0.0 value will cause all the files and directories defined by the `simulatedFilesystemParameters` specification to be visible immediately. For example value of 0.01 will increase the number of the visible filesystem entries by 1 file per 100 seconds, while 100.0 will increase it by 100 files per second.   # noqa: E501

        :return: The simulated_filesystem_grow_speed of this Nulldevice.  # noqa: E501
        :rtype: float
        """
        return self._simulated_filesystem_grow_speed

    @simulated_filesystem_grow_speed.setter
    def simulated_filesystem_grow_speed(self, simulated_filesystem_grow_speed):
        """Sets the simulated_filesystem_grow_speed of this Nulldevice.

        Determines the simulated filesystem grow rate. Default 0.0 value will cause all the files and directories defined by the `simulatedFilesystemParameters` specification to be visible immediately. For example value of 0.01 will increase the number of the visible filesystem entries by 1 file per 100 seconds, while 100.0 will increase it by 100 files per second.   # noqa: E501

        :param simulated_filesystem_grow_speed: The simulated_filesystem_grow_speed of this Nulldevice.  # noqa: E501
        :type: float
        """

        self._simulated_filesystem_grow_speed = simulated_filesystem_grow_speed

    @property
    def enable_data_verification(self):
        """Gets the enable_data_verification of this Nulldevice.  # noqa: E501

        Enables data verification for `read` and `write` operations. Read operations will always return a predictable pattern of characters based on `offset` and `size`, and `write` operations will fail with I/O error, if the input data does not match the pattern at a given `offset`.   # noqa: E501

        :return: The enable_data_verification of this Nulldevice.  # noqa: E501
        :rtype: bool
        """
        return self._enable_data_verification

    @enable_data_verification.setter
    def enable_data_verification(self, enable_data_verification):
        """Sets the enable_data_verification of this Nulldevice.

        Enables data verification for `read` and `write` operations. Read operations will always return a predictable pattern of characters based on `offset` and `size`, and `write` operations will fail with I/O error, if the input data does not match the pattern at a given `offset`.   # noqa: E501

        :param enable_data_verification: The enable_data_verification of this Nulldevice.  # noqa: E501
        :type: bool
        """

        self._enable_data_verification = enable_data_verification

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
        if issubclass(Nulldevice, dict):
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
        if not isinstance(other, Nulldevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
