# faxplus.FilesApi

All URIs are relative to *https://restapi.fax.plus/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fax_report**](FilesApi.md#get_fax_report) | **GET** /accounts/{user_id}/report/{fax_id} | Get fax confirmation report
[**get_file**](FilesApi.md#get_file) | **GET** /accounts/{user_id}/files/{fax_id} | Download fax file
[**upload_file**](FilesApi.md#upload_file) | **POST** /accounts/{user_id}/files | Upload a file

# **get_fax_report**
> Binary get_fax_report(user_id, fax_id)

Get fax confirmation report

Retrieve fax confirmation report

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
api_instance = faxplus.FilesApi(api_client)
user_id = 'user_id_example' # str | self or user id of a corporate member
fax_id = 'fax_id_example' # str | ID of the fax which you want to download

try:
    # Get fax confirmation report
    api_response = api_instance.get_fax_report(user_id, fax_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->get_fax_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| self or user id of a corporate member | 
 **fax_id** | **str**| ID of the fax which you want to download | 

### Return type

[**Binary**](Binary.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> Binary get_file(user_id, fax_id, format=format)

Download fax file

Download sent or received fax file

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
api_instance = faxplus.FilesApi(api_client)
user_id = 'user_id_example' # str | self or user id of a corporate member
fax_id = 'fax_id_example' # str | ID of the fax which you want to download
format = faxplus.FileType() # FileType | This parameter overrides the Accept header (optional)

try:
    # Download fax file
    api_response = api_instance.get_file(user_id, fax_id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| self or user id of a corporate member | 
 **fax_id** | **str**| ID of the fax which you want to download | 
 **format** | [**FileType**](.md)| This parameter overrides the Accept header | [optional] 

### Return type

[**Binary**](Binary.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, image/tiff, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> FilePath upload_file(user_id, fax_file=fax_file, format=format)

Upload a file

Before sending a fax you need to upload your files using this API. In order to upload your fax file, you have to send a `multipart/form-data` request with your file. Set the `name` to `fax_file`, `filename` to your file's name with extension, and the Content-Type to the file's MIME type. In most cases, the `filename` directive will be automatically added by your library of choice. If the upload was successful you would receive a `file_path` which you can use to send your fax.

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
api_instance = faxplus.FilesApi(api_client)
user_id = 'user_id_example' # str | self or user id of a corporate member
fax_file = 'fax_file_example' # str |  (optional)
format = faxplus.FileType() # FileType | Can be 'pdf' or 'tiff' (optional)

try:
    # Upload a file
    api_response = api_instance.upload_file(user_id, fax_file=fax_file, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| self or user id of a corporate member | 
 **fax_file** | **str**|  | [optional] 
 **format** | [**FileType**](.md)| Can be &#x27;pdf&#x27; or &#x27;tiff&#x27; | [optional] 

### Return type

[**FilePath**](FilePath.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

