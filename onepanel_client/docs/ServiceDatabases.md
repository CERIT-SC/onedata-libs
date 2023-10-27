# ServiceDatabases

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | **list[str]** | The list of hosts where service should be deployed. | 
**server_quota** | **int** | The server quota is the RAM memory in bytes that is allocated to the server when Couchbase Server is first installed. This sets the limit of RAM allocated by Couchbase for caching data for all buckets and is configured on a per-node basis.  | [optional] 
**bucket_quota** | **int** | The bucket quota is the amount of RAM memory in bytes allocated to an individual bucket for caching data.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

