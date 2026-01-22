# VPC

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** |  | [readonly] 
**Url** | **string** |  | [readonly] 
**Display** | Pointer to **interface{}** |  | [optional] [readonly] 
**Name** | **string** | Name of the VPC | 
**Environment** | Pointer to [**NullableBriefEnvironment**](BriefEnvironment.md) |  | [optional] 
**Created** | Pointer to **NullableTime** |  | [optional] [readonly] 
**LastUpdated** | Pointer to **NullableTime** |  | [optional] [readonly] 
**CustomFieldData** | Pointer to **interface{}** |  | [optional] 
**Tags** | Pointer to [**[]NestedTag**](NestedTag.md) |  | [optional] 

## Methods

### NewVPC

`func NewVPC(id int32, url string, name string, ) *VPC`

NewVPC instantiates a new VPC object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewVPCWithDefaults

`func NewVPCWithDefaults() *VPC`

NewVPCWithDefaults instantiates a new VPC object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *VPC) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *VPC) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *VPC) SetId(v int32)`

SetId sets Id field to given value.


### GetUrl

`func (o *VPC) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *VPC) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *VPC) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetDisplay

`func (o *VPC) GetDisplay() interface{}`

GetDisplay returns the Display field if non-nil, zero value otherwise.

### GetDisplayOk

`func (o *VPC) GetDisplayOk() (*interface{}, bool)`

GetDisplayOk returns a tuple with the Display field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplay

`func (o *VPC) SetDisplay(v interface{})`

SetDisplay sets Display field to given value.

### HasDisplay

`func (o *VPC) HasDisplay() bool`

HasDisplay returns a boolean if a field has been set.

### SetDisplayNil

`func (o *VPC) SetDisplayNil(b bool)`

 SetDisplayNil sets the value for Display to be an explicit nil

### UnsetDisplay
`func (o *VPC) UnsetDisplay()`

UnsetDisplay ensures that no value is present for Display, not even an explicit nil
### GetName

`func (o *VPC) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *VPC) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *VPC) SetName(v string)`

SetName sets Name field to given value.


### GetEnvironment

`func (o *VPC) GetEnvironment() BriefEnvironment`

GetEnvironment returns the Environment field if non-nil, zero value otherwise.

### GetEnvironmentOk

`func (o *VPC) GetEnvironmentOk() (*BriefEnvironment, bool)`

GetEnvironmentOk returns a tuple with the Environment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnvironment

`func (o *VPC) SetEnvironment(v BriefEnvironment)`

SetEnvironment sets Environment field to given value.

### HasEnvironment

`func (o *VPC) HasEnvironment() bool`

HasEnvironment returns a boolean if a field has been set.

### SetEnvironmentNil

`func (o *VPC) SetEnvironmentNil(b bool)`

 SetEnvironmentNil sets the value for Environment to be an explicit nil

### UnsetEnvironment
`func (o *VPC) UnsetEnvironment()`

UnsetEnvironment ensures that no value is present for Environment, not even an explicit nil
### GetCreated

`func (o *VPC) GetCreated() time.Time`

GetCreated returns the Created field if non-nil, zero value otherwise.

### GetCreatedOk

`func (o *VPC) GetCreatedOk() (*time.Time, bool)`

GetCreatedOk returns a tuple with the Created field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreated

`func (o *VPC) SetCreated(v time.Time)`

SetCreated sets Created field to given value.

### HasCreated

`func (o *VPC) HasCreated() bool`

HasCreated returns a boolean if a field has been set.

### SetCreatedNil

`func (o *VPC) SetCreatedNil(b bool)`

 SetCreatedNil sets the value for Created to be an explicit nil

### UnsetCreated
`func (o *VPC) UnsetCreated()`

UnsetCreated ensures that no value is present for Created, not even an explicit nil
### GetLastUpdated

`func (o *VPC) GetLastUpdated() time.Time`

GetLastUpdated returns the LastUpdated field if non-nil, zero value otherwise.

### GetLastUpdatedOk

`func (o *VPC) GetLastUpdatedOk() (*time.Time, bool)`

GetLastUpdatedOk returns a tuple with the LastUpdated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastUpdated

`func (o *VPC) SetLastUpdated(v time.Time)`

SetLastUpdated sets LastUpdated field to given value.

### HasLastUpdated

`func (o *VPC) HasLastUpdated() bool`

HasLastUpdated returns a boolean if a field has been set.

### SetLastUpdatedNil

`func (o *VPC) SetLastUpdatedNil(b bool)`

 SetLastUpdatedNil sets the value for LastUpdated to be an explicit nil

### UnsetLastUpdated
`func (o *VPC) UnsetLastUpdated()`

UnsetLastUpdated ensures that no value is present for LastUpdated, not even an explicit nil
### GetCustomFieldData

`func (o *VPC) GetCustomFieldData() interface{}`

GetCustomFieldData returns the CustomFieldData field if non-nil, zero value otherwise.

### GetCustomFieldDataOk

`func (o *VPC) GetCustomFieldDataOk() (*interface{}, bool)`

GetCustomFieldDataOk returns a tuple with the CustomFieldData field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomFieldData

`func (o *VPC) SetCustomFieldData(v interface{})`

SetCustomFieldData sets CustomFieldData field to given value.

### HasCustomFieldData

`func (o *VPC) HasCustomFieldData() bool`

HasCustomFieldData returns a boolean if a field has been set.

### SetCustomFieldDataNil

`func (o *VPC) SetCustomFieldDataNil(b bool)`

 SetCustomFieldDataNil sets the value for CustomFieldData to be an explicit nil

### UnsetCustomFieldData
`func (o *VPC) UnsetCustomFieldData()`

UnsetCustomFieldData ensures that no value is present for CustomFieldData, not even an explicit nil
### GetTags

`func (o *VPC) GetTags() []NestedTag`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *VPC) GetTagsOk() (*[]NestedTag, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTags

`func (o *VPC) SetTags(v []NestedTag)`

SetTags sets Tags field to given value.

### HasTags

`func (o *VPC) HasTags() bool`

HasTags returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


