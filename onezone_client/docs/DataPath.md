# DataPath

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Data path caveat - limits the paths in which data can be accessed with the token. The paths must be canonical - starting with a slash + space id and without a trailing slash - and must be base64 encoded. If a directory path is given, the token allows to access all nested files and directories starting from the specified directory.  This is a **data access caveat** - if added to a token, it greatly limits its power in the system APIs, to the minimum required for data access - [see more](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[data-access-caveats].html).  You can learn more about token caveats [here](https://onedata.org/#/home/documentation/doc/using_onedata/tokens[token-caveats].html).  | [optional] 
**whitelist** | **list[str]** | List of base64 encoded file paths in which data can be accessed using the token.  Example: &#x60;&#x60;&#x60;json   {     \&quot;type\&quot;: \&quot;data.path\&quot;,     \&quot;whitelist\&quot;: [       \&quot;L2QxYjM4OGY3Yzc&#x3D;\&quot;,   # /d1b388f7c7       \&quot;L2QxYjM4OGY3YzcvZGlyL2ZpbGUudHh0\&quot;    # /d1b388f7c7/dir/file.txt     ]   } &#x60;&#x60;&#x60;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

