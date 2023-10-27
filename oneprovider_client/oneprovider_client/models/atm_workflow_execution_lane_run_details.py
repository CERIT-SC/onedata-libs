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

class AtmWorkflowExecutionLaneRunDetails(object):
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
        'run_number': 'int',
        'origin_run_number': 'int',
        'run_type': 'str',
        'status': 'str',
        'iterated_store_id': 'str',
        'exception_store_id': 'str',
        'parallel_boxes': 'list[AtmWorkflowExecutionLaneRunDetailsParallelBoxes]',
        'is_retriable': 'bool',
        'is_rerunable': 'bool'
    }

    attribute_map = {
        'run_number': 'runNumber',
        'origin_run_number': 'originRunNumber',
        'run_type': 'runType',
        'status': 'status',
        'iterated_store_id': 'iteratedStoreId',
        'exception_store_id': 'exceptionStoreId',
        'parallel_boxes': 'parallelBoxes',
        'is_retriable': 'isRetriable',
        'is_rerunable': 'isRerunable'
    }

    def __init__(self, run_number=None, origin_run_number=None, run_type=None, status=None, iterated_store_id=None, exception_store_id=None, parallel_boxes=None, is_retriable=None, is_rerunable=None):  # noqa: E501
        """AtmWorkflowExecutionLaneRunDetails - a model defined in Swagger"""  # noqa: E501
        self._run_number = None
        self._origin_run_number = None
        self._run_type = None
        self._status = None
        self._iterated_store_id = None
        self._exception_store_id = None
        self._parallel_boxes = None
        self._is_retriable = None
        self._is_rerunable = None
        self.discriminator = None
        self.run_number = run_number
        self.origin_run_number = origin_run_number
        self.run_type = run_type
        self.status = status
        self.iterated_store_id = iterated_store_id
        self.exception_store_id = exception_store_id
        self.parallel_boxes = parallel_boxes
        self.is_retriable = is_retriable
        self.is_rerunable = is_rerunable

    @property
    def run_number(self):
        """Gets the run_number of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501

        Number of workflow execution run in which this lane run is included.  When prepared in advance, this value is `null`, as the specific number  is not yet known.   # noqa: E501

        :return: The run_number of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501
        :rtype: int
        """
        return self._run_number

    @run_number.setter
    def run_number(self, run_number):
        """Sets the run_number of this AtmWorkflowExecutionLaneRunDetails.

        Number of workflow execution run in which this lane run is included.  When prepared in advance, this value is `null`, as the specific number  is not yet known.   # noqa: E501

        :param run_number: The run_number of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501
        :type: int
        """
        if run_number is None:
            raise ValueError("Invalid value for `run_number`, must not be `None`")  # noqa: E501

        self._run_number = run_number

    @property
    def origin_run_number(self):
        """Gets the origin_run_number of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501

        Number of workflow execution lane run on which this lane run is based  in case of repeat (either rerun or retry) or `null` otherwise.   # noqa: E501

        :return: The origin_run_number of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501
        :rtype: int
        """
        return self._origin_run_number

    @origin_run_number.setter
    def origin_run_number(self, origin_run_number):
        """Sets the origin_run_number of this AtmWorkflowExecutionLaneRunDetails.

        Number of workflow execution lane run on which this lane run is based  in case of repeat (either rerun or retry) or `null` otherwise.   # noqa: E501

        :param origin_run_number: The origin_run_number of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501
        :type: int
        """
        if origin_run_number is None:
            raise ValueError("Invalid value for `origin_run_number`, must not be `None`")  # noqa: E501

        self._origin_run_number = origin_run_number

    @property
    def run_type(self):
        """Gets the run_type of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501

        Type of lane run.  # noqa: E501

        :return: The run_type of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501
        :rtype: str
        """
        return self._run_type

    @run_type.setter
    def run_type(self, run_type):
        """Sets the run_type of this AtmWorkflowExecutionLaneRunDetails.

        Type of lane run.  # noqa: E501

        :param run_type: The run_type of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501
        :type: str
        """
        if run_type is None:
            raise ValueError("Invalid value for `run_type`, must not be `None`")  # noqa: E501
        allowed_values = ["regular", "rerun", "retry"]  # noqa: E501
        if run_type not in allowed_values:
            raise ValueError(
                "Invalid value for `run_type` ({0}), must be one of {1}"  # noqa: E501
                .format(run_type, allowed_values)
            )

        self._run_type = run_type

    @property
    def status(self):
        """Gets the status of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501

        Overall status of the lane run.  # noqa: E501

        :return: The status of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AtmWorkflowExecutionLaneRunDetails.

        Overall status of the lane run.  # noqa: E501

        :param status: The status of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["resuming", "scheduled", "preparing", "enqueued", "active", "stopping", "interrupted", "paused", "finished", "crashed", "cancelled", "failed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def iterated_store_id(self):
        """Gets the iterated_store_id of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501

        Id of this lane run iterated store.  # noqa: E501

        :return: The iterated_store_id of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501
        :rtype: str
        """
        return self._iterated_store_id

    @iterated_store_id.setter
    def iterated_store_id(self, iterated_store_id):
        """Sets the iterated_store_id of this AtmWorkflowExecutionLaneRunDetails.

        Id of this lane run iterated store.  # noqa: E501

        :param iterated_store_id: The iterated_store_id of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501
        :type: str
        """
        if iterated_store_id is None:
            raise ValueError("Invalid value for `iterated_store_id`, must not be `None`")  # noqa: E501

        self._iterated_store_id = iterated_store_id

    @property
    def exception_store_id(self):
        """Gets the exception_store_id of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501

        Id of this lane run exception store.  # noqa: E501

        :return: The exception_store_id of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501
        :rtype: str
        """
        return self._exception_store_id

    @exception_store_id.setter
    def exception_store_id(self, exception_store_id):
        """Sets the exception_store_id of this AtmWorkflowExecutionLaneRunDetails.

        Id of this lane run exception store.  # noqa: E501

        :param exception_store_id: The exception_store_id of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501
        :type: str
        """
        if exception_store_id is None:
            raise ValueError("Invalid value for `exception_store_id`, must not be `None`")  # noqa: E501

        self._exception_store_id = exception_store_id

    @property
    def parallel_boxes(self):
        """Gets the parallel_boxes of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501

        Details of parallel boxes in this lane run.  # noqa: E501

        :return: The parallel_boxes of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501
        :rtype: list[AtmWorkflowExecutionLaneRunDetailsParallelBoxes]
        """
        return self._parallel_boxes

    @parallel_boxes.setter
    def parallel_boxes(self, parallel_boxes):
        """Sets the parallel_boxes of this AtmWorkflowExecutionLaneRunDetails.

        Details of parallel boxes in this lane run.  # noqa: E501

        :param parallel_boxes: The parallel_boxes of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501
        :type: list[AtmWorkflowExecutionLaneRunDetailsParallelBoxes]
        """
        if parallel_boxes is None:
            raise ValueError("Invalid value for `parallel_boxes`, must not be `None`")  # noqa: E501

        self._parallel_boxes = parallel_boxes

    @property
    def is_retriable(self):
        """Gets the is_retriable of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501

        Indicates whether this lane execution run can be retried or not.  # noqa: E501

        :return: The is_retriable of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_retriable

    @is_retriable.setter
    def is_retriable(self, is_retriable):
        """Sets the is_retriable of this AtmWorkflowExecutionLaneRunDetails.

        Indicates whether this lane execution run can be retried or not.  # noqa: E501

        :param is_retriable: The is_retriable of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501
        :type: bool
        """
        if is_retriable is None:
            raise ValueError("Invalid value for `is_retriable`, must not be `None`")  # noqa: E501

        self._is_retriable = is_retriable

    @property
    def is_rerunable(self):
        """Gets the is_rerunable of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501

        Indicates whether this lane execution run can be rerun or not.  # noqa: E501

        :return: The is_rerunable of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_rerunable

    @is_rerunable.setter
    def is_rerunable(self, is_rerunable):
        """Sets the is_rerunable of this AtmWorkflowExecutionLaneRunDetails.

        Indicates whether this lane execution run can be rerun or not.  # noqa: E501

        :param is_rerunable: The is_rerunable of this AtmWorkflowExecutionLaneRunDetails.  # noqa: E501
        :type: bool
        """
        if is_rerunable is None:
            raise ValueError("Invalid value for `is_rerunable`, must not be `None`")  # noqa: E501

        self._is_rerunable = is_rerunable

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
        if issubclass(AtmWorkflowExecutionLaneRunDetails, dict):
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
        if not isinstance(other, AtmWorkflowExecutionLaneRunDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
