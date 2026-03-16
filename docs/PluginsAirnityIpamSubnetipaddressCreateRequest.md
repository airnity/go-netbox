# PluginsAirnityIpamSubnetipaddressCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Address** | **string** |  | 
**Vpc** | Pointer to [**NullablePatchedSubnetIPAddressRequestVpc**](PatchedSubnetIPAddressRequestVpc.md) |  | [optional] 
**Country** | Pointer to [**PatchedSubnetIPAddressRequestCountry**](PatchedSubnetIPAddressRequestCountry.md) |  | [optional] 
**ClaimedBy** | Pointer to **NullableString** |  | [optional] 
**SubnetPrefix** | **int32** | The subnet prefix this IP belongs to | 
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
**CustomFields** | Pointer to **map[string]map[string]interface{}** |  | [optional] 
**GkeClusterId** | Pointer to **NullableString** |  | [optional] 
**CrIpaddressName** | Pointer to **NullableString** |  | [optional] 
**CrIpaddressNamespace** | Pointer to **NullableString** |  | [optional] 
**CrIpaddressclaimName** | Pointer to **NullableString** |  | [optional] 
**CrIpaddressclaimNamespace** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewPluginsAirnityIpamSubnetipaddressCreateRequest

`func NewPluginsAirnityIpamSubnetipaddressCreateRequest(address string, subnetPrefix int32, ) *PluginsAirnityIpamSubnetipaddressCreateRequest`

NewPluginsAirnityIpamSubnetipaddressCreateRequest instantiates a new PluginsAirnityIpamSubnetipaddressCreateRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPluginsAirnityIpamSubnetipaddressCreateRequestWithDefaults

`func NewPluginsAirnityIpamSubnetipaddressCreateRequestWithDefaults() *PluginsAirnityIpamSubnetipaddressCreateRequest`

NewPluginsAirnityIpamSubnetipaddressCreateRequestWithDefaults instantiates a new PluginsAirnityIpamSubnetipaddressCreateRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAddress

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetAddress() string`

GetAddress returns the Address field if non-nil, zero value otherwise.

### GetAddressOk

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetAddressOk() (*string, bool)`

GetAddressOk returns a tuple with the Address field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddress

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetAddress(v string)`

SetAddress sets Address field to given value.


### GetVpc

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetVpc() PatchedSubnetIPAddressRequestVpc`

GetVpc returns the Vpc field if non-nil, zero value otherwise.

### GetVpcOk

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetVpcOk() (*PatchedSubnetIPAddressRequestVpc, bool)`

GetVpcOk returns a tuple with the Vpc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVpc

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetVpc(v PatchedSubnetIPAddressRequestVpc)`

SetVpc sets Vpc field to given value.

### HasVpc

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) HasVpc() bool`

HasVpc returns a boolean if a field has been set.

### SetVpcNil

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetVpcNil(b bool)`

 SetVpcNil sets the value for Vpc to be an explicit nil

### UnsetVpc
`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) UnsetVpc()`

UnsetVpc ensures that no value is present for Vpc, not even an explicit nil
### GetCountry

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetCountry() PatchedSubnetIPAddressRequestCountry`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetCountryOk() (*PatchedSubnetIPAddressRequestCountry, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetCountry(v PatchedSubnetIPAddressRequestCountry)`

SetCountry sets Country field to given value.

### HasCountry

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) HasCountry() bool`

HasCountry returns a boolean if a field has been set.

### GetClaimedBy

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetClaimedBy() string`

GetClaimedBy returns the ClaimedBy field if non-nil, zero value otherwise.

### GetClaimedByOk

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetClaimedByOk() (*string, bool)`

GetClaimedByOk returns a tuple with the ClaimedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClaimedBy

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetClaimedBy(v string)`

SetClaimedBy sets ClaimedBy field to given value.

### HasClaimedBy

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) HasClaimedBy() bool`

HasClaimedBy returns a boolean if a field has been set.

### SetClaimedByNil

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetClaimedByNil(b bool)`

 SetClaimedByNil sets the value for ClaimedBy to be an explicit nil

### UnsetClaimedBy
`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) UnsetClaimedBy()`

UnsetClaimedBy ensures that no value is present for ClaimedBy, not even an explicit nil
### GetSubnetPrefix

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetSubnetPrefix() int32`

GetSubnetPrefix returns the SubnetPrefix field if non-nil, zero value otherwise.

### GetSubnetPrefixOk

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetSubnetPrefixOk() (*int32, bool)`

GetSubnetPrefixOk returns a tuple with the SubnetPrefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubnetPrefix

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetSubnetPrefix(v int32)`

SetSubnetPrefix sets SubnetPrefix field to given value.


### GetTenant

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetTenant() PatchedSubnetIPAddressRequestTenant`

GetTenant returns the Tenant field if non-nil, zero value otherwise.

### GetTenantOk

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetTenantOk() (*PatchedSubnetIPAddressRequestTenant, bool)`

GetTenantOk returns a tuple with the Tenant field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTenant

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetTenant(v PatchedSubnetIPAddressRequestTenant)`

