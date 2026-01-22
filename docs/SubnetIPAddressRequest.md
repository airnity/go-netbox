# SubnetIPAddressRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Address** | **string** |  | 
**Vpc** | Pointer to [**NullablePatchedSubnetIPAddressRequestVpc**](PatchedSubnetIPAddressRequestVpc.md) |  | [optional] 
**Country** | Pointer to [**NullablePatchedSubnetIPAddressRequestCountry**](PatchedSubnetIPAddressRequestCountry.md) |  | [optional] 
**SubnetPrefix** | **int32** | The subnet prefix this IP belongs to | 
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

### NewSubnetIPAddressRequest

`func NewSubnetIPAddressRequest(address string, subnetPrefix int32, ) *SubnetIPAddressRequest`

NewSubnetIPAddressRequest instantiates a new SubnetIPAddressRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSubnetIPAddressRequestWithDefaults

`func NewSubnetIPAddressRequestWithDefaults() *SubnetIPAddressRequest`

NewSubnetIPAddressRequestWithDefaults instantiates a new SubnetIPAddressRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAddress

`func (o *SubnetIPAddressRequest) GetAddress() string`

GetAddress returns the Address field if non-nil, zero value otherwise.

### GetAddressOk

`func (o *SubnetIPAddressRequest) GetAddressOk() (*string, bool)`

GetAddressOk returns a tuple with the Address field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddress

`func (o *SubnetIPAddressRequest) SetAddress(v string)`

SetAddress sets Address field to given value.


### GetVpc

`func (o *SubnetIPAddressRequest) GetVpc() PatchedSubnetIPAddressRequestVpc`

GetVpc returns the Vpc field if non-nil, zero value otherwise.

### GetVpcOk

`func (o *SubnetIPAddressRequest) GetVpcOk() (*PatchedSubnetIPAddressRequestVpc, bool)`

GetVpcOk returns a tuple with the Vpc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVpc

`func (o *SubnetIPAddressRequest) SetVpc(v PatchedSubnetIPAddressRequestVpc)`

SetVpc sets Vpc field to given value.

### HasVpc

`func (o *SubnetIPAddressRequest) HasVpc() bool`

HasVpc returns a boolean if a field has been set.

### SetVpcNil

`func (o *SubnetIPAddressRequest) SetVpcNil(b bool)`

 SetVpcNil sets the value for Vpc to be an explicit nil

### UnsetVpc
`func (o *SubnetIPAddressRequest) UnsetVpc()`

UnsetVpc ensures that no value is present for Vpc, not even an explicit nil
### GetCountry

`func (o *SubnetIPAddressRequest) GetCountry() PatchedSubnetIPAddressRequestCountry`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *SubnetIPAddressRequest) GetCountryOk() (*PatchedSubnetIPAddressRequestCountry, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *SubnetIPAddressRequest) SetCountry(v PatchedSubnetIPAddressRequestCountry)`

SetCountry sets Country field to given value.

### HasCountry

`func (o *SubnetIPAddressRequest) HasCountry() bool`

HasCountry returns a boolean if a field has been set.

### SetCountryNil

`func (o *SubnetIPAddressRequest) SetCountryNil(b bool)`

 SetCountryNil sets the value for Country to be an explicit nil

### UnsetCountry
`func (o *SubnetIPAddressRequest) UnsetCountry()`

UnsetCountry ensures that no value is present for Country, not even an explicit nil
### GetSubnetPrefix

`func (o *SubnetIPAddressRequest) GetSubnetPrefix() int32`

GetSubnetPrefix returns the SubnetPrefix field if non-nil, zero value otherwise.

### GetSubnetPrefixOk

`func (o *SubnetIPAddressRequest) GetSubnetPrefixOk() (*int32, bool)`

GetSubnetPrefixOk returns a tuple with the SubnetPrefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubnetPrefix

`func (o *SubnetIPAddressRequest) SetSubnetPrefix(v int32)`

SetSubnetPrefix sets SubnetPrefix field to given value.


### GetTenant

`func (o *SubnetIPAddressRequest) GetTenant() PatchedSubnetIPAddressRequestTenant`

GetTenant returns the Tenant field if non-nil, zero value otherwise.

### GetTenantOk

`func (o *SubnetIPAddressRequest) GetTenantOk() (*PatchedSubnetIPAddressRequestTenant, bool)`

GetTenantOk returns a tuple with the Tenant field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTenant

`func (o *SubnetIPAddressRequest) SetTenant(v PatchedSubnetIPAddressRequestTenant)`

SetTenant sets Tenant field to given value.

### HasTenant

`func (o *SubnetIPAddressRequest) HasTenant() bool`

HasTenant returns a boolean if a field has been set.

### SetTenantNil

`func (o *SubnetIPAddressRequest) SetTenantNil(b bool)`

 SetTenantNil sets the value for Tenant to be an explicit nil

### UnsetTenant
`func (o *SubnetIPAddressRequest) UnsetTenant()`

UnsetTenant ensures that no value is present for Tenant, not even an explicit nil
### GetStatus

`func (o *SubnetIPAddressRequest) GetStatus() PatchedSubnetIPAddressRequestStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *SubnetIPAddressRequest) GetStatusOk() (*PatchedSubnetIPAddressRequestStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *SubnetIPAddressRequest) SetStatus(v PatchedSubnetIPAddressRequestStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *SubnetIPAddressRequest) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetRole

