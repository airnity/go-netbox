# BulkSubnetIPAddressRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** |  | 
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
**CustomFields** | Pointer to **map[string]interface{}** |  | [optional] 
**CrIpaddressClusterId** | Pointer to **NullableString** |  | [optional] 
**CrIpaddressName** | Pointer to **NullableString** |  | [optional] 
**CrIpaddressNamespace** | Pointer to **NullableString** |  | [optional] 
**CrIpaddressclaimClusterId** | Pointer to **NullableString** |  | [optional] 
**CrIpaddressclaimName** | Pointer to **NullableString** |  | [optional] 
**CrIpaddressclaimNamespace** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewBulkSubnetIPAddressRequest

`func NewBulkSubnetIPAddressRequest(id int32, address string, subnetPrefix int32, ) *BulkSubnetIPAddressRequest`

NewBulkSubnetIPAddressRequest instantiates a new BulkSubnetIPAddressRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBulkSubnetIPAddressRequestWithDefaults

`func NewBulkSubnetIPAddressRequestWithDefaults() *BulkSubnetIPAddressRequest`

NewBulkSubnetIPAddressRequestWithDefaults instantiates a new BulkSubnetIPAddressRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *BulkSubnetIPAddressRequest) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *BulkSubnetIPAddressRequest) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *BulkSubnetIPAddressRequest) SetId(v int32)`

SetId sets Id field to given value.


### GetAddress

`func (o *BulkSubnetIPAddressRequest) GetAddress() string`

GetAddress returns the Address field if non-nil, zero value otherwise.

### GetAddressOk

`func (o *BulkSubnetIPAddressRequest) GetAddressOk() (*string, bool)`

GetAddressOk returns a tuple with the Address field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddress

`func (o *BulkSubnetIPAddressRequest) SetAddress(v string)`

SetAddress sets Address field to given value.


### GetVpc

`func (o *BulkSubnetIPAddressRequest) GetVpc() PatchedSubnetIPAddressRequestVpc`

GetVpc returns the Vpc field if non-nil, zero value otherwise.

### GetVpcOk

`func (o *BulkSubnetIPAddressRequest) GetVpcOk() (*PatchedSubnetIPAddressRequestVpc, bool)`

GetVpcOk returns a tuple with the Vpc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVpc

`func (o *BulkSubnetIPAddressRequest) SetVpc(v PatchedSubnetIPAddressRequestVpc)`

SetVpc sets Vpc field to given value.

### HasVpc

`func (o *BulkSubnetIPAddressRequest) HasVpc() bool`

HasVpc returns a boolean if a field has been set.

### SetVpcNil

`func (o *BulkSubnetIPAddressRequest) SetVpcNil(b bool)`

 SetVpcNil sets the value for Vpc to be an explicit nil

### UnsetVpc
`func (o *BulkSubnetIPAddressRequest) UnsetVpc()`

UnsetVpc ensures that no value is present for Vpc, not even an explicit nil
### GetCountry

`func (o *BulkSubnetIPAddressRequest) GetCountry() PatchedSubnetIPAddressRequestCountry`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *BulkSubnetIPAddressRequest) GetCountryOk() (*PatchedSubnetIPAddressRequestCountry, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *BulkSubnetIPAddressRequest) SetCountry(v PatchedSubnetIPAddressRequestCountry)`

SetCountry sets Country field to given value.

### HasCountry

`func (o *BulkSubnetIPAddressRequest) HasCountry() bool`

HasCountry returns a boolean if a field has been set.

### GetClaimedBy

`func (o *BulkSubnetIPAddressRequest) GetClaimedBy() string`

GetClaimedBy returns the ClaimedBy field if non-nil, zero value otherwise.

### GetClaimedByOk

`func (o *BulkSubnetIPAddressRequest) GetClaimedByOk() (*string, bool)`

GetClaimedByOk returns a tuple with the ClaimedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClaimedBy

`func (o *BulkSubnetIPAddressRequest) SetClaimedBy(v string)`

SetClaimedBy sets ClaimedBy field to given value.

### HasClaimedBy

`func (o *BulkSubnetIPAddressRequest) HasClaimedBy() bool`

HasClaimedBy returns a boolean if a field has been set.

### SetClaimedByNil

