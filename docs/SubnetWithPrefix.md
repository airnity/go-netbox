# SubnetWithPrefix

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** |  | [readonly] 
**Name** | Pointer to **string** | Name of the Subnet | [optional] 
**Purpose** | Pointer to **NullableString** |  | [optional] [readonly] 
**Prefix** | Pointer to [**NullableSubnetPrefixForSubnet**](SubnetPrefixForSubnet.md) |  | [optional] [readonly] 

## Methods

### NewSubnetWithPrefix

`func NewSubnetWithPrefix(id int32, ) *SubnetWithPrefix`

NewSubnetWithPrefix instantiates a new SubnetWithPrefix object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSubnetWithPrefixWithDefaults

`func NewSubnetWithPrefixWithDefaults() *SubnetWithPrefix`

NewSubnetWithPrefixWithDefaults instantiates a new SubnetWithPrefix object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SubnetWithPrefix) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SubnetWithPrefix) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SubnetWithPrefix) SetId(v int32)`

SetId sets Id field to given value.


### GetName

`func (o *SubnetWithPrefix) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *SubnetWithPrefix) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *SubnetWithPrefix) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *SubnetWithPrefix) HasName() bool`

HasName returns a boolean if a field has been set.

### GetPurpose

`func (o *SubnetWithPrefix) GetPurpose() string`

GetPurpose returns the Purpose field if non-nil, zero value otherwise.

### GetPurposeOk

`func (o *SubnetWithPrefix) GetPurposeOk() (*string, bool)`

GetPurposeOk returns a tuple with the Purpose field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPurpose

`func (o *SubnetWithPrefix) SetPurpose(v string)`

SetPurpose sets Purpose field to given value.

### HasPurpose

`func (o *SubnetWithPrefix) HasPurpose() bool`

HasPurpose returns a boolean if a field has been set.

### SetPurposeNil

`func (o *SubnetWithPrefix) SetPurposeNil(b bool)`

 SetPurposeNil sets the value for Purpose to be an explicit nil

### UnsetPurpose
`func (o *SubnetWithPrefix) UnsetPurpose()`

UnsetPurpose ensures that no value is present for Purpose, not even an explicit nil
### GetPrefix

`func (o *SubnetWithPrefix) GetPrefix() SubnetPrefixForSubnet`

GetPrefix returns the Prefix field if non-nil, zero value otherwise.

### GetPrefixOk

`func (o *SubnetWithPrefix) GetPrefixOk() (*SubnetPrefixForSubnet, bool)`

GetPrefixOk returns a tuple with the Prefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefix

`func (o *SubnetWithPrefix) SetPrefix(v SubnetPrefixForSubnet)`

SetPrefix sets Prefix field to given value.

### HasPrefix

`func (o *SubnetWithPrefix) HasPrefix() bool`

HasPrefix returns a boolean if a field has been set.

### SetPrefixNil

`func (o *SubnetWithPrefix) SetPrefixNil(b bool)`

 SetPrefixNil sets the value for Prefix to be an explicit nil

### UnsetPrefix
`func (o *SubnetWithPrefix) UnsetPrefix()`

UnsetPrefix ensures that no value is present for Prefix, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


