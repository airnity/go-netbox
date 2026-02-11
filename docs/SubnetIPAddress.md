# SubnetIPAddress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** |  | [readonly] 
**Url** | **string** |  | [readonly] 
**DisplayUrl** | Pointer to **string** |  | [optional] [readonly] 
**Display** | **string** |  | [readonly] 
**Family** | **int32** |  | [readonly] 
**Address** | **string** |  | 
**Vpc** | Pointer to [**NullableBriefVPC**](BriefVPC.md) |  | [optional] 
**Country** | Pointer to [**PatchedSubnetIPAddressRequestCountry**](PatchedSubnetIPAddressRequestCountry.md) |  | [optional] 
**SubnetPrefix** | **int32** | The subnet prefix this IP belongs to | 
**Tenant** | Pointer to [**NullableBriefTenant**](BriefTenant.md) |  | [optional] 
**Status** | Pointer to [**PatchedSubnetIPAddressRequestStatus**](PatchedSubnetIPAddressRequestStatus.md) |  | [optional] 
**Role** | Pointer to [**PatchedSubnetIPAddressRequestRole**](PatchedSubnetIPAddressRequestRole.md) |  | [optional] 
**NatInside** | Pointer to [**NullableNestedSubnetIPAddress**](NestedSubnetIPAddress.md) |  | [optional] 
**NatOutside** | [**[]NestedSubnetIPAddress**](NestedSubnetIPAddress.md) |  | [readonly] 
**DnsName** | Pointer to **string** | Hostname or FQDN (not case-sensitive) | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**Comments** | Pointer to **string** |  | [optional] 
**Tags** | Pointer to [**[]NestedTag**](NestedTag.md) |  | [optional] 
**CustomFields** | Pointer to **map[string]interface{}** |  | [optional] 
**Created** | Pointer to **NullableTime** |  | [optional] [readonly] 
**LastUpdated** | Pointer to **NullableTime** |  | [optional] [readonly] 
**Subnet** | **map[string]interface{}** | Return the subnet with its associated prefix. | [readonly] 

## Methods

### NewSubnetIPAddress

`func NewSubnetIPAddress(id int32, url string, display string, family int32, address string, subnetPrefix int32, natOutside []NestedSubnetIPAddress, subnet map[string]interface{}, ) *SubnetIPAddress`

NewSubnetIPAddress instantiates a new SubnetIPAddress object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSubnetIPAddressWithDefaults

`func NewSubnetIPAddressWithDefaults() *SubnetIPAddress`

NewSubnetIPAddressWithDefaults instantiates a new SubnetIPAddress object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SubnetIPAddress) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SubnetIPAddress) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SubnetIPAddress) SetId(v int32)`

SetId sets Id field to given value.


### GetUrl

`func (o *SubnetIPAddress) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *SubnetIPAddress) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *SubnetIPAddress) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetDisplayUrl

`func (o *SubnetIPAddress) GetDisplayUrl() string`

GetDisplayUrl returns the DisplayUrl field if non-nil, zero value otherwise.

### GetDisplayUrlOk

`func (o *SubnetIPAddress) GetDisplayUrlOk() (*string, bool)`

GetDisplayUrlOk returns a tuple with the DisplayUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayUrl

`func (o *SubnetIPAddress) SetDisplayUrl(v string)`

SetDisplayUrl sets DisplayUrl field to given value.

### HasDisplayUrl

`func (o *SubnetIPAddress) HasDisplayUrl() bool`

HasDisplayUrl returns a boolean if a field has been set.

### GetDisplay

`func (o *SubnetIPAddress) GetDisplay() string`

GetDisplay returns the Display field if non-nil, zero value otherwise.

### GetDisplayOk

`func (o *SubnetIPAddress) GetDisplayOk() (*string, bool)`

GetDisplayOk returns a tuple with the Display field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplay

`func (o *SubnetIPAddress) SetDisplay(v string)`

SetDisplay sets Display field to given value.


### GetFamily

`func (o *SubnetIPAddress) GetFamily() int32`

GetFamily returns the Family field if non-nil, zero value otherwise.

### GetFamilyOk

`func (o *SubnetIPAddress) GetFamilyOk() (*int32, bool)`

GetFamilyOk returns a tuple with the Family field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFamily

`func (o *SubnetIPAddress) SetFamily(v int32)`

SetFamily sets Family field to given value.


### GetAddress

`func (o *SubnetIPAddress) GetAddress() string`

GetAddress returns the Address field if non-nil, zero value otherwise.

### GetAddressOk

`func (o *SubnetIPAddress) GetAddressOk() (*string, bool)`

GetAddressOk returns a tuple with the Address field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddress

`func (o *SubnetIPAddress) SetAddress(v string)`

SetAddress sets Address field to given value.


### GetVpc

`func (o *SubnetIPAddress) GetVpc() BriefVPC`

GetVpc returns the Vpc field if non-nil, zero value otherwise.

### GetVpcOk

