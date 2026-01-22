# PatchedVPCRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **string** | Name of the VPC | [optional] 
**Environment** | Pointer to [**NullableBriefVPCRequestEnvironment**](BriefVPCRequestEnvironment.md) |  | [optional] 
**CustomFieldData** | Pointer to **interface{}** |  | [optional] 
**Tags** | Pointer to [**[]NestedTagRequest**](NestedTagRequest.md) |  | [optional] 

## Methods

### NewPatchedVPCRequest

`func NewPatchedVPCRequest() *PatchedVPCRequest`

NewPatchedVPCRequest instantiates a new PatchedVPCRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPatchedVPCRequestWithDefaults

`func NewPatchedVPCRequestWithDefaults() *PatchedVPCRequest`

NewPatchedVPCRequestWithDefaults instantiates a new PatchedVPCRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *PatchedVPCRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *PatchedVPCRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *PatchedVPCRequest) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *PatchedVPCRequest) HasName() bool`

HasName returns a boolean if a field has been set.

### GetEnvironment

`func (o *PatchedVPCRequest) GetEnvironment() BriefVPCRequestEnvironment`

GetEnvironment returns the Environment field if non-nil, zero value otherwise.

### GetEnvironmentOk

`func (o *PatchedVPCRequest) GetEnvironmentOk() (*BriefVPCRequestEnvironment, bool)`

GetEnvironmentOk returns a tuple with the Environment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnvironment

`func (o *PatchedVPCRequest) SetEnvironment(v BriefVPCRequestEnvironment)`

SetEnvironment sets Environment field to given value.

### HasEnvironment

`func (o *PatchedVPCRequest) HasEnvironment() bool`

HasEnvironment returns a boolean if a field has been set.

### SetEnvironmentNil

`func (o *PatchedVPCRequest) SetEnvironmentNil(b bool)`

 SetEnvironmentNil sets the value for Environment to be an explicit nil

### UnsetEnvironment
`func (o *PatchedVPCRequest) UnsetEnvironment()`

UnsetEnvironment ensures that no value is present for Environment, not even an explicit nil
### GetCustomFieldData

`func (o *PatchedVPCRequest) GetCustomFieldData() interface{}`

GetCustomFieldData returns the CustomFieldData field if non-nil, zero value otherwise.

### GetCustomFieldDataOk

`func (o *PatchedVPCRequest) GetCustomFieldDataOk() (*interface{}, bool)`

GetCustomFieldDataOk returns a tuple with the CustomFieldData field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomFieldData

`func (o *PatchedVPCRequest) SetCustomFieldData(v interface{})`

SetCustomFieldData sets CustomFieldData field to given value.

### HasCustomFieldData

`func (o *PatchedVPCRequest) HasCustomFieldData() bool`

HasCustomFieldData returns a boolean if a field has been set.

### SetCustomFieldDataNil

`func (o *PatchedVPCRequest) SetCustomFieldDataNil(b bool)`

 SetCustomFieldDataNil sets the value for CustomFieldData to be an explicit nil

### UnsetCustomFieldData
`func (o *PatchedVPCRequest) UnsetCustomFieldData()`

UnsetCustomFieldData ensures that no value is present for CustomFieldData, not even an explicit nil
### GetTags

`func (o *PatchedVPCRequest) GetTags() []NestedTagRequest`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *PatchedVPCRequest) GetTagsOk() (*[]NestedTagRequest, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTags

`func (o *PatchedVPCRequest) SetTags(v []NestedTagRequest)`

SetTags sets Tags field to given value.

### HasTags

`func (o *PatchedVPCRequest) HasTags() bool`

HasTags returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


