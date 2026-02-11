# WritableNestedSubnetPrefix

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **NullableInt32** |  | [optional] 
**Prefix** | **string** |  | 
**Label** | Pointer to **string** | Name of the Subnet | [optional] 
**IsSecondary** | Pointer to **bool** | Set Prefix subnet as secondary | [optional] 
**AutoReserveIps** | Pointer to **bool** | Automatically reserve IPs based on plugin configuration | [optional] [default to false]
**MarkUtilized** | Pointer to **bool** | Treat this prefix as fully utilized | [optional] 
**Status** | Pointer to [**NestedSubnetPrefixStatus**](NestedSubnetPrefixStatus.md) |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**Comments** | Pointer to **string** |  | [optional] 

## Methods

### NewWritableNestedSubnetPrefix

`func NewWritableNestedSubnetPrefix(prefix string, ) *WritableNestedSubnetPrefix`

NewWritableNestedSubnetPrefix instantiates a new WritableNestedSubnetPrefix object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWritableNestedSubnetPrefixWithDefaults

`func NewWritableNestedSubnetPrefixWithDefaults() *WritableNestedSubnetPrefix`

NewWritableNestedSubnetPrefixWithDefaults instantiates a new WritableNestedSubnetPrefix object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *WritableNestedSubnetPrefix) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *WritableNestedSubnetPrefix) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *WritableNestedSubnetPrefix) SetId(v int32)`

SetId sets Id field to given value.

### HasId

`func (o *WritableNestedSubnetPrefix) HasId() bool`

HasId returns a boolean if a field has been set.

### SetIdNil

`func (o *WritableNestedSubnetPrefix) SetIdNil(b bool)`

 SetIdNil sets the value for Id to be an explicit nil

### UnsetId
`func (o *WritableNestedSubnetPrefix) UnsetId()`

UnsetId ensures that no value is present for Id, not even an explicit nil
### GetPrefix

`func (o *WritableNestedSubnetPrefix) GetPrefix() string`

GetPrefix returns the Prefix field if non-nil, zero value otherwise.

### GetPrefixOk

`func (o *WritableNestedSubnetPrefix) GetPrefixOk() (*string, bool)`

GetPrefixOk returns a tuple with the Prefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefix

`func (o *WritableNestedSubnetPrefix) SetPrefix(v string)`

SetPrefix sets Prefix field to given value.


### GetLabel

`func (o *WritableNestedSubnetPrefix) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *WritableNestedSubnetPrefix) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *WritableNestedSubnetPrefix) SetLabel(v string)`

SetLabel sets Label field to given value.

### HasLabel

`func (o *WritableNestedSubnetPrefix) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### GetIsSecondary

`func (o *WritableNestedSubnetPrefix) GetIsSecondary() bool`

GetIsSecondary returns the IsSecondary field if non-nil, zero value otherwise.

### GetIsSecondaryOk

`func (o *WritableNestedSubnetPrefix) GetIsSecondaryOk() (*bool, bool)`

GetIsSecondaryOk returns a tuple with the IsSecondary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsSecondary

`func (o *WritableNestedSubnetPrefix) SetIsSecondary(v bool)`

SetIsSecondary sets IsSecondary field to given value.

### HasIsSecondary

`func (o *WritableNestedSubnetPrefix) HasIsSecondary() bool`

HasIsSecondary returns a boolean if a field has been set.

### GetAutoReserveIps

`func (o *WritableNestedSubnetPrefix) GetAutoReserveIps() bool`

GetAutoReserveIps returns the AutoReserveIps field if non-nil, zero value otherwise.

### GetAutoReserveIpsOk

`func (o *WritableNestedSubnetPrefix) GetAutoReserveIpsOk() (*bool, bool)`

GetAutoReserveIpsOk returns a tuple with the AutoReserveIps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoReserveIps

`func (o *WritableNestedSubnetPrefix) SetAutoReserveIps(v bool)`

SetAutoReserveIps sets AutoReserveIps field to given value.

### HasAutoReserveIps

`func (o *WritableNestedSubnetPrefix) HasAutoReserveIps() bool`

HasAutoReserveIps returns a boolean if a field has been set.

### GetMarkUtilized

`func (o *WritableNestedSubnetPrefix) GetMarkUtilized() bool`

GetMarkUtilized returns the MarkUtilized field if non-nil, zero value otherwise.

### GetMarkUtilizedOk

`func (o *WritableNestedSubnetPrefix) GetMarkUtilizedOk() (*bool, bool)`

GetMarkUtilizedOk returns a tuple with the MarkUtilized field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMarkUtilized

`func (o *WritableNestedSubnetPrefix) SetMarkUtilized(v bool)`

SetMarkUtilized sets MarkUtilized field to given value.

### HasMarkUtilized

`func (o *WritableNestedSubnetPrefix) HasMarkUtilized() bool`

HasMarkUtilized returns a boolean if a field has been set.

### GetStatus

`func (o *WritableNestedSubnetPrefix) GetStatus() NestedSubnetPrefixStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *WritableNestedSubnetPrefix) GetStatusOk() (*NestedSubnetPrefixStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *WritableNestedSubnetPrefix) SetStatus(v NestedSubnetPrefixStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *WritableNestedSubnetPrefix) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetDescription

`func (o *WritableNestedSubnetPrefix) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *WritableNestedSubnetPrefix) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *WritableNestedSubnetPrefix) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *WritableNestedSubnetPrefix) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetComments

`func (o *WritableNestedSubnetPrefix) GetComments() string`

GetComments returns the Comments field if non-nil, zero value otherwise.

### GetCommentsOk

`func (o *WritableNestedSubnetPrefix) GetCommentsOk() (*string, bool)`

GetCommentsOk returns a tuple with the Comments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComments

`func (o *WritableNestedSubnetPrefix) SetComments(v string)`

SetComments sets Comments field to given value.

### HasComments

`func (o *WritableNestedSubnetPrefix) HasComments() bool`

HasComments returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


