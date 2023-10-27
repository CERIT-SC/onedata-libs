# SupportStageDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_stage** | **str** | Current support stage of the provider - depends on the stages of its storages: * &#x60;joining&#x60; - the provider has freshly supported the space and is catching up   with dbsync changes from other providers  * &#x60;active&#x60; - the provider is operational and up-to-date with other providers,   all storages are in &#x27;active&#x27; stage  * &#x60;remodelling&#x60; - the provider is undergoing changes concerning its storage(s)   that support the space, e.g. a storage has been added or removed   and is not yet in active stage (such modifications may require   long-lasting data transfers between storages).  * &#x60;evicting_replicas&#x60; (unsupporting) - the provider has chosen to cease support   for the space with all of its storages and is now safely migrating   data to other providers  * &#x60;purging_storages&#x60; (unsupporting) - the provider has evicted all replicas and   is now purging its storages from support remnants  * &#x60;purging_database&#x60; (unsupporting) - the provider purged its storages and is   now purging the database (including file metadata, locations etc)  * &#x60;retired&#x60; - the provider has supported the space in the past, but not anymore  | [optional] 
**per_storage** | **dict(str, str)** | The map of storage Ids of the provider that support this space and their corresponding support stages.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

