# oneprovider_client.QoSApi

All URIs are relative to */api/v3/oneprovider*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_qos_requirement**](QoSApi.md#add_qos_requirement) | **POST** /qos_requirements | Add QoS requirement
[**evaluate_qos_expression**](QoSApi.md#evaluate_qos_expression) | **POST** /spaces/{sid}/evaluate_qos_expression | Evaluate QoS expression
[**get_file_qos_summary**](QoSApi.md#get_file_qos_summary) | **GET** /data/{id}/qos/summary | Get QoS summary for file or directory
[**get_qos_requirement**](QoSApi.md#get_qos_requirement) | **GET** /qos_requirements/{qid} | Get QoS requirement
[**get_qos_requirement_audit_log**](QoSApi.md#get_qos_requirement_audit_log) | **GET** /qos_requirements/{qid}/audit_log | Get QoS audit log
[**remove_qos_requirement**](QoSApi.md#remove_qos_requirement) | **DELETE** /qos_requirements/{qid} | Remove QoS requirement

# **add_qos_requirement**
> InlineResponse2014 add_qos_requirement(body)

Add QoS requirement

Adds new QoS requirement for given file or directory. This triggers data replication (if needed) based on requirements defined in new QoS requirement.  For more information about QoS, please see [here](https://onedata.org/#/home/documentation/doc/using_onedata/qos.html).  ***Example cURL requests***  **Add QoS requirement for file** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/qos_requirements\" \\ -H \"Content-Type: application/json\" -d '{     \"expression\": \"country=FR\",     \"replicasNum\": 2,     \"fileId\": \"'$FILE_ID'\" }' ``` 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.QoSApi(oneprovider_client.ApiClient(configuration))
body = oneprovider_client.QosCreateRequest() # QosCreateRequest | QoS requirement properties

try:
    # Add QoS requirement
    api_response = api_instance.add_qos_requirement(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QoSApi->add_qos_requirement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QosCreateRequest**](QosCreateRequest.md)| QoS requirement properties | 

### Return type

[**InlineResponse2014**](InlineResponse2014.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluate_qos_expression**
> InlineResponse2003 evaluate_qos_expression(body, sid)

Evaluate QoS expression

Parses given QoS expression and evaluates it against the parameters of storages supporting the space. Returns the list of storages that match the expression. In case of invalid expression, returns an error with the parser report.  This operation requires `space_manage_qos` privilege.  ***Example cURL requests***  **Evaluate QoS expression** ```bash curl -X POST -H \"X-Auth-Token: $TOKEN\" \\ -H \"Content-type: application/json\" \\ -d \"{\"expression\": \"key = value\"}\" \\ \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/evaluate_qos_expression\"  {   \"matchingStorages\": {     [{       \"id\": \"$STORAGE_ID\",       \"name\": \"storage_name\",       \"providerId\": \"$PROVIDER_ID\"     }] } ``` 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.QoSApi(oneprovider_client.ApiClient(configuration))
body = 'body_example' # str | QoS expression to be evaluated.
sid = 'sid_example' # str | Space Id in which to evaluate QoS expression. 

try:
    # Evaluate QoS expression
    api_response = api_instance.evaluate_qos_expression(body, sid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QoSApi->evaluate_qos_expression: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| QoS expression to be evaluated. | 
 **sid** | **str**| Space Id in which to evaluate QoS expression.  | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_qos_summary**
> QosSummary get_file_qos_summary(id)

Get QoS summary for file or directory

Returns QoS summary for a file specified by [$FILE_ID](#operation/lookup_file_id). QoS summary contains information about effective QoS, which is calculated by merging QoS requirements defined directly for file or directory with QoS requirements defined for all its ancestors.    ***Example cURL requests***  **Get file QoS summary** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/qos/summary\"  {     \"requirements\": [{\"$QOS_REQ_ID\": \"pending\"}],     \"status\": \"pending\" }  ``` 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.QoSApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | Id of the file or directory.

try:
    # Get QoS summary for file or directory
    api_response = api_instance.get_file_qos_summary(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QoSApi->get_file_qos_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the file or directory. | 

### Return type

[**QosSummary**](QosSummary.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_qos_requirement**
> QosRequirement get_qos_requirement(qid)

Get QoS requirement

Returns detailed information about particular QoS requirement.  ***Example cURL requests***  **Get detailed information about QoS requirement** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/qos_requirements/$QOS_REQ_ID\"  {     \"qosRequirementId\": \"c84f669f9522c46976fee490d80651f0\",     \"fileId\": \"$FILE_ID\",     \"qosExpression\": \"country=FR\",     \"replicasNum\": 2,     \"status\": \"fulfilled\" }  ``` 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.QoSApi(oneprovider_client.ApiClient(configuration))
qid = 'qid_example' # str | QoS requirement Id

try:
    # Get QoS requirement
    api_response = api_instance.get_qos_requirement(qid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QoSApi->get_qos_requirement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qid** | **str**| QoS requirement Id | 

### Return type

[**QosRequirement**](QosRequirement.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_qos_requirement_audit_log**
> QosRequirementAuditLog get_qos_requirement_audit_log(qid, timestamp=timestamp, offset=offset, limit=limit)

Get QoS audit log

Returns audit log of performed locally (on selected Oneprovider) files operations that were result of given QoS requirement. The audit log stores logs concerning all  files affected by a specific QoS requirement.  ***Example cURL requests***  **Get QoS audit log** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \\  \"https://$PROVIDER_HOST/api/v3/oneprovider/qos_requirements/$QOS_REQ_ID/audit_log?timestamp=1626334701662&offset=1\"  {     \"isLast\": false,     \"logEntries\": [{         \"index\": 0,         \"timestamp\": 1626334701662,         \"content\": {             \"fileId\": $FILE_ID,             \"severity\": \"info\"             \"status\": \"completed\",             \"description\": \"Local replica reconciled.\"         }     }] }  ``` 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.QoSApi(oneprovider_client.ApiClient(configuration))
qid = 'qid_example' # str | QoS requirement Id
timestamp = 56 # int | Starting timestamp for listing - the listing will start with an entry that has an equal or greater timestamp.  (optional)
offset = 0 # int | Offset from the beginning of the collection specifying starting point for listing relative to timestamp.  (optional) (default to 0)
limit = 1000 # int | Maximum number of entries that should be returned. If there are more entries, they can be retrieved using `offset` or `timestamp` query parameters.  (optional) (default to 1000)

try:
    # Get QoS audit log
    api_response = api_instance.get_qos_requirement_audit_log(qid, timestamp=timestamp, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QoSApi->get_qos_requirement_audit_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qid** | **str**| QoS requirement Id | 
 **timestamp** | **int**| Starting timestamp for listing - the listing will start with an entry that has an equal or greater timestamp.  | [optional] 
 **offset** | **int**| Offset from the beginning of the collection specifying starting point for listing relative to timestamp.  | [optional] [default to 0]
 **limit** | **int**| Maximum number of entries that should be returned. If there are more entries, they can be retrieved using &#x60;offset&#x60; or &#x60;timestamp&#x60; query parameters.  | [optional] [default to 1000]

### Return type

[**QosRequirementAuditLog**](QosRequirementAuditLog.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_qos_requirement**
> remove_qos_requirement(qid)

Remove QoS requirement

Removes QoS requirement.  ***Example cURL requests***  **Remove QoS requirement.** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/qos_requirements/$QOS_REQ_ID\" ``` 

### Example
```python
from __future__ import print_function
import time
import oneprovider_client
from oneprovider_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = oneprovider_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = oneprovider_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = oneprovider_client.QoSApi(oneprovider_client.ApiClient(configuration))
qid = 'qid_example' # str | QoS requirement Id

try:
    # Remove QoS requirement
    api_instance.remove_qos_requirement(qid)
except ApiException as e:
    print("Exception when calling QoSApi->remove_qos_requirement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qid** | **str**| QoS requirement Id | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

