# faxplus.NumbersApi

All URIs are relative to *https://restapi.fax.plus/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_number**](NumbersApi.md#get_number) | **GET** /accounts/{user_id}/numbers/{number} | Get number information
[**list_numbers**](NumbersApi.md#list_numbers) | **GET** /accounts/{user_id}/numbers | List phone numbers
[**revoke_number**](NumbersApi.md#revoke_number) | **DELETE** /accounts/{user_id}/numbers/{number} | Revoke number
[**update_number**](NumbersApi.md#update_number) | **PUT** /accounts/{user_id}/numbers/{number} | Assign number

# **get_number**
> Number get_number(user_id, number)

Get number information

Get information about a single purchased/assigned fax number

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
user_id = 'user_id_example' # str | ID of the number owner
number = 'number_example' # str | Fax number to get information about

try:
    # Get number information
    api_response = api_instance.get_number(user_id, number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumbersApi->get_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the number owner | 
 **number** | **str**| Fax number to get information about | 

### Return type

[**Number**](Number.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_numbers**
> NumberList list_numbers(user_id)

List phone numbers

List your purchased/assigned phone numbers. For corporate members all assigned numbers will be returned, while for the corporate admin, all purchased numbers

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
user_id = 'user_id_example' # str | ID of the user to get numbers for

try:
    # List phone numbers
    api_response = api_instance.list_numbers(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumbersApi->list_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the user to get numbers for | 

### Return type

[**NumberList**](NumberList.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_number**
> revoke_number(user_id, number)

Revoke number

Revoke fax number from a corporate member. To revoke your own number use self as a user_id

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
user_id = 'user_id_example' # str | ID of the user to revoke the number from. Number can not be removed from the admin
number = 'number_example' # str | Fax number to remove members from

try:
    # Revoke number
    api_instance.revoke_number(user_id, number)
except ApiException as e:
    print("Exception when calling NumbersApi->revoke_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the user to revoke the number from. Number can not be removed from the admin | 
 **number** | **str**| Fax number to remove members from | 

### Return type

void (empty response body)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_number**
> update_number(user_id, number, body=body)

Assign number

Assign fax number to a corporate member

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
user_id = 'user_id_example' # str | ID of the number owner
number = 'number_example' # str | Fax number to update
body = faxplus.PayloadNumberModification() # PayloadNumberModification | Request object for making changes in number object (optional)

try:
    # Assign number
    api_instance.update_number(user_id, number, body=body)
except ApiException as e:
    print("Exception when calling NumbersApi->update_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the number owner | 
 **number** | **str**| Fax number to update | 
 **body** | [**PayloadNumberModification**](PayloadNumberModification.md)| Request object for making changes in number object | [optional] 

### Return type

void (empty response body)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

