# SubnetPrefix

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** |  | [readonly] 
**Url** | **string** |  | [readonly] 
**Display** | **string** |  | [readonly] 
**Subnet** | [**NestedSubnet**](NestedSubnet.md) |  | [readonly] 
**Vpc** | Pointer to [**NullableBriefVPC**](BriefVPC.md) |  | [optional] [readonly] 
**Prefix** | **string** |  | 
**Label** | Pointer to **string** | Name of the Subnet | [optional] 
**IsSecondary** | Pointer to **bool** | Set Prefix subnet as secondary | [optional] 
**AutoReserveIps** | Pointer to **bool** | Automatically reserve IP addresses based on plugin configuration | [optional] 
**MarkUtilized** | Pointer to **bool** | Treat this prefix as fully utilized | [optional] 
**Status** | Pointer to [**NestedSubnetPrefixStatus**](NestedSubnetPrefixStatus.md) |  | [optional] 
**Family** | **int32** |  | [readonly] 
**Created** | Pointer to **NullableTime** |  | [optional] [readonly] 
**LastUpdated** | Pointer to **NullableTime** |  | [optional] [readonly] 

## Methods

### NewSubnetPrefix

`func NewSubnetPrefix(id int32, url string, display string, subnet NestedSubnet, prefix string, family int32, ) *SubnetPrefix`

NewSubnetPrefix instantiates a new SubnetPrefix object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSubnetPrefixWithDefaults

`func NewSubnetPrefixWithDefaults() *SubnetPrefix`

NewSubnetPrefixWithDefaults instantiates a new SubnetPrefix object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SubnetPrefix) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SubnetPrefix) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SubnetPrefix) SetId(v int32)`

SetId sets Id field to given value.


### GetUrl

`func (o *SubnetPrefix) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *SubnetPrefix) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *SubnetPrefix) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetDisplay

`func (o *SubnetPrefix) GetDisplay() string`

GetDisplay returns the Display field if non-nil, zero value otherwise.

### GetDisplayOk

`func (o *SubnetPrefix) GetDisplayOk() (*string, bool)`

GetDisplayOk returns a tuple with the Display field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplay

`func (o *SubnetPrefix) SetDisplay(v string)`

SetDisplay sets Display field to given value.


### GetSubnet

`func (o *SubnetPrefix) GetSubnet() NestedSubnet`

GetSubnet returns the Subnet field if non-nil, zero value otherwise.

### GetSubnetOk

`func (o *SubnetPrefix) GetSubnetOk() (*NestedSubnet, bool)`

GetSubnetOk returns a tuple with the Subnet field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubnet

`func (o *SubnetPrefix) SetSubnet(v NestedSubnet)`

SetSubnet sets Subnet field to given value.


### GetVpc

`func (o *SubnetPrefix) GetVpc() BriefVPC`

GetVpc returns the Vpc field if non-nil, zero value otherwise.

### GetVpcOk

`func (o *SubnetPrefix) GetVpcOk() (*BriefVPC, bool)`

GetVpcOk returns a tuple with the Vpc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVpc

`func (o *SubnetPrefix) SetVpc(v BriefVPC)`

SetVpc sets Vpc field to given value.

### HasVpc

`func (o *SubnetPrefix) HasVpc() bool`

HasVpc returns a boolean if a field has been set.

### SetVpcNil

`func (o *SubnetPrefix) SetVpcNil(b bool)`

 SetVpcNil sets the value for Vpc to be an explicit nil

### UnsetVpc
`func (o *SubnetPrefix) UnsetVpc()`

UnsetVpc ensures that no value is present for Vpc, not even an explicit nil
### GetPrefix

`func (o *SubnetPrefix) GetPrefix() string`

GetPrefix returns the Prefix field if non-nil, zero value otherwise.

### GetPrefixOk

`func (o *SubnetPrefix) GetPrefixOk() (*string, bool)`

GetPrefixOk returns a tuple with the Prefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefix

`func (o *SubnetPrefix) SetPrefix(v string)`

SetPrefix sets Prefix field to given value.


### GetLabel

`func (o *SubnetPrefix) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *SubnetPrefix) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *SubnetPrefix) SetLabel(v string)`

SetLabel sets Label field to given value.

### HasLabel

