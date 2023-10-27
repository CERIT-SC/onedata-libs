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

class AtmWorkflowExecutionScheduleRequest(object):
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
        'space_id': 'str',
        'atm_workflow_schema_id': 'str',
        'atm_workflow_schema_revision_number': 'str',
        'store_initial_content_overlay': 'dict(str, object)',
        'log_level': 'str',
        'callback': 'str'
    }

    attribute_map = {
        'space_id': 'spaceId',
        'atm_workflow_schema_id': 'atmWorkflowSchemaId',
        'atm_workflow_schema_revision_number': 'atmWorkflowSchemaRevisionNumber',
        'store_initial_content_overlay': 'storeInitialContentOverlay',
        'log_level': 'logLevel',
        'callback': 'callback'
    }

    def __init__(self, space_id=None, atm_workflow_schema_id=None, atm_workflow_schema_revision_number=None, store_initial_content_overlay=None, log_level='info', callback=None):  # noqa: E501
        """AtmWorkflowExecutionScheduleRequest - a model defined in Swagger"""  # noqa: E501
        self._space_id = None
        self._atm_workflow_schema_id = None
        self._atm_workflow_schema_revision_number = None
        self._store_initial_content_overlay = None
        self._log_level = None
        self._callback = None
        self.discriminator = None
        self.space_id = space_id
        self.atm_workflow_schema_id = atm_workflow_schema_id
        self.atm_workflow_schema_revision_number = atm_workflow_schema_revision_number
        if store_initial_content_overlay is not None:
            self.store_initial_content_overlay = store_initial_content_overlay
        if log_level is not None:
            self.log_level = log_level
        if callback is not None:
            self.callback = callback

    @property
    def space_id(self):
        """Gets the space_id of this AtmWorkflowExecutionScheduleRequest.  # noqa: E501

        Id of the space in context of which the workflow will be executed.   # noqa: E501

        :return: The space_id of this AtmWorkflowExecutionScheduleRequest.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this AtmWorkflowExecutionScheduleRequest.

        Id of the space in context of which the workflow will be executed.   # noqa: E501

        :param space_id: The space_id of this AtmWorkflowExecutionScheduleRequest.  # noqa: E501
        :type: str
        """
        if space_id is None:
            raise ValueError("Invalid value for `space_id`, must not be `None`")  # noqa: E501

        self._space_id = space_id

    @property
    def atm_workflow_schema_id(self):
        """Gets the atm_workflow_schema_id of this AtmWorkflowExecutionScheduleRequest.  # noqa: E501

        Id of the workflow schema.  # noqa: E501

        :return: The atm_workflow_schema_id of this AtmWorkflowExecutionScheduleRequest.  # noqa: E501
        :rtype: str
        """
        return self._atm_workflow_schema_id

    @atm_workflow_schema_id.setter
    def atm_workflow_schema_id(self, atm_workflow_schema_id):
        """Sets the atm_workflow_schema_id of this AtmWorkflowExecutionScheduleRequest.

        Id of the workflow schema.  # noqa: E501

        :param atm_workflow_schema_id: The atm_workflow_schema_id of this AtmWorkflowExecutionScheduleRequest.  # noqa: E501
        :type: str
        """
        if atm_workflow_schema_id is None:
            raise ValueError("Invalid value for `atm_workflow_schema_id`, must not be `None`")  # noqa: E501

        self._atm_workflow_schema_id = atm_workflow_schema_id

    @property
    def atm_workflow_schema_revision_number(self):
        """Gets the atm_workflow_schema_revision_number of this AtmWorkflowExecutionScheduleRequest.  # noqa: E501

        Number of workflow schema revision describing the tasks and stores for  the workflow.   # noqa: E501

        :return: The atm_workflow_schema_revision_number of this AtmWorkflowExecutionScheduleRequest.  # noqa: E501
        :rtype: str
        """
        return self._atm_workflow_schema_revision_number

    @atm_workflow_schema_revision_number.setter
    def atm_workflow_schema_revision_number(self, atm_workflow_schema_revision_number):
        """Sets the atm_workflow_schema_revision_number of this AtmWorkflowExecutionScheduleRequest.

        Number of workflow schema revision describing the tasks and stores for  the workflow.   # noqa: E501

        :param atm_workflow_schema_revision_number: The atm_workflow_schema_revision_number of this AtmWorkflowExecutionScheduleRequest.  # noqa: E501
        :type: str
        """
        if atm_workflow_schema_revision_number is None:
            raise ValueError("Invalid value for `atm_workflow_schema_revision_number`, must not be `None`")  # noqa: E501

        self._atm_workflow_schema_revision_number = atm_workflow_schema_revision_number

    @property
    def store_initial_content_overlay(self):
        """Gets the store_initial_content_overlay of this AtmWorkflowExecutionScheduleRequest.  # noqa: E501

        Map with store schema Ids (keys) and corresponding initial content  of the stores.   # noqa: E501

        :return: The store_initial_content_overlay of this AtmWorkflowExecutionScheduleRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._store_initial_content_overlay

    @store_initial_content_overlay.setter
    def store_initial_content_overlay(self, store_initial_content_overlay):
        """Sets the store_initial_content_overlay of this AtmWorkflowExecutionScheduleRequest.

        Map with store schema Ids (keys) and corresponding initial content  of the stores.   # noqa: E501

        :param store_initial_content_overlay: The store_initial_content_overlay of this AtmWorkflowExecutionScheduleRequest.  # noqa: E501
        :type: dict(str, object)
        """

        self._store_initial_content_overlay = store_initial_content_overlay

    @property
    def log_level(self):
        """Gets the log_level of this AtmWorkflowExecutionScheduleRequest.  # noqa: E501

        Level controling the amount of information recorded in audit logs as only logs with severity equal or higher to this level will be stored.    # noqa: E501

        :return: The log_level of this AtmWorkflowExecutionScheduleRequest.  # noqa: E501
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """Sets the log_level of this AtmWorkflowExecutionScheduleRequest.

        Level controling the amount of information recorded in audit logs as only logs with severity equal or higher to this level will be stored.    # noqa: E501

        :param log_level: The log_level of this AtmWorkflowExecutionScheduleRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["debug", "info", "notice", "warning", "error", "critical", "alert", "emergency"]  # noqa: E501
        if log_level not in allowed_values:
            raise ValueError(
                "Invalid value for `log_level` ({0}), must be one of {1}"  # noqa: E501
                .format(log_level, allowed_values)
            )

        self._log_level = log_level

    @property
    def callback(self):
        """Gets the callback of this AtmWorkflowExecutionScheduleRequest.  # noqa: E501

        Custom REST callback URL which will be called when the workflow execution ends - a http `POST` request with workflow execution Id and status in body.   # noqa: E501

        :return: The callback of this AtmWorkflowExecutionScheduleRequest.  # noqa: E501
        :rtype: str
        """
        return self._callback

    @callback.setter
    def callback(self, callback):
        """Sets the callback of this AtmWorkflowExecutionScheduleRequest.

        Custom REST callback URL which will be called when the workflow execution ends - a http `POST` request with workflow execution Id and status in body.   # noqa: E501

        :param callback: The callback of this AtmWorkflowExecutionScheduleRequest.  # noqa: E501
        :type: str
        """

        self._callback = callback

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
        if issubclass(AtmWorkflowExecutionScheduleRequest, dict):
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
        if not isinstance(other, AtmWorkflowExecutionScheduleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
