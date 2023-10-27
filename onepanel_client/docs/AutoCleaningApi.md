# onepanel_client.AutoCleaningApi

All URIs are relative to */api/v3/onepanel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_auto_cleaning**](AutoCleaningApi.md#cancel_auto_cleaning) | **POST** /provider/spaces/{id}/auto-cleaning/cancel | Cancel space auto-cleaning
[**configure_space_auto_cleaning**](AutoCleaningApi.md#configure_space_auto_cleaning) | **PATCH** /provider/spaces/{id}/auto-cleaning/configuration | Configure space auto-cleaning mechanism
[**get_provider_space_auto_cleaning_report**](AutoCleaningApi.md#get_provider_space_auto_cleaning_report) | **GET** /provider/spaces/{id}/auto-cleaning/reports/{report_id} | Get the report from a space auto-cleaning run
[**get_provider_space_auto_cleaning_reports**](AutoCleaningApi.md#get_provider_space_auto_cleaning_reports) | **GET** /provider/spaces/{id}/auto-cleaning/reports | Get Ids of of the space auto-cleaning reports
[**get_provider_space_auto_cleaning_status**](AutoCleaningApi.md#get_provider_space_auto_cleaning_status) | **GET** /provider/spaces/{id}/auto-cleaning/status | Get status of space auto-cleaning mechanism
[**get_space_auto_cleaning_configuration**](AutoCleaningApi.md#get_space_auto_cleaning_configuration) | **GET** /provider/spaces/{id}/auto-cleaning/configuration | Get space auto-cleaning configuration
[**trigger_auto_cleaning**](AutoCleaningApi.md#trigger_auto_cleaning) | **POST** /provider/spaces/{id}/auto-cleaning/start | Trigger space auto-cleaning

# **cancel_auto_cleaning**
> cancel_auto_cleaning(id)

Cancel space auto-cleaning

Cancel current run of auto-cleaning mechanism for given space.

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
api_instance = onepanel_client.AutoCleaningApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a space.

try:
    # Cancel space auto-cleaning
    api_instance.cancel_auto_cleaning(id)
except ApiException as e:
    print("Exception when calling AutoCleaningApi->cancel_auto_cleaning: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a space. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configure_space_auto_cleaning**
> configure_space_auto_cleaning(body, id)

Configure space auto-cleaning mechanism

Configures space auto-cleaning mechanism in the space. 

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
api_instance = onepanel_client.AutoCleaningApi(onepanel_client.ApiClient(configuration))
body = onepanel_client.SpaceAutoCleaningConfiguration() # SpaceAutoCleaningConfiguration | New configuration of space auto-cleaning mechanism.

id = 'id_example' # str | The Id of a space.

try:
    # Configure space auto-cleaning mechanism
    api_instance.configure_space_auto_cleaning(body, id)
except ApiException as e:
    print("Exception when calling AutoCleaningApi->configure_space_auto_cleaning: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpaceAutoCleaningConfiguration**](SpaceAutoCleaningConfiguration.md)| New configuration of space auto-cleaning mechanism.
 | 
 **id** | **str**| The Id of a space. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider_space_auto_cleaning_report**
> SpaceAutoCleaningReport get_provider_space_auto_cleaning_report(id, report_id)

Get the report from a space auto-cleaning run

Returns the details of a specific auto-cleaning run. 

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
api_instance = onepanel_client.AutoCleaningApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a space.
report_id = 'report_id_example' # str | The Id of an auto-cleaning report.

try:
    # Get the report from a space auto-cleaning run
    api_response = api_instance.get_provider_space_auto_cleaning_report(id, report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoCleaningApi->get_provider_space_auto_cleaning_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a space. | 
 **report_id** | **str**| The Id of an auto-cleaning report. | 

### Return type

[**SpaceAutoCleaningReport**](SpaceAutoCleaningReport.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider_space_auto_cleaning_reports**
> SpaceAutoCleaningReports get_provider_space_auto_cleaning_reports(id, offset=offset, limit=limit, index=index)

Get Ids of of the space auto-cleaning reports

Returns the list of Ids of space auto-cleaning reports. The list is sorted descending by start time of an auto-cleaning run (the newest report is first). 

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
api_instance = onepanel_client.AutoCleaningApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a space.
offset = 0 # int | Allows to skip N first report Ids. (optional) (default to 0)
limit = 56 # int | Allows to limit the number of returned report Ids up to N last reports. By default, all report Ids will be returned.  (optional)
index = 'index_example' # str | Allows to list the report Ids starting from the specific report.  (optional)

try:
    # Get Ids of of the space auto-cleaning reports
    api_response = api_instance.get_provider_space_auto_cleaning_reports(id, offset=offset, limit=limit, index=index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoCleaningApi->get_provider_space_auto_cleaning_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a space. | 
 **offset** | **int**| Allows to skip N first report Ids. | [optional] [default to 0]
 **limit** | **int**| Allows to limit the number of returned report Ids up to N last reports. By default, all report Ids will be returned.  | [optional] 
 **index** | **str**| Allows to list the report Ids starting from the specific report.  | [optional] 

### Return type

[**SpaceAutoCleaningReports**](SpaceAutoCleaningReports.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider_space_auto_cleaning_status**
> SpaceAutoCleaningStatus get_provider_space_auto_cleaning_status(id)

Get status of space auto-cleaning mechanism

Returns status of current process of auto-cleaning for the space. 

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
api_instance = onepanel_client.AutoCleaningApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a space.

try:
    # Get status of space auto-cleaning mechanism
    api_response = api_instance.get_provider_space_auto_cleaning_status(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoCleaningApi->get_provider_space_auto_cleaning_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a space. | 

### Return type

[**SpaceAutoCleaningStatus**](SpaceAutoCleaningStatus.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space_auto_cleaning_configuration**
> SpaceAutoCleaningConfiguration get_space_auto_cleaning_configuration(id)

Get space auto-cleaning configuration

Returns configuration of auto-cleaning mechanism in the space specified by space Id in the path. 

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
api_instance = onepanel_client.AutoCleaningApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a space of which auto-cleaning configuration should be returned.

try:
    # Get space auto-cleaning configuration
    api_response = api_instance.get_space_auto_cleaning_configuration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoCleaningApi->get_space_auto_cleaning_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a space of which auto-cleaning configuration should be returned. | 

### Return type

[**SpaceAutoCleaningConfiguration**](SpaceAutoCleaningConfiguration.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_auto_cleaning**
> InlineResponse202 trigger_auto_cleaning(id)

Trigger space auto-cleaning

Trigger one run of auto-cleaning mechanism for given space.

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
api_instance = onepanel_client.AutoCleaningApi(onepanel_client.ApiClient(configuration))
id = 'id_example' # str | The Id of a space.

try:
    # Trigger space auto-cleaning
    api_response = api_instance.trigger_auto_cleaning(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoCleaningApi->trigger_auto_cleaning: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of a space. | 

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

