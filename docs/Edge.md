# Edge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Higher-level relationship type of this edge | [optional] 
**relation** | **str** | Lower-level relationship type of this edge | [optional] 
**source_id** | **str** | Corresponds to the @id of source node of this edge | [optional] 
**target_id** | **str** | Corresponds to the @id of target node of this edge | [optional] 
**is_defined_by** | **str** | A CURIE/URI for the translator group that made the KG | [optional] 
**provided_by** | **str** | A CURIE/URI for the knowledge source that defined this edge | [optional] 
**confidence** | **float** | Confidence metric for this edge, a value 0.0 (no confidence) and 1.0 (highest confidence) | [optional] 
**publications** | **str** | A CURIE/URI for publications associated with this edge | [optional] 
**evidence_type** | **str** | A CURIE/URI for class of evidence supporting the statement made in an edge - typically a class from the ECO ontology | [optional] 
**qualifiers** | **str** | Terms representing qualifiers that modify or qualify the meaning of the statement made in an edge | [optional] 
**negated** | **bool** | Boolean that if set to true, indicates the edge statement is negated i.e. is not true | [optional] 
**attribute_list** | [**list[EdgeAttribute]**](EdgeAttribute.md) | A list of additional attributes for this edge | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


