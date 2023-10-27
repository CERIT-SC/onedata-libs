# Consumer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Consumer caveat - limits the consumers that can use the token. [Consumer](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[consumer].html) is the token bearer that utilizes the token - performs a request with an access token or attempts to consume an invite token. If the caveat is present, the consumer must prove their identity by sending their [identity token](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[identity-tokens].html) in the &#x60;x-onedata-consumer-token header&#x60; along with the request. The consumers must be encoded using proper [consumer format](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[consumer].html).  You can learn more about token caveats [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[token-caveats].html).  | [optional] 
**whitelist** | **list[str]** | List of consumers that are allowed to utilize the token.  Example: &#x60;&#x60;&#x60;json   {     \&quot;type\&quot;: \&quot;consumer\&quot;,     \&quot;whitelist\&quot;: [       \&quot;usr-d4f5876dbe7f1e7e8a511de6dd31144c\&quot;,       \&quot;grp-0921135ee61fe53a3df449365228e9b4\&quot;,       \&quot;prv-*\&quot;     ]   } &#x60;&#x60;&#x60;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

