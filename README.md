# swagger-client
GNBR Reasoner API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.8.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/NCATS-Infrared/gnbr_resoner_client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/NCATS-Infrared/gnbr_resoner_client.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://gnbr-reason.ncats.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*QueryApi* | [**query**](docs/QueryApi.md#query) | **POST** /query | Query using a predefined query type
*ResponseApi* | [**get_response**](docs/ResponseApi.md#get_response) | **GET** /response/{response_id} | Nonfunctional Endpoint
*ResponseApi* | [**get_response_feedback**](docs/ResponseApi.md#get_response_feedback) | **GET** /response/{response_id}/feedback | Nonfunctional Endpoint
*ResultApi* | [**get_result**](docs/ResultApi.md#get_result) | **GET** /result/{result_id} | Nonfunctional Endpoint
*ResultApi* | [**get_result_feedback**](docs/ResultApi.md#get_result_feedback) | **GET** /result/{result_id}/feedback | Nonfunctional Endpoint
*ResultApi* | [**post_result_feedback**](docs/ResultApi.md#post_result_feedback) | **POST** /result/{result_id}/feedback | Nonfunctional Endpoint
*TranslateApi* | [**translate**](docs/TranslateApi.md#translate) | **POST** /translate | Nonfunctional Endpoint


## Documentation For Models

 - [Edge](docs/Edge.md)
 - [EdgeAttribute](docs/EdgeAttribute.md)
 - [Feedback](docs/Feedback.md)
 - [Node](docs/Node.md)
 - [NodeAttribute](docs/NodeAttribute.md)
 - [Query](docs/Query.md)
 - [QueryTerms](docs/QueryTerms.md)
 - [Question](docs/Question.md)
 - [Response](docs/Response.md)
 - [ResponseFeedback](docs/ResponseFeedback.md)
 - [Result](docs/Result.md)
 - [ResultFeedback](docs/ResultFeedback.md)
 - [ResultGraph](docs/ResultGraph.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

srensi@stanford.edu

