# faxplus.OutboxApi

All URIs are relative to *https://restapi.fax.plus/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_outbox_fax**](OutboxApi.md#delete_outbox_fax) | **DELETE** /accounts/self/outbox/{outbox_fax_id} | Delete a fax from outbox
[**get_outbox_fax**](OutboxApi.md#get_outbox_fax) | **GET** /accounts/self/outbox/{outbox_fax_id} | Get an outbox record
[**list_outbox_faxes**](OutboxApi.md#list_outbox_faxes) | **GET** /accounts/self/outbox | Get list of faxes in the outbox
[**send_fax**](OutboxApi.md#send_fax) | **POST** /accounts/self/outbox | Send a fax
[**update_outbox_fax**](OutboxApi.md#update_outbox_fax) | **PUT** /accounts/self/outbox/{outbox_fax_id} | Modify a fax record in outbox

# **delete_outbox_fax**
> delete_outbox_fax(outbox_fax_id)

Delete a fax from outbox

Delete a fax that is being sent and is still in your outbox

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
outbox_fax_id = 'outbox_fax_id_example' # str | ID of the outgoing fax to delete

try:
    # Delete a fax from outbox
    api_instance.delete_outbox_fax(outbox_fax_id)
except ApiException as e:
    print("Exception when calling OutboxApi->delete_outbox_fax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> Outbox get_outbox_fax(outbox_fax_id)

Get an outbox record

Get an outbox fax record information

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
outbox_fax_id = 'outbox_fax_id_example' # str | ID of the outgoing fax to get

try:
    # Get an outbox record
    api_response = api_instance.get_outbox_fax(outbox_fax_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboxApi->get_outbox_fax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> OutboxList list_outbox_faxes()

Get list of faxes in the outbox

Get list of the faxes in the outbox which were not yet sent

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

try:
    # Get list of faxes in the outbox
    api_response = api_instance.list_outbox_faxes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboxApi->list_outbox_faxes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OutboxList**](OutboxList.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_fax**
> send_fax(body=body)

Send a fax

With this API call you will be able to send a fax (one or more files) to one or more destinations. If you are a corporate member and you don't have a fax number set your **from** parameter to **NO_NUMBER**

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
body = faxplus.PayloadOutbox() # PayloadOutbox | Request to send new outbound fax (optional)

try:
    # Send a fax
    api_instance.send_fax(body=body)
except ApiException as e:
    print("Exception when calling OutboxApi->send_fax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PayloadOutbox**](PayloadOutbox.md)| Request to send new outbound fax | [optional] 

### Return type

void (empty response body)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_outbox_fax**
> update_outbox_fax(outbox_fax_id, body=body)

Modify a fax record in outbox

Modify outbox record's comment

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
outbox_fax_id = 'outbox_fax_id_example' # str | ID of the outgoing fax to update
body = faxplus.PayloadOutboxModification() # PayloadOutboxModification | Request object for making changes in an outbox object (optional)

try:
    # Modify a fax record in outbox
    api_instance.update_outbox_fax(outbox_fax_id, body=body)
except ApiException as e:
    print("Exception when calling OutboxApi->update_outbox_fax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

