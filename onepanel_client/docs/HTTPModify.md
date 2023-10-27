# HTTPModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of storage.  &#x60;type &#x3D; \&quot;http\&quot;&#x60;  Any [HTTP](https://tools.ietf.org/html/rfc7231) or HTTPS compatible server. Supported only with Readonly option enabled and in manual import mode.  | 
**endpoint** | **str** | Full URL of the HTTP server, including scheme (http or https) and path.  | [optional] 
**verify_server_certificate** | **bool** | Determines whether Oneprovider should verify the certificate of the HTTP server.  | [optional] 
**credentials_type** | **str** | Determines the types of credentials provided in the credentials field.  | [optional] 
**credentials** | **str** | The credentials to authenticate with the HTTP server. &#x60;basic&#x60; credentials should be provided in the form &#x60;username:password&#x60;, for &#x60;token&#x60; just the token. For &#x60;none&#x60; this field is ignored.  | [optional] 
**authorization_header** | **str** | The authorization header to be used for passing the access token. This field can contain any prefix that should be added to the header value. Default is &#x60;Authorization: Bearer {}&#x60;. The token will placed where &#x60;{}&#x60; is provided.  | [optional] 
**connection_pool_size** | **int** | Defines the maximum number of parallel connections for a single HTTP storage.  | [optional] 
**max_requests_per_session** | **int** | Defines the maximum number of requests performed in a single HTTP session. After the limit is reached, &#x27;Connection: close&#x27; header is sent to the server. When set to 0 (default), number of requests per session is unlimited, unless imposed by the server.  | [optional] 
**file_mode** | **str** | Defines the file permissions, which files imported from HTTP storage will have in Onedata. Values should be provided in octal format e.g. &#x60;0664&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

