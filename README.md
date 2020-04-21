# faxplus-api
This is the FAX.PLUS API v1 developed for third party developers and organizations. In order to have a better coding experience with this API, let's quickly go through some points:<br /><br /> - This API assumes **/accounts** as an entry point with the base url of **https://restapi.fax.plus/v1**. <br /><br /> - This API treats all date and times sent to it in requests as **UTC**. Also, all dates and times returned in responses are in **UTC**<br /><br /> - Once you have an access_token, you can easily send a request to the resource server with the base url of **https://restapi.fax.plus/v1** to access your permitted resources. As an example to get the user's profile info you would send a request to **https://restapi.fax.plus/v1/accounts/self** when **Authorization** header is set to **Bearer YOUR_ACCESS_TOKEN** and custom header of **x-fax-clientid** is set to YOUR_CLIENT_ID

Note: this API is available to Enterprise clients only.

## Requirements.

Python 3.5+

## Installation & Usage
### pip install

To install the package from PyPi

```sh
pip install faxplus-api
```

Alternatively, you can install it directly from Github

```sh
pip install git+https://github.com/alohi/faxplus-python.git
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
git clone https://github.com/alohi/faxplus-python.git
cd faxplus-python
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

## Getting Started

After [installing the library](#installation--usage), setting up your API access, and obtaining the token,
you can try running the following code snippet:

```python
import faxplus
from faxplus.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: fax_oauth
configuration = faxplus.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_client = faxplus.ApiClient(configuration)
api_client.set_default_header('x-fax-clientid', 'YOUR_CLIENT_ID')
api_instance = faxplus.AccountsApi(api_client)

try:
    # Get account information of all non-admin members of your corporate account.
    api_response = api_instance.get_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_accounts: %s\n" % e)
