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

class MetadataChangesStreamRequestCustomMetadata(object):
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
        'always': 'bool',
        'fields': 'list[str]',
        'exists': 'list[str]'
    }

    attribute_map = {
        'always': 'always',
        'fields': 'fields',
        'exists': 'exists'
    }

    def __init__(self, always=False, fields=None, exists=None):  # noqa: E501
        """MetadataChangesStreamRequestCustomMetadata - a model defined in Swagger"""  # noqa: E501
        self._always = None
        self._fields = None
        self._exists = None
        self.discriminator = None
        if always is not None:
            self.always = always
        if fields is not None:
            self.fields = fields
        if exists is not None:
            self.exists = exists

    @property
    def always(self):
        """Gets the always of this MetadataChangesStreamRequestCustomMetadata.  # noqa: E501

        Indicates whether specified customMetadata fields should be sent on other metadata changes.  # noqa: E501

        :return: The always of this MetadataChangesStreamRequestCustomMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._always

    @always.setter
    def always(self, always):
        """Sets the always of this MetadataChangesStreamRequestCustomMetadata.

        Indicates whether specified customMetadata fields should be sent on other metadata changes.  # noqa: E501

        :param always: The always of this MetadataChangesStreamRequestCustomMetadata.  # noqa: E501
        :type: bool
        """

        self._always = always

    @property
    def fields(self):
        """Gets the fields of this MetadataChangesStreamRequestCustomMetadata.  # noqa: E501

        Xattrs names to retrieve. In case of missing fields `null` values are returned. In order to fetch special attributes additional keys can be specified, namely  `onedata_json`, `onedata_rdf` or `onedata_keyvalue` (fetches all fields beside special ones).   # noqa: E501

        :return: The fields of this MetadataChangesStreamRequestCustomMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this MetadataChangesStreamRequestCustomMetadata.

        Xattrs names to retrieve. In case of missing fields `null` values are returned. In order to fetch special attributes additional keys can be specified, namely  `onedata_json`, `onedata_rdf` or `onedata_keyvalue` (fetches all fields beside special ones).   # noqa: E501

        :param fields: The fields of this MetadataChangesStreamRequestCustomMetadata.  # noqa: E501
        :type: list[str]
        """

        self._fields = fields

    @property
    def exists(self):
        """Gets the exists of this MetadataChangesStreamRequestCustomMetadata.  # noqa: E501

        Xattrs names to check for existence. Existence of special attributes can also be checked by specifying `onedata_json`, `onedata_rdf` or `onedata_keyvalue`  (checks if any normal attribute exists).   # noqa: E501

        :return: The exists of this MetadataChangesStreamRequestCustomMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._exists

    @exists.setter
    def exists(self, exists):
        """Sets the exists of this MetadataChangesStreamRequestCustomMetadata.

        Xattrs names to check for existence. Existence of special attributes can also be checked by specifying `onedata_json`, `onedata_rdf` or `onedata_keyvalue`  (checks if any normal attribute exists).   # noqa: E501

        :param exists: The exists of this MetadataChangesStreamRequestCustomMetadata.  # noqa: E501
        :type: list[str]
        """

        self._exists = exists

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
        if issubclass(MetadataChangesStreamRequestCustomMetadata, dict):
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
        if not isinstance(other, MetadataChangesStreamRequestCustomMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
