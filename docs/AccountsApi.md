# faxplus.AccountsApi

All URIs are relative to *https://restapi.fax.plus/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accounts**](AccountsApi.md#get_accounts) | **GET** /accounts | List corporate members
[**get_member_details**](AccountsApi.md#get_member_details) | **GET** /accounts/self/member-details/{member_user_id} | Get member details
[**get_user**](AccountsApi.md#get_user) | **GET** /accounts/{user_id} | Get account information
[**update_member_details**](AccountsApi.md#update_member_details) | **PUT** /accounts/self/member-details/{member_user_id} | Modify member details
[**update_user**](AccountsApi.md#update_user) | **PUT** /accounts/{user_id} | Modify account information

# **get_accounts**
> AccountList get_accounts()

List corporate members

Get account information of all non-admin members of your corporate account. Only the admin account can send a request to this endpoint which returns the accounts of all members

### Example
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
    # List corporate members
    api_response = api_instance.get_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountList**](AccountList.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_member_details**
> MemberDetail get_member_details(member_user_id)

Get member details

Get corporate member's role and faxing quota

### Example
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
member_user_id = 'member_user_id_example' # str | Member user ID

try:
    # Get member details
    api_response = api_instance.get_member_details(member_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_member_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_user_id** | **str**| Member user ID | 

### Return type

[**MemberDetail**](MemberDetail.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> Account get_user(user_id)

Get account information

Get information about an account. For members user_id can only be self. For admin it can be either self, or a user_id of any corporate member

### Example
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
user_id = 'user_id_example' # str | User ID to get information about. For your own account use **'self'**

try:
    # Get account information
    api_response = api_instance.get_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID to get information about. For your own account use **&#x27;self&#x27;** | 

### Return type

[**Account**](Account.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_member_details**
> update_member_details(member_user_id, body=body)

Modify member details

Update corporate member's role and faxing quota

### Example
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
member_user_id = 'member_user_id_example' # str | Member user ID
body = faxplus.MemberDetail() # MemberDetail | Request object for making changes in member details (optional)

try:
    # Modify member details
    api_instance.update_member_details(member_user_id, body=body)
except ApiException as e:
    print("Exception when calling AccountsApi->update_member_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_user_id** | **str**| Member user ID | 
 **body** | [**MemberDetail**](MemberDetail.md)| Request object for making changes in member details | [optional] 

### Return type

void (empty response body)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> update_user(user_id, body=body)

Modify account information

Modify personal information of your own account or your corporate member's account. user_id can be either self, or a subordinate's user_id

### Example
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
user_id = 'user_id_example' # str | User ID to get information about. For your own account use **'self'**
body = faxplus.PayloadAccountModification() # PayloadAccountModification | Request object for making changes in account (optional)

try:
    # Modify account information
    api_instance.update_user(user_id, body=body)
except ApiException as e:
    print("Exception when calling AccountsApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID to get information about. For your own account use **&#x27;self&#x27;** | 
 **body** | [**PayloadAccountModification**](PayloadAccountModification.md)| Request object for making changes in account | [optional] 

### Return type

void (empty response body)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

