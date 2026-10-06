# PatchedBulkSubnetIPAddressRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** |  | 
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
**CrIpaddressClusterId** | Pointer to **NullableString** |  | [optional] 
**CrIpaddressName** | Pointer to **NullableString** |  | [optional] 
**CrIpaddressNamespace** | Pointer to **NullableString** |  | [optional] 
**CrIpaddressclaimClusterId** | Pointer to **NullableString** |  | [optional] 
**CrIpaddressclaimName** | Pointer to **NullableString** |  | [optional] 
**CrIpaddressclaimNamespace** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewPatchedBulkSubnetIPAddressRequest

`func NewPatchedBulkSubnetIPAddressRequest(id int32, ) *PatchedBulkSubnetIPAddressRequest`

NewPatchedBulkSubnetIPAddressRequest instantiates a new PatchedBulkSubnetIPAddressRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPatchedBulkSubnetIPAddressRequestWithDefaults

`func NewPatchedBulkSubnetIPAddressRequestWithDefaults() *PatchedBulkSubnetIPAddressRequest`

NewPatchedBulkSubnetIPAddressRequestWithDefaults instantiates a new PatchedBulkSubnetIPAddressRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *PatchedBulkSubnetIPAddressRequest) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *PatchedBulkSubnetIPAddressRequest) SetId(v int32)`

SetId sets Id field to given value.


### GetAddress

`func (o *PatchedBulkSubnetIPAddressRequest) GetAddress() string`

GetAddress returns the Address field if non-nil, zero value otherwise.

### GetAddressOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetAddressOk() (*string, bool)`

GetAddressOk returns a tuple with the Address field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddress

`func (o *PatchedBulkSubnetIPAddressRequest) SetAddress(v string)`

SetAddress sets Address field to given value.

### HasAddress

`func (o *PatchedBulkSubnetIPAddressRequest) HasAddress() bool`

HasAddress returns a boolean if a field has been set.

### GetVpc

`func (o *PatchedBulkSubnetIPAddressRequest) GetVpc() PatchedSubnetIPAddressRequestVpc`

GetVpc returns the Vpc field if non-nil, zero value otherwise.

### GetVpcOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetVpcOk() (*PatchedSubnetIPAddressRequestVpc, bool)`

GetVpcOk returns a tuple with the Vpc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVpc

`func (o *PatchedBulkSubnetIPAddressRequest) SetVpc(v PatchedSubnetIPAddressRequestVpc)`

SetVpc sets Vpc field to given value.

### HasVpc

`func (o *PatchedBulkSubnetIPAddressRequest) HasVpc() bool`

HasVpc returns a boolean if a field has been set.

### SetVpcNil

`func (o *PatchedBulkSubnetIPAddressRequest) SetVpcNil(b bool)`

 SetVpcNil sets the value for Vpc to be an explicit nil

### UnsetVpc
`func (o *PatchedBulkSubnetIPAddressRequest) UnsetVpc()`

UnsetVpc ensures that no value is present for Vpc, not even an explicit nil
### GetCountry

`func (o *PatchedBulkSubnetIPAddressRequest) GetCountry() PatchedSubnetIPAddressRequestCountry`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetCountryOk() (*PatchedSubnetIPAddressRequestCountry, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *PatchedBulkSubnetIPAddressRequest) SetCountry(v PatchedSubnetIPAddressRequestCountry)`

SetCountry sets Country field to given value.

### HasCountry

`func (o *PatchedBulkSubnetIPAddressRequest) HasCountry() bool`

HasCountry returns a boolean if a field has been set.

### GetClaimedBy

`func (o *PatchedBulkSubnetIPAddressRequest) GetClaimedBy() string`

GetClaimedBy returns the ClaimedBy field if non-nil, zero value otherwise.

### GetClaimedByOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetClaimedByOk() (*string, bool)`

GetClaimedByOk returns a tuple with the ClaimedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClaimedBy

`func (o *PatchedBulkSubnetIPAddressRequest) SetClaimedBy(v string)`

SetClaimedBy sets ClaimedBy field to given value.

### HasClaimedBy

`func (o *PatchedBulkSubnetIPAddressRequest) HasClaimedBy() bool`

HasClaimedBy returns a boolean if a field has been set.

### SetClaimedByNil