`func (o *BulkSubnetIPAddressRequest) SetClaimedByNil(b bool)`

 SetClaimedByNil sets the value for ClaimedBy to be an explicit nil

### UnsetClaimedBy
`func (o *BulkSubnetIPAddressRequest) UnsetClaimedBy()`

UnsetClaimedBy ensures that no value is present for ClaimedBy, not even an explicit nil
### GetSubnetPrefix

`func (o *BulkSubnetIPAddressRequest) GetSubnetPrefix() int32`

GetSubnetPrefix returns the SubnetPrefix field if non-nil, zero value otherwise.

### GetSubnetPrefixOk

`func (o *BulkSubnetIPAddressRequest) GetSubnetPrefixOk() (*int32, bool)`

GetSubnetPrefixOk returns a tuple with the SubnetPrefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubnetPrefix

`func (o *BulkSubnetIPAddressRequest) SetSubnetPrefix(v int32)`

SetSubnetPrefix sets SubnetPrefix field to given value.


### GetTenant

`func (o *BulkSubnetIPAddressRequest) GetTenant() PatchedSubnetIPAddressRequestTenant`

GetTenant returns the Tenant field if non-nil, zero value otherwise.

### GetTenantOk

`func (o *BulkSubnetIPAddressRequest) GetTenantOk() (*PatchedSubnetIPAddressRequestTenant, bool)`

GetTenantOk returns a tuple with the Tenant field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTenant

`func (o *BulkSubnetIPAddressRequest) SetTenant(v PatchedSubnetIPAddressRequestTenant)`

SetTenant sets Tenant field to given value.

### HasTenant

`func (o *BulkSubnetIPAddressRequest) HasTenant() bool`

HasTenant returns a boolean if a field has been set.

### SetTenantNil

`func (o *BulkSubnetIPAddressRequest) SetTenantNil(b bool)`

 SetTenantNil sets the value for Tenant to be an explicit nil

### UnsetTenant
`func (o *BulkSubnetIPAddressRequest) UnsetTenant()`

UnsetTenant ensures that no value is present for Tenant, not even an explicit nil
### GetStatus

`func (o *BulkSubnetIPAddressRequest) GetStatus() PatchedSubnetIPAddressRequestStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *BulkSubnetIPAddressRequest) GetStatusOk() (*PatchedSubnetIPAddressRequestStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *BulkSubnetIPAddressRequest) SetStatus(v PatchedSubnetIPAddressRequestStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *BulkSubnetIPAddressRequest) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetRole

`func (o *BulkSubnetIPAddressRequest) GetRole() PatchedSubnetIPAddressRequestRole`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *BulkSubnetIPAddressRequest) GetRoleOk() (*PatchedSubnetIPAddressRequestRole, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *BulkSubnetIPAddressRequest) SetRole(v PatchedSubnetIPAddressRequestRole)`

SetRole sets Role field to given value.

### HasRole

`func (o *BulkSubnetIPAddressRequest) HasRole() bool`

HasRole returns a boolean if a field has been set.

### GetNatInside

`func (o *BulkSubnetIPAddressRequest) GetNatInside() NestedSubnetIPAddressRequest`

GetNatInside returns the NatInside field if non-nil, zero value otherwise.

### GetNatInsideOk

`func (o *BulkSubnetIPAddressRequest) GetNatInsideOk() (*NestedSubnetIPAddressRequest, bool)`

GetNatInsideOk returns a tuple with the NatInside field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNatInside

`func (o *BulkSubnetIPAddressRequest) SetNatInside(v NestedSubnetIPAddressRequest)`

SetNatInside sets NatInside field to given value.

### HasNatInside

`func (o *BulkSubnetIPAddressRequest) HasNatInside() bool`

HasNatInside returns a boolean if a field has been set.

### SetNatInsideNil

`func (o *BulkSubnetIPAddressRequest) SetNatInsideNil(b bool)`

 SetNatInsideNil sets the value for NatInside to be an explicit nil

### UnsetNatInside
`func (o *BulkSubnetIPAddressRequest) UnsetNatInside()`

UnsetNatInside ensures that no value is present for NatInside, not even an explicit nil
### GetDnsName

`func (o *BulkSubnetIPAddressRequest) GetDnsName() string`

GetDnsName returns the DnsName field if non-nil, zero value otherwise.

