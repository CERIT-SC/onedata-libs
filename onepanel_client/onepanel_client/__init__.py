# coding: utf-8

# flake8: noqa

"""
    Onepanel

    # Overview  This is the RESTful API definition of **Onepanel** component of Onedata data management system [onedata.org](http://onedata.org).  > This API is defined using [Swagger](http://swagger.io/), the JSON specification can be used to automatically generate client libraries -   [swagger.json](../../../swagger/onepanel/swagger.json).  This API allows control and configuration of local Onedata deployment, in particular full control over the **Onezone** and **Oneprovider** services and their distribution and monitoring on the local resources.  The API is grouped into 3 categories of operations:   * **Onepanel** - for common operations   * **Oneprovider** - for Oneprovider specific administrative operations   * **Onezone** - for Onezone specific administrative operations  Each of these components is composed of the following services:   * **Worker services** - these are available under `/zone/workers` and     `/provider/workers` paths,   * **Databases services** - each Onedata component stores it's metadata in a     Couchbase backend, which can be distributed on any number of nodes, these     are available under `/zone/databases` and `/provider/databases` paths,   * **Cluster manager services** - this is a service which controls other     deployed processes in one site, these are availables under these are     available under `/zone/managers` and `/provider/managers` paths.  **Onezone** and **Oneprovider** components are composed of 3 types of services: **managers**, **databases** and **workers**.  Using this API each of these components can be deployed, configured, started and stopped on a specified host in the local site, in the context of either **Onezone** or **Oneprovider** service.  All paths listed in this documentation are relative to the base Onepanel REST API which is `/api/v3/onepanel`, so complete URL for a request to Onepanel service is:  ``` http://HOSTNAME:PORT/api/v3/onepanel/... ```  ## Authentication  ### Token authentication  The recommended, safest way of authenticating requests to Onepanel API is using the **Onedata access tokens**. The token should be present in `X-Auth-Token` or `Authorization: Bearer` header. See [Onezone documentation](/#/home/api/latest/onezone?anchor=section/Overview/Authentication-and-authorization) for detailed explanation of the token concepts.  Curl examples: ```bash curl -H \"X-Auth-Token: $TOKEN\" [...] curl -H \"Authorization: Bearer $TOKEN\" [...] curl -H \"Macaroon: $TOKEN\" [...]   # DEPRECATED ```   ### Passphrase authentication  The token authentication dependes on the Onezone service. In special cases - during Onezone deployment or its outage - it is necessary to use the local **emergency passphrase**.  The passphrase should be provided in a Basic authentication header with username `onepanel`. For curl users this means ```bash curl -u onepanel:TheEmergencyPassphrase ```  The passphrase can also be sent without any username, as the whole content of base64-encoded string in Basic authorization header, e.g. ```bash curl -H \"Authorization: Basic $(echo -n TheEmergencyPassphrase | base64)\" ```  The passphrase is set during deployment. It can be changed in the Onepanel GUI or with an API request: ```bash curl -X PUT 'https://$PANEL_HOST:9443/api/v3/onepanel/emergency_passphrase' \\ -u onepanel:TheEmergencyPassphrase -H 'Content-Type: application/json' \\ -d '{\"currentPassphrase\": \"TheEmergencyPassphrase\", \"newPassphrase\": \"TheNewPassphrase\"}' ```  ## API structure  The Onepanel API is structured to reflect that it can either be used to control **Onezone** or **Oneprovider** deployment, each Onedata component deployment has a separate Onepanel instance. In order to make the API calls explicit, **Onezone** or **Oneprovider** specific requests have different paths, i.e.:   * Onezone specific operations start with `/api/v3/onepanel/zone/`   * Oneprovider specific operations start with `/api/v3/onepanel/provider/`   * Common operations paths include `/api/v3/onepanel/users`,     `/api/v3/onepanel/hosts` and `/api/v3/onepanel/tasks`  The overall configuration of each component can be controlled by updating `/api/v3/onepanel/zone/configuration` and `/api/v3/onepanel/provider/configuration` resources.  ## Examples  Below are some example requests to Onepanel using cURL:  **Add storage resource to provider** ```bash curl -X POST -u onepanel:Passphrase1 -k -vvv -H \"content-type: application/json\" \\ -d '{\"NFS\": {\"type\": \"posix\", \"mountPoint\": \"/mnt/vfs\"}}' \\ https://172.17.0.4:9443/api/v3/onepanel/provider/storages ```  **Add a new Onezone worker** ```bash curl -X POST -u onepanel:Passphrase1 -k -vvv -H \"content-type: application/json\" \\ -d '{\"hosts\": [\"node1.p1.1.dev\"]}' \\ https://172.17.0.4:9443/api/v3/onepanel/zone/workers ```   # noqa: E501

    OpenAPI spec version: 21.02.3
    Contact: info@onedata.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from onepanel_client.api.auto_cleaning_api import AutoCleaningApi
from onepanel_client.api.ceph_api import CephApi
from onepanel_client.api.cluster_api import ClusterApi
from onepanel_client.api.current_user_api import CurrentUserApi
from onepanel_client.api.dns_api import DNSApi
from onepanel_client.api.debug_api import DebugApi
from onepanel_client.api.file_popularity_api import FilePopularityApi
from onepanel_client.api.internal_api import InternalApi
from onepanel_client.api.luma_db_api import LUMADBApi
from onepanel_client.api.luma_db_local_feed_api import LUMADBLocalFeedApi
from onepanel_client.api.oneprovider_cluster_api import OneproviderClusterApi
from onepanel_client.api.oneprovider_identity_api import OneproviderIdentityApi
from onepanel_client.api.onezone_cluster_api import OnezoneClusterApi
from onepanel_client.api.security_api import SecurityApi
from onepanel_client.api.service_configuration_api import ServiceConfigurationApi
from onepanel_client.api.space_support_api import SpaceSupportApi
from onepanel_client.api.storage_import_api import StorageImportApi
from onepanel_client.api.storages_api import StoragesApi
from onepanel_client.api.user_management_api import UserManagementApi
# import ApiClient
from onepanel_client.api_client import ApiClient
from onepanel_client.configuration import Configuration
# import models into sdk package
from onepanel_client.models.auto_storage_import_config import AutoStorageImportConfig
from onepanel_client.models.auto_storage_import_info import AutoStorageImportInfo
from onepanel_client.models.auto_storage_import_stats import AutoStorageImportStats
from onepanel_client.models.block_devices import BlockDevices
from onepanel_client.models.block_devices_block_devices import BlockDevicesBlockDevices
from onepanel_client.models.blockdevice import Blockdevice
from onepanel_client.models.ceph import Ceph
from onepanel_client.models.ceph_cluster import CephCluster
from onepanel_client.models.ceph_credentials import CephCredentials
from onepanel_client.models.ceph_global_params import CephGlobalParams
from onepanel_client.models.ceph_manager import CephManager
from onepanel_client.models.ceph_managers import CephManagers
from onepanel_client.models.ceph_modify import CephModify
from onepanel_client.models.ceph_monitor import CephMonitor
from onepanel_client.models.ceph_monitors import CephMonitors
from onepanel_client.models.ceph_osd import CephOsd
from onepanel_client.models.ceph_osds import CephOsds
from onepanel_client.models.ceph_pool import CephPool
from onepanel_client.models.ceph_pool_usage import CephPoolUsage
from onepanel_client.models.ceph_pools import CephPools
from onepanel_client.models.ceph_status import CephStatus
from onepanel_client.models.ceph_usage import CephUsage
from onepanel_client.models.cephrados import Cephrados
from onepanel_client.models.cephrados_credentials import CephradosCredentials
from onepanel_client.models.cephrados_modify import CephradosModify
from onepanel_client.models.cluster_configuration_details import ClusterConfigurationDetails
from onepanel_client.models.cluster_databases import ClusterDatabases
from onepanel_client.models.cluster_details import ClusterDetails
from onepanel_client.models.cluster_ips import ClusterIps
from onepanel_client.models.cluster_managers import ClusterManagers
from onepanel_client.models.cluster_members_summary import ClusterMembersSummary
from onepanel_client.models.cluster_workers import ClusterWorkers
from onepanel_client.models.configuration import Configuration
from onepanel_client.models.current_user import CurrentUser
from onepanel_client.models.data_usage import DataUsage
from onepanel_client.models.database_hosts import DatabaseHosts
from onepanel_client.models.dns_check import DnsCheck
from onepanel_client.models.dns_check_configuration import DnsCheckConfiguration
from onepanel_client.models.dns_check_result import DnsCheckResult
from onepanel_client.models.embeddedceph import Embeddedceph
from onepanel_client.models.embeddedceph_modify import EmbeddedcephModify
from onepanel_client.models.emergency_passphrase_change_request import EmergencyPassphraseChangeRequest
from onepanel_client.models.emergency_passphrase_status import EmergencyPassphraseStatus
from onepanel_client.models.error import Error
from onepanel_client.models.error_details import ErrorDetails
from onepanel_client.models.glusterfs import Glusterfs
from onepanel_client.models.glusterfs_credentials import GlusterfsCredentials
from onepanel_client.models.glusterfs_modify import GlusterfsModify
from onepanel_client.models.gui_message import GuiMessage
from onepanel_client.models.http import HTTP
from onepanel_client.models.http_credentials import HTTPCredentials
from onepanel_client.models.http_modify import HTTPModify
from onepanel_client.models.host import Host
from onepanel_client.models.host_add_request import HostAddRequest
from onepanel_client.models.id import Id
from onepanel_client.models.ids import Ids
from onepanel_client.models.inline_response202 import InlineResponse202
from onepanel_client.models.invite_token import InviteToken
from onepanel_client.models.loopdevice import Loopdevice
from onepanel_client.models.luma_config import LumaConfig
from onepanel_client.models.luma_idp_entitlement_scheme import LumaIdpEntitlementScheme
from onepanel_client.models.luma_idp_user_scheme import LumaIdpUserScheme
from onepanel_client.models.luma_onedata_group import LumaOnedataGroup
from onepanel_client.models.luma_onedata_group_scheme import LumaOnedataGroupScheme
from onepanel_client.models.luma_onedata_user import LumaOnedataUser
from onepanel_client.models.luma_onedata_user_scheme import LumaOnedataUserScheme
from onepanel_client.models.luma_storage_credentials import LumaStorageCredentials
from onepanel_client.models.luma_storage_user import LumaStorageUser
from onepanel_client.models.luma_user_mapping import LumaUserMapping
from onepanel_client.models.manager_hosts import ManagerHosts
from onepanel_client.models.manual_storage_import_example import ManualStorageImportExample
from onepanel_client.models.modify_cluster_ips import ModifyClusterIps
from onepanel_client.models.nfs import NFS
from onepanel_client.models.nfs_credentials import NFSCredentials
from onepanel_client.models.nfs_modify import NFSModify
from onepanel_client.models.node import Node
from onepanel_client.models.nulldevice import Nulldevice
from onepanel_client.models.nulldevice_credentials import NulldeviceCredentials
from onepanel_client.models.nulldevice_modify import NulldeviceModify
from onepanel_client.models.onezone_info import OnezoneInfo
from onepanel_client.models.onezone_user import OnezoneUser
from onepanel_client.models.onezone_user_create_request import OnezoneUserCreateRequest
from onepanel_client.models.op_configuration import OpConfiguration
from onepanel_client.models.oz_configuration import OzConfiguration
from onepanel_client.models.panel_configuration import PanelConfiguration
from onepanel_client.models.password_change_request import PasswordChangeRequest
from onepanel_client.models.posix import Posix
from onepanel_client.models.posix_compatible_credentials import PosixCompatibleCredentials
from onepanel_client.models.posix_credentials import PosixCredentials
from onepanel_client.models.posix_modify import PosixModify
from onepanel_client.models.progress import Progress
from onepanel_client.models.progress_modify import ProgressModify
from onepanel_client.models.provider_cluster_configuration import ProviderClusterConfiguration
from onepanel_client.models.provider_configuration import ProviderConfiguration
from onepanel_client.models.provider_configuration_details import ProviderConfigurationDetails
from onepanel_client.models.provider_configuration_details_oneprovider import ProviderConfigurationDetailsOneprovider
from onepanel_client.models.provider_configuration_oneprovider import ProviderConfigurationOneprovider
from onepanel_client.models.provider_details import ProviderDetails
from onepanel_client.models.provider_modify_request import ProviderModifyRequest
from onepanel_client.models.provider_register_request import ProviderRegisterRequest
from onepanel_client.models.provider_spaces import ProviderSpaces
from onepanel_client.models.provider_storages import ProviderStorages
from onepanel_client.models.remote_provider_details import RemoteProviderDetails
from onepanel_client.models.s3 import S3
from onepanel_client.models.s3_credentials import S3Credentials
from onepanel_client.models.s3_modify import S3Modify
from onepanel_client.models.service_databases import ServiceDatabases
from onepanel_client.models.service_hosts import ServiceHosts
from onepanel_client.models.service_status import ServiceStatus
from onepanel_client.models.service_status_host import ServiceStatusHost
from onepanel_client.models.space_auto_cleaning_configuration import SpaceAutoCleaningConfiguration
from onepanel_client.models.space_auto_cleaning_report import SpaceAutoCleaningReport
from onepanel_client.models.space_auto_cleaning_reports import SpaceAutoCleaningReports
from onepanel_client.models.space_auto_cleaning_rule_setting import SpaceAutoCleaningRuleSetting
from onepanel_client.models.space_auto_cleaning_rules import SpaceAutoCleaningRules
from onepanel_client.models.space_auto_cleaning_status import SpaceAutoCleaningStatus
from onepanel_client.models.space_details import SpaceDetails
from onepanel_client.models.space_file_popularity_configuration import SpaceFilePopularityConfiguration
from onepanel_client.models.space_modify_request import SpaceModifyRequest
from onepanel_client.models.space_support_request import SpaceSupportRequest
from onepanel_client.models.storage_create_details import StorageCreateDetails
from onepanel_client.models.storage_create_request import StorageCreateRequest
from onepanel_client.models.storage_create_response import StorageCreateResponse
from onepanel_client.models.storage_get_details import StorageGetDetails
from onepanel_client.models.storage_import import StorageImport
from onepanel_client.models.storage_modify_details import StorageModifyDetails
from onepanel_client.models.storage_modify_request import StorageModifyRequest
from onepanel_client.models.swift import Swift
from onepanel_client.models.swift_credentials import SwiftCredentials
from onepanel_client.models.swift_modify import SwiftModify
from onepanel_client.models.task_id import TaskId
from onepanel_client.models.task_status import TaskStatus
from onepanel_client.models.time_stats import TimeStats
from onepanel_client.models.token import Token
from onepanel_client.models.transfers_mock import TransfersMock
from onepanel_client.models.version_info import VersionInfo
from onepanel_client.models.web_cert import WebCert
from onepanel_client.models.web_cert_modify_request import WebCertModifyRequest
from onepanel_client.models.web_cert_paths import WebCertPaths
from onepanel_client.models.webdav import Webdav
from onepanel_client.models.webdav_credentials import WebdavCredentials
from onepanel_client.models.webdav_modify import WebdavModify
from onepanel_client.models.worker_hosts import WorkerHosts
from onepanel_client.models.x_root_d import XRootD
from onepanel_client.models.x_root_d_credentials import XRootDCredentials
from onepanel_client.models.x_root_d_modify import XRootDModify
from onepanel_client.models.zone_cluster_configuration import ZoneClusterConfiguration
from onepanel_client.models.zone_cluster_configuration_nodes import ZoneClusterConfigurationNodes
from onepanel_client.models.zone_configuration import ZoneConfiguration
from onepanel_client.models.zone_configuration_details import ZoneConfigurationDetails
from onepanel_client.models.zone_configuration_details_onezone import ZoneConfigurationDetailsOnezone
from onepanel_client.models.zone_configuration_onezone import ZoneConfigurationOnezone
from onepanel_client.models.zone_policies import ZonePolicies
