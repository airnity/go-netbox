# PatchedBulkSubnetRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** |  | 
**Name** | Pointer to **string** | Name of the Subnet | [optional] 
**Prefixes** | Pointer to [**[]WritableNestedSubnetPrefixRequest**](WritableNestedSubnetPrefixRequest.md) |  | [optional] 
**Vpc** | Pointer to [**NullablePatchedSubnetRequestVpc**](PatchedSubnetRequestVpc.md) |  | [optional] 
**Region** | Pointer to [**NullablePatchedSubnetRequestRegion**](PatchedSubnetRequestRegion.md) |  | [optional] 
**Tenant** | Pointer to [**NullablePatchedSubnetIPAddressRequestTenant**](PatchedSubnetIPAddressRequestTenant.md) |  | [optional] 
**Purpose** | Pointer to [**NullablePatchedSubnetRequestPurpose**](PatchedSubnetRequestPurpose.md) |  | [optional] 
**Metadata** | Pointer to **interface{}** |  | [optional] 
**Hash** | Pointer to **NullableString** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**Comments** | Pointer to **string** |  | [optional] 
**CustomFields** | Pointer to **map[string]interface{}** |  | [optional] 

## Methods

### NewPatchedBulkSubnetRequest

`func NewPatchedBulkSubnetRequest(id int32, ) *PatchedBulkSubnetRequest`

NewPatchedBulkSubnetRequest instantiates a new PatchedBulkSubnetRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPatchedBulkSubnetRequestWithDefaults

`func NewPatchedBulkSubnetRequestWithDefaults() *PatchedBulkSubnetRequest`

NewPatchedBulkSubnetRequestWithDefaults instantiates a new PatchedBulkSubnetRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *PatchedBulkSubnetRequest) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *PatchedBulkSubnetRequest) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *PatchedBulkSubnetRequest) SetId(v int32)`

SetId sets Id field to given value.


### GetName

`func (o *PatchedBulkSubnetRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *PatchedBulkSubnetRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *PatchedBulkSubnetRequest) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *PatchedBulkSubnetRequest) HasName() bool`

HasName returns a boolean if a field has been set.

### GetPrefixes

`func (o *PatchedBulkSubnetRequest) GetPrefixes() []WritableNestedSubnetPrefixRequest`

GetPrefixes returns the Prefixes field if non-nil, zero value otherwise.

### GetPrefixesOk

`func (o *PatchedBulkSubnetRequest) GetPrefixesOk() (*[]WritableNestedSubnetPrefixRequest, bool)`

GetPrefixesOk returns a tuple with the Prefixes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefixes

`func (o *PatchedBulkSubnetRequest) SetPrefixes(v []WritableNestedSubnetPrefixRequest)`

SetPrefixes sets Prefixes field to given value.

### HasPrefixes

`func (o *PatchedBulkSubnetRequest) HasPrefixes() bool`

HasPrefixes returns a boolean if a field has been set.

### GetVpc

`func (o *PatchedBulkSubnetRequest) GetVpc() PatchedSubnetRequestVpc`

GetVpc returns the Vpc field if non-nil, zero value otherwise.

### GetVpcOk

`func (o *PatchedBulkSubnetRequest) GetVpcOk() (*PatchedSubnetRequestVpc, bool)`

GetVpcOk returns a tuple with the Vpc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVpc

`func (o *PatchedBulkSubnetRequest) SetVpc(v PatchedSubnetRequestVpc)`

SetVpc sets Vpc field to given value.

### HasVpc

`func (o *PatchedBulkSubnetRequest) HasVpc() bool`

HasVpc returns a boolean if a field has been set.

### SetVpcNil

`func (o *PatchedBulkSubnetRequest) SetVpcNil(b bool)`

 SetVpcNil sets the value for Vpc to be an explicit nil

### UnsetVpc
`func (o *PatchedBulkSubnetRequest) UnsetVpc()`

UnsetVpc ensures that no value is present for Vpc, not even an explicit nil
### GetRegion

`func (o *PatchedBulkSubnetRequest) GetRegion() PatchedSubnetRequestRegion`

GetRegion returns the Region field if non-nil, zero value otherwise.

### GetRegionOk

`func (o *PatchedBulkSubnetRequest) GetRegionOk() (*PatchedSubnetRequestRegion, bool)`

GetRegionOk returns a tuple with the Region field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegion

`func (o *PatchedBulkSubnetRequest) SetRegion(v PatchedSubnetRequestRegion)`

SetRegion sets Region field to given value.

### HasRegion

`func (o *PatchedBulkSubnetRequest) HasRegion() bool`

HasRegion returns a boolean if a field has been set.

### SetRegionNil

`func (o *PatchedBulkSubnetRequest) SetRegionNil(b bool)`

 SetRegionNil sets the value for Region to be an explicit nil

### UnsetRegion
`func (o *PatchedBulkSubnetRequest) UnsetRegion()`

UnsetRegion ensures that no value is present for Region, not even an explicit nil
### GetTenant

`func (o *PatchedBulkSubnetRequest) GetTenant() PatchedSubnetIPAddressRequestTenant`

GetTenant returns the Tenant field if non-nil, zero value otherwise.

### GetTenantOk

`func (o *PatchedBulkSubnetRequest) GetTenantOk() (*PatchedSubnetIPAddressRequestTenant, bool)`

GetTenantOk returns a tuple with the Tenant field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTenant

`func (o *PatchedBulkSubnetRequest) SetTenant(v PatchedSubnetIPAddressRequestTenant)`

SetTenant sets Tenant field to given value.

### HasTenant

`func (o *PatchedBulkSubnetRequest) HasTenant() bool`

HasTenant returns a boolean if a field has been set.

### SetTenantNil

`func (o *PatchedBulkSubnetRequest) SetTenantNil(b bool)`

 SetTenantNil sets the value for Tenant to be an explicit nil

### UnsetTenant
`func (o *PatchedBulkSubnetRequest) UnsetTenant()`

UnsetTenant ensures that no value is present for Tenant, not even an explicit nil
### GetPurpose

`func (o *PatchedBulkSubnetRequest) GetPurpose() PatchedSubnetRequestPurpose`

GetPurpose returns the Purpose field if non-nil, zero value otherwise.

### GetPurposeOk

`func (o *PatchedBulkSubnetRequest) GetPurposeOk() (*PatchedSubnetRequestPurpose, bool)`

GetPurposeOk returns a tuple with the Purpose field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPurpose

`func (o *PatchedBulkSubnetRequest) SetPurpose(v PatchedSubnetRequestPurpose)`

SetPurpose sets Purpose field to given value.

### HasPurpose

`func (o *PatchedBulkSubnetRequest) HasPurpose() bool`

HasPurpose returns a boolean if a field has been set.

### SetPurposeNil

`func (o *PatchedBulkSubnetRequest) SetPurposeNil(b bool)`

 SetPurposeNil sets the value for Purpose to be an explicit nil

### UnsetPurpose
`func (o *PatchedBulkSubnetRequest) UnsetPurpose()`

UnsetPurpose ensures that no value is present for Purpose, not even an explicit nil
### GetMetadata

`func (o *PatchedBulkSubnetRequest) GetMetadata() interface{}`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *PatchedBulkSubnetRequest) GetMetadataOk() (*interface{}, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *PatchedBulkSubnetRequest) SetMetadata(v interface{})`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *PatchedBulkSubnetRequest) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### SetMetadataNil

