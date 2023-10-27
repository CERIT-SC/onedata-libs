# oneprovider_client.WorkflowExecutionApi

All URIs are relative to */api/v3/oneprovider*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_workflow_execution**](WorkflowExecutionApi.md#cancel_workflow_execution) | **POST** /automation/execution/workflows/{wid}/cancel | Cancel workflow execution
[**delete_workflow_execution**](WorkflowExecutionApi.md#delete_workflow_execution) | **DELETE** /automation/execution/workflows/{wid} | Delete workflow execution
[**force_continue_workflow_execution**](WorkflowExecutionApi.md#force_continue_workflow_execution) | **POST** /automation/execution/workflows/{wid}/force_continue | Force continue workflow execution
[**get_workflow_execution_details**](WorkflowExecutionApi.md#get_workflow_execution_details) | **GET** /automation/execution/workflows/{wid} | Get workflow execution details
[**list_workflow_executions**](WorkflowExecutionApi.md#list_workflow_executions) | **GET** /spaces/{sid}/automation/execution/workflows | List workflow executions
[**pause_workflow_execution**](WorkflowExecutionApi.md#pause_workflow_execution) | **POST** /automation/execution/workflows/{wid}/pause | Pause workflow execution
[**rerun_workflow_execution**](WorkflowExecutionApi.md#rerun_workflow_execution) | **POST** /automation/execution/workflows/{wid}/rerun | Rerun workflow execution
[**resume_workflow_execution**](WorkflowExecutionApi.md#resume_workflow_execution) | **POST** /automation/execution/workflows/{wid}/resume | Resume workflow execution
[**retry_workflow_execution**](WorkflowExecutionApi.md#retry_workflow_execution) | **POST** /automation/execution/workflows/{wid}/retry | Retry workflow execution
[**schedule_workflow_execution**](WorkflowExecutionApi.md#schedule_workflow_execution) | **POST** /automation/execution/workflows | Schedule workflow execution

# **cancel_workflow_execution**
> cancel_workflow_execution(wid)

Cancel workflow execution

Cancels scheduled, ongoing or suspended workflow execution.  This operation requires `space_schedule_atm_workflow_executions` when invoked by scheduling user, or `space_manage_atm_workflow_executions`  otherwise.  ***Example cURL requests***  **Cancel workflow execution** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID/cancel\" ``` 

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
api_instance = oneprovider_client.WorkflowExecutionApi(oneprovider_client.ApiClient(configuration))
wid = 'wid_example' # str | Workflow execution Id.

try:
    # Cancel workflow execution
    api_instance.cancel_workflow_execution(wid)
except ApiException as e:
    print("Exception when calling WorkflowExecutionApi->cancel_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wid** | **str**| Workflow execution Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workflow_execution**
> delete_workflow_execution(wid)

Delete workflow execution

Deletes stopped workflow execution.  This operation requires `space_schedule_atm_workflow_executions` when invoked by scheduling user, or `space_manage_atm_workflow_executions`  otherwise.  ***Example cURL requests***  **Delete workflow execution details** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID\" ``` 

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
api_instance = oneprovider_client.WorkflowExecutionApi(oneprovider_client.ApiClient(configuration))
wid = 'wid_example' # str | Workflow execution Id.

try:
    # Delete workflow execution
    api_instance.delete_workflow_execution(wid)
except ApiException as e:
    print("Exception when calling WorkflowExecutionApi->delete_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wid** | **str**| Workflow execution Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **force_continue_workflow_execution**
> force_continue_workflow_execution(wid)

Force continue workflow execution

Forcefully proceeds with a failed execution, commencing from the subsequent  lane to the one that failed.  This operation requires `space_schedule_atm_workflow_executions` when invoked by scheduling user, or `space_manage_atm_workflow_executions`  otherwise.  ***Example cURL requests***  **Force continue workflow execution** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID/force_continue\" ``` 

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
api_instance = oneprovider_client.WorkflowExecutionApi(oneprovider_client.ApiClient(configuration))
wid = 'wid_example' # str | Workflow execution Id.

try:
    # Force continue workflow execution
    api_instance.force_continue_workflow_execution(wid)
except ApiException as e:
    print("Exception when calling WorkflowExecutionApi->force_continue_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wid** | **str**| Workflow execution Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_execution_details**
> AtmWorkflowExecutionDetails get_workflow_execution_details(wid)

Get workflow execution details

Returns the details of a specific workflow execution.  This operation requires `space_view_atm_workflow_executions` privilege and the requesting user must belong to the automation inventory containing the corresponding workflow schema definition.  ***Example cURL requests***  **Get workflow execution details** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID\"  {     \"atmWorkflowExecutionId\": \"11a53ed06d175c89bc3ed5be61f8217cch1890\",     \"atmWorkflowSchemaSnapshotId\": \"821711ad53ed06be61f175c89bc3ed5cch1890\",     \"name\": \"test execution\",     \"atmInventoryId\": \"2d180796daafcf15d586d29dd13dae48chd5fc\",     \"spaceId\": \"c17147cc3188408c26f522881282cb83ch9853\",     \"userId\": \"08c26cc228812c3188417147f582cb83ch9853\",     \"status\": \"enqueued\",     \"scheduleTime\": 1626107063,     \"startTime\": 0,     \"suspendTime\": 0,     \"finishTime\": 0,     \"lambdaSnapshotRegistry\": {         \"e412848d415329d81b7edd15c80b7740chf93f\": \"3946496fb29e3cf3faa96dbbd58d42d9ch9e3c\"     },     \"storeRegistry\": {         \"216a5de15ba9f8f3138168682c3da954212abf\": \"805392e2b84fb7e6ff5b31b4b7e70845ch1995\"     },     \"systemAuditLogStoreId\": \"1439ca4dee1a251483923f4535bca500e72f2a\",     \"lanes\": [         {             \"schemaId\": \"3a1a829f714a41b043c4ce67402d8c136f125f\",             \"runs\": [                 {                     \"runNumber\": 3,                     \"originRunNumber\": 1,                     \"runType\": \"retry\",                     \"status\": \"pending\",                     \"iteratedStoreId\": \"1b502545a3f9faa7f1e339f4aea793117be91d\",                     \"exceptionStoreId\": \"98c669ec69c0394a38391c0ab0117f67ch260d\",                     \"parallelBoxes\": [                         {                             \"taskRegistry\": {                                 \"d92b861a5edfb08b920e0e80f4670a87f48176\": \"1697f7c1f46e0e22bb426bead5a3cb47chda3d\"                             },                             \"schemaId\": \"0068146d662adc878f699bf82af08b9ddbd9ab\"                         }                     ],                     \"isRetriable\": false,                     \"isRerunable\": false                 },                 ...             ]         }     ] } ``` 

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
api_instance = oneprovider_client.WorkflowExecutionApi(oneprovider_client.ApiClient(configuration))
wid = 'wid_example' # str | Workflow execution Id.

try:
    # Get workflow execution details
    api_response = api_instance.get_workflow_execution_details(wid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowExecutionApi->get_workflow_execution_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wid** | **str**| Workflow execution Id. | 

### Return type

[**AtmWorkflowExecutionDetails**](AtmWorkflowExecutionDetails.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflow_executions**
> InlineResponse2004 list_workflow_executions(sid, phase=phase, limit=limit, offset=offset, token=token)

List workflow executions

Returns the list of workflow execution Ids with given phase within a space. The list will include only workflow executions based on schemas from  inventories to which user has access.  This operation requires `space_view_atm_workflow_executions` privilege.  ***Example cURL requests***  **List at most 3 ongoing workflow executions starting from page id 757136151113c2f** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/automation/execution/workflows?phase=ongoing&limit=3&token=757136151113c2f\"  {     \"atmWorkflowExecutions\": [         \"2727a9fe5f5df6b43a8033386d2990e8ch5df6\",         \"4bd9b58f6387622bf07f7388945e4fc4ch8762\",         \"579a785181331e618b26980166b6ba2fch331e\"     ],     \"isLast\": false,     \"nextPageToken\": \"8471726779817b3a\" } ``` 

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
api_instance = oneprovider_client.WorkflowExecutionApi(oneprovider_client.ApiClient(configuration))
sid = 'sid_example' # str | Space Id in which to list workflow executions. 
phase = 'ongoing' # str | Specifies the phase of workflow executions to list. (optional) (default to ongoing)
limit = 1000 # int | Allows specifying maximum number of entries that should be returned.  If there are more workflow executions, they can be retrieved using  `offset` or `token` query parameters.  (optional) (default to 1000)
offset = 0 # int | Offset determining beginning of the list of workflow executions returned  in the response. Expressed in number of entries, further adjusts the  starting point of listing indicated by `token` parameter. The value can be negative, in such case entries preceding the starting  point will be returned.  (optional) (default to 0)
token = 'null' # str | Determines the starting point for listing. The listing will start from  the next page (batch) of entries which follows the page previously  obtained along with the corresponding `nextPageToken`.  (optional) (default to null)

try:
    # List workflow executions
    api_response = api_instance.list_workflow_executions(sid, phase=phase, limit=limit, offset=offset, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowExecutionApi->list_workflow_executions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Space Id in which to list workflow executions.  | 
 **phase** | **str**| Specifies the phase of workflow executions to list. | [optional] [default to ongoing]
 **limit** | **int**| Allows specifying maximum number of entries that should be returned.  If there are more workflow executions, they can be retrieved using  &#x60;offset&#x60; or &#x60;token&#x60; query parameters.  | [optional] [default to 1000]
 **offset** | **int**| Offset determining beginning of the list of workflow executions returned  in the response. Expressed in number of entries, further adjusts the  starting point of listing indicated by &#x60;token&#x60; parameter. The value can be negative, in such case entries preceding the starting  point will be returned.  | [optional] [default to 0]
 **token** | **str**| Determines the starting point for listing. The listing will start from  the next page (batch) of entries which follows the page previously  obtained along with the corresponding &#x60;nextPageToken&#x60;.  | [optional] [default to null]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_workflow_execution**
> pause_workflow_execution(wid)

Pause workflow execution

Pauses scheduled or ongoing workflow execution.  This operation requires `space_schedule_atm_workflow_executions` when invoked by scheduling user, or `space_manage_atm_workflow_executions`  otherwise.  ***Example cURL requests***  **Pause workflow execution** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID/pause\" ``` 

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
api_instance = oneprovider_client.WorkflowExecutionApi(oneprovider_client.ApiClient(configuration))
wid = 'wid_example' # str | Workflow execution Id.

try:
    # Pause workflow execution
    api_instance.pause_workflow_execution(wid)
except ApiException as e:
    print("Exception when calling WorkflowExecutionApi->pause_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wid** | **str**| Workflow execution Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rerun_workflow_execution**
> rerun_workflow_execution(body, wid)

Rerun workflow execution

Reruns stopped workflow execution starting from specified lane run.  This operation requires `space_schedule_atm_workflow_executions` when invoked by scheduling user, or `space_manage_atm_workflow_executions`  otherwise.  ***Example cURL requests***  **Rerun workflow execution** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID/rerun\" -H \"Content-Type: application/json\" -d '{     \"laneIndex\": 2,     \"laneRunNumber\": 3 }' ``` 

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
api_instance = oneprovider_client.WorkflowExecutionApi(oneprovider_client.ApiClient(configuration))
body = oneprovider_client.WidRerunBody() # WidRerunBody | Lane run reference.
wid = 'wid_example' # str | Workflow execution Id.

try:
    # Rerun workflow execution
    api_instance.rerun_workflow_execution(body, wid)
except ApiException as e:
    print("Exception when calling WorkflowExecutionApi->rerun_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WidRerunBody**](WidRerunBody.md)| Lane run reference. | 
 **wid** | **str**| Workflow execution Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_workflow_execution**
> resume_workflow_execution(wid)

Resume workflow execution

Resumes suspended (either paused or interrupted) workflow execution.  This operation requires `space_schedule_atm_workflow_executions` when invoked by scheduling user, or `space_manage_atm_workflow_executions`  otherwise.  ***Example cURL requests***  **Resume workflow execution** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID/resume\" ``` 

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
api_instance = oneprovider_client.WorkflowExecutionApi(oneprovider_client.ApiClient(configuration))
wid = 'wid_example' # str | Workflow execution Id.

try:
    # Resume workflow execution
    api_instance.resume_workflow_execution(wid)
except ApiException as e:
    print("Exception when calling WorkflowExecutionApi->resume_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wid** | **str**| Workflow execution Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_workflow_execution**
> retry_workflow_execution(body, wid)

Retry workflow execution

Retries failed workflow execution starting from specified lane run.  This operation requires `space_schedule_atm_workflow_executions` when invoked by scheduling user, or `space_manage_atm_workflow_executions`  otherwise.  ***Example cURL requests***  **Retry workflow execution** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID/retry\" -H \"Content-Type: application/json\" -d '{     \"laneIndex\": 2,     \"laneRunNumber\": 3 }' ``` 

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
api_instance = oneprovider_client.WorkflowExecutionApi(oneprovider_client.ApiClient(configuration))
body = oneprovider_client.WidRetryBody() # WidRetryBody | Lane run reference.
wid = 'wid_example' # str | Workflow execution Id.

try:
    # Retry workflow execution
    api_instance.retry_workflow_execution(body, wid)
except ApiException as e:
    print("Exception when calling WorkflowExecutionApi->retry_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WidRetryBody**](WidRetryBody.md)| Lane run reference. | 
 **wid** | **str**| Workflow execution Id. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_workflow_execution**
> InlineResponse2018 schedule_workflow_execution(body)

Schedule workflow execution

Schedules a workflow execution based on specified workflow schema revision. The execution is asynchronous.  This operation requires `space_schedule_atm_workflow_executions` privilege and the requesting user must belong to the automation inventory containing the corresponding workflow schema definition.  ***Example cURL requests***  **Create workflow execution** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows\" \\ -H \"Content-Type: application/json\" -d '{     \"spaceId\": \"'$SPACE_ID'\",     \"atmWorkflowSchemaId\": \"'$ATM_WORKFLOW_SCHEMA_ID'\",     \"atmWorkflowSchemaRevisionNumber\": 3,     \"storeInitialContentOverlay\": {         \"de6d2e524459dd235f80aa8652a68879b5dbe9\": [             {                 \"file_id\": \"0000000000523261677569642330376134636136616638613431366334386338343366356338643562323662\"             }         ],         \"83cf895501eb11f9bc71e4b2b41a252e8561b5\": {             \"file_id\": \"000000000052A6E0677569642334653938663463616538386232366437366539636462393634633031653733\"         }     },     \"logLevel\": \"debug\",     \"callback\": \"https://my-server.example.com/execution-callback\" }'  {\"atmWorkflowExecutionId\": \"11a53ed06d175c89bc3ed5be61f8217cch1890\"} ``` 

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
api_instance = oneprovider_client.WorkflowExecutionApi(oneprovider_client.ApiClient(configuration))
body = oneprovider_client.AtmWorkflowExecutionScheduleRequest() # AtmWorkflowExecutionScheduleRequest | Workflow execution properties.

try:
    # Schedule workflow execution
    api_response = api_instance.schedule_workflow_execution(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowExecutionApi->schedule_workflow_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AtmWorkflowExecutionScheduleRequest**](AtmWorkflowExecutionScheduleRequest.md)| Workflow execution properties. | 

### Return type

[**InlineResponse2018**](InlineResponse2018.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

