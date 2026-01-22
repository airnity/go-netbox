# NestedSubnetIPAddress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** |  | [readonly] 
**Url** | **string** |  | [readonly] 
**Display** | **string** |  | [readonly] 
**Address** | **string** | IPv4 or IPv6 address (with mask) | 
**MaskLength** | **string** |  | [readonly] 
**Family** | **string** |  | [readonly] 

## Methods

### NewNestedSubnetIPAddress

`func NewNestedSubnetIPAddress(id int32, url string, display string, address string, maskLength string, family string, ) *NestedSubnetIPAddress`

NewNestedSubnetIPAddress instantiates a new NestedSubnetIPAddress object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewNestedSubnetIPAddressWithDefaults

`func NewNestedSubnetIPAddressWithDefaults() *NestedSubnetIPAddress`

NewNestedSubnetIPAddressWithDefaults instantiates a new NestedSubnetIPAddress object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *NestedSubnetIPAddress) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *NestedSubnetIPAddress) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *NestedSubnetIPAddress) SetId(v int32)`

SetId sets Id field to given value.


### GetUrl

`func (o *NestedSubnetIPAddress) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *NestedSubnetIPAddress) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *NestedSubnetIPAddress) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetDisplay

`func (o *NestedSubnetIPAddress) GetDisplay() string`

GetDisplay returns the Display field if non-nil, zero value otherwise.

### GetDisplayOk

`func (o *NestedSubnetIPAddress) GetDisplayOk() (*string, bool)`

GetDisplayOk returns a tuple with the Display field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplay

`func (o *NestedSubnetIPAddress) SetDisplay(v string)`

SetDisplay sets Display field to given value.


### GetAddress

`func (o *NestedSubnetIPAddress) GetAddress() string`

GetAddress returns the Address field if non-nil, zero value otherwise.

### GetAddressOk

`func (o *NestedSubnetIPAddress) GetAddressOk() (*string, bool)`

GetAddressOk returns a tuple with the Address field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddress

`func (o *NestedSubnetIPAddress) SetAddress(v string)`

SetAddress sets Address field to given value.


### GetMaskLength

`func (o *NestedSubnetIPAddress) GetMaskLength() string`

GetMaskLength returns the MaskLength field if non-nil, zero value otherwise.

### GetMaskLengthOk

`func (o *NestedSubnetIPAddress) GetMaskLengthOk() (*string, bool)`

GetMaskLengthOk returns a tuple with the MaskLength field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaskLength

`func (o *NestedSubnetIPAddress) SetMaskLength(v string)`

SetMaskLength sets MaskLength field to given value.


### GetFamily

`func (o *NestedSubnetIPAddress) GetFamily() string`

GetFamily returns the Family field if non-nil, zero value otherwise.

### GetFamilyOk

`func (o *NestedSubnetIPAddress) GetFamilyOk() (*string, bool)`

GetFamilyOk returns a tuple with the Family field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFamily

`func (o *NestedSubnetIPAddress) SetFamily(v string)`

SetFamily sets Family field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


