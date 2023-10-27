# GeoCountry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GEO Country caveat - limits the countries from which the token can be utilized. The client&#x27;s country is resolved based on client&#x27;s IP and MaxMind&#x27;s GeoLite database.  You can learn more about token caveats [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[token-caveats].html).  | [optional] 
**filter** | **str** | Filter type to be applied: * whitelist limits allowed countries to the ones on the list only * blacklist limits allowed countries to any region that is not on the list  | [optional] 
**list** | **list[str]** | List of countries (ISO3166 2 letter codes) from which the token can be utilized.  Example: &#x60;&#x60;&#x60;json   {     \&quot;type\&quot;: \&quot;geo.country\&quot;,     \&quot;filter\&quot;: \&quot;whitelist\&quot;,     \&quot;list\&quot;: [       \&quot;PL\&quot;, \&quot;UK\&quot;, \&quot;DE\&quot;, \&quot;NL\&quot;     ]   } &#x60;&#x60;&#x60;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

