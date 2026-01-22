# PatchedSubnetIPAddressRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Address** | Pointer to **string** |  | [optional] 
**Vpc** | Pointer to [**NullablePatchedSubnetIPAddressRequestVpc**](PatchedSubnetIPAddressRequestVpc.md) |  | [optional] 
**Country** | Pointer to [**NullablePatchedSubnetIPAddressRequestCountry**](PatchedSubnetIPAddressRequestCountry.md) |  | [optional] 
**SubnetPrefix** | Pointer to **int32** | The subnet prefix this IP belongs to | [optional] 
**Tenant** | Pointer to [**NullablePatchedSubnetIPAddressRequestTenant**](PatchedSubnetIPAddressRequestTenant.md) |  | [optional] 
**Status** | Pointer to [**PatchedSubnetIPAddressRequestStatus**](PatchedSubnetIPAddressRequestStatus.md) |  | [optional] 
**Role** | Pointer to [**PatchedSubnetIPAddressRequestRole**](PatchedSubnetIPAddressRequestRole.md) |  | [optional] 
**NatInside** | Pointer to [**NullableNestedSubnetIPAddressRequest**](NestedSubnetIPAddressRequest.md) |  | [optional] 
**DnsName** | Pointer to **string** | Hostname or FQDN (not case-sensitive) | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**Comments** | Pointer to **string** |  | [optional] 
**Tags** | Pointer to [**[]NestedTagRequest**](NestedTagRequest.md) |  | [optional] 
**CustomFields** | Pointer to **map[string]interface{}** |  | [optional] 

## Methods

### NewPatchedSubnetIPAddressRequest

`func NewPatchedSubnetIPAddressRequest() *PatchedSubnetIPAddressRequest`

NewPatchedSubnetIPAddressRequest instantiates a new PatchedSubnetIPAddressRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPatchedSubnetIPAddressRequestWithDefaults

`func NewPatchedSubnetIPAddressRequestWithDefaults() *PatchedSubnetIPAddressRequest`

NewPatchedSubnetIPAddressRequestWithDefaults instantiates a new PatchedSubnetIPAddressRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAddress

`func (o *PatchedSubnetIPAddressRequest) GetAddress() string`

GetAddress returns the Address field if non-nil, zero value otherwise.

### GetAddressOk

`func (o *PatchedSubnetIPAddressRequest) GetAddressOk() (*string, bool)`

GetAddressOk returns a tuple with the Address field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddress

`func (o *PatchedSubnetIPAddressRequest) SetAddress(v string)`

SetAddress sets Address field to given value.

### HasAddress

`func (o *PatchedSubnetIPAddressRequest) HasAddress() bool`

HasAddress returns a boolean if a field has been set.

### GetVpc

`func (o *PatchedSubnetIPAddressRequest) GetVpc() PatchedSubnetIPAddressRequestVpc`

GetVpc returns the Vpc field if non-nil, zero value otherwise.

### GetVpcOk

`func (o *PatchedSubnetIPAddressRequest) GetVpcOk() (*PatchedSubnetIPAddressRequestVpc, bool)`

GetVpcOk returns a tuple with the Vpc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVpc

`func (o *PatchedSubnetIPAddressRequest) SetVpc(v PatchedSubnetIPAddressRequestVpc)`

SetVpc sets Vpc field to given value.

### HasVpc

`func (o *PatchedSubnetIPAddressRequest) HasVpc() bool`

HasVpc returns a boolean if a field has been set.

### SetVpcNil

`func (o *PatchedSubnetIPAddressRequest) SetVpcNil(b bool)`

 SetVpcNil sets the value for Vpc to be an explicit nil

### UnsetVpc
`func (o *PatchedSubnetIPAddressRequest) UnsetVpc()`

UnsetVpc ensures that no value is present for Vpc, not even an explicit nil
### GetCountry

`func (o *PatchedSubnetIPAddressRequest) GetCountry() PatchedSubnetIPAddressRequestCountry`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *PatchedSubnetIPAddressRequest) GetCountryOk() (*PatchedSubnetIPAddressRequestCountry, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *PatchedSubnetIPAddressRequest) SetCountry(v PatchedSubnetIPAddressRequestCountry)`

SetCountry sets Country field to given value.

### HasCountry

`func (o *PatchedSubnetIPAddressRequest) HasCountry() bool`

HasCountry returns a boolean if a field has been set.

### SetCountryNil

`func (o *PatchedSubnetIPAddressRequest) SetCountryNil(b bool)`

 SetCountryNil sets the value for Country to be an explicit nil

### UnsetCountry
`func (o *PatchedSubnetIPAddressRequest) UnsetCountry()`

UnsetCountry ensures that no value is present for Country, not even an explicit nil
### GetSubnetPrefix

`func (o *PatchedSubnetIPAddressRequest) GetSubnetPrefix() int32`

GetSubnetPrefix returns the SubnetPrefix field if non-nil, zero value otherwise.

### GetSubnetPrefixOk

`func (o *PatchedSubnetIPAddressRequest) GetSubnetPrefixOk() (*int32, bool)`

GetSubnetPrefixOk returns a tuple with the SubnetPrefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubnetPrefix

`func (o *PatchedSubnetIPAddressRequest) SetSubnetPrefix(v int32)`

SetSubnetPrefix sets SubnetPrefix field to given value.

### HasSubnetPrefix

`func (o *PatchedSubnetIPAddressRequest) HasSubnetPrefix() bool`

HasSubnetPrefix returns a boolean if a field has been set.

### GetTenant

`func (o *PatchedSubnetIPAddressRequest) GetTenant() PatchedSubnetIPAddressRequestTenant`

GetTenant returns the Tenant field if non-nil, zero value otherwise.

### GetTenantOk

`func (o *PatchedSubnetIPAddressRequest) GetTenantOk() (*PatchedSubnetIPAddressRequestTenant, bool)`

GetTenantOk returns a tuple with the Tenant field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTenant

`func (o *PatchedSubnetIPAddressRequest) SetTenant(v PatchedSubnetIPAddressRequestTenant)`

SetTenant sets Tenant field to given value.

### HasTenant

`func (o *PatchedSubnetIPAddressRequest) HasTenant() bool`

HasTenant returns a boolean if a field has been set.

### SetTenantNil

`func (o *PatchedSubnetIPAddressRequest) SetTenantNil(b bool)`

 SetTenantNil sets the value for Tenant to be an explicit nil

### UnsetTenant
`func (o *PatchedSubnetIPAddressRequest) UnsetTenant()`

UnsetTenant ensures that no value is present for Tenant, not even an explicit nil
### GetStatus

`func (o *PatchedSubnetIPAddressRequest) GetStatus() PatchedSubnetIPAddressRequestStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *PatchedSubnetIPAddressRequest) GetStatusOk() (*PatchedSubnetIPAddressRequestStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *PatchedSubnetIPAddressRequest) SetStatus(v PatchedSubnetIPAddressRequestStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *PatchedSubnetIPAddressRequest) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetRole

