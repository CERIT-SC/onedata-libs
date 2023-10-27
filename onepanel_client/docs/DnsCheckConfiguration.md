# DnsCheckConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_servers** | **list[str]** | A collection of IP addresses for DNS servers used in checking DNS. If empty, local system configuration will be used. | [optional] 
**built_in_dns_server** | **bool** | If true, DNS check will verify that control of DNS zone for Onezone&#x27;s domain was delegated to the DNS server built into Onezone service. This option is available only in Onezone service.  | [optional] 
**dns_check_acknowledged** | **bool** | Flag indicating that user completed the DNS check step during interactive deployment.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