`func (o *SubnetIPAddress) GetVpcOk() (*BriefVPC, bool)`

GetVpcOk returns a tuple with the Vpc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVpc

`func (o *SubnetIPAddress) SetVpc(v BriefVPC)`

SetVpc sets Vpc field to given value.

### HasVpc

`func (o *SubnetIPAddress) HasVpc() bool`

HasVpc returns a boolean if a field has been set.

### SetVpcNil

`func (o *SubnetIPAddress) SetVpcNil(b bool)`

 SetVpcNil sets the value for Vpc to be an explicit nil

### UnsetVpc
`func (o *SubnetIPAddress) UnsetVpc()`

UnsetVpc ensures that no value is present for Vpc, not even an explicit nil
### GetCountry

`func (o *SubnetIPAddress) GetCountry() PatchedSubnetIPAddressRequestCountry`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *SubnetIPAddress) GetCountryOk() (*PatchedSubnetIPAddressRequestCountry, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *SubnetIPAddress) SetCountry(v PatchedSubnetIPAddressRequestCountry)`

SetCountry sets Country field to given value.

### HasCountry

`func (o *SubnetIPAddress) HasCountry() bool`

HasCountry returns a boolean if a field has been set.

### GetSubnetPrefix

`func (o *SubnetIPAddress) GetSubnetPrefix() int32`

GetSubnetPrefix returns the SubnetPrefix field if non-nil, zero value otherwise.

### GetSubnetPrefixOk

`func (o *SubnetIPAddress) GetSubnetPrefixOk() (*int32, bool)`

GetSubnetPrefixOk returns a tuple with the SubnetPrefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubnetPrefix

`func (o *SubnetIPAddress) SetSubnetPrefix(v int32)`

SetSubnetPrefix sets SubnetPrefix field to given value.


### GetTenant

`func (o *SubnetIPAddress) GetTenant() BriefTenant`

GetTenant returns the Tenant field if non-nil, zero value otherwise.

### GetTenantOk

`func (o *SubnetIPAddress) GetTenantOk() (*BriefTenant, bool)`

GetTenantOk returns a tuple with the Tenant field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTenant

`func (o *SubnetIPAddress) SetTenant(v BriefTenant)`

SetTenant sets Tenant field to given value.

### HasTenant

`func (o *SubnetIPAddress) HasTenant() bool`

HasTenant returns a boolean if a field has been set.

### SetTenantNil

`func (o *SubnetIPAddress) SetTenantNil(b bool)`

 SetTenantNil sets the value for Tenant to be an explicit nil

### UnsetTenant
`func (o *SubnetIPAddress) UnsetTenant()`

UnsetTenant ensures that no value is present for Tenant, not even an explicit nil
### GetStatus

`func (o *SubnetIPAddress) GetStatus() PatchedSubnetIPAddressRequestStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *SubnetIPAddress) GetStatusOk() (*PatchedSubnetIPAddressRequestStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *SubnetIPAddress) SetStatus(v PatchedSubnetIPAddressRequestStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *SubnetIPAddress) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetRole

`func (o *SubnetIPAddress) GetRole() PatchedSubnetIPAddressRequestRole`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *SubnetIPAddress) GetRoleOk() (*PatchedSubnetIPAddressRequestRole, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *SubnetIPAddress) SetRole(v PatchedSubnetIPAddressRequestRole)`

SetRole sets Role field to given value.

### HasRole

`func (o *SubnetIPAddress) HasRole() bool`

HasRole returns a boolean if a field has been set.

### GetNatInside

`func (o *SubnetIPAddress) GetNatInside() NestedSubnetIPAddress`

GetNatInside returns the NatInside field if non-nil, zero value otherwise.

### GetNatInsideOk

`func (o *SubnetIPAddress) GetNatInsideOk() (*NestedSubnetIPAddress, bool)`

GetNatInsideOk returns a tuple with the NatInside field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNatInside

`func (o *SubnetIPAddress) SetNatInside(v NestedSubnetIPAddress)`

SetNatInside sets NatInside field to given value.

### HasNatInside

`func (o *SubnetIPAddress) HasNatInside() bool`

HasNatInside returns a boolean if a field has been set.

### SetNatInsideNil

`func (o *SubnetIPAddress) SetNatInsideNil(b bool)`

 SetNatInsideNil sets the value for NatInside to be an explicit nil

### UnsetNatInside
`func (o *SubnetIPAddress) UnsetNatInside()`

UnsetNatInside ensures that no value is present for NatInside, not even an explicit nil
### GetNatOutside

`func (o *SubnetIPAddress) GetNatOutside() []NestedSubnetIPAddress`

GetNatOutside returns the NatOutside field if non-nil, zero value otherwise.

### GetNatOutsideOk

`func (o *SubnetIPAddress) GetNatOutsideOk() (*[]NestedSubnetIPAddress, bool)`

GetNatOutsideOk returns a tuple with the NatOutside field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNatOutside

`func (o *SubnetIPAddress) SetNatOutside(v []NestedSubnetIPAddress)`

SetNatOutside sets NatOutside field to given value.


### GetDnsName

`func (o *SubnetIPAddress) GetDnsName() string`

GetDnsName returns the DnsName field if non-nil, zero value otherwise.

### GetDnsNameOk

`func (o *SubnetIPAddress) GetDnsNameOk() (*string, bool)`

GetDnsNameOk returns a tuple with the DnsName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDnsName

`func (o *SubnetIPAddress) SetDnsName(v string)`

SetDnsName sets DnsName field to given value.

### HasDnsName

`func (o *SubnetIPAddress) HasDnsName() bool`

HasDnsName returns a boolean if a field has been set.

### GetDescription

`func (o *SubnetIPAddress) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *SubnetIPAddress) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *SubnetIPAddress) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *SubnetIPAddress) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetComments

