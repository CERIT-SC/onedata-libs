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
from oneprovider_client.models.transfer_create_request import TransferCreateRequest  # noqa: F401,E501

class View(TransferCreateRequest):
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
        'data_source_type': 'str',
        'space_id': 'str',
        'view_name': 'str',
        'query_view_params': 'QueryViewParams'
    }
    if hasattr(TransferCreateRequest, "swagger_types"):
        swagger_types.update(TransferCreateRequest.swagger_types)

    attribute_map = {
        'data_source_type': 'dataSourceType',
        'space_id': 'spaceId',
        'view_name': 'viewName',
        'query_view_params': 'queryViewParams'
    }
    if hasattr(TransferCreateRequest, "attribute_map"):
        attribute_map.update(TransferCreateRequest.attribute_map)

    def __init__(self, data_source_type=None, space_id=None, view_name=None, query_view_params=None, *args, **kwargs):  # noqa: E501
        """View - a model defined in Swagger"""  # noqa: E501
        self._data_source_type = None
        self._space_id = None
        self._view_name = None
        self._query_view_params = None
        self.discriminator = None
        if data_source_type is not None:
            self.data_source_type = data_source_type
        if space_id is not None:
            self.space_id = space_id
        if view_name is not None:
            self.view_name = view_name
        if query_view_params is not None:
            self.query_view_params = query_view_params
        TransferCreateRequest.__init__(self, *args, **kwargs)

    @property
    def data_source_type(self):
        """Gets the data_source_type of this View.  # noqa: E501

        Indicates the method of determining files to be transferred.  `type = \"view\"` - this transfer covers files that are returned as a result of querying chosen view. The view must be defined on all providers involved in the process and querying it must return a valid list of file ids to be transferred. For more information about views, please see [here](https://onedata.org/#/home/documentation/doc/using_onedata/replication_management.html#advanced-operations-using-views).   # noqa: E501

        :return: The data_source_type of this View.  # noqa: E501
        :rtype: str
        """
        return self._data_source_type

    @data_source_type.setter
    def data_source_type(self, data_source_type):
        """Sets the data_source_type of this View.

        Indicates the method of determining files to be transferred.  `type = \"view\"` - this transfer covers files that are returned as a result of querying chosen view. The view must be defined on all providers involved in the process and querying it must return a valid list of file ids to be transferred. For more information about views, please see [here](https://onedata.org/#/home/documentation/doc/using_onedata/replication_management.html#advanced-operations-using-views).   # noqa: E501

        :param data_source_type: The data_source_type of this View.  # noqa: E501
        :type: str
        """
        allowed_values = ["view"]  # noqa: E501
        if data_source_type not in allowed_values:
            raise ValueError(
                "Invalid value for `data_source_type` ({0}), must be one of {1}"  # noqa: E501
                .format(data_source_type, allowed_values)
            )

        self._data_source_type = data_source_type

    @property
    def space_id(self):
        """Gets the space_id of this View.  # noqa: E501

        Id of space containing the view.  # noqa: E501

        :return: The space_id of this View.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this View.

        Id of space containing the view.  # noqa: E501

        :param space_id: The space_id of this View.  # noqa: E501
        :type: str
        """

        self._space_id = space_id

    @property
    def view_name(self):
        """Gets the view_name of this View.  # noqa: E501

        Name of the view that will be queried to obtain the list of files to be transferred.   # noqa: E501

        :return: The view_name of this View.  # noqa: E501
        :rtype: str
        """
        return self._view_name

    @view_name.setter
    def view_name(self, view_name):
        """Sets the view_name of this View.

        Name of the view that will be queried to obtain the list of files to be transferred.   # noqa: E501

        :param view_name: The view_name of this View.  # noqa: E501
        :type: str
        """

        self._view_name = view_name

    @property
    def query_view_params(self):
        """Gets the query_view_params of this View.  # noqa: E501


        :return: The query_view_params of this View.  # noqa: E501
        :rtype: QueryViewParams
        """
        return self._query_view_params

    @query_view_params.setter
    def query_view_params(self, query_view_params):
        """Sets the query_view_params of this View.


        :param query_view_params: The query_view_params of this View.  # noqa: E501
        :type: QueryViewParams
        """

        self._query_view_params = query_view_params

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
        if issubclass(View, dict):
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
        if not isinstance(other, View):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
