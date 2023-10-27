# ZoneConfigurationOnezone

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | The domain of Onezone cluster. | 
**name** | **str** | The Onezone cluster name. | 
**lets_encrypt_enabled** | **bool** | If enabled the zone will use Let&#x27;s Encrypt service to obtain SSL certificates. Otherwise certificates must be manually provided. By enabling this option you agree to the Let&#x27;s Encrypt Subscriber Agreement.  | [optional] [default to False]
**built_in_dns_server** | **bool** | If true, DNS check will verify that control of DNS zone for Onezone&#x27;s domain was delegated to the DNS server built into Onezone service.  | [optional] 
**policies** | [**ZonePolicies**](ZonePolicies.md) |  | [optional] 
**users** | [**list[OnezoneUserCreateRequest]**](OnezoneUserCreateRequest.md) | List of Onezone user specifications. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

