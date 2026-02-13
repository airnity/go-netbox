# SubnetPrefixForSubnet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** |  | [readonly] 
**Url** | **string** |  | [readonly] 
**Display** | **string** |  | [readonly] 
**Prefix** | **string** |  | 
**Label** | Pointer to **string** | Name of the Subnet | [optional] 
**IsSecondary** | Pointer to **bool** | Set Prefix subnet as secondary | [optional] 
**AutoReserveFirstIps** | Pointer to **bool** | Automatically reserve first IP addresses (network, gateway, etc.) | [optional] 
**AutoReserveLastIps** | Pointer to **bool** | Automatically reserve last IP addresses (broadcast, etc.) | [optional] 
**Status** | **map[string]interface{}** |  | [readonly] 
**Description** | Pointer to **string** |  | [optional] 
**Comments** | Pointer to **string** |  | [optional] 

## Methods

### NewSubnetPrefixForSubnet

`func NewSubnetPrefixForSubnet(id int32, url string, display string, prefix string, status map[string]interface{}, ) *SubnetPrefixForSubnet`

NewSubnetPrefixForSubnet instantiates a new SubnetPrefixForSubnet object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSubnetPrefixForSubnetWithDefaults

`func NewSubnetPrefixForSubnetWithDefaults() *SubnetPrefixForSubnet`

NewSubnetPrefixForSubnetWithDefaults instantiates a new SubnetPrefixForSubnet object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SubnetPrefixForSubnet) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SubnetPrefixForSubnet) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SubnetPrefixForSubnet) SetId(v int32)`

SetId sets Id field to given value.


### GetUrl

`func (o *SubnetPrefixForSubnet) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *SubnetPrefixForSubnet) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *SubnetPrefixForSubnet) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetDisplay

`func (o *SubnetPrefixForSubnet) GetDisplay() string`

GetDisplay returns the Display field if non-nil, zero value otherwise.

### GetDisplayOk

`func (o *SubnetPrefixForSubnet) GetDisplayOk() (*string, bool)`

GetDisplayOk returns a tuple with the Display field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplay

`func (o *SubnetPrefixForSubnet) SetDisplay(v string)`

SetDisplay sets Display field to given value.


### GetPrefix

`func (o *SubnetPrefixForSubnet) GetPrefix() string`

GetPrefix returns the Prefix field if non-nil, zero value otherwise.

### GetPrefixOk

`func (o *SubnetPrefixForSubnet) GetPrefixOk() (*string, bool)`

GetPrefixOk returns a tuple with the Prefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefix

`func (o *SubnetPrefixForSubnet) SetPrefix(v string)`

SetPrefix sets Prefix field to given value.


### GetLabel

`func (o *SubnetPrefixForSubnet) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *SubnetPrefixForSubnet) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *SubnetPrefixForSubnet) SetLabel(v string)`

SetLabel sets Label field to given value.

### HasLabel

`func (o *SubnetPrefixForSubnet) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### GetIsSecondary

`func (o *SubnetPrefixForSubnet) GetIsSecondary() bool`

GetIsSecondary returns the IsSecondary field if non-nil, zero value otherwise.

### GetIsSecondaryOk

`func (o *SubnetPrefixForSubnet) GetIsSecondaryOk() (*bool, bool)`

GetIsSecondaryOk returns a tuple with the IsSecondary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsSecondary

`func (o *SubnetPrefixForSubnet) SetIsSecondary(v bool)`

SetIsSecondary sets IsSecondary field to given value.

### HasIsSecondary

`func (o *SubnetPrefixForSubnet) HasIsSecondary() bool`

HasIsSecondary returns a boolean if a field has been set.

### GetAutoReserveFirstIps

`func (o *SubnetPrefixForSubnet) GetAutoReserveFirstIps() bool`

GetAutoReserveFirstIps returns the AutoReserveFirstIps field if non-nil, zero value otherwise.

### GetAutoReserveFirstIpsOk

`func (o *SubnetPrefixForSubnet) GetAutoReserveFirstIpsOk() (*bool, bool)`

GetAutoReserveFirstIpsOk returns a tuple with the AutoReserveFirstIps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoReserveFirstIps

`func (o *SubnetPrefixForSubnet) SetAutoReserveFirstIps(v bool)`

SetAutoReserveFirstIps sets AutoReserveFirstIps field to given value.

### HasAutoReserveFirstIps

`func (o *SubnetPrefixForSubnet) HasAutoReserveFirstIps() bool`

HasAutoReserveFirstIps returns a boolean if a field has been set.

### GetAutoReserveLastIps

`func (o *SubnetPrefixForSubnet) GetAutoReserveLastIps() bool`

GetAutoReserveLastIps returns the AutoReserveLastIps field if non-nil, zero value otherwise.

### GetAutoReserveLastIpsOk

`func (o *SubnetPrefixForSubnet) GetAutoReserveLastIpsOk() (*bool, bool)`

GetAutoReserveLastIpsOk returns a tuple with the AutoReserveLastIps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoReserveLastIps

`func (o *SubnetPrefixForSubnet) SetAutoReserveLastIps(v bool)`

SetAutoReserveLastIps sets AutoReserveLastIps field to given value.

### HasAutoReserveLastIps

`func (o *SubnetPrefixForSubnet) HasAutoReserveLastIps() bool`

HasAutoReserveLastIps returns a boolean if a field has been set.

### GetStatus

`func (o *SubnetPrefixForSubnet) GetStatus() map[string]interface{}`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *SubnetPrefixForSubnet) GetStatusOk() (*map[string]interface{}, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *SubnetPrefixForSubnet) SetStatus(v map[string]interface{})`

SetStatus sets Status field to given value.


### GetDescription

`func (o *SubnetPrefixForSubnet) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *SubnetPrefixForSubnet) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *SubnetPrefixForSubnet) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *SubnetPrefixForSubnet) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetComments

`func (o *SubnetPrefixForSubnet) GetComments() string`

GetComments returns the Comments field if non-nil, zero value otherwise.

### GetCommentsOk

`func (o *SubnetPrefixForSubnet) GetCommentsOk() (*string, bool)`

GetCommentsOk returns a tuple with the Comments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComments

`func (o *SubnetPrefixForSubnet) SetComments(v string)`

SetComments sets Comments field to given value.

### HasComments

`func (o *SubnetPrefixForSubnet) HasComments() bool`

HasComments returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