```

For more examples, see our sample Flask app at <https://github.com/alohi/faxplus-sample-python>

## Documentation

The API reference can be found on our website at <https://apidoc.fax.plus>

### Documentation for API Endpoints

All URIs are relative to *https://restapi.fax.plus/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**get_accounts**](docs/AccountsApi.md#get_accounts) | **GET** /accounts | Get account information of all non-admin members of your corporate account.
*AccountsApi* | [**get_member_details**](docs/AccountsApi.md#get_member_details) | **GET** /accounts/self/member-details/{member_user_id} | Get member details
*AccountsApi* | [**get_user**](docs/AccountsApi.md#get_user) | **GET** /accounts/{user_id} | Get account information for admin or member
*AccountsApi* | [**update_member_details**](docs/AccountsApi.md#update_member_details) | **PUT** /accounts/self/member-details/{member_user_id} | Modify member details
*AccountsApi* | [**update_user**](docs/AccountsApi.md#update_user) | **PUT** /accounts/self | Modify account information
*ArchivesApi* | [**delete_fax**](docs/ArchivesApi.md#delete_fax) | **DELETE** /accounts/self/archives/{fax_id} | Delete a fax
*ArchivesApi* | [**get_fax**](docs/ArchivesApi.md#get_fax) | **GET** /accounts/self/archives/{fax_id} | Get a fax record
*ArchivesApi* | [**list_faxes**](docs/ArchivesApi.md#list_faxes) | **GET** /accounts/{user_id}/archives | Get fax records
*ArchivesApi* | [**update_fax**](docs/ArchivesApi.md#update_fax) | **PUT** /accounts/self/archives/{fax_id} | Modify fax record
*FilesApi* | [**get_file**](docs/FilesApi.md#get_file) | **GET** /accounts/self/files/{fax_id} | get a file
*FilesApi* | [**upload_file**](docs/FilesApi.md#upload_file) | **POST** /accounts/self/files | upload a file
*NumbersApi* | [**get_number**](docs/NumbersApi.md#get_number) | **GET** /accounts/self/numbers/{number} | Get number information
*NumbersApi* | [**list_numbers**](docs/NumbersApi.md#list_numbers) | **GET** /accounts/self/numbers | Get your numbers
*NumbersApi* | [**revoke_number**](docs/NumbersApi.md#revoke_number) | **DELETE** /accounts/{user_id}/numbers/{number} | Revoke number
*NumbersApi* | [**update_number**](docs/NumbersApi.md#update_number) | **PUT** /accounts/self/numbers/{number} | Assign number
*OutboxApi* | [**delete_outbox_fax**](docs/OutboxApi.md#delete_outbox_fax) | **DELETE** /accounts/self/outbox/{outbox_fax_id} | Delete a fax from outbox
*OutboxApi* | [**get_outbox_fax**](docs/OutboxApi.md#get_outbox_fax) | **GET** /accounts/self/outbox/{outbox_fax_id} | Get an outbox record
*OutboxApi* | [**list_outbox_faxes**](docs/OutboxApi.md#list_outbox_faxes) | **GET** /accounts/self/outbox | Get list of faxes in the outbox
*OutboxApi* | [**send_fax**](docs/OutboxApi.md#send_fax) | **POST** /accounts/self/outbox | Send a fax
*OutboxApi* | [**update_outbox_fax**](docs/OutboxApi.md#update_outbox_fax) | **PUT** /accounts/self/outbox/{outbox_fax_id} | Modify a fax record in outbox

### Documentation For Models

 - [Account](docs/Account.md)
 - [AccountData](docs/AccountData.md)
 - [AccountList](docs/AccountList.md)
 - [AccountNotifications](docs/AccountNotifications.md)
 - [AccountNotificationsBlacklist](docs/AccountNotificationsBlacklist.md)
 - [AccountNotificationsEmailSettings](docs/AccountNotificationsEmailSettings.md)
 - [AccountNotificationsEmailSettingsAttachments](docs/AccountNotificationsEmailSettingsAttachments.md)
 - [AccountNotificationsLanguage](docs/AccountNotificationsLanguage.md)
 - [AccountNotificationsPushSettings](docs/AccountNotificationsPushSettings.md)
 - [AccountNotificationsSettings](docs/AccountNotificationsSettings.md)
 - [AccountNotificationsSlackSettings](docs/AccountNotificationsSlackSettings.md)
 - [AccountNotificationsSmsSettings](docs/AccountNotificationsSmsSettings.md)
 - [AccountSettings](docs/AccountSettings.md)
 - [AccountSettingsSendFax](docs/AccountSettingsSendFax.md)
 - [AccountStatus](docs/AccountStatus.md)
 - [AccountType](docs/AccountType.md)
 - [Binary](docs/Binary.md)
 - [Error](docs/Error.md)
 - [Fax](docs/Fax.md)
 - [FaxCategory](docs/FaxCategory.md)
 - [FaxCostDetails](docs/FaxCostDetails.md)
 - [FaxDirection](docs/FaxDirection.md)
 - [FaxList](docs/FaxList.md)
 - [FaxListData](docs/FaxListData.md)
 - [FaxStatus](docs/FaxStatus.md)
 - [File](docs/File.md)
 - [FilePath](docs/FilePath.md)
 - [FileType](docs/FileType.md)
 - [MemberDetail](docs/MemberDetail.md)
 - [Number](docs/Number.md)
 - [NumberList](docs/NumberList.md)
 - [NumberNotifications](docs/NumberNotifications.md)
 - [NumberStatus](docs/NumberStatus.md)
 - [Outbox](docs/Outbox.md)
 - [OutboxComment](docs/OutboxComment.md)
 - [OutboxFileChanges](docs/OutboxFileChanges.md)
 - [OutboxFiles](docs/OutboxFiles.md)
 - [OutboxInitiatedFrom](docs/OutboxInitiatedFrom.md)
 - [OutboxList](docs/OutboxList.md)
 - [OutboxStatus](docs/OutboxStatus.md)
 - [OutboxStatusChanges](docs/OutboxStatusChanges.md)
 - [PayloadAccountModification](docs/PayloadAccountModification.md)
 - [PayloadFaxModification](docs/PayloadFaxModification.md)
 - [PayloadNumberModification](docs/PayloadNumberModification.md)
 - [PayloadOutbox](docs/PayloadOutbox.md)
 - [PayloadOutboxComment](docs/PayloadOutboxComment.md)
 - [PayloadOutboxModification](docs/PayloadOutboxModification.md)
 - [PayloadOutboxOptions](docs/PayloadOutboxOptions.md)
 - [RetryOptions](docs/RetryOptions.md)
 - [SlackNotificationMode](docs/SlackNotificationMode.md)

## Author

© 2020 Alohi SA (Geneva, Switzerland)

https://www.alohi.com
