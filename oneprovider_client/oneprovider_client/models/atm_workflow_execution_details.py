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

class AtmWorkflowExecutionDetails(object):
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
        'atm_workflow_execution_id': 'str',
        'atm_workflow_schema_snapshot_id': 'str',
        'name': 'str',
        'atm_inventory_id': 'str',
        'space_id': 'str',
        'user_id': 'str',
        'status': 'str',
        'schedule_time': 'int',
        'start_time': 'int',
        'suspend_time': 'int',
        'finish_time': 'int',
        'lambda_snapshot_registry': 'dict(str, str)',
        'store_registry': 'dict(str, str)',
        'system_audit_log_store_id': 'str',
        'lanes': 'list[AtmWorkflowExecutionDetailsLanes]'
    }

    attribute_map = {
        'atm_workflow_execution_id': 'atmWorkflowExecutionId',
        'atm_workflow_schema_snapshot_id': 'atmWorkflowSchemaSnapshotId',
        'name': 'name',
        'atm_inventory_id': 'atmInventoryId',
        'space_id': 'spaceId',
        'user_id': 'userId',
        'status': 'status',
        'schedule_time': 'scheduleTime',
        'start_time': 'startTime',
        'suspend_time': 'suspendTime',
        'finish_time': 'finishTime',
        'lambda_snapshot_registry': 'lambdaSnapshotRegistry',
        'store_registry': 'storeRegistry',
        'system_audit_log_store_id': 'systemAuditLogStoreId',
        'lanes': 'lanes'
    }

    def __init__(self, atm_workflow_execution_id=None, atm_workflow_schema_snapshot_id=None, name=None, atm_inventory_id=None, space_id=None, user_id=None, status=None, schedule_time=None, start_time=None, suspend_time=None, finish_time=None, lambda_snapshot_registry=None, store_registry=None, system_audit_log_store_id=None, lanes=None):  # noqa: E501
        """AtmWorkflowExecutionDetails - a model defined in Swagger"""  # noqa: E501
        self._atm_workflow_execution_id = None
        self._atm_workflow_schema_snapshot_id = None
        self._name = None
        self._atm_inventory_id = None
        self._space_id = None
        self._user_id = None
        self._status = None
        self._schedule_time = None
        self._start_time = None
        self._suspend_time = None
        self._finish_time = None
        self._lambda_snapshot_registry = None
        self._store_registry = None
        self._system_audit_log_store_id = None
        self._lanes = None
        self.discriminator = None
        self.atm_workflow_execution_id = atm_workflow_execution_id
        self.atm_workflow_schema_snapshot_id = atm_workflow_schema_snapshot_id
        self.name = name
        self.atm_inventory_id = atm_inventory_id
        self.space_id = space_id
        self.user_id = user_id
        self.status = status
        self.schedule_time = schedule_time
        self.start_time = start_time
        self.suspend_time = suspend_time
        self.finish_time = finish_time
        self.lambda_snapshot_registry = lambda_snapshot_registry
        self.store_registry = store_registry
        self.system_audit_log_store_id = system_audit_log_store_id
        self.lanes = lanes

    @property
    def atm_workflow_execution_id(self):
        """Gets the atm_workflow_execution_id of this AtmWorkflowExecutionDetails.  # noqa: E501

        Id of this workflow execution.  # noqa: E501

        :return: The atm_workflow_execution_id of this AtmWorkflowExecutionDetails.  # noqa: E501
        :rtype: str
        """
        return self._atm_workflow_execution_id

    @atm_workflow_execution_id.setter
    def atm_workflow_execution_id(self, atm_workflow_execution_id):
        """Sets the atm_workflow_execution_id of this AtmWorkflowExecutionDetails.

        Id of this workflow execution.  # noqa: E501

        :param atm_workflow_execution_id: The atm_workflow_execution_id of this AtmWorkflowExecutionDetails.  # noqa: E501
        :type: str
        """
        if atm_workflow_execution_id is None:
            raise ValueError("Invalid value for `atm_workflow_execution_id`, must not be `None`")  # noqa: E501

        self._atm_workflow_execution_id = atm_workflow_execution_id

    @property
    def atm_workflow_schema_snapshot_id(self):
        """Gets the atm_workflow_schema_snapshot_id of this AtmWorkflowExecutionDetails.  # noqa: E501

        Id of the snapshot of the workflow schema describing the tasks and stores for this workflow.   # noqa: E501

        :return: The atm_workflow_schema_snapshot_id of this AtmWorkflowExecutionDetails.  # noqa: E501
        :rtype: str
        """
        return self._atm_workflow_schema_snapshot_id

    @atm_workflow_schema_snapshot_id.setter
    def atm_workflow_schema_snapshot_id(self, atm_workflow_schema_snapshot_id):
        """Sets the atm_workflow_schema_snapshot_id of this AtmWorkflowExecutionDetails.

        Id of the snapshot of the workflow schema describing the tasks and stores for this workflow.   # noqa: E501

        :param atm_workflow_schema_snapshot_id: The atm_workflow_schema_snapshot_id of this AtmWorkflowExecutionDetails.  # noqa: E501
        :type: str
        """
        if atm_workflow_schema_snapshot_id is None:
            raise ValueError("Invalid value for `atm_workflow_schema_snapshot_id`, must not be `None`")  # noqa: E501

        self._atm_workflow_schema_snapshot_id = atm_workflow_schema_snapshot_id

    @property
    def name(self):
        """Gets the name of this AtmWorkflowExecutionDetails.  # noqa: E501

        Name of the workflow schema used for this execution.  # noqa: E501

        :return: The name of this AtmWorkflowExecutionDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AtmWorkflowExecutionDetails.

        Name of the workflow schema used for this execution.  # noqa: E501

        :param name: The name of this AtmWorkflowExecutionDetails.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def atm_inventory_id(self):
        """Gets the atm_inventory_id of this AtmWorkflowExecutionDetails.  # noqa: E501

        Id of automation inventory from which the workflow schema originates.  # noqa: E501

        :return: The atm_inventory_id of this AtmWorkflowExecutionDetails.  # noqa: E501
        :rtype: str
        """
        return self._atm_inventory_id

    @atm_inventory_id.setter
    def atm_inventory_id(self, atm_inventory_id):
        """Sets the atm_inventory_id of this AtmWorkflowExecutionDetails.

        Id of automation inventory from which the workflow schema originates.  # noqa: E501

        :param atm_inventory_id: The atm_inventory_id of this AtmWorkflowExecutionDetails.  # noqa: E501
        :type: str
        """
        if atm_inventory_id is None:
            raise ValueError("Invalid value for `atm_inventory_id`, must not be `None`")  # noqa: E501

        self._atm_inventory_id = atm_inventory_id

    @property
    def space_id(self):
        """Gets the space_id of this AtmWorkflowExecutionDetails.  # noqa: E501

        Id of the space in context of which the workflow was executed.  # noqa: E501

        :return: The space_id of this AtmWorkflowExecutionDetails.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this AtmWorkflowExecutionDetails.

        Id of the space in context of which the workflow was executed.  # noqa: E501

        :param space_id: The space_id of this AtmWorkflowExecutionDetails.  # noqa: E501
        :type: str
        """
        if space_id is None:
            raise ValueError("Invalid value for `space_id`, must not be `None`")  # noqa: E501

        self._space_id = space_id

    @property
    def user_id(self):
        """Gets the user_id of this AtmWorkflowExecutionDetails.  # noqa: E501

        Id of the scheduling user.  # noqa: E501

        :return: The user_id of this AtmWorkflowExecutionDetails.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AtmWorkflowExecutionDetails.

        Id of the scheduling user.  # noqa: E501

        :param user_id: The user_id of this AtmWorkflowExecutionDetails.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def status(self):
        """Gets the status of this AtmWorkflowExecutionDetails.  # noqa: E501

        Overall status of the workflow execution.  # noqa: E501

        :return: The status of this AtmWorkflowExecutionDetails.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AtmWorkflowExecutionDetails.

        Overall status of the workflow execution.  # noqa: E501

        :param status: The status of this AtmWorkflowExecutionDetails.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["resuming", "scheduled", "active", "stopping", "interrupted", "paused", "finished", "crashed", "cancelled", "failed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def schedule_time(self):
        """Gets the schedule_time of this AtmWorkflowExecutionDetails.  # noqa: E501

        Schedule time in seconds (POSIX epoch timestamp).  # noqa: E501

        :return: The schedule_time of this AtmWorkflowExecutionDetails.  # noqa: E501
        :rtype: int
        """
        return self._schedule_time

    @schedule_time.setter
    def schedule_time(self, schedule_time):
        """Sets the schedule_time of this AtmWorkflowExecutionDetails.

        Schedule time in seconds (POSIX epoch timestamp).  # noqa: E501

        :param schedule_time: The schedule_time of this AtmWorkflowExecutionDetails.  # noqa: E501
        :type: int
        """
        if schedule_time is None:
            raise ValueError("Invalid value for `schedule_time`, must not be `None`")  # noqa: E501

        self._schedule_time = schedule_time

    @property
    def start_time(self):
        """Gets the start_time of this AtmWorkflowExecutionDetails.  # noqa: E501

        Start time in seconds (POSIX epoch timestamp).  # noqa: E501

        :return: The start_time of this AtmWorkflowExecutionDetails.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this AtmWorkflowExecutionDetails.

        Start time in seconds (POSIX epoch timestamp).  # noqa: E501

        :param start_time: The start_time of this AtmWorkflowExecutionDetails.  # noqa: E501
        :type: int
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def suspend_time(self):
        """Gets the suspend_time of this AtmWorkflowExecutionDetails.  # noqa: E501

        Suspend time in seconds (POSIX epoch timestamp).  # noqa: E501

        :return: The suspend_time of this AtmWorkflowExecutionDetails.  # noqa: E501
        :rtype: int
        """
        return self._suspend_time

    @suspend_time.setter
    def suspend_time(self, suspend_time):
        """Sets the suspend_time of this AtmWorkflowExecutionDetails.

        Suspend time in seconds (POSIX epoch timestamp).  # noqa: E501

        :param suspend_time: The suspend_time of this AtmWorkflowExecutionDetails.  # noqa: E501
        :type: int
        """
        if suspend_time is None:
            raise ValueError("Invalid value for `suspend_time`, must not be `None`")  # noqa: E501

        self._suspend_time = suspend_time

    @property
    def finish_time(self):
        """Gets the finish_time of this AtmWorkflowExecutionDetails.  # noqa: E501

        Finish time in seconds (POSIX epoch timestamp).  # noqa: E501

        :return: The finish_time of this AtmWorkflowExecutionDetails.  # noqa: E501
        :rtype: int
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this AtmWorkflowExecutionDetails.

        Finish time in seconds (POSIX epoch timestamp).  # noqa: E501

        :param finish_time: The finish_time of this AtmWorkflowExecutionDetails.  # noqa: E501
        :type: int
        """
        if finish_time is None:
            raise ValueError("Invalid value for `finish_time`, must not be `None`")  # noqa: E501

        self._finish_time = finish_time

    @property
    def lambda_snapshot_registry(self):
        """Gets the lambda_snapshot_registry of this AtmWorkflowExecutionDetails.  # noqa: E501

        Map with lambda Ids (keys) and corresponding snapshot Ids.  # noqa: E501

        :return: The lambda_snapshot_registry of this AtmWorkflowExecutionDetails.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._lambda_snapshot_registry

    @lambda_snapshot_registry.setter
    def lambda_snapshot_registry(self, lambda_snapshot_registry):
        """Sets the lambda_snapshot_registry of this AtmWorkflowExecutionDetails.

        Map with lambda Ids (keys) and corresponding snapshot Ids.  # noqa: E501

        :param lambda_snapshot_registry: The lambda_snapshot_registry of this AtmWorkflowExecutionDetails.  # noqa: E501
        :type: dict(str, str)
        """
        if lambda_snapshot_registry is None:
            raise ValueError("Invalid value for `lambda_snapshot_registry`, must not be `None`")  # noqa: E501

        self._lambda_snapshot_registry = lambda_snapshot_registry

    @property
    def store_registry(self):
        """Gets the store_registry of this AtmWorkflowExecutionDetails.  # noqa: E501

        Map with store schema Ids (keys) and corresponding store instance Ids.   # noqa: E501

        :return: The store_registry of this AtmWorkflowExecutionDetails.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._store_registry

    @store_registry.setter
    def store_registry(self, store_registry):
        """Sets the store_registry of this AtmWorkflowExecutionDetails.

        Map with store schema Ids (keys) and corresponding store instance Ids.   # noqa: E501

        :param store_registry: The store_registry of this AtmWorkflowExecutionDetails.  # noqa: E501
        :type: dict(str, str)
        """
        if store_registry is None:
            raise ValueError("Invalid value for `store_registry`, must not be `None`")  # noqa: E501

        self._store_registry = store_registry

    @property
    def system_audit_log_store_id(self):
        """Gets the system_audit_log_store_id of this AtmWorkflowExecutionDetails.  # noqa: E501

        Id of this execution system audit log store.  # noqa: E501

        :return: The system_audit_log_store_id of this AtmWorkflowExecutionDetails.  # noqa: E501
        :rtype: str
        """
        return self._system_audit_log_store_id

    @system_audit_log_store_id.setter
    def system_audit_log_store_id(self, system_audit_log_store_id):
        """Sets the system_audit_log_store_id of this AtmWorkflowExecutionDetails.

        Id of this execution system audit log store.  # noqa: E501

        :param system_audit_log_store_id: The system_audit_log_store_id of this AtmWorkflowExecutionDetails.  # noqa: E501
        :type: str
        """
        if system_audit_log_store_id is None:
            raise ValueError("Invalid value for `system_audit_log_store_id`, must not be `None`")  # noqa: E501

        self._system_audit_log_store_id = system_audit_log_store_id

    @property
    def lanes(self):
        """Gets the lanes of this AtmWorkflowExecutionDetails.  # noqa: E501

        Details of lanes in this workflow execution.  # noqa: E501

        :return: The lanes of this AtmWorkflowExecutionDetails.  # noqa: E501
        :rtype: list[AtmWorkflowExecutionDetailsLanes]
        """
        return self._lanes

    @lanes.setter
    def lanes(self, lanes):
        """Sets the lanes of this AtmWorkflowExecutionDetails.

        Details of lanes in this workflow execution.  # noqa: E501

        :param lanes: The lanes of this AtmWorkflowExecutionDetails.  # noqa: E501
        :type: list[AtmWorkflowExecutionDetailsLanes]
        """
        if lanes is None:
            raise ValueError("Invalid value for `lanes`, must not be `None`")  # noqa: E501

        self._lanes = lanes

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
        if issubclass(AtmWorkflowExecutionDetails, dict):
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
        if not isinstance(other, AtmWorkflowExecutionDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
