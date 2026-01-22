# Subnet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** |  | [readonly] 
**Url** | **string** |  | [readonly] 
**DisplayUrl** | Pointer to **string** |  | [optional] [readonly] 
**Display** | Pointer to **interface{}** |  | [optional] [readonly] 
**Name** | Pointer to **string** | Name of the Subnet | [optional] 
**Prefixes** | Pointer to [**[]WritableNestedSubnetPrefix**](WritableNestedSubnetPrefix.md) |  | [optional] 
**Vpc** | Pointer to [**NullableBriefNestedVPC**](BriefNestedVPC.md) |  | [optional] 
**Region** | Pointer to [**NullableBriefRegion**](BriefRegion.md) |  | [optional] 
**Tenant** | Pointer to [**NullableBriefTenant**](BriefTenant.md) |  | [optional] 
**Purpose** | Pointer to [**NullableBriefSubnetPurpose**](BriefSubnetPurpose.md) |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**Comments** | Pointer to **string** |  | [optional] 
**CustomFields** | Pointer to **map[string]interface{}** |  | [optional] 
**Created** | Pointer to **NullableTime** |  | [optional] [readonly] 
**LastUpdated** | Pointer to **NullableTime** |  | [optional] [readonly] 

## Methods

### NewSubnet

`func NewSubnet(id int32, url string, ) *Subnet`

NewSubnet instantiates a new Subnet object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSubnetWithDefaults

`func NewSubnetWithDefaults() *Subnet`

NewSubnetWithDefaults instantiates a new Subnet object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *Subnet) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Subnet) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Subnet) SetId(v int32)`

SetId sets Id field to given value.


### GetUrl

`func (o *Subnet) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *Subnet) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *Subnet) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetDisplayUrl

`func (o *Subnet) GetDisplayUrl() string`

GetDisplayUrl returns the DisplayUrl field if non-nil, zero value otherwise.

### GetDisplayUrlOk

`func (o *Subnet) GetDisplayUrlOk() (*string, bool)`

GetDisplayUrlOk returns a tuple with the DisplayUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayUrl

`func (o *Subnet) SetDisplayUrl(v string)`

SetDisplayUrl sets DisplayUrl field to given value.

### HasDisplayUrl

`func (o *Subnet) HasDisplayUrl() bool`

HasDisplayUrl returns a boolean if a field has been set.

### GetDisplay

`func (o *Subnet) GetDisplay() interface{}`

GetDisplay returns the Display field if non-nil, zero value otherwise.

### GetDisplayOk

`func (o *Subnet) GetDisplayOk() (*interface{}, bool)`

GetDisplayOk returns a tuple with the Display field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplay

`func (o *Subnet) SetDisplay(v interface{})`

SetDisplay sets Display field to given value.

### HasDisplay

`func (o *Subnet) HasDisplay() bool`

HasDisplay returns a boolean if a field has been set.

### SetDisplayNil

`func (o *Subnet) SetDisplayNil(b bool)`

 SetDisplayNil sets the value for Display to be an explicit nil

### UnsetDisplay
`func (o *Subnet) UnsetDisplay()`

UnsetDisplay ensures that no value is present for Display, not even an explicit nil
### GetName

`func (o *Subnet) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Subnet) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Subnet) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *Subnet) HasName() bool`

HasName returns a boolean if a field has been set.

### GetPrefixes

`func (o *Subnet) GetPrefixes() []WritableNestedSubnetPrefix`

GetPrefixes returns the Prefixes field if non-nil, zero value otherwise.

### GetPrefixesOk

`func (o *Subnet) GetPrefixesOk() (*[]WritableNestedSubnetPrefix, bool)`

GetPrefixesOk returns a tuple with the Prefixes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefixes

`func (o *Subnet) SetPrefixes(v []WritableNestedSubnetPrefix)`

SetPrefixes sets Prefixes field to given value.

### HasPrefixes

`func (o *Subnet) HasPrefixes() bool`

HasPrefixes returns a boolean if a field has been set.

### GetVpc

`func (o *Subnet) GetVpc() BriefNestedVPC`

GetVpc returns the Vpc field if non-nil, zero value otherwise.

### GetVpcOk

`func (o *Subnet) GetVpcOk() (*BriefNestedVPC, bool)`

GetVpcOk returns a tuple with the Vpc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVpc

`func (o *Subnet) SetVpc(v BriefNestedVPC)`

SetVpc sets Vpc field to given value.

### HasVpc

`func (o *Subnet) HasVpc() bool`

HasVpc returns a boolean if a field has been set.

### SetVpcNil

`func (o *Subnet) SetVpcNil(b bool)`

 SetVpcNil sets the value for Vpc to be an explicit nil

### UnsetVpc
`func (o *Subnet) UnsetVpc()`

UnsetVpc ensures that no value is present for Vpc, not even an explicit nil
### GetRegion

`func (o *Subnet) GetRegion() BriefRegion`

GetRegion returns the Region field if non-nil, zero value otherwise.

### GetRegionOk

`func (o *Subnet) GetRegionOk() (*BriefRegion, bool)`

GetRegionOk returns a tuple with the Region field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegion

`func (o *Subnet) SetRegion(v BriefRegion)`

