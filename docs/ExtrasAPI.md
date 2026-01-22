# \ExtrasAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ExtrasCustomFieldsBulkPartialUpdate**](ExtrasAPI.md#ExtrasCustomFieldsBulkPartialUpdate) | **Patch** /api/extras/custom-fields/ | 
[**ExtrasCustomFieldsBulkUpdate**](ExtrasAPI.md#ExtrasCustomFieldsBulkUpdate) | **Put** /api/extras/custom-fields/ | 
[**ExtrasCustomFieldsCreate**](ExtrasAPI.md#ExtrasCustomFieldsCreate) | **Post** /api/extras/custom-fields/ | 
[**ExtrasCustomFieldsPartialUpdate**](ExtrasAPI.md#ExtrasCustomFieldsPartialUpdate) | **Patch** /api/extras/custom-fields/{id}/ | 
[**ExtrasCustomFieldsRetrieve**](ExtrasAPI.md#ExtrasCustomFieldsRetrieve) | **Get** /api/extras/custom-fields/{id}/ | 
[**ExtrasCustomFieldsUpdate**](ExtrasAPI.md#ExtrasCustomFieldsUpdate) | **Put** /api/extras/custom-fields/{id}/ | 



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

