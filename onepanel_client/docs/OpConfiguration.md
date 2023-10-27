# OpConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_type** | **str** | Indicates that this is Oneprovider&#x27;s panel. | 
**provider_id** | **str** | This cluster&#x27;s Oneprovider Id. &#x60;null&#x60; if the Oneprovider is not registered or Oneprovider worker is down.  | 
**provider_name** | **str** | The name of this Oneprovider. If the cluster is not configured or malfunctioning (e.g. the op-worker service is down), the value may be &#x60;null&#x60;.  | 
**provider_domain** | **str** | The domain of this Oneprovider. If the cluster is not configured or malfunctioning (e.g. the op-worker service is down), the value may be &#x60;null&#x60;.  | 
**zone_domain** | **str** | The domain of the Onezone where this Oneprovider is registered. &#x60;null&#x60; if the Oneprovider is not registered.  | 
**is_registered** | **bool** | True if the Oneprovider has been registered at a Onezone.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

