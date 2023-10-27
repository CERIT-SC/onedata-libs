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
from oneprovider_client.models.dir_size_stats_query import DirSizeStatsQuery  # noqa: F401,E501

class Slice(DirSizeStatsQuery):
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
        'mode': 'str',
        'layout': 'TimeSeriesLayout',
        'start_timestamp': 'str',
        'stop_timestamp': 'str',
        'window_limit': 'str',
        'extended_info': 'str'
    }
    if hasattr(DirSizeStatsQuery, "swagger_types"):
        swagger_types.update(DirSizeStatsQuery.swagger_types)

    attribute_map = {
        'mode': 'mode',
        'layout': 'layout',
        'start_timestamp': 'startTimestamp',
        'stop_timestamp': 'stopTimestamp',
        'window_limit': 'windowLimit',
        'extended_info': 'extendedInfo'
    }
    if hasattr(DirSizeStatsQuery, "attribute_map"):
        attribute_map.update(DirSizeStatsQuery.attribute_map)

    def __init__(self, mode=None, layout=None, start_timestamp=None, stop_timestamp=None, window_limit=None, extended_info=None, *args, **kwargs):  # noqa: E501
        """Slice - a model defined in Swagger"""  # noqa: E501
        self._mode = None
        self._layout = None
        self._start_timestamp = None
        self._stop_timestamp = None
        self._window_limit = None
        self._extended_info = None
        self.discriminator = None
        if mode is not None:
            self.mode = mode
        if layout is not None:
            self.layout = layout
        if start_timestamp is not None:
            self.start_timestamp = start_timestamp
        if stop_timestamp is not None:
            self.stop_timestamp = stop_timestamp
        if window_limit is not None:
            self.window_limit = window_limit
        if extended_info is not None:
            self.extended_info = extended_info
        DirSizeStatsQuery.__init__(self, *args, **kwargs)

    @property
    def mode(self):
        """Gets the mode of this Slice.  # noqa: E501

        Indicates the mode of the query. The `slice` mode returns a collection of slices  of requested time series and metrics that were specified in the `layout` field (which may express a subset of the queried collection). A metric slice is a list of time windows in descending order. The list may be incomplete, since windows are created as needed - along with the first measurement falling in their timespan. Missing windows  should be treated as windows with zero value.   # noqa: E501

        :return: The mode of this Slice.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Slice.

        Indicates the mode of the query. The `slice` mode returns a collection of slices  of requested time series and metrics that were specified in the `layout` field (which may express a subset of the queried collection). A metric slice is a list of time windows in descending order. The list may be incomplete, since windows are created as needed - along with the first measurement falling in their timespan. Missing windows  should be treated as windows with zero value.   # noqa: E501

        :param mode: The mode of this Slice.  # noqa: E501
        :type: str
        """
        allowed_values = ["slice"]  # noqa: E501
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def layout(self):
        """Gets the layout of this Slice.  # noqa: E501


        :return: The layout of this Slice.  # noqa: E501
        :rtype: TimeSeriesLayout
        """
        return self._layout

    @layout.setter
    def layout(self, layout):
        """Sets the layout of this Slice.


        :param layout: The layout of this Slice.  # noqa: E501
        :type: TimeSeriesLayout
        """

        self._layout = layout

    @property
    def start_timestamp(self):
        """Gets the start_timestamp of this Slice.  # noqa: E501

        Latest timestamp used to determine the starting point for descending listing of time windows.  The first window to be listed is the one that includes the given timestamp in its timespan.  If no such window exists, the next existing one is taken.   # noqa: E501

        :return: The start_timestamp of this Slice.  # noqa: E501
        :rtype: str
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        """Sets the start_timestamp of this Slice.

        Latest timestamp used to determine the starting point for descending listing of time windows.  The first window to be listed is the one that includes the given timestamp in its timespan.  If no such window exists, the next existing one is taken.   # noqa: E501

        :param start_timestamp: The start_timestamp of this Slice.  # noqa: E501
        :type: str
        """

        self._start_timestamp = start_timestamp

    @property
    def stop_timestamp(self):
        """Gets the stop_timestamp of this Slice.  # noqa: E501

        Oldest timestamp used to determine the end of descending listing of time windows.   The last window to be listed is the one that includes the given timestamp in its timespan.  If no such window exists, the previous existing one is taken.   # noqa: E501

        :return: The stop_timestamp of this Slice.  # noqa: E501
        :rtype: str
        """
        return self._stop_timestamp

    @stop_timestamp.setter
    def stop_timestamp(self, stop_timestamp):
        """Sets the stop_timestamp of this Slice.

        Oldest timestamp used to determine the end of descending listing of time windows.   The last window to be listed is the one that includes the given timestamp in its timespan.  If no such window exists, the previous existing one is taken.   # noqa: E501

        :param stop_timestamp: The stop_timestamp of this Slice.  # noqa: E501
        :type: str
        """

        self._stop_timestamp = stop_timestamp

    @property
    def window_limit(self):
        """Gets the window_limit of this Slice.  # noqa: E501

        Maximum number of time windows to be listed.  # noqa: E501

        :return: The window_limit of this Slice.  # noqa: E501
        :rtype: str
        """
        return self._window_limit

    @window_limit.setter
    def window_limit(self, window_limit):
        """Sets the window_limit of this Slice.

        Maximum number of time windows to be listed.  # noqa: E501

        :param window_limit: The window_limit of this Slice.  # noqa: E501
        :type: str
        """

        self._window_limit = window_limit

    @property
    def extended_info(self):
        """Gets the extended_info of this Slice.  # noqa: E501

        If true, information about the first and last timestamp of measurements per window will be included.  # noqa: E501

        :return: The extended_info of this Slice.  # noqa: E501
        :rtype: str
        """
        return self._extended_info

    @extended_info.setter
    def extended_info(self, extended_info):
        """Sets the extended_info of this Slice.

        If true, information about the first and last timestamp of measurements per window will be included.  # noqa: E501

        :param extended_info: The extended_info of this Slice.  # noqa: E501
        :type: str
        """

        self._extended_info = extended_info

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
        if issubclass(Slice, dict):
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
        if not isinstance(other, Slice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
