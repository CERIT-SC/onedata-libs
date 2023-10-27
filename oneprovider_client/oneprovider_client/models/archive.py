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

class Archive(object):
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
        'archive_id': 'str',
        'state': 'ArchiveState',
        'dataset_id': 'str',
        'root_directory_id': 'str',
        'creation_time': 'Timestamp',
        'config': 'ArchiveConfig',
        'description': 'ArchiveDescription',
        'preserved_callback': 'ArchivePreservedCallback',
        'deleted_callback': 'ArchiveDeletedCallback',
        'stats': 'ArchiveStats',
        'base_archive_id': 'ArchiveBase',
        'related_aip_id': 'str',
        'related_dip_id': 'str'
    }

    attribute_map = {
        'archive_id': 'archiveId',
        'state': 'state',
        'dataset_id': 'datasetId',
        'root_directory_id': 'rootDirectoryId',
        'creation_time': 'creationTime',
        'config': 'config',
        'description': 'description',
        'preserved_callback': 'preservedCallback',
        'deleted_callback': 'deletedCallback',
        'stats': 'stats',
        'base_archive_id': 'baseArchiveId',
        'related_aip_id': 'relatedAipId',
        'related_dip_id': 'relatedDipId'
    }

    def __init__(self, archive_id=None, state=None, dataset_id=None, root_directory_id=None, creation_time=None, config=None, description=None, preserved_callback=None, deleted_callback=None, stats=None, base_archive_id=None, related_aip_id=None, related_dip_id=None):  # noqa: E501
        """Archive - a model defined in Swagger"""  # noqa: E501
        self._archive_id = None
        self._state = None
        self._dataset_id = None
        self._root_directory_id = None
        self._creation_time = None
        self._config = None
        self._description = None
        self._preserved_callback = None
        self._deleted_callback = None
        self._stats = None
        self._base_archive_id = None
        self._related_aip_id = None
        self._related_dip_id = None
        self.discriminator = None
        self.archive_id = archive_id
        self.state = state
        self.dataset_id = dataset_id
        self.root_directory_id = root_directory_id
        self.creation_time = creation_time
        if config is not None:
            self.config = config
        self.description = description
        if preserved_callback is not None:
            self.preserved_callback = preserved_callback
        if deleted_callback is not None:
            self.deleted_callback = deleted_callback
        self.stats = stats
        if base_archive_id is not None:
            self.base_archive_id = base_archive_id
        if related_aip_id is not None:
            self.related_aip_id = related_aip_id
        if related_dip_id is not None:
            self.related_dip_id = related_dip_id

    @property
    def archive_id(self):
        """Gets the archive_id of this Archive.  # noqa: E501

        Archive Id.  # noqa: E501

        :return: The archive_id of this Archive.  # noqa: E501
        :rtype: str
        """
        return self._archive_id

    @archive_id.setter
    def archive_id(self, archive_id):
        """Sets the archive_id of this Archive.

        Archive Id.  # noqa: E501

        :param archive_id: The archive_id of this Archive.  # noqa: E501
        :type: str
        """
        if archive_id is None:
            raise ValueError("Invalid value for `archive_id`, must not be `None`")  # noqa: E501

        self._archive_id = archive_id

    @property
    def state(self):
        """Gets the state of this Archive.  # noqa: E501


        :return: The state of this Archive.  # noqa: E501
        :rtype: ArchiveState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Archive.


        :param state: The state of this Archive.  # noqa: E501
        :type: ArchiveState
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def dataset_id(self):
        """Gets the dataset_id of this Archive.  # noqa: E501

        Id of the dataset from which the archive has been created.  # noqa: E501

        :return: The dataset_id of this Archive.  # noqa: E501
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this Archive.

        Id of the dataset from which the archive has been created.  # noqa: E501

        :param dataset_id: The dataset_id of this Archive.  # noqa: E501
        :type: str
        """
        if dataset_id is None:
            raise ValueError("Invalid value for `dataset_id`, must not be `None`")  # noqa: E501

        self._dataset_id = dataset_id

    @property
    def root_directory_id(self):
        """Gets the root_directory_id of this Archive.  # noqa: E501

        Id of the hidden directory in the space where the archive is stored.   # noqa: E501

        :return: The root_directory_id of this Archive.  # noqa: E501
        :rtype: str
        """
        return self._root_directory_id

    @root_directory_id.setter
    def root_directory_id(self, root_directory_id):
        """Sets the root_directory_id of this Archive.

        Id of the hidden directory in the space where the archive is stored.   # noqa: E501

        :param root_directory_id: The root_directory_id of this Archive.  # noqa: E501
        :type: str
        """
        if root_directory_id is None:
            raise ValueError("Invalid value for `root_directory_id`, must not be `None`")  # noqa: E501

        self._root_directory_id = root_directory_id

    @property
    def creation_time(self):
        """Gets the creation_time of this Archive.  # noqa: E501


        :return: The creation_time of this Archive.  # noqa: E501
        :rtype: Timestamp
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this Archive.


        :param creation_time: The creation_time of this Archive.  # noqa: E501
        :type: Timestamp
        """
        if creation_time is None:
            raise ValueError("Invalid value for `creation_time`, must not be `None`")  # noqa: E501

        self._creation_time = creation_time

    @property
    def config(self):
        """Gets the config of this Archive.  # noqa: E501


        :return: The config of this Archive.  # noqa: E501
        :rtype: ArchiveConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this Archive.


        :param config: The config of this Archive.  # noqa: E501
        :type: ArchiveConfig
        """

        self._config = config

    @property
    def description(self):
        """Gets the description of this Archive.  # noqa: E501


        :return: The description of this Archive.  # noqa: E501
        :rtype: ArchiveDescription
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Archive.


        :param description: The description of this Archive.  # noqa: E501
        :type: ArchiveDescription
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def preserved_callback(self):
        """Gets the preserved_callback of this Archive.  # noqa: E501


        :return: The preserved_callback of this Archive.  # noqa: E501
        :rtype: ArchivePreservedCallback
        """
        return self._preserved_callback

    @preserved_callback.setter
    def preserved_callback(self, preserved_callback):
        """Sets the preserved_callback of this Archive.


        :param preserved_callback: The preserved_callback of this Archive.  # noqa: E501
        :type: ArchivePreservedCallback
        """

        self._preserved_callback = preserved_callback

    @property
    def deleted_callback(self):
        """Gets the deleted_callback of this Archive.  # noqa: E501


        :return: The deleted_callback of this Archive.  # noqa: E501
        :rtype: ArchiveDeletedCallback
        """
        return self._deleted_callback

    @deleted_callback.setter
    def deleted_callback(self, deleted_callback):
        """Sets the deleted_callback of this Archive.


        :param deleted_callback: The deleted_callback of this Archive.  # noqa: E501
        :type: ArchiveDeletedCallback
        """

        self._deleted_callback = deleted_callback

    @property
    def stats(self):
        """Gets the stats of this Archive.  # noqa: E501


        :return: The stats of this Archive.  # noqa: E501
        :rtype: ArchiveStats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this Archive.


        :param stats: The stats of this Archive.  # noqa: E501
        :type: ArchiveStats
        """
        if stats is None:
            raise ValueError("Invalid value for `stats`, must not be `None`")  # noqa: E501

        self._stats = stats

    @property
    def base_archive_id(self):
        """Gets the base_archive_id of this Archive.  # noqa: E501


        :return: The base_archive_id of this Archive.  # noqa: E501
        :rtype: ArchiveBase
        """
        return self._base_archive_id

    @base_archive_id.setter
    def base_archive_id(self, base_archive_id):
        """Sets the base_archive_id of this Archive.


        :param base_archive_id: The base_archive_id of this Archive.  # noqa: E501
        :type: ArchiveBase
        """

        self._base_archive_id = base_archive_id

    @property
    def related_aip_id(self):
        """Gets the related_aip_id of this Archive.  # noqa: E501

        Id of the related archival information package (AIP) archive. Can be null when there is no such archive.   # noqa: E501

        :return: The related_aip_id of this Archive.  # noqa: E501
        :rtype: str
        """
        return self._related_aip_id

    @related_aip_id.setter
    def related_aip_id(self, related_aip_id):
        """Sets the related_aip_id of this Archive.

        Id of the related archival information package (AIP) archive. Can be null when there is no such archive.   # noqa: E501

        :param related_aip_id: The related_aip_id of this Archive.  # noqa: E501
        :type: str
        """

        self._related_aip_id = related_aip_id

    @property
    def related_dip_id(self):
        """Gets the related_dip_id of this Archive.  # noqa: E501

        Id of the related dissemination information package (DIP) archive. Can be null when there is no such archive.   # noqa: E501

        :return: The related_dip_id of this Archive.  # noqa: E501
        :rtype: str
        """
        return self._related_dip_id

    @related_dip_id.setter
    def related_dip_id(self, related_dip_id):
        """Sets the related_dip_id of this Archive.

        Id of the related dissemination information package (DIP) archive. Can be null when there is no such archive.   # noqa: E501

        :param related_dip_id: The related_dip_id of this Archive.  # noqa: E501
        :type: str
        """

        self._related_dip_id = related_dip_id

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
        if issubclass(Archive, dict):
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
        if not isinstance(other, Archive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
