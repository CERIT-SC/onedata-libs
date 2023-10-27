# S3Modify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of storage.  &#x60;type &#x3D; \&quot;s3\&quot;&#x60;  [Amazon S3](http://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) compatible storage.  | 
**hostname** | **str** | The hostname of a machine where S3 storage is installed. | [optional] 
**bucket_name** | **str** | The storage bucket name. | [optional] 
**access_key** | **str** | The access key to the S3 storage. | [optional] 
**secret_key** | **str** | The secret key to the S3 storage. | [optional] 
**signature_version** | **int** | The version of signature used to sign requests. Only version 4 is supported.  | [optional] 
**maximum_canonical_object_size** | **int** | Defines the maximum size for objects, which can be modified on the S3 storage in &#x60;canonical&#x60; path mode. In this mode, entire file needs to be downloaded to memory, modified and uploaded back, which is impractical for large files (default 64 MiB).  | [optional] 
**file_mode** | **str** | Defines the file permissions, which files imported from S3 storage will have in Onedata. Values should be provided in octal format e.g. &#x60;0644&#x60;.  | [optional] 
**dir_mode** | **str** | Defines the directory mode which directories imported from S3 storage will have in Onedata. Values should be provided in octal format e.g. &#x60;0775&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

