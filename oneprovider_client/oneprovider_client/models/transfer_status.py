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

class TransferStatus(object):
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
        'type': 'str',
        'user_id': 'str',
        'rerun_id': 'str',
        'effective_job_transfer_id': 'str',
        'space_id': 'str',
        'data_source_type': 'str',
        'file_id': 'str',
        'file_path': 'str',
        'view_name': 'str',
        'query_view_params': 'QueryViewParams',
        'transfer_status': 'str',
        'effective_job_status': 'str',
        'replication_status': 'str',
        'eviction_status': 'str',
        'replicating_provider_id': 'str',
        'evicting_provider_id': 'str',
        'callback': 'str',
        'files_to_process': 'int',
        'files_processed': 'int',
        'files_replicated': 'int',
        'files_evicted': 'int',
        'files_failed': 'int',
        'bytes_replicated': 'int',
        'schedule_time': 'int',
        'start_time': 'int',
        'finish_time': 'int',
        'last_update': 'int',
        'min_hist': 'dict(str, list[int])',
        'hr_hist': 'dict(str, list[int])',
        'dy_hist': 'dict(str, list[int])',
        'mth_hist': 'dict(str, list[int])'
    }

    attribute_map = {
        'type': 'type',
        'user_id': 'userId',
        'rerun_id': 'rerunId',
        'effective_job_transfer_id': 'effectiveJobTransferId',
        'space_id': 'spaceId',
        'data_source_type': 'dataSourceType',
        'file_id': 'fileId',
        'file_path': 'filePath',
        'view_name': 'viewName',
        'query_view_params': 'queryViewParams',
        'transfer_status': 'transferStatus',
        'effective_job_status': 'effectiveJobStatus',
        'replication_status': 'replicationStatus',
        'eviction_status': 'evictionStatus',
        'replicating_provider_id': 'replicatingProviderId',
        'evicting_provider_id': 'evictingProviderId',
        'callback': 'callback',
        'files_to_process': 'filesToProcess',
        'files_processed': 'filesProcessed',
        'files_replicated': 'filesReplicated',
        'files_evicted': 'filesEvicted',
        'files_failed': 'filesFailed',
        'bytes_replicated': 'bytesReplicated',
        'schedule_time': 'scheduleTime',
        'start_time': 'startTime',
        'finish_time': 'finishTime',
        'last_update': 'lastUpdate',
        'min_hist': 'minHist',
        'hr_hist': 'hrHist',
        'dy_hist': 'dyHist',
        'mth_hist': 'mthHist'
    }

    def __init__(self, type=None, user_id=None, rerun_id=None, effective_job_transfer_id=None, space_id=None, data_source_type=None, file_id=None, file_path=None, view_name=None, query_view_params=None, transfer_status=None, effective_job_status=None, replication_status=None, eviction_status=None, replicating_provider_id=None, evicting_provider_id=None, callback=None, files_to_process=None, files_processed=None, files_replicated=None, files_evicted=None, files_failed=None, bytes_replicated=None, schedule_time=None, start_time=None, finish_time=None, last_update=None, min_hist=None, hr_hist=None, dy_hist=None, mth_hist=None):  # noqa: E501
        """TransferStatus - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._user_id = None
        self._rerun_id = None
        self._effective_job_transfer_id = None
        self._space_id = None
        self._data_source_type = None
        self._file_id = None
        self._file_path = None
        self._view_name = None
        self._query_view_params = None
        self._transfer_status = None
        self._effective_job_status = None
        self._replication_status = None
        self._eviction_status = None
        self._replicating_provider_id = None
        self._evicting_provider_id = None
        self._callback = None
        self._files_to_process = None
        self._files_processed = None
        self._files_replicated = None
        self._files_evicted = None
        self._files_failed = None
        self._bytes_replicated = None
        self._schedule_time = None
        self._start_time = None
        self._finish_time = None
        self._last_update = None
        self._min_hist = None
        self._hr_hist = None
        self._dy_hist = None
        self._mth_hist = None
        self.discriminator = None
        self.type = type
        self.user_id = user_id
        self.rerun_id = rerun_id
        if effective_job_transfer_id is not None:
            self.effective_job_transfer_id = effective_job_transfer_id
        self.space_id = space_id
        self.data_source_type = data_source_type
        if file_id is not None:
            self.file_id = file_id
        if file_path is not None:
            self.file_path = file_path
        if view_name is not None:
            self.view_name = view_name
        if query_view_params is not None:
            self.query_view_params = query_view_params
        self.transfer_status = transfer_status
        if effective_job_status is not None:
            self.effective_job_status = effective_job_status
        self.replication_status = replication_status
        self.eviction_status = eviction_status
        self.replicating_provider_id = replicating_provider_id
        self.evicting_provider_id = evicting_provider_id
        self.callback = callback
        self.files_to_process = files_to_process
        self.files_processed = files_processed
        self.files_replicated = files_replicated
        self.files_evicted = files_evicted
        self.files_failed = files_failed
        self.bytes_replicated = bytes_replicated
        self.schedule_time = schedule_time
        self.start_time = start_time
        self.finish_time = finish_time
        self.last_update = last_update
        self.min_hist = min_hist
        self.hr_hist = hr_hist
        self.dy_hist = dy_hist
        self.mth_hist = mth_hist

    @property
    def type(self):
        """Gets the type of this TransferStatus.  # noqa: E501

        Requested type of transfer.  # noqa: E501

        :return: The type of this TransferStatus.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TransferStatus.

        Requested type of transfer.  # noqa: E501

        :param type: The type of this TransferStatus.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["replication", "eviction", "migration"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def user_id(self):
        """Gets the user_id of this TransferStatus.  # noqa: E501

        Id of the user that started the transfer.  # noqa: E501

        :return: The user_id of this TransferStatus.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TransferStatus.

        Id of the user that started the transfer.  # noqa: E501

        :param user_id: The user_id of this TransferStatus.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def rerun_id(self):
        """Gets the rerun_id of this TransferStatus.  # noqa: E501

        If the transfer was rerun, this field contains the Id of the new transfer, otherwise null.  # noqa: E501

        :return: The rerun_id of this TransferStatus.  # noqa: E501
        :rtype: str
        """
        return self._rerun_id

    @rerun_id.setter
    def rerun_id(self, rerun_id):
        """Sets the rerun_id of this TransferStatus.

        If the transfer was rerun, this field contains the Id of the new transfer, otherwise null.  # noqa: E501

        :param rerun_id: The rerun_id of this TransferStatus.  # noqa: E501
        :type: str
        """
        if rerun_id is None:
            raise ValueError("Invalid value for `rerun_id`, must not be `None`")  # noqa: E501

        self._rerun_id = rerun_id

    @property
    def effective_job_transfer_id(self):
        """Gets the effective_job_transfer_id of this TransferStatus.  # noqa: E501

        Last transfer Id in chain made of `rerunId`.  # noqa: E501

        :return: The effective_job_transfer_id of this TransferStatus.  # noqa: E501
        :rtype: str
        """
        return self._effective_job_transfer_id

    @effective_job_transfer_id.setter
    def effective_job_transfer_id(self, effective_job_transfer_id):
        """Sets the effective_job_transfer_id of this TransferStatus.

        Last transfer Id in chain made of `rerunId`.  # noqa: E501

        :param effective_job_transfer_id: The effective_job_transfer_id of this TransferStatus.  # noqa: E501
        :type: str
        """

        self._effective_job_transfer_id = effective_job_transfer_id

    @property
    def space_id(self):
        """Gets the space_id of this TransferStatus.  # noqa: E501

        Id of space in context of which transfer was performed.  # noqa: E501

        :return: The space_id of this TransferStatus.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this TransferStatus.

        Id of space in context of which transfer was performed.  # noqa: E501

        :param space_id: The space_id of this TransferStatus.  # noqa: E501
        :type: str
        """
        if space_id is None:
            raise ValueError("Invalid value for `space_id`, must not be `None`")  # noqa: E501

        self._space_id = space_id

    @property
    def data_source_type(self):
        """Gets the data_source_type of this TransferStatus.  # noqa: E501

        Indicates the method of determining files to be transferred.        `type = \"file\"` - this transfer covers a single file or a whole directory (recursively). When scheduling such transfer, the user must have permissions to access the file/directory.      `type = \"view\"` - this transfer covers files that are returned as a result of querying chosen view. The view must be defined on all providers involved in the process and querying it must return a valid list of file ids to be transferred. For more information about views, please see [here](https://onedata.org/#/home/documentation/doc/using_onedata/replication_management.html#advanced-operations-using-views).   # noqa: E501

        :return: The data_source_type of this TransferStatus.  # noqa: E501
        :rtype: str
        """
        return self._data_source_type

    @data_source_type.setter
    def data_source_type(self, data_source_type):
        """Sets the data_source_type of this TransferStatus.

        Indicates the method of determining files to be transferred.        `type = \"file\"` - this transfer covers a single file or a whole directory (recursively). When scheduling such transfer, the user must have permissions to access the file/directory.      `type = \"view\"` - this transfer covers files that are returned as a result of querying chosen view. The view must be defined on all providers involved in the process and querying it must return a valid list of file ids to be transferred. For more information about views, please see [here](https://onedata.org/#/home/documentation/doc/using_onedata/replication_management.html#advanced-operations-using-views).   # noqa: E501

        :param data_source_type: The data_source_type of this TransferStatus.  # noqa: E501
        :type: str
        """
        if data_source_type is None:
            raise ValueError("Invalid value for `data_source_type`, must not be `None`")  # noqa: E501
        allowed_values = ["file", "view"]  # noqa: E501
        if data_source_type not in allowed_values:
            raise ValueError(
                "Invalid value for `data_source_type` ({0}), must be one of {1}"  # noqa: E501
                .format(data_source_type, allowed_values)
            )

        self._data_source_type = data_source_type

    @property
    def file_id(self):
        """Gets the file_id of this TransferStatus.  # noqa: E501

        Id of the transferred file or directory.  # noqa: E501

        :return: The file_id of this TransferStatus.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this TransferStatus.

        Id of the transferred file or directory.  # noqa: E501

        :param file_id: The file_id of this TransferStatus.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def file_path(self):
        """Gets the file_path of this TransferStatus.  # noqa: E501

        Path to the file or directory in the virtual file system.  # noqa: E501

        :return: The file_path of this TransferStatus.  # noqa: E501
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this TransferStatus.

        Path to the file or directory in the virtual file system.  # noqa: E501

        :param file_path: The file_path of this TransferStatus.  # noqa: E501
        :type: str
        """

        self._file_path = file_path

    @property
    def view_name(self):
        """Gets the view_name of this TransferStatus.  # noqa: E501

        Name of the view that was queried to obtain the list of files to transfer.   # noqa: E501

        :return: The view_name of this TransferStatus.  # noqa: E501
        :rtype: str
        """
        return self._view_name

    @view_name.setter
    def view_name(self, view_name):
        """Sets the view_name of this TransferStatus.

        Name of the view that was queried to obtain the list of files to transfer.   # noqa: E501

        :param view_name: The view_name of this TransferStatus.  # noqa: E501
        :type: str
        """

        self._view_name = view_name

    @property
    def query_view_params(self):
        """Gets the query_view_params of this TransferStatus.  # noqa: E501


        :return: The query_view_params of this TransferStatus.  # noqa: E501
        :rtype: QueryViewParams
        """
        return self._query_view_params

    @query_view_params.setter
    def query_view_params(self, query_view_params):
        """Sets the query_view_params of this TransferStatus.


        :param query_view_params: The query_view_params of this TransferStatus.  # noqa: E501
        :type: QueryViewParams
        """

        self._query_view_params = query_view_params

    @property
    def transfer_status(self):
        """Gets the transfer_status of this TransferStatus.  # noqa: E501

        Overall status of transfer.  # noqa: E501

        :return: The transfer_status of this TransferStatus.  # noqa: E501
        :rtype: str
        """
        return self._transfer_status

    @transfer_status.setter
    def transfer_status(self, transfer_status):
        """Sets the transfer_status of this TransferStatus.

        Overall status of transfer.  # noqa: E501

        :param transfer_status: The transfer_status of this TransferStatus.  # noqa: E501
        :type: str
        """
        if transfer_status is None:
            raise ValueError("Invalid value for `transfer_status`, must not be `None`")  # noqa: E501
        allowed_values = ["scheduled", "enqueued", "skipped", "replicating", "evicting", "completed", "aborting", "cancelled", "failed"]  # noqa: E501
        if transfer_status not in allowed_values:
            raise ValueError(
                "Invalid value for `transfer_status` ({0}), must be one of {1}"  # noqa: E501
                .format(transfer_status, allowed_values)
            )

        self._transfer_status = transfer_status

    @property
    def effective_job_status(self):
        """Gets the effective_job_status of this TransferStatus.  # noqa: E501

        Overall status of effective transfer job (the last one in chain made of `rerunId`).   # noqa: E501

        :return: The effective_job_status of this TransferStatus.  # noqa: E501
        :rtype: str
        """
        return self._effective_job_status

    @effective_job_status.setter
    def effective_job_status(self, effective_job_status):
        """Sets the effective_job_status of this TransferStatus.

        Overall status of effective transfer job (the last one in chain made of `rerunId`).   # noqa: E501

        :param effective_job_status: The effective_job_status of this TransferStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["scheduled", "enqueued", "skipped", "replicating", "evicting", "completed", "aborting", "cancelled", "failed"]  # noqa: E501
        if effective_job_status not in allowed_values:
            raise ValueError(
                "Invalid value for `effective_job_status` ({0}), must be one of {1}"  # noqa: E501
                .format(effective_job_status, allowed_values)
            )

        self._effective_job_status = effective_job_status

    @property
    def replication_status(self):
        """Gets the replication_status of this TransferStatus.  # noqa: E501

        The status of transfer replication phase.  # noqa: E501

        :return: The replication_status of this TransferStatus.  # noqa: E501
        :rtype: str
        """
        return self._replication_status

    @replication_status.setter
    def replication_status(self, replication_status):
        """Sets the replication_status of this TransferStatus.

        The status of transfer replication phase.  # noqa: E501

        :param replication_status: The replication_status of this TransferStatus.  # noqa: E501
        :type: str
        """
        if replication_status is None:
            raise ValueError("Invalid value for `replication_status`, must not be `None`")  # noqa: E501
        allowed_values = ["scheduled", "enqueued", "skipped", "active", "completed", "aborting", "cancelled", "failed"]  # noqa: E501
        if replication_status not in allowed_values:
            raise ValueError(
                "Invalid value for `replication_status` ({0}), must be one of {1}"  # noqa: E501
                .format(replication_status, allowed_values)
            )

        self._replication_status = replication_status

    @property
    def eviction_status(self):
        """Gets the eviction_status of this TransferStatus.  # noqa: E501

        The status of transfer eviction phase.  # noqa: E501

        :return: The eviction_status of this TransferStatus.  # noqa: E501
        :rtype: str
        """
        return self._eviction_status

    @eviction_status.setter
    def eviction_status(self, eviction_status):
        """Sets the eviction_status of this TransferStatus.

        The status of transfer eviction phase.  # noqa: E501

        :param eviction_status: The eviction_status of this TransferStatus.  # noqa: E501
        :type: str
        """
        if eviction_status is None:
            raise ValueError("Invalid value for `eviction_status`, must not be `None`")  # noqa: E501
        allowed_values = ["scheduled", "enqueued", "skipped", "active", "completed", "aborting", "cancelled", "failed"]  # noqa: E501
        if eviction_status not in allowed_values:
            raise ValueError(
                "Invalid value for `eviction_status` ({0}), must be one of {1}"  # noqa: E501
                .format(eviction_status, allowed_values)
            )

        self._eviction_status = eviction_status

    @property
    def replicating_provider_id(self):
        """Gets the replicating_provider_id of this TransferStatus.  # noqa: E501

        Id of provider to which data was copied, ensuring that the provider has a complete replica at the end of the process.   # noqa: E501

        :return: The replicating_provider_id of this TransferStatus.  # noqa: E501
        :rtype: str
        """
        return self._replicating_provider_id

    @replicating_provider_id.setter
    def replicating_provider_id(self, replicating_provider_id):
        """Sets the replicating_provider_id of this TransferStatus.

        Id of provider to which data was copied, ensuring that the provider has a complete replica at the end of the process.   # noqa: E501

        :param replicating_provider_id: The replicating_provider_id of this TransferStatus.  # noqa: E501
        :type: str
        """
        if replicating_provider_id is None:
            raise ValueError("Invalid value for `replicating_provider_id`, must not be `None`")  # noqa: E501

        self._replicating_provider_id = replicating_provider_id

    @property
    def evicting_provider_id(self):
        """Gets the evicting_provider_id of this TransferStatus.  # noqa: E501

        Id of provider from which replica(s) were removed.  # noqa: E501

        :return: The evicting_provider_id of this TransferStatus.  # noqa: E501
        :rtype: str
        """
        return self._evicting_provider_id

    @evicting_provider_id.setter
    def evicting_provider_id(self, evicting_provider_id):
        """Sets the evicting_provider_id of this TransferStatus.

        Id of provider from which replica(s) were removed.  # noqa: E501

        :param evicting_provider_id: The evicting_provider_id of this TransferStatus.  # noqa: E501
        :type: str
        """
        if evicting_provider_id is None:
            raise ValueError("Invalid value for `evicting_provider_id`, must not be `None`")  # noqa: E501

        self._evicting_provider_id = evicting_provider_id

    @property
    def callback(self):
        """Gets the callback of this TransferStatus.  # noqa: E501

        Optional callback URL, which will be invoked on transfer completion.  # noqa: E501

        :return: The callback of this TransferStatus.  # noqa: E501
        :rtype: str
        """
        return self._callback

    @callback.setter
    def callback(self, callback):
        """Sets the callback of this TransferStatus.

        Optional callback URL, which will be invoked on transfer completion.  # noqa: E501

        :param callback: The callback of this TransferStatus.  # noqa: E501
        :type: str
        """
        if callback is None:
            raise ValueError("Invalid value for `callback`, must not be `None`")  # noqa: E501

        self._callback = callback

    @property
    def files_to_process(self):
        """Gets the files_to_process of this TransferStatus.  # noqa: E501

        Total number of files in this transfer.  # noqa: E501

        :return: The files_to_process of this TransferStatus.  # noqa: E501
        :rtype: int
        """
        return self._files_to_process

    @files_to_process.setter
    def files_to_process(self, files_to_process):
        """Sets the files_to_process of this TransferStatus.

        Total number of files in this transfer.  # noqa: E501

        :param files_to_process: The files_to_process of this TransferStatus.  # noqa: E501
        :type: int
        """
        if files_to_process is None:
            raise ValueError("Invalid value for `files_to_process`, must not be `None`")  # noqa: E501

        self._files_to_process = files_to_process

    @property
    def files_processed(self):
        """Gets the files_processed of this TransferStatus.  # noqa: E501

        Number of files already processed.  # noqa: E501

        :return: The files_processed of this TransferStatus.  # noqa: E501
        :rtype: int
        """
        return self._files_processed

    @files_processed.setter
    def files_processed(self, files_processed):
        """Sets the files_processed of this TransferStatus.

        Number of files already processed.  # noqa: E501

        :param files_processed: The files_processed of this TransferStatus.  # noqa: E501
        :type: int
        """
        if files_processed is None:
            raise ValueError("Invalid value for `files_processed`, must not be `None`")  # noqa: E501

        self._files_processed = files_processed

    @property
    def files_replicated(self):
        """Gets the files_replicated of this TransferStatus.  # noqa: E501

        Number of files already replicated.  # noqa: E501

        :return: The files_replicated of this TransferStatus.  # noqa: E501
        :rtype: int
        """
        return self._files_replicated

    @files_replicated.setter
    def files_replicated(self, files_replicated):
        """Sets the files_replicated of this TransferStatus.

        Number of files already replicated.  # noqa: E501

        :param files_replicated: The files_replicated of this TransferStatus.  # noqa: E501
        :type: int
        """
        if files_replicated is None:
            raise ValueError("Invalid value for `files_replicated`, must not be `None`")  # noqa: E501

        self._files_replicated = files_replicated

    @property
    def files_evicted(self):
        """Gets the files_evicted of this TransferStatus.  # noqa: E501

        Number of files already evicted.  # noqa: E501

        :return: The files_evicted of this TransferStatus.  # noqa: E501
        :rtype: int
        """
        return self._files_evicted

    @files_evicted.setter
    def files_evicted(self, files_evicted):
        """Sets the files_evicted of this TransferStatus.

        Number of files already evicted.  # noqa: E501

        :param files_evicted: The files_evicted of this TransferStatus.  # noqa: E501
        :type: int
        """
        if files_evicted is None:
            raise ValueError("Invalid value for `files_evicted`, must not be `None`")  # noqa: E501

        self._files_evicted = files_evicted

    @property
    def files_failed(self):
        """Gets the files_failed of this TransferStatus.  # noqa: E501

        Number of files for which eviction or replication has failed.  # noqa: E501

        :return: The files_failed of this TransferStatus.  # noqa: E501
        :rtype: int
        """
        return self._files_failed

    @files_failed.setter
    def files_failed(self, files_failed):
        """Sets the files_failed of this TransferStatus.

        Number of files for which eviction or replication has failed.  # noqa: E501

        :param files_failed: The files_failed of this TransferStatus.  # noqa: E501
        :type: int
        """
        if files_failed is None:
            raise ValueError("Invalid value for `files_failed`, must not be `None`")  # noqa: E501

        self._files_failed = files_failed

    @property
    def bytes_replicated(self):
        """Gets the bytes_replicated of this TransferStatus.  # noqa: E501

        Number of bytes already replicated.  # noqa: E501

        :return: The bytes_replicated of this TransferStatus.  # noqa: E501
        :rtype: int
        """
        return self._bytes_replicated

    @bytes_replicated.setter
    def bytes_replicated(self, bytes_replicated):
        """Sets the bytes_replicated of this TransferStatus.

        Number of bytes already replicated.  # noqa: E501

        :param bytes_replicated: The bytes_replicated of this TransferStatus.  # noqa: E501
        :type: int
        """
        if bytes_replicated is None:
            raise ValueError("Invalid value for `bytes_replicated`, must not be `None`")  # noqa: E501

        self._bytes_replicated = bytes_replicated

    @property
    def schedule_time(self):
        """Gets the schedule_time of this TransferStatus.  # noqa: E501

        Schedule time in seconds (POSIX epoch timestamp).  # noqa: E501

        :return: The schedule_time of this TransferStatus.  # noqa: E501
        :rtype: int
        """
        return self._schedule_time

    @schedule_time.setter
    def schedule_time(self, schedule_time):
        """Sets the schedule_time of this TransferStatus.

        Schedule time in seconds (POSIX epoch timestamp).  # noqa: E501

        :param schedule_time: The schedule_time of this TransferStatus.  # noqa: E501
        :type: int
        """
        if schedule_time is None:
            raise ValueError("Invalid value for `schedule_time`, must not be `None`")  # noqa: E501

        self._schedule_time = schedule_time

    @property
    def start_time(self):
        """Gets the start_time of this TransferStatus.  # noqa: E501

        Start time in seconds (POSIX epoch timestamp).  # noqa: E501

        :return: The start_time of this TransferStatus.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TransferStatus.

        Start time in seconds (POSIX epoch timestamp).  # noqa: E501

        :param start_time: The start_time of this TransferStatus.  # noqa: E501
        :type: int
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def finish_time(self):
        """Gets the finish_time of this TransferStatus.  # noqa: E501

        Finish time in seconds (POSIX epoch timestamp).  # noqa: E501

        :return: The finish_time of this TransferStatus.  # noqa: E501
        :rtype: int
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this TransferStatus.

        Finish time in seconds (POSIX epoch timestamp).  # noqa: E501

        :param finish_time: The finish_time of this TransferStatus.  # noqa: E501
        :type: int
        """
        if finish_time is None:
            raise ValueError("Invalid value for `finish_time`, must not be `None`")  # noqa: E501

        self._finish_time = finish_time

    @property
    def last_update(self):
        """Gets the last_update of this TransferStatus.  # noqa: E501

        Last transfer update time in seconds (POSIX epoch timestamp).  # noqa: E501

        :return: The last_update of this TransferStatus.  # noqa: E501
        :rtype: int
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this TransferStatus.

        Last transfer update time in seconds (POSIX epoch timestamp).  # noqa: E501

        :param last_update: The last_update of this TransferStatus.  # noqa: E501
        :type: int
        """
        if last_update is None:
            raise ValueError("Invalid value for `last_update`, must not be `None`")  # noqa: E501

        self._last_update = last_update

    @property
    def min_hist(self):
        """Gets the min_hist of this TransferStatus.  # noqa: E501

        Replication statistics within the last minute, per provider.  # noqa: E501

        :return: The min_hist of this TransferStatus.  # noqa: E501
        :rtype: dict(str, list[int])
        """
        return self._min_hist

    @min_hist.setter
    def min_hist(self, min_hist):
        """Sets the min_hist of this TransferStatus.

        Replication statistics within the last minute, per provider.  # noqa: E501

        :param min_hist: The min_hist of this TransferStatus.  # noqa: E501
        :type: dict(str, list[int])
        """
        if min_hist is None:
            raise ValueError("Invalid value for `min_hist`, must not be `None`")  # noqa: E501

        self._min_hist = min_hist

    @property
    def hr_hist(self):
        """Gets the hr_hist of this TransferStatus.  # noqa: E501

        Replication statistics within the last hour, per provider.  # noqa: E501

        :return: The hr_hist of this TransferStatus.  # noqa: E501
        :rtype: dict(str, list[int])
        """
        return self._hr_hist

    @hr_hist.setter
    def hr_hist(self, hr_hist):
        """Sets the hr_hist of this TransferStatus.

        Replication statistics within the last hour, per provider.  # noqa: E501

        :param hr_hist: The hr_hist of this TransferStatus.  # noqa: E501
        :type: dict(str, list[int])
        """
        if hr_hist is None:
            raise ValueError("Invalid value for `hr_hist`, must not be `None`")  # noqa: E501

        self._hr_hist = hr_hist

    @property
    def dy_hist(self):
        """Gets the dy_hist of this TransferStatus.  # noqa: E501

        Replication statistics within the last day, per provider.  # noqa: E501

        :return: The dy_hist of this TransferStatus.  # noqa: E501
        :rtype: dict(str, list[int])
        """
        return self._dy_hist

    @dy_hist.setter
    def dy_hist(self, dy_hist):
        """Sets the dy_hist of this TransferStatus.

        Replication statistics within the last day, per provider.  # noqa: E501

        :param dy_hist: The dy_hist of this TransferStatus.  # noqa: E501
        :type: dict(str, list[int])
        """
        if dy_hist is None:
            raise ValueError("Invalid value for `dy_hist`, must not be `None`")  # noqa: E501

        self._dy_hist = dy_hist

    @property
    def mth_hist(self):
        """Gets the mth_hist of this TransferStatus.  # noqa: E501

        Replication statistics within the last month, per provider.  # noqa: E501

        :return: The mth_hist of this TransferStatus.  # noqa: E501
        :rtype: dict(str, list[int])
        """
        return self._mth_hist

    @mth_hist.setter
    def mth_hist(self, mth_hist):
        """Sets the mth_hist of this TransferStatus.

        Replication statistics within the last month, per provider.  # noqa: E501

        :param mth_hist: The mth_hist of this TransferStatus.  # noqa: E501
        :type: dict(str, list[int])
        """
        if mth_hist is None:
            raise ValueError("Invalid value for `mth_hist`, must not be `None`")  # noqa: E501

        self._mth_hist = mth_hist

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
        if issubclass(TransferStatus, dict):
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
        if not isinstance(other, TransferStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
