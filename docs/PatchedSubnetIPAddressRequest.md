# PatchedSubnetIPAddressRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Address** | Pointer to **string** |  | [optional] 
**Vpc** | Pointer to [**NullablePatchedSubnetIPAddressRequestVpc**](PatchedSubnetIPAddressRequestVpc.md) |  | [optional] 
**Country** | Pointer to [**PatchedSubnetIPAddressRequestCountry**](PatchedSubnetIPAddressRequestCountry.md) |  | [optional] 
**ClaimedBy** | Pointer to **NullableString** |  | [optional] 
**SubnetPrefix** | Pointer to **int32** | The subnet prefix this IP belongs to | [optional] 
**Tenant** | Pointer to [**NullablePatchedSubnetIPAddressRequestTenant**](PatchedSubnetIPAddressRequestTenant.md) |  | [optional] 
**Status** | Pointer to [**PatchedSubnetIPAddressRequestStatus**](PatchedSubnetIPAddressRequestStatus.md) |  | [optional] 
**Role** | Pointer to [**PatchedSubnetIPAddressRequestRole**](PatchedSubnetIPAddressRequestRole.md) |  | [optional] 
**NatInside** | Pointer to [**NullableNestedSubnetIPAddressRequest**](NestedSubnetIPAddressRequest.md) |  | [optional] 
**DnsName** | Pointer to **string** | Hostname or FQDN (not case-sensitive) | [optional] 
**Metadata** | Pointer to **interface{}** |  | [optional] 
**Hash** | Pointer to **NullableString** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**Comments** | Pointer to **string** |  | [optional] 
**Tags** | Pointer to [**[]NestedTagRequest**](NestedTagRequest.md) |  | [optional] 
**CustomFields** | Pointer to **map[string]interface{}** |  | [optional] 
**GkeClusterId** | Pointer to **NullableString** |  | [optional] 
**CrIpaddressName** | Pointer to **NullableString** |  | [optional] 
**CrIpaddressNamespace** | Pointer to **NullableString** |  | [optional] 
**CrIpaddressclaimName** | Pointer to **NullableString** |  | [optional] 
**CrIpaddressclaimNamespace** | Pointer to **NullableString** |  | [optional] 

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

### GetClaimedBy

`func (o *PatchedSubnetIPAddressRequest) GetClaimedBy() string`

GetClaimedBy returns the ClaimedBy field if non-nil, zero value otherwise.

### GetClaimedByOk

`func (o *PatchedSubnetIPAddressRequest) GetClaimedByOk() (*string, bool)`

GetClaimedByOk returns a tuple with the ClaimedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClaimedBy

`func (o *PatchedSubnetIPAddressRequest) SetClaimedBy(v string)`

SetClaimedBy sets ClaimedBy field to given value.

### HasClaimedBy

`func (o *PatchedSubnetIPAddressRequest) HasClaimedBy() bool`

HasClaimedBy returns a boolean if a field has been set.

### SetClaimedByNil

`func (o *PatchedSubnetIPAddressRequest) SetClaimedByNil(b bool)`

 SetClaimedByNil sets the value for ClaimedBy to be an explicit nil

### UnsetClaimedBy
`func (o *PatchedSubnetIPAddressRequest) UnsetClaimedBy()`

UnsetClaimedBy ensures that no value is present for ClaimedBy, not even an explicit nil
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

### GetMetadata