`func (o *PatchedBulkSubnetIPAddressRequest) SetClaimedByNil(b bool)`

 SetClaimedByNil sets the value for ClaimedBy to be an explicit nil

### UnsetClaimedBy
`func (o *PatchedBulkSubnetIPAddressRequest) UnsetClaimedBy()`

UnsetClaimedBy ensures that no value is present for ClaimedBy, not even an explicit nil
### GetSubnetPrefix

`func (o *PatchedBulkSubnetIPAddressRequest) GetSubnetPrefix() int32`

GetSubnetPrefix returns the SubnetPrefix field if non-nil, zero value otherwise.

### GetSubnetPrefixOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetSubnetPrefixOk() (*int32, bool)`

GetSubnetPrefixOk returns a tuple with the SubnetPrefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubnetPrefix

`func (o *PatchedBulkSubnetIPAddressRequest) SetSubnetPrefix(v int32)`

SetSubnetPrefix sets SubnetPrefix field to given value.

### HasSubnetPrefix

`func (o *PatchedBulkSubnetIPAddressRequest) HasSubnetPrefix() bool`

HasSubnetPrefix returns a boolean if a field has been set.

### GetTenant

`func (o *PatchedBulkSubnetIPAddressRequest) GetTenant() PatchedSubnetIPAddressRequestTenant`

GetTenant returns the Tenant field if non-nil, zero value otherwise.

### GetTenantOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetTenantOk() (*PatchedSubnetIPAddressRequestTenant, bool)`

GetTenantOk returns a tuple with the Tenant field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTenant

`func (o *PatchedBulkSubnetIPAddressRequest) SetTenant(v PatchedSubnetIPAddressRequestTenant)`

SetTenant sets Tenant field to given value.

### HasTenant

`func (o *PatchedBulkSubnetIPAddressRequest) HasTenant() bool`

HasTenant returns a boolean if a field has been set.

### SetTenantNil

`func (o *PatchedBulkSubnetIPAddressRequest) SetTenantNil(b bool)`

 SetTenantNil sets the value for Tenant to be an explicit nil

### UnsetTenant
`func (o *PatchedBulkSubnetIPAddressRequest) UnsetTenant()`

UnsetTenant ensures that no value is present for Tenant, not even an explicit nil
### GetStatus

`func (o *PatchedBulkSubnetIPAddressRequest) GetStatus() PatchedSubnetIPAddressRequestStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetStatusOk() (*PatchedSubnetIPAddressRequestStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *PatchedBulkSubnetIPAddressRequest) SetStatus(v PatchedSubnetIPAddressRequestStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *PatchedBulkSubnetIPAddressRequest) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetRole

`func (o *PatchedBulkSubnetIPAddressRequest) GetRole() PatchedSubnetIPAddressRequestRole`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetRoleOk() (*PatchedSubnetIPAddressRequestRole, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *PatchedBulkSubnetIPAddressRequest) SetRole(v PatchedSubnetIPAddressRequestRole)`

SetRole sets Role field to given value.

### HasRole

`func (o *PatchedBulkSubnetIPAddressRequest) HasRole() bool`

HasRole returns a boolean if a field has been set.

### GetNatInside

`func (o *PatchedBulkSubnetIPAddressRequest) GetNatInside() NestedSubnetIPAddressRequest`

GetNatInside returns the NatInside field if non-nil, zero value otherwise.

### GetNatInsideOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetNatInsideOk() (*NestedSubnetIPAddressRequest, bool)`

GetNatInsideOk returns a tuple with the NatInside field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNatInside

`func (o *PatchedBulkSubnetIPAddressRequest) SetNatInside(v NestedSubnetIPAddressRequest)`

SetNatInside sets NatInside field to given value.

### HasNatInside

`func (o *PatchedBulkSubnetIPAddressRequest) HasNatInside() bool`

HasNatInside returns a boolean if a field has been set.

### SetNatInsideNil

`func (o *PatchedBulkSubnetIPAddressRequest) SetNatInsideNil(b bool)`

 SetNatInsideNil sets the value for NatInside to be an explicit nil

### UnsetNatInside
`func (o *PatchedBulkSubnetIPAddressRequest) UnsetNatInside()`

UnsetNatInside ensures that no value is present for NatInside, not even an explicit nil
### GetDnsName

