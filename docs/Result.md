# Result

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | URI for this response | [optional] 
**description** | **str** | A free text description of this result answer from the reasoner | [optional] 
**text** | **str** | DEPRECATED | [optional] 
**essence** | **str** | A single string that is the terse essence of the result (useful for simple answers) | [optional] 
**row_data** | **list[str]** | An arbitrary list of values that captures the essence of the result that can be turned into a tabular result across all answers (each result is a row) for a user that wants tabular output | [optional] 
**score** | **float** | Any type of score associated with this result (highest confidence) | [optional] 
**score_name** | **str** | Name for the score | [optional] 
**score_direction** | **str** | Sorting indicator for the score: one of higher_is_better or lower_is_better | [optional] 
**confidence** | **float** | Confidence metric for this result, a value 0.0 (no confidence) and 1.0 (highest confidence) | [optional] 
**result_type** | **str** | One of several possible result types: &#39;individual query answer&#39;, &#39;neighborhood graph&#39;, &#39;type summary graph&#39; | [optional] 
**result_group** | **int** | An integer group number for results for use in cases where several results should be grouped together. Also useful to control sorting ascending. | [optional] 
**result_group_similarity_score** | **float** | A score that denotes the similarity of this result to other members of the result_group | [optional] 
**reasoner_id** | **str** | Identifier string of the reasoner that provided this result (e.g., RTX, Robokop, Indigo, Integrator) | [optional] 
**result_graph** | [**ResultGraph**](ResultGraph.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


