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

class ClusterConfigurationDetails(object):
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
        'master': 'str',
        'hosts': 'list[str]',
        'databases': 'DatabaseHosts',
        'managers': 'ManagerHosts',
        'workers': 'WorkerHosts'
    }

    attribute_map = {
        'master': 'master',
        'hosts': 'hosts',
        'databases': 'databases',
        'managers': 'managers',
        'workers': 'workers'
    }

    def __init__(self, master=None, hosts=None, databases=None, managers=None, workers=None):  # noqa: E501
        """ClusterConfigurationDetails - a model defined in Swagger"""  # noqa: E501
        self._master = None
        self._hosts = None
        self._databases = None
        self._managers = None
        self._workers = None
        self.discriminator = None
        self.master = master
        self.hosts = hosts
        self.databases = databases
        self.managers = managers
        self.workers = workers

    @property
    def master(self):
        """Gets the master of this ClusterConfigurationDetails.  # noqa: E501

        Host responsible for deploying cluster and coordinating cluster restarts.  # noqa: E501

        :return: The master of this ClusterConfigurationDetails.  # noqa: E501
        :rtype: str
        """
        return self._master

    @master.setter
    def master(self, master):
        """Sets the master of this ClusterConfigurationDetails.

        Host responsible for deploying cluster and coordinating cluster restarts.  # noqa: E501

        :param master: The master of this ClusterConfigurationDetails.  # noqa: E501
        :type: str
        """
        if master is None:
            raise ValueError("Invalid value for `master`, must not be `None`")  # noqa: E501

        self._master = master

    @property
    def hosts(self):
        """Gets the hosts of this ClusterConfigurationDetails.  # noqa: E501

        List of hosts belonging to the Onepanel cluster.  # noqa: E501

        :return: The hosts of this ClusterConfigurationDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this ClusterConfigurationDetails.

        List of hosts belonging to the Onepanel cluster.  # noqa: E501

        :param hosts: The hosts of this ClusterConfigurationDetails.  # noqa: E501
        :type: list[str]
        """
        if hosts is None:
            raise ValueError("Invalid value for `hosts`, must not be `None`")  # noqa: E501

        self._hosts = hosts

    @property
    def databases(self):
        """Gets the databases of this ClusterConfigurationDetails.  # noqa: E501


        :return: The databases of this ClusterConfigurationDetails.  # noqa: E501
        :rtype: DatabaseHosts
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this ClusterConfigurationDetails.


        :param databases: The databases of this ClusterConfigurationDetails.  # noqa: E501
        :type: DatabaseHosts
        """
        if databases is None:
            raise ValueError("Invalid value for `databases`, must not be `None`")  # noqa: E501

        self._databases = databases

    @property
    def managers(self):
        """Gets the managers of this ClusterConfigurationDetails.  # noqa: E501


        :return: The managers of this ClusterConfigurationDetails.  # noqa: E501
        :rtype: ManagerHosts
        """
        return self._managers

    @managers.setter
    def managers(self, managers):
        """Sets the managers of this ClusterConfigurationDetails.


        :param managers: The managers of this ClusterConfigurationDetails.  # noqa: E501
        :type: ManagerHosts
        """
        if managers is None:
            raise ValueError("Invalid value for `managers`, must not be `None`")  # noqa: E501

        self._managers = managers

    @property
    def workers(self):
        """Gets the workers of this ClusterConfigurationDetails.  # noqa: E501


        :return: The workers of this ClusterConfigurationDetails.  # noqa: E501
        :rtype: WorkerHosts
        """
        return self._workers

    @workers.setter
    def workers(self, workers):
        """Sets the workers of this ClusterConfigurationDetails.


        :param workers: The workers of this ClusterConfigurationDetails.  # noqa: E501
        :type: WorkerHosts
        """
        if workers is None:
            raise ValueError("Invalid value for `workers`, must not be `None`")  # noqa: E501

        self._workers = workers

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
        if issubclass(ClusterConfigurationDetails, dict):
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
        if not isinstance(other, ClusterConfigurationDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other