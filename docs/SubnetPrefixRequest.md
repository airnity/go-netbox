# SubnetPrefixRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Prefix** | **string** |  | 
**Label** | Pointer to **string** | Name of the Subnet | [optional] 
**IsSecondary** | Pointer to **bool** | Set Prefix subnet as secondary | [optional] 
**AutoReserveIps** | Pointer to **bool** | Automatically reserve IP addresses based on plugin configuration | [optional] 
**MarkUtilized** | Pointer to **bool** | Treat this prefix as fully utilized | [optional] 
**Status** | Pointer to [**NestedSubnetPrefixStatusValue**](NestedSubnetPrefixStatusValue.md) |  | [optional] 

## Methods

### NewSubnetPrefixRequest

`func NewSubnetPrefixRequest(prefix string, ) *SubnetPrefixRequest`

NewSubnetPrefixRequest instantiates a new SubnetPrefixRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSubnetPrefixRequestWithDefaults

`func NewSubnetPrefixRequestWithDefaults() *SubnetPrefixRequest`

NewSubnetPrefixRequestWithDefaults instantiates a new SubnetPrefixRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPrefix

`func (o *SubnetPrefixRequest) GetPrefix() string`

GetPrefix returns the Prefix field if non-nil, zero value otherwise.

### GetPrefixOk

`func (o *SubnetPrefixRequest) GetPrefixOk() (*string, bool)`

GetPrefixOk returns a tuple with the Prefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefix

`func (o *SubnetPrefixRequest) SetPrefix(v string)`

SetPrefix sets Prefix field to given value.


### GetLabel

`func (o *SubnetPrefixRequest) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *SubnetPrefixRequest) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *SubnetPrefixRequest) SetLabel(v string)`

SetLabel sets Label field to given value.

### HasLabel

`func (o *SubnetPrefixRequest) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### GetIsSecondary

`func (o *SubnetPrefixRequest) GetIsSecondary() bool`

GetIsSecondary returns the IsSecondary field if non-nil, zero value otherwise.

### GetIsSecondaryOk

`func (o *SubnetPrefixRequest) GetIsSecondaryOk() (*bool, bool)`

GetIsSecondaryOk returns a tuple with the IsSecondary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsSecondary

`func (o *SubnetPrefixRequest) SetIsSecondary(v bool)`

SetIsSecondary sets IsSecondary field to given value.

### HasIsSecondary

`func (o *SubnetPrefixRequest) HasIsSecondary() bool`

HasIsSecondary returns a boolean if a field has been set.

### GetAutoReserveIps

`func (o *SubnetPrefixRequest) GetAutoReserveIps() bool`

GetAutoReserveIps returns the AutoReserveIps field if non-nil, zero value otherwise.

### GetAutoReserveIpsOk

`func (o *SubnetPrefixRequest) GetAutoReserveIpsOk() (*bool, bool)`

GetAutoReserveIpsOk returns a tuple with the AutoReserveIps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoReserveIps

`func (o *SubnetPrefixRequest) SetAutoReserveIps(v bool)`

SetAutoReserveIps sets AutoReserveIps field to given value.

### HasAutoReserveIps

`func (o *SubnetPrefixRequest) HasAutoReserveIps() bool`

HasAutoReserveIps returns a boolean if a field has been set.

### GetMarkUtilized

`func (o *SubnetPrefixRequest) GetMarkUtilized() bool`

GetMarkUtilized returns the MarkUtilized field if non-nil, zero value otherwise.

### GetMarkUtilizedOk

`func (o *SubnetPrefixRequest) GetMarkUtilizedOk() (*bool, bool)`

GetMarkUtilizedOk returns a tuple with the MarkUtilized field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMarkUtilized

`func (o *SubnetPrefixRequest) SetMarkUtilized(v bool)`

SetMarkUtilized sets MarkUtilized field to given value.

### HasMarkUtilized

`func (o *SubnetPrefixRequest) HasMarkUtilized() bool`

HasMarkUtilized returns a boolean if a field has been set.

### GetStatus

`func (o *SubnetPrefixRequest) GetStatus() NestedSubnetPrefixStatusValue`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *SubnetPrefixRequest) GetStatusOk() (*NestedSubnetPrefixStatusValue, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *SubnetPrefixRequest) SetStatus(v NestedSubnetPrefixStatusValue)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *SubnetPrefixRequest) HasStatus() bool`

HasStatus returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


