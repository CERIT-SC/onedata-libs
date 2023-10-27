# Space

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**space_id** | **str** | Unique Id of the space. | 
**name** | **str** | The name of the space. | 
**description** | [**SpaceDescription**](SpaceDescription.md) |  | 
**organization_name** | [**SpaceOrganizationName**](SpaceOrganizationName.md) |  | 
**tags** | [**SpaceTags**](SpaceTags.md) |  | 
**advertised_in_marketplace** | [**SpaceAdvertisedInMarketplace**](SpaceAdvertisedInMarketplace.md) |  | 
**marketplace_contact_email** | [**SpaceMarketplaceContactEmail**](SpaceMarketplaceContactEmail.md) |  | 
**providers** | **dict(str, int)** | A map of provider Ids supporting this space and corresponding size of provisioned storage in bytes.  | 
**support_parameters_registry** | [**dict(str, SupportParameters)**](SupportParameters.md) | A map of provider Ids supporting this space and corresponding support parameters of the provider.  | 
**creator** | [**Subject**](Subject.md) |  | 
**creation_time** | [**Timestamp**](Timestamp.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