SetRegion sets Region field to given value.

### HasRegion

`func (o *Subnet) HasRegion() bool`

HasRegion returns a boolean if a field has been set.

### SetRegionNil

`func (o *Subnet) SetRegionNil(b bool)`

 SetRegionNil sets the value for Region to be an explicit nil

### UnsetRegion
`func (o *Subnet) UnsetRegion()`

UnsetRegion ensures that no value is present for Region, not even an explicit nil
### GetTenant

`func (o *Subnet) GetTenant() BriefTenant`

GetTenant returns the Tenant field if non-nil, zero value otherwise.

### GetTenantOk

`func (o *Subnet) GetTenantOk() (*BriefTenant, bool)`

GetTenantOk returns a tuple with the Tenant field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTenant

`func (o *Subnet) SetTenant(v BriefTenant)`

SetTenant sets Tenant field to given value.

### HasTenant

`func (o *Subnet) HasTenant() bool`

HasTenant returns a boolean if a field has been set.

### SetTenantNil

`func (o *Subnet) SetTenantNil(b bool)`

 SetTenantNil sets the value for Tenant to be an explicit nil

### UnsetTenant
`func (o *Subnet) UnsetTenant()`

UnsetTenant ensures that no value is present for Tenant, not even an explicit nil
### GetPurpose

`func (o *Subnet) GetPurpose() BriefSubnetPurpose`

GetPurpose returns the Purpose field if non-nil, zero value otherwise.

### GetPurposeOk

`func (o *Subnet) GetPurposeOk() (*BriefSubnetPurpose, bool)`

GetPurposeOk returns a tuple with the Purpose field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPurpose

`func (o *Subnet) SetPurpose(v BriefSubnetPurpose)`

SetPurpose sets Purpose field to given value.

### HasPurpose

`func (o *Subnet) HasPurpose() bool`

HasPurpose returns a boolean if a field has been set.

### SetPurposeNil

`func (o *Subnet) SetPurposeNil(b bool)`

 SetPurposeNil sets the value for Purpose to be an explicit nil

### UnsetPurpose
`func (o *Subnet) UnsetPurpose()`

UnsetPurpose ensures that no value is present for Purpose, not even an explicit nil
### GetDescription

`func (o *Subnet) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Subnet) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Subnet) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *Subnet) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetComments

`func (o *Subnet) GetComments() string`

GetComments returns the Comments field if non-nil, zero value otherwise.

### GetCommentsOk

`func (o *Subnet) GetCommentsOk() (*string, bool)`

GetCommentsOk returns a tuple with the Comments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComments

`func (o *Subnet) SetComments(v string)`

SetComments sets Comments field to given value.

### HasComments

`func (o *Subnet) HasComments() bool`

HasComments returns a boolean if a field has been set.

### GetCustomFields

`func (o *Subnet) GetCustomFields() map[string]interface{}`

GetCustomFields returns the CustomFields field if non-nil, zero value otherwise.

### GetCustomFieldsOk

`func (o *Subnet) GetCustomFieldsOk() (*map[string]interface{}, bool)`

GetCustomFieldsOk returns a tuple with the CustomFields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomFields

`func (o *Subnet) SetCustomFields(v map[string]interface{})`

SetCustomFields sets CustomFields field to given value.

### HasCustomFields

`func (o *Subnet) HasCustomFields() bool`

HasCustomFields returns a boolean if a field has been set.

### GetCreated

`func (o *Subnet) GetCreated() time.Time`

GetCreated returns the Created field if non-nil, zero value otherwise.

### GetCreatedOk

`func (o *Subnet) GetCreatedOk() (*time.Time, bool)`

GetCreatedOk returns a tuple with the Created field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreated

`func (o *Subnet) SetCreated(v time.Time)`

SetCreated sets Created field to given value.

### HasCreated

`func (o *Subnet) HasCreated() bool`

HasCreated returns a boolean if a field has been set.

### SetCreatedNil

`func (o *Subnet) SetCreatedNil(b bool)`

 SetCreatedNil sets the value for Created to be an explicit nil

### UnsetCreated
`func (o *Subnet) UnsetCreated()`

UnsetCreated ensures that no value is present for Created, not even an explicit nil
### GetLastUpdated

`func (o *Subnet) GetLastUpdated() time.Time`

GetLastUpdated returns the LastUpdated field if non-nil, zero value otherwise.

### GetLastUpdatedOk

`func (o *Subnet) GetLastUpdatedOk() (*time.Time, bool)`

GetLastUpdatedOk returns a tuple with the LastUpdated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastUpdated

`func (o *Subnet) SetLastUpdated(v time.Time)`

SetLastUpdated sets LastUpdated field to given value.

### HasLastUpdated

`func (o *Subnet) HasLastUpdated() bool`

HasLastUpdated returns a boolean if a field has been set.

### SetLastUpdatedNil

`func (o *Subnet) SetLastUpdatedNil(b bool)`

 SetLastUpdatedNil sets the value for LastUpdated to be an explicit nil

### UnsetLastUpdated
`func (o *Subnet) UnsetLastUpdated()`

UnsetLastUpdated ensures that no value is present for LastUpdated, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


