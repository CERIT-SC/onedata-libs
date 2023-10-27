# GeoRegion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GEO Region caveat - limits the geographical regions from which the token can be utilized. The available values are the 7 continents (Oceania covers Australia and the pacific islands) or the EU meta region, which matches member countries of the European Union. The client&#x27;s region is resolved based on client&#x27;s IP and MaxMind&#x27;s GeoLite database.  You can learn more about token caveats [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[token-caveats].html).  | [optional] 
**filter** | **str** | Filter type to be applied: * whitelist limits allowed regions to the ones on the list only * blacklist limits allowed regions to any region that is not on the list  | [optional] 
**list** | **list[str]** | List of regions from which the token can be utilized.  Example: &#x60;&#x60;&#x60;json   {     \&quot;type\&quot;: \&quot;geo.region\&quot;,     \&quot;filter\&quot;: \&quot;blacklist\&quot;,     \&quot;list\&quot;: [       \&quot;Asia\&quot;,       \&quot;NorthAmerica\&quot;,       \&quot;Oceania\&quot;     ]   } &#x60;&#x60;&#x60;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

