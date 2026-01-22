# PatchedSubnetIPAddressRequestVpc

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Name of the VPC | 
**Environment** | Pointer to [**NullableBriefVPCRequestEnvironment**](BriefVPCRequestEnvironment.md) |  | [optional] 

## Methods

### NewPatchedSubnetIPAddressRequestVpc

`func NewPatchedSubnetIPAddressRequestVpc(name string, ) *PatchedSubnetIPAddressRequestVpc`

NewPatchedSubnetIPAddressRequestVpc instantiates a new PatchedSubnetIPAddressRequestVpc object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPatchedSubnetIPAddressRequestVpcWithDefaults

`func NewPatchedSubnetIPAddressRequestVpcWithDefaults() *PatchedSubnetIPAddressRequestVpc`

NewPatchedSubnetIPAddressRequestVpcWithDefaults instantiates a new PatchedSubnetIPAddressRequestVpc object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *PatchedSubnetIPAddressRequestVpc) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *PatchedSubnetIPAddressRequestVpc) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *PatchedSubnetIPAddressRequestVpc) SetName(v string)`

SetName sets Name field to given value.


### GetEnvironment

`func (o *PatchedSubnetIPAddressRequestVpc) GetEnvironment() BriefVPCRequestEnvironment`

GetEnvironment returns the Environment field if non-nil, zero value otherwise.

### GetEnvironmentOk

`func (o *PatchedSubnetIPAddressRequestVpc) GetEnvironmentOk() (*BriefVPCRequestEnvironment, bool)`

GetEnvironmentOk returns a tuple with the Environment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnvironment

`func (o *PatchedSubnetIPAddressRequestVpc) SetEnvironment(v BriefVPCRequestEnvironment)`

SetEnvironment sets Environment field to given value.

### HasEnvironment

`func (o *PatchedSubnetIPAddressRequestVpc) HasEnvironment() bool`

HasEnvironment returns a boolean if a field has been set.

### SetEnvironmentNil

`func (o *PatchedSubnetIPAddressRequestVpc) SetEnvironmentNil(b bool)`

 SetEnvironmentNil sets the value for Environment to be an explicit nil

### UnsetEnvironment
`func (o *PatchedSubnetIPAddressRequestVpc) UnsetEnvironment()`

UnsetEnvironment ensures that no value is present for Environment, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


