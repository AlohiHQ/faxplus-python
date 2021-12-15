# faxplus.Outbox
Model for the outbound fax stored in the outbox

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | [**OutboxComment**](OutboxComment.md) |  | [optional] 
**contact_name** | **str** |  | [optional] 
**designated_src** | **str** |  | [optional] 
**extra_info** | **object** |  | [optional] 
**file_changes** | [**list[OutboxFileChanges]**](OutboxFileChanges.md) |  | [optional] 
**files** | **list[str]** | Files to send | [optional] 
**id** | **str** | Fax ID | 
**initiated_from** | [**OutboxInitiatedFrom**](OutboxInitiatedFrom.md) |  | [optional] 
**ip** | **str** | IP address from which the send request originated | [optional] 
**last_updated_status_time** | **str** | Time and date when the send request status was last updated. Format: *YYYY-MM-DD HH:mm:ss* | [optional] 
**options** | [**OutboxOptions**](OutboxOptions.md) |  | [optional] 
**page_count** | **int** | Number of fax pages | [optional] 
**retry** | [**RetryOptions**](RetryOptions.md) |  | [optional] 
**send_time** | **str** |  | [optional] 
**should_enhance** | **bool** |  | [optional] 
**src** | **str** |  | [optional] 
**status** | [**OutboxStatus**](OutboxStatus.md) |  | 
**status_changes** | [**list[OutboxStatusChanges]**](OutboxStatusChanges.md) |  | [optional] 
**submit_time** | **str** | Date and time when the fax was submitted for sending | [optional] 
**to** | **list[str]** |  | [optional] 
**uid** | **str** | User ID | 
**cover_page** | [**OutboxCoverPage**](OutboxCoverPage.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

