# faxplus.OutboxApi

All URIs are relative to *https://restapi.fax.plus/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_outbox_fax**](OutboxApi.md#delete_outbox_fax) | **DELETE** /accounts/{user_id}/outbox/{outbox_fax_id} | Delete an outgoing fax
[**get_outbox_fax**](OutboxApi.md#get_outbox_fax) | **GET** /accounts/{user_id}/outbox/{outbox_fax_id} | List outgoing faxes
[**list_outbox_faxes**](OutboxApi.md#list_outbox_faxes) | **GET** /accounts/{user_id}/outbox | List faxes in the outbox
[**send_fax**](OutboxApi.md#send_fax) | **POST** /accounts/{user_id}/outbox | Send a fax
[**update_outbox_fax**](OutboxApi.md#update_outbox_fax) | **PUT** /accounts/{user_id}/outbox/{outbox_fax_id} | Modify an outgoing fax

# **delete_outbox_fax**
> delete_outbox_fax(user_id, outbox_fax_id)

Delete an outgoing fax

Delete an outgoing fax that is being scheduled for sending

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
api_instance = faxplus.OutboxApi(api_client)
user_id = 'user_id_example' # str | self or user id of a corporate member
outbox_fax_id = 'outbox_fax_id_example' # str | ID of the outgoing fax to delete

try:
    # Delete an outgoing fax
    api_instance.delete_outbox_fax(user_id, outbox_fax_id)
except ApiException as e:
    print("Exception when calling OutboxApi->delete_outbox_fax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| self or user id of a corporate member | 
 **outbox_fax_id** | **str**| ID of the outgoing fax to delete | 

### Return type

void (empty response body)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outbox_fax**
> Outbox get_outbox_fax(user_id, outbox_fax_id)

List outgoing faxes

Get a list of faxes currently scheduled for sending

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
api_instance = faxplus.OutboxApi(api_client)
user_id = 'user_id_example' # str | self or user id of a corporate member
outbox_fax_id = 'outbox_fax_id_example' # str | ID of the outgoing fax to get

try:
    # List outgoing faxes
    api_response = api_instance.get_outbox_fax(user_id, outbox_fax_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboxApi->get_outbox_fax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| self or user id of a corporate member | 
 **outbox_fax_id** | **str**| ID of the outgoing fax to get | 

### Return type

[**Outbox**](Outbox.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_outbox_faxes**
> OutboxList list_outbox_faxes(user_id)

List faxes in the outbox

Get a list of the faxes in the outbox which were not yet sent

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
api_instance = faxplus.OutboxApi(api_client)
user_id = 'user_id_example' # str | self or user id of a corporate member

try:
    # List faxes in the outbox
    api_response = api_instance.list_outbox_faxes(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboxApi->list_outbox_faxes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| self or user id of a corporate member | 

### Return type

[**OutboxList**](OutboxList.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_fax**
> SendFaxResponse send_fax(user_id, body=body)

Send a fax

Send a fax to one or more destinations. For corporate members without a fax number assigned set the 'from' parameter to 'no_number'

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
api_instance = faxplus.OutboxApi(api_client)
user_id = 'user_id_example' # str | self or user id of a corporate member
body = faxplus.PayloadOutbox() # PayloadOutbox | Request to send new outbound fax (optional)

try:
    # Send a fax
    api_response = api_instance.send_fax(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboxApi->send_fax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| self or user id of a corporate member | 
 **body** | [**PayloadOutbox**](PayloadOutbox.md)| Request to send new outbound fax | [optional] 

### Return type

[**SendFaxResponse**](SendFaxResponse.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_outbox_fax**
> update_outbox_fax(user_id, outbox_fax_id, body=body)

Modify an outgoing fax

Modify an outgoing fax that is being scheduled for sending

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
api_instance = faxplus.OutboxApi(api_client)
user_id = 'user_id_example' # str | self or user id of a corporate member
outbox_fax_id = 'outbox_fax_id_example' # str | ID of the outgoing fax to update
body = faxplus.PayloadOutboxModification() # PayloadOutboxModification | Request object for making changes in an outbox object (optional)

try:
    # Modify an outgoing fax
    api_instance.update_outbox_fax(user_id, outbox_fax_id, body=body)
except ApiException as e:
    print("Exception when calling OutboxApi->update_outbox_fax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| self or user id of a corporate member | 
 **outbox_fax_id** | **str**| ID of the outgoing fax to update | 
 **body** | [**PayloadOutboxModification**](PayloadOutboxModification.md)| Request object for making changes in an outbox object | [optional] 

### Return type

void (empty response body)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

