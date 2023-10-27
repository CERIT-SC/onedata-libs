# SpaceFilePopularityConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | If true, collecting file-popularity mechanism in the space is enabled. | [optional] 
**example_query** | **str** | Example &#x60;curl&#x60; command that can be executed to query the file-popularity view in the space.  | [optional] 
**last_open_hour_weight** | **float** | Weight of &#x60;lastOpenHour&#x60; parameter.  | [optional] [default to 1.0]
**avg_open_count_per_day_weight** | **float** | Weight of &#x60;avgOpenCountPerDayWeight&#x60; parameter.  | [optional] [default to 20.0]
**max_avg_open_count_per_day** | **float** | Maximal value of average open count per day taken to calculate the value of popularity function.  | [optional] [default to 100.0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

