# Api

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | API caveat - limits the API operations that can be performed with the token. The operations are whitelisted using the Onedata API matchspec format, which includes the service identifier, operation type (CRUD) and resource identifier.  You can learn more about token caveats [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[token-caveats].html).  | [optional] 
**whitelist** | **list[str]** | List of API matchspecs that narrow down allowed API calls.  Example: &#x60;&#x60;&#x60;json   {     \&quot;type\&quot;: \&quot;api\&quot;,     \&quot;whitelist\&quot;: [       \&quot;ozw/all/user.*.*:*\&quot;,       \&quot;all/get/space.*.*:*\&quot;     ]   } &#x60;&#x60;&#x60;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

