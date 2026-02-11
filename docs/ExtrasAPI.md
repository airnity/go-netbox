# \ExtrasAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ExtrasCustomFieldsBulkDestroy**](ExtrasAPI.md#ExtrasCustomFieldsBulkDestroy) | **Delete** /api/extras/custom-fields/ | 
[**ExtrasCustomFieldsBulkPartialUpdate**](ExtrasAPI.md#ExtrasCustomFieldsBulkPartialUpdate) | **Patch** /api/extras/custom-fields/ | 
[**ExtrasCustomFieldsBulkUpdate**](ExtrasAPI.md#ExtrasCustomFieldsBulkUpdate) | **Put** /api/extras/custom-fields/ | 
[**ExtrasCustomFieldsCreate**](ExtrasAPI.md#ExtrasCustomFieldsCreate) | **Post** /api/extras/custom-fields/ | 
[**ExtrasCustomFieldsDestroy**](ExtrasAPI.md#ExtrasCustomFieldsDestroy) | **Delete** /api/extras/custom-fields/{id}/ | 
[**ExtrasCustomFieldsList**](ExtrasAPI.md#ExtrasCustomFieldsList) | **Get** /api/extras/custom-fields/ | 
[**ExtrasCustomFieldsPartialUpdate**](ExtrasAPI.md#ExtrasCustomFieldsPartialUpdate) | **Patch** /api/extras/custom-fields/{id}/ | 
[**ExtrasCustomFieldsRetrieve**](ExtrasAPI.md#ExtrasCustomFieldsRetrieve) | **Get** /api/extras/custom-fields/{id}/ | 
[**ExtrasCustomFieldsUpdate**](ExtrasAPI.md#ExtrasCustomFieldsUpdate) | **Put** /api/extras/custom-fields/{id}/ | 



## ExtrasCustomFieldsBulkDestroy

> ExtrasCustomFieldsBulkDestroy(ctx).CustomFieldRequest(customFieldRequest).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/airnity/go-netbox/v4"
)

func main() {
	customFieldRequest := []openapiclient.CustomFieldRequest{*openapiclient.NewCustomFieldRequest([]string{"ObjectTypes_example"}, openapiclient.CustomField_type_value("text"), "Name_example")} // []CustomFieldRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.ExtrasAPI.ExtrasCustomFieldsBulkDestroy(context.Background()).CustomFieldRequest(customFieldRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ExtrasAPI.ExtrasCustomFieldsBulkDestroy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiExtrasCustomFieldsBulkDestroyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customFieldRequest** | [**[]CustomFieldRequest**](CustomFieldRequest.md) |  | 

### Return type

 (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ExtrasCustomFieldsBulkPartialUpdate

> []CustomField ExtrasCustomFieldsBulkPartialUpdate(ctx).CustomFieldRequest(customFieldRequest).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/airnity/go-netbox/v4"
)

func main() {
	customFieldRequest := []openapiclient.CustomFieldRequest{*openapiclient.NewCustomFieldRequest([]string{"ObjectTypes_example"}, openapiclient.CustomField_type_value("text"), "Name_example")} // []CustomFieldRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ExtrasAPI.ExtrasCustomFieldsBulkPartialUpdate(context.Background()).CustomFieldRequest(customFieldRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ExtrasAPI.ExtrasCustomFieldsBulkPartialUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ExtrasCustomFieldsBulkPartialUpdate`: []CustomField
	fmt.Fprintf(os.Stdout, "Response from `ExtrasAPI.ExtrasCustomFieldsBulkPartialUpdate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiExtrasCustomFieldsBulkPartialUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customFieldRequest** | [**[]CustomFieldRequest**](CustomFieldRequest.md) |  | 

### Return type

[**[]CustomField**](CustomField.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ExtrasCustomFieldsBulkUpdate

> []CustomField ExtrasCustomFieldsBulkUpdate(ctx).CustomFieldRequest(customFieldRequest).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/airnity/go-netbox/v4"
)

func main() {
	customFieldRequest := []openapiclient.CustomFieldRequest{*openapiclient.NewCustomFieldRequest([]string{"ObjectTypes_example"}, openapiclient.CustomField_type_value("text"), "Name_example")} // []CustomFieldRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ExtrasAPI.ExtrasCustomFieldsBulkUpdate(context.Background()).CustomFieldRequest(customFieldRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ExtrasAPI.ExtrasCustomFieldsBulkUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ExtrasCustomFieldsBulkUpdate`: []CustomField
	fmt.Fprintf(os.Stdout, "Response from `ExtrasAPI.ExtrasCustomFieldsBulkUpdate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiExtrasCustomFieldsBulkUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customFieldRequest** | [**[]CustomFieldRequest**](CustomFieldRequest.md) |  | 

### Return type

[**[]CustomField**](CustomField.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ExtrasCustomFieldsCreate

> CustomField ExtrasCustomFieldsCreate(ctx).ExtrasCustomFieldsCreateRequest(extrasCustomFieldsCreateRequest).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/airnity/go-netbox/v4"
)

func main() {
	extrasCustomFieldsCreateRequest := openapiclient.extras_custom_fields_create_request{WritableCustomFieldRequest: openapiclient.NewWritableCustomFieldRequest([]string{"ObjectTypes_example"}, "Name_example")} // ExtrasCustomFieldsCreateRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ExtrasAPI.ExtrasCustomFieldsCreate(context.Background()).ExtrasCustomFieldsCreateRequest(extrasCustomFieldsCreateRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ExtrasAPI.ExtrasCustomFieldsCreate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ExtrasCustomFieldsCreate`: CustomField
	fmt.Fprintf(os.Stdout, "Response from `ExtrasAPI.ExtrasCustomFieldsCreate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiExtrasCustomFieldsCreateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extrasCustomFieldsCreateRequest** | [**ExtrasCustomFieldsCreateRequest**](ExtrasCustomFieldsCreateRequest.md) |  | 

### Return type

[**CustomField**](CustomField.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ExtrasCustomFieldsDestroy

> ExtrasCustomFieldsDestroy(ctx, id).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/airnity/go-netbox/v4"
)

func main() {
	id := int32(56) // int32 | A unique integer value identifying this custom field.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.ExtrasAPI.ExtrasCustomFieldsDestroy(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ExtrasAPI.ExtrasCustomFieldsDestroy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this custom field. | 

### Other Parameters

Other parameters are passed through a pointer to a apiExtrasCustomFieldsDestroyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ExtrasCustomFieldsList

> PaginatedCustomFieldList ExtrasCustomFieldsList(ctx).ChoiceSet(choiceSet).ChoiceSetN(choiceSetN).ChoiceSetId(choiceSetId).ChoiceSetIdN(choiceSetIdN).Created(created).CreatedEmpty(createdEmpty).CreatedGt(createdGt).CreatedGte(createdGte).CreatedLt(createdLt).CreatedLte(createdLte).CreatedN(createdN).CreatedByRequest(createdByRequest).Description(description).DescriptionEmpty(descriptionEmpty).DescriptionIc(descriptionIc).DescriptionIe(descriptionIe).DescriptionIew(descriptionIew).DescriptionIregex(descriptionIregex).DescriptionIsw(descriptionIsw).DescriptionN(descriptionN).DescriptionNic(descriptionNic).DescriptionNie(descriptionNie).DescriptionNiew(descriptionNiew).DescriptionNisw(descriptionNisw).DescriptionRegex(descriptionRegex).FilterLogic(filterLogic).FilterLogicEmpty(filterLogicEmpty).FilterLogicIc(filterLogicIc).FilterLogicIe(filterLogicIe).FilterLogicIew(filterLogicIew).FilterLogicIregex(filterLogicIregex).FilterLogicIsw(filterLogicIsw).FilterLogicN(filterLogicN).FilterLogicNic(filterLogicNic).FilterLogicNie(filterLogicNie).FilterLogicNiew(filterLogicNiew).FilterLogicNisw(filterLogicNisw).FilterLogicRegex(filterLogicRegex).GroupName(groupName).GroupNameEmpty(groupNameEmpty).GroupNameIc(groupNameIc).GroupNameIe(groupNameIe).GroupNameIew(groupNameIew).GroupNameIregex(groupNameIregex).GroupNameIsw(groupNameIsw).GroupNameN(groupNameN).GroupNameNic(groupNameNic).GroupNameNie(groupNameNie).GroupNameNiew(groupNameNiew).GroupNameNisw(groupNameNisw).GroupNameRegex(groupNameRegex).Id(id).IdEmpty(idEmpty).IdGt(idGt).IdGte(idGte).IdLt(idLt).IdLte(idLte).IdN(idN).IsCloneable(isCloneable).Label(label).LabelEmpty(labelEmpty).LabelIc(labelIc).LabelIe(labelIe).LabelIew(labelIew).LabelIregex(labelIregex).LabelIsw(labelIsw).LabelN(labelN).LabelNic(labelNic).LabelNie(labelNie).LabelNiew(labelNiew).LabelNisw(labelNisw).LabelRegex(labelRegex).LastUpdated(lastUpdated).LastUpdatedEmpty(lastUpdatedEmpty).LastUpdatedGt(lastUpdatedGt).LastUpdatedGte(lastUpdatedGte).LastUpdatedLt(lastUpdatedLt).LastUpdatedLte(lastUpdatedLte).LastUpdatedN(lastUpdatedN).Limit(limit).ModifiedByRequest(modifiedByRequest).Name(name).NameEmpty(nameEmpty).NameIc(nameIc).NameIe(nameIe).NameIew(nameIew).NameIregex(nameIregex).NameIsw(nameIsw).NameN(nameN).NameNic(nameNic).NameNie(nameNie).NameNiew(nameNiew).NameNisw(nameNisw).NameRegex(nameRegex).ObjectType(objectType).ObjectTypeIc(objectTypeIc).ObjectTypeIe(objectTypeIe).ObjectTypeIew(objectTypeIew).ObjectTypeIregex(objectTypeIregex).ObjectTypeIsw(objectTypeIsw).ObjectTypeN(objectTypeN).ObjectTypeNic(objectTypeNic).ObjectTypeNie(objectTypeNie).ObjectTypeNiew(objectTypeNiew).ObjectTypeNisw(objectTypeNisw).ObjectTypeRegex(objectTypeRegex).ObjectTypeId(objectTypeId).ObjectTypeIdN(objectTypeIdN).Offset(offset).Ordering(ordering).Owner(owner).OwnerN(ownerN).OwnerGroup(ownerGroup).OwnerGroupN(ownerGroupN).OwnerGroupId(ownerGroupId).OwnerGroupIdN(ownerGroupIdN).OwnerId(ownerId).OwnerIdN(ownerIdN).Q(q).RelatedObjectType(relatedObjectType).RelatedObjectTypeN(relatedObjectTypeN).RelatedObjectTypeId(relatedObjectTypeId).RelatedObjectTypeIdN(relatedObjectTypeIdN).Required(required).SearchWeight(searchWeight).SearchWeightEmpty(searchWeightEmpty).SearchWeightGt(searchWeightGt).SearchWeightGte(searchWeightGte).SearchWeightLt(searchWeightLt).SearchWeightLte(searchWeightLte).SearchWeightN(searchWeightN).Type_(type_).TypeEmpty(typeEmpty).TypeIc(typeIc).TypeIe(typeIe).TypeIew(typeIew).TypeIregex(typeIregex).TypeIsw(typeIsw).TypeN(typeN).TypeNic(typeNic).TypeNie(typeNie).TypeNiew(typeNiew).TypeNisw(typeNisw).TypeRegex(typeRegex).UiEditable(uiEditable).UiEditableEmpty(uiEditableEmpty).UiEditableIc(uiEditableIc).UiEditableIe(uiEditableIe).UiEditableIew(uiEditableIew).UiEditableIregex(uiEditableIregex).UiEditableIsw(uiEditableIsw).UiEditableN(uiEditableN).UiEditableNic(uiEditableNic).UiEditableNie(uiEditableNie).UiEditableNiew(uiEditableNiew).UiEditableNisw(uiEditableNisw).UiEditableRegex(uiEditableRegex).UiVisible(uiVisible).UiVisibleEmpty(uiVisibleEmpty).UiVisibleIc(uiVisibleIc).UiVisibleIe(uiVisibleIe).UiVisibleIew(uiVisibleIew).UiVisibleIregex(uiVisibleIregex).UiVisibleIsw(uiVisibleIsw).UiVisibleN(uiVisibleN).UiVisibleNic(uiVisibleNic).UiVisibleNie(uiVisibleNie).UiVisibleNiew(uiVisibleNiew).UiVisibleNisw(uiVisibleNisw).UiVisibleRegex(uiVisibleRegex).Unique(unique).UpdatedByRequest(updatedByRequest).ValidationMaximum(validationMaximum).ValidationMaximumEmpty(validationMaximumEmpty).ValidationMaximumGt(validationMaximumGt).ValidationMaximumGte(validationMaximumGte).ValidationMaximumLt(validationMaximumLt).ValidationMaximumLte(validationMaximumLte).ValidationMaximumN(validationMaximumN).ValidationMinimum(validationMinimum).ValidationMinimumEmpty(validationMinimumEmpty).ValidationMinimumGt(validationMinimumGt).ValidationMinimumGte(validationMinimumGte).ValidationMinimumLt(validationMinimumLt).ValidationMinimumLte(validationMinimumLte).ValidationMinimumN(validationMinimumN).ValidationRegex(validationRegex).ValidationRegexEmpty(validationRegexEmpty).ValidationRegexIc(validationRegexIc).ValidationRegexIe(validationRegexIe).ValidationRegexIew(validationRegexIew).ValidationRegexIregex(validationRegexIregex).ValidationRegexIsw(validationRegexIsw).ValidationRegexN(validationRegexN).ValidationRegexNic(validationRegexNic).ValidationRegexNie(validationRegexNie).ValidationRegexNiew(validationRegexNiew).ValidationRegexNisw(validationRegexNisw).ValidationRegexRegex(validationRegexRegex).Weight(weight).WeightEmpty(weightEmpty).WeightGt(weightGt).WeightGte(weightGte).WeightLt(weightLt).WeightLte(weightLte).WeightN(weightN).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/airnity/go-netbox/v4"
)

func main() {
	choiceSet := []string{"Inner_example"} // []string |  (optional)
	choiceSetN := []string{"Inner_example"} // []string |  (optional)
	choiceSetId := []*int32{int32(123)} // []*int32 |  (optional)
	choiceSetIdN := []*int32{int32(123)} // []*int32 |  (optional)
	created := []time.Time{time.Now()} // []time.Time |  (optional)
	createdEmpty := []time.Time{time.Now()} // []time.Time |  (optional)
	createdGt := []time.Time{time.Now()} // []time.Time |  (optional)
	createdGte := []time.Time{time.Now()} // []time.Time |  (optional)
	createdLt := []time.Time{time.Now()} // []time.Time |  (optional)
	createdLte := []time.Time{time.Now()} // []time.Time |  (optional)
	createdN := []time.Time{time.Now()} // []time.Time |  (optional)
	createdByRequest := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |  (optional)
	description := []string{"Inner_example"} // []string |  (optional)
	descriptionEmpty := true // bool |  (optional)
	descriptionIc := []string{"Inner_example"} // []string |  (optional)
	descriptionIe := []string{"Inner_example"} // []string |  (optional)
	descriptionIew := []string{"Inner_example"} // []string |  (optional)
	descriptionIregex := []string{"Inner_example"} // []string |  (optional)
	descriptionIsw := []string{"Inner_example"} // []string |  (optional)
	descriptionN := []string{"Inner_example"} // []string |  (optional)
	descriptionNic := []string{"Inner_example"} // []string |  (optional)
	descriptionNie := []string{"Inner_example"} // []string |  (optional)
	descriptionNiew := []string{"Inner_example"} // []string |  (optional)
	descriptionNisw := []string{"Inner_example"} // []string |  (optional)
	descriptionRegex := []string{"Inner_example"} // []string |  (optional)
	filterLogic := openapiclient.extras_custom_fields_list_filter_logic_parameter("disabled") // ExtrasCustomFieldsListFilterLogicParameter | Loose matches any instance of a given string; exact matches the entire field.  * `disabled` - Disabled * `loose` - Loose * `exact` - Exact (optional)
	filterLogicEmpty := true // bool |  (optional)
	filterLogicIc := []string{"Inner_example"} // []string |  (optional)
	filterLogicIe := []string{"Inner_example"} // []string |  (optional)
	filterLogicIew := []string{"Inner_example"} // []string |  (optional)
	filterLogicIregex := []string{"Inner_example"} // []string |  (optional)
	filterLogicIsw := []string{"Inner_example"} // []string |  (optional)
	filterLogicN := openapiclient.extras_custom_fields_list_filter_logic_parameter("disabled") // ExtrasCustomFieldsListFilterLogicParameter | Loose matches any instance of a given string; exact matches the entire field.  * `disabled` - Disabled * `loose` - Loose * `exact` - Exact (optional)
	filterLogicNic := []string{"Inner_example"} // []string |  (optional)
	filterLogicNie := []string{"Inner_example"} // []string |  (optional)
	filterLogicNiew := []string{"Inner_example"} // []string |  (optional)
	filterLogicNisw := []string{"Inner_example"} // []string |  (optional)
	filterLogicRegex := []string{"Inner_example"} // []string |  (optional)
	groupName := []string{"Inner_example"} // []string |  (optional)
	groupNameEmpty := true // bool |  (optional)
	groupNameIc := []string{"Inner_example"} // []string |  (optional)
	groupNameIe := []string{"Inner_example"} // []string |  (optional)
	groupNameIew := []string{"Inner_example"} // []string |  (optional)
	groupNameIregex := []string{"Inner_example"} // []string |  (optional)
	groupNameIsw := []string{"Inner_example"} // []string |  (optional)
	groupNameN := []string{"Inner_example"} // []string |  (optional)
	groupNameNic := []string{"Inner_example"} // []string |  (optional)
	groupNameNie := []string{"Inner_example"} // []string |  (optional)
	groupNameNiew := []string{"Inner_example"} // []string |  (optional)
	groupNameNisw := []string{"Inner_example"} // []string |  (optional)
	groupNameRegex := []string{"Inner_example"} // []string |  (optional)
	id := []int32{int32(123)} // []int32 |  (optional)
	idEmpty := true // bool |  (optional)
	idGt := []int32{int32(123)} // []int32 |  (optional)
	idGte := []int32{int32(123)} // []int32 |  (optional)
	idLt := []int32{int32(123)} // []int32 |  (optional)
	idLte := []int32{int32(123)} // []int32 |  (optional)
	idN := []int32{int32(123)} // []int32 |  (optional)
	isCloneable := true // bool |  (optional)
	label := []string{"Inner_example"} // []string |  (optional)
	labelEmpty := true // bool |  (optional)
	labelIc := []string{"Inner_example"} // []string |  (optional)
	labelIe := []string{"Inner_example"} // []string |  (optional)
	labelIew := []string{"Inner_example"} // []string |  (optional)
	labelIregex := []string{"Inner_example"} // []string |  (optional)
	labelIsw := []string{"Inner_example"} // []string |  (optional)
	labelN := []string{"Inner_example"} // []string |  (optional)
	labelNic := []string{"Inner_example"} // []string |  (optional)
	labelNie := []string{"Inner_example"} // []string |  (optional)
	labelNiew := []string{"Inner_example"} // []string |  (optional)
	labelNisw := []string{"Inner_example"} // []string |  (optional)
	labelRegex := []string{"Inner_example"} // []string |  (optional)
	lastUpdated := []time.Time{time.Now()} // []time.Time |  (optional)
	lastUpdatedEmpty := []time.Time{time.Now()} // []time.Time |  (optional)
	lastUpdatedGt := []time.Time{time.Now()} // []time.Time |  (optional)
	lastUpdatedGte := []time.Time{time.Now()} // []time.Time |  (optional)
	lastUpdatedLt := []time.Time{time.Now()} // []time.Time |  (optional)
	lastUpdatedLte := []time.Time{time.Now()} // []time.Time |  (optional)
	lastUpdatedN := []time.Time{time.Now()} // []time.Time |  (optional)
	limit := int32(56) // int32 | Number of results to return per page. (optional)
	modifiedByRequest := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |  (optional)
	name := []string{"Inner_example"} // []string |  (optional)
	nameEmpty := true // bool |  (optional)
	nameIc := []string{"Inner_example"} // []string |  (optional)
	nameIe := []string{"Inner_example"} // []string |  (optional)
	nameIew := []string{"Inner_example"} // []string |  (optional)
	nameIregex := []string{"Inner_example"} // []string |  (optional)
	nameIsw := []string{"Inner_example"} // []string |  (optional)
	nameN := []string{"Inner_example"} // []string |  (optional)
	nameNic := []string{"Inner_example"} // []string |  (optional)
	nameNie := []string{"Inner_example"} // []string |  (optional)
	nameNiew := []string{"Inner_example"} // []string |  (optional)
	nameNisw := []string{"Inner_example"} // []string |  (optional)
	nameRegex := []string{"Inner_example"} // []string |  (optional)
	objectType := "objectType_example" // string |  (optional)
	objectTypeIc := "objectTypeIc_example" // string |  (optional)
	objectTypeIe := "objectTypeIe_example" // string |  (optional)
	objectTypeIew := "objectTypeIew_example" // string |  (optional)
	objectTypeIregex := "objectTypeIregex_example" // string |  (optional)
	objectTypeIsw := "objectTypeIsw_example" // string |  (optional)
	objectTypeN := "objectTypeN_example" // string |  (optional)
	objectTypeNic := "objectTypeNic_example" // string |  (optional)
	objectTypeNie := "objectTypeNie_example" // string |  (optional)
	objectTypeNiew := "objectTypeNiew_example" // string |  (optional)
	objectTypeNisw := "objectTypeNisw_example" // string |  (optional)
	objectTypeRegex := "objectTypeRegex_example" // string |  (optional)
	objectTypeId := []int32{int32(123)} // []int32 |  (optional)
	objectTypeIdN := []int32{int32(123)} // []int32 |  (optional)
	offset := int32(56) // int32 | The initial index from which to return the results. (optional)
	ordering := "ordering_example" // string | Which field to use when ordering the results. (optional)
	owner := []string{"Inner_example"} // []string | Owner (name) (optional)
	ownerN := []string{"Inner_example"} // []string | Owner (name) (optional)
	ownerGroup := []string{"Inner_example"} // []string | Owner Group (name) (optional)
	ownerGroupN := []string{"Inner_example"} // []string | Owner Group (name) (optional)
	ownerGroupId := []int32{int32(123)} // []int32 | Owner Group (ID) (optional)
	ownerGroupIdN := []int32{int32(123)} // []int32 | Owner Group (ID) (optional)
	ownerId := []*int32{int32(123)} // []*int32 | Owner (ID) (optional)
	ownerIdN := []*int32{int32(123)} // []*int32 | Owner (ID) (optional)
	q := "q_example" // string | Search (optional)
	relatedObjectType := "relatedObjectType_example" // string |  (optional)
	relatedObjectTypeN := "relatedObjectTypeN_example" // string |  (optional)
	relatedObjectTypeId := []int32{int32(123)} // []int32 |  (optional)
	relatedObjectTypeIdN := []int32{int32(123)} // []int32 |  (optional)
	required := true // bool |  (optional)
	searchWeight := []int32{int32(123)} // []int32 |  (optional)
	searchWeightEmpty := true // bool |  (optional)
	searchWeightGt := []int32{int32(123)} // []int32 |  (optional)
	searchWeightGte := []int32{int32(123)} // []int32 |  (optional)
	searchWeightLt := []int32{int32(123)} // []int32 |  (optional)
	searchWeightLte := []int32{int32(123)} // []int32 |  (optional)
	searchWeightN := []int32{int32(123)} // []int32 |  (optional)
	type_ := []string{"Inner_example"} // []string | The type of data this custom field holds (optional)
	typeEmpty := true // bool |  (optional)
	typeIc := []string{"Inner_example"} // []string | The type of data this custom field holds (optional)
	typeIe := []string{"Inner_example"} // []string | The type of data this custom field holds (optional)
	typeIew := []string{"Inner_example"} // []string | The type of data this custom field holds (optional)
	typeIregex := []string{"Inner_example"} // []string | The type of data this custom field holds (optional)
	typeIsw := []string{"Inner_example"} // []string | The type of data this custom field holds (optional)
	typeN := []string{"Inner_example"} // []string | The type of data this custom field holds (optional)
	typeNic := []string{"Inner_example"} // []string | The type of data this custom field holds (optional)
	typeNie := []string{"Inner_example"} // []string | The type of data this custom field holds (optional)
	typeNiew := []string{"Inner_example"} // []string | The type of data this custom field holds (optional)
	typeNisw := []string{"Inner_example"} // []string | The type of data this custom field holds (optional)
	typeRegex := []string{"Inner_example"} // []string | The type of data this custom field holds (optional)
	uiEditable := openapiclient.extras_custom_fields_list_ui_editable_parameter("hidden") // ExtrasCustomFieldsListUiEditableParameter | Specifies whether the custom field value can be edited in the UI  * `yes` - Yes * `no` - No * `hidden` - Hidden (optional)
	uiEditableEmpty := true // bool |  (optional)
	uiEditableIc := []string{"Inner_example"} // []string |  (optional)
	uiEditableIe := []string{"Inner_example"} // []string |  (optional)
	uiEditableIew := []string{"Inner_example"} // []string |  (optional)
	uiEditableIregex := []string{"Inner_example"} // []string |  (optional)
	uiEditableIsw := []string{"Inner_example"} // []string |  (optional)
	uiEditableN := openapiclient.extras_custom_fields_list_ui_editable_parameter("hidden") // ExtrasCustomFieldsListUiEditableParameter | Specifies whether the custom field value can be edited in the UI  * `yes` - Yes * `no` - No * `hidden` - Hidden (optional)
	uiEditableNic := []string{"Inner_example"} // []string |  (optional)
	uiEditableNie := []string{"Inner_example"} // []string |  (optional)
	uiEditableNiew := []string{"Inner_example"} // []string |  (optional)
	uiEditableNisw := []string{"Inner_example"} // []string |  (optional)
	uiEditableRegex := []string{"Inner_example"} // []string |  (optional)
	uiVisible := openapiclient.extras_custom_fields_list_ui_visible_parameter("always") // ExtrasCustomFieldsListUiVisibleParameter | Specifies whether the custom field is displayed in the UI  * `always` - Always * `if-set` - If set * `hidden` - Hidden (optional)
	uiVisibleEmpty := true // bool |  (optional)
	uiVisibleIc := []string{"Inner_example"} // []string |  (optional)
	uiVisibleIe := []string{"Inner_example"} // []string |  (optional)
	uiVisibleIew := []string{"Inner_example"} // []string |  (optional)
	uiVisibleIregex := []string{"Inner_example"} // []string |  (optional)
	uiVisibleIsw := []string{"Inner_example"} // []string |  (optional)
	uiVisibleN := openapiclient.extras_custom_fields_list_ui_visible_parameter("always") // ExtrasCustomFieldsListUiVisibleParameter | Specifies whether the custom field is displayed in the UI  * `always` - Always * `if-set` - If set * `hidden` - Hidden (optional)
	uiVisibleNic := []string{"Inner_example"} // []string |  (optional)
	uiVisibleNie := []string{"Inner_example"} // []string |  (optional)
	uiVisibleNiew := []string{"Inner_example"} // []string |  (optional)
	uiVisibleNisw := []string{"Inner_example"} // []string |  (optional)
	uiVisibleRegex := []string{"Inner_example"} // []string |  (optional)
	unique := true // bool |  (optional)
	updatedByRequest := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |  (optional)
	validationMaximum := []float64{float64(123)} // []float64 |  (optional)
	validationMaximumEmpty := true // bool |  (optional)
	validationMaximumGt := []float64{float64(123)} // []float64 |  (optional)
	validationMaximumGte := []float64{float64(123)} // []float64 |  (optional)
	validationMaximumLt := []float64{float64(123)} // []float64 |  (optional)
	validationMaximumLte := []float64{float64(123)} // []float64 |  (optional)
	validationMaximumN := []float64{float64(123)} // []float64 |  (optional)
	validationMinimum := []float64{float64(123)} // []float64 |  (optional)
	validationMinimumEmpty := true // bool |  (optional)
	validationMinimumGt := []float64{float64(123)} // []float64 |  (optional)
	validationMinimumGte := []float64{float64(123)} // []float64 |  (optional)
	validationMinimumLt := []float64{float64(123)} // []float64 |  (optional)
	validationMinimumLte := []float64{float64(123)} // []float64 |  (optional)
	validationMinimumN := []float64{float64(123)} // []float64 |  (optional)
	validationRegex := []string{"Inner_example"} // []string |  (optional)
	validationRegexEmpty := true // bool |  (optional)
	validationRegexIc := []string{"Inner_example"} // []string |  (optional)
	validationRegexIe := []string{"Inner_example"} // []string |  (optional)
	validationRegexIew := []string{"Inner_example"} // []string |  (optional)
	validationRegexIregex := []string{"Inner_example"} // []string |  (optional)
	validationRegexIsw := []string{"Inner_example"} // []string |  (optional)
	validationRegexN := []string{"Inner_example"} // []string |  (optional)
	validationRegexNic := []string{"Inner_example"} // []string |  (optional)
	validationRegexNie := []string{"Inner_example"} // []string |  (optional)
	validationRegexNiew := []string{"Inner_example"} // []string |  (optional)
	validationRegexNisw := []string{"Inner_example"} // []string |  (optional)
	validationRegexRegex := []string{"Inner_example"} // []string |  (optional)
	weight := []int32{int32(123)} // []int32 |  (optional)
	weightEmpty := true // bool |  (optional)
	weightGt := []int32{int32(123)} // []int32 |  (optional)
	weightGte := []int32{int32(123)} // []int32 |  (optional)
	weightLt := []int32{int32(123)} // []int32 |  (optional)
	weightLte := []int32{int32(123)} // []int32 |  (optional)
	weightN := []int32{int32(123)} // []int32 |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ExtrasAPI.ExtrasCustomFieldsList(context.Background()).ChoiceSet(choiceSet).ChoiceSetN(choiceSetN).ChoiceSetId(choiceSetId).ChoiceSetIdN(choiceSetIdN).Created(created).CreatedEmpty(createdEmpty).CreatedGt(createdGt).CreatedGte(createdGte).CreatedLt(createdLt).CreatedLte(createdLte).CreatedN(createdN).CreatedByRequest(createdByRequest).Description(description).DescriptionEmpty(descriptionEmpty).DescriptionIc(descriptionIc).DescriptionIe(descriptionIe).DescriptionIew(descriptionIew).DescriptionIregex(descriptionIregex).DescriptionIsw(descriptionIsw).DescriptionN(descriptionN).DescriptionNic(descriptionNic).DescriptionNie(descriptionNie).DescriptionNiew(descriptionNiew).DescriptionNisw(descriptionNisw).DescriptionRegex(descriptionRegex).FilterLogic(filterLogic).FilterLogicEmpty(filterLogicEmpty).FilterLogicIc(filterLogicIc).FilterLogicIe(filterLogicIe).FilterLogicIew(filterLogicIew).FilterLogicIregex(filterLogicIregex).FilterLogicIsw(filterLogicIsw).FilterLogicN(filterLogicN).FilterLogicNic(filterLogicNic).FilterLogicNie(filterLogicNie).FilterLogicNiew(filterLogicNiew).FilterLogicNisw(filterLogicNisw).FilterLogicRegex(filterLogicRegex).GroupName(groupName).GroupNameEmpty(groupNameEmpty).GroupNameIc(groupNameIc).GroupNameIe(groupNameIe).GroupNameIew(groupNameIew).GroupNameIregex(groupNameIregex).GroupNameIsw(groupNameIsw).GroupNameN(groupNameN).GroupNameNic(groupNameNic).GroupNameNie(groupNameNie).GroupNameNiew(groupNameNiew).GroupNameNisw(groupNameNisw).GroupNameRegex(groupNameRegex).Id(id).IdEmpty(idEmpty).IdGt(idGt).IdGte(idGte).IdLt(idLt).IdLte(idLte).IdN(idN).IsCloneable(isCloneable).Label(label).LabelEmpty(labelEmpty).LabelIc(labelIc).LabelIe(labelIe).LabelIew(labelIew).LabelIregex(labelIregex).LabelIsw(labelIsw).LabelN(labelN).LabelNic(labelNic).LabelNie(labelNie).LabelNiew(labelNiew).LabelNisw(labelNisw).LabelRegex(labelRegex).LastUpdated(lastUpdated).LastUpdatedEmpty(lastUpdatedEmpty).LastUpdatedGt(lastUpdatedGt).LastUpdatedGte(lastUpdatedGte).LastUpdatedLt(lastUpdatedLt).LastUpdatedLte(lastUpdatedLte).LastUpdatedN(lastUpdatedN).Limit(limit).ModifiedByRequest(modifiedByRequest).Name(name).NameEmpty(nameEmpty).NameIc(nameIc).NameIe(nameIe).NameIew(nameIew).NameIregex(nameIregex).NameIsw(nameIsw).NameN(nameN).NameNic(nameNic).NameNie(nameNie).NameNiew(nameNiew).NameNisw(nameNisw).NameRegex(nameRegex).ObjectType(objectType).ObjectTypeIc(objectTypeIc).ObjectTypeIe(objectTypeIe).ObjectTypeIew(objectTypeIew).ObjectTypeIregex(objectTypeIregex).ObjectTypeIsw(objectTypeIsw).ObjectTypeN(objectTypeN).ObjectTypeNic(objectTypeNic).ObjectTypeNie(objectTypeNie).ObjectTypeNiew(objectTypeNiew).ObjectTypeNisw(objectTypeNisw).ObjectTypeRegex(objectTypeRegex).ObjectTypeId(objectTypeId).ObjectTypeIdN(objectTypeIdN).Offset(offset).Ordering(ordering).Owner(owner).OwnerN(ownerN).OwnerGroup(ownerGroup).OwnerGroupN(ownerGroupN).OwnerGroupId(ownerGroupId).OwnerGroupIdN(ownerGroupIdN).OwnerId(ownerId).OwnerIdN(ownerIdN).Q(q).RelatedObjectType(relatedObjectType).RelatedObjectTypeN(relatedObjectTypeN).RelatedObjectTypeId(relatedObjectTypeId).RelatedObjectTypeIdN(relatedObjectTypeIdN).Required(required).SearchWeight(searchWeight).SearchWeightEmpty(searchWeightEmpty).SearchWeightGt(searchWeightGt).SearchWeightGte(searchWeightGte).SearchWeightLt(searchWeightLt).SearchWeightLte(searchWeightLte).SearchWeightN(searchWeightN).Type_(type_).TypeEmpty(typeEmpty).TypeIc(typeIc).TypeIe(typeIe).TypeIew(typeIew).TypeIregex(typeIregex).TypeIsw(typeIsw).TypeN(typeN).TypeNic(typeNic).TypeNie(typeNie).TypeNiew(typeNiew).TypeNisw(typeNisw).TypeRegex(typeRegex).UiEditable(uiEditable).UiEditableEmpty(uiEditableEmpty).UiEditableIc(uiEditableIc).UiEditableIe(uiEditableIe).UiEditableIew(uiEditableIew).UiEditableIregex(uiEditableIregex).UiEditableIsw(uiEditableIsw).UiEditableN(uiEditableN).UiEditableNic(uiEditableNic).UiEditableNie(uiEditableNie).UiEditableNiew(uiEditableNiew).UiEditableNisw(uiEditableNisw).UiEditableRegex(uiEditableRegex).UiVisible(uiVisible).UiVisibleEmpty(uiVisibleEmpty).UiVisibleIc(uiVisibleIc).UiVisibleIe(uiVisibleIe).UiVisibleIew(uiVisibleIew).UiVisibleIregex(uiVisibleIregex).UiVisibleIsw(uiVisibleIsw).UiVisibleN(uiVisibleN).UiVisibleNic(uiVisibleNic).UiVisibleNie(uiVisibleNie).UiVisibleNiew(uiVisibleNiew).UiVisibleNisw(uiVisibleNisw).UiVisibleRegex(uiVisibleRegex).Unique(unique).UpdatedByRequest(updatedByRequest).ValidationMaximum(validationMaximum).ValidationMaximumEmpty(validationMaximumEmpty).ValidationMaximumGt(validationMaximumGt).ValidationMaximumGte(validationMaximumGte).ValidationMaximumLt(validationMaximumLt).ValidationMaximumLte(validationMaximumLte).ValidationMaximumN(validationMaximumN).ValidationMinimum(validationMinimum).ValidationMinimumEmpty(validationMinimumEmpty).ValidationMinimumGt(validationMinimumGt).ValidationMinimumGte(validationMinimumGte).ValidationMinimumLt(validationMinimumLt).ValidationMinimumLte(validationMinimumLte).ValidationMinimumN(validationMinimumN).ValidationRegex(validationRegex).ValidationRegexEmpty(validationRegexEmpty).ValidationRegexIc(validationRegexIc).ValidationRegexIe(validationRegexIe).ValidationRegexIew(validationRegexIew).ValidationRegexIregex(validationRegexIregex).ValidationRegexIsw(validationRegexIsw).ValidationRegexN(validationRegexN).ValidationRegexNic(validationRegexNic).ValidationRegexNie(validationRegexNie).ValidationRegexNiew(validationRegexNiew).ValidationRegexNisw(validationRegexNisw).ValidationRegexRegex(validationRegexRegex).Weight(weight).WeightEmpty(weightEmpty).WeightGt(weightGt).WeightGte(weightGte).WeightLt(weightLt).WeightLte(weightLte).WeightN(weightN).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ExtrasAPI.ExtrasCustomFieldsList``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ExtrasCustomFieldsList`: PaginatedCustomFieldList
	fmt.Fprintf(os.Stdout, "Response from `ExtrasAPI.ExtrasCustomFieldsList`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiExtrasCustomFieldsListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **choiceSet** | **[]string** |  | 
 **choiceSetN** | **[]string** |  | 
 **choiceSetId** | **[]int32** |  | 
 **choiceSetIdN** | **[]int32** |  | 
 **created** | [**[]time.Time**](time.Time.md) |  | 
 **createdEmpty** | [**[]time.Time**](time.Time.md) |  | 
 **createdGt** | [**[]time.Time**](time.Time.md) |  | 
 **createdGte** | [**[]time.Time**](time.Time.md) |  | 
 **createdLt** | [**[]time.Time**](time.Time.md) |  | 
 **createdLte** | [**[]time.Time**](time.Time.md) |  | 
 **createdN** | [**[]time.Time**](time.Time.md) |  | 
 **createdByRequest** | **string** |  | 
 **description** | **[]string** |  | 
 **descriptionEmpty** | **bool** |  | 
 **descriptionIc** | **[]string** |  | 
 **descriptionIe** | **[]string** |  | 
 **descriptionIew** | **[]string** |  | 
 **descriptionIregex** | **[]string** |  | 
 **descriptionIsw** | **[]string** |  | 
 **descriptionN** | **[]string** |  | 
 **descriptionNic** | **[]string** |  | 
 **descriptionNie** | **[]string** |  | 
 **descriptionNiew** | **[]string** |  | 
 **descriptionNisw** | **[]string** |  | 
 **descriptionRegex** | **[]string** |  | 
 **filterLogic** | [**ExtrasCustomFieldsListFilterLogicParameter**](ExtrasCustomFieldsListFilterLogicParameter.md) | Loose matches any instance of a given string; exact matches the entire field.  * &#x60;disabled&#x60; - Disabled * &#x60;loose&#x60; - Loose * &#x60;exact&#x60; - Exact | 
 **filterLogicEmpty** | **bool** |  | 
 **filterLogicIc** | **[]string** |  | 
 **filterLogicIe** | **[]string** |  | 
 **filterLogicIew** | **[]string** |  | 
 **filterLogicIregex** | **[]string** |  | 
 **filterLogicIsw** | **[]string** |  | 
 **filterLogicN** | [**ExtrasCustomFieldsListFilterLogicParameter**](ExtrasCustomFieldsListFilterLogicParameter.md) | Loose matches any instance of a given string; exact matches the entire field.  * &#x60;disabled&#x60; - Disabled * &#x60;loose&#x60; - Loose * &#x60;exact&#x60; - Exact | 
 **filterLogicNic** | **[]string** |  | 
 **filterLogicNie** | **[]string** |  | 
 **filterLogicNiew** | **[]string** |  | 
 **filterLogicNisw** | **[]string** |  | 
 **filterLogicRegex** | **[]string** |  | 
 **groupName** | **[]string** |  | 
 **groupNameEmpty** | **bool** |  | 
 **groupNameIc** | **[]string** |  | 
 **groupNameIe** | **[]string** |  | 
 **groupNameIew** | **[]string** |  | 
 **groupNameIregex** | **[]string** |  | 
 **groupNameIsw** | **[]string** |  | 
 **groupNameN** | **[]string** |  | 
 **groupNameNic** | **[]string** |  | 
 **groupNameNie** | **[]string** |  | 
 **groupNameNiew** | **[]string** |  | 
 **groupNameNisw** | **[]string** |  | 
 **groupNameRegex** | **[]string** |  | 
 **id** | **[]int32** |  | 
 **idEmpty** | **bool** |  | 
 **idGt** | **[]int32** |  | 
 **idGte** | **[]int32** |  | 
 **idLt** | **[]int32** |  | 
 **idLte** | **[]int32** |  | 
 **idN** | **[]int32** |  | 
 **isCloneable** | **bool** |  | 
 **label** | **[]string** |  | 
 **labelEmpty** | **bool** |  | 
 **labelIc** | **[]string** |  | 
 **labelIe** | **[]string** |  | 
 **labelIew** | **[]string** |  | 
 **labelIregex** | **[]string** |  | 
 **labelIsw** | **[]string** |  | 
 **labelN** | **[]string** |  | 
 **labelNic** | **[]string** |  | 
 **labelNie** | **[]string** |  | 
 **labelNiew** | **[]string** |  | 
 **labelNisw** | **[]string** |  | 
 **labelRegex** | **[]string** |  | 
 **lastUpdated** | [**[]time.Time**](time.Time.md) |  | 
 **lastUpdatedEmpty** | [**[]time.Time**](time.Time.md) |  | 
 **lastUpdatedGt** | [**[]time.Time**](time.Time.md) |  | 
 **lastUpdatedGte** | [**[]time.Time**](time.Time.md) |  | 
 **lastUpdatedLt** | [**[]time.Time**](time.Time.md) |  | 
 **lastUpdatedLte** | [**[]time.Time**](time.Time.md) |  | 
 **lastUpdatedN** | [**[]time.Time**](time.Time.md) |  | 
 **limit** | **int32** | Number of results to return per page. | 
 **modifiedByRequest** | **string** |  | 
 **name** | **[]string** |  | 
 **nameEmpty** | **bool** |  | 
 **nameIc** | **[]string** |  | 
 **nameIe** | **[]string** |  | 
 **nameIew** | **[]string** |  | 
 **nameIregex** | **[]string** |  | 
 **nameIsw** | **[]string** |  | 
 **nameN** | **[]string** |  | 
 **nameNic** | **[]string** |  | 
 **nameNie** | **[]string** |  | 
 **nameNiew** | **[]string** |  | 
 **nameNisw** | **[]string** |  | 
 **nameRegex** | **[]string** |  | 
 **objectType** | **string** |  | 
 **objectTypeIc** | **string** |  | 
 **objectTypeIe** | **string** |  | 
 **objectTypeIew** | **string** |  | 
 **objectTypeIregex** | **string** |  | 
 **objectTypeIsw** | **string** |  | 
 **objectTypeN** | **string** |  | 
 **objectTypeNic** | **string** |  | 
 **objectTypeNie** | **string** |  | 
 **objectTypeNiew** | **string** |  | 
 **objectTypeNisw** | **string** |  | 
 **objectTypeRegex** | **string** |  | 
 **objectTypeId** | **[]int32** |  | 
 **objectTypeIdN** | **[]int32** |  | 
 **offset** | **int32** | The initial index from which to return the results. | 
 **ordering** | **string** | Which field to use when ordering the results. | 
 **owner** | **[]string** | Owner (name) | 
 **ownerN** | **[]string** | Owner (name) | 
 **ownerGroup** | **[]string** | Owner Group (name) | 
 **ownerGroupN** | **[]string** | Owner Group (name) | 
 **ownerGroupId** | **[]int32** | Owner Group (ID) | 
 **ownerGroupIdN** | **[]int32** | Owner Group (ID) | 
 **ownerId** | **[]int32** | Owner (ID) | 
 **ownerIdN** | **[]int32** | Owner (ID) | 
 **q** | **string** | Search | 
 **relatedObjectType** | **string** |  | 
 **relatedObjectTypeN** | **string** |  | 
 **relatedObjectTypeId** | **[]int32** |  | 
 **relatedObjectTypeIdN** | **[]int32** |  | 
 **required** | **bool** |  | 
 **searchWeight** | **[]int32** |  | 
 **searchWeightEmpty** | **bool** |  | 
 **searchWeightGt** | **[]int32** |  | 
 **searchWeightGte** | **[]int32** |  | 
 **searchWeightLt** | **[]int32** |  | 
 **searchWeightLte** | **[]int32** |  | 
 **searchWeightN** | **[]int32** |  | 
 **type_** | **[]string** | The type of data this custom field holds | 
 **typeEmpty** | **bool** |  | 
 **typeIc** | **[]string** | The type of data this custom field holds | 
 **typeIe** | **[]string** | The type of data this custom field holds | 
 **typeIew** | **[]string** | The type of data this custom field holds | 
 **typeIregex** | **[]string** | The type of data this custom field holds | 
 **typeIsw** | **[]string** | The type of data this custom field holds | 
 **typeN** | **[]string** | The type of data this custom field holds | 
 **typeNic** | **[]string** | The type of data this custom field holds | 
 **typeNie** | **[]string** | The type of data this custom field holds | 
 **typeNiew** | **[]string** | The type of data this custom field holds | 
 **typeNisw** | **[]string** | The type of data this custom field holds | 
 **typeRegex** | **[]string** | The type of data this custom field holds | 
 **uiEditable** | [**ExtrasCustomFieldsListUiEditableParameter**](ExtrasCustomFieldsListUiEditableParameter.md) | Specifies whether the custom field value can be edited in the UI  * &#x60;yes&#x60; - Yes * &#x60;no&#x60; - No * &#x60;hidden&#x60; - Hidden | 
 **uiEditableEmpty** | **bool** |  | 
 **uiEditableIc** | **[]string** |  | 
 **uiEditableIe** | **[]string** |  | 
 **uiEditableIew** | **[]string** |  | 
 **uiEditableIregex** | **[]string** |  | 
 **uiEditableIsw** | **[]string** |  | 
 **uiEditableN** | [**ExtrasCustomFieldsListUiEditableParameter**](ExtrasCustomFieldsListUiEditableParameter.md) | Specifies whether the custom field value can be edited in the UI  * &#x60;yes&#x60; - Yes * &#x60;no&#x60; - No * &#x60;hidden&#x60; - Hidden | 
 **uiEditableNic** | **[]string** |  | 
 **uiEditableNie** | **[]string** |  | 
 **uiEditableNiew** | **[]string** |  | 
 **uiEditableNisw** | **[]string** |  | 
 **uiEditableRegex** | **[]string** |  | 
 **uiVisible** | [**ExtrasCustomFieldsListUiVisibleParameter**](ExtrasCustomFieldsListUiVisibleParameter.md) | Specifies whether the custom field is displayed in the UI  * &#x60;always&#x60; - Always * &#x60;if-set&#x60; - If set * &#x60;hidden&#x60; - Hidden | 
 **uiVisibleEmpty** | **bool** |  | 
 **uiVisibleIc** | **[]string** |  | 
 **uiVisibleIe** | **[]string** |  | 
 **uiVisibleIew** | **[]string** |  | 
 **uiVisibleIregex** | **[]string** |  | 
 **uiVisibleIsw** | **[]string** |  | 
 **uiVisibleN** | [**ExtrasCustomFieldsListUiVisibleParameter**](ExtrasCustomFieldsListUiVisibleParameter.md) | Specifies whether the custom field is displayed in the UI  * &#x60;always&#x60; - Always * &#x60;if-set&#x60; - If set * &#x60;hidden&#x60; - Hidden | 
 **uiVisibleNic** | **[]string** |  | 
 **uiVisibleNie** | **[]string** |  | 
 **uiVisibleNiew** | **[]string** |  | 
 **uiVisibleNisw** | **[]string** |  | 
 **uiVisibleRegex** | **[]string** |  | 
 **unique** | **bool** |  | 
 **updatedByRequest** | **string** |  | 
 **validationMaximum** | **[]float64** |  | 
 **validationMaximumEmpty** | **bool** |  | 
 **validationMaximumGt** | **[]float64** |  | 
 **validationMaximumGte** | **[]float64** |  | 
 **validationMaximumLt** | **[]float64** |  | 
 **validationMaximumLte** | **[]float64** |  | 
 **validationMaximumN** | **[]float64** |  | 
 **validationMinimum** | **[]float64** |  | 
 **validationMinimumEmpty** | **bool** |  | 
 **validationMinimumGt** | **[]float64** |  | 
 **validationMinimumGte** | **[]float64** |  | 
 **validationMinimumLt** | **[]float64** |  | 
 **validationMinimumLte** | **[]float64** |  | 
 **validationMinimumN** | **[]float64** |  | 
 **validationRegex** | **[]string** |  | 
 **validationRegexEmpty** | **bool** |  | 
 **validationRegexIc** | **[]string** |  | 
 **validationRegexIe** | **[]string** |  | 
 **validationRegexIew** | **[]string** |  | 
 **validationRegexIregex** | **[]string** |  | 
 **validationRegexIsw** | **[]string** |  | 
 **validationRegexN** | **[]string** |  | 
 **validationRegexNic** | **[]string** |  | 
 **validationRegexNie** | **[]string** |  | 
 **validationRegexNiew** | **[]string** |  | 
 **validationRegexNisw** | **[]string** |  | 
 **validationRegexRegex** | **[]string** |  | 
 **weight** | **[]int32** |  | 
 **weightEmpty** | **bool** |  | 
 **weightGt** | **[]int32** |  | 
 **weightGte** | **[]int32** |  | 
 **weightLt** | **[]int32** |  | 
 **weightLte** | **[]int32** |  | 
 **weightN** | **[]int32** |  | 

### Return type

[**PaginatedCustomFieldList**](PaginatedCustomFieldList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ExtrasCustomFieldsPartialUpdate

> CustomField ExtrasCustomFieldsPartialUpdate(ctx, id).PatchedWritableCustomFieldRequest(patchedWritableCustomFieldRequest).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/airnity/go-netbox/v4"
)

func main() {
	id := int32(56) // int32 | A unique integer value identifying this custom field.
	patchedWritableCustomFieldRequest := *openapiclient.NewPatchedWritableCustomFieldRequest() // PatchedWritableCustomFieldRequest |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ExtrasAPI.ExtrasCustomFieldsPartialUpdate(context.Background(), id).PatchedWritableCustomFieldRequest(patchedWritableCustomFieldRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ExtrasAPI.ExtrasCustomFieldsPartialUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ExtrasCustomFieldsPartialUpdate`: CustomField
	fmt.Fprintf(os.Stdout, "Response from `ExtrasAPI.ExtrasCustomFieldsPartialUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this custom field. | 

### Other Parameters

Other parameters are passed through a pointer to a apiExtrasCustomFieldsPartialUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **patchedWritableCustomFieldRequest** | [**PatchedWritableCustomFieldRequest**](PatchedWritableCustomFieldRequest.md) |  | 

### Return type

[**CustomField**](CustomField.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ExtrasCustomFieldsRetrieve

> CustomField ExtrasCustomFieldsRetrieve(ctx, id).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/airnity/go-netbox/v4"
)

func main() {
	id := int32(56) // int32 | A unique integer value identifying this custom field.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ExtrasAPI.ExtrasCustomFieldsRetrieve(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ExtrasAPI.ExtrasCustomFieldsRetrieve``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ExtrasCustomFieldsRetrieve`: CustomField
	fmt.Fprintf(os.Stdout, "Response from `ExtrasAPI.ExtrasCustomFieldsRetrieve`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this custom field. | 

### Other Parameters

Other parameters are passed through a pointer to a apiExtrasCustomFieldsRetrieveRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**CustomField**](CustomField.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ExtrasCustomFieldsUpdate

> CustomField ExtrasCustomFieldsUpdate(ctx, id).WritableCustomFieldRequest(writableCustomFieldRequest).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/airnity/go-netbox/v4"
)

func main() {
	id := int32(56) // int32 | A unique integer value identifying this custom field.
	writableCustomFieldRequest := *openapiclient.NewWritableCustomFieldRequest([]string{"ObjectTypes_example"}, "Name_example") // WritableCustomFieldRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ExtrasAPI.ExtrasCustomFieldsUpdate(context.Background(), id).WritableCustomFieldRequest(writableCustomFieldRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ExtrasAPI.ExtrasCustomFieldsUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ExtrasCustomFieldsUpdate`: CustomField
	fmt.Fprintf(os.Stdout, "Response from `ExtrasAPI.ExtrasCustomFieldsUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this custom field. | 

### Other Parameters

Other parameters are passed through a pointer to a apiExtrasCustomFieldsUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **writableCustomFieldRequest** | [**WritableCustomFieldRequest**](WritableCustomFieldRequest.md) |  | 

### Return type

[**CustomField**](CustomField.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

