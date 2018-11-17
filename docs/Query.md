# Query

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_question** | **str** | Original question as it was typed in by the user | [optional] 
**restated_question** | **str** | Restatement of the question as understood by the translator | [optional] 
**message** | **str** | Response from the translation engine to the user | [optional] 
**known_query_type_id** | **str** | DEPRECATED in favor of query_type_id | [optional] 
**query_type_id** | **str** | Identifier for the specific query type | [optional] 
**bypass_cache** | **str** | Set to true in order to bypass any possible cached response and try to answer the query over again | [optional] 
**asynchronous** | **str** | Set to true in order to receive an incomplete response_id if the query will take a while. Client can then periodically request that response_id for a status update and eventual complete response | [optional] 
**options** | **str** | A string of options that can be sent with the query. Options are tool specific and not stipulated here | [optional] 
**max_results** | **int** | Maximum number of individual results to return | [optional] 
**page_size** | **int** | Split the results into pages with this number of results each | [optional] 
**page_number** | **int** | Page number of results when the number of results exceeds the page_size | [optional] 
**terms** | [**QueryTerms**](QueryTerms.md) |  | [optional] 
**reasoner_ids** | **list[str]** | List of reasoners to consult for the query | [optional] 
**query_plan** | **list[object]** | List of node types and edge types in a series that constitute a query plan. Experimental. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


