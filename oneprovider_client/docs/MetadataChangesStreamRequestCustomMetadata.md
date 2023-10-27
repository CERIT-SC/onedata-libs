# MetadataChangesStreamRequestCustomMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**always** | **bool** | Indicates whether specified customMetadata fields should be sent on other metadata changes. | [optional] [default to False]
**fields** | **list[str]** | Xattrs names to retrieve. In case of missing fields &#x60;null&#x60; values are returned. In order to fetch special attributes additional keys can be specified, namely  &#x60;onedata_json&#x60;, &#x60;onedata_rdf&#x60; or &#x60;onedata_keyvalue&#x60; (fetches all fields beside special ones).  | [optional] 
**exists** | **list[str]** | Xattrs names to check for existence. Existence of special attributes can also be checked by specifying &#x60;onedata_json&#x60;, &#x60;onedata_rdf&#x60; or &#x60;onedata_keyvalue&#x60;  (checks if any normal attribute exists).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

