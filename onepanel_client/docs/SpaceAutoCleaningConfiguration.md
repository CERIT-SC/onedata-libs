# SpaceAutoCleaningConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | If true, auto-cleaning mechanism is enabled in the space. | [optional] 
**threshold** | **int** | Amount of data [b], which should trigger the auto-cleaning in the space. Only replicas maintained by this storage provider will be removed.  This parameter is required to enable auto-cleaning.  | [optional] 
**target** | **int** | Amount of data [b], at which the auto-cleaning process should stop. This parameter is required to enable auto-cleaning.  | [optional] 
**rules** | [**SpaceAutoCleaningRules**](SpaceAutoCleaningRules.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

