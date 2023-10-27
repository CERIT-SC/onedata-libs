# Interface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Interface caveat - limits the available interfaces on which the token can be used to a certain one.  If the *oneclient* interface is specified, this caveat is treated as a **data access caveat** - if added to a token, it greatly limits its power in the system APIs, to the minimum required for data access - [see more](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[data-access-caveats].html).  You can learn more about token caveats [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[token-caveats].html).  | [optional] 
**interface** | **str** | The interface on which this token will be exclusively accepted.  Example: &#x60;&#x60;&#x60;json   {     \&quot;type\&quot;: \&quot;interface\&quot;,     \&quot;interface\&quot;: \&quot;rest\&quot;   } &#x60;&#x60;&#x60;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

