# coding: utf-8

# flake8: noqa

"""
    Oneprovider

    # Overview  This is the RESTful API definition of Oneprovider component of Onedata data management system [onedata.org](http://onedata.org).  > This API is defined using [Swagger](http://swagger.io/), the JSON specification can be used to automatically generate > client libraries - [swagger.json](../../../swagger/oneprovider/swagger.json).  All paths below are relative to a common Oneprovider basepath which is `/api/v3/oneprovider`, thus a complete example query for 'mode' file attributes would be: ``` https://ONEPROVIDER_HOSTNAME/api/v3/oneprovider/data/$FILE_ID?attribute=mode ``` Please note that currently the default port for Oneprovider instances is `443`.  In addition to REST API, Oneprovider also provides support for [CDMI](http://onedata.org/#/home/documentation/doc/advanced/cdmi.html) protocol.   ## Authentication To use the APIs, the REST client must authenticate with the Oneprovider service and present a proof of authorization to perform a specific operation. This is done using access tokens, which can be generated using the Onedata GUI or Onezone's REST API.  The token is passed in the request header like this: ``` X-Auth-Token: MIIFrzCCA5egAwIBAgIBEzANBgkqhkiG9w0BAQUFADBcMQswCQYDVQQGEwJQTDET... ```  The authorization to perform a specific operation depends on the authenticated user's privileges in the corresponding space, file level permissions (posix, ACL) and caveats (restrictions) inscribed in the provided access token.   ## Data management basics The Onedata system organizes all user data into logical containers called spaces. <!--- TODO VFS-7218 uncomment when the new docs are deployed --> <!--- For more information, please refer to the [documentation](https://onedata.org/#/home/documentation). -->  Files and directories in Onedata can be globally identified using unique File Ids or logical paths. Whenever possible, it is recommended to use File Ids, due to better performance and no need for escaping or encoding.  ### File path All logical paths in Onedata use the slash (`/`) delimiter and must start with a space name: ```lang-none /CMS 1/file.txt /MyExperiment/directory/subdirectory/image.jpg ```  When referencing files by path in the REST API, make sure to urlencode the path in the URL: ```bash {...}/CMS%201/file.txt ```  ### File Id  File Id is a unique, global identifier associated with a file or directory and can be used universally in the REST and CDMI APIs. There are several ways to find out the File Id of given file or directory: <!---  @TODO VFS-7218 remove redundant information and provide a link to the new docs -->  **Web GUI** - click on Information in the file/directory context menu and look for File Id.  **REST API** - use the File Id resolution endpoint. Below example returns the File Id of `/CMS 1/file.txt`, where `CMS 1` is the space name:  ```bash curl -H \"X-Auth-Token: ${ACCESS_TOKEN}\" \\ -X POST \"https://${ONEPROVIDER_DOMAIN}/api/v3/oneprovider/lookup-file-id/CMS%201/file.txt\" {     \"fileId\": \"094576776E667431723230677767776C6B497031394E445F6E3868677873...\" } ```  ### Space Id  Space Id is a unique, global identifier associated with a space and can be used universally in the REST APIs. In order to find out the Space Id:  **Web GUI** - click on Information in the file/directory context menu and look for Space Id.  **REST API** - use the [Get all user spaces](#operation/get_all_spaces) endpoint.  The Space Id can be used interchangeably with the space root directory's File Id in the path-based enpoints.  **Remove specific file relative to the space root** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_ID/path/dir1/file.txt\" # is equivalent to curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_ROOT_FILE_ID/path/dir1/file.txt\" ``` **Remove specific file relative to any parent directory** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$PARENT_FILE_ID/path/dir1/file.txt\" ```   ## API structure  The API is divided into the following sections:  ### Space management These methods provide means for getting basic information about spaces directly from the Oneprovider service, but also allows to define database views.  ### File access and management The API provides capabilities for:   - browsing files in spaces and directories,   - creating and deleting files as well as updating their content   - querying for file attributes, such as 'mode' file permissions and updating them,   - managing custom file metadata (xattrs, JSON, RDF),   - manual registration of files for imported storages.  More information can be found [here](#section/Overview/Data-management-basics).  ### Replica and QoS management These methods allow viewing file replica distribution, requesting file replication (transfers) between Oneproviders, viewing ongoing and historical transfers data, as well as managing QoS requirements that trigger automatic replication according to the QoS rules.  ### Share management Offers methods for creating, modyfying and deleting shares. Shares are files or directories that were made publicly available, so that they can be viewed by everyone through a public URL.  ### Dataset & archive management API for managing datasets - designated files or directories that are used to facilitate building collections of data meaningful for the users with additional features, such as write protection and archivisation mechanisms.  ### Automation Basic API for scheduling and viewing workflow executions.  ### Monitoring The API provides means for subscribing (through HTTP long-polling technique) for file related events such as reads, writes or deletes which are returned as complete file metadata records with sequence numbers representing their current version.  ### Service information Publicly available, basic configuration of the Oneprovider service.  Detailed examples of API usage are available in the documentation of each operation.   # noqa: E501

    OpenAPI spec version: 21.02.3
    Contact: info@onedata.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from oneprovider_client.api.archive_api import ArchiveApi
from oneprovider_client.api.basic_file_operations_api import BasicFileOperationsApi
from oneprovider_client.api.custom_file_metadata_api import CustomFileMetadataApi
from oneprovider_client.api.dataset_api import DatasetApi
from oneprovider_client.api.file_distribution_api import FileDistributionApi
from oneprovider_client.api.file_path_resolution_api import FilePathResolutionApi
from oneprovider_client.api.miscellaneous_api import MiscellaneousApi
from oneprovider_client.api.monitoring_api import MonitoringApi
from oneprovider_client.api.oneprovider_api import OneproviderApi
from oneprovider_client.api.qo_s_api import QoSApi
from oneprovider_client.api.share_api import ShareApi
from oneprovider_client.api.space_api import SpaceApi
from oneprovider_client.api.transfer_api import TransferApi
from oneprovider_client.api.view_api import ViewApi
from oneprovider_client.api.workflow_execution_api import WorkflowExecutionApi
# import ApiClient
from oneprovider_client.api_client import ApiClient
from oneprovider_client.configuration import Configuration
# import models into sdk package
from oneprovider_client.models.archive import Archive
from oneprovider_client.models.archive_base import ArchiveBase
from oneprovider_client.models.archive_config import ArchiveConfig
from oneprovider_client.models.archive_create_nested_archives import ArchiveCreateNestedArchives
from oneprovider_client.models.archive_create_request import ArchiveCreateRequest
from oneprovider_client.models.archive_delete_request import ArchiveDeleteRequest
from oneprovider_client.models.archive_deleted_callback import ArchiveDeletedCallback
from oneprovider_client.models.archive_description import ArchiveDescription
from oneprovider_client.models.archive_follow_symlinks import ArchiveFollowSymlinks
from oneprovider_client.models.archive_include_dip import ArchiveIncludeDip
from oneprovider_client.models.archive_incremental import ArchiveIncremental
from oneprovider_client.models.archive_layout import ArchiveLayout
from oneprovider_client.models.archive_preserved_callback import ArchivePreservedCallback
from oneprovider_client.models.archive_recall_details import ArchiveRecallDetails
from oneprovider_client.models.archive_recall_details_last_error import ArchiveRecallDetailsLastError
from oneprovider_client.models.archive_recall_progress import ArchiveRecallProgress
from oneprovider_client.models.archive_recall_request import ArchiveRecallRequest
from oneprovider_client.models.archive_recall_response import ArchiveRecallResponse
from oneprovider_client.models.archive_state import ArchiveState
from oneprovider_client.models.archive_stats import ArchiveStats
from oneprovider_client.models.archive_update_request import ArchiveUpdateRequest
from oneprovider_client.models.archives import Archives
from oneprovider_client.models.atm_workflow_execution_details import AtmWorkflowExecutionDetails
from oneprovider_client.models.atm_workflow_execution_details_lanes import AtmWorkflowExecutionDetailsLanes
from oneprovider_client.models.atm_workflow_execution_lane_run_details import AtmWorkflowExecutionLaneRunDetails
from oneprovider_client.models.atm_workflow_execution_lane_run_details_parallel_boxes import AtmWorkflowExecutionLaneRunDetailsParallelBoxes
from oneprovider_client.models.atm_workflow_execution_schedule_request import AtmWorkflowExecutionScheduleRequest
from oneprovider_client.models.configuration import Configuration
from oneprovider_client.models.dataset import Dataset
from oneprovider_client.models.dataset_establish_request import DatasetEstablishRequest
from oneprovider_client.models.dataset_protection_flags import DatasetProtectionFlags
from oneprovider_client.models.dataset_state import DatasetState
from oneprovider_client.models.dataset_summary import DatasetSummary
from oneprovider_client.models.dataset_update_request import DatasetUpdateRequest
from oneprovider_client.models.datasets import Datasets
from oneprovider_client.models.datasets_datasets import DatasetsDatasets
from oneprovider_client.models.dir_size_stats_query import DirSizeStatsQuery
from oneprovider_client.models.dir_size_stats_response import DirSizeStatsResponse
from oneprovider_client.models.directory_children import DirectoryChildren
from oneprovider_client.models.effective_file_protection_flags import EffectiveFileProtectionFlags
from oneprovider_client.models.error import Error
from oneprovider_client.models.error_json import ErrorJson
from oneprovider_client.models.file import File
from oneprovider_client.models.file_attributes import FileAttributes
from oneprovider_client.models.file_distribution import FileDistribution
from oneprovider_client.models.file_distribution_distribution_per_provider import FileDistributionDistributionPerProvider
from oneprovider_client.models.file_distribution_distribution_per_storage import FileDistributionDistributionPerStorage
from oneprovider_client.models.file_distribution_error import FileDistributionError
from oneprovider_client.models.file_registration_request import FileRegistrationRequest
from oneprovider_client.models.file_type import FileType
from oneprovider_client.models.inline_response200 import InlineResponse200
from oneprovider_client.models.inline_response2001 import InlineResponse2001
from oneprovider_client.models.inline_response2002 import InlineResponse2002
from oneprovider_client.models.inline_response2003 import InlineResponse2003
from oneprovider_client.models.inline_response2004 import InlineResponse2004
from oneprovider_client.models.inline_response201 import InlineResponse201
from oneprovider_client.models.inline_response2011 import InlineResponse2011
from oneprovider_client.models.inline_response2012 import InlineResponse2012
from oneprovider_client.models.inline_response2013 import InlineResponse2013
from oneprovider_client.models.inline_response2014 import InlineResponse2014
from oneprovider_client.models.inline_response2015 import InlineResponse2015
from oneprovider_client.models.inline_response2016 import InlineResponse2016
from oneprovider_client.models.inline_response2017 import InlineResponse2017
from oneprovider_client.models.inline_response2018 import InlineResponse2018
from oneprovider_client.models.is_last import IsLast
from oneprovider_client.models.layout import Layout
from oneprovider_client.models.list_page_token import ListPageToken
from oneprovider_client.models.metadata_changes_event import MetadataChangesEvent
from oneprovider_client.models.metadata_changes_event_custom_metadata import MetadataChangesEventCustomMetadata
from oneprovider_client.models.metadata_changes_event_file_location import MetadataChangesEventFileLocation
from oneprovider_client.models.metadata_changes_event_file_location_fields import MetadataChangesEventFileLocationFields
from oneprovider_client.models.metadata_changes_event_file_meta import MetadataChangesEventFileMeta
from oneprovider_client.models.metadata_changes_event_file_meta_fields import MetadataChangesEventFileMetaFields
from oneprovider_client.models.metadata_changes_event_times import MetadataChangesEventTimes
from oneprovider_client.models.metadata_changes_event_times_fields import MetadataChangesEventTimesFields
from oneprovider_client.models.metadata_changes_stream_request import MetadataChangesStreamRequest
from oneprovider_client.models.metadata_changes_stream_request_custom_metadata import MetadataChangesStreamRequestCustomMetadata
from oneprovider_client.models.metadata_changes_stream_request_file_location import MetadataChangesStreamRequestFileLocation
from oneprovider_client.models.metadata_changes_stream_request_file_meta import MetadataChangesStreamRequestFileMeta
from oneprovider_client.models.metadata_changes_stream_request_times import MetadataChangesStreamRequestTimes
from oneprovider_client.models.metadata_xattrs_body import MetadataXattrsBody
from oneprovider_client.models.metrics import Metrics
from oneprovider_client.models.provider import Provider
from oneprovider_client.models.qos_create_request import QosCreateRequest
from oneprovider_client.models.qos_requirement import QosRequirement
from oneprovider_client.models.qos_requirement_audit_log import QosRequirementAuditLog
from oneprovider_client.models.qos_requirement_audit_log_content import QosRequirementAuditLogContent
from oneprovider_client.models.qos_requirement_audit_log_log_entries import QosRequirementAuditLogLogEntries
from oneprovider_client.models.qos_summary import QosSummary
from oneprovider_client.models.query_view_params import QueryViewParams
from oneprovider_client.models.rrd import RRD
from oneprovider_client.models.rrd_meta import RRDMeta
from oneprovider_client.models.recursive_file_list import RecursiveFileList
from oneprovider_client.models.share import Share
from oneprovider_client.models.share_create_request import ShareCreateRequest
from oneprovider_client.models.shares import Shares
from oneprovider_client.models.shares_shid_body import SharesShidBody
from oneprovider_client.models.slice import Slice
from oneprovider_client.models.space import Space
from oneprovider_client.models.storage_details import StorageDetails
from oneprovider_client.models.storage_file_locations import StorageFileLocations
from oneprovider_client.models.storage_file_locations_locations_per_provider import StorageFileLocationsLocationsPerProvider
from oneprovider_client.models.ts_window_info import TSWindowInfo
from oneprovider_client.models.time_series_layout import TimeSeriesLayout
from oneprovider_client.models.time_series_slice import TimeSeriesSlice
from oneprovider_client.models.timestamp import Timestamp
from oneprovider_client.models.transfer_create_request import TransferCreateRequest
from oneprovider_client.models.transfer_status import TransferStatus
from oneprovider_client.models.view import View
from oneprovider_client.models.view_options import ViewOptions
from oneprovider_client.models.views import Views
from oneprovider_client.models.wid_rerun_body import WidRerunBody
from oneprovider_client.models.wid_retry_body import WidRetryBody
