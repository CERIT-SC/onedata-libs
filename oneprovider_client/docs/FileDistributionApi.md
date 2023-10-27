# oneprovider_client.FileDistributionApi

All URIs are relative to */api/v3/oneprovider*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_file_distribution**](FileDistributionApi.md#get_file_distribution) | **GET** /data/{id}/distribution | Get file distribution
[**get_file_storage_locations**](FileDistributionApi.md#get_file_storage_locations) | **GET** /data/{id}/storage_locations | Get file storage locations

# **get_file_distribution**
> FileDistribution get_file_distribution(id)

Get file distribution

Returns information about distribution of a specific file among different storage providers.  ***Example cURL requests***  **Get file distribution** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/distribution\"  {   \"type\": \"REG\"   \"distributionPerProvider\": {     \"$PROVIDER_ID1\": {       \"success\": true       \"logicalSize\": 8       \"distributionPerStorage\": {         \"$STORAGE_ID\": {           \"blocks\": [[0, 4], [6, 2]]           \"physicalSize\": 6         }       }     }     \"$PROVIDER_ID2\": {       \"success\": false       \"distributionPerStorage\": {         \"$STORAGE_ID\": {           \"error\": {             \"description\": \"Operation failed with POSIX error: enoent.\"             \"details\": {               \"errno\": \"enoent\"             }           }         }       }     }   } } ``` 

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
api_instance = oneprovider_client.FileDistributionApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | The Id of the file

try:
    # Get file distribution
    api_response = api_instance.get_file_distribution(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileDistributionApi->get_file_distribution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the file | 

### Return type

[**FileDistribution**](FileDistribution.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_storage_locations**
> StorageFileLocations get_file_storage_locations(id)

Get file storage locations

Returns information about regular file location on each storage. `null` value for a storage  means that there is no file replica on this storage.  ***Example cURL requests***  **Get file storage locations** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/storage_locations\"  {   \"locationsPerProvider\": {     \"$PROVIDER_ID1\": {       \"locationsPerStorage\": {         \"$STORAGE_ID1\": \"path/to/file\"       }     },     \"$PROVIDER_ID2\": {       \"locationsPerStorage\": {         \"$STORAGE_ID2\": null       }     }   } } ``` 

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
api_instance = oneprovider_client.FileDistributionApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | The Id of the file

try:
    # Get file storage locations
    api_response = api_instance.get_file_storage_locations(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileDistributionApi->get_file_storage_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the file | 

### Return type

[**StorageFileLocations**](StorageFileLocations.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

