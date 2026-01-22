# PatchedWritableSubnetPrefixRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Prefix** | Pointer to **string** |  | [optional] 
**Label** | Pointer to **string** | Name of the Subnet | [optional] 
**IsSecondary** | Pointer to **bool** | Set Prefix subnet as secondary | [optional] 
**Status** | Pointer to [**PatchedWritableSubnetPrefixRequestStatus**](PatchedWritableSubnetPrefixRequestStatus.md) |  | [optional] 

## Methods

### NewPatchedWritableSubnetPrefixRequest

`func NewPatchedWritableSubnetPrefixRequest() *PatchedWritableSubnetPrefixRequest`

NewPatchedWritableSubnetPrefixRequest instantiates a new PatchedWritableSubnetPrefixRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPatchedWritableSubnetPrefixRequestWithDefaults

`func NewPatchedWritableSubnetPrefixRequestWithDefaults() *PatchedWritableSubnetPrefixRequest`

NewPatchedWritableSubnetPrefixRequestWithDefaults instantiates a new PatchedWritableSubnetPrefixRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPrefix

`func (o *PatchedWritableSubnetPrefixRequest) GetPrefix() string`

GetPrefix returns the Prefix field if non-nil, zero value otherwise.

### GetPrefixOk

`func (o *PatchedWritableSubnetPrefixRequest) GetPrefixOk() (*string, bool)`

GetPrefixOk returns a tuple with the Prefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefix

`func (o *PatchedWritableSubnetPrefixRequest) SetPrefix(v string)`

SetPrefix sets Prefix field to given value.

### HasPrefix

`func (o *PatchedWritableSubnetPrefixRequest) HasPrefix() bool`

HasPrefix returns a boolean if a field has been set.

### GetLabel

`func (o *PatchedWritableSubnetPrefixRequest) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *PatchedWritableSubnetPrefixRequest) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *PatchedWritableSubnetPrefixRequest) SetLabel(v string)`

SetLabel sets Label field to given value.

### HasLabel

`func (o *PatchedWritableSubnetPrefixRequest) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### GetIsSecondary

`func (o *PatchedWritableSubnetPrefixRequest) GetIsSecondary() bool`

GetIsSecondary returns the IsSecondary field if non-nil, zero value otherwise.

### GetIsSecondaryOk

`func (o *PatchedWritableSubnetPrefixRequest) GetIsSecondaryOk() (*bool, bool)`

GetIsSecondaryOk returns a tuple with the IsSecondary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsSecondary

`func (o *PatchedWritableSubnetPrefixRequest) SetIsSecondary(v bool)`

SetIsSecondary sets IsSecondary field to given value.

### HasIsSecondary

`func (o *PatchedWritableSubnetPrefixRequest) HasIsSecondary() bool`

HasIsSecondary returns a boolean if a field has been set.

### GetStatus

`func (o *PatchedWritableSubnetPrefixRequest) GetStatus() PatchedWritableSubnetPrefixRequestStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *PatchedWritableSubnetPrefixRequest) GetStatusOk() (*PatchedWritableSubnetPrefixRequestStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *PatchedWritableSubnetPrefixRequest) SetStatus(v PatchedWritableSubnetPrefixRequestStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *PatchedWritableSubnetPrefixRequest) HasStatus() bool`

HasStatus returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


