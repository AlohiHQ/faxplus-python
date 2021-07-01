# faxplus.ArchivesApi

All URIs are relative to *https://restapi.fax.plus/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_fax**](ArchivesApi.md#delete_fax) | **DELETE** /accounts/{user_id}/archives/{fax_id} | Delete a fax
[**get_fax**](ArchivesApi.md#get_fax) | **GET** /accounts/{user_id}/archives/{fax_id} | Get a fax record
[**list_faxes**](ArchivesApi.md#list_faxes) | **GET** /accounts/{user_id}/archives | List fax records
[**update_fax**](ArchivesApi.md#update_fax) | **PUT** /accounts/{user_id}/archives/{fax_id} | Modify fax record

# **delete_fax**
> delete_fax(user_id, fax_id)

Delete a fax

Delete a specific fax record by providing its id

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
api_instance = faxplus.ArchivesApi(api_client)
user_id = 'user_id_example' # str | self or user id of a corporate member
fax_id = 'fax_id_example' # str | 

try:
    # Delete a fax
    api_instance.delete_fax(user_id, fax_id)
except ApiException as e:
    print("Exception when calling ArchivesApi->delete_fax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| self or user id of a corporate member | 
 **fax_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fax**
> Fax get_fax(user_id, fax_id)

Get a fax record

Get a specific fax record details like duration, pages etc.

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
api_instance = faxplus.ArchivesApi(api_client)
user_id = 'user_id_example' # str | self or user id of a corporate member
fax_id = 'fax_id_example' # str | 

try:
    # Get a fax record
    api_response = api_instance.get_fax(user_id, fax_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchivesApi->get_fax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| self or user id of a corporate member | 
 **fax_id** | **str**|  | 

### Return type

[**Fax**](Fax.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_faxes**
> FaxList list_faxes(user_id, category=category, after=after, before=before, limit=limit)

List fax records

Get your own or your subordinate's fax archive information

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
api_instance = faxplus.ArchivesApi(api_client)
user_id = 'user_id_example' # str | self or user id of a corporate member
category = faxplus.FaxCategory() # FaxCategory | Category parameter. Valid values: **inbox**, **sent**, **spam** (optional)
after = 'after_example' # str | Start date to get records from that date. Format: *YYYY-MM-DD HH:mm:ss* (optional)
before = 'before_example' # str | End date to get records before that date. Format: *YYYY-MM-DD HH:mm:ss* (optional)
limit = 50 # int | Limit of fax records you want to get per request (optional) (default to 50)

try:
    # List fax records
    api_response = api_instance.list_faxes(user_id, category=category, after=after, before=before, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchivesApi->list_faxes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| self or user id of a corporate member | 
 **category** | [**FaxCategory**](.md)| Category parameter. Valid values: **inbox**, **sent**, **spam** | [optional] 
 **after** | **str**| Start date to get records from that date. Format: *YYYY-MM-DD HH:mm:ss* | [optional] 
 **before** | **str**| End date to get records before that date. Format: *YYYY-MM-DD HH:mm:ss* | [optional] 
 **limit** | **int**| Limit of fax records you want to get per request | [optional] [default to 50]

### Return type

[**FaxList**](FaxList.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fax**
> update_fax(user_id, fax_id, body=body)

Modify fax record

You can modify a fax record's comment or mark it as read

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
api_instance = faxplus.ArchivesApi(api_client)
user_id = 'user_id_example' # str | self or user id of a corporate member
fax_id = 'fax_id_example' # str | 
body = faxplus.PayloadFaxModification() # PayloadFaxModification | Request object for making changes in a fax object (optional)

try:
    # Modify fax record
    api_instance.update_fax(user_id, fax_id, body=body)
except ApiException as e:
    print("Exception when calling ArchivesApi->update_fax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| self or user id of a corporate member | 
 **fax_id** | **str**|  | 
 **body** | [**PayloadFaxModification**](PayloadFaxModification.md)| Request object for making changes in a fax object | [optional] 

### Return type

void (empty response body)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

