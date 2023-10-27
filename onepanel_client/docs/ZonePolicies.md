# ZonePolicies

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oneprovider_registration** | **str** | Indicates policy enforced during provider registration. Possible options are: open - anyone can acquire a registration token and register a new Oneprovider restricted - requires an administrative privilege &#x27;oz_providers_invite&#x27;              to generate a Oneprovider registration token. The token              can be issued for someone else.  | [optional] 
**subdomain_delegation** | **bool** | If true, Oneproviders are allowed to request subdomains of the Onezone domain for use as their domains. | [optional] 
**gui_package_verification** | **bool** | When this value is true, GUI packages uploaded by services operating under Onezone or by harvester admins are checked against known SHA-256 checksums using the compatibility registry. Setting this value to false disables the verification. WARNING: disabling GUI package verification poses a severe security threat, allowing Oneprovider owners to upload arbitrary GUI to Onezone (which is then hosted in Onezone&#x27;s domain).  | [optional] [default to True]
**harvester_gui_package_verification** | **bool** | This policy can be used to disable GUI package verification for harvester plugins only. See \&quot;guiPackageVerification\&quot; for detailed description. This setting has no effect if \&quot;guiPackageVerification\&quot; is set to false.  | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

