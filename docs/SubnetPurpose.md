# SubnetPurpose

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** |  | [readonly] 
**Url** | **string** |  | [readonly] 
**Display** | **string** |  | [readonly] 
**Name** | **string** |  | 
**Slug** | **string** |  | 
**Color** | Pointer to **string** |  | [optional] 
**Created** | Pointer to **NullableTime** |  | [optional] [readonly] 
**LastUpdated** | Pointer to **NullableTime** |  | [optional] [readonly] 
**CustomFieldData** | Pointer to **interface{}** |  | [optional] 
**Tags** | Pointer to [**[]NestedTag**](NestedTag.md) |  | [optional] 

## Methods

### NewSubnetPurpose

`func NewSubnetPurpose(id int32, url string, display string, name string, slug string, ) *SubnetPurpose`

NewSubnetPurpose instantiates a new SubnetPurpose object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSubnetPurposeWithDefaults

`func NewSubnetPurposeWithDefaults() *SubnetPurpose`

NewSubnetPurposeWithDefaults instantiates a new SubnetPurpose object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SubnetPurpose) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SubnetPurpose) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SubnetPurpose) SetId(v int32)`

SetId sets Id field to given value.


### GetUrl

`func (o *SubnetPurpose) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *SubnetPurpose) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *SubnetPurpose) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetDisplay

`func (o *SubnetPurpose) GetDisplay() string`

GetDisplay returns the Display field if non-nil, zero value otherwise.

### GetDisplayOk

`func (o *SubnetPurpose) GetDisplayOk() (*string, bool)`

GetDisplayOk returns a tuple with the Display field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplay

`func (o *SubnetPurpose) SetDisplay(v string)`

SetDisplay sets Display field to given value.


### GetName

`func (o *SubnetPurpose) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *SubnetPurpose) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *SubnetPurpose) SetName(v string)`

SetName sets Name field to given value.


### GetSlug

`func (o *SubnetPurpose) GetSlug() string`

GetSlug returns the Slug field if non-nil, zero value otherwise.

### GetSlugOk

`func (o *SubnetPurpose) GetSlugOk() (*string, bool)`

GetSlugOk returns a tuple with the Slug field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSlug

`func (o *SubnetPurpose) SetSlug(v string)`

SetSlug sets Slug field to given value.


### GetColor

`func (o *SubnetPurpose) GetColor() string`

GetColor returns the Color field if non-nil, zero value otherwise.

### GetColorOk

`func (o *SubnetPurpose) GetColorOk() (*string, bool)`

GetColorOk returns a tuple with the Color field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColor

`func (o *SubnetPurpose) SetColor(v string)`

SetColor sets Color field to given value.

### HasColor

`func (o *SubnetPurpose) HasColor() bool`

HasColor returns a boolean if a field has been set.

### GetCreated

`func (o *SubnetPurpose) GetCreated() time.Time`

GetCreated returns the Created field if non-nil, zero value otherwise.

### GetCreatedOk

`func (o *SubnetPurpose) GetCreatedOk() (*time.Time, bool)`

GetCreatedOk returns a tuple with the Created field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreated

`func (o *SubnetPurpose) SetCreated(v time.Time)`

SetCreated sets Created field to given value.

### HasCreated

`func (o *SubnetPurpose) HasCreated() bool`

HasCreated returns a boolean if a field has been set.

### SetCreatedNil

`func (o *SubnetPurpose) SetCreatedNil(b bool)`

 SetCreatedNil sets the value for Created to be an explicit nil

### UnsetCreated
`func (o *SubnetPurpose) UnsetCreated()`

UnsetCreated ensures that no value is present for Created, not even an explicit nil
### GetLastUpdated

`func (o *SubnetPurpose) GetLastUpdated() time.Time`

GetLastUpdated returns the LastUpdated field if non-nil, zero value otherwise.

### GetLastUpdatedOk

`func (o *SubnetPurpose) GetLastUpdatedOk() (*time.Time, bool)`

GetLastUpdatedOk returns a tuple with the LastUpdated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastUpdated

`func (o *SubnetPurpose) SetLastUpdated(v time.Time)`

SetLastUpdated sets LastUpdated field to given value.

### HasLastUpdated

`func (o *SubnetPurpose) HasLastUpdated() bool`

HasLastUpdated returns a boolean if a field has been set.

### SetLastUpdatedNil

`func (o *SubnetPurpose) SetLastUpdatedNil(b bool)`

 SetLastUpdatedNil sets the value for LastUpdated to be an explicit nil

### UnsetLastUpdated
`func (o *SubnetPurpose) UnsetLastUpdated()`

UnsetLastUpdated ensures that no value is present for LastUpdated, not even an explicit nil
### GetCustomFieldData

`func (o *SubnetPurpose) GetCustomFieldData() interface{}`

GetCustomFieldData returns the CustomFieldData field if non-nil, zero value otherwise.

### GetCustomFieldDataOk

`func (o *SubnetPurpose) GetCustomFieldDataOk() (*interface{}, bool)`

GetCustomFieldDataOk returns a tuple with the CustomFieldData field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomFieldData

`func (o *SubnetPurpose) SetCustomFieldData(v interface{})`

SetCustomFieldData sets CustomFieldData field to given value.

### HasCustomFieldData

`func (o *SubnetPurpose) HasCustomFieldData() bool`

HasCustomFieldData returns a boolean if a field has been set.

### SetCustomFieldDataNil

`func (o *SubnetPurpose) SetCustomFieldDataNil(b bool)`

 SetCustomFieldDataNil sets the value for CustomFieldData to be an explicit nil

### UnsetCustomFieldData
`func (o *SubnetPurpose) UnsetCustomFieldData()`

UnsetCustomFieldData ensures that no value is present for CustomFieldData, not even an explicit nil
### GetTags

`func (o *SubnetPurpose) GetTags() []NestedTag`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *SubnetPurpose) GetTagsOk() (*[]NestedTag, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTags

`func (o *SubnetPurpose) SetTags(v []NestedTag)`

SetTags sets Tags field to given value.

### HasTags

`func (o *SubnetPurpose) HasTags() bool`

HasTags returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


