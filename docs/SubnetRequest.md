# SubnetRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **string** | Name of the Subnet | [optional] 
**Prefixes** | Pointer to [**[]WritableNestedSubnetPrefixRequest**](WritableNestedSubnetPrefixRequest.md) |  | [optional] 
**Vpc** | Pointer to [**NullablePatchedSubnetRequestVpc**](PatchedSubnetRequestVpc.md) |  | [optional] 
**Region** | Pointer to [**NullablePatchedSubnetRequestRegion**](PatchedSubnetRequestRegion.md) |  | [optional] 
**Tenant** | Pointer to [**NullablePatchedSubnetIPAddressRequestTenant**](PatchedSubnetIPAddressRequestTenant.md) |  | [optional] 
**Purpose** | Pointer to [**NullablePatchedSubnetRequestPurpose**](PatchedSubnetRequestPurpose.md) |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**Comments** | Pointer to **string** |  | [optional] 
**CustomFields** | Pointer to **map[string]interface{}** |  | [optional] 

## Methods

### NewSubnetRequest

`func NewSubnetRequest() *SubnetRequest`

NewSubnetRequest instantiates a new SubnetRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSubnetRequestWithDefaults

`func NewSubnetRequestWithDefaults() *SubnetRequest`

NewSubnetRequestWithDefaults instantiates a new SubnetRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *SubnetRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *SubnetRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *SubnetRequest) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *SubnetRequest) HasName() bool`

HasName returns a boolean if a field has been set.

### GetPrefixes

`func (o *SubnetRequest) GetPrefixes() []WritableNestedSubnetPrefixRequest`

GetPrefixes returns the Prefixes field if non-nil, zero value otherwise.

### GetPrefixesOk

`func (o *SubnetRequest) GetPrefixesOk() (*[]WritableNestedSubnetPrefixRequest, bool)`

GetPrefixesOk returns a tuple with the Prefixes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefixes

`func (o *SubnetRequest) SetPrefixes(v []WritableNestedSubnetPrefixRequest)`

SetPrefixes sets Prefixes field to given value.

### HasPrefixes

`func (o *SubnetRequest) HasPrefixes() bool`

HasPrefixes returns a boolean if a field has been set.

### GetVpc

`func (o *SubnetRequest) GetVpc() PatchedSubnetRequestVpc`

GetVpc returns the Vpc field if non-nil, zero value otherwise.

### GetVpcOk

`func (o *SubnetRequest) GetVpcOk() (*PatchedSubnetRequestVpc, bool)`

GetVpcOk returns a tuple with the Vpc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVpc

`func (o *SubnetRequest) SetVpc(v PatchedSubnetRequestVpc)`

SetVpc sets Vpc field to given value.

### HasVpc

`func (o *SubnetRequest) HasVpc() bool`

HasVpc returns a boolean if a field has been set.

### SetVpcNil

`func (o *SubnetRequest) SetVpcNil(b bool)`

 SetVpcNil sets the value for Vpc to be an explicit nil

### UnsetVpc
`func (o *SubnetRequest) UnsetVpc()`

UnsetVpc ensures that no value is present for Vpc, not even an explicit nil
### GetRegion

`func (o *SubnetRequest) GetRegion() PatchedSubnetRequestRegion`

GetRegion returns the Region field if non-nil, zero value otherwise.

### GetRegionOk

`func (o *SubnetRequest) GetRegionOk() (*PatchedSubnetRequestRegion, bool)`

GetRegionOk returns a tuple with the Region field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegion

`func (o *SubnetRequest) SetRegion(v PatchedSubnetRequestRegion)`

SetRegion sets Region field to given value.

### HasRegion

`func (o *SubnetRequest) HasRegion() bool`

HasRegion returns a boolean if a field has been set.

### SetRegionNil

`func (o *SubnetRequest) SetRegionNil(b bool)`

 SetRegionNil sets the value for Region to be an explicit nil

### UnsetRegion
`func (o *SubnetRequest) UnsetRegion()`

UnsetRegion ensures that no value is present for Region, not even an explicit nil
### GetTenant

`func (o *SubnetRequest) GetTenant() PatchedSubnetIPAddressRequestTenant`

GetTenant returns the Tenant field if non-nil, zero value otherwise.

### GetTenantOk

`func (o *SubnetRequest) GetTenantOk() (*PatchedSubnetIPAddressRequestTenant, bool)`

GetTenantOk returns a tuple with the Tenant field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTenant

`func (o *SubnetRequest) SetTenant(v PatchedSubnetIPAddressRequestTenant)`

SetTenant sets Tenant field to given value.

### HasTenant

`func (o *SubnetRequest) HasTenant() bool`

HasTenant returns a boolean if a field has been set.

### SetTenantNil

`func (o *SubnetRequest) SetTenantNil(b bool)`

 SetTenantNil sets the value for Tenant to be an explicit nil

### UnsetTenant
`func (o *SubnetRequest) UnsetTenant()`

UnsetTenant ensures that no value is present for Tenant, not even an explicit nil
### GetPurpose

`func (o *SubnetRequest) GetPurpose() PatchedSubnetRequestPurpose`

GetPurpose returns the Purpose field if non-nil, zero value otherwise.

### GetPurposeOk

`func (o *SubnetRequest) GetPurposeOk() (*PatchedSubnetRequestPurpose, bool)`

GetPurposeOk returns a tuple with the Purpose field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPurpose

`func (o *SubnetRequest) SetPurpose(v PatchedSubnetRequestPurpose)`

SetPurpose sets Purpose field to given value.

### HasPurpose

`func (o *SubnetRequest) HasPurpose() bool`

HasPurpose returns a boolean if a field has been set.

### SetPurposeNil

`func (o *SubnetRequest) SetPurposeNil(b bool)`

 SetPurposeNil sets the value for Purpose to be an explicit nil

### UnsetPurpose
`func (o *SubnetRequest) UnsetPurpose()`

UnsetPurpose ensures that no value is present for Purpose, not even an explicit nil
### GetDescription

`func (o *SubnetRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *SubnetRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *SubnetRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *SubnetRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetComments

`func (o *SubnetRequest) GetComments() string`

GetComments returns the Comments field if non-nil, zero value otherwise.

### GetCommentsOk

`func (o *SubnetRequest) GetCommentsOk() (*string, bool)`

GetCommentsOk returns a tuple with the Comments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComments

`func (o *SubnetRequest) SetComments(v string)`

SetComments sets Comments field to given value.

### HasComments

`func (o *SubnetRequest) HasComments() bool`

HasComments returns a boolean if a field has been set.

### GetCustomFields

`func (o *SubnetRequest) GetCustomFields() map[string]interface{}`

GetCustomFields returns the CustomFields field if non-nil, zero value otherwise.

### GetCustomFieldsOk

`func (o *SubnetRequest) GetCustomFieldsOk() (*map[string]interface{}, bool)`

GetCustomFieldsOk returns a tuple with the CustomFields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomFields

`func (o *SubnetRequest) SetCustomFields(v map[string]interface{})`

SetCustomFields sets CustomFields field to given value.

### HasCustomFields

`func (o *SubnetRequest) HasCustomFields() bool`

HasCustomFields returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


