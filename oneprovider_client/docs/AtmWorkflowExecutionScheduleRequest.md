# AtmWorkflowExecutionScheduleRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**space_id** | **str** | Id of the space in context of which the workflow will be executed.  | 
**atm_workflow_schema_id** | **str** | Id of the workflow schema. | 
**atm_workflow_schema_revision_number** | **str** | Number of workflow schema revision describing the tasks and stores for  the workflow.  | 
**store_initial_content_overlay** | **dict(str, object)** | Map with store schema Ids (keys) and corresponding initial content  of the stores.  | [optional] 
**log_level** | **str** | Level controling the amount of information recorded in audit logs as only logs with severity equal or higher to this level will be stored.   | [optional] [default to 'info']
**callback** | **str** | Custom REST callback URL which will be called when the workflow execution ends - a http &#x60;POST&#x60; request with workflow execution Id and status in body.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

