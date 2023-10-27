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

class S3Modify(StorageModifyDetails):
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
        'hostname': 'str',
        'bucket_name': 'str',
        'access_key': 'str',
        'secret_key': 'str',
        'signature_version': 'int',
        'maximum_canonical_object_size': 'int',
        'file_mode': 'str',
        'dir_mode': 'str'
    }
    if hasattr(StorageModifyDetails, "swagger_types"):
        swagger_types.update(StorageModifyDetails.swagger_types)

    attribute_map = {
        'type': 'type',
        'hostname': 'hostname',
        'bucket_name': 'bucketName',
        'access_key': 'accessKey',
        'secret_key': 'secretKey',
        'signature_version': 'signatureVersion',
        'maximum_canonical_object_size': 'maximumCanonicalObjectSize',
        'file_mode': 'fileMode',
        'dir_mode': 'dirMode'
    }
    if hasattr(StorageModifyDetails, "attribute_map"):
        attribute_map.update(StorageModifyDetails.attribute_map)

    def __init__(self, type=None, hostname=None, bucket_name=None, access_key=None, secret_key=None, signature_version=None, maximum_canonical_object_size=None, file_mode=None, dir_mode=None, *args, **kwargs):  # noqa: E501
        """S3Modify - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._hostname = None
        self._bucket_name = None
        self._access_key = None
        self._secret_key = None
        self._signature_version = None
        self._maximum_canonical_object_size = None
        self._file_mode = None
        self._dir_mode = None
        self.discriminator = None
        self.type = type
        if hostname is not None:
            self.hostname = hostname
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if access_key is not None:
            self.access_key = access_key
        if secret_key is not None:
            self.secret_key = secret_key
        if signature_version is not None:
            self.signature_version = signature_version
        if maximum_canonical_object_size is not None:
            self.maximum_canonical_object_size = maximum_canonical_object_size
        if file_mode is not None:
            self.file_mode = file_mode
        if dir_mode is not None:
            self.dir_mode = dir_mode
        StorageModifyDetails.__init__(self, *args, **kwargs)

    @property
    def type(self):
        """Gets the type of this S3Modify.  # noqa: E501

        The type of storage.  `type = \"s3\"`  [Amazon S3](http://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) compatible storage.   # noqa: E501

        :return: The type of this S3Modify.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this S3Modify.

        The type of storage.  `type = \"s3\"`  [Amazon S3](http://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) compatible storage.   # noqa: E501

        :param type: The type of this S3Modify.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["s3"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def hostname(self):
        """Gets the hostname of this S3Modify.  # noqa: E501

        The hostname of a machine where S3 storage is installed.  # noqa: E501

        :return: The hostname of this S3Modify.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this S3Modify.

        The hostname of a machine where S3 storage is installed.  # noqa: E501

        :param hostname: The hostname of this S3Modify.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def bucket_name(self):
        """Gets the bucket_name of this S3Modify.  # noqa: E501

        The storage bucket name.  # noqa: E501

        :return: The bucket_name of this S3Modify.  # noqa: E501
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this S3Modify.

        The storage bucket name.  # noqa: E501

        :param bucket_name: The bucket_name of this S3Modify.  # noqa: E501
        :type: str
        """

        self._bucket_name = bucket_name

    @property
    def access_key(self):
        """Gets the access_key of this S3Modify.  # noqa: E501

        The access key to the S3 storage.  # noqa: E501

        :return: The access_key of this S3Modify.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this S3Modify.

        The access key to the S3 storage.  # noqa: E501

        :param access_key: The access_key of this S3Modify.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    @property
    def secret_key(self):
        """Gets the secret_key of this S3Modify.  # noqa: E501

        The secret key to the S3 storage.  # noqa: E501

        :return: The secret_key of this S3Modify.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this S3Modify.

        The secret key to the S3 storage.  # noqa: E501

        :param secret_key: The secret_key of this S3Modify.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def signature_version(self):
        """Gets the signature_version of this S3Modify.  # noqa: E501

        The version of signature used to sign requests. Only version 4 is supported.   # noqa: E501

        :return: The signature_version of this S3Modify.  # noqa: E501
        :rtype: int
        """
        return self._signature_version

    @signature_version.setter
    def signature_version(self, signature_version):
        """Sets the signature_version of this S3Modify.

        The version of signature used to sign requests. Only version 4 is supported.   # noqa: E501

        :param signature_version: The signature_version of this S3Modify.  # noqa: E501
        :type: int
        """

        self._signature_version = signature_version

    @property
    def maximum_canonical_object_size(self):
        """Gets the maximum_canonical_object_size of this S3Modify.  # noqa: E501

        Defines the maximum size for objects, which can be modified on the S3 storage in `canonical` path mode. In this mode, entire file needs to be downloaded to memory, modified and uploaded back, which is impractical for large files (default 64 MiB).   # noqa: E501

        :return: The maximum_canonical_object_size of this S3Modify.  # noqa: E501
        :rtype: int
        """
        return self._maximum_canonical_object_size

    @maximum_canonical_object_size.setter
    def maximum_canonical_object_size(self, maximum_canonical_object_size):
        """Sets the maximum_canonical_object_size of this S3Modify.

        Defines the maximum size for objects, which can be modified on the S3 storage in `canonical` path mode. In this mode, entire file needs to be downloaded to memory, modified and uploaded back, which is impractical for large files (default 64 MiB).   # noqa: E501

        :param maximum_canonical_object_size: The maximum_canonical_object_size of this S3Modify.  # noqa: E501
        :type: int
        """

        self._maximum_canonical_object_size = maximum_canonical_object_size

    @property
    def file_mode(self):
        """Gets the file_mode of this S3Modify.  # noqa: E501

        Defines the file permissions, which files imported from S3 storage will have in Onedata. Values should be provided in octal format e.g. `0644`.   # noqa: E501

        :return: The file_mode of this S3Modify.  # noqa: E501
        :rtype: str
        """
        return self._file_mode

    @file_mode.setter
    def file_mode(self, file_mode):
        """Sets the file_mode of this S3Modify.

        Defines the file permissions, which files imported from S3 storage will have in Onedata. Values should be provided in octal format e.g. `0644`.   # noqa: E501

        :param file_mode: The file_mode of this S3Modify.  # noqa: E501
        :type: str
        """

        self._file_mode = file_mode

    @property
    def dir_mode(self):
        """Gets the dir_mode of this S3Modify.  # noqa: E501

        Defines the directory mode which directories imported from S3 storage will have in Onedata. Values should be provided in octal format e.g. `0775`.   # noqa: E501

        :return: The dir_mode of this S3Modify.  # noqa: E501
        :rtype: str
        """
        return self._dir_mode

    @dir_mode.setter
    def dir_mode(self, dir_mode):
        """Sets the dir_mode of this S3Modify.

        Defines the directory mode which directories imported from S3 storage will have in Onedata. Values should be provided in octal format e.g. `0775`.   # noqa: E501

        :param dir_mode: The dir_mode of this S3Modify.  # noqa: E501
        :type: str
        """

        self._dir_mode = dir_mode

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
        if issubclass(S3Modify, dict):
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
        if not isinstance(other, S3Modify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
