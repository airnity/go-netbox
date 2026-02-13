# PluginsAirnityIpamSubnetprefixCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Prefix** | **string** |  | 
**Label** | Pointer to **string** | Name of the Subnet | [optional] 
**IsSecondary** | Pointer to **bool** | Set Prefix subnet as secondary | [optional] 
**AutoReserveFirstIps** | Pointer to **bool** | Automatically reserve first IP addresses (network, gateway, etc.) | [optional] 
**AutoReserveLastIps** | Pointer to **bool** | Automatically reserve last IP addresses (broadcast, etc.) | [optional] 
**MarkUtilized** | Pointer to **bool** | Treat this prefix as fully utilized | [optional] 
**Status** | Pointer to [**PatchedWritableSubnetPrefixRequestStatus**](PatchedWritableSubnetPrefixRequestStatus.md) |  | [optional] 

## Methods

### NewPluginsAirnityIpamSubnetprefixCreateRequest

`func NewPluginsAirnityIpamSubnetprefixCreateRequest(prefix string, ) *PluginsAirnityIpamSubnetprefixCreateRequest`

NewPluginsAirnityIpamSubnetprefixCreateRequest instantiates a new PluginsAirnityIpamSubnetprefixCreateRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPluginsAirnityIpamSubnetprefixCreateRequestWithDefaults

`func NewPluginsAirnityIpamSubnetprefixCreateRequestWithDefaults() *PluginsAirnityIpamSubnetprefixCreateRequest`

NewPluginsAirnityIpamSubnetprefixCreateRequestWithDefaults instantiates a new PluginsAirnityIpamSubnetprefixCreateRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPrefix

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) GetPrefix() string`

GetPrefix returns the Prefix field if non-nil, zero value otherwise.

### GetPrefixOk

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) GetPrefixOk() (*string, bool)`

GetPrefixOk returns a tuple with the Prefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefix

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) SetPrefix(v string)`

SetPrefix sets Prefix field to given value.


### GetLabel

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) SetLabel(v string)`

SetLabel sets Label field to given value.

### HasLabel

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### GetIsSecondary

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) GetIsSecondary() bool`

GetIsSecondary returns the IsSecondary field if non-nil, zero value otherwise.

### GetIsSecondaryOk

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) GetIsSecondaryOk() (*bool, bool)`

GetIsSecondaryOk returns a tuple with the IsSecondary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsSecondary

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) SetIsSecondary(v bool)`

SetIsSecondary sets IsSecondary field to given value.

### HasIsSecondary

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) HasIsSecondary() bool`

HasIsSecondary returns a boolean if a field has been set.

### GetAutoReserveFirstIps

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) GetAutoReserveFirstIps() bool`

GetAutoReserveFirstIps returns the AutoReserveFirstIps field if non-nil, zero value otherwise.

### GetAutoReserveFirstIpsOk

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) GetAutoReserveFirstIpsOk() (*bool, bool)`

GetAutoReserveFirstIpsOk returns a tuple with the AutoReserveFirstIps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoReserveFirstIps

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) SetAutoReserveFirstIps(v bool)`

SetAutoReserveFirstIps sets AutoReserveFirstIps field to given value.

### HasAutoReserveFirstIps

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) HasAutoReserveFirstIps() bool`

HasAutoReserveFirstIps returns a boolean if a field has been set.

### GetAutoReserveLastIps

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) GetAutoReserveLastIps() bool`

GetAutoReserveLastIps returns the AutoReserveLastIps field if non-nil, zero value otherwise.

### GetAutoReserveLastIpsOk

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) GetAutoReserveLastIpsOk() (*bool, bool)`

GetAutoReserveLastIpsOk returns a tuple with the AutoReserveLastIps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoReserveLastIps

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) SetAutoReserveLastIps(v bool)`

SetAutoReserveLastIps sets AutoReserveLastIps field to given value.

### HasAutoReserveLastIps

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) HasAutoReserveLastIps() bool`

HasAutoReserveLastIps returns a boolean if a field has been set.

### GetMarkUtilized

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) GetMarkUtilized() bool`

GetMarkUtilized returns the MarkUtilized field if non-nil, zero value otherwise.

### GetMarkUtilizedOk

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) GetMarkUtilizedOk() (*bool, bool)`

GetMarkUtilizedOk returns a tuple with the MarkUtilized field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMarkUtilized

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) SetMarkUtilized(v bool)`

SetMarkUtilized sets MarkUtilized field to given value.

### HasMarkUtilized

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) HasMarkUtilized() bool`

HasMarkUtilized returns a boolean if a field has been set.

### GetStatus

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) GetStatus() PatchedWritableSubnetPrefixRequestStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) GetStatusOk() (*PatchedWritableSubnetPrefixRequestStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) SetStatus(v PatchedWritableSubnetPrefixRequestStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *PluginsAirnityIpamSubnetprefixCreateRequest) HasStatus() bool`

HasStatus returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