`func (o *SubnetIPAddress) GetComments() string`

GetComments returns the Comments field if non-nil, zero value otherwise.

### GetCommentsOk

`func (o *SubnetIPAddress) GetCommentsOk() (*string, bool)`

GetCommentsOk returns a tuple with the Comments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComments

`func (o *SubnetIPAddress) SetComments(v string)`

SetComments sets Comments field to given value.

### HasComments

`func (o *SubnetIPAddress) HasComments() bool`

HasComments returns a boolean if a field has been set.

### GetTags

`func (o *SubnetIPAddress) GetTags() []NestedTag`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *SubnetIPAddress) GetTagsOk() (*[]NestedTag, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTags

`func (o *SubnetIPAddress) SetTags(v []NestedTag)`

SetTags sets Tags field to given value.

### HasTags

`func (o *SubnetIPAddress) HasTags() bool`

HasTags returns a boolean if a field has been set.

### GetCustomFields

`func (o *SubnetIPAddress) GetCustomFields() map[string]interface{}`

GetCustomFields returns the CustomFields field if non-nil, zero value otherwise.

### GetCustomFieldsOk

`func (o *SubnetIPAddress) GetCustomFieldsOk() (*map[string]interface{}, bool)`

GetCustomFieldsOk returns a tuple with the CustomFields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomFields

`func (o *SubnetIPAddress) SetCustomFields(v map[string]interface{})`

SetCustomFields sets CustomFields field to given value.

### HasCustomFields

`func (o *SubnetIPAddress) HasCustomFields() bool`

HasCustomFields returns a boolean if a field has been set.

### GetCreated

`func (o *SubnetIPAddress) GetCreated() time.Time`

GetCreated returns the Created field if non-nil, zero value otherwise.

### GetCreatedOk

`func (o *SubnetIPAddress) GetCreatedOk() (*time.Time, bool)`

GetCreatedOk returns a tuple with the Created field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreated

`func (o *SubnetIPAddress) SetCreated(v time.Time)`

SetCreated sets Created field to given value.

### HasCreated

`func (o *SubnetIPAddress) HasCreated() bool`

HasCreated returns a boolean if a field has been set.

### SetCreatedNil

`func (o *SubnetIPAddress) SetCreatedNil(b bool)`

 SetCreatedNil sets the value for Created to be an explicit nil

### UnsetCreated
`func (o *SubnetIPAddress) UnsetCreated()`

UnsetCreated ensures that no value is present for Created, not even an explicit nil
### GetLastUpdated

`func (o *SubnetIPAddress) GetLastUpdated() time.Time`

GetLastUpdated returns the LastUpdated field if non-nil, zero value otherwise.

### GetLastUpdatedOk

`func (o *SubnetIPAddress) GetLastUpdatedOk() (*time.Time, bool)`

GetLastUpdatedOk returns a tuple with the LastUpdated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastUpdated

`func (o *SubnetIPAddress) SetLastUpdated(v time.Time)`

SetLastUpdated sets LastUpdated field to given value.

### HasLastUpdated

`func (o *SubnetIPAddress) HasLastUpdated() bool`

HasLastUpdated returns a boolean if a field has been set.

### SetLastUpdatedNil

`func (o *SubnetIPAddress) SetLastUpdatedNil(b bool)`

 SetLastUpdatedNil sets the value for LastUpdated to be an explicit nil

### UnsetLastUpdated
`func (o *SubnetIPAddress) UnsetLastUpdated()`

UnsetLastUpdated ensures that no value is present for LastUpdated, not even an explicit nil
### GetSubnet

`func (o *SubnetIPAddress) GetSubnet() map[string]interface{}`

GetSubnet returns the Subnet field if non-nil, zero value otherwise.

### GetSubnetOk

`func (o *SubnetIPAddress) GetSubnetOk() (*map[string]interface{}, bool)`

GetSubnetOk returns a tuple with the Subnet field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubnet

`func (o *SubnetIPAddress) SetSubnet(v map[string]interface{})`

SetSubnet sets Subnet field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


