# BulkSubnetPrefixRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** |  | 
**Prefix** | **string** |  | 
**Label** | Pointer to **string** | Name of the Subnet | [optional] 
**IsSecondary** | Pointer to **bool** | Set Prefix subnet as secondary | [optional] 
**AutoReserveFirstIps** | Pointer to **bool** | Automatically reserve first IP addresses (network, gateway, etc.) | [optional] 
**AutoReserveLastIps** | Pointer to **bool** | Automatically reserve last IP addresses (broadcast, etc.) | [optional] 
**MarkUtilized** | Pointer to **bool** | Treat this prefix as fully utilized | [optional] 
**Status** | Pointer to [**NestedSubnetPrefixStatusValue**](NestedSubnetPrefixStatusValue.md) |  | [optional] 
**Metadata** | Pointer to **interface{}** |  | [optional] 
**Hash** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewBulkSubnetPrefixRequest

`func NewBulkSubnetPrefixRequest(id int32, prefix string, ) *BulkSubnetPrefixRequest`

NewBulkSubnetPrefixRequest instantiates a new BulkSubnetPrefixRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBulkSubnetPrefixRequestWithDefaults

`func NewBulkSubnetPrefixRequestWithDefaults() *BulkSubnetPrefixRequest`

NewBulkSubnetPrefixRequestWithDefaults instantiates a new BulkSubnetPrefixRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *BulkSubnetPrefixRequest) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *BulkSubnetPrefixRequest) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *BulkSubnetPrefixRequest) SetId(v int32)`

SetId sets Id field to given value.


### GetPrefix

`func (o *BulkSubnetPrefixRequest) GetPrefix() string`

GetPrefix returns the Prefix field if non-nil, zero value otherwise.

### GetPrefixOk

`func (o *BulkSubnetPrefixRequest) GetPrefixOk() (*string, bool)`

GetPrefixOk returns a tuple with the Prefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefix

`func (o *BulkSubnetPrefixRequest) SetPrefix(v string)`

SetPrefix sets Prefix field to given value.


### GetLabel

`func (o *BulkSubnetPrefixRequest) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *BulkSubnetPrefixRequest) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *BulkSubnetPrefixRequest) SetLabel(v string)`

SetLabel sets Label field to given value.

### HasLabel

`func (o *BulkSubnetPrefixRequest) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### GetIsSecondary

`func (o *BulkSubnetPrefixRequest) GetIsSecondary() bool`

GetIsSecondary returns the IsSecondary field if non-nil, zero value otherwise.

### GetIsSecondaryOk

`func (o *BulkSubnetPrefixRequest) GetIsSecondaryOk() (*bool, bool)`

GetIsSecondaryOk returns a tuple with the IsSecondary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsSecondary

`func (o *BulkSubnetPrefixRequest) SetIsSecondary(v bool)`

SetIsSecondary sets IsSecondary field to given value.

### HasIsSecondary

`func (o *BulkSubnetPrefixRequest) HasIsSecondary() bool`

HasIsSecondary returns a boolean if a field has been set.

### GetAutoReserveFirstIps

`func (o *BulkSubnetPrefixRequest) GetAutoReserveFirstIps() bool`

GetAutoReserveFirstIps returns the AutoReserveFirstIps field if non-nil, zero value otherwise.

### GetAutoReserveFirstIpsOk

`func (o *BulkSubnetPrefixRequest) GetAutoReserveFirstIpsOk() (*bool, bool)`

GetAutoReserveFirstIpsOk returns a tuple with the AutoReserveFirstIps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoReserveFirstIps

`func (o *BulkSubnetPrefixRequest) SetAutoReserveFirstIps(v bool)`

SetAutoReserveFirstIps sets AutoReserveFirstIps field to given value.

### HasAutoReserveFirstIps

`func (o *BulkSubnetPrefixRequest) HasAutoReserveFirstIps() bool`

HasAutoReserveFirstIps returns a boolean if a field has been set.

### GetAutoReserveLastIps

`func (o *BulkSubnetPrefixRequest) GetAutoReserveLastIps() bool`

GetAutoReserveLastIps returns the AutoReserveLastIps field if non-nil, zero value otherwise.

### GetAutoReserveLastIpsOk

`func (o *BulkSubnetPrefixRequest) GetAutoReserveLastIpsOk() (*bool, bool)`

GetAutoReserveLastIpsOk returns a tuple with the AutoReserveLastIps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoReserveLastIps

`func (o *BulkSubnetPrefixRequest) SetAutoReserveLastIps(v bool)`

SetAutoReserveLastIps sets AutoReserveLastIps field to given value.

### HasAutoReserveLastIps

`func (o *BulkSubnetPrefixRequest) HasAutoReserveLastIps() bool`

HasAutoReserveLastIps returns a boolean if a field has been set.

### GetMarkUtilized

`func (o *BulkSubnetPrefixRequest) GetMarkUtilized() bool`

GetMarkUtilized returns the MarkUtilized field if non-nil, zero value otherwise.

### GetMarkUtilizedOk

`func (o *BulkSubnetPrefixRequest) GetMarkUtilizedOk() (*bool, bool)`

GetMarkUtilizedOk returns a tuple with the MarkUtilized field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMarkUtilized

`func (o *BulkSubnetPrefixRequest) SetMarkUtilized(v bool)`

SetMarkUtilized sets MarkUtilized field to given value.

### HasMarkUtilized

`func (o *BulkSubnetPrefixRequest) HasMarkUtilized() bool`

HasMarkUtilized returns a boolean if a field has been set.

### GetStatus

`func (o *BulkSubnetPrefixRequest) GetStatus() NestedSubnetPrefixStatusValue`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *BulkSubnetPrefixRequest) GetStatusOk() (*NestedSubnetPrefixStatusValue, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *BulkSubnetPrefixRequest) SetStatus(v NestedSubnetPrefixStatusValue)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *BulkSubnetPrefixRequest) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetMetadata

`func (o *BulkSubnetPrefixRequest) GetMetadata() interface{}`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *BulkSubnetPrefixRequest) GetMetadataOk() (*interface{}, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *BulkSubnetPrefixRequest) SetMetadata(v interface{})`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *BulkSubnetPrefixRequest) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### SetMetadataNil

`func (o *BulkSubnetPrefixRequest) SetMetadataNil(b bool)`

 SetMetadataNil sets the value for Metadata to be an explicit nil

### UnsetMetadata
`func (o *BulkSubnetPrefixRequest) UnsetMetadata()`

UnsetMetadata ensures that no value is present for Metadata, not even an explicit nil
### GetHash

`func (o *BulkSubnetPrefixRequest) GetHash() string`

GetHash returns the Hash field if non-nil, zero value otherwise.

### GetHashOk

`func (o *BulkSubnetPrefixRequest) GetHashOk() (*string, bool)`

GetHashOk returns a tuple with the Hash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHash

`func (o *BulkSubnetPrefixRequest) SetHash(v string)`

SetHash sets Hash field to given value.

### HasHash

`func (o *BulkSubnetPrefixRequest) HasHash() bool`

HasHash returns a boolean if a field has been set.

### SetHashNil

`func (o *BulkSubnetPrefixRequest) SetHashNil(b bool)`

 SetHashNil sets the value for Hash to be an explicit nil

### UnsetHash
`func (o *BulkSubnetPrefixRequest) UnsetHash()`

UnsetHash ensures that no value is present for Hash, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