`func (o *PatchedSubnetIPAddressRequest) GetRole() PatchedSubnetIPAddressRequestRole`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *PatchedSubnetIPAddressRequest) GetRoleOk() (*PatchedSubnetIPAddressRequestRole, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *PatchedSubnetIPAddressRequest) SetRole(v PatchedSubnetIPAddressRequestRole)`

SetRole sets Role field to given value.

### HasRole

`func (o *PatchedSubnetIPAddressRequest) HasRole() bool`

HasRole returns a boolean if a field has been set.

### GetNatInside

`func (o *PatchedSubnetIPAddressRequest) GetNatInside() NestedSubnetIPAddressRequest`

GetNatInside returns the NatInside field if non-nil, zero value otherwise.

### GetNatInsideOk

`func (o *PatchedSubnetIPAddressRequest) GetNatInsideOk() (*NestedSubnetIPAddressRequest, bool)`

GetNatInsideOk returns a tuple with the NatInside field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNatInside

`func (o *PatchedSubnetIPAddressRequest) SetNatInside(v NestedSubnetIPAddressRequest)`

SetNatInside sets NatInside field to given value.

### HasNatInside

`func (o *PatchedSubnetIPAddressRequest) HasNatInside() bool`

HasNatInside returns a boolean if a field has been set.

### SetNatInsideNil

`func (o *PatchedSubnetIPAddressRequest) SetNatInsideNil(b bool)`

 SetNatInsideNil sets the value for NatInside to be an explicit nil

### UnsetNatInside
`func (o *PatchedSubnetIPAddressRequest) UnsetNatInside()`

UnsetNatInside ensures that no value is present for NatInside, not even an explicit nil
### GetDnsName

`func (o *PatchedSubnetIPAddressRequest) GetDnsName() string`

GetDnsName returns the DnsName field if non-nil, zero value otherwise.

### GetDnsNameOk

`func (o *PatchedSubnetIPAddressRequest) GetDnsNameOk() (*string, bool)`

GetDnsNameOk returns a tuple with the DnsName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDnsName

`func (o *PatchedSubnetIPAddressRequest) SetDnsName(v string)`

SetDnsName sets DnsName field to given value.

### HasDnsName

`func (o *PatchedSubnetIPAddressRequest) HasDnsName() bool`

HasDnsName returns a boolean if a field has been set.

### GetDescription

`func (o *PatchedSubnetIPAddressRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *PatchedSubnetIPAddressRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *PatchedSubnetIPAddressRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *PatchedSubnetIPAddressRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetComments

`func (o *PatchedSubnetIPAddressRequest) GetComments() string`

GetComments returns the Comments field if non-nil, zero value otherwise.

### GetCommentsOk

`func (o *PatchedSubnetIPAddressRequest) GetCommentsOk() (*string, bool)`

GetCommentsOk returns a tuple with the Comments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComments

`func (o *PatchedSubnetIPAddressRequest) SetComments(v string)`

SetComments sets Comments field to given value.

### HasComments

`func (o *PatchedSubnetIPAddressRequest) HasComments() bool`

HasComments returns a boolean if a field has been set.

### GetTags

`func (o *PatchedSubnetIPAddressRequest) GetTags() []NestedTagRequest`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *PatchedSubnetIPAddressRequest) GetTagsOk() (*[]NestedTagRequest, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTags

`func (o *PatchedSubnetIPAddressRequest) SetTags(v []NestedTagRequest)`

SetTags sets Tags field to given value.

### HasTags

`func (o *PatchedSubnetIPAddressRequest) HasTags() bool`

HasTags returns a boolean if a field has been set.

### GetCustomFields

`func (o *PatchedSubnetIPAddressRequest) GetCustomFields() map[string]interface{}`

GetCustomFields returns the CustomFields field if non-nil, zero value otherwise.

### GetCustomFieldsOk

`func (o *PatchedSubnetIPAddressRequest) GetCustomFieldsOk() (*map[string]interface{}, bool)`

GetCustomFieldsOk returns a tuple with the CustomFields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomFields

`func (o *PatchedSubnetIPAddressRequest) SetCustomFields(v map[string]interface{})`

SetCustomFields sets CustomFields field to given value.

### HasCustomFields

`func (o *PatchedSubnetIPAddressRequest) HasCustomFields() bool`

HasCustomFields returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


