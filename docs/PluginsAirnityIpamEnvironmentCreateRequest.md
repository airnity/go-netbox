# PluginsAirnityIpamEnvironmentCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  | 
**Color** | Pointer to **string** |  | [optional] 
**Slug** | **string** |  | 
**Description** | Pointer to **string** |  | [optional] 
**Tags** | Pointer to [**[]NestedTagRequest**](NestedTagRequest.md) |  | [optional] 
**CustomFields** | Pointer to **map[string]map[string]interface{}** |  | [optional] 

## Methods

### NewPluginsAirnityIpamEnvironmentCreateRequest

`func NewPluginsAirnityIpamEnvironmentCreateRequest(name string, slug string, ) *PluginsAirnityIpamEnvironmentCreateRequest`

NewPluginsAirnityIpamEnvironmentCreateRequest instantiates a new PluginsAirnityIpamEnvironmentCreateRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPluginsAirnityIpamEnvironmentCreateRequestWithDefaults

`func NewPluginsAirnityIpamEnvironmentCreateRequestWithDefaults() *PluginsAirnityIpamEnvironmentCreateRequest`

NewPluginsAirnityIpamEnvironmentCreateRequestWithDefaults instantiates a new PluginsAirnityIpamEnvironmentCreateRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) SetName(v string)`

SetName sets Name field to given value.


### GetColor

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) GetColor() string`

GetColor returns the Color field if non-nil, zero value otherwise.

### GetColorOk

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) GetColorOk() (*string, bool)`

GetColorOk returns a tuple with the Color field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColor

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) SetColor(v string)`

SetColor sets Color field to given value.

### HasColor

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) HasColor() bool`

HasColor returns a boolean if a field has been set.

### GetSlug

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) GetSlug() string`

GetSlug returns the Slug field if non-nil, zero value otherwise.

### GetSlugOk

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) GetSlugOk() (*string, bool)`

GetSlugOk returns a tuple with the Slug field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSlug

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) SetSlug(v string)`

SetSlug sets Slug field to given value.


### GetDescription

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetTags

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) GetTags() []NestedTagRequest`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) GetTagsOk() (*[]NestedTagRequest, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTags

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) SetTags(v []NestedTagRequest)`

SetTags sets Tags field to given value.

### HasTags

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) HasTags() bool`

HasTags returns a boolean if a field has been set.

### GetCustomFields

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) GetCustomFields() map[string]map[string]interface{}`

GetCustomFields returns the CustomFields field if non-nil, zero value otherwise.

### GetCustomFieldsOk

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) GetCustomFieldsOk() (*map[string]map[string]interface{}, bool)`

GetCustomFieldsOk returns a tuple with the CustomFields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomFields

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) SetCustomFields(v map[string]map[string]interface{})`

SetCustomFields sets CustomFields field to given value.

### HasCustomFields

`func (o *PluginsAirnityIpamEnvironmentCreateRequest) HasCustomFields() bool`

HasCustomFields returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


