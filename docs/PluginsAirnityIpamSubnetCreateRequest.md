# PluginsAirnityIpamSubnetCreateRequest

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
**CustomFields** | Pointer to **map[string]map[string]interface{}** |  | [optional] 

## Methods

### NewPluginsAirnityIpamSubnetCreateRequest

`func NewPluginsAirnityIpamSubnetCreateRequest() *PluginsAirnityIpamSubnetCreateRequest`

NewPluginsAirnityIpamSubnetCreateRequest instantiates a new PluginsAirnityIpamSubnetCreateRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPluginsAirnityIpamSubnetCreateRequestWithDefaults

`func NewPluginsAirnityIpamSubnetCreateRequestWithDefaults() *PluginsAirnityIpamSubnetCreateRequest`

NewPluginsAirnityIpamSubnetCreateRequestWithDefaults instantiates a new PluginsAirnityIpamSubnetCreateRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *PluginsAirnityIpamSubnetCreateRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *PluginsAirnityIpamSubnetCreateRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *PluginsAirnityIpamSubnetCreateRequest) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *PluginsAirnityIpamSubnetCreateRequest) HasName() bool`

HasName returns a boolean if a field has been set.

### GetPrefixes

`func (o *PluginsAirnityIpamSubnetCreateRequest) GetPrefixes() []WritableNestedSubnetPrefixRequest`

GetPrefixes returns the Prefixes field if non-nil, zero value otherwise.

### GetPrefixesOk

`func (o *PluginsAirnityIpamSubnetCreateRequest) GetPrefixesOk() (*[]WritableNestedSubnetPrefixRequest, bool)`

GetPrefixesOk returns a tuple with the Prefixes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefixes

`func (o *PluginsAirnityIpamSubnetCreateRequest) SetPrefixes(v []WritableNestedSubnetPrefixRequest)`

SetPrefixes sets Prefixes field to given value.

### HasPrefixes

`func (o *PluginsAirnityIpamSubnetCreateRequest) HasPrefixes() bool`

HasPrefixes returns a boolean if a field has been set.

### GetVpc

`func (o *PluginsAirnityIpamSubnetCreateRequest) GetVpc() PatchedSubnetRequestVpc`

GetVpc returns the Vpc field if non-nil, zero value otherwise.

### GetVpcOk

`func (o *PluginsAirnityIpamSubnetCreateRequest) GetVpcOk() (*PatchedSubnetRequestVpc, bool)`

GetVpcOk returns a tuple with the Vpc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVpc

`func (o *PluginsAirnityIpamSubnetCreateRequest) SetVpc(v PatchedSubnetRequestVpc)`

SetVpc sets Vpc field to given value.

### HasVpc

`func (o *PluginsAirnityIpamSubnetCreateRequest) HasVpc() bool`

HasVpc returns a boolean if a field has been set.

### SetVpcNil

`func (o *PluginsAirnityIpamSubnetCreateRequest) SetVpcNil(b bool)`

 SetVpcNil sets the value for Vpc to be an explicit nil

### UnsetVpc
`func (o *PluginsAirnityIpamSubnetCreateRequest) UnsetVpc()`

UnsetVpc ensures that no value is present for Vpc, not even an explicit nil
### GetRegion

`func (o *PluginsAirnityIpamSubnetCreateRequest) GetRegion() PatchedSubnetRequestRegion`

GetRegion returns the Region field if non-nil, zero value otherwise.

### GetRegionOk

`func (o *PluginsAirnityIpamSubnetCreateRequest) GetRegionOk() (*PatchedSubnetRequestRegion, bool)`

GetRegionOk returns a tuple with the Region field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegion

`func (o *PluginsAirnityIpamSubnetCreateRequest) SetRegion(v PatchedSubnetRequestRegion)`

SetRegion sets Region field to given value.

### HasRegion

`func (o *PluginsAirnityIpamSubnetCreateRequest) HasRegion() bool`

HasRegion returns a boolean if a field has been set.

### SetRegionNil

`func (o *PluginsAirnityIpamSubnetCreateRequest) SetRegionNil(b bool)`

 SetRegionNil sets the value for Region to be an explicit nil

### UnsetRegion
`func (o *PluginsAirnityIpamSubnetCreateRequest) UnsetRegion()`

UnsetRegion ensures that no value is present for Region, not even an explicit nil
### GetTenant

`func (o *PluginsAirnityIpamSubnetCreateRequest) GetTenant() PatchedSubnetIPAddressRequestTenant`

GetTenant returns the Tenant field if non-nil, zero value otherwise.

### GetTenantOk

`func (o *PluginsAirnityIpamSubnetCreateRequest) GetTenantOk() (*PatchedSubnetIPAddressRequestTenant, bool)`

GetTenantOk returns a tuple with the Tenant field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTenant

`func (o *PluginsAirnityIpamSubnetCreateRequest) SetTenant(v PatchedSubnetIPAddressRequestTenant)`

SetTenant sets Tenant field to given value.

### HasTenant

`func (o *PluginsAirnityIpamSubnetCreateRequest) HasTenant() bool`

HasTenant returns a boolean if a field has been set.

### SetTenantNil

`func (o *PluginsAirnityIpamSubnetCreateRequest) SetTenantNil(b bool)`

 SetTenantNil sets the value for Tenant to be an explicit nil

### UnsetTenant
`func (o *PluginsAirnityIpamSubnetCreateRequest) UnsetTenant()`

UnsetTenant ensures that no value is present for Tenant, not even an explicit nil
### GetPurpose

`func (o *PluginsAirnityIpamSubnetCreateRequest) GetPurpose() PatchedSubnetRequestPurpose`

GetPurpose returns the Purpose field if non-nil, zero value otherwise.

### GetPurposeOk

`func (o *PluginsAirnityIpamSubnetCreateRequest) GetPurposeOk() (*PatchedSubnetRequestPurpose, bool)`

GetPurposeOk returns a tuple with the Purpose field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPurpose

`func (o *PluginsAirnityIpamSubnetCreateRequest) SetPurpose(v PatchedSubnetRequestPurpose)`

SetPurpose sets Purpose field to given value.

### HasPurpose

`func (o *PluginsAirnityIpamSubnetCreateRequest) HasPurpose() bool`

HasPurpose returns a boolean if a field has been set.

### SetPurposeNil

`func (o *PluginsAirnityIpamSubnetCreateRequest) SetPurposeNil(b bool)`

 SetPurposeNil sets the value for Purpose to be an explicit nil

### UnsetPurpose
`func (o *PluginsAirnityIpamSubnetCreateRequest) UnsetPurpose()`

UnsetPurpose ensures that no value is present for Purpose, not even an explicit nil
### GetDescription

`func (o *PluginsAirnityIpamSubnetCreateRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *PluginsAirnityIpamSubnetCreateRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *PluginsAirnityIpamSubnetCreateRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *PluginsAirnityIpamSubnetCreateRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetComments

`func (o *PluginsAirnityIpamSubnetCreateRequest) GetComments() string`

GetComments returns the Comments field if non-nil, zero value otherwise.

### GetCommentsOk

`func (o *PluginsAirnityIpamSubnetCreateRequest) GetCommentsOk() (*string, bool)`

GetCommentsOk returns a tuple with the Comments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComments

`func (o *PluginsAirnityIpamSubnetCreateRequest) SetComments(v string)`

SetComments sets Comments field to given value.

### HasComments

`func (o *PluginsAirnityIpamSubnetCreateRequest) HasComments() bool`

HasComments returns a boolean if a field has been set.

### GetCustomFields

`func (o *PluginsAirnityIpamSubnetCreateRequest) GetCustomFields() map[string]map[string]interface{}`

GetCustomFields returns the CustomFields field if non-nil, zero value otherwise.

### GetCustomFieldsOk

`func (o *PluginsAirnityIpamSubnetCreateRequest) GetCustomFieldsOk() (*map[string]map[string]interface{}, bool)`

GetCustomFieldsOk returns a tuple with the CustomFields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomFields

`func (o *PluginsAirnityIpamSubnetCreateRequest) SetCustomFields(v map[string]map[string]interface{})`

SetCustomFields sets CustomFields field to given value.

### HasCustomFields

`func (o *PluginsAirnityIpamSubnetCreateRequest) HasCustomFields() bool`

HasCustomFields returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


