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

class FileRegistrationRequest(object):
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
        'space_id': 'str',
        'storage_id': 'str',
        'storage_file_id': 'str',
        'destination_path': 'str',
        'size': 'int',
        'mode': 'str',
        'atime': 'int',
        'mtime': 'int',
        'ctime': 'int',
        'uid': 'str',
        'gid': 'str',
        'xattrs': 'dict(str, str)',
        'json': 'dict(str, str)',
        'rdf': 'str',
        'auto_detect_attributes': 'bool'
    }

    attribute_map = {
        'space_id': 'spaceId',
        'storage_id': 'storageId',
        'storage_file_id': 'storageFileId',
        'destination_path': 'destinationPath',
        'size': 'size',
        'mode': 'mode',
        'atime': 'atime',
        'mtime': 'mtime',
        'ctime': 'ctime',
        'uid': 'uid',
        'gid': 'gid',
        'xattrs': 'xattrs',
        'json': 'json',
        'rdf': 'rdf',
        'auto_detect_attributes': 'autoDetectAttributes'
    }

    def __init__(self, space_id=None, storage_id=None, storage_file_id=None, destination_path=None, size=None, mode=None, atime=None, mtime=None, ctime=None, uid=None, gid=None, xattrs=None, json=None, rdf=None, auto_detect_attributes=True):  # noqa: E501
        """FileRegistrationRequest - a model defined in Swagger"""  # noqa: E501
        self._space_id = None
        self._storage_id = None
        self._storage_file_id = None
        self._destination_path = None
        self._size = None
        self._mode = None
        self._atime = None
        self._mtime = None
        self._ctime = None
        self._uid = None
        self._gid = None
        self._xattrs = None
        self._json = None
        self._rdf = None
        self._auto_detect_attributes = None
        self.discriminator = None
        if space_id is not None:
            self.space_id = space_id
        if storage_id is not None:
            self.storage_id = storage_id
        if storage_file_id is not None:
            self.storage_file_id = storage_file_id
        if destination_path is not None:
            self.destination_path = destination_path
        if size is not None:
            self.size = size
        if mode is not None:
            self.mode = mode
        if atime is not None:
            self.atime = atime
        if mtime is not None:
            self.mtime = mtime
        if ctime is not None:
            self.ctime = ctime
        if uid is not None:
            self.uid = uid
        if gid is not None:
            self.gid = gid
        if xattrs is not None:
            self.xattrs = xattrs
        if json is not None:
            self.json = json
        if rdf is not None:
            self.rdf = rdf
        if auto_detect_attributes is not None:
            self.auto_detect_attributes = auto_detect_attributes

    @property
    def space_id(self):
        """Gets the space_id of this FileRegistrationRequest.  # noqa: E501

        Id of the space in which the file will be registered - the space must be supported by the storage hosting the file (`storageId`). The space support must have `manual import mode`.   # noqa: E501

        :return: The space_id of this FileRegistrationRequest.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this FileRegistrationRequest.

        Id of the space in which the file will be registered - the space must be supported by the storage hosting the file (`storageId`). The space support must have `manual import mode`.   # noqa: E501

        :param space_id: The space_id of this FileRegistrationRequest.  # noqa: E501
        :type: str
        """

        self._space_id = space_id

    @property
    def storage_id(self):
        """Gets the storage_id of this FileRegistrationRequest.  # noqa: E501

        Id of the storage hosting the file - the storage must support the target space (`spaceId`). The storage must be configured as an `imported storage` with `canonical` path type.   # noqa: E501

        :return: The storage_id of this FileRegistrationRequest.  # noqa: E501
        :rtype: str
        """
        return self._storage_id

    @storage_id.setter
    def storage_id(self, storage_id):
        """Sets the storage_id of this FileRegistrationRequest.

        Id of the storage hosting the file - the storage must support the target space (`spaceId`). The storage must be configured as an `imported storage` with `canonical` path type.   # noqa: E501

        :param storage_id: The storage_id of this FileRegistrationRequest.  # noqa: E501
        :type: str
        """

        self._storage_id = storage_id

    @property
    def storage_file_id(self):
        """Gets the storage_file_id of this FileRegistrationRequest.  # noqa: E501

        Identifier of the file on storage, relevant for given storage backend:    * path on POSIX-compatible or canonical object storages, e.g. `/dir/file.txt`    * URL on HTTP based storages, e.g. `https://www.example.org/data/21/run123.tar`   # noqa: E501

        :return: The storage_file_id of this FileRegistrationRequest.  # noqa: E501
        :rtype: str
        """
        return self._storage_file_id

    @storage_file_id.setter
    def storage_file_id(self, storage_file_id):
        """Sets the storage_file_id of this FileRegistrationRequest.

        Identifier of the file on storage, relevant for given storage backend:    * path on POSIX-compatible or canonical object storages, e.g. `/dir/file.txt`    * URL on HTTP based storages, e.g. `https://www.example.org/data/21/run123.tar`   # noqa: E501

        :param storage_file_id: The storage_file_id of this FileRegistrationRequest.  # noqa: E501
        :type: str
        """

        self._storage_file_id = storage_file_id

    @property
    def destination_path(self):
        """Gets the destination_path of this FileRegistrationRequest.  # noqa: E501

        An absolute path in space where file should be created.  # noqa: E501

        :return: The destination_path of this FileRegistrationRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination_path

    @destination_path.setter
    def destination_path(self, destination_path):
        """Sets the destination_path of this FileRegistrationRequest.

        An absolute path in space where file should be created.  # noqa: E501

        :param destination_path: The destination_path of this FileRegistrationRequest.  # noqa: E501
        :type: str
        """

        self._destination_path = destination_path

    @property
    def size(self):
        """Gets the size of this FileRegistrationRequest.  # noqa: E501

        Size of the file in bytes. If not passed, it will be acquired from storage. If storage does not support the `stat` operation or equivalent used for acquiring files metadata, registration will fail if this value is missing.   # noqa: E501

        :return: The size of this FileRegistrationRequest.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FileRegistrationRequest.

        Size of the file in bytes. If not passed, it will be acquired from storage. If storage does not support the `stat` operation or equivalent used for acquiring files metadata, registration will fail if this value is missing.   # noqa: E501

        :param size: The size of this FileRegistrationRequest.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def mode(self):
        """Gets the mode of this FileRegistrationRequest.  # noqa: E501

        User defined POSIX file permissions in octal format. If not passed, it will be acquired from storage or default `\"664\"` mode will be used.   # noqa: E501

        :return: The mode of this FileRegistrationRequest.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this FileRegistrationRequest.

        User defined POSIX file permissions in octal format. If not passed, it will be acquired from storage or default `\"664\"` mode will be used.   # noqa: E501

        :param mode: The mode of this FileRegistrationRequest.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def atime(self):
        """Gets the atime of this FileRegistrationRequest.  # noqa: E501

        User defined last access timestamp (in seconds). If not passed, it will be acquired from storage or current timestamp will be used.   # noqa: E501

        :return: The atime of this FileRegistrationRequest.  # noqa: E501
        :rtype: int
        """
        return self._atime

    @atime.setter
    def atime(self, atime):
        """Sets the atime of this FileRegistrationRequest.

        User defined last access timestamp (in seconds). If not passed, it will be acquired from storage or current timestamp will be used.   # noqa: E501

        :param atime: The atime of this FileRegistrationRequest.  # noqa: E501
        :type: int
        """

        self._atime = atime

    @property
    def mtime(self):
        """Gets the mtime of this FileRegistrationRequest.  # noqa: E501

        User defined last modification timestamp (in seconds). If not passed, it will be acquired from storage or current timestamp will be used.   # noqa: E501

        :return: The mtime of this FileRegistrationRequest.  # noqa: E501
        :rtype: int
        """
        return self._mtime

    @mtime.setter
    def mtime(self, mtime):
        """Sets the mtime of this FileRegistrationRequest.

        User defined last modification timestamp (in seconds). If not passed, it will be acquired from storage or current timestamp will be used.   # noqa: E501

        :param mtime: The mtime of this FileRegistrationRequest.  # noqa: E501
        :type: int
        """

        self._mtime = mtime

    @property
    def ctime(self):
        """Gets the ctime of this FileRegistrationRequest.  # noqa: E501

        User defined last attributes modification timestamp (in seconds). If not passed, it will be acquired from storage or current timestamp will be used.   # noqa: E501

        :return: The ctime of this FileRegistrationRequest.  # noqa: E501
        :rtype: int
        """
        return self._ctime

    @ctime.setter
    def ctime(self, ctime):
        """Sets the ctime of this FileRegistrationRequest.

        User defined last attributes modification timestamp (in seconds). If not passed, it will be acquired from storage or current timestamp will be used.   # noqa: E501

        :param ctime: The ctime of this FileRegistrationRequest.  # noqa: E501
        :type: int
        """

        self._ctime = ctime

    @property
    def uid(self):
        """Gets the uid of this FileRegistrationRequest.  # noqa: E501

        User defined of the Id of the owner of this file on storage. If not passed, it will be acquired from storage or `0` will be used. This value will be mapped, using LUMA DB, to acquire Onedata user Id of the file owner.   # noqa: E501

        :return: The uid of this FileRegistrationRequest.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this FileRegistrationRequest.

        User defined of the Id of the owner of this file on storage. If not passed, it will be acquired from storage or `0` will be used. This value will be mapped, using LUMA DB, to acquire Onedata user Id of the file owner.   # noqa: E501

        :param uid: The uid of this FileRegistrationRequest.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def gid(self):
        """Gets the gid of this FileRegistrationRequest.  # noqa: E501

        User defined Id of the group owner of this file on storage. If not passed, it will be acquired from storage or `0` will be used. This value will be used as display GID in `getattr` operation.   # noqa: E501

        :return: The gid of this FileRegistrationRequest.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this FileRegistrationRequest.

        User defined Id of the group owner of this file on storage. If not passed, it will be acquired from storage or `0` will be used. This value will be used as display GID in `getattr` operation.   # noqa: E501

        :param gid: The gid of this FileRegistrationRequest.  # noqa: E501
        :type: str
        """

        self._gid = gid

    @property
    def xattrs(self):
        """Gets the xattrs of this FileRegistrationRequest.  # noqa: E501

        Map with extended attributes key-value pairs which will be attached to newly created file.  # noqa: E501

        :return: The xattrs of this FileRegistrationRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._xattrs

    @xattrs.setter
    def xattrs(self, xattrs):
        """Sets the xattrs of this FileRegistrationRequest.

        Map with extended attributes key-value pairs which will be attached to newly created file.  # noqa: E501

        :param xattrs: The xattrs of this FileRegistrationRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._xattrs = xattrs

    @property
    def json(self):
        """Gets the json of this FileRegistrationRequest.  # noqa: E501

        Map with custom JSON metadata which will be attached to newly created file.  # noqa: E501

        :return: The json of this FileRegistrationRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this FileRegistrationRequest.

        Map with custom JSON metadata which will be attached to newly created file.  # noqa: E501

        :param json: The json of this FileRegistrationRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._json = json

    @property
    def rdf(self):
        """Gets the rdf of this FileRegistrationRequest.  # noqa: E501

        Base64 encoded RDF metadata which will be attached to newly created file.  # noqa: E501

        :return: The rdf of this FileRegistrationRequest.  # noqa: E501
        :rtype: str
        """
        return self._rdf

    @rdf.setter
    def rdf(self, rdf):
        """Sets the rdf of this FileRegistrationRequest.

        Base64 encoded RDF metadata which will be attached to newly created file.  # noqa: E501

        :param rdf: The rdf of this FileRegistrationRequest.  # noqa: E501
        :type: str
        """

        self._rdf = rdf

    @property
    def auto_detect_attributes(self):
        """Gets the auto_detect_attributes of this FileRegistrationRequest.  # noqa: E501

        Flag which determines whether additional `stat` operation (or equivalent) should be performed on the storage to automatically detect file attributes - they will be used if not provided explicitly in the request. The detection also ensures that the file exists - it is performed if the flag is set to `true`, even if all attributes are provided. If this flag is set to `false`, default attributes are used if not provided explicitly. The only exception is the `size` attribute, which is mandatory. The registration request will fail if `autoDetectAttributes` is set to `false` and `size` is not provided. It is possible to register a file that does not exist on storage if `autoDetectAttributes` is set to `false`. Such file will be visible in Onedata but not accessible.   # noqa: E501

        :return: The auto_detect_attributes of this FileRegistrationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_detect_attributes

    @auto_detect_attributes.setter
    def auto_detect_attributes(self, auto_detect_attributes):
        """Sets the auto_detect_attributes of this FileRegistrationRequest.

        Flag which determines whether additional `stat` operation (or equivalent) should be performed on the storage to automatically detect file attributes - they will be used if not provided explicitly in the request. The detection also ensures that the file exists - it is performed if the flag is set to `true`, even if all attributes are provided. If this flag is set to `false`, default attributes are used if not provided explicitly. The only exception is the `size` attribute, which is mandatory. The registration request will fail if `autoDetectAttributes` is set to `false` and `size` is not provided. It is possible to register a file that does not exist on storage if `autoDetectAttributes` is set to `false`. Such file will be visible in Onedata but not accessible.   # noqa: E501

        :param auto_detect_attributes: The auto_detect_attributes of this FileRegistrationRequest.  # noqa: E501
        :type: bool
        """

        self._auto_detect_attributes = auto_detect_attributes

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
        if issubclass(FileRegistrationRequest, dict):
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
        if not isinstance(other, FileRegistrationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
