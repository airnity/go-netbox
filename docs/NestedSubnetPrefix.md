# NestedSubnetPrefix

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
**MarkUtilized** | Pointer to **bool** | Treat this prefix as fully utilized | [optional] 
**Status** | Pointer to [**NestedSubnetPrefixStatus**](NestedSubnetPrefixStatus.md) |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**Comments** | Pointer to **string** |  | [optional] 

## Methods

### NewNestedSubnetPrefix

`func NewNestedSubnetPrefix(id int32, url string, display string, prefix string, ) *NestedSubnetPrefix`

NewNestedSubnetPrefix instantiates a new NestedSubnetPrefix object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewNestedSubnetPrefixWithDefaults

`func NewNestedSubnetPrefixWithDefaults() *NestedSubnetPrefix`

NewNestedSubnetPrefixWithDefaults instantiates a new NestedSubnetPrefix object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *NestedSubnetPrefix) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *NestedSubnetPrefix) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *NestedSubnetPrefix) SetId(v int32)`

SetId sets Id field to given value.


### GetUrl

`func (o *NestedSubnetPrefix) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *NestedSubnetPrefix) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *NestedSubnetPrefix) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetDisplay

`func (o *NestedSubnetPrefix) GetDisplay() string`

GetDisplay returns the Display field if non-nil, zero value otherwise.

### GetDisplayOk

`func (o *NestedSubnetPrefix) GetDisplayOk() (*string, bool)`

GetDisplayOk returns a tuple with the Display field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplay

`func (o *NestedSubnetPrefix) SetDisplay(v string)`

SetDisplay sets Display field to given value.


### GetPrefix

`func (o *NestedSubnetPrefix) GetPrefix() string`

GetPrefix returns the Prefix field if non-nil, zero value otherwise.

### GetPrefixOk

`func (o *NestedSubnetPrefix) GetPrefixOk() (*string, bool)`

GetPrefixOk returns a tuple with the Prefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefix

`func (o *NestedSubnetPrefix) SetPrefix(v string)`

SetPrefix sets Prefix field to given value.


### GetLabel

`func (o *NestedSubnetPrefix) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *NestedSubnetPrefix) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *NestedSubnetPrefix) SetLabel(v string)`

SetLabel sets Label field to given value.

### HasLabel

`func (o *NestedSubnetPrefix) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### GetIsSecondary

`func (o *NestedSubnetPrefix) GetIsSecondary() bool`

GetIsSecondary returns the IsSecondary field if non-nil, zero value otherwise.

### GetIsSecondaryOk

`func (o *NestedSubnetPrefix) GetIsSecondaryOk() (*bool, bool)`

GetIsSecondaryOk returns a tuple with the IsSecondary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsSecondary

`func (o *NestedSubnetPrefix) SetIsSecondary(v bool)`

SetIsSecondary sets IsSecondary field to given value.

### HasIsSecondary

`func (o *NestedSubnetPrefix) HasIsSecondary() bool`

HasIsSecondary returns a boolean if a field has been set.

### GetAutoReserveFirstIps

`func (o *NestedSubnetPrefix) GetAutoReserveFirstIps() bool`

GetAutoReserveFirstIps returns the AutoReserveFirstIps field if non-nil, zero value otherwise.

### GetAutoReserveFirstIpsOk

`func (o *NestedSubnetPrefix) GetAutoReserveFirstIpsOk() (*bool, bool)`

GetAutoReserveFirstIpsOk returns a tuple with the AutoReserveFirstIps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoReserveFirstIps

`func (o *NestedSubnetPrefix) SetAutoReserveFirstIps(v bool)`

SetAutoReserveFirstIps sets AutoReserveFirstIps field to given value.

### HasAutoReserveFirstIps

`func (o *NestedSubnetPrefix) HasAutoReserveFirstIps() bool`

HasAutoReserveFirstIps returns a boolean if a field has been set.

### GetAutoReserveLastIps

`func (o *NestedSubnetPrefix) GetAutoReserveLastIps() bool`

GetAutoReserveLastIps returns the AutoReserveLastIps field if non-nil, zero value otherwise.

### GetAutoReserveLastIpsOk

`func (o *NestedSubnetPrefix) GetAutoReserveLastIpsOk() (*bool, bool)`

GetAutoReserveLastIpsOk returns a tuple with the AutoReserveLastIps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoReserveLastIps

`func (o *NestedSubnetPrefix) SetAutoReserveLastIps(v bool)`

SetAutoReserveLastIps sets AutoReserveLastIps field to given value.

### HasAutoReserveLastIps

`func (o *NestedSubnetPrefix) HasAutoReserveLastIps() bool`

HasAutoReserveLastIps returns a boolean if a field has been set.

### GetMarkUtilized

`func (o *NestedSubnetPrefix) GetMarkUtilized() bool`

GetMarkUtilized returns the MarkUtilized field if non-nil, zero value otherwise.

### GetMarkUtilizedOk

`func (o *NestedSubnetPrefix) GetMarkUtilizedOk() (*bool, bool)`

GetMarkUtilizedOk returns a tuple with the MarkUtilized field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMarkUtilized

`func (o *NestedSubnetPrefix) SetMarkUtilized(v bool)`

SetMarkUtilized sets MarkUtilized field to given value.

### HasMarkUtilized

`func (o *NestedSubnetPrefix) HasMarkUtilized() bool`

HasMarkUtilized returns a boolean if a field has been set.

### GetStatus

`func (o *NestedSubnetPrefix) GetStatus() NestedSubnetPrefixStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *NestedSubnetPrefix) GetStatusOk() (*NestedSubnetPrefixStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *NestedSubnetPrefix) SetStatus(v NestedSubnetPrefixStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *NestedSubnetPrefix) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetDescription

`func (o *NestedSubnetPrefix) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *NestedSubnetPrefix) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *NestedSubnetPrefix) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *NestedSubnetPrefix) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetComments

`func (o *NestedSubnetPrefix) GetComments() string`

GetComments returns the Comments field if non-nil, zero value otherwise.

### GetCommentsOk

`func (o *NestedSubnetPrefix) GetCommentsOk() (*string, bool)`

GetCommentsOk returns a tuple with the Comments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComments

`func (o *NestedSubnetPrefix) SetComments(v string)`

SetComments sets Comments field to given value.

### HasComments

`func (o *NestedSubnetPrefix) HasComments() bool`

HasComments returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


