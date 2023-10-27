# AtmWorkflowExecutionLaneRunDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_number** | **int** | Number of workflow execution run in which this lane run is included.  When prepared in advance, this value is &#x60;null&#x60;, as the specific number  is not yet known.  | 
**origin_run_number** | **int** | Number of workflow execution lane run on which this lane run is based  in case of repeat (either rerun or retry) or &#x60;null&#x60; otherwise.  | 
**run_type** | **str** | Type of lane run. | 
**status** | **str** | Overall status of the lane run. | 
**iterated_store_id** | **str** | Id of this lane run iterated store. | 
**exception_store_id** | **str** | Id of this lane run exception store. | 
**parallel_boxes** | [**list[AtmWorkflowExecutionLaneRunDetailsParallelBoxes]**](AtmWorkflowExecutionLaneRunDetailsParallelBoxes.md) | Details of parallel boxes in this lane run. | 
**is_retriable** | **bool** | Indicates whether this lane execution run can be retried or not. | 
**is_rerunable** | **bool** | Indicates whether this lane execution run can be rerun or not. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

