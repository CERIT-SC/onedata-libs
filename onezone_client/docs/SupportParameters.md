# SupportParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_enabled** | **bool** | Indicates if accounting is enabled. The accounting mechanism utilizes directory statistics to keep track of quota usage within a space for the corresponding supporting provider.&lt;br/&gt; It can be toggled by an administrator of the provider with &#x60;cluster_update&#x60; privilege or by an administrator of the zone with &#x60;oz_spaces_update&#x60; privilege.  | [optional] 
**dir_stats_service_enabled** | **bool** | Indicates if the directory statistics service should be enabled. The service gathers statistics concerning logical and physical directory size, file count and update times.&lt;br/&gt; It can be toggled by a space member with &#x60;space_update&#x60; privilege, by an administrator of the provider with &#x60;cluster_update&#x60; privilege or by an administrator of the zone with &#x60;oz_spaces_update&#x60; privilege.&lt;br/&gt; **NOTE**: Directory statistics are required for accounting and cannot be disabled independently.&lt;br/&gt; **NOTE**: Statistics collection causes an additional load on the provider and has a slight negative impact on file operation performance.&lt;br/&gt; **NOTE**: Applying a new setting may take some time, depending on the space size and current state of the directory statistics service. This process is reflected by the &#x60;initializing&#x60; and &#x60;stopping&#x60; intermediate statuses.  | [optional] 
**dir_stats_service_status** | **str** | The current status of the directory statistics service, as reported by the supporting provider. It cannot be modified by a user. May be different from the &#x60;dirStatsServiceEnabled&#x60; setting if the service is in one of the intermediate states or the provider has not yet acknowledged a change in the parameters.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

