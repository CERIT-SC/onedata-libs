# Webdav

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the storage. Must be given explicitly and must match the actual type of subject storage - this redundancy is needed due to limitations of OpenAPI polymorphism.  | 
**timeout** | **int** | Storage operation timeout in milliseconds. | [optional] 
**skip_storage_detection** | **bool** | If true, detecting whether storage is directly accessible by the Oneclient will not be performed. This option should be set to true on readonly storages.  | [optional] [default to False]
**luma_feed** | **str** | Type of feed for LUMA DB. Feed is a source of user/group mappings used to populate the LUMA DB. For more info please read: https://onedata.org/#/home/documentation/doc/administering_onedata/luma.html  | [optional] [default to 'auto']
**luma_feed_url** | **str** | URL of external feed for LUMA DB. Relevant only if lumaFeed equals &#x60;external&#x60;. | [optional] 
**luma_feed_api_key** | **str** | API key checked by external service used as feed for LUMA DB. Relevant only if lumaFeed equals &#x60;external&#x60;.  | [optional] 
**qos_parameters** | **dict(str, str)** | Map with key-value pairs used for describing storage QoS parameters. | [optional] 
**imported_storage** | **bool** | Defines whether storage contains existing data to be imported.  | [optional] [default to False]
**archive_storage** | **bool** | Defines whether storage supports long-term dataset archiving.  | [optional] [default to False]
**readonly** | **bool** | Defines whether the storage is readonly. If enabled, Oneprovider will block any operation that writes, modifies or deletes data on the storage. Such storage can only be used to import data into the space. Mandatory to ensure proper behaviour if the backend storage is actually configured as readonly. This option is available only for imported storages.  | [optional] [default to False]
**credentials_type** | **str** | Determines the types of credentials provided in the credentials field.  | [optional] [default to 'none']
**credentials** | **str** | The credentials to authenticate with the WebDAV server. &#x60;basic&#x60; credentials should be provided in the form &#x60;username:password&#x60;, for &#x60;token&#x60; just the token. In case of &#x60;oauth2&#x60;, this field should contain the username for the WebDAV, while the token will be obtained and refreshed automatically in the background. For &#x60;none&#x60; this field is ignored.  | [optional] 
**oauth2_id_p** | **str** | In case &#x60;oauth2&#x60; credential type is selected and Onezone is configured with support for multiple external IdP&#x27;s, this field must contain the name of the IdP which authenticates requests to the WebDAV endpoint. If Onezone has only one external IdP, it will be selected automatically.  | [optional] 
**onedata_access_token** | **str** | When registering storage with feed of LUMA DB set to&#x60;auto&#x60; and with &#x60;oauth2&#x60; external IdP, this field must contain a valid Onedata access token of the user on whose behalf the WebDAV storage will be accessed by all users with access to any space supported by this storage.  | [optional] 
**endpoint** | **str** | Full URL of the WebDAV server, including scheme (http or https) and path.  | 
**verify_server_certificate** | **bool** | Determines whether Oneprovider should verify the certificate of the WebDAV server.  | [optional] [default to True]
**authorization_header** | **str** | The authorization header to be used for passing the access token. This field can contain any prefix that should be added to the header value. Default is &#x60;Authorization: Bearer {}&#x60;. The token will placed where &#x60;{}&#x60; is provided.  | [optional] [default to 'Authorization: Bearer {}']
**range_write_support** | **str** | The type of partial write support enabled in the WebDAV server. Currently 2 types are supported &#x60;sabredav&#x60; which assumes the server supports the SabreDAV PartialUpdate extension via &#x60;PATCH&#x60; method, and &#x60;moddav&#x60; which assumes server supports partial &#x60;PUT&#x60; requests with &#x60;Content-Range&#x60; header. If &#x60;none&#x60; is selected no write support is available for this WebDAV storage.  | [optional] [default to 'none']
**connection_pool_size** | **int** | Defines the maximum number of parallel connections for a single WebDAV storage.  | [optional] 
**maximum_upload_size** | **int** | Defines the maximum upload size for a single &#x60;PUT&#x60; or &#x60;PATCH&#x60; request. If set to 0, assumes that the WebDAV server has no upload limit.  | [optional] 
**file_mode** | **str** | Defines the file permissions, which files imported from WebDAV storage will have in Onedata. Values should be provided in octal format e.g. &#x60;0644&#x60;.  | [optional] [default to '0664']
**dir_mode** | **str** | Defines the directory mode which directories imported from WebDAV storage will have in Onedata. Values should be provided in octal format e.g. &#x60;0775&#x60;.  | [optional] [default to '0775']
**storage_path_type** | **str** | Determines how the logical file paths will be mapped on the storage. &#x27;canonical&#x27; paths reflect the logical file names and directory structure, however each rename operation will require renaming the files on the storage. &#x27;flat&#x27; paths are based on unique file UUID&#x27;s and do not require on-storage rename when logical file name is changed. **Note that &#x27;flat&#x27; paths are not allowed on this type of storage.**  | [optional] [default to 'canonical']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

