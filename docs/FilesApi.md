# faxplus.FilesApi

All URIs are relative to *https://restapi.fax.plus/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_file**](FilesApi.md#get_file) | **GET** /accounts/self/files/{fax_id} | get a file
[**upload_file**](FilesApi.md#upload_file) | **POST** /accounts/self/files | upload a file


# **get_file**
> file get_file(fax_id, format=format)

get a file

Get your fax archive file using it's id.

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
api_instance = faxplus.FilesApi(faxplus.ApiClient(configuration))
fax_id = 'fax_id_example' # str | 
format = 'format_example' # str | can be 'pdf' or 'tiff' (optional)

try:
    # get a file
    api_response = api_instance.get_file(fax_id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fax_id** | **str**|  | 
 **format** | **str**| can be &#39;pdf&#39; or &#39;tiff&#39; | [optional] 

### Return type

[**file**](file.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf, image/tiff

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> File upload_file(fax_file, format=format)

upload a file

Before sending a fax you need to upload your files using this API. In order to upload your fax file, you have to send a `multipart/form-data` request with your file. If the upload was successful you would receive a `file_path` which you can use to send your fax.

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
api_instance = faxplus.FilesApi(faxplus.ApiClient(configuration))
fax_file = '/path/to/file.txt' # file | 
format = 'format_example' # str | can be 'pdf' or 'tiff' (optional)

try:
    # upload a file
    api_response = api_instance.upload_file(fax_file, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fax_file** | **file**|  | 
 **format** | **str**| can be &#39;pdf&#39; or &#39;tiff&#39; | [optional] 

### Return type

[**File**](File.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

