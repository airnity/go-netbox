# PluginsAirnityIpamVpcCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Name of the VPC | 
**Environment** | Pointer to [**NullableBriefVPCRequestEnvironment**](BriefVPCRequestEnvironment.md) |  | [optional] 
**CustomFieldData** | Pointer to **interface{}** |  | [optional] 
**Tags** | Pointer to [**[]NestedTagRequest**](NestedTagRequest.md) |  | [optional] 

## Methods

### NewPluginsAirnityIpamVpcCreateRequest

`func NewPluginsAirnityIpamVpcCreateRequest(name string, ) *PluginsAirnityIpamVpcCreateRequest`

NewPluginsAirnityIpamVpcCreateRequest instantiates a new PluginsAirnityIpamVpcCreateRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPluginsAirnityIpamVpcCreateRequestWithDefaults

`func NewPluginsAirnityIpamVpcCreateRequestWithDefaults() *PluginsAirnityIpamVpcCreateRequest`

NewPluginsAirnityIpamVpcCreateRequestWithDefaults instantiates a new PluginsAirnityIpamVpcCreateRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *PluginsAirnityIpamVpcCreateRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *PluginsAirnityIpamVpcCreateRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *PluginsAirnityIpamVpcCreateRequest) SetName(v string)`

SetName sets Name field to given value.


### GetEnvironment

`func (o *PluginsAirnityIpamVpcCreateRequest) GetEnvironment() BriefVPCRequestEnvironment`

GetEnvironment returns the Environment field if non-nil, zero value otherwise.

### GetEnvironmentOk

`func (o *PluginsAirnityIpamVpcCreateRequest) GetEnvironmentOk() (*BriefVPCRequestEnvironment, bool)`

GetEnvironmentOk returns a tuple with the Environment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnvironment

`func (o *PluginsAirnityIpamVpcCreateRequest) SetEnvironment(v BriefVPCRequestEnvironment)`

SetEnvironment sets Environment field to given value.

### HasEnvironment

`func (o *PluginsAirnityIpamVpcCreateRequest) HasEnvironment() bool`

HasEnvironment returns a boolean if a field has been set.

### SetEnvironmentNil

`func (o *PluginsAirnityIpamVpcCreateRequest) SetEnvironmentNil(b bool)`

 SetEnvironmentNil sets the value for Environment to be an explicit nil

### UnsetEnvironment
`func (o *PluginsAirnityIpamVpcCreateRequest) UnsetEnvironment()`

UnsetEnvironment ensures that no value is present for Environment, not even an explicit nil
### GetCustomFieldData

`func (o *PluginsAirnityIpamVpcCreateRequest) GetCustomFieldData() interface{}`

GetCustomFieldData returns the CustomFieldData field if non-nil, zero value otherwise.

### GetCustomFieldDataOk

`func (o *PluginsAirnityIpamVpcCreateRequest) GetCustomFieldDataOk() (*interface{}, bool)`

GetCustomFieldDataOk returns a tuple with the CustomFieldData field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomFieldData

`func (o *PluginsAirnityIpamVpcCreateRequest) SetCustomFieldData(v interface{})`

SetCustomFieldData sets CustomFieldData field to given value.

### HasCustomFieldData

`func (o *PluginsAirnityIpamVpcCreateRequest) HasCustomFieldData() bool`

HasCustomFieldData returns a boolean if a field has been set.

### SetCustomFieldDataNil

`func (o *PluginsAirnityIpamVpcCreateRequest) SetCustomFieldDataNil(b bool)`

 SetCustomFieldDataNil sets the value for CustomFieldData to be an explicit nil

### UnsetCustomFieldData
`func (o *PluginsAirnityIpamVpcCreateRequest) UnsetCustomFieldData()`

UnsetCustomFieldData ensures that no value is present for CustomFieldData, not even an explicit nil
### GetTags

`func (o *PluginsAirnityIpamVpcCreateRequest) GetTags() []NestedTagRequest`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *PluginsAirnityIpamVpcCreateRequest) GetTagsOk() (*[]NestedTagRequest, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTags

`func (o *PluginsAirnityIpamVpcCreateRequest) SetTags(v []NestedTagRequest)`

SetTags sets Tags field to given value.

### HasTags

`func (o *PluginsAirnityIpamVpcCreateRequest) HasTags() bool`

HasTags returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


