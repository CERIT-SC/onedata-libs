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

class AutoStorageImportConfig(object):
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
        'max_depth': 'int',
        'sync_acl': 'bool',
        'continuous_scan': 'bool',
        'scan_interval': 'int',
        'detect_modifications': 'bool',
        'detect_deletions': 'bool'
    }

    attribute_map = {
        'max_depth': 'maxDepth',
        'sync_acl': 'syncAcl',
        'continuous_scan': 'continuousScan',
        'scan_interval': 'scanInterval',
        'detect_modifications': 'detectModifications',
        'detect_deletions': 'detectDeletions'
    }

    def __init__(self, max_depth=None, sync_acl=False, continuous_scan=False, scan_interval=None, detect_modifications=True, detect_deletions=True):  # noqa: E501
        """AutoStorageImportConfig - a model defined in Swagger"""  # noqa: E501
        self._max_depth = None
        self._sync_acl = None
        self._continuous_scan = None
        self._scan_interval = None
        self._detect_modifications = None
        self._detect_deletions = None
        self.discriminator = None
        if max_depth is not None:
            self.max_depth = max_depth
        if sync_acl is not None:
            self.sync_acl = sync_acl
        if continuous_scan is not None:
            self.continuous_scan = continuous_scan
        if scan_interval is not None:
            self.scan_interval = scan_interval
        if detect_modifications is not None:
            self.detect_modifications = detect_modifications
        if detect_deletions is not None:
            self.detect_deletions = detect_deletions

    @property
    def max_depth(self):
        """Gets the max_depth of this AutoStorageImportConfig.  # noqa: E501

        Maximum depth of filesystem tree that will be traversed during the scan.   # noqa: E501

        :return: The max_depth of this AutoStorageImportConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_depth

    @max_depth.setter
    def max_depth(self, max_depth):
        """Sets the max_depth of this AutoStorageImportConfig.

        Maximum depth of filesystem tree that will be traversed during the scan.   # noqa: E501

        :param max_depth: The max_depth of this AutoStorageImportConfig.  # noqa: E501
        :type: int
        """

        self._max_depth = max_depth

    @property
    def sync_acl(self):
        """Gets the sync_acl of this AutoStorageImportConfig.  # noqa: E501

        Flag that enables synchronization of NFSv4 ACLs.   # noqa: E501

        :return: The sync_acl of this AutoStorageImportConfig.  # noqa: E501
        :rtype: bool
        """
        return self._sync_acl

    @sync_acl.setter
    def sync_acl(self, sync_acl):
        """Sets the sync_acl of this AutoStorageImportConfig.

        Flag that enables synchronization of NFSv4 ACLs.   # noqa: E501

        :param sync_acl: The sync_acl of this AutoStorageImportConfig.  # noqa: E501
        :type: bool
        """

        self._sync_acl = sync_acl

    @property
    def continuous_scan(self):
        """Gets the continuous_scan of this AutoStorageImportConfig.  # noqa: E501

        With this option enabled the storage will be scanned periodically and direct changes on the storage will be reflected in the assigned Onedata space (upon the consecutive scan).   # noqa: E501

        :return: The continuous_scan of this AutoStorageImportConfig.  # noqa: E501
        :rtype: bool
        """
        return self._continuous_scan

    @continuous_scan.setter
    def continuous_scan(self, continuous_scan):
        """Sets the continuous_scan of this AutoStorageImportConfig.

        With this option enabled the storage will be scanned periodically and direct changes on the storage will be reflected in the assigned Onedata space (upon the consecutive scan).   # noqa: E501

        :param continuous_scan: The continuous_scan of this AutoStorageImportConfig.  # noqa: E501
        :type: bool
        """

        self._continuous_scan = continuous_scan

    @property
    def scan_interval(self):
        """Gets the scan_interval of this AutoStorageImportConfig.  # noqa: E501

        Period between subsequent scans in seconds (counted from end of one scan till beginning of the following). This parameter is relevant only for continuous scans.   # noqa: E501

        :return: The scan_interval of this AutoStorageImportConfig.  # noqa: E501
        :rtype: int
        """
        return self._scan_interval

    @scan_interval.setter
    def scan_interval(self, scan_interval):
        """Sets the scan_interval of this AutoStorageImportConfig.

        Period between subsequent scans in seconds (counted from end of one scan till beginning of the following). This parameter is relevant only for continuous scans.   # noqa: E501

        :param scan_interval: The scan_interval of this AutoStorageImportConfig.  # noqa: E501
        :type: int
        """

        self._scan_interval = scan_interval

    @property
    def detect_modifications(self):
        """Gets the detect_modifications of this AutoStorageImportConfig.  # noqa: E501

        Flag determining that modifications of files on the synchronized storage will be detected. If disabled, the storage will be treated as immutable (only creations and deletions of files on storage will be detected). This parameter is relevant only for continuous scans.   # noqa: E501

        :return: The detect_modifications of this AutoStorageImportConfig.  # noqa: E501
        :rtype: bool
        """
        return self._detect_modifications

    @detect_modifications.setter
    def detect_modifications(self, detect_modifications):
        """Sets the detect_modifications of this AutoStorageImportConfig.

        Flag determining that modifications of files on the synchronized storage will be detected. If disabled, the storage will be treated as immutable (only creations and deletions of files on storage will be detected). This parameter is relevant only for continuous scans.   # noqa: E501

        :param detect_modifications: The detect_modifications of this AutoStorageImportConfig.  # noqa: E501
        :type: bool
        """

        self._detect_modifications = detect_modifications

    @property
    def detect_deletions(self):
        """Gets the detect_deletions of this AutoStorageImportConfig.  # noqa: E501

        Flag determining that deletions of files from the synchronized storage will be detected. This parameter is relevant only for continuous scans.   # noqa: E501

        :return: The detect_deletions of this AutoStorageImportConfig.  # noqa: E501
        :rtype: bool
        """
        return self._detect_deletions

    @detect_deletions.setter
    def detect_deletions(self, detect_deletions):
        """Sets the detect_deletions of this AutoStorageImportConfig.

        Flag determining that deletions of files from the synchronized storage will be detected. This parameter is relevant only for continuous scans.   # noqa: E501

        :param detect_deletions: The detect_deletions of this AutoStorageImportConfig.  # noqa: E501
        :type: bool
        """

        self._detect_deletions = detect_deletions

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
        if issubclass(AutoStorageImportConfig, dict):
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
        if not isinstance(other, AutoStorageImportConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
