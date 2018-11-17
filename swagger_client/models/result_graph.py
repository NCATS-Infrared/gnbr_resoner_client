# coding: utf-8

"""
    GNBR Reasoner API

    GNBR Reasoner API  # noqa: E501

    OpenAPI spec version: 0.8.0
    Contact: srensi@stanford.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.edge import Edge  # noqa: F401,E501
from swagger_client.models.node import Node  # noqa: F401,E501


class ResultGraph(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'node_list': 'list[Node]',
        'edge_list': 'list[Edge]'
    }

    attribute_map = {
        'node_list': 'node_list',
        'edge_list': 'edge_list'
    }

    def __init__(self, node_list=None, edge_list=None):  # noqa: E501
        """ResultGraph - a model defined in Swagger"""  # noqa: E501

        self._node_list = None
        self._edge_list = None
        self.discriminator = None

        if node_list is not None:
            self.node_list = node_list
        if edge_list is not None:
            self.edge_list = edge_list

    @property
    def node_list(self):
        """Gets the node_list of this ResultGraph.  # noqa: E501


        :return: The node_list of this ResultGraph.  # noqa: E501
        :rtype: list[Node]
        """
        return self._node_list

    @node_list.setter
    def node_list(self, node_list):
        """Sets the node_list of this ResultGraph.


        :param node_list: The node_list of this ResultGraph.  # noqa: E501
        :type: list[Node]
        """

        self._node_list = node_list

    @property
    def edge_list(self):
        """Gets the edge_list of this ResultGraph.  # noqa: E501


        :return: The edge_list of this ResultGraph.  # noqa: E501
        :rtype: list[Edge]
        """
        return self._edge_list

    @edge_list.setter
    def edge_list(self, edge_list):
        """Sets the edge_list of this ResultGraph.


        :param edge_list: The edge_list of this ResultGraph.  # noqa: E501
        :type: list[Edge]
        """

        self._edge_list = edge_list

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResultGraph):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
