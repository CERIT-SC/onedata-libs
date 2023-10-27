# View

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_source_type** | **str** | Indicates the method of determining files to be transferred.  &#x60;type &#x3D; \&quot;view\&quot;&#x60; - this transfer covers files that are returned as a result of querying chosen view. The view must be defined on all providers involved in the process and querying it must return a valid list of file ids to be transferred. For more information about views, please see [here](https://onedata.org/#/home/documentation/doc/using_onedata/replication_management.html#advanced-operations-using-views).  | [optional] 
**space_id** | **str** | Id of space containing the view. | [optional] 
**view_name** | **str** | Name of the view that will be queried to obtain the list of files to be transferred.  | [optional] 
**query_view_params** | [**QueryViewParams**](QueryViewParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

