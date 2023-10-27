# DataObjectid

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Data objectid caveat - limits the object ids in which data can be accessed with the token. The object ids comply with the CDMI format and can be used in the Oneprovider&#x27;s REST and CDMI APIs. If a directory object id is given, the token allows to access all nested files and directories starting from the specified directory.  This is a **data access caveat** - if added to a token, it greatly limits its power in the system APIs, to the minimum required for data access - [see more](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[data-access-caveats].html).  You can learn more about token caveats [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[token-caveats].html).  | [optional] 
**whitelist** | **list[str]** | List of CDMI ObjectIds in which data can be accessed using the token.  Example: &#x60;&#x60;&#x60;json   {     \&quot;type\&quot;: \&quot;data.objectid\&quot;,     \&quot;whitelist\&quot;: [       \&quot;000000000055D4E4836803640004677569646D000000167\&quot;,       \&quot;39592D594E736C676D0000002B43592D347247454C535F6\&quot;     ]   } &#x60;&#x60;&#x60;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

