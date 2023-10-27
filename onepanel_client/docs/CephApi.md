# onepanel_client.CephApi

All URIs are relative to */api/v3/onepanel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ceph_managers**](CephApi.md#add_ceph_managers) | **POST** /provider/ceph/managers | Add managers to ceph cluster
[**add_ceph_monitors**](CephApi.md#add_ceph_monitors) | **POST** /provider/ceph/monitors | Add monitors to Ceph cluster
[**add_ceph_osds**](CephApi.md#add_ceph_osds) | **POST** /provider/ceph/osds | Add OSDs to Ceph cluster
[**configure_ceph**](CephApi.md#configure_ceph) | **POST** /provider/ceph | Configure Ceph cluster
[**get_block_devices**](CephApi.md#get_block_devices) | **GET** /provider/ceph/preflight/block_devices | Get block devices for Ceph OSD
[**get_ceph_manager**](CephApi.md#get_ceph_manager) | **GET** /provider/ceph/managers/{id} | Get Ceph manager
[**get_ceph_managers**](CephApi.md#get_ceph_managers) | **GET** /provider/ceph/managers | List Ceph managers
[**get_ceph_monitor**](CephApi.md#get_ceph_monitor) | **GET** /provider/ceph/monitors/{id} | Get Ceph monitor
[**get_ceph_monitors**](CephApi.md#get_ceph_monitors) | **GET** /provider/ceph/monitors | List Ceph monitors
[**get_ceph_osd**](CephApi.md#get_ceph_osd) | **GET** /provider/ceph/osds/{id} | Get Ceph OSD
[**get_ceph_osd_usage**](CephApi.md#get_ceph_osd_usage) | **GET** /provider/ceph/osds/{id}/usage | Get storage space usage details for specific OSD
[**get_ceph_osds**](CephApi.md#get_ceph_osds) | **GET** /provider/ceph/osds | Get Ceph OSDs list
[**get_ceph_params**](CephApi.md#get_ceph_params) | **GET** /provider/ceph | Get global Ceph params
[**get_ceph_pool**](CephApi.md#get_ceph_pool) | **GET** /provider/ceph/pools/{name} | Get details of a Ceph pool
[**get_ceph_pool_usage**](CephApi.md#get_ceph_pool_usage) | **GET** /provider/ceph/pools/{name}/usage | Get storage space usage details for specific pool
[**get_ceph_pools**](CephApi.md#get_ceph_pools) | **GET** /provider/ceph/pools | List Ceph pools
[**get_ceph_status**](CephApi.md#get_ceph_status) | **GET** /provider/ceph/status | Get Ceph cluster health
[**get_ceph_usage**](CephApi.md#get_ceph_usage) | **GET** /provider/ceph/usage | Get Ceph storage space usage.
[**modify_ceph_pool**](CephApi.md#modify_ceph_pool) | **PATCH** /provider/ceph/pools/{name} | Modify pool params

# **add_ceph_managers**
> TaskId add_ceph_managers(body)

Add managers to ceph cluster

Deploys Ceph manager services on given hosts.

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
api_instance = onepanel_client.CephApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.CephManagers() # CephManagers | Object with a list of Ceph manager configurations.

try:
    # Add managers to ceph cluster
    api_response = api_instance.add_ceph_managers(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CephApi->add_ceph_managers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CephManagers**](CephManagers.md)| Object with a list of Ceph manager configurations. | 

### Return type

[**TaskId**](TaskId.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_ceph_monitors**
> TaskId add_ceph_monitors(body)

Add monitors to Ceph cluster

Deploys Ceph monitor services on given hosts.

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
api_instance = onepanel_client.CephApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.CephMonitors() # CephMonitors | List of Ceph monitor specifications.

try:
    # Add monitors to Ceph cluster
    api_response = api_instance.add_ceph_monitors(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CephApi->add_ceph_monitors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CephMonitors**](CephMonitors.md)| List of Ceph monitor specifications. | 

### Return type

[**TaskId**](TaskId.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_ceph_osds**
> TaskId add_ceph_osds(body)

Add OSDs to Ceph cluster

Deploys Ceph OSD services in the cluster.

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
api_instance = onepanel_client.CephApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.CephOsds() # CephOsds | List of OSD specifications.

try:
    # Add OSDs to Ceph cluster
    api_response = api_instance.add_ceph_osds(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CephApi->add_ceph_osds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CephOsds**](CephOsds.md)| List of OSD specifications. | 

### Return type

[**TaskId**](TaskId.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configure_ceph**
> TaskId configure_ceph(body)

Configure Ceph cluster

Configures Ceph services. Any services and pools specified in the request are deployed. This request IS NOT idempotent.

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
api_instance = onepanel_client.CephApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.CephCluster() # CephCluster | The Ceph cluster specification.

try:
    # Configure Ceph cluster
    api_response = api_instance.configure_ceph(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CephApi->configure_ceph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CephCluster**](CephCluster.md)| The Ceph cluster specification. | 

### Return type

[**TaskId**](TaskId.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_devices**
> BlockDevices get_block_devices(host)

Get block devices for Ceph OSD

Lists block devices available at given host. This list can be used to choose device to be formatted for use by Ceph Blockdevice OSD.

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
api_instance = onepanel_client.CephApi(onepanel_client.ApiClient(configuration))
host = 'host_example' # str | Host for which block devices should be returned.

try:
    # Get block devices for Ceph OSD
    api_response = api_instance.get_block_devices(host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CephApi->get_block_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| Host for which block devices should be returned. | 

### Return type

[**BlockDevices**](BlockDevices.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ceph_manager**
> CephManager get_ceph_manager(id)

Get Ceph manager

Returns Ceph manager configuration.

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
api_instance = onepanel_client.CephApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | Id of the Ceph manager to be described.

try:
    # Get Ceph manager
    api_response = api_instance.get_ceph_manager(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CephApi->get_ceph_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Ceph manager to be described. | 

### Return type

[**CephManager**](CephManager.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ceph_managers**
> CephManagers get_ceph_managers()

List Ceph managers

Returns object with a list of Ceph manager instances.

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
api_instance = onepanel_client.CephApi(onepanel_client.ApiClient(configuration))

try:
    # List Ceph managers
    api_response = api_instance.get_ceph_managers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CephApi->get_ceph_managers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CephManagers**](CephManagers.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ceph_monitor**
> CephMonitor get_ceph_monitor(id)

Get Ceph monitor

Returns details of a Ceph monitor instance.

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
api_instance = onepanel_client.CephApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | Id of the Ceph monitor to describe.

try:
    # Get Ceph monitor
    api_response = api_instance.get_ceph_monitor(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CephApi->get_ceph_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Ceph monitor to describe. | 

### Return type

[**CephMonitor**](CephMonitor.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ceph_monitors**
> CephMonitors get_ceph_monitors()

List Ceph monitors

Returns object with a list of Ceph monitor instances.

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
api_instance = onepanel_client.CephApi(onepanel_client.ApiClient(configuration))

try:
    # List Ceph monitors
    api_response = api_instance.get_ceph_monitors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CephApi->get_ceph_monitors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CephMonitors**](CephMonitors.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ceph_osd**
> CephOsd get_ceph_osd(id)

Get Ceph OSD

Returns details of a Ceph OSD instance.

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
api_instance = onepanel_client.CephApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | Id of the Ceph OSD to describe.

try:
    # Get Ceph OSD
    api_response = api_instance.get_ceph_osd(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CephApi->get_ceph_osd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Ceph OSD to describe. | 

### Return type

[**CephOsd**](CephOsd.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ceph_osd_usage**
> DataUsage get_ceph_osd_usage(id)

Get storage space usage details for specific OSD

Returns storage space usage statistics of given Ceph OSD.

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
api_instance = onepanel_client.CephApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The id of the OSD for usage check.

try:
    # Get storage space usage details for specific OSD
    api_response = api_instance.get_ceph_osd_usage(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CephApi->get_ceph_osd_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the OSD for usage check. | 

### Return type

[**DataUsage**](DataUsage.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ceph_osds**
> CephOsds get_ceph_osds()

Get Ceph OSDs list

Return list of Ceph OSD configurations. 

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
api_instance = onepanel_client.CephApi(onepanel_client.ApiClient(configuration))

try:
    # Get Ceph OSDs list
    api_response = api_instance.get_ceph_osds()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CephApi->get_ceph_osds: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CephOsds**](CephOsds.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ceph_params**
> CephGlobalParams get_ceph_params()

Get global Ceph params

Returns settings global for the Ceph cluster.

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
api_instance = onepanel_client.CephApi(onepanel_client.ApiClient(configuration))

try:
    # Get global Ceph params
    api_response = api_instance.get_ceph_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CephApi->get_ceph_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CephGlobalParams**](CephGlobalParams.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ceph_pool**
> CephPool get_ceph_pool(name)

Get details of a Ceph pool

Returns object describng single Ceph pool specified by name.

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
api_instance = onepanel_client.CephApi(onepanel_client.ApiClient(configuration))
name = 'name_example' # str | The name of the pool to describe.

try:
    # Get details of a Ceph pool
    api_response = api_instance.get_ceph_pool(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CephApi->get_ceph_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the pool to describe. | 

### Return type

[**CephPool**](CephPool.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ceph_pool_usage**
> CephPoolUsage get_ceph_pool_usage(name)

Get storage space usage details for specific pool

Returns storage space usage statistics of given Ceph pool.

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
api_instance = onepanel_client.CephApi(onepanel_client.ApiClient(configuration))
name = 'name_example' # str | The name of the pool for usage check.

try:
    # Get storage space usage details for specific pool
    api_response = api_instance.get_ceph_pool_usage(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CephApi->get_ceph_pool_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the pool for usage check. | 

### Return type

[**CephPoolUsage**](CephPoolUsage.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ceph_pools**
> CephPools get_ceph_pools()

List Ceph pools

Returns object containing list of Ceph pool details.

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
api_instance = onepanel_client.CephApi(onepanel_client.ApiClient(configuration))

try:
    # List Ceph pools
    api_response = api_instance.get_ceph_pools()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CephApi->get_ceph_pools: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CephPools**](CephPools.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ceph_status**
> CephStatus get_ceph_status()

Get Ceph cluster health

Returns Ceph cluster health.

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
api_instance = onepanel_client.CephApi(onepanel_client.ApiClient(configuration))

try:
    # Get Ceph cluster health
    api_response = api_instance.get_ceph_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CephApi->get_ceph_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CephStatus**](CephStatus.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ceph_usage**
> CephUsage get_ceph_usage()

Get Ceph storage space usage.

Returns summary of storage space usage in the Ceph cluster.

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
api_instance = onepanel_client.CephApi(onepanel_client.ApiClient(configuration))

try:
    # Get Ceph storage space usage.
    api_response = api_instance.get_ceph_usage()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CephApi->get_ceph_usage: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CephUsage**](CephUsage.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_ceph_pool**
> modify_ceph_pool(body, name)

Modify pool params

Modifies the pool redundancy settings.

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
api_instance = onepanel_client.CephApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.CephPool() # CephPool | 
name = 'name_example' # str | The name of the pool to describe.

try:
    # Modify pool params
    api_instance.modify_ceph_pool(body, name)
except ApiException as e:
    print("Exception when calling CephApi->modify_ceph_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CephPool**](CephPool.md)|  | 
 **name** | **str**| The name of the pool to describe. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

