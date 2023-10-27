# coding: utf-8

"""
    Oneprovider

    # Overview  This is the RESTful API definition of Oneprovider component of Onedata data management system [onedata.org](http://onedata.org).  > This API is defined using [Swagger](http://swagger.io/), the JSON specification can be used to automatically generate > client libraries - [swagger.json](../../../swagger/oneprovider/swagger.json).  All paths below are relative to a common Oneprovider basepath which is `/api/v3/oneprovider`, thus a complete example query for 'mode' file attributes would be: ``` https://ONEPROVIDER_HOSTNAME/api/v3/oneprovider/data/$FILE_ID?attribute=mode ``` Please note that currently the default port for Oneprovider instances is `443`.  In addition to REST API, Oneprovider also provides support for [CDMI](http://onedata.org/#/home/documentation/doc/advanced/cdmi.html) protocol.   ## Authentication To use the APIs, the REST client must authenticate with the Oneprovider service and present a proof of authorization to perform a specific operation. This is done using access tokens, which can be generated using the Onedata GUI or Onezone's REST API.  The token is passed in the request header like this: ``` X-Auth-Token: MIIFrzCCA5egAwIBAgIBEzANBgkqhkiG9w0BAQUFADBcMQswCQYDVQQGEwJQTDET... ```  The authorization to perform a specific operation depends on the authenticated user's privileges in the corresponding space, file level permissions (posix, ACL) and caveats (restrictions) inscribed in the provided access token.   ## Data management basics The Onedata system organizes all user data into logical containers called spaces. <!--- TODO VFS-7218 uncomment when the new docs are deployed --> <!--- For more information, please refer to the [documentation](https://onedata.org/#/home/documentation). -->  Files and directories in Onedata can be globally identified using unique File Ids or logical paths. Whenever possible, it is recommended to use File Ids, due to better performance and no need for escaping or encoding.  ### File path All logical paths in Onedata use the slash (`/`) delimiter and must start with a space name: ```lang-none /CMS 1/file.txt /MyExperiment/directory/subdirectory/image.jpg ```  When referencing files by path in the REST API, make sure to urlencode the path in the URL: ```bash {...}/CMS%201/file.txt ```  ### File Id  File Id is a unique, global identifier associated with a file or directory and can be used universally in the REST and CDMI APIs. There are several ways to find out the File Id of given file or directory: <!---  @TODO VFS-7218 remove redundant information and provide a link to the new docs -->  **Web GUI** - click on Information in the file/directory context menu and look for File Id.  **REST API** - use the File Id resolution endpoint. Below example returns the File Id of `/CMS 1/file.txt`, where `CMS 1` is the space name:  ```bash curl -H \"X-Auth-Token: ${ACCESS_TOKEN}\" \\ -X POST \"https://${ONEPROVIDER_DOMAIN}/api/v3/oneprovider/lookup-file-id/CMS%201/file.txt\" {     \"fileId\": \"094576776E667431723230677767776C6B497031394E445F6E3868677873...\" } ```  ### Space Id  Space Id is a unique, global identifier associated with a space and can be used universally in the REST APIs. In order to find out the Space Id:  **Web GUI** - click on Information in the file/directory context menu and look for Space Id.  **REST API** - use the [Get all user spaces](#operation/get_all_spaces) endpoint.  The Space Id can be used interchangeably with the space root directory's File Id in the path-based enpoints.  **Remove specific file relative to the space root** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_ID/path/dir1/file.txt\" # is equivalent to curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_ROOT_FILE_ID/path/dir1/file.txt\" ``` **Remove specific file relative to any parent directory** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$PARENT_FILE_ID/path/dir1/file.txt\" ```   ## API structure  The API is divided into the following sections:  ### Space management These methods provide means for getting basic information about spaces directly from the Oneprovider service, but also allows to define database views.  ### File access and management The API provides capabilities for:   - browsing files in spaces and directories,   - creating and deleting files as well as updating their content   - querying for file attributes, such as 'mode' file permissions and updating them,   - managing custom file metadata (xattrs, JSON, RDF),   - manual registration of files for imported storages.  More information can be found [here](#section/Overview/Data-management-basics).  ### Replica and QoS management These methods allow viewing file replica distribution, requesting file replication (transfers) between Oneproviders, viewing ongoing and historical transfers data, as well as managing QoS requirements that trigger automatic replication according to the QoS rules.  ### Share management Offers methods for creating, modyfying and deleting shares. Shares are files or directories that were made publicly available, so that they can be viewed by everyone through a public URL.  ### Dataset & archive management API for managing datasets - designated files or directories that are used to facilitate building collections of data meaningful for the users with additional features, such as write protection and archivisation mechanisms.  ### Automation Basic API for scheduling and viewing workflow executions.  ### Monitoring The API provides means for subscribing (through HTTP long-polling technique) for file related events such as reads, writes or deletes which are returned as complete file metadata records with sequence numbers representing their current version.  ### Service information Publicly available, basic configuration of the Oneprovider service.  Detailed examples of API usage are available in the documentation of each operation.   # noqa: E501

    OpenAPI spec version: 21.02.3
    Contact: info@onedata.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Configuration(object):
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
        'provider_id': 'str',
        'name': 'str',
        'domain': 'str',
        'onezone_domain': 'str',
        'version': 'str',
        'build': 'str',
        'compatible_onezone_versions': 'list[str]',
        'compatible_oneprovider_versions': 'list[str]',
        'compatible_oneclient_versions': 'list[str]'
    }

    attribute_map = {
        'provider_id': 'providerId',
        'name': 'name',
        'domain': 'domain',
        'onezone_domain': 'onezoneDomain',
        'version': 'version',
        'build': 'build',
        'compatible_onezone_versions': 'compatibleOnezoneVersions',
        'compatible_oneprovider_versions': 'compatibleOneproviderVersions',
        'compatible_oneclient_versions': 'compatibleOneclientVersions'
    }

    def __init__(self, provider_id=None, name=None, domain=None, onezone_domain=None, version=None, build=None, compatible_onezone_versions=None, compatible_oneprovider_versions=None, compatible_oneclient_versions=None):  # noqa: E501
        """Configuration - a model defined in Swagger"""  # noqa: E501
        self._provider_id = None
        self._name = None
        self._domain = None
        self._onezone_domain = None
        self._version = None
        self._build = None
        self._compatible_onezone_versions = None
        self._compatible_oneprovider_versions = None
        self._compatible_oneclient_versions = None
        self.discriminator = None
        if provider_id is not None:
            self.provider_id = provider_id
        if name is not None:
            self.name = name
        if domain is not None:
            self.domain = domain
        if onezone_domain is not None:
            self.onezone_domain = onezone_domain
        if version is not None:
            self.version = version
        if build is not None:
            self.build = build
        if compatible_onezone_versions is not None:
            self.compatible_onezone_versions = compatible_onezone_versions
        if compatible_oneprovider_versions is not None:
            self.compatible_oneprovider_versions = compatible_oneprovider_versions
        if compatible_oneclient_versions is not None:
            self.compatible_oneclient_versions = compatible_oneclient_versions

    @property
    def provider_id(self):
        """Gets the provider_id of this Configuration.  # noqa: E501

        Id of the Oneprovider  # noqa: E501

        :return: The provider_id of this Configuration.  # noqa: E501
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this Configuration.

        Id of the Oneprovider  # noqa: E501

        :param provider_id: The provider_id of this Configuration.  # noqa: E501
        :type: str
        """

        self._provider_id = provider_id

    @property
    def name(self):
        """Gets the name of this Configuration.  # noqa: E501

        Oneprovider's name  # noqa: E501

        :return: The name of this Configuration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Configuration.

        Oneprovider's name  # noqa: E501

        :param name: The name of this Configuration.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def domain(self):
        """Gets the domain of this Configuration.  # noqa: E501

        Oneprovider's domain  # noqa: E501

        :return: The domain of this Configuration.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Configuration.

        Oneprovider's domain  # noqa: E501

        :param domain: The domain of this Configuration.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def onezone_domain(self):
        """Gets the onezone_domain of this Configuration.  # noqa: E501

        Domain of the Onezone where this Oneprovider is registered  # noqa: E501

        :return: The onezone_domain of this Configuration.  # noqa: E501
        :rtype: str
        """
        return self._onezone_domain

    @onezone_domain.setter
    def onezone_domain(self, onezone_domain):
        """Sets the onezone_domain of this Configuration.

        Domain of the Onezone where this Oneprovider is registered  # noqa: E501

        :param onezone_domain: The onezone_domain of this Configuration.  # noqa: E501
        :type: str
        """

        self._onezone_domain = onezone_domain

    @property
    def version(self):
        """Gets the version of this Configuration.  # noqa: E501

        Version of this Oneprovider  # noqa: E501

        :return: The version of this Configuration.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Configuration.

        Version of this Oneprovider  # noqa: E501

        :param version: The version of this Configuration.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def build(self):
        """Gets the build of this Configuration.  # noqa: E501

        Build number of this Oneprovider  # noqa: E501

        :return: The build of this Configuration.  # noqa: E501
        :rtype: str
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this Configuration.

        Build number of this Oneprovider  # noqa: E501

        :param build: The build of this Configuration.  # noqa: E501
        :type: str
        """

        self._build = build

    @property
    def compatible_onezone_versions(self):
        """Gets the compatible_onezone_versions of this Configuration.  # noqa: E501

        List of compatible Onezone versions  # noqa: E501

        :return: The compatible_onezone_versions of this Configuration.  # noqa: E501
        :rtype: list[str]
        """
        return self._compatible_onezone_versions

    @compatible_onezone_versions.setter
    def compatible_onezone_versions(self, compatible_onezone_versions):
        """Sets the compatible_onezone_versions of this Configuration.

        List of compatible Onezone versions  # noqa: E501

        :param compatible_onezone_versions: The compatible_onezone_versions of this Configuration.  # noqa: E501
        :type: list[str]
        """

        self._compatible_onezone_versions = compatible_onezone_versions

    @property
    def compatible_oneprovider_versions(self):
        """Gets the compatible_oneprovider_versions of this Configuration.  # noqa: E501

        List of compatible Oneprovider versions  # noqa: E501

        :return: The compatible_oneprovider_versions of this Configuration.  # noqa: E501
        :rtype: list[str]
        """
        return self._compatible_oneprovider_versions

    @compatible_oneprovider_versions.setter
    def compatible_oneprovider_versions(self, compatible_oneprovider_versions):
        """Sets the compatible_oneprovider_versions of this Configuration.

        List of compatible Oneprovider versions  # noqa: E501

        :param compatible_oneprovider_versions: The compatible_oneprovider_versions of this Configuration.  # noqa: E501
        :type: list[str]
        """

        self._compatible_oneprovider_versions = compatible_oneprovider_versions

    @property
    def compatible_oneclient_versions(self):
        """Gets the compatible_oneclient_versions of this Configuration.  # noqa: E501

        List of compatible Oneclient versions  # noqa: E501

        :return: The compatible_oneclient_versions of this Configuration.  # noqa: E501
        :rtype: list[str]
        """
        return self._compatible_oneclient_versions

    @compatible_oneclient_versions.setter
    def compatible_oneclient_versions(self, compatible_oneclient_versions):
        """Sets the compatible_oneclient_versions of this Configuration.

        List of compatible Oneclient versions  # noqa: E501

        :param compatible_oneclient_versions: The compatible_oneclient_versions of this Configuration.  # noqa: E501
        :type: list[str]
        """

        self._compatible_oneclient_versions = compatible_oneclient_versions

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
        if issubclass(Configuration, dict):
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
        if not isinstance(other, Configuration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
