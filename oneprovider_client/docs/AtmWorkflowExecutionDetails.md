# AtmWorkflowExecutionDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**atm_workflow_execution_id** | **str** | Id of this workflow execution. | 
**atm_workflow_schema_snapshot_id** | **str** | Id of the snapshot of the workflow schema describing the tasks and stores for this workflow.  | 
**name** | **str** | Name of the workflow schema used for this execution. | 
**atm_inventory_id** | **str** | Id of automation inventory from which the workflow schema originates. | 
**space_id** | **str** | Id of the space in context of which the workflow was executed. | 
**user_id** | **str** | Id of the scheduling user. | 
**status** | **str** | Overall status of the workflow execution. | 
**schedule_time** | **int** | Schedule time in seconds (POSIX epoch timestamp). | 
**start_time** | **int** | Start time in seconds (POSIX epoch timestamp). | 
**suspend_time** | **int** | Suspend time in seconds (POSIX epoch timestamp). | 
**finish_time** | **int** | Finish time in seconds (POSIX epoch timestamp). | 
**lambda_snapshot_registry** | **dict(str, str)** | Map with lambda Ids (keys) and corresponding snapshot Ids. | 
**store_registry** | **dict(str, str)** | Map with store schema Ids (keys) and corresponding store instance Ids.  | 
**system_audit_log_store_id** | **str** | Id of this execution system audit log store. | 
**lanes** | [**list[AtmWorkflowExecutionDetailsLanes]**](AtmWorkflowExecutionDetailsLanes.md) | Details of lanes in this workflow execution. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

