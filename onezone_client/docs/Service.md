# Service

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Service caveat - limits the services that can process the token. [Service](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[service].html) is the Onedata service that received the client&#x27;s request - e.g. the Oneprovider service chosen by a user to mount a Oneclient or make a CDMI request. If the caveat is present, the service must prove its identity by sending their [identity token](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[identity-tokens].html) in the &#x60;x-onedata-service-token header&#x60; along with the request. The services must be encoded using proper [service format](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[service].html).  You can learn more about token caveats [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[token-caveats].html).  | [optional] 
**whitelist** | **list[str]** | List of services that are allowed to utilize the token.  Example: &#x60;&#x60;&#x60;json   {     \&quot;type\&quot;: \&quot;service\&quot;,     \&quot;whitelist\&quot;: [       \&quot;ozw-onezone\&quot;,       \&quot;ozp-onezone\&quot;,       \&quot;opp-*\&quot;,       \&quot;opw-01c4455bef059353c9dfb35ba93a24f3\&quot;     ]   } &#x60;&#x60;&#x60;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

