# swagger_client.ResultApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_result**](ResultApi.md#get_result) | **GET** /result/{result_id} | Nonfunctional Endpoint
[**get_result_feedback**](ResultApi.md#get_result_feedback) | **GET** /result/{result_id}/feedback | Nonfunctional Endpoint
[**post_result_feedback**](ResultApi.md#post_result_feedback) | **POST** /result/{result_id}/feedback | Nonfunctional Endpoint


# **get_result**
> Result get_result(result_id)

Nonfunctional Endpoint



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResultApi()
result_id = 56 # int | Integer identifier of the result to return

try:
    # Nonfunctional Endpoint
    api_response = api_instance.get_result(result_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultApi->get_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **int**| Integer identifier of the result to return | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result_feedback**
> ResultFeedback get_result_feedback(result_id)

Nonfunctional Endpoint



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResultApi()
result_id = 56 # int | Integer identifier of the result to return

try:
    # Nonfunctional Endpoint
    api_response = api_instance.get_result_feedback(result_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultApi->get_result_feedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **int**| Integer identifier of the result to return | 

### Return type

[**ResultFeedback**](ResultFeedback.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_result_feedback**
> post_result_feedback(result_id, body)

Nonfunctional Endpoint



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResultApi()
result_id = 56 # int | Integer identifier of the result to return
body = swagger_client.Feedback() # Feedback | Comment information

try:
    # Nonfunctional Endpoint
    api_instance.post_result_feedback(result_id, body)
except ApiException as e:
    print("Exception when calling ResultApi->post_result_feedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **int**| Integer identifier of the result to return | 
 **body** | [**Feedback**](Feedback.md)| Comment information | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

