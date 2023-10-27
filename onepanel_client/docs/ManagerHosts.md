# ManagerHosts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**main_host** | **str** | The main cluster manager host. Main cluster manager node is responsible for monitoring cluster worker nodes. Other nodes, which are redundant, are suspended. In case of main cluster manager node failure one of redundant nodes is resumed and takes over main node responsibilities.  | 
**hosts** | **list[str]** | The list of service hosts. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