`func (o *PatchedBulkSubnetIPAddressRequest) GetDnsName() string`

GetDnsName returns the DnsName field if non-nil, zero value otherwise.

### GetDnsNameOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetDnsNameOk() (*string, bool)`

GetDnsNameOk returns a tuple with the DnsName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDnsName

`func (o *PatchedBulkSubnetIPAddressRequest) SetDnsName(v string)`

SetDnsName sets DnsName field to given value.

### HasDnsName

`func (o *PatchedBulkSubnetIPAddressRequest) HasDnsName() bool`

HasDnsName returns a boolean if a field has been set.

### GetMetadata

`func (o *PatchedBulkSubnetIPAddressRequest) GetMetadata() interface{}`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetMetadataOk() (*interface{}, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *PatchedBulkSubnetIPAddressRequest) SetMetadata(v interface{})`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *PatchedBulkSubnetIPAddressRequest) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### SetMetadataNil

`func (o *PatchedBulkSubnetIPAddressRequest) SetMetadataNil(b bool)`

 SetMetadataNil sets the value for Metadata to be an explicit nil

### UnsetMetadata
`func (o *PatchedBulkSubnetIPAddressRequest) UnsetMetadata()`

UnsetMetadata ensures that no value is present for Metadata, not even an explicit nil
### GetHash

`func (o *PatchedBulkSubnetIPAddressRequest) GetHash() string`

GetHash returns the Hash field if non-nil, zero value otherwise.

### GetHashOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetHashOk() (*string, bool)`

GetHashOk returns a tuple with the Hash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHash

`func (o *PatchedBulkSubnetIPAddressRequest) SetHash(v string)`

SetHash sets Hash field to given value.

### HasHash

`func (o *PatchedBulkSubnetIPAddressRequest) HasHash() bool`

HasHash returns a boolean if a field has been set.

### SetHashNil

`func (o *PatchedBulkSubnetIPAddressRequest) SetHashNil(b bool)`

 SetHashNil sets the value for Hash to be an explicit nil

### UnsetHash
`func (o *PatchedBulkSubnetIPAddressRequest) UnsetHash()`

UnsetHash ensures that no value is present for Hash, not even an explicit nil
### GetDescription

`func (o *PatchedBulkSubnetIPAddressRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *PatchedBulkSubnetIPAddressRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *PatchedBulkSubnetIPAddressRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetComments

`func (o *PatchedBulkSubnetIPAddressRequest) GetComments() string`

GetComments returns the Comments field if non-nil, zero value otherwise.

### GetCommentsOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetCommentsOk() (*string, bool)`

GetCommentsOk returns a tuple with the Comments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComments

`func (o *PatchedBulkSubnetIPAddressRequest) SetComments(v string)`

SetComments sets Comments field to given value.

### HasComments

`func (o *PatchedBulkSubnetIPAddressRequest) HasComments() bool`

HasComments returns a boolean if a field has been set.

### GetTags

