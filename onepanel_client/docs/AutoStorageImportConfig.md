# AutoStorageImportConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_depth** | **int** | Maximum depth of filesystem tree that will be traversed during the scan.  | [optional] 
**sync_acl** | **bool** | Flag that enables synchronization of NFSv4 ACLs.  | [optional] [default to False]
**continuous_scan** | **bool** | With this option enabled the storage will be scanned periodically and direct changes on the storage will be reflected in the assigned Onedata space (upon the consecutive scan).  | [optional] [default to False]
**scan_interval** | **int** | Period between subsequent scans in seconds (counted from end of one scan till beginning of the following). This parameter is relevant only for continuous scans.  | [optional] 
**detect_modifications** | **bool** | Flag determining that modifications of files on the synchronized storage will be detected. If disabled, the storage will be treated as immutable (only creations and deletions of files on storage will be detected). This parameter is relevant only for continuous scans.  | [optional] [default to True]
**detect_deletions** | **bool** | Flag determining that deletions of files from the synchronized storage will be detected. This parameter is relevant only for continuous scans.  | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

