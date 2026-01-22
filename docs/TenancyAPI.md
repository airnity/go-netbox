# \TenancyAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**TenancyTenantGroupsBulkPartialUpdate**](TenancyAPI.md#TenancyTenantGroupsBulkPartialUpdate) | **Patch** /api/tenancy/tenant-groups/ | 
[**TenancyTenantGroupsBulkUpdate**](TenancyAPI.md#TenancyTenantGroupsBulkUpdate) | **Put** /api/tenancy/tenant-groups/ | 
[**TenancyTenantGroupsCreate**](TenancyAPI.md#TenancyTenantGroupsCreate) | **Post** /api/tenancy/tenant-groups/ | 
[**TenancyTenantGroupsPartialUpdate**](TenancyAPI.md#TenancyTenantGroupsPartialUpdate) | **Patch** /api/tenancy/tenant-groups/{id}/ | 
[**TenancyTenantGroupsRetrieve**](TenancyAPI.md#TenancyTenantGroupsRetrieve) | **Get** /api/tenancy/tenant-groups/{id}/ | 
[**TenancyTenantGroupsUpdate**](TenancyAPI.md#TenancyTenantGroupsUpdate) | **Put** /api/tenancy/tenant-groups/{id}/ | 
[**TenancyTenantsBulkDestroy**](TenancyAPI.md#TenancyTenantsBulkDestroy) | **Delete** /api/tenancy/tenants/ | 
[**TenancyTenantsBulkPartialUpdate**](TenancyAPI.md#TenancyTenantsBulkPartialUpdate) | **Patch** /api/tenancy/tenants/ | 
[**TenancyTenantsBulkUpdate**](TenancyAPI.md#TenancyTenantsBulkUpdate) | **Put** /api/tenancy/tenants/ | 
[**TenancyTenantsCreate**](TenancyAPI.md#TenancyTenantsCreate) | **Post** /api/tenancy/tenants/ | 
[**TenancyTenantsDestroy**](TenancyAPI.md#TenancyTenantsDestroy) | **Delete** /api/tenancy/tenants/{id}/ | 
[**TenancyTenantsList**](TenancyAPI.md#TenancyTenantsList) | **Get** /api/tenancy/tenants/ | 
[**TenancyTenantsPartialUpdate**](TenancyAPI.md#TenancyTenantsPartialUpdate) | **Patch** /api/tenancy/tenants/{id}/ | 
[**TenancyTenantsRetrieve**](TenancyAPI.md#TenancyTenantsRetrieve) | **Get** /api/tenancy/tenants/{id}/ | 
[**TenancyTenantsUpdate**](TenancyAPI.md#TenancyTenantsUpdate) | **Put** /api/tenancy/tenants/{id}/ | 



## TenancyTenantGroupsBulkPartialUpdate

> []TenantGroup TenancyTenantGroupsBulkPartialUpdate(ctx).TenantGroupRequest(tenantGroupRequest).Execute()





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
	tenantGroupRequest := []openapiclient.TenantGroupRequest{*openapiclient.NewTenantGroupRequest("Name_example", "Slug_example")} // []TenantGroupRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TenancyAPI.TenancyTenantGroupsBulkPartialUpdate(context.Background()).TenantGroupRequest(tenantGroupRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TenancyAPI.TenancyTenantGroupsBulkPartialUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TenancyTenantGroupsBulkPartialUpdate`: []TenantGroup
	fmt.Fprintf(os.Stdout, "Response from `TenancyAPI.TenancyTenantGroupsBulkPartialUpdate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTenancyTenantGroupsBulkPartialUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenantGroupRequest** | [**[]TenantGroupRequest**](TenantGroupRequest.md) |  | 

### Return type

[**[]TenantGroup**](TenantGroup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TenancyTenantGroupsBulkUpdate

> []TenantGroup TenancyTenantGroupsBulkUpdate(ctx).TenantGroupRequest(tenantGroupRequest).Execute()





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
	tenantGroupRequest := []openapiclient.TenantGroupRequest{*openapiclient.NewTenantGroupRequest("Name_example", "Slug_example")} // []TenantGroupRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TenancyAPI.TenancyTenantGroupsBulkUpdate(context.Background()).TenantGroupRequest(tenantGroupRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TenancyAPI.TenancyTenantGroupsBulkUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TenancyTenantGroupsBulkUpdate`: []TenantGroup
	fmt.Fprintf(os.Stdout, "Response from `TenancyAPI.TenancyTenantGroupsBulkUpdate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTenancyTenantGroupsBulkUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenantGroupRequest** | [**[]TenantGroupRequest**](TenantGroupRequest.md) |  | 

### Return type

[**[]TenantGroup**](TenantGroup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TenancyTenantGroupsCreate

> TenantGroup TenancyTenantGroupsCreate(ctx).TenancyTenantGroupsCreateRequest(tenancyTenantGroupsCreateRequest).Execute()





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
	tenancyTenantGroupsCreateRequest := openapiclient.tenancy_tenant_groups_create_request{WritableTenantGroupRequest: openapiclient.NewWritableTenantGroupRequest("Name_example", "Slug_example")} // TenancyTenantGroupsCreateRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TenancyAPI.TenancyTenantGroupsCreate(context.Background()).TenancyTenantGroupsCreateRequest(tenancyTenantGroupsCreateRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TenancyAPI.TenancyTenantGroupsCreate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TenancyTenantGroupsCreate`: TenantGroup
	fmt.Fprintf(os.Stdout, "Response from `TenancyAPI.TenancyTenantGroupsCreate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTenancyTenantGroupsCreateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenancyTenantGroupsCreateRequest** | [**TenancyTenantGroupsCreateRequest**](TenancyTenantGroupsCreateRequest.md) |  | 

### Return type

[**TenantGroup**](TenantGroup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TenancyTenantGroupsPartialUpdate

> TenantGroup TenancyTenantGroupsPartialUpdate(ctx, id).PatchedWritableTenantGroupRequest(patchedWritableTenantGroupRequest).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this tenant group.
	patchedWritableTenantGroupRequest := *openapiclient.NewPatchedWritableTenantGroupRequest() // PatchedWritableTenantGroupRequest |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TenancyAPI.TenancyTenantGroupsPartialUpdate(context.Background(), id).PatchedWritableTenantGroupRequest(patchedWritableTenantGroupRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TenancyAPI.TenancyTenantGroupsPartialUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TenancyTenantGroupsPartialUpdate`: TenantGroup
	fmt.Fprintf(os.Stdout, "Response from `TenancyAPI.TenancyTenantGroupsPartialUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this tenant group. | 

### Other Parameters

Other parameters are passed through a pointer to a apiTenancyTenantGroupsPartialUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **patchedWritableTenantGroupRequest** | [**PatchedWritableTenantGroupRequest**](PatchedWritableTenantGroupRequest.md) |  | 

### Return type

[**TenantGroup**](TenantGroup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TenancyTenantGroupsRetrieve

> TenantGroup TenancyTenantGroupsRetrieve(ctx, id).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this tenant group.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TenancyAPI.TenancyTenantGroupsRetrieve(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TenancyAPI.TenancyTenantGroupsRetrieve``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TenancyTenantGroupsRetrieve`: TenantGroup
	fmt.Fprintf(os.Stdout, "Response from `TenancyAPI.TenancyTenantGroupsRetrieve`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this tenant group. | 

### Other Parameters

Other parameters are passed through a pointer to a apiTenancyTenantGroupsRetrieveRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**TenantGroup**](TenantGroup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TenancyTenantGroupsUpdate

> TenantGroup TenancyTenantGroupsUpdate(ctx, id).WritableTenantGroupRequest(writableTenantGroupRequest).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this tenant group.
	writableTenantGroupRequest := *openapiclient.NewWritableTenantGroupRequest("Name_example", "Slug_example") // WritableTenantGroupRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TenancyAPI.TenancyTenantGroupsUpdate(context.Background(), id).WritableTenantGroupRequest(writableTenantGroupRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TenancyAPI.TenancyTenantGroupsUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TenancyTenantGroupsUpdate`: TenantGroup
	fmt.Fprintf(os.Stdout, "Response from `TenancyAPI.TenancyTenantGroupsUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this tenant group. | 

### Other Parameters

Other parameters are passed through a pointer to a apiTenancyTenantGroupsUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **writableTenantGroupRequest** | [**WritableTenantGroupRequest**](WritableTenantGroupRequest.md) |  | 

### Return type

[**TenantGroup**](TenantGroup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TenancyTenantsBulkDestroy

> TenancyTenantsBulkDestroy(ctx).TenantRequest(tenantRequest).Execute()





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
	tenantRequest := []openapiclient.TenantRequest{*openapiclient.NewTenantRequest("Name_example", "Slug_example")} // []TenantRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TenancyAPI.TenancyTenantsBulkDestroy(context.Background()).TenantRequest(tenantRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TenancyAPI.TenancyTenantsBulkDestroy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTenancyTenantsBulkDestroyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenantRequest** | [**[]TenantRequest**](TenantRequest.md) |  | 

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


## TenancyTenantsBulkPartialUpdate

> []Tenant TenancyTenantsBulkPartialUpdate(ctx).TenantRequest(tenantRequest).Execute()





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
	tenantRequest := []openapiclient.TenantRequest{*openapiclient.NewTenantRequest("Name_example", "Slug_example")} // []TenantRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TenancyAPI.TenancyTenantsBulkPartialUpdate(context.Background()).TenantRequest(tenantRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TenancyAPI.TenancyTenantsBulkPartialUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TenancyTenantsBulkPartialUpdate`: []Tenant
	fmt.Fprintf(os.Stdout, "Response from `TenancyAPI.TenancyTenantsBulkPartialUpdate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTenancyTenantsBulkPartialUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenantRequest** | [**[]TenantRequest**](TenantRequest.md) |  | 

### Return type

[**[]Tenant**](Tenant.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TenancyTenantsBulkUpdate

> []Tenant TenancyTenantsBulkUpdate(ctx).TenantRequest(tenantRequest).Execute()





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
	tenantRequest := []openapiclient.TenantRequest{*openapiclient.NewTenantRequest("Name_example", "Slug_example")} // []TenantRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TenancyAPI.TenancyTenantsBulkUpdate(context.Background()).TenantRequest(tenantRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TenancyAPI.TenancyTenantsBulkUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TenancyTenantsBulkUpdate`: []Tenant
	fmt.Fprintf(os.Stdout, "Response from `TenancyAPI.TenancyTenantsBulkUpdate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTenancyTenantsBulkUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenantRequest** | [**[]TenantRequest**](TenantRequest.md) |  | 

### Return type

[**[]Tenant**](Tenant.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TenancyTenantsCreate

> Tenant TenancyTenantsCreate(ctx).TenancyTenantsCreateRequest(tenancyTenantsCreateRequest).Execute()





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
	tenancyTenantsCreateRequest := openapiclient.tenancy_tenants_create_request{TenantRequest: openapiclient.NewTenantRequest("Name_example", "Slug_example")} // TenancyTenantsCreateRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TenancyAPI.TenancyTenantsCreate(context.Background()).TenancyTenantsCreateRequest(tenancyTenantsCreateRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TenancyAPI.TenancyTenantsCreate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TenancyTenantsCreate`: Tenant
	fmt.Fprintf(os.Stdout, "Response from `TenancyAPI.TenancyTenantsCreate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTenancyTenantsCreateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenancyTenantsCreateRequest** | [**TenancyTenantsCreateRequest**](TenancyTenantsCreateRequest.md) |  | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TenancyTenantsDestroy

> TenancyTenantsDestroy(ctx, id).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this tenant.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TenancyAPI.TenancyTenantsDestroy(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TenancyAPI.TenancyTenantsDestroy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this tenant. | 

### Other Parameters

Other parameters are passed through a pointer to a apiTenancyTenantsDestroyRequest struct via the builder pattern


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


## TenancyTenantsList

> PaginatedTenantList TenancyTenantsList(ctx).Contact(contact).ContactN(contactN).ContactGroup(contactGroup).ContactGroupN(contactGroupN).ContactRole(contactRole).ContactRoleN(contactRoleN).Created(created).CreatedEmpty(createdEmpty).CreatedGt(createdGt).CreatedGte(createdGte).CreatedLt(createdLt).CreatedLte(createdLte).CreatedN(createdN).CreatedByRequest(createdByRequest).Description(description).DescriptionEmpty(descriptionEmpty).DescriptionIc(descriptionIc).DescriptionIe(descriptionIe).DescriptionIew(descriptionIew).DescriptionIregex(descriptionIregex).DescriptionIsw(descriptionIsw).DescriptionN(descriptionN).DescriptionNic(descriptionNic).DescriptionNie(descriptionNie).DescriptionNiew(descriptionNiew).DescriptionNisw(descriptionNisw).DescriptionRegex(descriptionRegex).Group(group).GroupN(groupN).GroupId(groupId).GroupIdN(groupIdN).Id(id).IdEmpty(idEmpty).IdGt(idGt).IdGte(idGte).IdLt(idLt).IdLte(idLte).IdN(idN).LastUpdated(lastUpdated).LastUpdatedEmpty(lastUpdatedEmpty).LastUpdatedGt(lastUpdatedGt).LastUpdatedGte(lastUpdatedGte).LastUpdatedLt(lastUpdatedLt).LastUpdatedLte(lastUpdatedLte).LastUpdatedN(lastUpdatedN).Limit(limit).ModifiedByRequest(modifiedByRequest).Name(name).NameEmpty(nameEmpty).NameIc(nameIc).NameIe(nameIe).NameIew(nameIew).NameIregex(nameIregex).NameIsw(nameIsw).NameN(nameN).NameNic(nameNic).NameNie(nameNie).NameNiew(nameNiew).NameNisw(nameNisw).NameRegex(nameRegex).Offset(offset).Ordering(ordering).Owner(owner).OwnerN(ownerN).OwnerId(ownerId).OwnerIdN(ownerIdN).Q(q).Slug(slug).SlugEmpty(slugEmpty).SlugIc(slugIc).SlugIe(slugIe).SlugIew(slugIew).SlugIregex(slugIregex).SlugIsw(slugIsw).SlugN(slugN).SlugNic(slugNic).SlugNie(slugNie).SlugNiew(slugNiew).SlugNisw(slugNisw).SlugRegex(slugRegex).Tag(tag).TagN(tagN).TagId(tagId).TagIdN(tagIdN).UpdatedByRequest(updatedByRequest).Execute()





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
	contact := []int32{int32(123)} // []int32 | Contact (optional)
	contactN := []int32{int32(123)} // []int32 | Contact (optional)
	contactGroup := []string{"Inner_example"} // []string |  (optional)
	contactGroupN := []string{"Inner_example"} // []string |  (optional)
	contactRole := []int32{int32(123)} // []int32 | Contact Role (optional)
	contactRoleN := []int32{int32(123)} // []int32 | Contact Role (optional)
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
	group := []string{"Inner_example"} // []string |  (optional)
	groupN := []string{"Inner_example"} // []string |  (optional)
	groupId := []string{"Inner_example"} // []string |  (optional)
	groupIdN := []string{"Inner_example"} // []string |  (optional)
	id := []int32{int32(123)} // []int32 |  (optional)
	idEmpty := true // bool |  (optional)
	idGt := []int32{int32(123)} // []int32 |  (optional)
	idGte := []int32{int32(123)} // []int32 |  (optional)
	idLt := []int32{int32(123)} // []int32 |  (optional)
	idLte := []int32{int32(123)} // []int32 |  (optional)
	idN := []int32{int32(123)} // []int32 |  (optional)
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
	offset := int32(56) // int32 | The initial index from which to return the results. (optional)
	ordering := "ordering_example" // string | Which field to use when ordering the results. (optional)
	owner := []string{"Inner_example"} // []string | Owner (name) (optional)
	ownerN := []string{"Inner_example"} // []string | Owner (name) (optional)
	ownerId := []*int32{int32(123)} // []*int32 | Owner (ID) (optional)
	ownerIdN := []*int32{int32(123)} // []*int32 | Owner (ID) (optional)
	q := "q_example" // string | Search (optional)
	slug := []string{"Inner_example"} // []string |  (optional)
	slugEmpty := true // bool |  (optional)
	slugIc := []string{"Inner_example"} // []string |  (optional)
	slugIe := []string{"Inner_example"} // []string |  (optional)
	slugIew := []string{"Inner_example"} // []string |  (optional)
	slugIregex := []string{"Inner_example"} // []string |  (optional)
	slugIsw := []string{"Inner_example"} // []string |  (optional)
	slugN := []string{"Inner_example"} // []string |  (optional)
	slugNic := []string{"Inner_example"} // []string |  (optional)
	slugNie := []string{"Inner_example"} // []string |  (optional)
	slugNiew := []string{"Inner_example"} // []string |  (optional)
	slugNisw := []string{"Inner_example"} // []string |  (optional)
	slugRegex := []string{"Inner_example"} // []string |  (optional)
	tag := []string{"Inner_example"} // []string |  (optional)
	tagN := []string{"Inner_example"} // []string |  (optional)
	tagId := []string{"Inner_example"} // []string |  (optional)
	tagIdN := []string{"Inner_example"} // []string |  (optional)
	updatedByRequest := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TenancyAPI.TenancyTenantsList(context.Background()).Contact(contact).ContactN(contactN).ContactGroup(contactGroup).ContactGroupN(contactGroupN).ContactRole(contactRole).ContactRoleN(contactRoleN).Created(created).CreatedEmpty(createdEmpty).CreatedGt(createdGt).CreatedGte(createdGte).CreatedLt(createdLt).CreatedLte(createdLte).CreatedN(createdN).CreatedByRequest(createdByRequest).Description(description).DescriptionEmpty(descriptionEmpty).DescriptionIc(descriptionIc).DescriptionIe(descriptionIe).DescriptionIew(descriptionIew).DescriptionIregex(descriptionIregex).DescriptionIsw(descriptionIsw).DescriptionN(descriptionN).DescriptionNic(descriptionNic).DescriptionNie(descriptionNie).DescriptionNiew(descriptionNiew).DescriptionNisw(descriptionNisw).DescriptionRegex(descriptionRegex).Group(group).GroupN(groupN).GroupId(groupId).GroupIdN(groupIdN).Id(id).IdEmpty(idEmpty).IdGt(idGt).IdGte(idGte).IdLt(idLt).IdLte(idLte).IdN(idN).LastUpdated(lastUpdated).LastUpdatedEmpty(lastUpdatedEmpty).LastUpdatedGt(lastUpdatedGt).LastUpdatedGte(lastUpdatedGte).LastUpdatedLt(lastUpdatedLt).LastUpdatedLte(lastUpdatedLte).LastUpdatedN(lastUpdatedN).Limit(limit).ModifiedByRequest(modifiedByRequest).Name(name).NameEmpty(nameEmpty).NameIc(nameIc).NameIe(nameIe).NameIew(nameIew).NameIregex(nameIregex).NameIsw(nameIsw).NameN(nameN).NameNic(nameNic).NameNie(nameNie).NameNiew(nameNiew).NameNisw(nameNisw).NameRegex(nameRegex).Offset(offset).Ordering(ordering).Owner(owner).OwnerN(ownerN).OwnerId(ownerId).OwnerIdN(ownerIdN).Q(q).Slug(slug).SlugEmpty(slugEmpty).SlugIc(slugIc).SlugIe(slugIe).SlugIew(slugIew).SlugIregex(slugIregex).SlugIsw(slugIsw).SlugN(slugN).SlugNic(slugNic).SlugNie(slugNie).SlugNiew(slugNiew).SlugNisw(slugNisw).SlugRegex(slugRegex).Tag(tag).TagN(tagN).TagId(tagId).TagIdN(tagIdN).UpdatedByRequest(updatedByRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TenancyAPI.TenancyTenantsList``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TenancyTenantsList`: PaginatedTenantList
	fmt.Fprintf(os.Stdout, "Response from `TenancyAPI.TenancyTenantsList`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTenancyTenantsListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact** | **[]int32** | Contact | 
 **contactN** | **[]int32** | Contact | 
 **contactGroup** | **[]string** |  | 
 **contactGroupN** | **[]string** |  | 
 **contactRole** | **[]int32** | Contact Role | 
 **contactRoleN** | **[]int32** | Contact Role | 
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
 **group** | **[]string** |  | 
 **groupN** | **[]string** |  | 
 **groupId** | **[]string** |  | 
 **groupIdN** | **[]string** |  | 
 **id** | **[]int32** |  | 
 **idEmpty** | **bool** |  | 
 **idGt** | **[]int32** |  | 
 **idGte** | **[]int32** |  | 
 **idLt** | **[]int32** |  | 
 **idLte** | **[]int32** |  | 
 **idN** | **[]int32** |  | 
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
 **offset** | **int32** | The initial index from which to return the results. | 
 **ordering** | **string** | Which field to use when ordering the results. | 
 **owner** | **[]string** | Owner (name) | 
 **ownerN** | **[]string** | Owner (name) | 
 **ownerId** | **[]int32** | Owner (ID) | 
 **ownerIdN** | **[]int32** | Owner (ID) | 
 **q** | **string** | Search | 
 **slug** | **[]string** |  | 
 **slugEmpty** | **bool** |  | 
 **slugIc** | **[]string** |  | 
 **slugIe** | **[]string** |  | 
 **slugIew** | **[]string** |  | 
 **slugIregex** | **[]string** |  | 
 **slugIsw** | **[]string** |  | 
 **slugN** | **[]string** |  | 
 **slugNic** | **[]string** |  | 
 **slugNie** | **[]string** |  | 
 **slugNiew** | **[]string** |  | 
 **slugNisw** | **[]string** |  | 
 **slugRegex** | **[]string** |  | 
 **tag** | **[]string** |  | 
 **tagN** | **[]string** |  | 
 **tagId** | **[]string** |  | 
 **tagIdN** | **[]string** |  | 
 **updatedByRequest** | **string** |  | 

### Return type

[**PaginatedTenantList**](PaginatedTenantList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TenancyTenantsPartialUpdate

> Tenant TenancyTenantsPartialUpdate(ctx, id).PatchedTenantRequest(patchedTenantRequest).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this tenant.
	patchedTenantRequest := *openapiclient.NewPatchedTenantRequest() // PatchedTenantRequest |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TenancyAPI.TenancyTenantsPartialUpdate(context.Background(), id).PatchedTenantRequest(patchedTenantRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TenancyAPI.TenancyTenantsPartialUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TenancyTenantsPartialUpdate`: Tenant
	fmt.Fprintf(os.Stdout, "Response from `TenancyAPI.TenancyTenantsPartialUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this tenant. | 

### Other Parameters

Other parameters are passed through a pointer to a apiTenancyTenantsPartialUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **patchedTenantRequest** | [**PatchedTenantRequest**](PatchedTenantRequest.md) |  | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TenancyTenantsRetrieve

> Tenant TenancyTenantsRetrieve(ctx, id).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this tenant.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TenancyAPI.TenancyTenantsRetrieve(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TenancyAPI.TenancyTenantsRetrieve``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TenancyTenantsRetrieve`: Tenant
	fmt.Fprintf(os.Stdout, "Response from `TenancyAPI.TenancyTenantsRetrieve`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this tenant. | 

### Other Parameters

Other parameters are passed through a pointer to a apiTenancyTenantsRetrieveRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**Tenant**](Tenant.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TenancyTenantsUpdate

> Tenant TenancyTenantsUpdate(ctx, id).TenantRequest(tenantRequest).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this tenant.
	tenantRequest := *openapiclient.NewTenantRequest("Name_example", "Slug_example") // TenantRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TenancyAPI.TenancyTenantsUpdate(context.Background(), id).TenantRequest(tenantRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TenancyAPI.TenancyTenantsUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TenancyTenantsUpdate`: Tenant
	fmt.Fprintf(os.Stdout, "Response from `TenancyAPI.TenancyTenantsUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this tenant. | 

### Other Parameters

Other parameters are passed through a pointer to a apiTenancyTenantsUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **tenantRequest** | [**TenantRequest**](TenantRequest.md) |  | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

