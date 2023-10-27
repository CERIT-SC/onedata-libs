# QueryViewParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descending** | **bool** | Return the documents in descending order (by key). | [optional] [default to False]
**key** | **str** | Return only documents that match the specified key. Key must be specified as a JSON value.  | [optional] 
**limit** | **int** | Limit the number of the returned documents to the specified number.  | [optional] 
**skip** | **int** | Skip this number of records before starting to return the results.  | [optional] 
**startkey** | **str** | Return records with a value equal to or greater than the specified key. Key must be specified as a JSON value.  | [optional] 
**startkey_docid** | **str** | Return records starting with the specified document Id.  | [optional] 
**endkey** | **str** | Stop returning records when the specified key is reached. Key must be specified as a JSON value.  | [optional] 
**endkey_docid** | **str** | Stop returning records when the specified document Id is reached.  | [optional] 
**inclusive_end** | **bool** | Specifies whether the specified end key is included in the result. ***Note:*** Do not use &#x60;inclusive_end&#x60; with &#x60;key&#x60; or &#x60;keys&#x60;.  | [optional] [default to False]
**stale** | **str** | Allow records from a stale view to be used. Allowed values are &#x60;ok&#x60;, &#x60;update_after&#x60; or &#x60;false&#x60;.  | [optional] [default to 'update_after']
**bbox** | **str** | Specify the bounding box for a spatial query (e.g. &#x60;bbox&#x3D;-180,-90,0,0&#x60;)  | [optional] 
**spatial** | **bool** | Enable spatial type of query. When querying the file-popularity view, the &#x60;start_range&#x60; and &#x60;end_range&#x60; constraints should be specified as 6-dimensional arrays, with the following fields: &#x60;[SizeLowerLimit, LastOpenHoursEpochLowerLimit, TotalOpenLowerLimit, HoursOpenAvgLowerLimit, DayOpenAvgLowerLimit, MonthOpenAvgLowerLimit]&#x60;.  | [optional] 
**start_range** | **str** | Array specifying the range in spatial queries (e.g. &#x60;start_range&#x3D;[1,0,0,0,0,0]&#x60;).  | [optional] 
**end_range** | **str** | Array specifying the range in spatial queries (e.g. &#x60;end_range&#x3D;[null,null,null,null,null,null]&#x60;).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

