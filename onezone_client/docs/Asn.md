# Asn

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | ASN caveat - limits the ASNs (Autonomous System Number) from which the token can be utilized. The client&#x27;s ASN is resolved based on client&#x27;s IP and MaxMind&#x27;s GeoLite database.  You can learn more about token caveats [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[token-caveats].html).  | [optional] 
**whitelist** | **list[int]** | List of ASNs from which the token can be utilized.  Example: &#x60;&#x60;&#x60;json   {     \&quot;type\&quot;: \&quot;asn\&quot;,     \&quot;whitelist\&quot;: [       631, 632, 1671     ]   } &#x60;&#x60;&#x60;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