### GetDnsNameOk

`func (o *BulkSubnetIPAddressRequest) GetDnsNameOk() (*string, bool)`

GetDnsNameOk returns a tuple with the DnsName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDnsName

`func (o *BulkSubnetIPAddressRequest) SetDnsName(v string)`

SetDnsName sets DnsName field to given value.

### HasDnsName

`func (o *BulkSubnetIPAddressRequest) HasDnsName() bool`

HasDnsName returns a boolean if a field has been set.

### GetMetadata

`func (o *BulkSubnetIPAddressRequest) GetMetadata() interface{}`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *BulkSubnetIPAddressRequest) GetMetadataOk() (*interface{}, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *BulkSubnetIPAddressRequest) SetMetadata(v interface{})`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *BulkSubnetIPAddressRequest) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### SetMetadataNil

`func (o *BulkSubnetIPAddressRequest) SetMetadataNil(b bool)`

 SetMetadataNil sets the value for Metadata to be an explicit nil

### UnsetMetadata
`func (o *BulkSubnetIPAddressRequest) UnsetMetadata()`

UnsetMetadata ensures that no value is present for Metadata, not even an explicit nil
### GetHash

`func (o *BulkSubnetIPAddressRequest) GetHash() string`

GetHash returns the Hash field if non-nil, zero value otherwise.

### GetHashOk

`func (o *BulkSubnetIPAddressRequest) GetHashOk() (*string, bool)`

GetHashOk returns a tuple with the Hash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHash

`func (o *BulkSubnetIPAddressRequest) SetHash(v string)`

SetHash sets Hash field to given value.

### HasHash

`func (o *BulkSubnetIPAddressRequest) HasHash() bool`

HasHash returns a boolean if a field has been set.

### SetHashNil

`func (o *BulkSubnetIPAddressRequest) SetHashNil(b bool)`

 SetHashNil sets the value for Hash to be an explicit nil

### UnsetHash
`func (o *BulkSubnetIPAddressRequest) UnsetHash()`

UnsetHash ensures that no value is present for Hash, not even an explicit nil
### GetDescription

`func (o *BulkSubnetIPAddressRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *BulkSubnetIPAddressRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *BulkSubnetIPAddressRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *BulkSubnetIPAddressRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetComments

`func (o *BulkSubnetIPAddressRequest) GetComments() string`

GetComments returns the Comments field if non-nil, zero value otherwise.

### GetCommentsOk

`func (o *BulkSubnetIPAddressRequest) GetCommentsOk() (*string, bool)`

GetCommentsOk returns a tuple with the Comments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComments

`func (o *BulkSubnetIPAddressRequest) SetComments(v string)`

SetComments sets Comments field to given value.

### HasComments

`func (o *BulkSubnetIPAddressRequest) HasComments() bool`

HasComments returns a boolean if a field has been set.

### GetTags

`func (o *BulkSubnetIPAddressRequest) GetTags() []NestedTagRequest`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *BulkSubnetIPAddressRequest) GetTagsOk() (*[]NestedTagRequest, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTags

`func (o *BulkSubnetIPAddressRequest) SetTags(v []NestedTagRequest)`

SetTags sets Tags field to given value.

### HasTags

`func (o *BulkSubnetIPAddressRequest) HasTags() bool`

HasTags returns a boolean if a field has been set.

### GetCustomFields

`func (o *BulkSubnetIPAddressRequest) GetCustomFields() map[string]interface{}`

GetCustomFields returns the CustomFields field if non-nil, zero value otherwise.

### GetCustomFieldsOk

`func (o *BulkSubnetIPAddressRequest) GetCustomFieldsOk() (*map[string]interface{}, bool)`

GetCustomFieldsOk returns a tuple with the CustomFields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomFields

`func (o *BulkSubnetIPAddressRequest) SetCustomFields(v map[string]interface{})`

SetCustomFields sets CustomFields field to given value.

### HasCustomFields

`func (o *BulkSubnetIPAddressRequest) HasCustomFields() bool`

HasCustomFields returns a boolean if a field has been set.

### GetCrIpaddressClusterId

`func (o *BulkSubnetIPAddressRequest) GetCrIpaddressClusterId() string`

GetCrIpaddressClusterId returns the CrIpaddressClusterId field if non-nil, zero value otherwise.

### GetCrIpaddressClusterIdOk

`func (o *BulkSubnetIPAddressRequest) GetCrIpaddressClusterIdOk() (*string, bool)`

GetCrIpaddressClusterIdOk returns a tuple with the CrIpaddressClusterId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrIpaddressClusterId

`func (o *BulkSubnetIPAddressRequest) SetCrIpaddressClusterId(v string)`

SetCrIpaddressClusterId sets CrIpaddressClusterId field to given value.

### HasCrIpaddressClusterId

`func (o *BulkSubnetIPAddressRequest) HasCrIpaddressClusterId() bool`

HasCrIpaddressClusterId returns a boolean if a field has been set.

### SetCrIpaddressClusterIdNil

`func (o *BulkSubnetIPAddressRequest) SetCrIpaddressClusterIdNil(b bool)`

 SetCrIpaddressClusterIdNil sets the value for CrIpaddressClusterId to be an explicit nil

### UnsetCrIpaddressClusterId
`func (o *BulkSubnetIPAddressRequest) UnsetCrIpaddressClusterId()`

UnsetCrIpaddressClusterId ensures that no value is present for CrIpaddressClusterId, not even an explicit nil
### GetCrIpaddressName

`func (o *BulkSubnetIPAddressRequest) GetCrIpaddressName() string`

GetCrIpaddressName returns the CrIpaddressName field if non-nil, zero value otherwise.

### GetCrIpaddressNameOk

`func (o *BulkSubnetIPAddressRequest) GetCrIpaddressNameOk() (*string, bool)`

GetCrIpaddressNameOk returns a tuple with the CrIpaddressName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrIpaddressName

`func (o *BulkSubnetIPAddressRequest) SetCrIpaddressName(v string)`

SetCrIpaddressName sets CrIpaddressName field to given value.

### HasCrIpaddressName

`func (o *BulkSubnetIPAddressRequest) HasCrIpaddressName() bool`

HasCrIpaddressName returns a boolean if a field has been set.

### SetCrIpaddressNameNil

`func (o *BulkSubnetIPAddressRequest) SetCrIpaddressNameNil(b bool)`

 SetCrIpaddressNameNil sets the value for CrIpaddressName to be an explicit nil

### UnsetCrIpaddressName
`func (o *BulkSubnetIPAddressRequest) UnsetCrIpaddressName()`

UnsetCrIpaddressName ensures that no value is present for CrIpaddressName, not even an explicit nil
### GetCrIpaddressNamespace

`func (o *BulkSubnetIPAddressRequest) GetCrIpaddressNamespace() string`

GetCrIpaddressNamespace returns the CrIpaddressNamespace field if non-nil, zero value otherwise.

### GetCrIpaddressNamespaceOk

`func (o *BulkSubnetIPAddressRequest) GetCrIpaddressNamespaceOk() (*string, bool)`

GetCrIpaddressNamespaceOk returns a tuple with the CrIpaddressNamespace field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrIpaddressNamespace

`func (o *BulkSubnetIPAddressRequest) SetCrIpaddressNamespace(v string)`

SetCrIpaddressNamespace sets CrIpaddressNamespace field to given value.

### HasCrIpaddressNamespace

`func (o *BulkSubnetIPAddressRequest) HasCrIpaddressNamespace() bool`

HasCrIpaddressNamespace returns a boolean if a field has been set.

### SetCrIpaddressNamespaceNil

`func (o *BulkSubnetIPAddressRequest) SetCrIpaddressNamespaceNil(b bool)`

 SetCrIpaddressNamespaceNil sets the value for CrIpaddressNamespace to be an explicit nil

### UnsetCrIpaddressNamespace
`func (o *BulkSubnetIPAddressRequest) UnsetCrIpaddressNamespace()`

UnsetCrIpaddressNamespace ensures that no value is present for CrIpaddressNamespace, not even an explicit nil
### GetCrIpaddressclaimClusterId

`func (o *BulkSubnetIPAddressRequest) GetCrIpaddressclaimClusterId() string`

GetCrIpaddressclaimClusterId returns the CrIpaddressclaimClusterId field if non-nil, zero value otherwise.

### GetCrIpaddressclaimClusterIdOk

`func (o *BulkSubnetIPAddressRequest) GetCrIpaddressclaimClusterIdOk() (*string, bool)`

GetCrIpaddressclaimClusterIdOk returns a tuple with the CrIpaddressclaimClusterId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrIpaddressclaimClusterId

`func (o *BulkSubnetIPAddressRequest) SetCrIpaddressclaimClusterId(v string)`

SetCrIpaddressclaimClusterId sets CrIpaddressclaimClusterId field to given value.

### HasCrIpaddressclaimClusterId

`func (o *BulkSubnetIPAddressRequest) HasCrIpaddressclaimClusterId() bool`

HasCrIpaddressclaimClusterId returns a boolean if a field has been set.

### SetCrIpaddressclaimClusterIdNil

`func (o *BulkSubnetIPAddressRequest) SetCrIpaddressclaimClusterIdNil(b bool)`

 SetCrIpaddressclaimClusterIdNil sets the value for CrIpaddressclaimClusterId to be an explicit nil

### UnsetCrIpaddressclaimClusterId
`func (o *BulkSubnetIPAddressRequest) UnsetCrIpaddressclaimClusterId()`

UnsetCrIpaddressclaimClusterId ensures that no value is present for CrIpaddressclaimClusterId, not even an explicit nil
### GetCrIpaddressclaimName

`func (o *BulkSubnetIPAddressRequest) GetCrIpaddressclaimName() string`

GetCrIpaddressclaimName returns the CrIpaddressclaimName field if non-nil, zero value otherwise.

### GetCrIpaddressclaimNameOk

`func (o *BulkSubnetIPAddressRequest) GetCrIpaddressclaimNameOk() (*string, bool)`

GetCrIpaddressclaimNameOk returns a tuple with the CrIpaddressclaimName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrIpaddressclaimName

`func (o *BulkSubnetIPAddressRequest) SetCrIpaddressclaimName(v string)`

SetCrIpaddressclaimName sets CrIpaddressclaimName field to given value.

### HasCrIpaddressclaimName

`func (o *BulkSubnetIPAddressRequest) HasCrIpaddressclaimName() bool`

HasCrIpaddressclaimName returns a boolean if a field has been set.

### SetCrIpaddressclaimNameNil

`func (o *BulkSubnetIPAddressRequest) SetCrIpaddressclaimNameNil(b bool)`

 SetCrIpaddressclaimNameNil sets the value for CrIpaddressclaimName to be an explicit nil

### UnsetCrIpaddressclaimName
`func (o *BulkSubnetIPAddressRequest) UnsetCrIpaddressclaimName()`

UnsetCrIpaddressclaimName ensures that no value is present for CrIpaddressclaimName, not even an explicit nil
### GetCrIpaddressclaimNamespace

`func (o *BulkSubnetIPAddressRequest) GetCrIpaddressclaimNamespace() string`

GetCrIpaddressclaimNamespace returns the CrIpaddressclaimNamespace field if non-nil, zero value otherwise.

### GetCrIpaddressclaimNamespaceOk

`func (o *BulkSubnetIPAddressRequest) GetCrIpaddressclaimNamespaceOk() (*string, bool)`

GetCrIpaddressclaimNamespaceOk returns a tuple with the CrIpaddressclaimNamespace field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrIpaddressclaimNamespace

`func (o *BulkSubnetIPAddressRequest) SetCrIpaddressclaimNamespace(v string)`

SetCrIpaddressclaimNamespace sets CrIpaddressclaimNamespace field to given value.

### HasCrIpaddressclaimNamespace

`func (o *BulkSubnetIPAddressRequest) HasCrIpaddressclaimNamespace() bool`

HasCrIpaddressclaimNamespace returns a boolean if a field has been set.

### SetCrIpaddressclaimNamespaceNil

`func (o *BulkSubnetIPAddressRequest) SetCrIpaddressclaimNamespaceNil(b bool)`

 SetCrIpaddressclaimNamespaceNil sets the value for CrIpaddressclaimNamespace to be an explicit nil

### UnsetCrIpaddressclaimNamespace
`func (o *BulkSubnetIPAddressRequest) UnsetCrIpaddressclaimNamespace()`

UnsetCrIpaddressclaimNamespace ensures that no value is present for CrIpaddressclaimNamespace, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


