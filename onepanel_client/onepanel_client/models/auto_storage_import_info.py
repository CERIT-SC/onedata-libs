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

class AutoStorageImportInfo(object):
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
        'status': 'str',
        'start': 'int',
        'stop': 'int',
        'created_files': 'int',
        'modified_files': 'int',
        'deleted_files': 'int',
        'unmodified_files': 'int',
        'failed_files': 'int',
        'next_scan': 'int',
        'total_scans': 'int'
    }

    attribute_map = {
        'status': 'status',
        'start': 'start',
        'stop': 'stop',
        'created_files': 'createdFiles',
        'modified_files': 'modifiedFiles',
        'deleted_files': 'deletedFiles',
        'unmodified_files': 'unmodifiedFiles',
        'failed_files': 'failedFiles',
        'next_scan': 'nextScan',
        'total_scans': 'totalScans'
    }

    def __init__(self, status=None, start=None, stop=None, created_files=None, modified_files=None, deleted_files=None, unmodified_files=None, failed_files=None, next_scan=None, total_scans=None):  # noqa: E501
        """AutoStorageImportInfo - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._start = None
        self._stop = None
        self._created_files = None
        self._modified_files = None
        self._deleted_files = None
        self._unmodified_files = None
        self._failed_files = None
        self._next_scan = None
        self._total_scans = None
        self.discriminator = None
        self.status = status
        self.start = start
        self.stop = stop
        self.created_files = created_files
        self.modified_files = modified_files
        self.deleted_files = deleted_files
        self.unmodified_files = unmodified_files
        self.failed_files = failed_files
        if next_scan is not None:
            self.next_scan = next_scan
        self.total_scans = total_scans

    @property
    def status(self):
        """Gets the status of this AutoStorageImportInfo.  # noqa: E501

        Describes status of current (or last finished) auto storage import scan in given space.  # noqa: E501

        :return: The status of this AutoStorageImportInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AutoStorageImportInfo.

        Describes status of current (or last finished) auto storage import scan in given space.  # noqa: E501

        :param status: The status of this AutoStorageImportInfo.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["enqueued", "running", "aborting", "completed", "failed", "aborted"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def start(self):
        """Gets the start of this AutoStorageImportInfo.  # noqa: E501

        Time at which current (or last finished) scan has been started.  # noqa: E501

        :return: The start of this AutoStorageImportInfo.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this AutoStorageImportInfo.

        Time at which current (or last finished) scan has been started.  # noqa: E501

        :param start: The start of this AutoStorageImportInfo.  # noqa: E501
        :type: int
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def stop(self):
        """Gets the stop of this AutoStorageImportInfo.  # noqa: E501

        Time at which current (or last finished) scan has been stopped.  # noqa: E501

        :return: The stop of this AutoStorageImportInfo.  # noqa: E501
        :rtype: int
        """
        return self._stop

    @stop.setter
    def stop(self, stop):
        """Sets the stop of this AutoStorageImportInfo.

        Time at which current (or last finished) scan has been stopped.  # noqa: E501

        :param stop: The stop of this AutoStorageImportInfo.  # noqa: E501
        :type: int
        """
        if stop is None:
            raise ValueError("Invalid value for `stop`, must not be `None`")  # noqa: E501

        self._stop = stop

    @property
    def created_files(self):
        """Gets the created_files of this AutoStorageImportInfo.  # noqa: E501

        Counter of created files (both directories and regular files) that has been detected during current (or last finished) scan.  # noqa: E501

        :return: The created_files of this AutoStorageImportInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_files

    @created_files.setter
    def created_files(self, created_files):
        """Sets the created_files of this AutoStorageImportInfo.

        Counter of created files (both directories and regular files) that has been detected during current (or last finished) scan.  # noqa: E501

        :param created_files: The created_files of this AutoStorageImportInfo.  # noqa: E501
        :type: int
        """
        if created_files is None:
            raise ValueError("Invalid value for `created_files`, must not be `None`")  # noqa: E501

        self._created_files = created_files

    @property
    def modified_files(self):
        """Gets the modified_files of this AutoStorageImportInfo.  # noqa: E501

        Counter of modified files (both directories and regular files) that has been detected during current (or last finished) scan.  # noqa: E501

        :return: The modified_files of this AutoStorageImportInfo.  # noqa: E501
        :rtype: int
        """
        return self._modified_files

    @modified_files.setter
    def modified_files(self, modified_files):
        """Sets the modified_files of this AutoStorageImportInfo.

        Counter of modified files (both directories and regular files) that has been detected during current (or last finished) scan.  # noqa: E501

        :param modified_files: The modified_files of this AutoStorageImportInfo.  # noqa: E501
        :type: int
        """
        if modified_files is None:
            raise ValueError("Invalid value for `modified_files`, must not be `None`")  # noqa: E501

        self._modified_files = modified_files

    @property
    def deleted_files(self):
        """Gets the deleted_files of this AutoStorageImportInfo.  # noqa: E501

        Counter of deleted files (both directories and regular files) that has been detected during current (or last finished) scan.  # noqa: E501

        :return: The deleted_files of this AutoStorageImportInfo.  # noqa: E501
        :rtype: int
        """
        return self._deleted_files

    @deleted_files.setter
    def deleted_files(self, deleted_files):
        """Sets the deleted_files of this AutoStorageImportInfo.

        Counter of deleted files (both directories and regular files) that has been detected during current (or last finished) scan.  # noqa: E501

        :param deleted_files: The deleted_files of this AutoStorageImportInfo.  # noqa: E501
        :type: int
        """
        if deleted_files is None:
            raise ValueError("Invalid value for `deleted_files`, must not be `None`")  # noqa: E501

        self._deleted_files = deleted_files

    @property
    def unmodified_files(self):
        """Gets the unmodified_files of this AutoStorageImportInfo.  # noqa: E501

        Counter of unmodified files (both directories and regular files) that has been detected during current (or last finished) scan.  # noqa: E501

        :return: The unmodified_files of this AutoStorageImportInfo.  # noqa: E501
        :rtype: int
        """
        return self._unmodified_files

    @unmodified_files.setter
    def unmodified_files(self, unmodified_files):
        """Sets the unmodified_files of this AutoStorageImportInfo.

        Counter of unmodified files (both directories and regular files) that has been detected during current (or last finished) scan.  # noqa: E501

        :param unmodified_files: The unmodified_files of this AutoStorageImportInfo.  # noqa: E501
        :type: int
        """
        if unmodified_files is None:
            raise ValueError("Invalid value for `unmodified_files`, must not be `None`")  # noqa: E501

        self._unmodified_files = unmodified_files

    @property
    def failed_files(self):
        """Gets the failed_files of this AutoStorageImportInfo.  # noqa: E501

        Counter of files (both directories and regular files) for which the processing has failed during current (or last finished) scan.  # noqa: E501

        :return: The failed_files of this AutoStorageImportInfo.  # noqa: E501
        :rtype: int
        """
        return self._failed_files

    @failed_files.setter
    def failed_files(self, failed_files):
        """Sets the failed_files of this AutoStorageImportInfo.

        Counter of files (both directories and regular files) for which the processing has failed during current (or last finished) scan.  # noqa: E501

        :param failed_files: The failed_files of this AutoStorageImportInfo.  # noqa: E501
        :type: int
        """
        if failed_files is None:
            raise ValueError("Invalid value for `failed_files`, must not be `None`")  # noqa: E501

        self._failed_files = failed_files

    @property
    def next_scan(self):
        """Gets the next_scan of this AutoStorageImportInfo.  # noqa: E501

        Estimated time at which next scan will be enqueued.  # noqa: E501

        :return: The next_scan of this AutoStorageImportInfo.  # noqa: E501
        :rtype: int
        """
        return self._next_scan

    @next_scan.setter
    def next_scan(self, next_scan):
        """Sets the next_scan of this AutoStorageImportInfo.

        Estimated time at which next scan will be enqueued.  # noqa: E501

        :param next_scan: The next_scan of this AutoStorageImportInfo.  # noqa: E501
        :type: int
        """

        self._next_scan = next_scan

    @property
    def total_scans(self):
        """Gets the total_scans of this AutoStorageImportInfo.  # noqa: E501

        Total number of performed scans.  # noqa: E501

        :return: The total_scans of this AutoStorageImportInfo.  # noqa: E501
        :rtype: int
        """
        return self._total_scans

    @total_scans.setter
    def total_scans(self, total_scans):
        """Sets the total_scans of this AutoStorageImportInfo.

        Total number of performed scans.  # noqa: E501

        :param total_scans: The total_scans of this AutoStorageImportInfo.  # noqa: E501
        :type: int
        """
        if total_scans is None:
            raise ValueError("Invalid value for `total_scans`, must not be `None`")  # noqa: E501

        self._total_scans = total_scans

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
        if issubclass(AutoStorageImportInfo, dict):
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
        if not isinstance(other, AutoStorageImportInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other