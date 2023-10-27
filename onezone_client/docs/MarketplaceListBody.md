# MarketplaceListBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **list[str]** | A list of tags to be used as listing filter. The resulting list will contain only the spaces that have at least one of the specified tags. Available space tags can be retrieved from the [configuration endpoint](#operation/get_configuration).  | [optional] 
**limit** | **int** | Allows specifying maximum number of spaces that should be returned. If there are more spaces, they can be retrieved using the &#x60;token&#x60; or &#x60;index&#x60; options in the consecutive call.  | [optional] 
**token** | **str** | Determines the starting point for listing. The listing will start from the next page (batch) of entries which follows the page previously obtained along with the corresponding &#x60;nextPageToken&#x60;. Cannot be provided alongside the &#x60;index&#x60; parameter.  | [optional] 
**index** | **str** | Determines the starting point for listing - it will be started from given space (inclusively). Cannot be provided alongside the &#x60;token&#x60; parameter.  | [optional] 
**offset** | **int** | Expressed in number of entries, further adjusts the starting point of listing indicated by &#x60;index&#x60; or &#x60;token&#x60; parameters. The value can be negative, in such case entries preceding the starting point will be returned.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

