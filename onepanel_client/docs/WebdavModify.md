# WebdavModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of storage.  &#x60;type &#x3D; \&quot;webdav\&quot;&#x60;  Storage backend compatible with [WebDAV](https://tools.ietf.org/html/rfc4918) protocol.  | 
**endpoint** | **str** | Full URL of the WebDAV server, including scheme (http or https) and path.  | [optional] 
**verify_server_certificate** | **bool** | Determines whether Oneprovider should verify the certificate of the WebDAV server.  | [optional] 
**credentials_type** | **str** | Determines the types of credentials provided in the credentials field.  | [optional] 
**credentials** | **str** | The credentials to authenticate with the WebDAV server. &#x60;basic&#x60; credentials should be provided in the form &#x60;username:password&#x60;, for &#x60;token&#x60; just the token. For &#x60;none&#x60; this field is ignored.  | [optional] 
**authorization_header** | **str** | The authorization header to be used for passing the access token. This field can contain any prefix that should be added to the header value. Default is &#x60;Authorization: Bearer {}&#x60;. The token will placed where &#x60;{}&#x60; is provided.  | [optional] 
**range_write_support** | **str** | The type of partial write support enabled in the WebDAV server. Currently 2 types are supported &#x60;sabredav&#x60; which assumes the server supports the SabreDAV PartialUpdate extension via &#x60;PATCH&#x60; method, and &#x60;moddav&#x60; which assumes server supports partial &#x60;PUT&#x60; requests with &#x60;Content-Range&#x60; header. If &#x60;none&#x60; is selected no write support is available for this WebDAV storage.  | [optional] 
**connection_pool_size** | **int** | Defines the maximum number of parallel connections for a single WebDAV storage.  | [optional] 
**maximum_upload_size** | **int** | Defines the maximum upload size for a single &#x60;PUT&#x60; or &#x60;PATCH&#x60; request. If set to 0, assumes that the WebDAV server has no upload limit.  | [optional] 
**file_mode** | **str** | Defines the file permissions, which files imported from WebDAV storage will have in Onedata. Values should be provided in octal format e.g. &#x60;0644&#x60;.  | [optional] 
**dir_mode** | **str** | Defines the directory mode which directories imported from WebDAV storage will have in Onedata. Values should be provided in octal format e.g. &#x60;0775&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

