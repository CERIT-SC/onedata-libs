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

class DatasetSummary(object):
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
        'direct_dataset': 'str',
        'effective_ancestor_datasets': 'list[str]',
        'effective_protection_flags': 'EffectiveFileProtectionFlags'
    }

    attribute_map = {
        'direct_dataset': 'directDataset',
        'effective_ancestor_datasets': 'effectiveAncestorDatasets',
        'effective_protection_flags': 'effectiveProtectionFlags'
    }

    def __init__(self, direct_dataset=None, effective_ancestor_datasets=None, effective_protection_flags=None):  # noqa: E501
        """DatasetSummary - a model defined in Swagger"""  # noqa: E501
        self._direct_dataset = None
        self._effective_ancestor_datasets = None
        self._effective_protection_flags = None
        self.discriminator = None
        if direct_dataset is not None:
            self.direct_dataset = direct_dataset
        if effective_ancestor_datasets is not None:
            self.effective_ancestor_datasets = effective_ancestor_datasets
        if effective_protection_flags is not None:
            self.effective_protection_flags = effective_protection_flags

    @property
    def direct_dataset(self):
        """Gets the direct_dataset of this DatasetSummary.  # noqa: E501

        Id of dataset established for this file regardless if attached or detached, or `null` if there isn't one.   # noqa: E501

        :return: The direct_dataset of this DatasetSummary.  # noqa: E501
        :rtype: str
        """
        return self._direct_dataset

    @direct_dataset.setter
    def direct_dataset(self, direct_dataset):
        """Sets the direct_dataset of this DatasetSummary.

        Id of dataset established for this file regardless if attached or detached, or `null` if there isn't one.   # noqa: E501

        :param direct_dataset: The direct_dataset of this DatasetSummary.  # noqa: E501
        :type: str
        """

        self._direct_dataset = direct_dataset

    @property
    def effective_ancestor_datasets(self):
        """Gets the effective_ancestor_datasets of this DatasetSummary.  # noqa: E501

        Ids of all datasets in `attached` state registered for this file ancestor directories.  # noqa: E501

        :return: The effective_ancestor_datasets of this DatasetSummary.  # noqa: E501
        :rtype: list[str]
        """
        return self._effective_ancestor_datasets

    @effective_ancestor_datasets.setter
    def effective_ancestor_datasets(self, effective_ancestor_datasets):
        """Sets the effective_ancestor_datasets of this DatasetSummary.

        Ids of all datasets in `attached` state registered for this file ancestor directories.  # noqa: E501

        :param effective_ancestor_datasets: The effective_ancestor_datasets of this DatasetSummary.  # noqa: E501
        :type: list[str]
        """

        self._effective_ancestor_datasets = effective_ancestor_datasets

    @property
    def effective_protection_flags(self):
        """Gets the effective_protection_flags of this DatasetSummary.  # noqa: E501


        :return: The effective_protection_flags of this DatasetSummary.  # noqa: E501
        :rtype: EffectiveFileProtectionFlags
        """
        return self._effective_protection_flags

    @effective_protection_flags.setter
    def effective_protection_flags(self, effective_protection_flags):
        """Sets the effective_protection_flags of this DatasetSummary.


        :param effective_protection_flags: The effective_protection_flags of this DatasetSummary.  # noqa: E501
        :type: EffectiveFileProtectionFlags
        """

        self._effective_protection_flags = effective_protection_flags

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
        if issubclass(DatasetSummary, dict):
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
        if not isinstance(other, DatasetSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