SetTenant sets Tenant field to given value.

### HasTenant

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) HasTenant() bool`

HasTenant returns a boolean if a field has been set.

### SetTenantNil

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetTenantNil(b bool)`

 SetTenantNil sets the value for Tenant to be an explicit nil

### UnsetTenant
`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) UnsetTenant()`

UnsetTenant ensures that no value is present for Tenant, not even an explicit nil
### GetStatus

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetStatus() PatchedSubnetIPAddressRequestStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetStatusOk() (*PatchedSubnetIPAddressRequestStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetStatus(v PatchedSubnetIPAddressRequestStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetRole

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetRole() PatchedSubnetIPAddressRequestRole`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetRoleOk() (*PatchedSubnetIPAddressRequestRole, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetRole(v PatchedSubnetIPAddressRequestRole)`

SetRole sets Role field to given value.

### HasRole

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) HasRole() bool`

HasRole returns a boolean if a field has been set.

### GetNatInside

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetNatInside() NestedSubnetIPAddressRequest`

GetNatInside returns the NatInside field if non-nil, zero value otherwise.

### GetNatInsideOk

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetNatInsideOk() (*NestedSubnetIPAddressRequest, bool)`

GetNatInsideOk returns a tuple with the NatInside field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNatInside

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetNatInside(v NestedSubnetIPAddressRequest)`

SetNatInside sets NatInside field to given value.

### HasNatInside

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) HasNatInside() bool`

HasNatInside returns a boolean if a field has been set.

### SetNatInsideNil

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetNatInsideNil(b bool)`

 SetNatInsideNil sets the value for NatInside to be an explicit nil

### UnsetNatInside
`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) UnsetNatInside()`

UnsetNatInside ensures that no value is present for NatInside, not even an explicit nil
### GetDnsName

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetDnsName() string`

GetDnsName returns the DnsName field if non-nil, zero value otherwise.

### GetDnsNameOk

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetDnsNameOk() (*string, bool)`

GetDnsNameOk returns a tuple with the DnsName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDnsName

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetDnsName(v string)`

SetDnsName sets DnsName field to given value.

### HasDnsName

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) HasDnsName() bool`

HasDnsName returns a boolean if a field has been set.

### GetMetadata

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetMetadata() interface{}`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetMetadataOk() (*interface{}, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetMetadata(v interface{})`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### SetMetadataNil

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetMetadataNil(b bool)`

 SetMetadataNil sets the value for Metadata to be an explicit nil

### UnsetMetadata
`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) UnsetMetadata()`

UnsetMetadata ensures that no value is present for Metadata, not even an explicit nil
### GetHash

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetHash() string`

GetHash returns the Hash field if non-nil, zero value otherwise.

### GetHashOk

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetHashOk() (*string, bool)`

GetHashOk returns a tuple with the Hash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHash

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetHash(v string)`

SetHash sets Hash field to given value.

### HasHash

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) HasHash() bool`

HasHash returns a boolean if a field has been set.

### SetHashNil

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetHashNil(b bool)`

 SetHashNil sets the value for Hash to be an explicit nil

### UnsetHash
`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) UnsetHash()`

UnsetHash ensures that no value is present for Hash, not even an explicit nil
### GetDescription

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetComments

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetComments() string`

GetComments returns the Comments field if non-nil, zero value otherwise.

### GetCommentsOk

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetCommentsOk() (*string, bool)`

GetCommentsOk returns a tuple with the Comments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComments

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetComments(v string)`

SetComments sets Comments field to given value.

### HasComments

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) HasComments() bool`

HasComments returns a boolean if a field has been set.

### GetTags

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetTags() []NestedTagRequest`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetTagsOk() (*[]NestedTagRequest, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTags

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetTags(v []NestedTagRequest)`

SetTags sets Tags field to given value.

### HasTags

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) HasTags() bool`

HasTags returns a boolean if a field has been set.

### GetCustomFields

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetCustomFields() map[string]map[string]interface{}`

GetCustomFields returns the CustomFields field if non-nil, zero value otherwise.

### GetCustomFieldsOk

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetCustomFieldsOk() (*map[string]map[string]interface{}, bool)`

GetCustomFieldsOk returns a tuple with the CustomFields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomFields

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetCustomFields(v map[string]map[string]interface{})`

SetCustomFields sets CustomFields field to given value.

### HasCustomFields

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) HasCustomFields() bool`

HasCustomFields returns a boolean if a field has been set.

### GetGkeClusterId

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetGkeClusterId() string`

GetGkeClusterId returns the GkeClusterId field if non-nil, zero value otherwise.

### GetGkeClusterIdOk

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetGkeClusterIdOk() (*string, bool)`

GetGkeClusterIdOk returns a tuple with the GkeClusterId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGkeClusterId

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetGkeClusterId(v string)`

SetGkeClusterId sets GkeClusterId field to given value.

