# TokenPropertyMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_time** | [**Timestamp**](Timestamp.md) |  | [optional] 
**usage_limit** | **object** | (Invite tokens only) limits how many times the token can be consumed - can be a positive integer or the literal string \&quot;infinity\&quot;  | [optional] 
**usage_count** | **int** | (Invite tokens only) informs how many times the token has been consumed so far  | [optional] 
**privileges** | **list[str]** | (Invite tokens only) the list of privileges that will be granted to the joining user/group upon token consumption  | [optional] 
**custom** | [**TokenPropertyCustomMetadata**](TokenPropertyCustomMetadata.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

