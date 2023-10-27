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

class Dataset(object):
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
        'state': 'DatasetState',
        'dataset_id': 'str',
        'parent_id': 'str',
        'root_file_id': 'str',
        'root_file_type': 'FileType',
        'root_file_path': 'str',
        'root_file_deleted': 'bool',
        'protection_flags': 'DatasetProtectionFlags',
        'effective_protection_flags': 'DatasetProtectionFlags',
        'creation_time': 'Timestamp',
        'archive_count': 'int'
    }

    attribute_map = {
        'state': 'state',
        'dataset_id': 'datasetId',
        'parent_id': 'parentId',
        'root_file_id': 'rootFileId',
        'root_file_type': 'rootFileType',
        'root_file_path': 'rootFilePath',
        'root_file_deleted': 'rootFileDeleted',
        'protection_flags': 'protectionFlags',
        'effective_protection_flags': 'effectiveProtectionFlags',
        'creation_time': 'creationTime',
        'archive_count': 'archiveCount'
    }

    def __init__(self, state=None, dataset_id=None, parent_id=None, root_file_id=None, root_file_type=None, root_file_path=None, root_file_deleted=None, protection_flags=None, effective_protection_flags=None, creation_time=None, archive_count=None):  # noqa: E501
        """Dataset - a model defined in Swagger"""  # noqa: E501
        self._state = None
        self._dataset_id = None
        self._parent_id = None
        self._root_file_id = None
        self._root_file_type = None
        self._root_file_path = None
        self._root_file_deleted = None
        self._protection_flags = None
        self._effective_protection_flags = None
        self._creation_time = None
        self._archive_count = None
        self.discriminator = None
        self.state = state
        self.dataset_id = dataset_id
        if parent_id is not None:
            self.parent_id = parent_id
        self.root_file_id = root_file_id
        self.root_file_type = root_file_type
        self.root_file_path = root_file_path
        if root_file_deleted is not None:
            self.root_file_deleted = root_file_deleted
        self.protection_flags = protection_flags
        self.effective_protection_flags = effective_protection_flags
        self.creation_time = creation_time
        if archive_count is not None:
            self.archive_count = archive_count

    @property
    def state(self):
        """Gets the state of this Dataset.  # noqa: E501


        :return: The state of this Dataset.  # noqa: E501
        :rtype: DatasetState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Dataset.


        :param state: The state of this Dataset.  # noqa: E501
        :type: DatasetState
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def dataset_id(self):
        """Gets the dataset_id of this Dataset.  # noqa: E501

        Dataset Id.  # noqa: E501

        :return: The dataset_id of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this Dataset.

        Dataset Id.  # noqa: E501

        :param dataset_id: The dataset_id of this Dataset.  # noqa: E501
        :type: str
        """
        if dataset_id is None:
            raise ValueError("Invalid value for `dataset_id`, must not be `None`")  # noqa: E501

        self._dataset_id = dataset_id

    @property
    def parent_id(self):
        """Gets the parent_id of this Dataset.  # noqa: E501

        Parent dataset Id or `null` in case of top dataset.  # noqa: E501

        :return: The parent_id of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this Dataset.

        Parent dataset Id or `null` in case of top dataset.  # noqa: E501

        :param parent_id: The parent_id of this Dataset.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def root_file_id(self):
        """Gets the root_file_id of this Dataset.  # noqa: E501

        Id of file or directory being the dataset root. Once the dataset has been established the root file can no longer be changed. Even after detaching dataset it can be reattached only to the same file and only if it still exists.   # noqa: E501

        :return: The root_file_id of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._root_file_id

    @root_file_id.setter
    def root_file_id(self, root_file_id):
        """Sets the root_file_id of this Dataset.

        Id of file or directory being the dataset root. Once the dataset has been established the root file can no longer be changed. Even after detaching dataset it can be reattached only to the same file and only if it still exists.   # noqa: E501

        :param root_file_id: The root_file_id of this Dataset.  # noqa: E501
        :type: str
        """
        if root_file_id is None:
            raise ValueError("Invalid value for `root_file_id`, must not be `None`")  # noqa: E501

        self._root_file_id = root_file_id

    @property
    def root_file_type(self):
        """Gets the root_file_type of this Dataset.  # noqa: E501


        :return: The root_file_type of this Dataset.  # noqa: E501
        :rtype: FileType
        """
        return self._root_file_type

    @root_file_type.setter
    def root_file_type(self, root_file_type):
        """Sets the root_file_type of this Dataset.


        :param root_file_type: The root_file_type of this Dataset.  # noqa: E501
        :type: FileType
        """
        if root_file_type is None:
            raise ValueError("Invalid value for `root_file_type`, must not be `None`")  # noqa: E501

        self._root_file_type = root_file_type

    @property
    def root_file_path(self):
        """Gets the root_file_path of this Dataset.  # noqa: E501

        Path to the file or directory in the virtual file system. For datasets in `detached` state this field is frozen and shows the value it had at the time of detaching. It is done for archival purposes as file may have been renamed or removed.   # noqa: E501

        :return: The root_file_path of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._root_file_path

    @root_file_path.setter
    def root_file_path(self, root_file_path):
        """Sets the root_file_path of this Dataset.

        Path to the file or directory in the virtual file system. For datasets in `detached` state this field is frozen and shows the value it had at the time of detaching. It is done for archival purposes as file may have been renamed or removed.   # noqa: E501

        :param root_file_path: The root_file_path of this Dataset.  # noqa: E501
        :type: str
        """
        if root_file_path is None:
            raise ValueError("Invalid value for `root_file_path`, must not be `None`")  # noqa: E501

        self._root_file_path = root_file_path

    @property
    def root_file_deleted(self):
        """Gets the root_file_deleted of this Dataset.  # noqa: E501

        Flag informing whether dataset's root file has been deleted.  Only relevant for detached datasets. If the root file has been deleted, it is no longer possible to reattach the dataset.   # noqa: E501

        :return: The root_file_deleted of this Dataset.  # noqa: E501
        :rtype: bool
        """
        return self._root_file_deleted

    @root_file_deleted.setter
    def root_file_deleted(self, root_file_deleted):
        """Sets the root_file_deleted of this Dataset.

        Flag informing whether dataset's root file has been deleted.  Only relevant for detached datasets. If the root file has been deleted, it is no longer possible to reattach the dataset.   # noqa: E501

        :param root_file_deleted: The root_file_deleted of this Dataset.  # noqa: E501
        :type: bool
        """

        self._root_file_deleted = root_file_deleted

    @property
    def protection_flags(self):
        """Gets the protection_flags of this Dataset.  # noqa: E501


        :return: The protection_flags of this Dataset.  # noqa: E501
        :rtype: DatasetProtectionFlags
        """
        return self._protection_flags

    @protection_flags.setter
    def protection_flags(self, protection_flags):
        """Sets the protection_flags of this Dataset.


        :param protection_flags: The protection_flags of this Dataset.  # noqa: E501
        :type: DatasetProtectionFlags
        """
        if protection_flags is None:
            raise ValueError("Invalid value for `protection_flags`, must not be `None`")  # noqa: E501

        self._protection_flags = protection_flags

    @property
    def effective_protection_flags(self):
        """Gets the effective_protection_flags of this Dataset.  # noqa: E501


        :return: The effective_protection_flags of this Dataset.  # noqa: E501
        :rtype: DatasetProtectionFlags
        """
        return self._effective_protection_flags

    @effective_protection_flags.setter
    def effective_protection_flags(self, effective_protection_flags):
        """Sets the effective_protection_flags of this Dataset.


        :param effective_protection_flags: The effective_protection_flags of this Dataset.  # noqa: E501
        :type: DatasetProtectionFlags
        """
        if effective_protection_flags is None:
            raise ValueError("Invalid value for `effective_protection_flags`, must not be `None`")  # noqa: E501

        self._effective_protection_flags = effective_protection_flags

    @property
    def creation_time(self):
        """Gets the creation_time of this Dataset.  # noqa: E501


        :return: The creation_time of this Dataset.  # noqa: E501
        :rtype: Timestamp
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this Dataset.


        :param creation_time: The creation_time of this Dataset.  # noqa: E501
        :type: Timestamp
        """
        if creation_time is None:
            raise ValueError("Invalid value for `creation_time`, must not be `None`")  # noqa: E501

        self._creation_time = creation_time

    @property
    def archive_count(self):
        """Gets the archive_count of this Dataset.  # noqa: E501

        Number of archives created from the dataset.   # noqa: E501

        :return: The archive_count of this Dataset.  # noqa: E501
        :rtype: int
        """
        return self._archive_count

    @archive_count.setter
    def archive_count(self, archive_count):
        """Sets the archive_count of this Dataset.

        Number of archives created from the dataset.   # noqa: E501

        :param archive_count: The archive_count of this Dataset.  # noqa: E501
        :type: int
        """

        self._archive_count = archive_count

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
        if issubclass(Dataset, dict):
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
        if not isinstance(other, Dataset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
