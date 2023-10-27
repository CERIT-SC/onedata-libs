# onepanel_client.OnezoneClusterApi

All URIs are relative to */api/v3/onepanel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_zone_databases**](OnezoneClusterApi.md#add_zone_databases) | **POST** /zone/databases | Add zone databases
[**add_zone_managers**](OnezoneClusterApi.md#add_zone_managers) | **POST** /zone/managers | Add zone cluster managers
[**add_zone_workers**](OnezoneClusterApi.md#add_zone_workers) | **POST** /zone/workers | Add zone cluster workers
[**configure_zone**](OnezoneClusterApi.md#configure_zone) | **POST** /zone/configuration | Configure zone deployment
[**get_zone_cluster_ips**](OnezoneClusterApi.md#get_zone_cluster_ips) | **GET** /zone/cluster_ips | Get zone cluster nodes IPs
[**get_zone_configuration**](OnezoneClusterApi.md#get_zone_configuration) | **GET** /zone/configuration | Get zone cluster configuration
[**get_zone_database_status**](OnezoneClusterApi.md#get_zone_database_status) | **GET** /zone/databases/{host} | Get zone database status
[**get_zone_databases_status**](OnezoneClusterApi.md#get_zone_databases_status) | **GET** /zone/databases | Get zone databases status
[**get_zone_manager_status**](OnezoneClusterApi.md#get_zone_manager_status) | **GET** /zone/managers/{host} | Get zone cluster manager status
[**get_zone_managers_status**](OnezoneClusterApi.md#get_zone_managers_status) | **GET** /zone/managers | Get zone cluster managers status
[**get_zone_nagios_report**](OnezoneClusterApi.md#get_zone_nagios_report) | **GET** /zone/nagios | Get zone nagios report
[**get_zone_worker_status**](OnezoneClusterApi.md#get_zone_worker_status) | **GET** /zone/workers/{host} | Get zone cluster worker status
[**get_zone_workers_status**](OnezoneClusterApi.md#get_zone_workers_status) | **GET** /zone/workers | Get zone cluster workers status
[**modify_zone_cluster_ips**](OnezoneClusterApi.md#modify_zone_cluster_ips) | **PATCH** /zone/cluster_ips | Set external IPs of nodes in application config
[**start_stop_zone_databases**](OnezoneClusterApi.md#start_stop_zone_databases) | **PATCH** /zone/databases | Start/stop zone databases
[**start_stop_zone_databases_host**](OnezoneClusterApi.md#start_stop_zone_databases_host) | **PATCH** /zone/databases/{host} | Start/stop zone database
[**start_stop_zone_manager**](OnezoneClusterApi.md#start_stop_zone_manager) | **PATCH** /zone/managers/{host} | Start/stop zone cluster manager
[**start_stop_zone_managers**](OnezoneClusterApi.md#start_stop_zone_managers) | **PATCH** /zone/managers | Start/stop zone cluster managers
[**start_stop_zone_worker**](OnezoneClusterApi.md#start_stop_zone_worker) | **PATCH** /zone/workers/{host} | Start/stop zone cluster worker
[**start_stop_zone_workers**](OnezoneClusterApi.md#start_stop_zone_workers) | **PATCH** /zone/workers | Start/stop zone cluster workers

# **add_zone_databases**
> TaskId add_zone_databases(body)

Add zone databases

Deploys a database service on provided hosts.

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.OnezoneClusterApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.ServiceDatabases() # ServiceDatabases | The service hosts configuration where databases should be deployed.


try:
    # Add zone databases
    api_response = api_instance.add_zone_databases(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OnezoneClusterApi->add_zone_databases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceDatabases**](ServiceDatabases.md)| The service hosts configuration where databases should be deployed.
 | 

### Return type

[**TaskId**](TaskId.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_zone_managers**
> TaskId add_zone_managers(body)

Add zone cluster managers

Deploys a cluster manager service on provided hosts.

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.OnezoneClusterApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.ManagerHosts() # ManagerHosts | The hosts specification where cluster managers should be deployed.


try:
    # Add zone cluster managers
    api_response = api_instance.add_zone_managers(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OnezoneClusterApi->add_zone_managers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ManagerHosts**](ManagerHosts.md)| The hosts specification where cluster managers should be deployed.
 | 

### Return type

[**TaskId**](TaskId.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_zone_workers**
> TaskId add_zone_workers(body)

Add zone cluster workers

Deploys a cluster worker service on provided hosts.

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.OnezoneClusterApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.ServiceHosts() # ServiceHosts | The hosts specification where the workers should be deployed.

try:
    # Add zone cluster workers
    api_response = api_instance.add_zone_workers(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OnezoneClusterApi->add_zone_workers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceHosts**](ServiceHosts.md)| The hosts specification where the workers should be deployed. | 

### Return type

[**TaskId**](TaskId.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configure_zone**
> TaskId configure_zone(body)

Configure zone deployment

Configures and starts zone services, such as database, cluster manager and cluster worker. This request can be executed by unauthorized users as long as there are no admin users in the system. 

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.OnezoneClusterApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.ZoneConfiguration() # ZoneConfiguration | The zone configuration description.

try:
    # Configure zone deployment
    api_response = api_instance.configure_zone(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OnezoneClusterApi->configure_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ZoneConfiguration**](ZoneConfiguration.md)| The zone configuration description. | 

### Return type

[**TaskId**](TaskId.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_cluster_ips**
> ClusterIps get_zone_cluster_ips()

Get zone cluster nodes IPs

Returns IPs of nodes in zone cluster.

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.OnezoneClusterApi(onepanel_client.ApiClient(configuration))

try:
    # Get zone cluster nodes IPs
    api_response = api_instance.get_zone_cluster_ips()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OnezoneClusterApi->get_zone_cluster_ips: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterIps**](ClusterIps.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_configuration**
> ZoneConfigurationDetails get_zone_configuration()

Get zone cluster configuration

Returns the zone cluster configuration.

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.OnezoneClusterApi(onepanel_client.ApiClient(configuration))

try:
    # Get zone cluster configuration
    api_response = api_instance.get_zone_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OnezoneClusterApi->get_zone_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ZoneConfigurationDetails**](ZoneConfigurationDetails.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_database_status**
> ServiceStatusHost get_zone_database_status(host)

Get zone database status

Returns status of database service on the selected host.

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.OnezoneClusterApi(onepanel_client.ApiClient(configuration))
host = 'host_example' # str | The name of a host for which database service status should be returned. 

try:
    # Get zone database status
    api_response = api_instance.get_zone_database_status(host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OnezoneClusterApi->get_zone_database_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| The name of a host for which database service status should be returned.  | 

### Return type

[**ServiceStatusHost**](ServiceStatusHost.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_databases_status**
> ServiceStatus get_zone_databases_status()

Get zone databases status

Returns status of database service on each host where it has been deployed. 

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.OnezoneClusterApi(onepanel_client.ApiClient(configuration))

try:
    # Get zone databases status
    api_response = api_instance.get_zone_databases_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OnezoneClusterApi->get_zone_databases_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceStatus**](ServiceStatus.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_manager_status**
> ServiceStatusHost get_zone_manager_status(host)

Get zone cluster manager status

Returns status of cluster manager service on the selected host.

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.OnezoneClusterApi(onepanel_client.ApiClient(configuration))
host = 'host_example' # str | The name of a host for which cluster manager service status should be returned. 

try:
    # Get zone cluster manager status
    api_response = api_instance.get_zone_manager_status(host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OnezoneClusterApi->get_zone_manager_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| The name of a host for which cluster manager service status should be returned.  | 

### Return type

[**ServiceStatusHost**](ServiceStatusHost.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_managers_status**
> ServiceStatus get_zone_managers_status()

Get zone cluster managers status

Returns status of cluster manager service on each host where it has been eployed. 

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.OnezoneClusterApi(onepanel_client.ApiClient(configuration))

try:
    # Get zone cluster managers status
    api_response = api_instance.get_zone_managers_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OnezoneClusterApi->get_zone_managers_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceStatus**](ServiceStatus.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_nagios_report**
> get_zone_nagios_report()

Get zone nagios report

Returns the zone nagios report.

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.OnezoneClusterApi(onepanel_client.ApiClient(configuration))

try:
    # Get zone nagios report
    api_instance.get_zone_nagios_report()
except ApiException as e:
    print("Exception when calling OnezoneClusterApi->get_zone_nagios_report: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_worker_status**
> ServiceStatusHost get_zone_worker_status(host)

Get zone cluster worker status

Returns status of cluster worker service on the selected host.

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.OnezoneClusterApi(onepanel_client.ApiClient(configuration))
host = 'host_example' # str | The name of a host for which cluster worker service status should be returned. 

try:
    # Get zone cluster worker status
    api_response = api_instance.get_zone_worker_status(host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OnezoneClusterApi->get_zone_worker_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| The name of a host for which cluster worker service status should be returned.  | 

### Return type

[**ServiceStatusHost**](ServiceStatusHost.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_workers_status**
> ServiceStatus get_zone_workers_status()

Get zone cluster workers status

Returns status of cluster worker service on each host where it has been deployed. 

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.OnezoneClusterApi(onepanel_client.ApiClient(configuration))

try:
    # Get zone cluster workers status
    api_response = api_instance.get_zone_workers_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OnezoneClusterApi->get_zone_workers_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceStatus**](ServiceStatus.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_zone_cluster_ips**
> modify_zone_cluster_ips(body)

Set external IPs of nodes in application config

Informs cluster nodes about external IPs which can be used to access them by other zones. 

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.OnezoneClusterApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.ModifyClusterIps() # ModifyClusterIps | The zone configuration description.

try:
    # Set external IPs of nodes in application config
    api_instance.modify_zone_cluster_ips(body)
except ApiException as e:
    print("Exception when calling OnezoneClusterApi->modify_zone_cluster_ips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModifyClusterIps**](ModifyClusterIps.md)| The zone configuration description. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_stop_zone_databases**
> start_stop_zone_databases(started=started)

Start/stop zone databases

Starts or stops database service on all hosts in the local deployment. 

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.OnezoneClusterApi(onepanel_client.ApiClient(configuration))
started = true # bool | Defines the intended state of the database service. The service will be started or stopped in order to match the requested state.  (optional) (default to true)

try:
    # Start/stop zone databases
    api_instance.start_stop_zone_databases(started=started)
except ApiException as e:
    print("Exception when calling OnezoneClusterApi->start_stop_zone_databases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **started** | **bool**| Defines the intended state of the database service. The service will be started or stopped in order to match the requested state.  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_stop_zone_databases_host**
> start_stop_zone_databases_host(host, started=started)

Start/stop zone database

Starts or stops database service on the selected hosts in the local deployment. 

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.OnezoneClusterApi(onepanel_client.ApiClient(configuration))
host = 'host_example' # str | The name of a host for which database service status should be changed. 
started = true # bool | Defines the intended state of the database service. The service will be started or stopped in order to match the requested state.  (optional) (default to true)

try:
    # Start/stop zone database
    api_instance.start_stop_zone_databases_host(host, started=started)
except ApiException as e:
    print("Exception when calling OnezoneClusterApi->start_stop_zone_databases_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| The name of a host for which database service status should be changed.  | 
 **started** | **bool**| Defines the intended state of the database service. The service will be started or stopped in order to match the requested state.  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_stop_zone_manager**
> start_stop_zone_manager(host, started=started)

Start/stop zone cluster manager

Starts or stops cluster manager service on the selected hosts in the local deployment. 

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.OnezoneClusterApi(onepanel_client.ApiClient(configuration))
host = 'host_example' # str | The name of a host for which cluster manager service status should be changed. 
started = true # bool | Defines the intended state of the cluster manager service. The service will be started or stopped in order to match the requested state.  (optional) (default to true)

try:
    # Start/stop zone cluster manager
    api_instance.start_stop_zone_manager(host, started=started)
except ApiException as e:
    print("Exception when calling OnezoneClusterApi->start_stop_zone_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| The name of a host for which cluster manager service status should be changed.  | 
 **started** | **bool**| Defines the intended state of the cluster manager service. The service will be started or stopped in order to match the requested state.  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_stop_zone_managers**
> start_stop_zone_managers(started=started)

Start/stop zone cluster managers

Starts or stops cluster manager service on all hosts in the local deployment. 

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.OnezoneClusterApi(onepanel_client.ApiClient(configuration))
started = true # bool | Defines the intended state of the cluster manager service. The service will be started or stopped in order to match the requested state.  (optional) (default to true)

try:
    # Start/stop zone cluster managers
    api_instance.start_stop_zone_managers(started=started)
except ApiException as e:
    print("Exception when calling OnezoneClusterApi->start_stop_zone_managers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **started** | **bool**| Defines the intended state of the cluster manager service. The service will be started or stopped in order to match the requested state.  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_stop_zone_worker**
> start_stop_zone_worker(host, started=started)

Start/stop zone cluster worker

Starts or stops cluster worker service on the selected hosts in the local deployment. 

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.OnezoneClusterApi(onepanel_client.ApiClient(configuration))
host = 'host_example' # str | The name of a host for which cluster worker service status should be changed. 
started = true # bool | Defines the intended state of the cluster worker service. The service will be started or stopped in order to match the requested state.  (optional) (default to true)

try:
    # Start/stop zone cluster worker
    api_instance.start_stop_zone_worker(host, started=started)
except ApiException as e:
    print("Exception when calling OnezoneClusterApi->start_stop_zone_worker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| The name of a host for which cluster worker service status should be changed.  | 
 **started** | **bool**| Defines the intended state of the cluster worker service. The service will be started or stopped in order to match the requested state.  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_stop_zone_workers**
> start_stop_zone_workers(started=started)

Start/stop zone cluster workers

Starts or stops cluster worker service on all hosts in the local deployment. 

### Example
```python
from __future__ import print_function
import time
import onepanel_client
from onepanel_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onepanel_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onepanel_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onepanel_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onepanel_client.OnezoneClusterApi(onepanel_client.ApiClient(configuration))
started = true # bool | Defines the intended state of the cluster worker service. The service will be started or stopped in order to match the requested state.  (optional) (default to true)

try:
    # Start/stop zone cluster workers
    api_instance.start_stop_zone_workers(started=started)
except ApiException as e:
    print("Exception when calling OnezoneClusterApi->start_stop_zone_workers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **started** | **bool**| Defines the intended state of the cluster worker service. The service will be started or stopped in order to match the requested state.  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

