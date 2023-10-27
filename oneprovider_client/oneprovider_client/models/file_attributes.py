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

class FileAttributes(object):
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
        'name': 'str',
        'type': 'FileType',
        'mode': 'str',
        'size': 'int',
        'atime': 'int',
        'mtime': 'int',
        'ctime': 'int',
        'owner_id': 'str',
        'file_id': 'str',
        'parent_id': 'str',
        'provider_id': 'str',
        'storage_user_id': 'str',
        'storage_group_id': 'str',
        'shares': 'list[str]',
        'hardlinks_count': 'int',
        'index': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'mode': 'mode',
        'size': 'size',
        'atime': 'atime',
        'mtime': 'mtime',
        'ctime': 'ctime',
        'owner_id': 'owner_id',
        'file_id': 'file_id',
        'parent_id': 'parent_id',
        'provider_id': 'provider_id',
        'storage_user_id': 'storage_user_id',
        'storage_group_id': 'storage_group_id',
        'shares': 'shares',
        'hardlinks_count': 'hardlinks_count',
        'index': 'index'
    }

    def __init__(self, name=None, type=None, mode=None, size=None, atime=None, mtime=None, ctime=None, owner_id=None, file_id=None, parent_id=None, provider_id=None, storage_user_id=None, storage_group_id=None, shares=None, hardlinks_count=None, index=None):  # noqa: E501
        """FileAttributes - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._type = None
        self._mode = None
        self._size = None
        self._atime = None
        self._mtime = None
        self._ctime = None
        self._owner_id = None
        self._file_id = None
        self._parent_id = None
        self._provider_id = None
        self._storage_user_id = None
        self._storage_group_id = None
        self._shares = None
        self._hardlinks_count = None
        self._index = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if mode is not None:
            self.mode = mode
        if size is not None:
            self.size = size
        if atime is not None:
            self.atime = atime
        if mtime is not None:
            self.mtime = mtime
        if ctime is not None:
            self.ctime = ctime
        if owner_id is not None:
            self.owner_id = owner_id
        if file_id is not None:
            self.file_id = file_id
        if parent_id is not None:
            self.parent_id = parent_id
        if provider_id is not None:
            self.provider_id = provider_id
        if storage_user_id is not None:
            self.storage_user_id = storage_user_id
        if storage_group_id is not None:
            self.storage_group_id = storage_group_id
        if shares is not None:
            self.shares = shares
        if hardlinks_count is not None:
            self.hardlinks_count = hardlinks_count
        if index is not None:
            self.index = index

    @property
    def name(self):
        """Gets the name of this FileAttributes.  # noqa: E501

        File name.  # noqa: E501

        :return: The name of this FileAttributes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileAttributes.

        File name.  # noqa: E501

        :param name: The name of this FileAttributes.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this FileAttributes.  # noqa: E501


        :return: The type of this FileAttributes.  # noqa: E501
        :rtype: FileType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FileAttributes.


        :param type: The type of this FileAttributes.  # noqa: E501
        :type: FileType
        """

        self._type = type

    @property
    def mode(self):
        """Gets the mode of this FileAttributes.  # noqa: E501

        POSIX file permissions as string expressing octal notation.  # noqa: E501

        :return: The mode of this FileAttributes.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this FileAttributes.

        POSIX file permissions as string expressing octal notation.  # noqa: E501

        :param mode: The mode of this FileAttributes.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def size(self):
        """Gets the size of this FileAttributes.  # noqa: E501

        Size of the file in bytes.  # noqa: E501

        :return: The size of this FileAttributes.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FileAttributes.

        Size of the file in bytes.  # noqa: E501

        :param size: The size of this FileAttributes.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def atime(self):
        """Gets the atime of this FileAttributes.  # noqa: E501

        Last access timestamp (in seconds).  # noqa: E501

        :return: The atime of this FileAttributes.  # noqa: E501
        :rtype: int
        """
        return self._atime

    @atime.setter
    def atime(self, atime):
        """Sets the atime of this FileAttributes.

        Last access timestamp (in seconds).  # noqa: E501

        :param atime: The atime of this FileAttributes.  # noqa: E501
        :type: int
        """

        self._atime = atime

    @property
    def mtime(self):
        """Gets the mtime of this FileAttributes.  # noqa: E501

        Last modification timestamp (in seconds).  # noqa: E501

        :return: The mtime of this FileAttributes.  # noqa: E501
        :rtype: int
        """
        return self._mtime

    @mtime.setter
    def mtime(self, mtime):
        """Sets the mtime of this FileAttributes.

        Last modification timestamp (in seconds).  # noqa: E501

        :param mtime: The mtime of this FileAttributes.  # noqa: E501
        :type: int
        """

        self._mtime = mtime

    @property
    def ctime(self):
        """Gets the ctime of this FileAttributes.  # noqa: E501

        Last attributes modification timestamp (in seconds).  # noqa: E501

        :return: The ctime of this FileAttributes.  # noqa: E501
        :rtype: int
        """
        return self._ctime

    @ctime.setter
    def ctime(self, ctime):
        """Sets the ctime of this FileAttributes.

        Last attributes modification timestamp (in seconds).  # noqa: E501

        :param ctime: The ctime of this FileAttributes.  # noqa: E501
        :type: int
        """

        self._ctime = ctime

    @property
    def owner_id(self):
        """Gets the owner_id of this FileAttributes.  # noqa: E501

        Id of the owner of this file.  # noqa: E501

        :return: The owner_id of this FileAttributes.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this FileAttributes.

        Id of the owner of this file.  # noqa: E501

        :param owner_id: The owner_id of this FileAttributes.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def file_id(self):
        """Gets the file_id of this FileAttributes.  # noqa: E501

        Id of the file.  # noqa: E501

        :return: The file_id of this FileAttributes.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this FileAttributes.

        Id of the file.  # noqa: E501

        :param file_id: The file_id of this FileAttributes.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def parent_id(self):
        """Gets the parent_id of this FileAttributes.  # noqa: E501

        Id of the parent directory or `null` in case of file tree root.  # noqa: E501

        :return: The parent_id of this FileAttributes.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this FileAttributes.

        Id of the parent directory or `null` in case of file tree root.  # noqa: E501

        :param parent_id: The parent_id of this FileAttributes.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def provider_id(self):
        """Gets the provider_id of this FileAttributes.  # noqa: E501

        Id of the provider on which this file was created.  # noqa: E501

        :return: The provider_id of this FileAttributes.  # noqa: E501
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this FileAttributes.

        Id of the provider on which this file was created.  # noqa: E501

        :param provider_id: The provider_id of this FileAttributes.  # noqa: E501
        :type: str
        """

        self._provider_id = provider_id

    @property
    def storage_user_id(self):
        """Gets the storage_user_id of this FileAttributes.  # noqa: E501

        Id of the owner of this file on storage.  # noqa: E501

        :return: The storage_user_id of this FileAttributes.  # noqa: E501
        :rtype: str
        """
        return self._storage_user_id

    @storage_user_id.setter
    def storage_user_id(self, storage_user_id):
        """Sets the storage_user_id of this FileAttributes.

        Id of the owner of this file on storage.  # noqa: E501

        :param storage_user_id: The storage_user_id of this FileAttributes.  # noqa: E501
        :type: str
        """

        self._storage_user_id = storage_user_id

    @property
    def storage_group_id(self):
        """Gets the storage_group_id of this FileAttributes.  # noqa: E501

        Id of the group owner of this file on storage.  # noqa: E501

        :return: The storage_group_id of this FileAttributes.  # noqa: E501
        :rtype: str
        """
        return self._storage_group_id

    @storage_group_id.setter
    def storage_group_id(self, storage_group_id):
        """Sets the storage_group_id of this FileAttributes.

        Id of the group owner of this file on storage.  # noqa: E501

        :param storage_group_id: The storage_group_id of this FileAttributes.  # noqa: E501
        :type: str
        """

        self._storage_group_id = storage_group_id

    @property
    def shares(self):
        """Gets the shares of this FileAttributes.  # noqa: E501

        The list of Ids of shares created for this file.  # noqa: E501

        :return: The shares of this FileAttributes.  # noqa: E501
        :rtype: list[str]
        """
        return self._shares

    @shares.setter
    def shares(self, shares):
        """Sets the shares of this FileAttributes.

        The list of Ids of shares created for this file.  # noqa: E501

        :param shares: The shares of this FileAttributes.  # noqa: E501
        :type: list[str]
        """

        self._shares = shares

    @property
    def hardlinks_count(self):
        """Gets the hardlinks_count of this FileAttributes.  # noqa: E501

        The number of hard links (including this one) associated with this file.   # noqa: E501

        :return: The hardlinks_count of this FileAttributes.  # noqa: E501
        :rtype: int
        """
        return self._hardlinks_count

    @hardlinks_count.setter
    def hardlinks_count(self, hardlinks_count):
        """Sets the hardlinks_count of this FileAttributes.

        The number of hard links (including this one) associated with this file.   # noqa: E501

        :param hardlinks_count: The hardlinks_count of this FileAttributes.  # noqa: E501
        :type: int
        """

        self._hardlinks_count = hardlinks_count

    @property
    def index(self):
        """Gets the index of this FileAttributes.  # noqa: E501

        File index that can be provided as starting point when listing files.   # noqa: E501

        :return: The index of this FileAttributes.  # noqa: E501
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this FileAttributes.

        File index that can be provided as starting point when listing files.   # noqa: E501

        :param index: The index of this FileAttributes.  # noqa: E501
        :type: str
        """

        self._index = index

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
        if issubclass(FileAttributes, dict):
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
        if not isinstance(other, FileAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
