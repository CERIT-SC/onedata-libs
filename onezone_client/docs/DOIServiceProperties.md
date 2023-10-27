# DOIServiceProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The service host, including the protocol.  | 
**doi_endpoint** | **str** | DOI registration API endpoint relative to the host.  | 
**metadata_endpoint** | **str** | Metadata registration API endpoint relative to the host.  | 
**media_endpoint** | **str** | Media registration API endpoint relative to the host.  | 
**prefix** | **str** | The DOI prefix under which new DOI&#x27;s can be minted using this account.  | 
**username** | **str** | The username for login to the DOI service.  | 
**password** | **str** | The password for login to the DOI service.  | 
**identifier_template** | **str** | The template for generation of new DOI&#x27;s using this account.  | [optional] 
**allow_template_override** | **bool** | Specifies whether users can override the DOI suffix template for this account during registration of new DOI&#x27;s.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

