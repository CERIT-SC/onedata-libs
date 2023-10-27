# Slice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Indicates the mode of the query. The &#x60;slice&#x60; mode returns a collection of slices  of requested time series and metrics that were specified in the &#x60;layout&#x60; field (which may express a subset of the queried collection). A metric slice is a list of time windows in descending order. The list may be incomplete, since windows are created as needed - along with the first measurement falling in their timespan. Missing windows  should be treated as windows with zero value.  | [optional] 
**layout** | [**TimeSeriesLayout**](TimeSeriesLayout.md) |  | [optional] 
**start_timestamp** | **str** | Latest timestamp used to determine the starting point for descending listing of time windows.  The first window to be listed is the one that includes the given timestamp in its timespan.  If no such window exists, the next existing one is taken.  | [optional] 
**stop_timestamp** | **str** | Oldest timestamp used to determine the end of descending listing of time windows.   The last window to be listed is the one that includes the given timestamp in its timespan.  If no such window exists, the previous existing one is taken.  | [optional] 
**window_limit** | **str** | Maximum number of time windows to be listed. | [optional] 
**extended_info** | **str** | If true, information about the first and last timestamp of measurements per window will be included. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

