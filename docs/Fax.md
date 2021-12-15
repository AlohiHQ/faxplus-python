# faxplus.Fax


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Free-form comment | 
**cost** | **int** | Fax cost in the user currency | [optional] 
**cost_details** | [**FaxCostDetails**](FaxCostDetails.md) |  | 
**description** | **str** |  | [optional] 
**direction** | [**FaxDirection**](FaxDirection.md) |  | [optional] 
**duration** | **int** |  | [optional] 
**file** | **str** | Fax file ID for the getFile handle | [optional] 
**file_name** | **str** | Human-readable file name | [optional] 
**from_number** | **str** | Sender number. Might be a userId for faxes sent or received with free accounts | [optional] 
**header** | **str** |  | [optional] 
**id** | **str** | Fax ID | 
**is_read** | **bool** |  | [optional] 
**is_spam** | **bool** | True if the fax is marked as spam | [optional] 
**last_update** | **str** |  | [optional] 
**max_retry** | **int** | Maximum number of retries | [optional] 
**owner_id** | **str** | User ID of the fax owner | 
**pages** | **int** | Number of pages in the fax | 
**retry_delay** | **int** | Delay between two retries | [optional] 
**scheduled_time** | **str** |  | [optional] 
**start_time** | **str** | Time at which faxing session started. Format: YYYY-MM-DD HH:mm:ss | [optional] 
**status** | [**FaxStatus**](FaxStatus.md) |  | 
**submit_time** | **str** | Time when the fax was submitted for sending. For outgoing faxes only | [optional] 
**to** | **str** | Fax destination number. Might be a userId for faxes sent or received with free accounts | [optional] 
**cover_page** | [**FaxCoverPage**](FaxCoverPage.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

