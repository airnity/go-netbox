# AvailablePrefixIP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Family** | **int32** |  | [readonly] 
**Address** | **string** |  | [readonly] 
**MaskLength** | **int32** |  | [readonly] 
**Vpc** | Pointer to [**NullableVPC**](VPC.md) |  | [optional] [readonly] 
**SubnetPrefix** | [**NestedSubnetPrefix**](NestedSubnetPrefix.md) |  | [readonly] 
**Description** | Pointer to **string** |  | [optional] 

## Methods

### NewAvailablePrefixIP

`func NewAvailablePrefixIP(family int32, address string, maskLength int32, subnetPrefix NestedSubnetPrefix, ) *AvailablePrefixIP`

NewAvailablePrefixIP instantiates a new AvailablePrefixIP object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAvailablePrefixIPWithDefaults

`func NewAvailablePrefixIPWithDefaults() *AvailablePrefixIP`

NewAvailablePrefixIPWithDefaults instantiates a new AvailablePrefixIP object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFamily

`func (o *AvailablePrefixIP) GetFamily() int32`

GetFamily returns the Family field if non-nil, zero value otherwise.

### GetFamilyOk

`func (o *AvailablePrefixIP) GetFamilyOk() (*int32, bool)`

GetFamilyOk returns a tuple with the Family field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFamily

`func (o *AvailablePrefixIP) SetFamily(v int32)`

SetFamily sets Family field to given value.


### GetAddress

`func (o *AvailablePrefixIP) GetAddress() string`

GetAddress returns the Address field if non-nil, zero value otherwise.

### GetAddressOk

`func (o *AvailablePrefixIP) GetAddressOk() (*string, bool)`

GetAddressOk returns a tuple with the Address field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddress

`func (o *AvailablePrefixIP) SetAddress(v string)`

SetAddress sets Address field to given value.


### GetMaskLength

`func (o *AvailablePrefixIP) GetMaskLength() int32`

GetMaskLength returns the MaskLength field if non-nil, zero value otherwise.

### GetMaskLengthOk

`func (o *AvailablePrefixIP) GetMaskLengthOk() (*int32, bool)`

GetMaskLengthOk returns a tuple with the MaskLength field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaskLength

`func (o *AvailablePrefixIP) SetMaskLength(v int32)`

SetMaskLength sets MaskLength field to given value.


### GetVpc

`func (o *AvailablePrefixIP) GetVpc() VPC`

GetVpc returns the Vpc field if non-nil, zero value otherwise.

### GetVpcOk

`func (o *AvailablePrefixIP) GetVpcOk() (*VPC, bool)`

GetVpcOk returns a tuple with the Vpc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVpc

`func (o *AvailablePrefixIP) SetVpc(v VPC)`

SetVpc sets Vpc field to given value.

### HasVpc

`func (o *AvailablePrefixIP) HasVpc() bool`

HasVpc returns a boolean if a field has been set.

### SetVpcNil

`func (o *AvailablePrefixIP) SetVpcNil(b bool)`

 SetVpcNil sets the value for Vpc to be an explicit nil

### UnsetVpc
`func (o *AvailablePrefixIP) UnsetVpc()`

UnsetVpc ensures that no value is present for Vpc, not even an explicit nil
### GetSubnetPrefix

`func (o *AvailablePrefixIP) GetSubnetPrefix() NestedSubnetPrefix`

GetSubnetPrefix returns the SubnetPrefix field if non-nil, zero value otherwise.

### GetSubnetPrefixOk

`func (o *AvailablePrefixIP) GetSubnetPrefixOk() (*NestedSubnetPrefix, bool)`

GetSubnetPrefixOk returns a tuple with the SubnetPrefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubnetPrefix

`func (o *AvailablePrefixIP) SetSubnetPrefix(v NestedSubnetPrefix)`

SetSubnetPrefix sets SubnetPrefix field to given value.


### GetDescription

`func (o *AvailablePrefixIP) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *AvailablePrefixIP) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *AvailablePrefixIP) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *AvailablePrefixIP) HasDescription() bool`

HasDescription returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


