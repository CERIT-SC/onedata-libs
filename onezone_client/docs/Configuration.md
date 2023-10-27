# Configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Onezone&#x27;s name | 
**domain** | **str** | Onezone&#x27;s cluster domain | 
**version** | **str** | Version of this Onezone service | 
**build** | **str** | Build number of this Onezone service | 
**subdomain_delegation_supported** | **bool** | If true, registering Oneproviders are allowed to request subdomains of the Onezone domain for use as their domains. | 
**compatible_oneprovider_versions** | **list[str]** | List of compatible Oneprovider versions | 
**compatibility_registry_revision** | **int** | Revision of the compatibility registry enforced by this Onezone service | 
**supported_id_ps** | [**list[ConfigurationSupportedIdPs]**](ConfigurationSupportedIdPs.md) | List of IdPs supported by Onezone | 
**available_space_tags** | **dict(str, list[str])** | A map of tag categories and corresponding available tags for each category.  Space tag is a short keyword or phrase that helps to understand the purpose of a space. Tag categories and available tags are arbitrary strings configured by the Onezone admin.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

