# oneprovider_client.ViewApi

All URIs are relative to */api/v3/oneprovider*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_space_view**](ViewApi.md#create_space_view) | **PUT** /spaces/{sid}/views/{view_name} | Create view
[**get_space_view**](ViewApi.md#get_space_view) | **GET** /spaces/{sid}/views/{view_name} | Get view
[**get_space_views**](ViewApi.md#get_space_views) | **GET** /spaces/{sid}/views | Get all space views
[**query_space_view**](ViewApi.md#query_space_view) | **GET** /spaces/{sid}/views/{view_name}/query | Query view
[**remove_space_view**](ViewApi.md#remove_space_view) | **DELETE** /spaces/{sid}/views/{view_name} | Remove view
[**remove_view_reduce_function**](ViewApi.md#remove_view_reduce_function) | **DELETE** /spaces/{sid}/views/{view_name}/reduce | Remove view reduce function
[**update_space_view**](ViewApi.md#update_space_view) | **PATCH** /spaces/{sid}/views/{view_name} | Update view
[**update_view_reduce_function**](ViewApi.md#update_view_reduce_function) | **PUT** /spaces/{sid}/views/{view_name}/reduce | Update view reduce function

# **create_space_view**
> create_space_view(body, sid, view_name, spatial=spatial, update_min_changes=update_min_changes, replica_update_min_changes=replica_update_min_changes, providers=providers)

Create view

This method creates or replaces an existing view with a new one.  This operation requires `space_manage_views` privilege.  ***Example cURL requests***  **Create space view** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/$VIEW_NAME?spatial=false&providers[]=$PROVIDER_ID_1&providers[]=$PROVIDER_ID_2 \\ -H \"Content-Type: application/javascript\" -d \"@./my_view1.js\" ``` 

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
api_instance = oneprovider_client.ViewApi(oneprovider_client.ApiClient(configuration))
body = 'body_example' # str | The view map function.
sid = 'sid_example' # str | Space Id in which view will be created. 
view_name = 'view_name_example' # str | Name of the view.
spatial = false # bool | Specifies whether view is spatial or not. (optional) (default to false)
update_min_changes = 56 # int | Minimum number of document changes to trigger re-viewing. (optional)
replica_update_min_changes = 56 # int | Minimum number of document changes to trigger re-viewing of a replica view. (optional)
providers = ['providers_example'] # list[str] | Providers which will create view. (optional)

try:
    # Create view
    api_instance.create_space_view(body, sid, view_name, spatial=spatial, update_min_changes=update_min_changes, replica_update_min_changes=replica_update_min_changes, providers=providers)
except ApiException as e:
    print("Exception when calling ViewApi->create_space_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| The view map function. | 
 **sid** | **str**| Space Id in which view will be created.  | 
 **view_name** | **str**| Name of the view. | 
 **spatial** | **bool**| Specifies whether view is spatial or not. | [optional] [default to false]
 **update_min_changes** | **int**| Minimum number of document changes to trigger re-viewing. | [optional] 
 **replica_update_min_changes** | **int**| Minimum number of document changes to trigger re-viewing of a replica view. | [optional] 
 **providers** | [**list[str]**](str.md)| Providers which will create view. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/javascript
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space_view**
> View get_space_view(sid, view_name)

Get view

This method returns a JSON describing specific view.  This operation requires `space_view_views` privilege.  ***Example cURL requests***  **Get information about specific view** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/$VIEW_NAME  {     \"spatial\": false,     \"mapFunction\": \"function (id, type, meta, ctx) {\\\\n        if(type == \\\\'custom_metadata\\\\' && meta[\\\\'onexattr\\\\']) {\\\\n            return [meta[\\\\'onexattr\\\\'], id];\\\\n        }\\\\n        return null;\\\\n    }\"     \"reduceFunction\": null,     \"viewOptions\": {         \"update_min_changes\": 100     },     \"providers\": [         \"6b9bc70630547d925861a27e1f050dfe\"     ] } ``` 

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
api_instance = oneprovider_client.ViewApi(oneprovider_client.ApiClient(configuration))
sid = 'sid_example' # str | Space Id in which view exist. 
view_name = 'view_name_example' # str | Name of the view.

try:
    # Get view
    api_response = api_instance.get_space_view(sid, view_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewApi->get_space_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Space Id in which view exist.  | 
 **view_name** | **str**| Name of the view. | 

### Return type

[**View**](View.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space_views**
> Views get_space_views(sid, limit=limit, page_token=page_token)

Get all space views

Returns the list of all view names in a space. The list is broken down into pages, each with length less or equal to the limit parameter. If the nextPageToken in the response has non-null value, there are more names to list - provide the token in the page_token parameter in the following request.  This operation requires `space_view_views` privilege.  ***Example cURL requests***  **List at most 3 view names starting from page id 757136151113c2f** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views?limit=3&page_token=757136151113c2f\"  {     \"views\": [         \"favourites\",         \"images\",         \"videos\"     ],     \"nextPageToken\": \"8471726779817b3a\" } ``` 

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
api_instance = oneprovider_client.ViewApi(oneprovider_client.ApiClient(configuration))
sid = 'sid_example' # str | Space Id in which to list views. 
limit = 100 # int | Allows to limit the number of returned views.  (optional) (default to 100)
page_token = 'page_token_example' # str | Allows to start the listing from a certain point, identified by the page token.  (optional)

try:
    # Get all space views
    api_response = api_instance.get_space_views(sid, limit=limit, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewApi->get_space_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Space Id in which to list views.  | 
 **limit** | **int**| Allows to limit the number of returned views.  | [optional] [default to 100]
 **page_token** | **str**| Allows to start the listing from a certain point, identified by the page token.  | [optional] 

### Return type

[**Views**](Views.md)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_space_view**
> list[object] query_space_view(sid, view_name, descending=descending, key=key, keys=keys, limit=limit, skip=skip, startkey=startkey, startkey_docid=startkey_docid, endkey=endkey, endkey_docid=endkey_docid, inclusive_end=inclusive_end, stale=stale, bbox=bbox, spatial=spatial, start_range=start_range, end_range=end_range)

Query view

This method returns the list of result objects for files which match the query on a predefined view. Those objects contains following fields: * ``id`` - for use as `startkey_docid` or `endkey_docid` in following queries * ``key`` - the first element of list returned by user defined mapping/spatial function * ``value`` - the second element of list returned by user defined mapping/spatial function * ``geometry`` - describes geometry of data (only available in case of spatial views)  Currently, views are defined per space, i.e. the result will be limited to files and directories in a space for which the view was defined.  This operation supports also custom view query attributes as provided by [Couchbase](http://docs.couchbase.com/admin/admin/Views/views-querying.html).  Additionaly, Couchbase [spatial queries](http://docs.couchbase.com/admin/admin/Views/views-geospatial.html) are possible using `bbox` query parameter. These queries are possible on views which emit values conforming to the [GeoJSON](http://geojson.org/) format.  This operation requires `space_query_views` privilege.  ***Example cURL requests***  **Get 4 files from view skipping first 10**  With example map function used: ```javascript function (id, type, meta, ctx) {     if(type == 'custom_metadata' && meta['onexattr']) {         return [meta['onexattr'], id];     }     return null; } ```  ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/VIEW_NAME/query?skip=10&limit=4  [     {         \"id\": \"fd18b793d446099ae84f8bd5c054ad34\",         \"key\": 1,         \"value\": \"00000000002C45416775696423633062636533343133336336636633393238336134323333396430656461393323737061636531\"     },     {         \"id\": \"2785dbd91120e341265f9ee2370ccf08\",         \"key\": 2,         \"value\": \"00000000002CF7DB6775696423396261373964653764643866336432393436323262313133393738643338383323737061636531\"     },     {         \"id\": \"60a9e6da61e12deeb3e6c688fe861c01\",         \"key\": 3,         \"value\": \"00000000002C47916775696423336330336538623730333439353233383631313966346139343731316631656323737061636531\"     },     {         \"id\": \"651d696a8446e92ab55de163f9b8594d\",         \"key\": 4,         \"value\": \"00000000002CA8906775696423633835366438613139666565336337666165623538303736356465383039356223737061636531\"     },     ... ] ```  **Get list of files associated with geospatial coordinates**  With example spatial function used: ```javascript function (id, type, meta, ctx) {     if(type == 'custom_metadata' && meta['onexattr']) {         return [meta['onexattr'], id];     }     return null; } ```  ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/$VIEW_NAME/query?spatial=true&stale=false  [     {         \"geometry\": {             \"type\": \"Point\",             \"coordinates\": [0, 0]         },         \"id\": \"36cfb018c312653e65b346c421d7a678\",         \"key\": [[0, 0], [0, 0]],         \"value\": \"00000000002C5DA36775696423663535633934306564393632656530666133663330633137393362333765356223737061636531\"     },     {         \"geometry\": {             \"type\": \"Point\",             \"coordinates\": [5.1, 10.22]         },         \"id\": \"972eb78ff8e262c4bebdc11799c20f51\",         \"key\": [[5.1, 5.1], [10.22, 10.22]],         \"value\": \"00000000002C678A6775696423363030666461383130623030386333616664363637396666653334366137656623737061636531\"     } ] ```  **Get file popularity for a specific space** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/file-popularity/query?spatial=true&start_range=\\[1,0,0,0,0,0\\]&end_range=\\[null,null,null,null,null,null\\]\" ``` 

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
api_instance = oneprovider_client.ViewApi(oneprovider_client.ApiClient(configuration))
sid = 'sid_example' # str | Space Id in which view exist.
view_name = 'view_name_example' # str | Name of the view.
descending = false # bool | Return the documents in descending order (by key). (optional) (default to false)
key = 'key_example' # str | Return only documents that match the specified key. Key must be specified as a JSON value.  (optional)
keys = 'keys_example' # str | Return only documents that match any of the keys specified within the given array. Keys must be specified as a JSON array, escaped properly. Sorting is not applied when using this option.  (optional)
limit = 56 # int | Limit the number of the returned documents to the specified number.  (optional)
skip = 56 # int | Skip this number of records before starting to return the results.  (optional)
startkey = 'startkey_example' # str | Return records with a value equal to or greater than the specified key. Key must be specified as a JSON value.  (optional)
startkey_docid = 'startkey_docid_example' # str | Return records starting with the specified document Id.  (optional)
endkey = 'endkey_example' # str | Stop returning records when the specified key is reached. Key must be specified as a JSON value.  (optional)
endkey_docid = 'endkey_docid_example' # str | Stop returning records when the specified document Id is reached.  (optional)
inclusive_end = false # bool | Specifies whether the specified end key is included in the result. ***Note:*** Do not use `inclusive_end` with `key` or `keys`.  (optional) (default to false)
stale = 'update_after' # str | Allow records from a stale view to be used. Allowed values are `ok`, `update_after` or `false`.  (optional) (default to update_after)
bbox = 'bbox_example' # str | Specify the bounding box for a spatial query (e.g. ?bbox=-180,-90,0,0)  (optional)
spatial = true # bool | Enable spatial type of query. When querying the file-popularity view, the `start_range` and `end_range` constraints should be specified as 6-dimensional arrays, with the following fields: `[SizeLowerLimit, LastOpenHoursEpochLowerLimit, TotalOpenLowerLimit, HoursOpenAvgLowerLimit, DayOpenAvgLowerLimit, MonthOpenAvgLowerLimit]`.  (optional)
start_range = 'start_range_example' # str | Array specifying the range in spatial queries (e.g. `start_range=[1,0,0,0,0,0]`). (optional)
end_range = 'end_range_example' # str | Array specifying the range in spatial queries (e.g. `end_range=[null,null,null,null,null,null]`). (optional)

try:
    # Query view
    api_response = api_instance.query_space_view(sid, view_name, descending=descending, key=key, keys=keys, limit=limit, skip=skip, startkey=startkey, startkey_docid=startkey_docid, endkey=endkey, endkey_docid=endkey_docid, inclusive_end=inclusive_end, stale=stale, bbox=bbox, spatial=spatial, start_range=start_range, end_range=end_range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewApi->query_space_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Space Id in which view exist. | 
 **view_name** | **str**| Name of the view. | 
 **descending** | **bool**| Return the documents in descending order (by key). | [optional] [default to false]
 **key** | **str**| Return only documents that match the specified key. Key must be specified as a JSON value.  | [optional] 
 **keys** | **str**| Return only documents that match any of the keys specified within the given array. Keys must be specified as a JSON array, escaped properly. Sorting is not applied when using this option.  | [optional] 
 **limit** | **int**| Limit the number of the returned documents to the specified number.  | [optional] 
 **skip** | **int**| Skip this number of records before starting to return the results.  | [optional] 
 **startkey** | **str**| Return records with a value equal to or greater than the specified key. Key must be specified as a JSON value.  | [optional] 
 **startkey_docid** | **str**| Return records starting with the specified document Id.  | [optional] 
 **endkey** | **str**| Stop returning records when the specified key is reached. Key must be specified as a JSON value.  | [optional] 
 **endkey_docid** | **str**| Stop returning records when the specified document Id is reached.  | [optional] 
 **inclusive_end** | **bool**| Specifies whether the specified end key is included in the result. ***Note:*** Do not use &#x60;inclusive_end&#x60; with &#x60;key&#x60; or &#x60;keys&#x60;.  | [optional] [default to false]
 **stale** | **str**| Allow records from a stale view to be used. Allowed values are &#x60;ok&#x60;, &#x60;update_after&#x60; or &#x60;false&#x60;.  | [optional] [default to update_after]
 **bbox** | **str**| Specify the bounding box for a spatial query (e.g. ?bbox&#x3D;-180,-90,0,0)  | [optional] 
 **spatial** | **bool**| Enable spatial type of query. When querying the file-popularity view, the &#x60;start_range&#x60; and &#x60;end_range&#x60; constraints should be specified as 6-dimensional arrays, with the following fields: &#x60;[SizeLowerLimit, LastOpenHoursEpochLowerLimit, TotalOpenLowerLimit, HoursOpenAvgLowerLimit, DayOpenAvgLowerLimit, MonthOpenAvgLowerLimit]&#x60;.  | [optional] 
 **start_range** | **str**| Array specifying the range in spatial queries (e.g. &#x60;start_range&#x3D;[1,0,0,0,0,0]&#x60;). | [optional] 
 **end_range** | **str**| Array specifying the range in spatial queries (e.g. &#x60;end_range&#x3D;[null,null,null,null,null,null]&#x60;). | [optional] 

### Return type

**list[object]**

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_space_view**
> remove_space_view(sid, view_name)

Remove view

This method removes an existing view.  This operation requires `space_manage_views` privilege.  ***Example cURL requests***  **Remove existing view** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/$VIEW_NAME ``` 

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
api_instance = oneprovider_client.ViewApi(oneprovider_client.ApiClient(configuration))
sid = 'sid_example' # str | Space Id in which view exist. 
view_name = 'view_name_example' # str | Name of the view.

try:
    # Remove view
    api_instance.remove_space_view(sid, view_name)
except ApiException as e:
    print("Exception when calling ViewApi->remove_space_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Space Id in which view exist.  | 
 **view_name** | **str**| Name of the view. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_view_reduce_function**
> remove_view_reduce_function(sid, view_name)

Remove view reduce function

This method removes the view reduce function.  This operation requires `space_manage_views` privilege.  ***Example cURL requests***  **Remove view reduce function** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/$VIEW_NAME/reduce ``` 

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
api_instance = oneprovider_client.ViewApi(oneprovider_client.ApiClient(configuration))
sid = 'sid_example' # str | Space Id in which view exist. 
view_name = 'view_name_example' # str | Name of the view.

try:
    # Remove view reduce function
    api_instance.remove_view_reduce_function(sid, view_name)
except ApiException as e:
    print("Exception when calling ViewApi->remove_view_reduce_function: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Space Id in which view exist.  | 
 **view_name** | **str**| Name of the view. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_space_view**
> update_space_view(sid, view_name, body=body, spatial=spatial, update_min_changes=update_min_changes, replica_update_min_changes=replica_update_min_changes, providers=providers)

Update view

This method updates existing view definition.  It takes the same arguments as PUT. Only specified parameters will be overwritten.  This operation requires `space_manage_views` privilege.  ***Example cURL requests***  **Update space view** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PATCH https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/$VIEW_NAME?update_min_changes=10 \\ -H \"Content-Type: application/javascript\" -d \"@./my_improved_view1.js\" ``` 

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
api_instance = oneprovider_client.ViewApi(oneprovider_client.ApiClient(configuration))
sid = 'sid_example' # str | Space Id in which view exist. 
view_name = 'view_name_example' # str | Name of the view.
body = 'body_example' # str | The view map function. (optional)
spatial = true # bool | Specifies whether view is spatial or not. (optional)
update_min_changes = 56 # int | Minimum number of document changes to trigger re-viewing. (optional)
replica_update_min_changes = 56 # int | Minimum number of document changes to trigger re-viewing of a replica view. (optional)
providers = ['providers_example'] # list[str] | Providers which will create view. (optional)

try:
    # Update view
    api_instance.update_space_view(sid, view_name, body=body, spatial=spatial, update_min_changes=update_min_changes, replica_update_min_changes=replica_update_min_changes, providers=providers)
except ApiException as e:
    print("Exception when calling ViewApi->update_space_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Space Id in which view exist.  | 
 **view_name** | **str**| Name of the view. | 
 **body** | [**str**](str.md)| The view map function. | [optional] 
 **spatial** | **bool**| Specifies whether view is spatial or not. | [optional] 
 **update_min_changes** | **int**| Minimum number of document changes to trigger re-viewing. | [optional] 
 **replica_update_min_changes** | **int**| Minimum number of document changes to trigger re-viewing of a replica view. | [optional] 
 **providers** | [**list[str]**](str.md)| Providers which will create view. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/javascript
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_view_reduce_function**
> update_view_reduce_function(body, sid, view_name)

Update view reduce function

This method replaces the existing view reduce function code with the request body.  The reduce functions are defined as JavaScript functions which are executed on the database backend.  This operation requires `space_manage_views` privilege.  ***Example cURL requests***  **Update space view** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X PUT https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/views/$VIEW_NAME/reduce \\ -H \"Content-Type: application/javascript\" -d \"@./my_improved_reduce_fun.js\" ``` 

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
api_instance = oneprovider_client.ViewApi(oneprovider_client.ApiClient(configuration))
body = 'body_example' # str | The view reduce function.
sid = 'sid_example' # str | Space Id in which view exist. 
view_name = 'view_name_example' # str | Name of the view.

try:
    # Update view reduce function
    api_instance.update_view_reduce_function(body, sid, view_name)
except ApiException as e:
    print("Exception when calling ViewApi->update_view_reduce_function: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| The view reduce function. | 
 **sid** | **str**| Space Id in which view exist.  | 
 **view_name** | **str**| Name of the view. | 

### Return type

void (empty response body)

### Authorization

[api_key1](../README.md#api_key1), [api_key2](../README.md#api_key2)

### HTTP request headers

 - **Content-Type**: application/javascript
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

