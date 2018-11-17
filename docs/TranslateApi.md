# swagger_client.TranslateApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translate**](TranslateApi.md#translate) | **POST** /translate | Nonfunctional Endpoint


# **translate**
> list[Query] translate(body)

Nonfunctional Endpoint



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TranslateApi()
body = swagger_client.Question() # Question | Question object that needs to be translated

try:
    # Nonfunctional Endpoint
    api_response = api_instance.translate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslateApi->translate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Question**](Question.md)| Question object that needs to be translated | 

### Return type

[**list[Query]**](Query.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

