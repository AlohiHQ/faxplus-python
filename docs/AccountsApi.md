# faxplus.AccountsApi

All URIs are relative to *https://restapi.fax.plus/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accounts**](AccountsApi.md#get_accounts) | **GET** /accounts | Get account information of all members of your corporate account
[**get_member_details**](AccountsApi.md#get_member_details) | **GET** /accounts/self/member-details/{member_id} | Get member details
[**get_user**](AccountsApi.md#get_user) | **GET** /accounts/{user_id} | Get account information for admin or member
[**update_member_details**](AccountsApi.md#update_member_details) | **PUT** /accounts/self/member-details/{member_id} | Modify member details
[**update_user**](AccountsApi.md#update_user) | **PUT** /accounts/self | Modify account information


# **get_accounts**
> ResponseAccountList get_accounts()

Get account information of all members of your corporate account

Only admin account can send request to this endpoint which returns accounts of all members

### Example
```python
from __future__ import print_function
import time
import faxplus
from faxplus.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: fax_oauth
configuration = faxplus.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = faxplus.AccountsApi(faxplus.ApiClient(configuration))

try:
    # Get account information of all members of your corporate account
    api_response = api_instance.get_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseAccountList**](ResponseAccountList.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_member_details**
> MemberDetail get_member_details(member_id)

Get member details

Get your member details (quota and role)

### Example
```python
from __future__ import print_function
import time
import faxplus
from faxplus.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: fax_oauth
configuration = faxplus.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = faxplus.AccountsApi(faxplus.ApiClient(configuration))
member_id = 'member_id_example' # str | 

try:
    # Get member details
    api_response = api_instance.get_member_details(member_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_member_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | 

### Return type

[**MemberDetail**](MemberDetail.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> Account get_user(user_id)

Get account information for admin or member

Get account information. For members user_id can only be self. form admin it can be user_id of any <br />**In case you want to get your own account information please use *`self`* as an alias for your user_id.**

### Example
```python
from __future__ import print_function
import time
import faxplus
from faxplus.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: fax_oauth
configuration = faxplus.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = faxplus.AccountsApi(faxplus.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    # Get account information for admin or member
    api_response = api_instance.get_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**Account**](Account.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_member_details**
> update_member_details(member_id, payload_member_detail)

Modify member details

One of the paramters below is needed to modify member information

### Example
```python
from __future__ import print_function
import time
import faxplus
from faxplus.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: fax_oauth
configuration = faxplus.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = faxplus.AccountsApi(faxplus.ApiClient(configuration))
member_id = 'member_id_example' # str | 
payload_member_detail = faxplus.MemberDetail() # MemberDetail | 

try:
    # Modify member details
    api_instance.update_member_details(member_id, payload_member_detail)
except ApiException as e:
    print("Exception when calling AccountsApi->update_member_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | 
 **payload_member_detail** | [**MemberDetail**](MemberDetail.md)|  | 

### Return type

void (empty response body)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> update_user(user_id, payload_account)

Modify account information

You can only modify your account

### Example
```python
from __future__ import print_function
import time
import faxplus
from faxplus.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: fax_oauth
configuration = faxplus.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = faxplus.AccountsApi(faxplus.ApiClient(configuration))
user_id = 'user_id_example' # str | 
payload_account = faxplus.Account() # Account | 

try:
    # Modify account information
    api_instance.update_user(user_id, payload_account)
except ApiException as e:
    print("Exception when calling AccountsApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **payload_account** | [**Account**](Account.md)|  | 

### Return type

void (empty response body)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

