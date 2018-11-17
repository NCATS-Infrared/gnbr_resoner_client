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

from swagger_client.models.result import Result  # noqa: F401,E501


class Response(object):
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
        'context': 'str',
        'type': 'str',
        'id': 'str',
        'reasoner_id': 'str',
        'tool_version': 'str',
        'schema_version': 'str',
        'datetime': 'str',
        'original_question_text': 'str',
        'restated_question_text': 'str',
        'known_query_type_id': 'str',
        'query_type_id': 'str',
        'terms': 'object',
        'n_results': 'int',
        'response_code': 'str',
        'result_code': 'str',
        'message': 'str',
        'table_column_names': 'list[str]',
        'result_list': 'list[Result]'
    }

    attribute_map = {
        'context': 'context',
        'type': 'type',
        'id': 'id',
        'reasoner_id': 'reasoner_id',
        'tool_version': 'tool_version',
        'schema_version': 'schema_version',
        'datetime': 'datetime',
        'original_question_text': 'original_question_text',
        'restated_question_text': 'restated_question_text',
        'known_query_type_id': 'known_query_type_id',
        'query_type_id': 'query_type_id',
        'terms': 'terms',
        'n_results': 'n_results',
        'response_code': 'response_code',
        'result_code': 'result_code',
        'message': 'message',
        'table_column_names': 'table_column_names',
        'result_list': 'result_list'
    }

    def __init__(self, context=None, type=None, id=None, reasoner_id=None, tool_version=None, schema_version=None, datetime=None, original_question_text=None, restated_question_text=None, known_query_type_id=None, query_type_id=None, terms=None, n_results=None, response_code=None, result_code=None, message=None, table_column_names=None, result_list=None):  # noqa: E501
        """Response - a model defined in Swagger"""  # noqa: E501

        self._context = None
        self._type = None
        self._id = None
        self._reasoner_id = None
        self._tool_version = None
        self._schema_version = None
        self._datetime = None
        self._original_question_text = None
        self._restated_question_text = None
        self._known_query_type_id = None
        self._query_type_id = None
        self._terms = None
        self._n_results = None
        self._response_code = None
        self._result_code = None
        self._message = None
        self._table_column_names = None
        self._result_list = None
        self.discriminator = None

        if context is not None:
            self.context = context
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if reasoner_id is not None:
            self.reasoner_id = reasoner_id
        if tool_version is not None:
            self.tool_version = tool_version
        if schema_version is not None:
            self.schema_version = schema_version
        if datetime is not None:
            self.datetime = datetime
        if original_question_text is not None:
            self.original_question_text = original_question_text
        if restated_question_text is not None:
            self.restated_question_text = restated_question_text
        if known_query_type_id is not None:
            self.known_query_type_id = known_query_type_id
        if query_type_id is not None:
            self.query_type_id = query_type_id
        if terms is not None:
            self.terms = terms
        if n_results is not None:
            self.n_results = n_results
        if response_code is not None:
            self.response_code = response_code
        if result_code is not None:
            self.result_code = result_code
        if message is not None:
            self.message = message
        if table_column_names is not None:
            self.table_column_names = table_column_names
        if result_list is not None:
            self.result_list = result_list

    @property
    def context(self):
        """Gets the context of this Response.  # noqa: E501

        JSON-LD context URI  # noqa: E501

        :return: The context of this Response.  # noqa: E501
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this Response.

        JSON-LD context URI  # noqa: E501

        :param context: The context of this Response.  # noqa: E501
        :type: str
        """

        self._context = context

    @property
    def type(self):
        """Gets the type of this Response.  # noqa: E501

        Entity type of this response  # noqa: E501

        :return: The type of this Response.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Response.

        Entity type of this response  # noqa: E501

        :param type: The type of this Response.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this Response.  # noqa: E501

        URI for this response  # noqa: E501

        :return: The id of this Response.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Response.

        URI for this response  # noqa: E501

        :param id: The id of this Response.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def reasoner_id(self):
        """Gets the reasoner_id of this Response.  # noqa: E501

        Identifier string of the reasoner that provided this response (e.g., RTX, Robokop, Indigo, Integrator)  # noqa: E501

        :return: The reasoner_id of this Response.  # noqa: E501
        :rtype: str
        """
        return self._reasoner_id

    @reasoner_id.setter
    def reasoner_id(self, reasoner_id):
        """Sets the reasoner_id of this Response.

        Identifier string of the reasoner that provided this response (e.g., RTX, Robokop, Indigo, Integrator)  # noqa: E501

        :param reasoner_id: The reasoner_id of this Response.  # noqa: E501
        :type: str
        """

        self._reasoner_id = reasoner_id

    @property
    def tool_version(self):
        """Gets the tool_version of this Response.  # noqa: E501

        Version label of the tool that generated this response  # noqa: E501

        :return: The tool_version of this Response.  # noqa: E501
        :rtype: str
        """
        return self._tool_version

    @tool_version.setter
    def tool_version(self, tool_version):
        """Sets the tool_version of this Response.

        Version label of the tool that generated this response  # noqa: E501

        :param tool_version: The tool_version of this Response.  # noqa: E501
        :type: str
        """

        self._tool_version = tool_version

    @property
    def schema_version(self):
        """Gets the schema_version of this Response.  # noqa: E501

        Version label of this JSON-LD schema  # noqa: E501

        :return: The schema_version of this Response.  # noqa: E501
        :rtype: str
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version):
        """Sets the schema_version of this Response.

        Version label of this JSON-LD schema  # noqa: E501

        :param schema_version: The schema_version of this Response.  # noqa: E501
        :type: str
        """

        self._schema_version = schema_version

    @property
    def datetime(self):
        """Gets the datetime of this Response.  # noqa: E501

        ISO standard datetime string for the time that this response was generated  # noqa: E501

        :return: The datetime of this Response.  # noqa: E501
        :rtype: str
        """
        return self._datetime

    @datetime.setter
    def datetime(self, datetime):
        """Sets the datetime of this Response.

        ISO standard datetime string for the time that this response was generated  # noqa: E501

        :param datetime: The datetime of this Response.  # noqa: E501
        :type: str
        """

        self._datetime = datetime

    @property
    def original_question_text(self):
        """Gets the original_question_text of this Response.  # noqa: E501

        The original question text typed in by the user  # noqa: E501

        :return: The original_question_text of this Response.  # noqa: E501
        :rtype: str
        """
        return self._original_question_text

    @original_question_text.setter
    def original_question_text(self, original_question_text):
        """Sets the original_question_text of this Response.

        The original question text typed in by the user  # noqa: E501

        :param original_question_text: The original_question_text of this Response.  # noqa: E501
        :type: str
        """

        self._original_question_text = original_question_text

    @property
    def restated_question_text(self):
        """Gets the restated_question_text of this Response.  # noqa: E501

        A precise restatement of the question, as understood by the Translator, for which the answer applies. The user should verify that the restated question matches the intent of their original question (it might not).  # noqa: E501

        :return: The restated_question_text of this Response.  # noqa: E501
        :rtype: str
        """
        return self._restated_question_text

    @restated_question_text.setter
    def restated_question_text(self, restated_question_text):
        """Sets the restated_question_text of this Response.

        A precise restatement of the question, as understood by the Translator, for which the answer applies. The user should verify that the restated question matches the intent of their original question (it might not).  # noqa: E501

        :param restated_question_text: The restated_question_text of this Response.  # noqa: E501
        :type: str
        """

        self._restated_question_text = restated_question_text

    @property
    def known_query_type_id(self):
        """Gets the known_query_type_id of this Response.  # noqa: E501

        DEPRECATED  # noqa: E501

        :return: The known_query_type_id of this Response.  # noqa: E501
        :rtype: str
        """
        return self._known_query_type_id

    @known_query_type_id.setter
    def known_query_type_id(self, known_query_type_id):
        """Sets the known_query_type_id of this Response.

        DEPRECATED  # noqa: E501

        :param known_query_type_id: The known_query_type_id of this Response.  # noqa: E501
        :type: str
        """

        self._known_query_type_id = known_query_type_id

    @property
    def query_type_id(self):
        """Gets the query_type_id of this Response.  # noqa: E501

        The query type id if one is known for the query/response (as defined in https://docs.google.com/spreadsheets/d/1Gna_yCbHj14Brp-8GBY50Mq36nwKGl5T5z4REUQQsfw/edit )  # noqa: E501

        :return: The query_type_id of this Response.  # noqa: E501
        :rtype: str
        """
        return self._query_type_id

    @query_type_id.setter
    def query_type_id(self, query_type_id):
        """Sets the query_type_id of this Response.

        The query type id if one is known for the query/response (as defined in https://docs.google.com/spreadsheets/d/1Gna_yCbHj14Brp-8GBY50Mq36nwKGl5T5z4REUQQsfw/edit )  # noqa: E501

        :param query_type_id: The query_type_id of this Response.  # noqa: E501
        :type: str
        """

        self._query_type_id = query_type_id

    @property
    def terms(self):
        """Gets the terms of this Response.  # noqa: E501

        The is string of the query type id if one is known for the query/response  # noqa: E501

        :return: The terms of this Response.  # noqa: E501
        :rtype: object
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """Sets the terms of this Response.

        The is string of the query type id if one is known for the query/response  # noqa: E501

        :param terms: The terms of this Response.  # noqa: E501
        :type: object
        """

        self._terms = terms

    @property
    def n_results(self):
        """Gets the n_results of this Response.  # noqa: E501

        Total number of results in the response (which may be less than what is returned if limits were placed on the results to return)  # noqa: E501

        :return: The n_results of this Response.  # noqa: E501
        :rtype: int
        """
        return self._n_results

    @n_results.setter
    def n_results(self, n_results):
        """Sets the n_results of this Response.

        Total number of results in the response (which may be less than what is returned if limits were placed on the results to return)  # noqa: E501

        :param n_results: The n_results of this Response.  # noqa: E501
        :type: int
        """

        self._n_results = n_results

    @property
    def response_code(self):
        """Gets the response_code of this Response.  # noqa: E501

        Set to OK for success, or some other short string to indicate and error (e.g., KGUnavailable, TermNotFound, etc.)  # noqa: E501

        :return: The response_code of this Response.  # noqa: E501
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """Sets the response_code of this Response.

        Set to OK for success, or some other short string to indicate and error (e.g., KGUnavailable, TermNotFound, etc.)  # noqa: E501

        :param response_code: The response_code of this Response.  # noqa: E501
        :type: str
        """

        self._response_code = response_code

    @property
    def result_code(self):
        """Gets the result_code of this Response.  # noqa: E501

        DEPRECATED  # noqa: E501

        :return: The result_code of this Response.  # noqa: E501
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """Sets the result_code of this Response.

        DEPRECATED  # noqa: E501

        :param result_code: The result_code of this Response.  # noqa: E501
        :type: str
        """

        self._result_code = result_code

    @property
    def message(self):
        """Gets the message of this Response.  # noqa: E501

        Extended message denoting the success or mode of failure for the response  # noqa: E501

        :return: The message of this Response.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Response.

        Extended message denoting the success or mode of failure for the response  # noqa: E501

        :param message: The message of this Response.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def table_column_names(self):
        """Gets the table_column_names of this Response.  # noqa: E501

        List of column names that corresponds to the row_data for each result  # noqa: E501

        :return: The table_column_names of this Response.  # noqa: E501
        :rtype: list[str]
        """
        return self._table_column_names

    @table_column_names.setter
    def table_column_names(self, table_column_names):
        """Sets the table_column_names of this Response.

        List of column names that corresponds to the row_data for each result  # noqa: E501

        :param table_column_names: The table_column_names of this Response.  # noqa: E501
        :type: list[str]
        """

        self._table_column_names = table_column_names

    @property
    def result_list(self):
        """Gets the result_list of this Response.  # noqa: E501


        :return: The result_list of this Response.  # noqa: E501
        :rtype: list[Result]
        """
        return self._result_list

    @result_list.setter
    def result_list(self, result_list):
        """Sets the result_list of this Response.


        :param result_list: The result_list of this Response.  # noqa: E501
        :type: list[Result]
        """

        self._result_list = result_list

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
        if not isinstance(other, Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
