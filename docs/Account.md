# faxplus.Account
User account model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_data** | [**AccountData**](AccountData.md) |  | [optional] 
**account_type** | [**AccountType**](AccountType.md) |  | 
**creation_date** | **str** | Creation date in UTC. Format: *YYYY-MM-DD HH:mm:ss* | 
**email** | **str** | Account email address | 
**last_password_modification_date** | **str** | The date on which you have changed your password | [optional] 
**lastname** | **str** | Your last name | [optional] 
**member_of** | **list[str]** | List of user ids that you are member of. | [optional] 
**name** | **str** | Your first name | [optional] 
**notifications** | [**AccountNotifications**](AccountNotifications.md) |  | [optional] 
**phone** | **str** | Your account phone number | [optional] 
**profile_image** | **str** | Profile image path | [optional] 
**settings** | [**AccountSettings**](AccountSettings.md) |  | [optional] 
**status** | [**AccountStatus**](AccountStatus.md) |  | 
**uid** | **str** | User ID of current user | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

