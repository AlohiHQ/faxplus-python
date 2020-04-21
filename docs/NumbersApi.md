# faxplus.NumbersApi

All URIs are relative to *https://restapi.fax.plus/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_number**](NumbersApi.md#get_number) | **GET** /accounts/self/numbers/{number} | Get number information
[**list_numbers**](NumbersApi.md#list_numbers) | **GET** /accounts/self/numbers | Get your numbers
[**revoke_number**](NumbersApi.md#revoke_number) | **DELETE** /accounts/{user_id}/numbers/{number} | Revoke number
[**update_number**](NumbersApi.md#update_number) | **PUT** /accounts/self/numbers/{number} | Assign number

# **get_number**
> Number get_number(number)

Get number information

Get info of a single number

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
api_instance = faxplus.NumbersApi(api_client)
number = 'number_example' # str | Phone number to get information about

try:
    # Get number information
    api_response = api_instance.get_number(number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumbersApi->get_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| Phone number to get information about | 

### Return type

[**Number**](Number.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_numbers**
> NumberList list_numbers()

Get your numbers

List all your purchased numbers

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
api_instance = faxplus.NumbersApi(api_client)

try:
    # Get your numbers
    api_response = api_instance.list_numbers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumbersApi->list_numbers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NumberList**](NumberList.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_number**
> revoke_number(number, user_id)

Revoke number

Revoke a specific number from a member<br />**In case you want to revoke your own number please use *`self`* as an alias for your user_id.**

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
api_instance = faxplus.NumbersApi(api_client)
number = 'number_example' # str | Phone number to remove members from
user_id = 'user_id_example' # str | ID of the user to revoke the number from. Number can not be removed from the admin

try:
    # Revoke number
    api_instance.revoke_number(number, user_id)
except ApiException as e:
    print("Exception when calling NumbersApi->revoke_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| Phone number to remove members from | 
 **user_id** | **str**| ID of the user to revoke the number from. Number can not be removed from the admin | 

### Return type

void (empty response body)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_number**
> update_number(number, body=body)

Assign number

With this API call you will be able to assign a specific number to a specific account (one of your members).

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
api_instance = faxplus.NumbersApi(api_client)
number = 'number_example' # str | Phone number to update
body = faxplus.PayloadNumberModification() # PayloadNumberModification | Request object for making changes in number object (optional)

try:
    # Assign number
    api_instance.update_number(number, body=body)
except ApiException as e:
    print("Exception when calling NumbersApi->update_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| Phone number to update | 
 **body** | [**PayloadNumberModification**](PayloadNumberModification.md)| Request object for making changes in number object | [optional] 

### Return type

void (empty response body)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

