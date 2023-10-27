# onepanel_client.OneproviderClusterApi

All URIs are relative to */api/v3/onepanel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_provider_databases**](OneproviderClusterApi.md#add_provider_databases) | **POST** /provider/databases | Deploy provider databases
[**add_provider_managers**](OneproviderClusterApi.md#add_provider_managers) | **POST** /provider/managers | Add provider cluster managers
[**add_provider_workers**](OneproviderClusterApi.md#add_provider_workers) | **POST** /provider/workers | Add provider cluster workers
[**configure_provider**](OneproviderClusterApi.md#configure_provider) | **POST** /provider/configuration | Configure provider deployment
[**get_provider_cluster_ips**](OneproviderClusterApi.md#get_provider_cluster_ips) | **GET** /provider/cluster_ips | Get provider cluster nodes IPs
[**get_provider_configuration**](OneproviderClusterApi.md#get_provider_configuration) | **GET** /provider/configuration | Get provider cluster configuration
[**get_provider_database_status**](OneproviderClusterApi.md#get_provider_database_status) | **GET** /provider/databases/{host} | Get provider database status
[**get_provider_databases_status**](OneproviderClusterApi.md#get_provider_databases_status) | **GET** /provider/databases | Get provider databases status
[**get_provider_manager_status**](OneproviderClusterApi.md#get_provider_manager_status) | **GET** /provider/managers/{host} | Get provider cluster manager status
[**get_provider_managers_status**](OneproviderClusterApi.md#get_provider_managers_status) | **GET** /provider/managers | Get provider cluster managers status
[**get_provider_nagios_report**](OneproviderClusterApi.md#get_provider_nagios_report) | **GET** /provider/nagios | Get provider nagios report
[**get_provider_worker_status**](OneproviderClusterApi.md#get_provider_worker_status) | **GET** /provider/workers/{host} | Get provider cluster worker status
[**get_provider_workers_status**](OneproviderClusterApi.md#get_provider_workers_status) | **GET** /provider/workers | Get provider cluster workers status
[**modify_provider_cluster_ips**](OneproviderClusterApi.md#modify_provider_cluster_ips) | **PATCH** /provider/cluster_ips | Set external IPs of nodes in application config
[**start_stop_provider_database**](OneproviderClusterApi.md#start_stop_provider_database) | **PATCH** /provider/databases/{host} | Start/stop provider database
[**start_stop_provider_databases**](OneproviderClusterApi.md#start_stop_provider_databases) | **PATCH** /provider/databases | Start/stop provider databases
[**start_stop_provider_manager**](OneproviderClusterApi.md#start_stop_provider_manager) | **PATCH** /provider/managers/{host} | Start/stop provider cluster manager
[**start_stop_provider_managers**](OneproviderClusterApi.md#start_stop_provider_managers) | **PATCH** /provider/managers | Start/stop provider cluster managers
[**start_stop_provider_worker**](OneproviderClusterApi.md#start_stop_provider_worker) | **PATCH** /provider/workers/{host} | Start/stop provider cluster worker
[**start_stop_provider_workers**](OneproviderClusterApi.md#start_stop_provider_workers) | **PATCH** /provider/workers | Start/stop provider cluster workers

# **add_provider_databases**
> TaskId add_provider_databases(body)

Deploy provider databases

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
api_instance = onepanel_client.OneproviderClusterApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.ServiceDatabases() # ServiceDatabases | The service hosts configuration where databases should be deployed.


try:
    # Deploy provider databases
    api_response = api_instance.add_provider_databases(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OneproviderClusterApi->add_provider_databases: %s\n" % e)
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

# **add_provider_managers**
> TaskId add_provider_managers(body)

Add provider cluster managers

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
api_instance = onepanel_client.OneproviderClusterApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.ManagerHosts() # ManagerHosts | The cluster manager service hosts configuration.

try:
    # Add provider cluster managers
    api_response = api_instance.add_provider_managers(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OneproviderClusterApi->add_provider_managers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ManagerHosts**](ManagerHosts.md)| The cluster manager service hosts configuration. | 

### Return type

[**TaskId**](TaskId.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_provider_workers**
> TaskId add_provider_workers(body)

Add provider cluster workers

Deploys cluster worker services on provided hosts.

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
api_instance = onepanel_client.OneproviderClusterApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.ServiceHosts() # ServiceHosts | The service hosts configuration where workers should be deployed.


try:
    # Add provider cluster workers
    api_response = api_instance.add_provider_workers(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OneproviderClusterApi->add_provider_workers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceHosts**](ServiceHosts.md)| The service hosts configuration where workers should be deployed.
 | 

### Return type

[**TaskId**](TaskId.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configure_provider**
> TaskId configure_provider(body)

Configure provider deployment

Configures and starts provider services, such as database, cluster manager and cluster worker. Depending on the configuration, sets up provider storage and registers in the zone. This request can be executed unauthorized as long as there are no admin users. 

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
api_instance = onepanel_client.OneproviderClusterApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.ProviderConfiguration() # ProviderConfiguration | The provider configuration description.

try:
    # Configure provider deployment
    api_response = api_instance.configure_provider(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OneproviderClusterApi->configure_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProviderConfiguration**](ProviderConfiguration.md)| The provider configuration description. | 

### Return type

[**TaskId**](TaskId.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider_cluster_ips**
> ClusterIps get_provider_cluster_ips()

Get provider cluster nodes IPs

Returns IPs of nodes in provider cluster.

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
api_instance = onepanel_client.OneproviderClusterApi(onepanel_client.ApiClient(configuration))

try:
    # Get provider cluster nodes IPs
    api_response = api_instance.get_provider_cluster_ips()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OneproviderClusterApi->get_provider_cluster_ips: %s\n" % e)
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

# **get_provider_configuration**
> ProviderConfigurationDetails get_provider_configuration()

Get provider cluster configuration

Returns the provider cluster configuration.

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
api_instance = onepanel_client.OneproviderClusterApi(onepanel_client.ApiClient(configuration))

try:
    # Get provider cluster configuration
    api_response = api_instance.get_provider_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OneproviderClusterApi->get_provider_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProviderConfigurationDetails**](ProviderConfigurationDetails.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider_database_status**
> ServiceStatusHost get_provider_database_status(host)

Get provider database status

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
api_instance = onepanel_client.OneproviderClusterApi(onepanel_client.ApiClient(configuration))
host = 'host_example' # str | The name of a host for which database service status should be returned. 

try:
    # Get provider database status
    api_response = api_instance.get_provider_database_status(host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OneproviderClusterApi->get_provider_database_status: %s\n" % e)
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

# **get_provider_databases_status**
> ServiceStatus get_provider_databases_status()

Get provider databases status

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
api_instance = onepanel_client.OneproviderClusterApi(onepanel_client.ApiClient(configuration))

try:
    # Get provider databases status
    api_response = api_instance.get_provider_databases_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OneproviderClusterApi->get_provider_databases_status: %s\n" % e)
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

# **get_provider_manager_status**
> ServiceStatusHost get_provider_manager_status(host)

Get provider cluster manager status

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
api_instance = onepanel_client.OneproviderClusterApi(onepanel_client.ApiClient(configuration))
host = 'host_example' # str | The name of a host for which cluster manager service status should be returned. 

try:
    # Get provider cluster manager status
    api_response = api_instance.get_provider_manager_status(host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OneproviderClusterApi->get_provider_manager_status: %s\n" % e)
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

# **get_provider_managers_status**
> ServiceStatus get_provider_managers_status()

Get provider cluster managers status

Returns status of cluster manager service on each host where it has been deployed. 

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
api_instance = onepanel_client.OneproviderClusterApi(onepanel_client.ApiClient(configuration))

try:
    # Get provider cluster managers status
    api_response = api_instance.get_provider_managers_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OneproviderClusterApi->get_provider_managers_status: %s\n" % e)
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

# **get_provider_nagios_report**
> get_provider_nagios_report()

Get provider nagios report

Returns the provider nagios report.

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
api_instance = onepanel_client.OneproviderClusterApi(onepanel_client.ApiClient(configuration))

try:
    # Get provider nagios report
    api_instance.get_provider_nagios_report()
except ApiException as e:
    print("Exception when calling OneproviderClusterApi->get_provider_nagios_report: %s\n" % e)
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

# **get_provider_worker_status**
> ServiceStatusHost get_provider_worker_status(host)

Get provider cluster worker status

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
api_instance = onepanel_client.OneproviderClusterApi(onepanel_client.ApiClient(configuration))
host = 'host_example' # str | The name of a host for which cluster worker service status should be returned. 

try:
    # Get provider cluster worker status
    api_response = api_instance.get_provider_worker_status(host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OneproviderClusterApi->get_provider_worker_status: %s\n" % e)
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

# **get_provider_workers_status**
> ServiceStatus get_provider_workers_status()

Get provider cluster workers status

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
api_instance = onepanel_client.OneproviderClusterApi(onepanel_client.ApiClient(configuration))

try:
    # Get provider cluster workers status
    api_response = api_instance.get_provider_workers_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OneproviderClusterApi->get_provider_workers_status: %s\n" % e)
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

# **modify_provider_cluster_ips**
> modify_provider_cluster_ips(body)

Set external IPs of nodes in application config

Informs cluster nodes about external IPs which can be used to access them by other providers. 

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
api_instance = onepanel_client.OneproviderClusterApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.ModifyClusterIps() # ModifyClusterIps | The provider configuration description.

try:
    # Set external IPs of nodes in application config
    api_instance.modify_provider_cluster_ips(body)
except ApiException as e:
    print("Exception when calling OneproviderClusterApi->modify_provider_cluster_ips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModifyClusterIps**](ModifyClusterIps.md)| The provider configuration description. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_stop_provider_database**
> start_stop_provider_database(host, started=started)

Start/stop provider database

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
api_instance = onepanel_client.OneproviderClusterApi(onepanel_client.ApiClient(configuration))
host = 'host_example' # str | The name of a host for which database service status should be changed. 
started = true # bool | Defines the intended state of the database service. The service will be started or stopped in order to match the requested state.  (optional) (default to true)

try:
    # Start/stop provider database
    api_instance.start_stop_provider_database(host, started=started)
except ApiException as e:
    print("Exception when calling OneproviderClusterApi->start_stop_provider_database: %s\n" % e)
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

# **start_stop_provider_databases**
> start_stop_provider_databases(started=started)

Start/stop provider databases

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
api_instance = onepanel_client.OneproviderClusterApi(onepanel_client.ApiClient(configuration))
started = true # bool | Defines the intended state of the database service. The service will be started or stopped in order to match the requested state.  (optional) (default to true)

try:
    # Start/stop provider databases
    api_instance.start_stop_provider_databases(started=started)
except ApiException as e:
    print("Exception when calling OneproviderClusterApi->start_stop_provider_databases: %s\n" % e)
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

# **start_stop_provider_manager**
> start_stop_provider_manager(host, started=started)

Start/stop provider cluster manager

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
api_instance = onepanel_client.OneproviderClusterApi(onepanel_client.ApiClient(configuration))
host = 'host_example' # str | The name of a host for which cluster manager service status should be changed. 
started = true # bool | Defines the intended state of the cluster manager service. The service will be started or stopped in order to match the requested state.  (optional) (default to true)

try:
    # Start/stop provider cluster manager
    api_instance.start_stop_provider_manager(host, started=started)
except ApiException as e:
    print("Exception when calling OneproviderClusterApi->start_stop_provider_manager: %s\n" % e)
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

# **start_stop_provider_managers**
> start_stop_provider_managers(started=started)

Start/stop provider cluster managers

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
api_instance = onepanel_client.OneproviderClusterApi(onepanel_client.ApiClient(configuration))
started = true # bool | Defines the intended state of the cluster manager service. The service will be started or stopped in order to match the requested state.  (optional) (default to true)

try:
    # Start/stop provider cluster managers
    api_instance.start_stop_provider_managers(started=started)
except ApiException as e:
    print("Exception when calling OneproviderClusterApi->start_stop_provider_managers: %s\n" % e)
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

# **start_stop_provider_worker**
> start_stop_provider_worker(host, started=started)

Start/stop provider cluster worker

Starts or stops cluster worker service on the selected host in the local deployment. 

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
api_instance = onepanel_client.OneproviderClusterApi(onepanel_client.ApiClient(configuration))
host = 'host_example' # str | The name of a host for which cluster worker service status should be changed. 
started = true # bool | Defines the intended state of the cluster worker service. The service will be started or stopped in order to match the requested state.  (optional) (default to true)

try:
    # Start/stop provider cluster worker
    api_instance.start_stop_provider_worker(host, started=started)
except ApiException as e:
    print("Exception when calling OneproviderClusterApi->start_stop_provider_worker: %s\n" % e)
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

# **start_stop_provider_workers**
> start_stop_provider_workers(started=started)

Start/stop provider cluster workers

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
api_instance = onepanel_client.OneproviderClusterApi(onepanel_client.ApiClient(configuration))
started = true # bool | Defines the intended state of the cluster worker service. The service will be started or stopped in order to match the requested state.  (optional) (default to true)

try:
    # Start/stop provider cluster workers
    api_instance.start_stop_provider_workers(started=started)
except ApiException as e:
    print("Exception when calling OneproviderClusterApi->start_stop_provider_workers: %s\n" % e)
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

