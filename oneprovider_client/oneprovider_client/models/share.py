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

class Share(object):
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
        'share_id': 'str',
        'name': 'str',
        'description': 'str',
        'public_url': 'str',
        'space_id': 'str',
        'root_file_id': 'str',
        'root_file_type': 'FileType',
        'handle_id': 'str'
    }

    attribute_map = {
        'share_id': 'shareId',
        'name': 'name',
        'description': 'description',
        'public_url': 'publicUrl',
        'space_id': 'spaceId',
        'root_file_id': 'rootFileId',
        'root_file_type': 'rootFileType',
        'handle_id': 'handleId'
    }

    def __init__(self, share_id=None, name=None, description=None, public_url=None, space_id=None, root_file_id=None, root_file_type=None, handle_id=None):  # noqa: E501
        """Share - a model defined in Swagger"""  # noqa: E501
        self._share_id = None
        self._name = None
        self._description = None
        self._public_url = None
        self._space_id = None
        self._root_file_id = None
        self._root_file_type = None
        self._handle_id = None
        self.discriminator = None
        self.share_id = share_id
        self.name = name
        self.description = description
        self.public_url = public_url
        self.space_id = space_id
        self.root_file_id = root_file_id
        self.root_file_type = root_file_type
        if handle_id is not None:
            self.handle_id = handle_id

    @property
    def share_id(self):
        """Gets the share_id of this Share.  # noqa: E501

        Share Id.  # noqa: E501

        :return: The share_id of this Share.  # noqa: E501
        :rtype: str
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        """Sets the share_id of this Share.

        Share Id.  # noqa: E501

        :param share_id: The share_id of this Share.  # noqa: E501
        :type: str
        """
        if share_id is None:
            raise ValueError("Invalid value for `share_id`, must not be `None`")  # noqa: E501

        self._share_id = share_id

    @property
    def name(self):
        """Gets the name of this Share.  # noqa: E501

        The name of the share.  # noqa: E501

        :return: The name of this Share.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Share.

        The name of the share.  # noqa: E501

        :param name: The name of this Share.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Share.  # noqa: E501

        Description of the share contents, interpreted as markdown format when displayed in GUI.  # noqa: E501

        :return: The description of this Share.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Share.

        Description of the share contents, interpreted as markdown format when displayed in GUI.  # noqa: E501

        :param description: The description of this Share.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def public_url(self):
        """Gets the public_url of this Share.  # noqa: E501

        The publicly accessible URL for the share.  # noqa: E501

        :return: The public_url of this Share.  # noqa: E501
        :rtype: str
        """
        return self._public_url

    @public_url.setter
    def public_url(self, public_url):
        """Sets the public_url of this Share.

        The publicly accessible URL for the share.  # noqa: E501

        :param public_url: The public_url of this Share.  # noqa: E501
        :type: str
        """
        if public_url is None:
            raise ValueError("Invalid value for `public_url`, must not be `None`")  # noqa: E501

        self._public_url = public_url

    @property
    def space_id(self):
        """Gets the space_id of this Share.  # noqa: E501

        The Id of the space in which the share was created.  # noqa: E501

        :return: The space_id of this Share.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this Share.

        The Id of the space in which the share was created.  # noqa: E501

        :param space_id: The space_id of this Share.  # noqa: E501
        :type: str
        """
        if space_id is None:
            raise ValueError("Invalid value for `space_id`, must not be `None`")  # noqa: E501

        self._space_id = space_id

    @property
    def root_file_id(self):
        """Gets the root_file_id of this Share.  # noqa: E501

        Public Id of shared file or directory, allowing read access to its contents without authentication.  # noqa: E501

        :return: The root_file_id of this Share.  # noqa: E501
        :rtype: str
        """
        return self._root_file_id

    @root_file_id.setter
    def root_file_id(self, root_file_id):
        """Sets the root_file_id of this Share.

        Public Id of shared file or directory, allowing read access to its contents without authentication.  # noqa: E501

        :param root_file_id: The root_file_id of this Share.  # noqa: E501
        :type: str
        """
        if root_file_id is None:
            raise ValueError("Invalid value for `root_file_id`, must not be `None`")  # noqa: E501

        self._root_file_id = root_file_id

    @property
    def root_file_type(self):
        """Gets the root_file_type of this Share.  # noqa: E501


        :return: The root_file_type of this Share.  # noqa: E501
        :rtype: FileType
        """
        return self._root_file_type

    @root_file_type.setter
    def root_file_type(self, root_file_type):
        """Sets the root_file_type of this Share.


        :param root_file_type: The root_file_type of this Share.  # noqa: E501
        :type: FileType
        """
        if root_file_type is None:
            raise ValueError("Invalid value for `root_file_type`, must not be `None`")  # noqa: E501

        self._root_file_type = root_file_type

    @property
    def handle_id(self):
        """Gets the handle_id of this Share.  # noqa: E501

        The Id of open data Handle (e.g. DOI or PID) assigned to this share or null.  # noqa: E501

        :return: The handle_id of this Share.  # noqa: E501
        :rtype: str
        """
        return self._handle_id

    @handle_id.setter
    def handle_id(self, handle_id):
        """Sets the handle_id of this Share.

        The Id of open data Handle (e.g. DOI or PID) assigned to this share or null.  # noqa: E501

        :param handle_id: The handle_id of this Share.  # noqa: E501
        :type: str
        """

        self._handle_id = handle_id

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
        if issubclass(Share, dict):
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
        if not isinstance(other, Share):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
