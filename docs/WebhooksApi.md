# faxplus.WebhooksApi

All URIs are relative to *https://restapi.fax.plus/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhooksApi.md#create_webhook) | **POST** /hooks | Register new webhook
[**delete_webhook**](WebhooksApi.md#delete_webhook) | **DELETE** /hooks/{hook_id} | Delete webhook
[**get_webhooks**](WebhooksApi.md#get_webhooks) | **GET** /hooks | List user webhooks

# **create_webhook**
> WebhookId create_webhook(body=body)

Register new webhook

Register a new webhook which will be called on a specific event. See the WebhookCallback model

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
api_instance = faxplus.WebhooksApi(api_client)
body = faxplus.Webhook() # Webhook | Request to create new webhook (optional)

try:
    # Register new webhook
    api_response = api_instance.create_webhook(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->create_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Webhook**](Webhook.md)| Request to create new webhook | [optional] 

### Return type

[**WebhookId**](WebhookId.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> delete_webhook(hook_id)

Delete webhook

Delete a webhook by its ID

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
api_instance = faxplus.WebhooksApi(api_client)
hook_id = 'hook_id_example' # str | ID of the webhook to delete

try:
    # Delete webhook
    api_instance.delete_webhook(hook_id)
except ApiException as e:
    print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hook_id** | **str**| ID of the webhook to delete | 

### Return type

void (empty response body)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhooks**
> WebhookList get_webhooks(event)

List user webhooks

Returns a list of currently registered webhooks for the requested **event**

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
api_instance = faxplus.WebhooksApi(api_client)
event = faxplus.WebhookEventType() # WebhookEventType | 

try:
    # List user webhooks
    api_response = api_instance.get_webhooks(event)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event** | [**WebhookEventType**](.md)|  | 

### Return type

[**WebhookList**](WebhookList.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

