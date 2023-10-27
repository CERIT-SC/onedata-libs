# VerifyAccessTokenRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | [**SerializedToken**](SerializedToken.md) |  | 
**peer_ip** | **str** | The IP address of the token bearer. | [optional] 
**service_token** | [**SerializedToken**](SerializedToken.md) |  | [optional] 
**consumer_token** | [**SerializedToken**](SerializedToken.md) |  | [optional] 
**interface** | **str** | The interface to which the token bearer has connected as seen by the verifying party. | [optional] 
**allow_data_access_caveats** | **bool** | Indication if verifying party allows data access caveats in the token. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