`func (o *PatchedBulkSubnetIPAddressRequest) GetTags() []NestedTagRequest`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetTagsOk() (*[]NestedTagRequest, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTags

`func (o *PatchedBulkSubnetIPAddressRequest) SetTags(v []NestedTagRequest)`

SetTags sets Tags field to given value.

### HasTags

`func (o *PatchedBulkSubnetIPAddressRequest) HasTags() bool`

HasTags returns a boolean if a field has been set.

### GetCustomFields

`func (o *PatchedBulkSubnetIPAddressRequest) GetCustomFields() map[string]interface{}`

GetCustomFields returns the CustomFields field if non-nil, zero value otherwise.

### GetCustomFieldsOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetCustomFieldsOk() (*map[string]interface{}, bool)`

GetCustomFieldsOk returns a tuple with the CustomFields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomFields

`func (o *PatchedBulkSubnetIPAddressRequest) SetCustomFields(v map[string]interface{})`

SetCustomFields sets CustomFields field to given value.

### HasCustomFields

`func (o *PatchedBulkSubnetIPAddressRequest) HasCustomFields() bool`

HasCustomFields returns a boolean if a field has been set.

### GetCrIpaddressClusterId

`func (o *PatchedBulkSubnetIPAddressRequest) GetCrIpaddressClusterId() string`

GetCrIpaddressClusterId returns the CrIpaddressClusterId field if non-nil, zero value otherwise.

### GetCrIpaddressClusterIdOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetCrIpaddressClusterIdOk() (*string, bool)`

GetCrIpaddressClusterIdOk returns a tuple with the CrIpaddressClusterId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrIpaddressClusterId

`func (o *PatchedBulkSubnetIPAddressRequest) SetCrIpaddressClusterId(v string)`

SetCrIpaddressClusterId sets CrIpaddressClusterId field to given value.

### HasCrIpaddressClusterId

`func (o *PatchedBulkSubnetIPAddressRequest) HasCrIpaddressClusterId() bool`

HasCrIpaddressClusterId returns a boolean if a field has been set.

### SetCrIpaddressClusterIdNil

`func (o *PatchedBulkSubnetIPAddressRequest) SetCrIpaddressClusterIdNil(b bool)`

 SetCrIpaddressClusterIdNil sets the value for CrIpaddressClusterId to be an explicit nil

### UnsetCrIpaddressClusterId
`func (o *PatchedBulkSubnetIPAddressRequest) UnsetCrIpaddressClusterId()`

UnsetCrIpaddressClusterId ensures that no value is present for CrIpaddressClusterId, not even an explicit nil
### GetCrIpaddressName

`func (o *PatchedBulkSubnetIPAddressRequest) GetCrIpaddressName() string`

GetCrIpaddressName returns the CrIpaddressName field if non-nil, zero value otherwise.

### GetCrIpaddressNameOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetCrIpaddressNameOk() (*string, bool)`

GetCrIpaddressNameOk returns a tuple with the CrIpaddressName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrIpaddressName

`func (o *PatchedBulkSubnetIPAddressRequest) SetCrIpaddressName(v string)`

SetCrIpaddressName sets CrIpaddressName field to given value.

### HasCrIpaddressName

`func (o *PatchedBulkSubnetIPAddressRequest) HasCrIpaddressName() bool`

HasCrIpaddressName returns a boolean if a field has been set.

### SetCrIpaddressNameNil

`func (o *PatchedBulkSubnetIPAddressRequest) SetCrIpaddressNameNil(b bool)`

 SetCrIpaddressNameNil sets the value for CrIpaddressName to be an explicit nil

### UnsetCrIpaddressName
`func (o *PatchedBulkSubnetIPAddressRequest) UnsetCrIpaddressName()`

UnsetCrIpaddressName ensures that no value is present for CrIpaddressName, not even an explicit nil
### GetCrIpaddressNamespace

`func (o *PatchedBulkSubnetIPAddressRequest) GetCrIpaddressNamespace() string`

GetCrIpaddressNamespace returns the CrIpaddressNamespace field if non-nil, zero value otherwise.

### GetCrIpaddressNamespaceOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetCrIpaddressNamespaceOk() (*string, bool)`

GetCrIpaddressNamespaceOk returns a tuple with the CrIpaddressNamespace field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrIpaddressNamespace

`func (o *PatchedBulkSubnetIPAddressRequest) SetCrIpaddressNamespace(v string)`

SetCrIpaddressNamespace sets CrIpaddressNamespace field to given value.

### HasCrIpaddressNamespace

`func (o *PatchedBulkSubnetIPAddressRequest) HasCrIpaddressNamespace() bool`

HasCrIpaddressNamespace returns a boolean if a field has been set.

### SetCrIpaddressNamespaceNil

`func (o *PatchedBulkSubnetIPAddressRequest) SetCrIpaddressNamespaceNil(b bool)`

 SetCrIpaddressNamespaceNil sets the value for CrIpaddressNamespace to be an explicit nil

### UnsetCrIpaddressNamespace
`func (o *PatchedBulkSubnetIPAddressRequest) UnsetCrIpaddressNamespace()`

UnsetCrIpaddressNamespace ensures that no value is present for CrIpaddressNamespace, not even an explicit nil
### GetCrIpaddressclaimClusterId

`func (o *PatchedBulkSubnetIPAddressRequest) GetCrIpaddressclaimClusterId() string`

GetCrIpaddressclaimClusterId returns the CrIpaddressclaimClusterId field if non-nil, zero value otherwise.

### GetCrIpaddressclaimClusterIdOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetCrIpaddressclaimClusterIdOk() (*string, bool)`

GetCrIpaddressclaimClusterIdOk returns a tuple with the CrIpaddressclaimClusterId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrIpaddressclaimClusterId

`func (o *PatchedBulkSubnetIPAddressRequest) SetCrIpaddressclaimClusterId(v string)`

SetCrIpaddressclaimClusterId sets CrIpaddressclaimClusterId field to given value.

### HasCrIpaddressclaimClusterId

`func (o *PatchedBulkSubnetIPAddressRequest) HasCrIpaddressclaimClusterId() bool`

HasCrIpaddressclaimClusterId returns a boolean if a field has been set.

### SetCrIpaddressclaimClusterIdNil

`func (o *PatchedBulkSubnetIPAddressRequest) SetCrIpaddressclaimClusterIdNil(b bool)`

 SetCrIpaddressclaimClusterIdNil sets the value for CrIpaddressclaimClusterId to be an explicit nil

### UnsetCrIpaddressclaimClusterId
`func (o *PatchedBulkSubnetIPAddressRequest) UnsetCrIpaddressclaimClusterId()`

UnsetCrIpaddressclaimClusterId ensures that no value is present for CrIpaddressclaimClusterId, not even an explicit nil
### GetCrIpaddressclaimName

`func (o *PatchedBulkSubnetIPAddressRequest) GetCrIpaddressclaimName() string`

GetCrIpaddressclaimName returns the CrIpaddressclaimName field if non-nil, zero value otherwise.

### GetCrIpaddressclaimNameOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetCrIpaddressclaimNameOk() (*string, bool)`

GetCrIpaddressclaimNameOk returns a tuple with the CrIpaddressclaimName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrIpaddressclaimName

`func (o *PatchedBulkSubnetIPAddressRequest) SetCrIpaddressclaimName(v string)`

SetCrIpaddressclaimName sets CrIpaddressclaimName field to given value.

### HasCrIpaddressclaimName

`func (o *PatchedBulkSubnetIPAddressRequest) HasCrIpaddressclaimName() bool`

HasCrIpaddressclaimName returns a boolean if a field has been set.

### SetCrIpaddressclaimNameNil

`func (o *PatchedBulkSubnetIPAddressRequest) SetCrIpaddressclaimNameNil(b bool)`

 SetCrIpaddressclaimNameNil sets the value for CrIpaddressclaimName to be an explicit nil

### UnsetCrIpaddressclaimName
`func (o *PatchedBulkSubnetIPAddressRequest) UnsetCrIpaddressclaimName()`

UnsetCrIpaddressclaimName ensures that no value is present for CrIpaddressclaimName, not even an explicit nil
### GetCrIpaddressclaimNamespace

`func (o *PatchedBulkSubnetIPAddressRequest) GetCrIpaddressclaimNamespace() string`

GetCrIpaddressclaimNamespace returns the CrIpaddressclaimNamespace field if non-nil, zero value otherwise.

### GetCrIpaddressclaimNamespaceOk

`func (o *PatchedBulkSubnetIPAddressRequest) GetCrIpaddressclaimNamespaceOk() (*string, bool)`

GetCrIpaddressclaimNamespaceOk returns a tuple with the CrIpaddressclaimNamespace field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrIpaddressclaimNamespace

`func (o *PatchedBulkSubnetIPAddressRequest) SetCrIpaddressclaimNamespace(v string)`

SetCrIpaddressclaimNamespace sets CrIpaddressclaimNamespace field to given value.

### HasCrIpaddressclaimNamespace

`func (o *PatchedBulkSubnetIPAddressRequest) HasCrIpaddressclaimNamespace() bool`

HasCrIpaddressclaimNamespace returns a boolean if a field has been set.

### SetCrIpaddressclaimNamespaceNil

`func (o *PatchedBulkSubnetIPAddressRequest) SetCrIpaddressclaimNamespaceNil(b bool)`

 SetCrIpaddressclaimNamespaceNil sets the value for CrIpaddressclaimNamespace to be an explicit nil

### UnsetCrIpaddressclaimNamespace
`func (o *PatchedBulkSubnetIPAddressRequest) UnsetCrIpaddressclaimNamespace()`

UnsetCrIpaddressclaimNamespace ensures that no value is present for CrIpaddressclaimNamespace, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


