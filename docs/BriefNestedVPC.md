# BriefNestedVPC

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** |  | [readonly] 
**Url** | **string** |  | [readonly] 
**Display** | **string** |  | [readonly] 
**Name** | **string** | Name of the VPC | 
**Environment** | Pointer to **NullableInt32** |  | [optional] 

## Methods

### NewBriefNestedVPC

`func NewBriefNestedVPC(id int32, url string, display string, name string, ) *BriefNestedVPC`

NewBriefNestedVPC instantiates a new BriefNestedVPC object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBriefNestedVPCWithDefaults

`func NewBriefNestedVPCWithDefaults() *BriefNestedVPC`

NewBriefNestedVPCWithDefaults instantiates a new BriefNestedVPC object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *BriefNestedVPC) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *BriefNestedVPC) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *BriefNestedVPC) SetId(v int32)`

SetId sets Id field to given value.


### GetUrl

`func (o *BriefNestedVPC) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *BriefNestedVPC) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *BriefNestedVPC) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetDisplay

`func (o *BriefNestedVPC) GetDisplay() string`

GetDisplay returns the Display field if non-nil, zero value otherwise.

### GetDisplayOk

`func (o *BriefNestedVPC) GetDisplayOk() (*string, bool)`

GetDisplayOk returns a tuple with the Display field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplay

`func (o *BriefNestedVPC) SetDisplay(v string)`

SetDisplay sets Display field to given value.


### GetName

`func (o *BriefNestedVPC) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *BriefNestedVPC) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *BriefNestedVPC) SetName(v string)`

SetName sets Name field to given value.


### GetEnvironment

`func (o *BriefNestedVPC) GetEnvironment() int32`

GetEnvironment returns the Environment field if non-nil, zero value otherwise.

### GetEnvironmentOk

`func (o *BriefNestedVPC) GetEnvironmentOk() (*int32, bool)`

GetEnvironmentOk returns a tuple with the Environment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnvironment

`func (o *BriefNestedVPC) SetEnvironment(v int32)`

SetEnvironment sets Environment field to given value.

### HasEnvironment

`func (o *BriefNestedVPC) HasEnvironment() bool`

HasEnvironment returns a boolean if a field has been set.

### SetEnvironmentNil

`func (o *BriefNestedVPC) SetEnvironmentNil(b bool)`

 SetEnvironmentNil sets the value for Environment to be an explicit nil

### UnsetEnvironment
`func (o *BriefNestedVPC) UnsetEnvironment()`

UnsetEnvironment ensures that no value is present for Environment, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


