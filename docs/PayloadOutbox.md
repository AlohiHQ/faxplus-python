# faxplus.PayloadOutbox
Model for creating new outbound fax

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_number** | **str** | Number to use for sending the fax | 
**to** | **list[str]** | List of fax destination numbers | 
**files** | **list[str]** | List of file names to send. Files should be uploaded beforehand. | 
**comment** | [**OutboxComment**](OutboxComment.md) |  | [optional] 
**options** | [**OutboxOptions**](OutboxOptions.md) |  | [optional] 
**send_time** | **str** | Date when to send the fax. Format: **YYYY-MM-DD HH:mm:ss +HHMM** | [optional] 
**return_ids** | **bool** | Return scheduled fax IDs to use for tracking and with webhooks | [optional] [default to False]
**cover_page** | [**OutboxCoverPage**](OutboxCoverPage.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