`func (o *SubnetIPAddressRequest) GetRole() PatchedSubnetIPAddressRequestRole`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *SubnetIPAddressRequest) GetRoleOk() (*PatchedSubnetIPAddressRequestRole, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *SubnetIPAddressRequest) SetRole(v PatchedSubnetIPAddressRequestRole)`

SetRole sets Role field to given value.

### HasRole

`func (o *SubnetIPAddressRequest) HasRole() bool`

HasRole returns a boolean if a field has been set.

### GetNatInside

`func (o *SubnetIPAddressRequest) GetNatInside() NestedSubnetIPAddressRequest`

GetNatInside returns the NatInside field if non-nil, zero value otherwise.

### GetNatInsideOk

`func (o *SubnetIPAddressRequest) GetNatInsideOk() (*NestedSubnetIPAddressRequest, bool)`

GetNatInsideOk returns a tuple with the NatInside field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNatInside

`func (o *SubnetIPAddressRequest) SetNatInside(v NestedSubnetIPAddressRequest)`

SetNatInside sets NatInside field to given value.

### HasNatInside

`func (o *SubnetIPAddressRequest) HasNatInside() bool`

HasNatInside returns a boolean if a field has been set.

### SetNatInsideNil

`func (o *SubnetIPAddressRequest) SetNatInsideNil(b bool)`

 SetNatInsideNil sets the value for NatInside to be an explicit nil

### UnsetNatInside
`func (o *SubnetIPAddressRequest) UnsetNatInside()`

UnsetNatInside ensures that no value is present for NatInside, not even an explicit nil
### GetDnsName

`func (o *SubnetIPAddressRequest) GetDnsName() string`

GetDnsName returns the DnsName field if non-nil, zero value otherwise.

### GetDnsNameOk

`func (o *SubnetIPAddressRequest) GetDnsNameOk() (*string, bool)`

GetDnsNameOk returns a tuple with the DnsName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDnsName

`func (o *SubnetIPAddressRequest) SetDnsName(v string)`

SetDnsName sets DnsName field to given value.

### HasDnsName

`func (o *SubnetIPAddressRequest) HasDnsName() bool`

HasDnsName returns a boolean if a field has been set.

### GetDescription

`func (o *SubnetIPAddressRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *SubnetIPAddressRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *SubnetIPAddressRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *SubnetIPAddressRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetComments

`func (o *SubnetIPAddressRequest) GetComments() string`

GetComments returns the Comments field if non-nil, zero value otherwise.

### GetCommentsOk

`func (o *SubnetIPAddressRequest) GetCommentsOk() (*string, bool)`

GetCommentsOk returns a tuple with the Comments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComments

`func (o *SubnetIPAddressRequest) SetComments(v string)`

SetComments sets Comments field to given value.

### HasComments

`func (o *SubnetIPAddressRequest) HasComments() bool`

HasComments returns a boolean if a field has been set.

### GetTags

`func (o *SubnetIPAddressRequest) GetTags() []NestedTagRequest`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *SubnetIPAddressRequest) GetTagsOk() (*[]NestedTagRequest, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTags

`func (o *SubnetIPAddressRequest) SetTags(v []NestedTagRequest)`

SetTags sets Tags field to given value.

### HasTags

`func (o *SubnetIPAddressRequest) HasTags() bool`

HasTags returns a boolean if a field has been set.

### GetCustomFields

`func (o *SubnetIPAddressRequest) GetCustomFields() map[string]interface{}`

GetCustomFields returns the CustomFields field if non-nil, zero value otherwise.

### GetCustomFieldsOk

`func (o *SubnetIPAddressRequest) GetCustomFieldsOk() (*map[string]interface{}, bool)`

GetCustomFieldsOk returns a tuple with the CustomFields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomFields

`func (o *SubnetIPAddressRequest) SetCustomFields(v map[string]interface{})`

SetCustomFields sets CustomFields field to given value.

### HasCustomFields

`func (o *SubnetIPAddressRequest) HasCustomFields() bool`

HasCustomFields returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


