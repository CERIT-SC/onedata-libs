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

class AutoStorageImportStats(object):
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
        'queue_length': 'TimeStats',
        'created_files': 'TimeStats',
        'modified_files': 'TimeStats',
        'deleted_files': 'TimeStats'
    }

    attribute_map = {
        'queue_length': 'queueLength',
        'created_files': 'createdFiles',
        'modified_files': 'modifiedFiles',
        'deleted_files': 'deletedFiles'
    }

    def __init__(self, queue_length=None, created_files=None, modified_files=None, deleted_files=None):  # noqa: E501
        """AutoStorageImportStats - a model defined in Swagger"""  # noqa: E501
        self._queue_length = None
        self._created_files = None
        self._modified_files = None
        self._deleted_files = None
        self.discriminator = None
        if queue_length is not None:
            self.queue_length = queue_length
        if created_files is not None:
            self.created_files = created_files
        if modified_files is not None:
            self.modified_files = modified_files
        if deleted_files is not None:
            self.deleted_files = deleted_files

    @property
    def queue_length(self):
        """Gets the queue_length of this AutoStorageImportStats.  # noqa: E501


        :return: The queue_length of this AutoStorageImportStats.  # noqa: E501
        :rtype: TimeStats
        """
        return self._queue_length

    @queue_length.setter
    def queue_length(self, queue_length):
        """Sets the queue_length of this AutoStorageImportStats.


        :param queue_length: The queue_length of this AutoStorageImportStats.  # noqa: E501
        :type: TimeStats
        """

        self._queue_length = queue_length

    @property
    def created_files(self):
        """Gets the created_files of this AutoStorageImportStats.  # noqa: E501


        :return: The created_files of this AutoStorageImportStats.  # noqa: E501
        :rtype: TimeStats
        """
        return self._created_files

    @created_files.setter
    def created_files(self, created_files):
        """Sets the created_files of this AutoStorageImportStats.


        :param created_files: The created_files of this AutoStorageImportStats.  # noqa: E501
        :type: TimeStats
        """

        self._created_files = created_files

    @property
    def modified_files(self):
        """Gets the modified_files of this AutoStorageImportStats.  # noqa: E501


        :return: The modified_files of this AutoStorageImportStats.  # noqa: E501
        :rtype: TimeStats
        """
        return self._modified_files

    @modified_files.setter
    def modified_files(self, modified_files):
        """Sets the modified_files of this AutoStorageImportStats.


        :param modified_files: The modified_files of this AutoStorageImportStats.  # noqa: E501
        :type: TimeStats
        """

        self._modified_files = modified_files

    @property
    def deleted_files(self):
        """Gets the deleted_files of this AutoStorageImportStats.  # noqa: E501


        :return: The deleted_files of this AutoStorageImportStats.  # noqa: E501
        :rtype: TimeStats
        """
        return self._deleted_files

    @deleted_files.setter
    def deleted_files(self, deleted_files):
        """Sets the deleted_files of this AutoStorageImportStats.


        :param deleted_files: The deleted_files of this AutoStorageImportStats.  # noqa: E501
        :type: TimeStats
        """

        self._deleted_files = deleted_files

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
        if issubclass(AutoStorageImportStats, dict):
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
        if not isinstance(other, AutoStorageImportStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