`func (o *PatchedSubnetIPAddressRequest) GetMetadata() interface{}`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *PatchedSubnetIPAddressRequest) GetMetadataOk() (*interface{}, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *PatchedSubnetIPAddressRequest) SetMetadata(v interface{})`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *PatchedSubnetIPAddressRequest) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### SetMetadataNil

`func (o *PatchedSubnetIPAddressRequest) SetMetadataNil(b bool)`

 SetMetadataNil sets the value for Metadata to be an explicit nil

### UnsetMetadata
`func (o *PatchedSubnetIPAddressRequest) UnsetMetadata()`

UnsetMetadata ensures that no value is present for Metadata, not even an explicit nil
### GetHash

`func (o *PatchedSubnetIPAddressRequest) GetHash() string`

GetHash returns the Hash field if non-nil, zero value otherwise.

### GetHashOk

`func (o *PatchedSubnetIPAddressRequest) GetHashOk() (*string, bool)`

GetHashOk returns a tuple with the Hash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHash

`func (o *PatchedSubnetIPAddressRequest) SetHash(v string)`

SetHash sets Hash field to given value.

### HasHash

`func (o *PatchedSubnetIPAddressRequest) HasHash() bool`

HasHash returns a boolean if a field has been set.

### SetHashNil

`func (o *PatchedSubnetIPAddressRequest) SetHashNil(b bool)`

 SetHashNil sets the value for Hash to be an explicit nil

### UnsetHash
`func (o *PatchedSubnetIPAddressRequest) UnsetHash()`

UnsetHash ensures that no value is present for Hash, not even an explicit nil
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

### GetGkeClusterId

`func (o *PatchedSubnetIPAddressRequest) GetGkeClusterId() string`

GetGkeClusterId returns the GkeClusterId field if non-nil, zero value otherwise.

### GetGkeClusterIdOk

`func (o *PatchedSubnetIPAddressRequest) GetGkeClusterIdOk() (*string, bool)`

GetGkeClusterIdOk returns a tuple with the GkeClusterId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGkeClusterId

`func (o *PatchedSubnetIPAddressRequest) SetGkeClusterId(v string)`

SetGkeClusterId sets GkeClusterId field to given value.

### HasGkeClusterId

`func (o *PatchedSubnetIPAddressRequest) HasGkeClusterId() bool`

HasGkeClusterId returns a boolean if a field has been set.

### SetGkeClusterIdNil

`func (o *PatchedSubnetIPAddressRequest) SetGkeClusterIdNil(b bool)`

 SetGkeClusterIdNil sets the value for GkeClusterId to be an explicit nil

### UnsetGkeClusterId
`func (o *PatchedSubnetIPAddressRequest) UnsetGkeClusterId()`

UnsetGkeClusterId ensures that no value is present for GkeClusterId, not even an explicit nil
### GetCrIpaddressName

`func (o *PatchedSubnetIPAddressRequest) GetCrIpaddressName() string`

GetCrIpaddressName returns the CrIpaddressName field if non-nil, zero value otherwise.

### GetCrIpaddressNameOk

`func (o *PatchedSubnetIPAddressRequest) GetCrIpaddressNameOk() (*string, bool)`

GetCrIpaddressNameOk returns a tuple with the CrIpaddressName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrIpaddressName

`func (o *PatchedSubnetIPAddressRequest) SetCrIpaddressName(v string)`

SetCrIpaddressName sets CrIpaddressName field to given value.

### HasCrIpaddressName

`func (o *PatchedSubnetIPAddressRequest) HasCrIpaddressName() bool`

HasCrIpaddressName returns a boolean if a field has been set.

### SetCrIpaddressNameNil

`func (o *PatchedSubnetIPAddressRequest) SetCrIpaddressNameNil(b bool)`

 SetCrIpaddressNameNil sets the value for CrIpaddressName to be an explicit nil

### UnsetCrIpaddressName
`func (o *PatchedSubnetIPAddressRequest) UnsetCrIpaddressName()`

UnsetCrIpaddressName ensures that no value is present for CrIpaddressName, not even an explicit nil
### GetCrIpaddressNamespace

`func (o *PatchedSubnetIPAddressRequest) GetCrIpaddressNamespace() string`

GetCrIpaddressNamespace returns the CrIpaddressNamespace field if non-nil, zero value otherwise.

### GetCrIpaddressNamespaceOk

`func (o *PatchedSubnetIPAddressRequest) GetCrIpaddressNamespaceOk() (*string, bool)`

GetCrIpaddressNamespaceOk returns a tuple with the CrIpaddressNamespace field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrIpaddressNamespace

`func (o *PatchedSubnetIPAddressRequest) SetCrIpaddressNamespace(v string)`

SetCrIpaddressNamespace sets CrIpaddressNamespace field to given value.

### HasCrIpaddressNamespace

`func (o *PatchedSubnetIPAddressRequest) HasCrIpaddressNamespace() bool`

HasCrIpaddressNamespace returns a boolean if a field has been set.

### SetCrIpaddressNamespaceNil

`func (o *PatchedSubnetIPAddressRequest) SetCrIpaddressNamespaceNil(b bool)`

 SetCrIpaddressNamespaceNil sets the value for CrIpaddressNamespace to be an explicit nil

### UnsetCrIpaddressNamespace
`func (o *PatchedSubnetIPAddressRequest) UnsetCrIpaddressNamespace()`

UnsetCrIpaddressNamespace ensures that no value is present for CrIpaddressNamespace, not even an explicit nil
### GetCrIpaddressclaimName

`func (o *PatchedSubnetIPAddressRequest) GetCrIpaddressclaimName() string`

GetCrIpaddressclaimName returns the CrIpaddressclaimName field if non-nil, zero value otherwise.

### GetCrIpaddressclaimNameOk

`func (o *PatchedSubnetIPAddressRequest) GetCrIpaddressclaimNameOk() (*string, bool)`

GetCrIpaddressclaimNameOk returns a tuple with the CrIpaddressclaimName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrIpaddressclaimName

`func (o *PatchedSubnetIPAddressRequest) SetCrIpaddressclaimName(v string)`

SetCrIpaddressclaimName sets CrIpaddressclaimName field to given value.

### HasCrIpaddressclaimName

`func (o *PatchedSubnetIPAddressRequest) HasCrIpaddressclaimName() bool`

HasCrIpaddressclaimName returns a boolean if a field has been set.

### SetCrIpaddressclaimNameNil

`func (o *PatchedSubnetIPAddressRequest) SetCrIpaddressclaimNameNil(b bool)`

 SetCrIpaddressclaimNameNil sets the value for CrIpaddressclaimName to be an explicit nil

### UnsetCrIpaddressclaimName
`func (o *PatchedSubnetIPAddressRequest) UnsetCrIpaddressclaimName()`

UnsetCrIpaddressclaimName ensures that no value is present for CrIpaddressclaimName, not even an explicit nil
### GetCrIpaddressclaimNamespace

`func (o *PatchedSubnetIPAddressRequest) GetCrIpaddressclaimNamespace() string`

GetCrIpaddressclaimNamespace returns the CrIpaddressclaimNamespace field if non-nil, zero value otherwise.

### GetCrIpaddressclaimNamespaceOk

`func (o *PatchedSubnetIPAddressRequest) GetCrIpaddressclaimNamespaceOk() (*string, bool)`

GetCrIpaddressclaimNamespaceOk returns a tuple with the CrIpaddressclaimNamespace field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrIpaddressclaimNamespace

`func (o *PatchedSubnetIPAddressRequest) SetCrIpaddressclaimNamespace(v string)`

SetCrIpaddressclaimNamespace sets CrIpaddressclaimNamespace field to given value.

### HasCrIpaddressclaimNamespace

`func (o *PatchedSubnetIPAddressRequest) HasCrIpaddressclaimNamespace() bool`

HasCrIpaddressclaimNamespace returns a boolean if a field has been set.

### SetCrIpaddressclaimNamespaceNil

`func (o *PatchedSubnetIPAddressRequest) SetCrIpaddressclaimNamespaceNil(b bool)`

 SetCrIpaddressclaimNamespaceNil sets the value for CrIpaddressclaimNamespace to be an explicit nil

### UnsetCrIpaddressclaimNamespace
`func (o *PatchedSubnetIPAddressRequest) UnsetCrIpaddressclaimNamespace()`

UnsetCrIpaddressclaimNamespace ensures that no value is present for CrIpaddressclaimNamespace, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


