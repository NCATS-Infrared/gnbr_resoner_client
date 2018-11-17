# swagger_client.QueryApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query**](QueryApi.md#query) | **POST** /query | Query using a predefined query type


# **query**
> Response query(body)

Query using a predefined query type



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryApi()
body = swagger_client.Query() # Query | Query information to be submitted

try:
    # Query using a predefined query type
    api_response = api_instance.query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Query**](Query.md)| Query information to be submitted | 

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

