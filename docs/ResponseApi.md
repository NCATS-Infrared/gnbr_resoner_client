# swagger_client.ResponseApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_response**](ResponseApi.md#get_response) | **GET** /response/{response_id} | Nonfunctional Endpoint
[**get_response_feedback**](ResponseApi.md#get_response_feedback) | **GET** /response/{response_id}/feedback | Nonfunctional Endpoint


# **get_response**
> Response get_response(response_id)

Nonfunctional Endpoint



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResponseApi()
response_id = 56 # int | Integer identifier of the response to return

try:
    # Nonfunctional Endpoint
    api_response = api_instance.get_response(response_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponseApi->get_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | **int**| Integer identifier of the response to return | 

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_response_feedback**
> ResponseFeedback get_response_feedback(response_id)

Nonfunctional Endpoint



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResponseApi()
response_id = 56 # int | Integer identifier of the response to return

try:
    # Nonfunctional Endpoint
    api_response = api_instance.get_response_feedback(response_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponseApi->get_response_feedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | **int**| Integer identifier of the response to return | 

### Return type

[**ResponseFeedback**](ResponseFeedback.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

