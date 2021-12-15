# faxplus.WebhookCallbackData
Callback data, depends on the event type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Fax session ID. Note that this ID might be different from the one returned by the listFaxes handle, as this ID refers to the faxing session as a whole, with retries included. Both IDs can be used with the API getFile handle | [optional] 
**uid** | **str** | Sender user ID | [optional] 
**pages** | **float** | Number of pages in the fax | [optional] 
**from_number** | **str** | Sender number. Might be a user ID for faxes sent from free accounts | [optional] 
**to_number** | **str** | Fax destination number. Might be a user ID for faxes sent from free accounts | [optional] 
**start_time** | **str** | Time at which faxing session started. Format: YYYY-MM-DD HH:mm:ss | [optional] 
**file** | **str** | File ID | [optional] 
**file_name** | **str** | Human-readable file name | [optional] 
**cost** | **float** | Fax cost (in pages) | [optional] 
**status** | [**FaxStatus**](FaxStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

