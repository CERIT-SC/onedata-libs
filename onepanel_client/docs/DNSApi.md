# onepanel_client.DNSApi

All URIs are relative to */api/v3/onepanel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_dns**](DNSApi.md#check_dns) | **GET** /dns_check | Check correctness of DNS entries for the cluster&#x27;s domain
[**get_dns_check_configuration**](DNSApi.md#get_dns_check_configuration) | **GET** /dns_check/configuration | Return settings used when performing the DNS check
[**modify_dns_check_configuration**](DNSApi.md#modify_dns_check_configuration) | **PATCH** /dns_check/configuration | Configure dns check

# **check_dns**
> DnsCheck check_dns(force_check=force_check)

Check correctness of DNS entries for the cluster's domain

Returns results of the last DNS check, verifying the validity of DNS configuration for cluster's domain. Unless 'forceCheck' flag is set, the results may be cached. If the cluster is configured with an IP instead of a domain no results are returned. Settings used for the check, ie. DNS servers used can be modified using the dns_check/configuration endpoint. 

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
api_instance = onepanel_client.DNSApi(onepanel_client.ApiClient(configuration))
force_check = false # bool | If true the DNS check cache is overridden and check is performed during handling of the request. (optional) (default to false)

try:
    # Check correctness of DNS entries for the cluster's domain
    api_response = api_instance.check_dns(force_check=force_check)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DNSApi->check_dns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **force_check** | **bool**| If true the DNS check cache is overridden and check is performed during handling of the request. | [optional] [default to false]

### Return type

[**DnsCheck**](DnsCheck.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dns_check_configuration**
> DnsCheckConfiguration get_dns_check_configuration()

Return settings used when performing the DNS check

Returns servers queried to check DNS configuration correctness. 

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
api_instance = onepanel_client.DNSApi(onepanel_client.ApiClient(configuration))

try:
    # Return settings used when performing the DNS check
    api_response = api_instance.get_dns_check_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DNSApi->get_dns_check_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DnsCheckConfiguration**](DnsCheckConfiguration.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_dns_check_configuration**
> modify_dns_check_configuration(body)

Configure dns check

Informs what DNS servers to use for checking external DNS records validity. 

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
api_instance = onepanel_client.DNSApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.DnsCheckConfiguration() # DnsCheckConfiguration | The configuration changes.

try:
    # Configure dns check
    api_instance.modify_dns_check_configuration(body)
except ApiException as e:
    print("Exception when calling DNSApi->modify_dns_check_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DnsCheckConfiguration**](DnsCheckConfiguration.md)| The configuration changes. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

