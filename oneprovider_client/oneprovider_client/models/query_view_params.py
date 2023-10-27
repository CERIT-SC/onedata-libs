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

class QueryViewParams(object):
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
        'descending': 'bool',
        'key': 'str',
        'limit': 'int',
        'skip': 'int',
        'startkey': 'str',
        'startkey_docid': 'str',
        'endkey': 'str',
        'endkey_docid': 'str',
        'inclusive_end': 'bool',
        'stale': 'str',
        'bbox': 'str',
        'spatial': 'bool',
        'start_range': 'str',
        'end_range': 'str'
    }

    attribute_map = {
        'descending': 'descending',
        'key': 'key',
        'limit': 'limit',
        'skip': 'skip',
        'startkey': 'startkey',
        'startkey_docid': 'startkey_docid',
        'endkey': 'endkey',
        'endkey_docid': 'endkey_docid',
        'inclusive_end': 'inclusive_end',
        'stale': 'stale',
        'bbox': 'bbox',
        'spatial': 'spatial',
        'start_range': 'start_range',
        'end_range': 'end_range'
    }

    def __init__(self, descending=False, key=None, limit=None, skip=None, startkey=None, startkey_docid=None, endkey=None, endkey_docid=None, inclusive_end=False, stale='update_after', bbox=None, spatial=None, start_range=None, end_range=None):  # noqa: E501
        """QueryViewParams - a model defined in Swagger"""  # noqa: E501
        self._descending = None
        self._key = None
        self._limit = None
        self._skip = None
        self._startkey = None
        self._startkey_docid = None
        self._endkey = None
        self._endkey_docid = None
        self._inclusive_end = None
        self._stale = None
        self._bbox = None
        self._spatial = None
        self._start_range = None
        self._end_range = None
        self.discriminator = None
        if descending is not None:
            self.descending = descending
        if key is not None:
            self.key = key
        if limit is not None:
            self.limit = limit
        if skip is not None:
            self.skip = skip
        if startkey is not None:
            self.startkey = startkey
        if startkey_docid is not None:
            self.startkey_docid = startkey_docid
        if endkey is not None:
            self.endkey = endkey
        if endkey_docid is not None:
            self.endkey_docid = endkey_docid
        if inclusive_end is not None:
            self.inclusive_end = inclusive_end
        if stale is not None:
            self.stale = stale
        if bbox is not None:
            self.bbox = bbox
        if spatial is not None:
            self.spatial = spatial
        if start_range is not None:
            self.start_range = start_range
        if end_range is not None:
            self.end_range = end_range

    @property
    def descending(self):
        """Gets the descending of this QueryViewParams.  # noqa: E501

        Return the documents in descending order (by key).  # noqa: E501

        :return: The descending of this QueryViewParams.  # noqa: E501
        :rtype: bool
        """
        return self._descending

    @descending.setter
    def descending(self, descending):
        """Sets the descending of this QueryViewParams.

        Return the documents in descending order (by key).  # noqa: E501

        :param descending: The descending of this QueryViewParams.  # noqa: E501
        :type: bool
        """

        self._descending = descending

    @property
    def key(self):
        """Gets the key of this QueryViewParams.  # noqa: E501

        Return only documents that match the specified key. Key must be specified as a JSON value.   # noqa: E501

        :return: The key of this QueryViewParams.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this QueryViewParams.

        Return only documents that match the specified key. Key must be specified as a JSON value.   # noqa: E501

        :param key: The key of this QueryViewParams.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def limit(self):
        """Gets the limit of this QueryViewParams.  # noqa: E501

        Limit the number of the returned documents to the specified number.   # noqa: E501

        :return: The limit of this QueryViewParams.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this QueryViewParams.

        Limit the number of the returned documents to the specified number.   # noqa: E501

        :param limit: The limit of this QueryViewParams.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def skip(self):
        """Gets the skip of this QueryViewParams.  # noqa: E501

        Skip this number of records before starting to return the results.   # noqa: E501

        :return: The skip of this QueryViewParams.  # noqa: E501
        :rtype: int
        """
        return self._skip

    @skip.setter
    def skip(self, skip):
        """Sets the skip of this QueryViewParams.

        Skip this number of records before starting to return the results.   # noqa: E501

        :param skip: The skip of this QueryViewParams.  # noqa: E501
        :type: int
        """

        self._skip = skip

    @property
    def startkey(self):
        """Gets the startkey of this QueryViewParams.  # noqa: E501

        Return records with a value equal to or greater than the specified key. Key must be specified as a JSON value.   # noqa: E501

        :return: The startkey of this QueryViewParams.  # noqa: E501
        :rtype: str
        """
        return self._startkey

    @startkey.setter
    def startkey(self, startkey):
        """Sets the startkey of this QueryViewParams.

        Return records with a value equal to or greater than the specified key. Key must be specified as a JSON value.   # noqa: E501

        :param startkey: The startkey of this QueryViewParams.  # noqa: E501
        :type: str
        """

        self._startkey = startkey

    @property
    def startkey_docid(self):
        """Gets the startkey_docid of this QueryViewParams.  # noqa: E501

        Return records starting with the specified document Id.   # noqa: E501

        :return: The startkey_docid of this QueryViewParams.  # noqa: E501
        :rtype: str
        """
        return self._startkey_docid

    @startkey_docid.setter
    def startkey_docid(self, startkey_docid):
        """Sets the startkey_docid of this QueryViewParams.

        Return records starting with the specified document Id.   # noqa: E501

        :param startkey_docid: The startkey_docid of this QueryViewParams.  # noqa: E501
        :type: str
        """

        self._startkey_docid = startkey_docid

    @property
    def endkey(self):
        """Gets the endkey of this QueryViewParams.  # noqa: E501

        Stop returning records when the specified key is reached. Key must be specified as a JSON value.   # noqa: E501

        :return: The endkey of this QueryViewParams.  # noqa: E501
        :rtype: str
        """
        return self._endkey

    @endkey.setter
    def endkey(self, endkey):
        """Sets the endkey of this QueryViewParams.

        Stop returning records when the specified key is reached. Key must be specified as a JSON value.   # noqa: E501

        :param endkey: The endkey of this QueryViewParams.  # noqa: E501
        :type: str
        """

        self._endkey = endkey

    @property
    def endkey_docid(self):
        """Gets the endkey_docid of this QueryViewParams.  # noqa: E501

        Stop returning records when the specified document Id is reached.   # noqa: E501

        :return: The endkey_docid of this QueryViewParams.  # noqa: E501
        :rtype: str
        """
        return self._endkey_docid

    @endkey_docid.setter
    def endkey_docid(self, endkey_docid):
        """Sets the endkey_docid of this QueryViewParams.

        Stop returning records when the specified document Id is reached.   # noqa: E501

        :param endkey_docid: The endkey_docid of this QueryViewParams.  # noqa: E501
        :type: str
        """

        self._endkey_docid = endkey_docid

    @property
    def inclusive_end(self):
        """Gets the inclusive_end of this QueryViewParams.  # noqa: E501

        Specifies whether the specified end key is included in the result. ***Note:*** Do not use `inclusive_end` with `key` or `keys`.   # noqa: E501

        :return: The inclusive_end of this QueryViewParams.  # noqa: E501
        :rtype: bool
        """
        return self._inclusive_end

    @inclusive_end.setter
    def inclusive_end(self, inclusive_end):
        """Sets the inclusive_end of this QueryViewParams.

        Specifies whether the specified end key is included in the result. ***Note:*** Do not use `inclusive_end` with `key` or `keys`.   # noqa: E501

        :param inclusive_end: The inclusive_end of this QueryViewParams.  # noqa: E501
        :type: bool
        """

        self._inclusive_end = inclusive_end

    @property
    def stale(self):
        """Gets the stale of this QueryViewParams.  # noqa: E501

        Allow records from a stale view to be used. Allowed values are `ok`, `update_after` or `false`.   # noqa: E501

        :return: The stale of this QueryViewParams.  # noqa: E501
        :rtype: str
        """
        return self._stale

    @stale.setter
    def stale(self, stale):
        """Sets the stale of this QueryViewParams.

        Allow records from a stale view to be used. Allowed values are `ok`, `update_after` or `false`.   # noqa: E501

        :param stale: The stale of this QueryViewParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["ok", "update_after", "false"]  # noqa: E501
        if stale not in allowed_values:
            raise ValueError(
                "Invalid value for `stale` ({0}), must be one of {1}"  # noqa: E501
                .format(stale, allowed_values)
            )

        self._stale = stale

    @property
    def bbox(self):
        """Gets the bbox of this QueryViewParams.  # noqa: E501

        Specify the bounding box for a spatial query (e.g. `bbox=-180,-90,0,0`)   # noqa: E501

        :return: The bbox of this QueryViewParams.  # noqa: E501
        :rtype: str
        """
        return self._bbox

    @bbox.setter
    def bbox(self, bbox):
        """Sets the bbox of this QueryViewParams.

        Specify the bounding box for a spatial query (e.g. `bbox=-180,-90,0,0`)   # noqa: E501

        :param bbox: The bbox of this QueryViewParams.  # noqa: E501
        :type: str
        """

        self._bbox = bbox

    @property
    def spatial(self):
        """Gets the spatial of this QueryViewParams.  # noqa: E501

        Enable spatial type of query. When querying the file-popularity view, the `start_range` and `end_range` constraints should be specified as 6-dimensional arrays, with the following fields: `[SizeLowerLimit, LastOpenHoursEpochLowerLimit, TotalOpenLowerLimit, HoursOpenAvgLowerLimit, DayOpenAvgLowerLimit, MonthOpenAvgLowerLimit]`.   # noqa: E501

        :return: The spatial of this QueryViewParams.  # noqa: E501
        :rtype: bool
        """
        return self._spatial

    @spatial.setter
    def spatial(self, spatial):
        """Sets the spatial of this QueryViewParams.

        Enable spatial type of query. When querying the file-popularity view, the `start_range` and `end_range` constraints should be specified as 6-dimensional arrays, with the following fields: `[SizeLowerLimit, LastOpenHoursEpochLowerLimit, TotalOpenLowerLimit, HoursOpenAvgLowerLimit, DayOpenAvgLowerLimit, MonthOpenAvgLowerLimit]`.   # noqa: E501

        :param spatial: The spatial of this QueryViewParams.  # noqa: E501
        :type: bool
        """

        self._spatial = spatial

    @property
    def start_range(self):
        """Gets the start_range of this QueryViewParams.  # noqa: E501

        Array specifying the range in spatial queries (e.g. `start_range=[1,0,0,0,0,0]`).   # noqa: E501

        :return: The start_range of this QueryViewParams.  # noqa: E501
        :rtype: str
        """
        return self._start_range

    @start_range.setter
    def start_range(self, start_range):
        """Sets the start_range of this QueryViewParams.

        Array specifying the range in spatial queries (e.g. `start_range=[1,0,0,0,0,0]`).   # noqa: E501

        :param start_range: The start_range of this QueryViewParams.  # noqa: E501
        :type: str
        """

        self._start_range = start_range

    @property
    def end_range(self):
        """Gets the end_range of this QueryViewParams.  # noqa: E501

        Array specifying the range in spatial queries (e.g. `end_range=[null,null,null,null,null,null]`).   # noqa: E501

        :return: The end_range of this QueryViewParams.  # noqa: E501
        :rtype: str
        """
        return self._end_range

    @end_range.setter
    def end_range(self, end_range):
        """Sets the end_range of this QueryViewParams.

        Array specifying the range in spatial queries (e.g. `end_range=[null,null,null,null,null,null]`).   # noqa: E501

        :param end_range: The end_range of this QueryViewParams.  # noqa: E501
        :type: str
        """

        self._end_range = end_range

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
        if issubclass(QueryViewParams, dict):
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
        if not isinstance(other, QueryViewParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
