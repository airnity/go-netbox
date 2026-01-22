# PatchedSubnetPurposeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **string** |  | [optional] 
**Slug** | Pointer to **string** |  | [optional] 
**Color** | Pointer to **string** |  | [optional] 
**CustomFieldData** | Pointer to **interface{}** |  | [optional] 
**Tags** | Pointer to [**[]NestedTagRequest**](NestedTagRequest.md) |  | [optional] 

## Methods

### NewPatchedSubnetPurposeRequest

`func NewPatchedSubnetPurposeRequest() *PatchedSubnetPurposeRequest`

NewPatchedSubnetPurposeRequest instantiates a new PatchedSubnetPurposeRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPatchedSubnetPurposeRequestWithDefaults

`func NewPatchedSubnetPurposeRequestWithDefaults() *PatchedSubnetPurposeRequest`

NewPatchedSubnetPurposeRequestWithDefaults instantiates a new PatchedSubnetPurposeRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *PatchedSubnetPurposeRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *PatchedSubnetPurposeRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *PatchedSubnetPurposeRequest) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *PatchedSubnetPurposeRequest) HasName() bool`

HasName returns a boolean if a field has been set.

### GetSlug

`func (o *PatchedSubnetPurposeRequest) GetSlug() string`

GetSlug returns the Slug field if non-nil, zero value otherwise.

### GetSlugOk

`func (o *PatchedSubnetPurposeRequest) GetSlugOk() (*string, bool)`

GetSlugOk returns a tuple with the Slug field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSlug

`func (o *PatchedSubnetPurposeRequest) SetSlug(v string)`

SetSlug sets Slug field to given value.

### HasSlug

`func (o *PatchedSubnetPurposeRequest) HasSlug() bool`

HasSlug returns a boolean if a field has been set.

### GetColor

`func (o *PatchedSubnetPurposeRequest) GetColor() string`

GetColor returns the Color field if non-nil, zero value otherwise.

### GetColorOk

`func (o *PatchedSubnetPurposeRequest) GetColorOk() (*string, bool)`

GetColorOk returns a tuple with the Color field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColor

`func (o *PatchedSubnetPurposeRequest) SetColor(v string)`

SetColor sets Color field to given value.

### HasColor

`func (o *PatchedSubnetPurposeRequest) HasColor() bool`

HasColor returns a boolean if a field has been set.

### GetCustomFieldData

`func (o *PatchedSubnetPurposeRequest) GetCustomFieldData() interface{}`

GetCustomFieldData returns the CustomFieldData field if non-nil, zero value otherwise.

### GetCustomFieldDataOk

`func (o *PatchedSubnetPurposeRequest) GetCustomFieldDataOk() (*interface{}, bool)`

GetCustomFieldDataOk returns a tuple with the CustomFieldData field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomFieldData

`func (o *PatchedSubnetPurposeRequest) SetCustomFieldData(v interface{})`

SetCustomFieldData sets CustomFieldData field to given value.

### HasCustomFieldData

`func (o *PatchedSubnetPurposeRequest) HasCustomFieldData() bool`

HasCustomFieldData returns a boolean if a field has been set.

### SetCustomFieldDataNil

`func (o *PatchedSubnetPurposeRequest) SetCustomFieldDataNil(b bool)`

 SetCustomFieldDataNil sets the value for CustomFieldData to be an explicit nil

### UnsetCustomFieldData
`func (o *PatchedSubnetPurposeRequest) UnsetCustomFieldData()`

UnsetCustomFieldData ensures that no value is present for CustomFieldData, not even an explicit nil
### GetTags

`func (o *PatchedSubnetPurposeRequest) GetTags() []NestedTagRequest`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *PatchedSubnetPurposeRequest) GetTagsOk() (*[]NestedTagRequest, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTags

`func (o *PatchedSubnetPurposeRequest) SetTags(v []NestedTagRequest)`

SetTags sets Tags field to given value.

### HasTags

`func (o *PatchedSubnetPurposeRequest) HasTags() bool`

HasTags returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