`func (o *PatchedBulkSubnetRequest) SetMetadataNil(b bool)`

 SetMetadataNil sets the value for Metadata to be an explicit nil

### UnsetMetadata
`func (o *PatchedBulkSubnetRequest) UnsetMetadata()`

UnsetMetadata ensures that no value is present for Metadata, not even an explicit nil
### GetHash

`func (o *PatchedBulkSubnetRequest) GetHash() string`

GetHash returns the Hash field if non-nil, zero value otherwise.

### GetHashOk

`func (o *PatchedBulkSubnetRequest) GetHashOk() (*string, bool)`

GetHashOk returns a tuple with the Hash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHash

`func (o *PatchedBulkSubnetRequest) SetHash(v string)`

SetHash sets Hash field to given value.

### HasHash

`func (o *PatchedBulkSubnetRequest) HasHash() bool`

HasHash returns a boolean if a field has been set.

### SetHashNil

`func (o *PatchedBulkSubnetRequest) SetHashNil(b bool)`

 SetHashNil sets the value for Hash to be an explicit nil

### UnsetHash
`func (o *PatchedBulkSubnetRequest) UnsetHash()`

UnsetHash ensures that no value is present for Hash, not even an explicit nil
### GetDescription

`func (o *PatchedBulkSubnetRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *PatchedBulkSubnetRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *PatchedBulkSubnetRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *PatchedBulkSubnetRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetComments

`func (o *PatchedBulkSubnetRequest) GetComments() string`

GetComments returns the Comments field if non-nil, zero value otherwise.

### GetCommentsOk

`func (o *PatchedBulkSubnetRequest) GetCommentsOk() (*string, bool)`

GetCommentsOk returns a tuple with the Comments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComments

`func (o *PatchedBulkSubnetRequest) SetComments(v string)`

SetComments sets Comments field to given value.

### HasComments

`func (o *PatchedBulkSubnetRequest) HasComments() bool`

HasComments returns a boolean if a field has been set.

### GetCustomFields

`func (o *PatchedBulkSubnetRequest) GetCustomFields() map[string]interface{}`

GetCustomFields returns the CustomFields field if non-nil, zero value otherwise.

### GetCustomFieldsOk

`func (o *PatchedBulkSubnetRequest) GetCustomFieldsOk() (*map[string]interface{}, bool)`

GetCustomFieldsOk returns a tuple with the CustomFields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomFields

`func (o *PatchedBulkSubnetRequest) SetCustomFields(v map[string]interface{})`

SetCustomFields sets CustomFields field to given value.

### HasCustomFields

`func (o *PatchedBulkSubnetRequest) HasCustomFields() bool`

HasCustomFields returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


