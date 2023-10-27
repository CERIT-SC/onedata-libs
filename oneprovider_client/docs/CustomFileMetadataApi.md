# oneprovider_client.CustomFileMetadataApi

All URIs are relative to */api/v3/oneprovider*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_json_metadata**](CustomFileMetadataApi.md#get_json_metadata) | **GET** /data/{id}/metadata/json | Get file json metadata
[**get_rdf_metadata**](CustomFileMetadataApi.md#get_rdf_metadata) | **GET** /data/{id}/metadata/rdf | Get file rdf metadata
[**get_xattrs**](CustomFileMetadataApi.md#get_xattrs) | **GET** /data/{id}/metadata/xattrs | Get file extended attributes
[**remove_json_metadata**](CustomFileMetadataApi.md#remove_json_metadata) | **DELETE** /data/{id}/metadata/json | Remove file json metadata
[**remove_rdf_metadata**](CustomFileMetadataApi.md#remove_rdf_metadata) | **DELETE** /data/{id}/metadata/rdf | Remove file rdf metadata
[**remove_xattrs**](CustomFileMetadataApi.md#remove_xattrs) | **DELETE** /data/{id}/metadata/xattrs | Remove file xattrs
[**set_json_metadata**](CustomFileMetadataApi.md#set_json_metadata) | **PUT** /data/{id}/metadata/json | Set file json metadata
[**set_rdf_metadata**](CustomFileMetadataApi.md#set_rdf_metadata) | **PUT** /data/{id}/metadata/rdf | Set file rdf metadata
[**set_xattr**](CustomFileMetadataApi.md#set_xattr) | **PUT** /data/{id}/metadata/xattrs | Set file extended attribute

# **get_json_metadata**
> str get_json_metadata(id, filter_type=filter_type, filter=filter, inherited=inherited, resolve_symlink=resolve_symlink)

Get file json metadata

This method returns the json metadata associated with file specified by [$FILE_ID](#operation/lookup_file_id).  By default the method returns the complete json metadata. But it is possible to request only a part of the document by specifying `filter_type` and `filter` attributes in the query.  Supported filter types are:   * **keypath** - list of JSON keys which point to requested JSON object,     separated by `.`, array elements should be expressed as `[i]`     (e.g. `key1.key2.[2].key3`)  ***Example cURL requests***  **Get specific JSON value from metadata document** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/json?filter_type=keypath&filter=key1.key2.[2].key3  {\"key4\": \"value\"} ``` 

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
api_instance = oneprovider_client.CustomFileMetadataApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | Id of the file.
filter_type = 'filter_type_example' # str | The type of filter to apply to the metadata document. (optional)
filter = 'filter_example' # str | The filter to apply to the metadata document before returning. Required if `filter_type` is specified.  (optional)
inherited = true # bool | When set to true, this operation will merge the metadata documents from parent directories as well as entire space into a single JSON document.  (optional)
resolve_symlink = true # bool | Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`).  (optional) (default to true)

try:
    # Get file json metadata
    api_response = api_instance.get_json_metadata(id, filter_type=filter_type, filter=filter, inherited=inherited, resolve_symlink=resolve_symlink)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFileMetadataApi->get_json_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the file. | 
 **filter_type** | **str**| The type of filter to apply to the metadata document. | [optional] 
 **filter** | **str**| The filter to apply to the metadata document before returning. Required if &#x60;filter_type&#x60; is specified.  | [optional] 
 **inherited** | **bool**| When set to true, this operation will merge the metadata documents from parent directories as well as entire space into a single JSON document.  | [optional] 
 **resolve_symlink** | **bool**| Indicates whether the operation should be performed on the symbolic link itself (&#x60;false&#x60;) or on the target file that it points to (&#x60;true&#x60;).  | [optional] [default to true]

### Return type

**str**

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rdf_metadata**
> str get_rdf_metadata(id, resolve_symlink=resolve_symlink)

Get file rdf metadata

This method returns the rdf metadata for a file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Get complete RDF metadata document for file**  ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/rdf  <RDF><homepage>https://www.onedata.org</homepage></RDF> ``` 

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
api_instance = oneprovider_client.CustomFileMetadataApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | Id of the file.
resolve_symlink = true # bool | Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`).  (optional) (default to true)

try:
    # Get file rdf metadata
    api_response = api_instance.get_rdf_metadata(id, resolve_symlink=resolve_symlink)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFileMetadataApi->get_rdf_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the file. | 
 **resolve_symlink** | **bool**| Indicates whether the operation should be performed on the symbolic link itself (&#x60;false&#x60;) or on the target file that it points to (&#x60;true&#x60;).  | [optional] [default to true]

### Return type

**str**

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/rdf+xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xattrs**
> dict(str, str) get_xattrs(id, attribute=attribute, inherited=inherited, show_internal=show_internal, resolve_symlink=resolve_symlink)

Get file extended attributes

This method returns the selected extended attributes associated with file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Get extended file attributes** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/xattrs?attribute=license\"  {     \"license\": \"CC-0\" } ``` 

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
api_instance = oneprovider_client.CustomFileMetadataApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | Id of the file.
attribute = 'attribute_example' # str | Name of attribute to query for. (optional)
inherited = false # bool | When set to true, this operation returns attributes including those inherited from parent directories and from the space root directory. If the same attribute is set on different nesting levels, the lowest level takes precedence (e.g. file attributes override the attributes from its parent directory).  (optional) (default to false)
show_internal = false # bool | When set to true, this operation returns all attributes including those normally not shown (e.g. json/rdf metadata, acl and cdmi attributes).  (optional) (default to false)
resolve_symlink = true # bool | Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`).  (optional) (default to true)

try:
    # Get file extended attributes
    api_response = api_instance.get_xattrs(id, attribute=attribute, inherited=inherited, show_internal=show_internal, resolve_symlink=resolve_symlink)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFileMetadataApi->get_xattrs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the file. | 
 **attribute** | **str**| Name of attribute to query for. | [optional] 
 **inherited** | **bool**| When set to true, this operation returns attributes including those inherited from parent directories and from the space root directory. If the same attribute is set on different nesting levels, the lowest level takes precedence (e.g. file attributes override the attributes from its parent directory).  | [optional] [default to false]
 **show_internal** | **bool**| When set to true, this operation returns all attributes including those normally not shown (e.g. json/rdf metadata, acl and cdmi attributes).  | [optional] [default to false]
 **resolve_symlink** | **bool**| Indicates whether the operation should be performed on the symbolic link itself (&#x60;false&#x60;) or on the target file that it points to (&#x60;true&#x60;).  | [optional] [default to true]

### Return type

**dict(str, str)**

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_json_metadata**
> remove_json_metadata(id, resolve_symlink=resolve_symlink)

Remove file json metadata

Removes json metadata from the file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Remove file json metadata** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/json ``` 

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
api_instance = oneprovider_client.CustomFileMetadataApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | Id of the file.
resolve_symlink = true # bool | Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`).  (optional) (default to true)

try:
    # Remove file json metadata
    api_instance.remove_json_metadata(id, resolve_symlink=resolve_symlink)
except ApiException as e:
    print("Exception when calling CustomFileMetadataApi->remove_json_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the file. | 
 **resolve_symlink** | **bool**| Indicates whether the operation should be performed on the symbolic link itself (&#x60;false&#x60;) or on the target file that it points to (&#x60;true&#x60;).  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_rdf_metadata**
> remove_rdf_metadata(id, resolve_symlink=resolve_symlink)

Remove file rdf metadata

Removes rdf metadata from the file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Remove file rdf metadata** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/rdf ``` 

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
api_instance = oneprovider_client.CustomFileMetadataApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | Id of the file.
resolve_symlink = true # bool | Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`).  (optional) (default to true)

try:
    # Remove file rdf metadata
    api_instance.remove_rdf_metadata(id, resolve_symlink=resolve_symlink)
except ApiException as e:
    print("Exception when calling CustomFileMetadataApi->remove_rdf_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the file. | 
 **resolve_symlink** | **bool**| Indicates whether the operation should be performed on the symbolic link itself (&#x60;false&#x60;) or on the target file that it points to (&#x60;true&#x60;).  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_xattrs**
> remove_xattrs(body, id, resolve_symlink=resolve_symlink)

Remove file xattrs

Removes specific xattrs from the file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Remove specific file xattrs** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/xattrs \\ -H 'Content-Type: application/json' -d '{ \"keys\": [\"license\"] }' ``` 

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
api_instance = oneprovider_client.CustomFileMetadataApi(oneprovider_client.ApiClient(configuration))
body = oneprovider_client.MetadataXattrsBody() # MetadataXattrsBody | The xattrs to remove.
id = 'id_example' # str | Id of the file.
resolve_symlink = true # bool | Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`).  (optional) (default to true)

try:
    # Remove file xattrs
    api_instance.remove_xattrs(body, id, resolve_symlink=resolve_symlink)
except ApiException as e:
    print("Exception when calling CustomFileMetadataApi->remove_xattrs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataXattrsBody**](MetadataXattrsBody.md)| The xattrs to remove. | 
 **id** | **str**| Id of the file. | 
 **resolve_symlink** | **bool**| Indicates whether the operation should be performed on the symbolic link itself (&#x60;false&#x60;) or on the target file that it points to (&#x60;true&#x60;).  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_json_metadata**
> set_json_metadata(body, id, filter_type=filter_type, filter=filter, resolve_symlink=resolve_symlink)

Set file json metadata

This method allows to set json metadata for a file specified by [$FILE_ID](#operation/lookup_file_id).  This operation will replace the previous json metadata if any.  ***Example cURL requests***  **Set JSON metadata for file** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/json \\ -H \"Content-Type: application/json\" -d '{     \"key1\": {         \"key2\": [\"val1\", \"val2\", \"val3\", \"val4\"]     } }' ``` 

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
api_instance = oneprovider_client.CustomFileMetadataApi(oneprovider_client.ApiClient(configuration))
body = 'body_example' # str | The json metadata.
id = 'id_example' # str | Id of the file.
filter_type = 'filter_type_example' # str | The type of filter to apply to the metadata document. (optional)
filter = 'filter_example' # str | The filter allowing to set specific metadata document key. Required if `filter_type` is specified.  (optional)
resolve_symlink = true # bool | Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`).  (optional) (default to true)

try:
    # Set file json metadata
    api_instance.set_json_metadata(body, id, filter_type=filter_type, filter=filter, resolve_symlink=resolve_symlink)
except ApiException as e:
    print("Exception when calling CustomFileMetadataApi->set_json_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| The json metadata. | 
 **id** | **str**| Id of the file. | 
 **filter_type** | **str**| The type of filter to apply to the metadata document. | [optional] 
 **filter** | **str**| The filter allowing to set specific metadata document key. Required if &#x60;filter_type&#x60; is specified.  | [optional] 
 **resolve_symlink** | **bool**| Indicates whether the operation should be performed on the symbolic link itself (&#x60;false&#x60;) or on the target file that it points to (&#x60;true&#x60;).  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_rdf_metadata**
> set_rdf_metadata(body, id, resolve_symlink=resolve_symlink)

Set file rdf metadata

This method allows to set specific rdf metadata for a file specified by [$FILE_ID](#operation/lookup_file_id).  This operation will replace the previous rdf metadata if any.  ***Example cURL requests***  **Set RDF metadata for space from RDF file** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/rdf \\ -H \"Content-Type: application/rdf+xml\" -d \"@./space1_dublincore.rdf\" ``` 

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
api_instance = oneprovider_client.CustomFileMetadataApi(oneprovider_client.ApiClient(configuration))
body = 'body_example' # str | The rdf metadata.
id = 'id_example' # str | Id of the file.
resolve_symlink = true # bool | Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`).  (optional) (default to true)

try:
    # Set file rdf metadata
    api_instance.set_rdf_metadata(body, id, resolve_symlink=resolve_symlink)
except ApiException as e:
    print("Exception when calling CustomFileMetadataApi->set_rdf_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| The rdf metadata. | 
 **id** | **str**| Id of the file. | 
 **resolve_symlink** | **bool**| Indicates whether the operation should be performed on the symbolic link itself (&#x60;false&#x60;) or on the target file that it points to (&#x60;true&#x60;).  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/rdf+xml
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_xattr**
> set_xattr(id, body=body, resolve_symlink=resolve_symlink)

Set file extended attribute

This method allows to set a value of a given extended file attributes (leaving other ones intact) for a file specified by [$FILE_ID](#operation/lookup_file_id).  ***Example cURL requests***  **Set extended file attribute** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$FILE_ID/metadata/xattrs\" \\ -H 'Content-Type: application/json' -d '{ \"license\": \"CC-0\" }' ``` 

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
api_instance = oneprovider_client.CustomFileMetadataApi(oneprovider_client.ApiClient(configuration))
id = 'id_example' # str | Id of the file.
body = NULL # dict(str, str) | Extended attribute name and value. (optional)
resolve_symlink = true # bool | Indicates whether the operation should be performed on the symbolic link itself (`false`) or on the target file that it points to (`true`).  (optional) (default to true)

try:
    # Set file extended attribute
    api_instance.set_xattr(id, body=body, resolve_symlink=resolve_symlink)
except ApiException as e:
    print("Exception when calling CustomFileMetadataApi->set_xattr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the file. | 
 **body** | [**dict(str, str)**](dict.md)| Extended attribute name and value. | [optional] 
 **resolve_symlink** | **bool**| Indicates whether the operation should be performed on the symbolic link itself (&#x60;false&#x60;) or on the target file that it points to (&#x60;true&#x60;).  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

