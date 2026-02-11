# PatchedSubnetRequestVpc

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Name of the VPC | 
**Environment** | Pointer to **NullableInt32** |  | [optional] 

## Methods

### NewPatchedSubnetRequestVpc

`func NewPatchedSubnetRequestVpc(name string, ) *PatchedSubnetRequestVpc`

NewPatchedSubnetRequestVpc instantiates a new PatchedSubnetRequestVpc object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPatchedSubnetRequestVpcWithDefaults

`func NewPatchedSubnetRequestVpcWithDefaults() *PatchedSubnetRequestVpc`

NewPatchedSubnetRequestVpcWithDefaults instantiates a new PatchedSubnetRequestVpc object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *PatchedSubnetRequestVpc) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *PatchedSubnetRequestVpc) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *PatchedSubnetRequestVpc) SetName(v string)`

SetName sets Name field to given value.


### GetEnvironment

`func (o *PatchedSubnetRequestVpc) GetEnvironment() int32`

GetEnvironment returns the Environment field if non-nil, zero value otherwise.

### GetEnvironmentOk

`func (o *PatchedSubnetRequestVpc) GetEnvironmentOk() (*int32, bool)`

GetEnvironmentOk returns a tuple with the Environment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnvironment

`func (o *PatchedSubnetRequestVpc) SetEnvironment(v int32)`

SetEnvironment sets Environment field to given value.

### HasEnvironment

`func (o *PatchedSubnetRequestVpc) HasEnvironment() bool`

HasEnvironment returns a boolean if a field has been set.

### SetEnvironmentNil

`func (o *PatchedSubnetRequestVpc) SetEnvironmentNil(b bool)`

 SetEnvironmentNil sets the value for Environment to be an explicit nil

### UnsetEnvironment
`func (o *PatchedSubnetRequestVpc) UnsetEnvironment()`

UnsetEnvironment ensures that no value is present for Environment, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


