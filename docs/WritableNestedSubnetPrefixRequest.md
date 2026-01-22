# WritableNestedSubnetPrefixRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **NullableInt32** |  | [optional] 
**Prefix** | **string** |  | 
**Label** | Pointer to **string** | Name of the Subnet | [optional] 
**IsSecondary** | Pointer to **bool** | Set Prefix subnet as secondary | [optional] 
**AutoReserveIps** | Pointer to **bool** | Automatically reserve IPs based on plugin configuration | [optional] [default to false]
**Status** | Pointer to [**NestedSubnetPrefixStatusValue**](NestedSubnetPrefixStatusValue.md) |  | [optional] 

## Methods

### NewWritableNestedSubnetPrefixRequest

`func NewWritableNestedSubnetPrefixRequest(prefix string, ) *WritableNestedSubnetPrefixRequest`

NewWritableNestedSubnetPrefixRequest instantiates a new WritableNestedSubnetPrefixRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWritableNestedSubnetPrefixRequestWithDefaults

`func NewWritableNestedSubnetPrefixRequestWithDefaults() *WritableNestedSubnetPrefixRequest`

NewWritableNestedSubnetPrefixRequestWithDefaults instantiates a new WritableNestedSubnetPrefixRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *WritableNestedSubnetPrefixRequest) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *WritableNestedSubnetPrefixRequest) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *WritableNestedSubnetPrefixRequest) SetId(v int32)`

SetId sets Id field to given value.

### HasId

`func (o *WritableNestedSubnetPrefixRequest) HasId() bool`

HasId returns a boolean if a field has been set.

### SetIdNil

`func (o *WritableNestedSubnetPrefixRequest) SetIdNil(b bool)`

 SetIdNil sets the value for Id to be an explicit nil

### UnsetId
`func (o *WritableNestedSubnetPrefixRequest) UnsetId()`

UnsetId ensures that no value is present for Id, not even an explicit nil
### GetPrefix

`func (o *WritableNestedSubnetPrefixRequest) GetPrefix() string`

GetPrefix returns the Prefix field if non-nil, zero value otherwise.

### GetPrefixOk

`func (o *WritableNestedSubnetPrefixRequest) GetPrefixOk() (*string, bool)`

GetPrefixOk returns a tuple with the Prefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefix

`func (o *WritableNestedSubnetPrefixRequest) SetPrefix(v string)`

SetPrefix sets Prefix field to given value.


### GetLabel

`func (o *WritableNestedSubnetPrefixRequest) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *WritableNestedSubnetPrefixRequest) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *WritableNestedSubnetPrefixRequest) SetLabel(v string)`

SetLabel sets Label field to given value.

### HasLabel

`func (o *WritableNestedSubnetPrefixRequest) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### GetIsSecondary

`func (o *WritableNestedSubnetPrefixRequest) GetIsSecondary() bool`

GetIsSecondary returns the IsSecondary field if non-nil, zero value otherwise.

### GetIsSecondaryOk

`func (o *WritableNestedSubnetPrefixRequest) GetIsSecondaryOk() (*bool, bool)`

GetIsSecondaryOk returns a tuple with the IsSecondary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsSecondary

`func (o *WritableNestedSubnetPrefixRequest) SetIsSecondary(v bool)`

SetIsSecondary sets IsSecondary field to given value.

### HasIsSecondary

`func (o *WritableNestedSubnetPrefixRequest) HasIsSecondary() bool`

HasIsSecondary returns a boolean if a field has been set.

### GetAutoReserveIps

`func (o *WritableNestedSubnetPrefixRequest) GetAutoReserveIps() bool`

GetAutoReserveIps returns the AutoReserveIps field if non-nil, zero value otherwise.

### GetAutoReserveIpsOk

`func (o *WritableNestedSubnetPrefixRequest) GetAutoReserveIpsOk() (*bool, bool)`

GetAutoReserveIpsOk returns a tuple with the AutoReserveIps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoReserveIps

`func (o *WritableNestedSubnetPrefixRequest) SetAutoReserveIps(v bool)`

SetAutoReserveIps sets AutoReserveIps field to given value.

### HasAutoReserveIps

`func (o *WritableNestedSubnetPrefixRequest) HasAutoReserveIps() bool`

HasAutoReserveIps returns a boolean if a field has been set.

### GetStatus

`func (o *WritableNestedSubnetPrefixRequest) GetStatus() NestedSubnetPrefixStatusValue`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *WritableNestedSubnetPrefixRequest) GetStatusOk() (*NestedSubnetPrefixStatusValue, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *WritableNestedSubnetPrefixRequest) SetStatus(v NestedSubnetPrefixStatusValue)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *WritableNestedSubnetPrefixRequest) HasStatus() bool`

HasStatus returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


