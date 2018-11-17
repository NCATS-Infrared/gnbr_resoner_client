# coding: utf-8

"""
    GNBR Reasoner API

    GNBR Reasoner API  # noqa: E501

    OpenAPI spec version: 0.8.0
    Contact: srensi@stanford.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.query_api import QueryApi  # noqa: E501
from swagger_client.rest import ApiException


class TestQueryApi(unittest.TestCase):
    """QueryApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.query_api.QueryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_query(self):
        """Test case for query

        Query using a predefined query type  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