`func (o *SubnetPrefix) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### GetIsSecondary

`func (o *SubnetPrefix) GetIsSecondary() bool`

GetIsSecondary returns the IsSecondary field if non-nil, zero value otherwise.

### GetIsSecondaryOk

`func (o *SubnetPrefix) GetIsSecondaryOk() (*bool, bool)`

GetIsSecondaryOk returns a tuple with the IsSecondary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsSecondary

`func (o *SubnetPrefix) SetIsSecondary(v bool)`

SetIsSecondary sets IsSecondary field to given value.

### HasIsSecondary

`func (o *SubnetPrefix) HasIsSecondary() bool`

HasIsSecondary returns a boolean if a field has been set.

### GetAutoReserveIps

`func (o *SubnetPrefix) GetAutoReserveIps() bool`

GetAutoReserveIps returns the AutoReserveIps field if non-nil, zero value otherwise.

### GetAutoReserveIpsOk

`func (o *SubnetPrefix) GetAutoReserveIpsOk() (*bool, bool)`

GetAutoReserveIpsOk returns a tuple with the AutoReserveIps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoReserveIps

`func (o *SubnetPrefix) SetAutoReserveIps(v bool)`

SetAutoReserveIps sets AutoReserveIps field to given value.

### HasAutoReserveIps

`func (o *SubnetPrefix) HasAutoReserveIps() bool`

HasAutoReserveIps returns a boolean if a field has been set.

### GetMarkUtilized

`func (o *SubnetPrefix) GetMarkUtilized() bool`

GetMarkUtilized returns the MarkUtilized field if non-nil, zero value otherwise.

### GetMarkUtilizedOk

`func (o *SubnetPrefix) GetMarkUtilizedOk() (*bool, bool)`

GetMarkUtilizedOk returns a tuple with the MarkUtilized field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMarkUtilized

`func (o *SubnetPrefix) SetMarkUtilized(v bool)`

SetMarkUtilized sets MarkUtilized field to given value.

### HasMarkUtilized

`func (o *SubnetPrefix) HasMarkUtilized() bool`

HasMarkUtilized returns a boolean if a field has been set.

### GetStatus

`func (o *SubnetPrefix) GetStatus() NestedSubnetPrefixStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *SubnetPrefix) GetStatusOk() (*NestedSubnetPrefixStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *SubnetPrefix) SetStatus(v NestedSubnetPrefixStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *SubnetPrefix) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetFamily

`func (o *SubnetPrefix) GetFamily() int32`

GetFamily returns the Family field if non-nil, zero value otherwise.

### GetFamilyOk

`func (o *SubnetPrefix) GetFamilyOk() (*int32, bool)`

GetFamilyOk returns a tuple with the Family field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFamily

`func (o *SubnetPrefix) SetFamily(v int32)`

SetFamily sets Family field to given value.


### GetCreated

`func (o *SubnetPrefix) GetCreated() time.Time`

GetCreated returns the Created field if non-nil, zero value otherwise.

### GetCreatedOk

`func (o *SubnetPrefix) GetCreatedOk() (*time.Time, bool)`

GetCreatedOk returns a tuple with the Created field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreated

`func (o *SubnetPrefix) SetCreated(v time.Time)`

SetCreated sets Created field to given value.

### HasCreated

`func (o *SubnetPrefix) HasCreated() bool`

HasCreated returns a boolean if a field has been set.

### SetCreatedNil

`func (o *SubnetPrefix) SetCreatedNil(b bool)`

 SetCreatedNil sets the value for Created to be an explicit nil

### UnsetCreated
`func (o *SubnetPrefix) UnsetCreated()`

UnsetCreated ensures that no value is present for Created, not even an explicit nil
### GetLastUpdated

`func (o *SubnetPrefix) GetLastUpdated() time.Time`

GetLastUpdated returns the LastUpdated field if non-nil, zero value otherwise.

### GetLastUpdatedOk

`func (o *SubnetPrefix) GetLastUpdatedOk() (*time.Time, bool)`

GetLastUpdatedOk returns a tuple with the LastUpdated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastUpdated

`func (o *SubnetPrefix) SetLastUpdated(v time.Time)`

SetLastUpdated sets LastUpdated field to given value.

### HasLastUpdated

`func (o *SubnetPrefix) HasLastUpdated() bool`

HasLastUpdated returns a boolean if a field has been set.

### SetLastUpdatedNil

`func (o *SubnetPrefix) SetLastUpdatedNil(b bool)`

 SetLastUpdatedNil sets the value for LastUpdated to be an explicit nil

### UnsetLastUpdated
`func (o *SubnetPrefix) UnsetLastUpdated()`

UnsetLastUpdated ensures that no value is present for LastUpdated, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