### HasGkeClusterId

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) HasGkeClusterId() bool`

HasGkeClusterId returns a boolean if a field has been set.

### SetGkeClusterIdNil

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetGkeClusterIdNil(b bool)`

 SetGkeClusterIdNil sets the value for GkeClusterId to be an explicit nil

### UnsetGkeClusterId
`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) UnsetGkeClusterId()`

UnsetGkeClusterId ensures that no value is present for GkeClusterId, not even an explicit nil
### GetCrIpaddressName

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetCrIpaddressName() string`

GetCrIpaddressName returns the CrIpaddressName field if non-nil, zero value otherwise.

### GetCrIpaddressNameOk

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetCrIpaddressNameOk() (*string, bool)`

GetCrIpaddressNameOk returns a tuple with the CrIpaddressName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrIpaddressName

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetCrIpaddressName(v string)`

SetCrIpaddressName sets CrIpaddressName field to given value.

### HasCrIpaddressName

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) HasCrIpaddressName() bool`

HasCrIpaddressName returns a boolean if a field has been set.

### SetCrIpaddressNameNil

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetCrIpaddressNameNil(b bool)`

 SetCrIpaddressNameNil sets the value for CrIpaddressName to be an explicit nil

### UnsetCrIpaddressName
`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) UnsetCrIpaddressName()`

UnsetCrIpaddressName ensures that no value is present for CrIpaddressName, not even an explicit nil
### GetCrIpaddressNamespace

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetCrIpaddressNamespace() string`

GetCrIpaddressNamespace returns the CrIpaddressNamespace field if non-nil, zero value otherwise.

### GetCrIpaddressNamespaceOk

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetCrIpaddressNamespaceOk() (*string, bool)`

GetCrIpaddressNamespaceOk returns a tuple with the CrIpaddressNamespace field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrIpaddressNamespace

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetCrIpaddressNamespace(v string)`

SetCrIpaddressNamespace sets CrIpaddressNamespace field to given value.

### HasCrIpaddressNamespace

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) HasCrIpaddressNamespace() bool`

HasCrIpaddressNamespace returns a boolean if a field has been set.

### SetCrIpaddressNamespaceNil

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetCrIpaddressNamespaceNil(b bool)`

 SetCrIpaddressNamespaceNil sets the value for CrIpaddressNamespace to be an explicit nil

### UnsetCrIpaddressNamespace
`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) UnsetCrIpaddressNamespace()`

UnsetCrIpaddressNamespace ensures that no value is present for CrIpaddressNamespace, not even an explicit nil
### GetCrIpaddressclaimName

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetCrIpaddressclaimName() string`

GetCrIpaddressclaimName returns the CrIpaddressclaimName field if non-nil, zero value otherwise.

### GetCrIpaddressclaimNameOk

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetCrIpaddressclaimNameOk() (*string, bool)`

GetCrIpaddressclaimNameOk returns a tuple with the CrIpaddressclaimName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrIpaddressclaimName

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetCrIpaddressclaimName(v string)`

SetCrIpaddressclaimName sets CrIpaddressclaimName field to given value.

### HasCrIpaddressclaimName

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) HasCrIpaddressclaimName() bool`

HasCrIpaddressclaimName returns a boolean if a field has been set.

### SetCrIpaddressclaimNameNil

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetCrIpaddressclaimNameNil(b bool)`

 SetCrIpaddressclaimNameNil sets the value for CrIpaddressclaimName to be an explicit nil

### UnsetCrIpaddressclaimName
`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) UnsetCrIpaddressclaimName()`

UnsetCrIpaddressclaimName ensures that no value is present for CrIpaddressclaimName, not even an explicit nil
### GetCrIpaddressclaimNamespace

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetCrIpaddressclaimNamespace() string`

GetCrIpaddressclaimNamespace returns the CrIpaddressclaimNamespace field if non-nil, zero value otherwise.

### GetCrIpaddressclaimNamespaceOk

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) GetCrIpaddressclaimNamespaceOk() (*string, bool)`

GetCrIpaddressclaimNamespaceOk returns a tuple with the CrIpaddressclaimNamespace field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrIpaddressclaimNamespace

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetCrIpaddressclaimNamespace(v string)`

SetCrIpaddressclaimNamespace sets CrIpaddressclaimNamespace field to given value.

### HasCrIpaddressclaimNamespace

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) HasCrIpaddressclaimNamespace() bool`

HasCrIpaddressclaimNamespace returns a boolean if a field has been set.

### SetCrIpaddressclaimNamespaceNil

`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) SetCrIpaddressclaimNamespaceNil(b bool)`

 SetCrIpaddressclaimNamespaceNil sets the value for CrIpaddressclaimNamespace to be an explicit nil

### UnsetCrIpaddressclaimNamespace
`func (o *PluginsAirnityIpamSubnetipaddressCreateRequest) UnsetCrIpaddressclaimNamespace()`

UnsetCrIpaddressclaimNamespace ensures that no value is present for CrIpaddressclaimNamespace, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


