# DnsCheckResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | **str** | An interpretation of results obtained from DNS check. Possible values are: &#x27;unresolvable&#x27; - query returned empty results; &#x27;missing_records&#x27; - only some of the expected results were returned; &#x27;bad_records&#x27; - none of the expected results were returned; &#x27;ok&#x27; - all of expected values were present in obtained results.  | 
**expected** | **list[str]** | List of expected query results. | 
**got** | **list[str]** | List of obtained query results. | 
**recommended** | **list[str]** | List of suggested DNS records to set at your DNS provider to fulfill this check. Each record is provided in the format of BIND server. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

