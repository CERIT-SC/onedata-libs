# Ip

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | IP caveat - limits the allowed client IPs to a certain whitelist (masks are supported).  You can learn more about token caveats [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[token-caveats].html).  | [optional] 
**whitelist** | **list[str]** | List of IPs or masks that are allowed to utilize the token.  Example: &#x60;&#x60;&#x60;json   {     \&quot;type\&quot;: \&quot;ip\&quot;,     \&quot;whitelist\&quot;: [       \&quot;189.34.15.0/24\&quot;,       \&quot;127.0.0.0/8\&quot;,       \&quot;167.73.12.17\&quot;     ]   } &#x60;&#x60;&#x60;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

