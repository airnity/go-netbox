# BriefVPC

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** |  | [readonly] 
**Url** | **string** |  | [readonly] 
**Display** | Pointer to **interface{}** |  | [optional] [readonly] 
**Name** | **string** | Name of the VPC | 
**Environment** | Pointer to [**NullableBriefEnvironment**](BriefEnvironment.md) |  | [optional] 

## Methods

### NewBriefVPC

`func NewBriefVPC(id int32, url string, name string, ) *BriefVPC`

NewBriefVPC instantiates a new BriefVPC object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBriefVPCWithDefaults

`func NewBriefVPCWithDefaults() *BriefVPC`

NewBriefVPCWithDefaults instantiates a new BriefVPC object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *BriefVPC) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *BriefVPC) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *BriefVPC) SetId(v int32)`

SetId sets Id field to given value.


### GetUrl

`func (o *BriefVPC) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *BriefVPC) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *BriefVPC) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetDisplay

`func (o *BriefVPC) GetDisplay() interface{}`

GetDisplay returns the Display field if non-nil, zero value otherwise.

### GetDisplayOk

`func (o *BriefVPC) GetDisplayOk() (*interface{}, bool)`

GetDisplayOk returns a tuple with the Display field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplay

`func (o *BriefVPC) SetDisplay(v interface{})`

SetDisplay sets Display field to given value.

### HasDisplay

`func (o *BriefVPC) HasDisplay() bool`

HasDisplay returns a boolean if a field has been set.

### SetDisplayNil

`func (o *BriefVPC) SetDisplayNil(b bool)`

 SetDisplayNil sets the value for Display to be an explicit nil

### UnsetDisplay
`func (o *BriefVPC) UnsetDisplay()`

UnsetDisplay ensures that no value is present for Display, not even an explicit nil
### GetName

`func (o *BriefVPC) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *BriefVPC) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *BriefVPC) SetName(v string)`

SetName sets Name field to given value.


### GetEnvironment

`func (o *BriefVPC) GetEnvironment() BriefEnvironment`

GetEnvironment returns the Environment field if non-nil, zero value otherwise.

### GetEnvironmentOk

`func (o *BriefVPC) GetEnvironmentOk() (*BriefEnvironment, bool)`

GetEnvironmentOk returns a tuple with the Environment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnvironment

`func (o *BriefVPC) SetEnvironment(v BriefEnvironment)`

SetEnvironment sets Environment field to given value.

### HasEnvironment

`func (o *BriefVPC) HasEnvironment() bool`

HasEnvironment returns a boolean if a field has been set.

### SetEnvironmentNil

`func (o *BriefVPC) SetEnvironmentNil(b bool)`

 SetEnvironmentNil sets the value for Environment to be an explicit nil

### UnsetEnvironment
`func (o *BriefVPC) UnsetEnvironment()`

UnsetEnvironment ensures that no value is present for Environment, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


