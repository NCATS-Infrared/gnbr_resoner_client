# Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | JSON-LD context URI | [optional] 
**type** | **str** | Entity type of this response | [optional] 
**id** | **str** | URI for this response | [optional] 
**reasoner_id** | **str** | Identifier string of the reasoner that provided this response (e.g., RTX, Robokop, Indigo, Integrator) | [optional] 
**tool_version** | **str** | Version label of the tool that generated this response | [optional] 
**schema_version** | **str** | Version label of this JSON-LD schema | [optional] 
**datetime** | **str** | ISO standard datetime string for the time that this response was generated | [optional] 
**original_question_text** | **str** | The original question text typed in by the user | [optional] 
**restated_question_text** | **str** | A precise restatement of the question, as understood by the Translator, for which the answer applies. The user should verify that the restated question matches the intent of their original question (it might not). | [optional] 
**known_query_type_id** | **str** | DEPRECATED | [optional] 
**query_type_id** | **str** | The query type id if one is known for the query/response (as defined in https://docs.google.com/spreadsheets/d/1Gna_yCbHj14Brp-8GBY50Mq36nwKGl5T5z4REUQQsfw/edit ) | [optional] 
**terms** | **object** | The is string of the query type id if one is known for the query/response | [optional] 
**n_results** | **int** | Total number of results in the response (which may be less than what is returned if limits were placed on the results to return) | [optional] 
**response_code** | **str** | Set to OK for success, or some other short string to indicate and error (e.g., KGUnavailable, TermNotFound, etc.) | [optional] 
**result_code** | **str** | DEPRECATED | [optional] 
**message** | **str** | Extended message denoting the success or mode of failure for the response | [optional] 
**table_column_names** | **list[str]** | List of column names that corresponds to the row_data for each result | [optional] 
**result_list** | [**list[Result]**](Result.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


