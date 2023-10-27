# TransferCreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Requested type of transfer. Depending on selected type specifying also &#x60;replicatingProviderId&#x60;, &#x60;evictingProviderId&#x60; or both may be required.  | 
**replicating_provider_id** | **str** | Id of provider to which data will be copied, ensuring that the provider has a complete replica at the end of the process. The data will be copied from one or more providers in the space that hold replicas or some fragments.  | [optional] 
**evicting_provider_id** | **str** | Id of provider from which replica(s) are to be removed. Eviction is safe - will succeed only if there is at least one complete replica (accumulated) on other providers in the space.  | [optional] 
**callback** | **str** | This parameter allows the user to specify a REST callback URL which will be called (http &#x60;POST&#x60; request with transfer Id in body) when the transfer is complete.  | [optional] 
**data_source_type** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

