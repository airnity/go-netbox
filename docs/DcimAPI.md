# \DcimAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DcimRegionsBulkDestroy**](DcimAPI.md#DcimRegionsBulkDestroy) | **Delete** /api/dcim/regions/ | 
[**DcimRegionsBulkPartialUpdate**](DcimAPI.md#DcimRegionsBulkPartialUpdate) | **Patch** /api/dcim/regions/ | 
[**DcimRegionsBulkUpdate**](DcimAPI.md#DcimRegionsBulkUpdate) | **Put** /api/dcim/regions/ | 
[**DcimRegionsCreate**](DcimAPI.md#DcimRegionsCreate) | **Post** /api/dcim/regions/ | 
[**DcimRegionsDestroy**](DcimAPI.md#DcimRegionsDestroy) | **Delete** /api/dcim/regions/{id}/ | 
[**DcimRegionsList**](DcimAPI.md#DcimRegionsList) | **Get** /api/dcim/regions/ | 
[**DcimRegionsPartialUpdate**](DcimAPI.md#DcimRegionsPartialUpdate) | **Patch** /api/dcim/regions/{id}/ | 
[**DcimRegionsRetrieve**](DcimAPI.md#DcimRegionsRetrieve) | **Get** /api/dcim/regions/{id}/ | 
[**DcimRegionsUpdate**](DcimAPI.md#DcimRegionsUpdate) | **Put** /api/dcim/regions/{id}/ | 
[**DcimSiteGroupsBulkDestroy**](DcimAPI.md#DcimSiteGroupsBulkDestroy) | **Delete** /api/dcim/site-groups/ | 
[**DcimSiteGroupsBulkPartialUpdate**](DcimAPI.md#DcimSiteGroupsBulkPartialUpdate) | **Patch** /api/dcim/site-groups/ | 
[**DcimSiteGroupsBulkUpdate**](DcimAPI.md#DcimSiteGroupsBulkUpdate) | **Put** /api/dcim/site-groups/ | 
[**DcimSiteGroupsCreate**](DcimAPI.md#DcimSiteGroupsCreate) | **Post** /api/dcim/site-groups/ | 
[**DcimSiteGroupsDestroy**](DcimAPI.md#DcimSiteGroupsDestroy) | **Delete** /api/dcim/site-groups/{id}/ | 
[**DcimSiteGroupsList**](DcimAPI.md#DcimSiteGroupsList) | **Get** /api/dcim/site-groups/ | 
[**DcimSiteGroupsPartialUpdate**](DcimAPI.md#DcimSiteGroupsPartialUpdate) | **Patch** /api/dcim/site-groups/{id}/ | 
[**DcimSiteGroupsRetrieve**](DcimAPI.md#DcimSiteGroupsRetrieve) | **Get** /api/dcim/site-groups/{id}/ | 
[**DcimSiteGroupsUpdate**](DcimAPI.md#DcimSiteGroupsUpdate) | **Put** /api/dcim/site-groups/{id}/ | 
[**DcimSitesBulkDestroy**](DcimAPI.md#DcimSitesBulkDestroy) | **Delete** /api/dcim/sites/ | 
[**DcimSitesBulkPartialUpdate**](DcimAPI.md#DcimSitesBulkPartialUpdate) | **Patch** /api/dcim/sites/ | 
[**DcimSitesBulkUpdate**](DcimAPI.md#DcimSitesBulkUpdate) | **Put** /api/dcim/sites/ | 
[**DcimSitesCreate**](DcimAPI.md#DcimSitesCreate) | **Post** /api/dcim/sites/ | 
[**DcimSitesDestroy**](DcimAPI.md#DcimSitesDestroy) | **Delete** /api/dcim/sites/{id}/ | 
[**DcimSitesList**](DcimAPI.md#DcimSitesList) | **Get** /api/dcim/sites/ | 
[**DcimSitesPartialUpdate**](DcimAPI.md#DcimSitesPartialUpdate) | **Patch** /api/dcim/sites/{id}/ | 
[**DcimSitesRetrieve**](DcimAPI.md#DcimSitesRetrieve) | **Get** /api/dcim/sites/{id}/ | 
[**DcimSitesUpdate**](DcimAPI.md#DcimSitesUpdate) | **Put** /api/dcim/sites/{id}/ | 



## DcimRegionsBulkDestroy

> DcimRegionsBulkDestroy(ctx).RegionRequest(regionRequest).Execute()





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
	regionRequest := []openapiclient.RegionRequest{*openapiclient.NewRegionRequest("Name_example", "Slug_example")} // []RegionRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DcimAPI.DcimRegionsBulkDestroy(context.Background()).RegionRequest(regionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimRegionsBulkDestroy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDcimRegionsBulkDestroyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regionRequest** | [**[]RegionRequest**](RegionRequest.md) |  | 

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


## DcimRegionsBulkPartialUpdate

> []Region DcimRegionsBulkPartialUpdate(ctx).RegionRequest(regionRequest).Execute()





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
	regionRequest := []openapiclient.RegionRequest{*openapiclient.NewRegionRequest("Name_example", "Slug_example")} // []RegionRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DcimAPI.DcimRegionsBulkPartialUpdate(context.Background()).RegionRequest(regionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimRegionsBulkPartialUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DcimRegionsBulkPartialUpdate`: []Region
	fmt.Fprintf(os.Stdout, "Response from `DcimAPI.DcimRegionsBulkPartialUpdate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDcimRegionsBulkPartialUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regionRequest** | [**[]RegionRequest**](RegionRequest.md) |  | 

### Return type

[**[]Region**](Region.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DcimRegionsBulkUpdate

> []Region DcimRegionsBulkUpdate(ctx).RegionRequest(regionRequest).Execute()





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
	regionRequest := []openapiclient.RegionRequest{*openapiclient.NewRegionRequest("Name_example", "Slug_example")} // []RegionRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DcimAPI.DcimRegionsBulkUpdate(context.Background()).RegionRequest(regionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimRegionsBulkUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DcimRegionsBulkUpdate`: []Region
	fmt.Fprintf(os.Stdout, "Response from `DcimAPI.DcimRegionsBulkUpdate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDcimRegionsBulkUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regionRequest** | [**[]RegionRequest**](RegionRequest.md) |  | 

### Return type

[**[]Region**](Region.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DcimRegionsCreate

> Region DcimRegionsCreate(ctx).DcimRegionsCreateRequest(dcimRegionsCreateRequest).Execute()





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
	dcimRegionsCreateRequest := openapiclient.dcim_regions_create_request{WritableRegionRequest: openapiclient.NewWritableRegionRequest("Name_example", "Slug_example")} // DcimRegionsCreateRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DcimAPI.DcimRegionsCreate(context.Background()).DcimRegionsCreateRequest(dcimRegionsCreateRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimRegionsCreate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DcimRegionsCreate`: Region
	fmt.Fprintf(os.Stdout, "Response from `DcimAPI.DcimRegionsCreate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDcimRegionsCreateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dcimRegionsCreateRequest** | [**DcimRegionsCreateRequest**](DcimRegionsCreateRequest.md) |  | 

### Return type

[**Region**](Region.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DcimRegionsDestroy

> DcimRegionsDestroy(ctx, id).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this region.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DcimAPI.DcimRegionsDestroy(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimRegionsDestroy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this region. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDcimRegionsDestroyRequest struct via the builder pattern


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


## DcimRegionsList

> PaginatedRegionList DcimRegionsList(ctx).Ancestor(ancestor).AncestorN(ancestorN).AncestorId(ancestorId).AncestorIdN(ancestorIdN).Contact(contact).ContactN(contactN).ContactGroup(contactGroup).ContactGroupN(contactGroupN).ContactRole(contactRole).ContactRoleN(contactRoleN).Created(created).CreatedEmpty(createdEmpty).CreatedGt(createdGt).CreatedGte(createdGte).CreatedLt(createdLt).CreatedLte(createdLte).CreatedN(createdN).CreatedByRequest(createdByRequest).Description(description).DescriptionEmpty(descriptionEmpty).DescriptionIc(descriptionIc).DescriptionIe(descriptionIe).DescriptionIew(descriptionIew).DescriptionIregex(descriptionIregex).DescriptionIsw(descriptionIsw).DescriptionN(descriptionN).DescriptionNic(descriptionNic).DescriptionNie(descriptionNie).DescriptionNiew(descriptionNiew).DescriptionNisw(descriptionNisw).DescriptionRegex(descriptionRegex).Id(id).IdEmpty(idEmpty).IdGt(idGt).IdGte(idGte).IdLt(idLt).IdLte(idLte).IdN(idN).LastUpdated(lastUpdated).LastUpdatedEmpty(lastUpdatedEmpty).LastUpdatedGt(lastUpdatedGt).LastUpdatedGte(lastUpdatedGte).LastUpdatedLt(lastUpdatedLt).LastUpdatedLte(lastUpdatedLte).LastUpdatedN(lastUpdatedN).Limit(limit).ModifiedByRequest(modifiedByRequest).Name(name).NameEmpty(nameEmpty).NameIc(nameIc).NameIe(nameIe).NameIew(nameIew).NameIregex(nameIregex).NameIsw(nameIsw).NameN(nameN).NameNic(nameNic).NameNie(nameNie).NameNiew(nameNiew).NameNisw(nameNisw).NameRegex(nameRegex).Offset(offset).Ordering(ordering).Owner(owner).OwnerN(ownerN).OwnerGroup(ownerGroup).OwnerGroupN(ownerGroupN).OwnerGroupId(ownerGroupId).OwnerGroupIdN(ownerGroupIdN).OwnerId(ownerId).OwnerIdN(ownerIdN).Parent(parent).ParentN(parentN).ParentId(parentId).ParentIdN(parentIdN).Q(q).Slug(slug).SlugEmpty(slugEmpty).SlugIc(slugIc).SlugIe(slugIe).SlugIew(slugIew).SlugIregex(slugIregex).SlugIsw(slugIsw).SlugN(slugN).SlugNic(slugNic).SlugNie(slugNie).SlugNiew(slugNiew).SlugNisw(slugNisw).SlugRegex(slugRegex).Tag(tag).TagN(tagN).TagId(tagId).TagIdN(tagIdN).UpdatedByRequest(updatedByRequest).Execute()





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
	ancestor := []string{"Inner_example"} // []string |  (optional)
	ancestorN := []string{"Inner_example"} // []string |  (optional)
	ancestorId := []string{"Inner_example"} // []string |  (optional)
	ancestorIdN := []string{"Inner_example"} // []string |  (optional)
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
	ownerGroup := []string{"Inner_example"} // []string | Owner Group (name) (optional)
	ownerGroupN := []string{"Inner_example"} // []string | Owner Group (name) (optional)
	ownerGroupId := []int32{int32(123)} // []int32 | Owner Group (ID) (optional)
	ownerGroupIdN := []int32{int32(123)} // []int32 | Owner Group (ID) (optional)
	ownerId := []*int32{int32(123)} // []*int32 | Owner (ID) (optional)
	ownerIdN := []*int32{int32(123)} // []*int32 | Owner (ID) (optional)
	parent := []string{"Inner_example"} // []string | Parent region (slug) (optional)
	parentN := []string{"Inner_example"} // []string | Parent region (slug) (optional)
	parentId := []*int32{int32(123)} // []*int32 | Parent region (ID) (optional)
	parentIdN := []*int32{int32(123)} // []*int32 | Parent region (ID) (optional)
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
	resp, r, err := apiClient.DcimAPI.DcimRegionsList(context.Background()).Ancestor(ancestor).AncestorN(ancestorN).AncestorId(ancestorId).AncestorIdN(ancestorIdN).Contact(contact).ContactN(contactN).ContactGroup(contactGroup).ContactGroupN(contactGroupN).ContactRole(contactRole).ContactRoleN(contactRoleN).Created(created).CreatedEmpty(createdEmpty).CreatedGt(createdGt).CreatedGte(createdGte).CreatedLt(createdLt).CreatedLte(createdLte).CreatedN(createdN).CreatedByRequest(createdByRequest).Description(description).DescriptionEmpty(descriptionEmpty).DescriptionIc(descriptionIc).DescriptionIe(descriptionIe).DescriptionIew(descriptionIew).DescriptionIregex(descriptionIregex).DescriptionIsw(descriptionIsw).DescriptionN(descriptionN).DescriptionNic(descriptionNic).DescriptionNie(descriptionNie).DescriptionNiew(descriptionNiew).DescriptionNisw(descriptionNisw).DescriptionRegex(descriptionRegex).Id(id).IdEmpty(idEmpty).IdGt(idGt).IdGte(idGte).IdLt(idLt).IdLte(idLte).IdN(idN).LastUpdated(lastUpdated).LastUpdatedEmpty(lastUpdatedEmpty).LastUpdatedGt(lastUpdatedGt).LastUpdatedGte(lastUpdatedGte).LastUpdatedLt(lastUpdatedLt).LastUpdatedLte(lastUpdatedLte).LastUpdatedN(lastUpdatedN).Limit(limit).ModifiedByRequest(modifiedByRequest).Name(name).NameEmpty(nameEmpty).NameIc(nameIc).NameIe(nameIe).NameIew(nameIew).NameIregex(nameIregex).NameIsw(nameIsw).NameN(nameN).NameNic(nameNic).NameNie(nameNie).NameNiew(nameNiew).NameNisw(nameNisw).NameRegex(nameRegex).Offset(offset).Ordering(ordering).Owner(owner).OwnerN(ownerN).OwnerGroup(ownerGroup).OwnerGroupN(ownerGroupN).OwnerGroupId(ownerGroupId).OwnerGroupIdN(ownerGroupIdN).OwnerId(ownerId).OwnerIdN(ownerIdN).Parent(parent).ParentN(parentN).ParentId(parentId).ParentIdN(parentIdN).Q(q).Slug(slug).SlugEmpty(slugEmpty).SlugIc(slugIc).SlugIe(slugIe).SlugIew(slugIew).SlugIregex(slugIregex).SlugIsw(slugIsw).SlugN(slugN).SlugNic(slugNic).SlugNie(slugNie).SlugNiew(slugNiew).SlugNisw(slugNisw).SlugRegex(slugRegex).Tag(tag).TagN(tagN).TagId(tagId).TagIdN(tagIdN).UpdatedByRequest(updatedByRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimRegionsList``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DcimRegionsList`: PaginatedRegionList
	fmt.Fprintf(os.Stdout, "Response from `DcimAPI.DcimRegionsList`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDcimRegionsListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ancestor** | **[]string** |  | 
 **ancestorN** | **[]string** |  | 
 **ancestorId** | **[]string** |  | 
 **ancestorIdN** | **[]string** |  | 
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
 **ownerGroup** | **[]string** | Owner Group (name) | 
 **ownerGroupN** | **[]string** | Owner Group (name) | 
 **ownerGroupId** | **[]int32** | Owner Group (ID) | 
 **ownerGroupIdN** | **[]int32** | Owner Group (ID) | 
 **ownerId** | **[]int32** | Owner (ID) | 
 **ownerIdN** | **[]int32** | Owner (ID) | 
 **parent** | **[]string** | Parent region (slug) | 
 **parentN** | **[]string** | Parent region (slug) | 
 **parentId** | **[]int32** | Parent region (ID) | 
 **parentIdN** | **[]int32** | Parent region (ID) | 
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

[**PaginatedRegionList**](PaginatedRegionList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DcimRegionsPartialUpdate

> Region DcimRegionsPartialUpdate(ctx, id).PatchedWritableRegionRequest(patchedWritableRegionRequest).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this region.
	patchedWritableRegionRequest := *openapiclient.NewPatchedWritableRegionRequest() // PatchedWritableRegionRequest |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DcimAPI.DcimRegionsPartialUpdate(context.Background(), id).PatchedWritableRegionRequest(patchedWritableRegionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimRegionsPartialUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DcimRegionsPartialUpdate`: Region
	fmt.Fprintf(os.Stdout, "Response from `DcimAPI.DcimRegionsPartialUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this region. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDcimRegionsPartialUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **patchedWritableRegionRequest** | [**PatchedWritableRegionRequest**](PatchedWritableRegionRequest.md) |  | 

### Return type

[**Region**](Region.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DcimRegionsRetrieve

> Region DcimRegionsRetrieve(ctx, id).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this region.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DcimAPI.DcimRegionsRetrieve(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimRegionsRetrieve``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DcimRegionsRetrieve`: Region
	fmt.Fprintf(os.Stdout, "Response from `DcimAPI.DcimRegionsRetrieve`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this region. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDcimRegionsRetrieveRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**Region**](Region.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DcimRegionsUpdate

> Region DcimRegionsUpdate(ctx, id).WritableRegionRequest(writableRegionRequest).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this region.
	writableRegionRequest := *openapiclient.NewWritableRegionRequest("Name_example", "Slug_example") // WritableRegionRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DcimAPI.DcimRegionsUpdate(context.Background(), id).WritableRegionRequest(writableRegionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimRegionsUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DcimRegionsUpdate`: Region
	fmt.Fprintf(os.Stdout, "Response from `DcimAPI.DcimRegionsUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this region. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDcimRegionsUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **writableRegionRequest** | [**WritableRegionRequest**](WritableRegionRequest.md) |  | 

### Return type

[**Region**](Region.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DcimSiteGroupsBulkDestroy

> DcimSiteGroupsBulkDestroy(ctx).SiteGroupRequest(siteGroupRequest).Execute()





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
	siteGroupRequest := []openapiclient.SiteGroupRequest{*openapiclient.NewSiteGroupRequest("Name_example", "Slug_example")} // []SiteGroupRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DcimAPI.DcimSiteGroupsBulkDestroy(context.Background()).SiteGroupRequest(siteGroupRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimSiteGroupsBulkDestroy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDcimSiteGroupsBulkDestroyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **siteGroupRequest** | [**[]SiteGroupRequest**](SiteGroupRequest.md) |  | 

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


## DcimSiteGroupsBulkPartialUpdate

> []SiteGroup DcimSiteGroupsBulkPartialUpdate(ctx).SiteGroupRequest(siteGroupRequest).Execute()





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
	siteGroupRequest := []openapiclient.SiteGroupRequest{*openapiclient.NewSiteGroupRequest("Name_example", "Slug_example")} // []SiteGroupRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DcimAPI.DcimSiteGroupsBulkPartialUpdate(context.Background()).SiteGroupRequest(siteGroupRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimSiteGroupsBulkPartialUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DcimSiteGroupsBulkPartialUpdate`: []SiteGroup
	fmt.Fprintf(os.Stdout, "Response from `DcimAPI.DcimSiteGroupsBulkPartialUpdate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDcimSiteGroupsBulkPartialUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **siteGroupRequest** | [**[]SiteGroupRequest**](SiteGroupRequest.md) |  | 

### Return type

[**[]SiteGroup**](SiteGroup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DcimSiteGroupsBulkUpdate

> []SiteGroup DcimSiteGroupsBulkUpdate(ctx).SiteGroupRequest(siteGroupRequest).Execute()





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
	siteGroupRequest := []openapiclient.SiteGroupRequest{*openapiclient.NewSiteGroupRequest("Name_example", "Slug_example")} // []SiteGroupRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DcimAPI.DcimSiteGroupsBulkUpdate(context.Background()).SiteGroupRequest(siteGroupRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimSiteGroupsBulkUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DcimSiteGroupsBulkUpdate`: []SiteGroup
	fmt.Fprintf(os.Stdout, "Response from `DcimAPI.DcimSiteGroupsBulkUpdate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDcimSiteGroupsBulkUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **siteGroupRequest** | [**[]SiteGroupRequest**](SiteGroupRequest.md) |  | 

### Return type

[**[]SiteGroup**](SiteGroup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DcimSiteGroupsCreate

> SiteGroup DcimSiteGroupsCreate(ctx).DcimSiteGroupsCreateRequest(dcimSiteGroupsCreateRequest).Execute()





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
	dcimSiteGroupsCreateRequest := openapiclient.dcim_site_groups_create_request{WritableSiteGroupRequest: openapiclient.NewWritableSiteGroupRequest("Name_example", "Slug_example")} // DcimSiteGroupsCreateRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DcimAPI.DcimSiteGroupsCreate(context.Background()).DcimSiteGroupsCreateRequest(dcimSiteGroupsCreateRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimSiteGroupsCreate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DcimSiteGroupsCreate`: SiteGroup
	fmt.Fprintf(os.Stdout, "Response from `DcimAPI.DcimSiteGroupsCreate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDcimSiteGroupsCreateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dcimSiteGroupsCreateRequest** | [**DcimSiteGroupsCreateRequest**](DcimSiteGroupsCreateRequest.md) |  | 

### Return type

[**SiteGroup**](SiteGroup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DcimSiteGroupsDestroy

> DcimSiteGroupsDestroy(ctx, id).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this site group.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DcimAPI.DcimSiteGroupsDestroy(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimSiteGroupsDestroy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this site group. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDcimSiteGroupsDestroyRequest struct via the builder pattern


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


## DcimSiteGroupsList

> PaginatedSiteGroupList DcimSiteGroupsList(ctx).Ancestor(ancestor).AncestorN(ancestorN).AncestorId(ancestorId).AncestorIdN(ancestorIdN).Contact(contact).ContactN(contactN).ContactGroup(contactGroup).ContactGroupN(contactGroupN).ContactRole(contactRole).ContactRoleN(contactRoleN).Created(created).CreatedEmpty(createdEmpty).CreatedGt(createdGt).CreatedGte(createdGte).CreatedLt(createdLt).CreatedLte(createdLte).CreatedN(createdN).CreatedByRequest(createdByRequest).Description(description).DescriptionEmpty(descriptionEmpty).DescriptionIc(descriptionIc).DescriptionIe(descriptionIe).DescriptionIew(descriptionIew).DescriptionIregex(descriptionIregex).DescriptionIsw(descriptionIsw).DescriptionN(descriptionN).DescriptionNic(descriptionNic).DescriptionNie(descriptionNie).DescriptionNiew(descriptionNiew).DescriptionNisw(descriptionNisw).DescriptionRegex(descriptionRegex).Id(id).IdEmpty(idEmpty).IdGt(idGt).IdGte(idGte).IdLt(idLt).IdLte(idLte).IdN(idN).LastUpdated(lastUpdated).LastUpdatedEmpty(lastUpdatedEmpty).LastUpdatedGt(lastUpdatedGt).LastUpdatedGte(lastUpdatedGte).LastUpdatedLt(lastUpdatedLt).LastUpdatedLte(lastUpdatedLte).LastUpdatedN(lastUpdatedN).Limit(limit).ModifiedByRequest(modifiedByRequest).Name(name).NameEmpty(nameEmpty).NameIc(nameIc).NameIe(nameIe).NameIew(nameIew).NameIregex(nameIregex).NameIsw(nameIsw).NameN(nameN).NameNic(nameNic).NameNie(nameNie).NameNiew(nameNiew).NameNisw(nameNisw).NameRegex(nameRegex).Offset(offset).Ordering(ordering).Owner(owner).OwnerN(ownerN).OwnerGroup(ownerGroup).OwnerGroupN(ownerGroupN).OwnerGroupId(ownerGroupId).OwnerGroupIdN(ownerGroupIdN).OwnerId(ownerId).OwnerIdN(ownerIdN).Parent(parent).ParentN(parentN).ParentId(parentId).ParentIdN(parentIdN).Q(q).Slug(slug).SlugEmpty(slugEmpty).SlugIc(slugIc).SlugIe(slugIe).SlugIew(slugIew).SlugIregex(slugIregex).SlugIsw(slugIsw).SlugN(slugN).SlugNic(slugNic).SlugNie(slugNie).SlugNiew(slugNiew).SlugNisw(slugNisw).SlugRegex(slugRegex).Tag(tag).TagN(tagN).TagId(tagId).TagIdN(tagIdN).UpdatedByRequest(updatedByRequest).Execute()





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
	ancestor := []string{"Inner_example"} // []string |  (optional)
	ancestorN := []string{"Inner_example"} // []string |  (optional)
	ancestorId := []string{"Inner_example"} // []string |  (optional)
	ancestorIdN := []string{"Inner_example"} // []string |  (optional)
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
	ownerGroup := []string{"Inner_example"} // []string | Owner Group (name) (optional)
	ownerGroupN := []string{"Inner_example"} // []string | Owner Group (name) (optional)
	ownerGroupId := []int32{int32(123)} // []int32 | Owner Group (ID) (optional)
	ownerGroupIdN := []int32{int32(123)} // []int32 | Owner Group (ID) (optional)
	ownerId := []*int32{int32(123)} // []*int32 | Owner (ID) (optional)
	ownerIdN := []*int32{int32(123)} // []*int32 | Owner (ID) (optional)
	parent := []string{"Inner_example"} // []string | Parent site group (slug) (optional)
	parentN := []string{"Inner_example"} // []string | Parent site group (slug) (optional)
	parentId := []*int32{int32(123)} // []*int32 | Parent site group (ID) (optional)
	parentIdN := []*int32{int32(123)} // []*int32 | Parent site group (ID) (optional)
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
	resp, r, err := apiClient.DcimAPI.DcimSiteGroupsList(context.Background()).Ancestor(ancestor).AncestorN(ancestorN).AncestorId(ancestorId).AncestorIdN(ancestorIdN).Contact(contact).ContactN(contactN).ContactGroup(contactGroup).ContactGroupN(contactGroupN).ContactRole(contactRole).ContactRoleN(contactRoleN).Created(created).CreatedEmpty(createdEmpty).CreatedGt(createdGt).CreatedGte(createdGte).CreatedLt(createdLt).CreatedLte(createdLte).CreatedN(createdN).CreatedByRequest(createdByRequest).Description(description).DescriptionEmpty(descriptionEmpty).DescriptionIc(descriptionIc).DescriptionIe(descriptionIe).DescriptionIew(descriptionIew).DescriptionIregex(descriptionIregex).DescriptionIsw(descriptionIsw).DescriptionN(descriptionN).DescriptionNic(descriptionNic).DescriptionNie(descriptionNie).DescriptionNiew(descriptionNiew).DescriptionNisw(descriptionNisw).DescriptionRegex(descriptionRegex).Id(id).IdEmpty(idEmpty).IdGt(idGt).IdGte(idGte).IdLt(idLt).IdLte(idLte).IdN(idN).LastUpdated(lastUpdated).LastUpdatedEmpty(lastUpdatedEmpty).LastUpdatedGt(lastUpdatedGt).LastUpdatedGte(lastUpdatedGte).LastUpdatedLt(lastUpdatedLt).LastUpdatedLte(lastUpdatedLte).LastUpdatedN(lastUpdatedN).Limit(limit).ModifiedByRequest(modifiedByRequest).Name(name).NameEmpty(nameEmpty).NameIc(nameIc).NameIe(nameIe).NameIew(nameIew).NameIregex(nameIregex).NameIsw(nameIsw).NameN(nameN).NameNic(nameNic).NameNie(nameNie).NameNiew(nameNiew).NameNisw(nameNisw).NameRegex(nameRegex).Offset(offset).Ordering(ordering).Owner(owner).OwnerN(ownerN).OwnerGroup(ownerGroup).OwnerGroupN(ownerGroupN).OwnerGroupId(ownerGroupId).OwnerGroupIdN(ownerGroupIdN).OwnerId(ownerId).OwnerIdN(ownerIdN).Parent(parent).ParentN(parentN).ParentId(parentId).ParentIdN(parentIdN).Q(q).Slug(slug).SlugEmpty(slugEmpty).SlugIc(slugIc).SlugIe(slugIe).SlugIew(slugIew).SlugIregex(slugIregex).SlugIsw(slugIsw).SlugN(slugN).SlugNic(slugNic).SlugNie(slugNie).SlugNiew(slugNiew).SlugNisw(slugNisw).SlugRegex(slugRegex).Tag(tag).TagN(tagN).TagId(tagId).TagIdN(tagIdN).UpdatedByRequest(updatedByRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimSiteGroupsList``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DcimSiteGroupsList`: PaginatedSiteGroupList
	fmt.Fprintf(os.Stdout, "Response from `DcimAPI.DcimSiteGroupsList`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDcimSiteGroupsListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ancestor** | **[]string** |  | 
 **ancestorN** | **[]string** |  | 
 **ancestorId** | **[]string** |  | 
 **ancestorIdN** | **[]string** |  | 
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
 **ownerGroup** | **[]string** | Owner Group (name) | 
 **ownerGroupN** | **[]string** | Owner Group (name) | 
 **ownerGroupId** | **[]int32** | Owner Group (ID) | 
 **ownerGroupIdN** | **[]int32** | Owner Group (ID) | 
 **ownerId** | **[]int32** | Owner (ID) | 
 **ownerIdN** | **[]int32** | Owner (ID) | 
 **parent** | **[]string** | Parent site group (slug) | 
 **parentN** | **[]string** | Parent site group (slug) | 
 **parentId** | **[]int32** | Parent site group (ID) | 
 **parentIdN** | **[]int32** | Parent site group (ID) | 
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

[**PaginatedSiteGroupList**](PaginatedSiteGroupList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DcimSiteGroupsPartialUpdate

> SiteGroup DcimSiteGroupsPartialUpdate(ctx, id).PatchedWritableSiteGroupRequest(patchedWritableSiteGroupRequest).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this site group.
	patchedWritableSiteGroupRequest := *openapiclient.NewPatchedWritableSiteGroupRequest() // PatchedWritableSiteGroupRequest |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DcimAPI.DcimSiteGroupsPartialUpdate(context.Background(), id).PatchedWritableSiteGroupRequest(patchedWritableSiteGroupRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimSiteGroupsPartialUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DcimSiteGroupsPartialUpdate`: SiteGroup
	fmt.Fprintf(os.Stdout, "Response from `DcimAPI.DcimSiteGroupsPartialUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this site group. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDcimSiteGroupsPartialUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **patchedWritableSiteGroupRequest** | [**PatchedWritableSiteGroupRequest**](PatchedWritableSiteGroupRequest.md) |  | 

### Return type

[**SiteGroup**](SiteGroup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DcimSiteGroupsRetrieve

> SiteGroup DcimSiteGroupsRetrieve(ctx, id).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this site group.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DcimAPI.DcimSiteGroupsRetrieve(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimSiteGroupsRetrieve``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DcimSiteGroupsRetrieve`: SiteGroup
	fmt.Fprintf(os.Stdout, "Response from `DcimAPI.DcimSiteGroupsRetrieve`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this site group. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDcimSiteGroupsRetrieveRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**SiteGroup**](SiteGroup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DcimSiteGroupsUpdate

> SiteGroup DcimSiteGroupsUpdate(ctx, id).WritableSiteGroupRequest(writableSiteGroupRequest).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this site group.
	writableSiteGroupRequest := *openapiclient.NewWritableSiteGroupRequest("Name_example", "Slug_example") // WritableSiteGroupRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DcimAPI.DcimSiteGroupsUpdate(context.Background(), id).WritableSiteGroupRequest(writableSiteGroupRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimSiteGroupsUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DcimSiteGroupsUpdate`: SiteGroup
	fmt.Fprintf(os.Stdout, "Response from `DcimAPI.DcimSiteGroupsUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this site group. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDcimSiteGroupsUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **writableSiteGroupRequest** | [**WritableSiteGroupRequest**](WritableSiteGroupRequest.md) |  | 

### Return type

[**SiteGroup**](SiteGroup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DcimSitesBulkDestroy

> DcimSitesBulkDestroy(ctx).SiteRequest(siteRequest).Execute()





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
	siteRequest := []openapiclient.SiteRequest{*openapiclient.NewSiteRequest("Name_example", "Slug_example")} // []SiteRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DcimAPI.DcimSitesBulkDestroy(context.Background()).SiteRequest(siteRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimSitesBulkDestroy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDcimSitesBulkDestroyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **siteRequest** | [**[]SiteRequest**](SiteRequest.md) |  | 

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


## DcimSitesBulkPartialUpdate

> []Site DcimSitesBulkPartialUpdate(ctx).SiteRequest(siteRequest).Execute()





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
	siteRequest := []openapiclient.SiteRequest{*openapiclient.NewSiteRequest("Name_example", "Slug_example")} // []SiteRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DcimAPI.DcimSitesBulkPartialUpdate(context.Background()).SiteRequest(siteRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimSitesBulkPartialUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DcimSitesBulkPartialUpdate`: []Site
	fmt.Fprintf(os.Stdout, "Response from `DcimAPI.DcimSitesBulkPartialUpdate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDcimSitesBulkPartialUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **siteRequest** | [**[]SiteRequest**](SiteRequest.md) |  | 

### Return type

[**[]Site**](Site.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DcimSitesBulkUpdate

> []Site DcimSitesBulkUpdate(ctx).SiteRequest(siteRequest).Execute()





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
	siteRequest := []openapiclient.SiteRequest{*openapiclient.NewSiteRequest("Name_example", "Slug_example")} // []SiteRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DcimAPI.DcimSitesBulkUpdate(context.Background()).SiteRequest(siteRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimSitesBulkUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DcimSitesBulkUpdate`: []Site
	fmt.Fprintf(os.Stdout, "Response from `DcimAPI.DcimSitesBulkUpdate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDcimSitesBulkUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **siteRequest** | [**[]SiteRequest**](SiteRequest.md) |  | 

### Return type

[**[]Site**](Site.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DcimSitesCreate

> Site DcimSitesCreate(ctx).DcimSitesCreateRequest(dcimSitesCreateRequest).Execute()





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
	dcimSitesCreateRequest := openapiclient.dcim_sites_create_request{WritableSiteRequest: openapiclient.NewWritableSiteRequest("Name_example", "Slug_example")} // DcimSitesCreateRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DcimAPI.DcimSitesCreate(context.Background()).DcimSitesCreateRequest(dcimSitesCreateRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimSitesCreate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DcimSitesCreate`: Site
	fmt.Fprintf(os.Stdout, "Response from `DcimAPI.DcimSitesCreate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDcimSitesCreateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dcimSitesCreateRequest** | [**DcimSitesCreateRequest**](DcimSitesCreateRequest.md) |  | 

### Return type

[**Site**](Site.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DcimSitesDestroy

> DcimSitesDestroy(ctx, id).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this site.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DcimAPI.DcimSitesDestroy(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimSitesDestroy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this site. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDcimSitesDestroyRequest struct via the builder pattern


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


## DcimSitesList

> PaginatedSiteList DcimSitesList(ctx).Asn(asn).AsnN(asnN).AsnId(asnId).AsnIdN(asnIdN).Contact(contact).ContactN(contactN).ContactGroup(contactGroup).ContactGroupN(contactGroupN).ContactRole(contactRole).ContactRoleN(contactRoleN).Created(created).CreatedEmpty(createdEmpty).CreatedGt(createdGt).CreatedGte(createdGte).CreatedLt(createdLt).CreatedLte(createdLte).CreatedN(createdN).CreatedByRequest(createdByRequest).Description(description).DescriptionEmpty(descriptionEmpty).DescriptionIc(descriptionIc).DescriptionIe(descriptionIe).DescriptionIew(descriptionIew).DescriptionIregex(descriptionIregex).DescriptionIsw(descriptionIsw).DescriptionN(descriptionN).DescriptionNic(descriptionNic).DescriptionNie(descriptionNie).DescriptionNiew(descriptionNiew).DescriptionNisw(descriptionNisw).DescriptionRegex(descriptionRegex).Facility(facility).FacilityEmpty(facilityEmpty).FacilityIc(facilityIc).FacilityIe(facilityIe).FacilityIew(facilityIew).FacilityIregex(facilityIregex).FacilityIsw(facilityIsw).FacilityN(facilityN).FacilityNic(facilityNic).FacilityNie(facilityNie).FacilityNiew(facilityNiew).FacilityNisw(facilityNisw).FacilityRegex(facilityRegex).Group(group).GroupN(groupN).GroupId(groupId).GroupIdN(groupIdN).Id(id).IdEmpty(idEmpty).IdGt(idGt).IdGte(idGte).IdLt(idLt).IdLte(idLte).IdN(idN).LastUpdated(lastUpdated).LastUpdatedEmpty(lastUpdatedEmpty).LastUpdatedGt(lastUpdatedGt).LastUpdatedGte(lastUpdatedGte).LastUpdatedLt(lastUpdatedLt).LastUpdatedLte(lastUpdatedLte).LastUpdatedN(lastUpdatedN).Latitude(latitude).LatitudeEmpty(latitudeEmpty).LatitudeGt(latitudeGt).LatitudeGte(latitudeGte).LatitudeLt(latitudeLt).LatitudeLte(latitudeLte).LatitudeN(latitudeN).Limit(limit).Longitude(longitude).LongitudeEmpty(longitudeEmpty).LongitudeGt(longitudeGt).LongitudeGte(longitudeGte).LongitudeLt(longitudeLt).LongitudeLte(longitudeLte).LongitudeN(longitudeN).ModifiedByRequest(modifiedByRequest).Name(name).NameEmpty(nameEmpty).NameIc(nameIc).NameIe(nameIe).NameIew(nameIew).NameIregex(nameIregex).NameIsw(nameIsw).NameN(nameN).NameNic(nameNic).NameNie(nameNie).NameNiew(nameNiew).NameNisw(nameNisw).NameRegex(nameRegex).Offset(offset).Ordering(ordering).Owner(owner).OwnerN(ownerN).OwnerGroup(ownerGroup).OwnerGroupN(ownerGroupN).OwnerGroupId(ownerGroupId).OwnerGroupIdN(ownerGroupIdN).OwnerId(ownerId).OwnerIdN(ownerIdN).Q(q).Region(region).RegionN(regionN).RegionId(regionId).RegionIdN(regionIdN).Slug(slug).SlugEmpty(slugEmpty).SlugIc(slugIc).SlugIe(slugIe).SlugIew(slugIew).SlugIregex(slugIregex).SlugIsw(slugIsw).SlugN(slugN).SlugNic(slugNic).SlugNie(slugNie).SlugNiew(slugNiew).SlugNisw(slugNisw).SlugRegex(slugRegex).Status(status).StatusEmpty(statusEmpty).StatusIc(statusIc).StatusIe(statusIe).StatusIew(statusIew).StatusIregex(statusIregex).StatusIsw(statusIsw).StatusN(statusN).StatusNic(statusNic).StatusNie(statusNie).StatusNiew(statusNiew).StatusNisw(statusNisw).StatusRegex(statusRegex).Tag(tag).TagN(tagN).TagId(tagId).TagIdN(tagIdN).Tenant(tenant).TenantN(tenantN).TenantGroup(tenantGroup).TenantGroupN(tenantGroupN).TenantGroupId(tenantGroupId).TenantGroupIdN(tenantGroupIdN).TenantId(tenantId).TenantIdN(tenantIdN).TimeZone(timeZone).TimeZoneIc(timeZoneIc).TimeZoneIe(timeZoneIe).TimeZoneIew(timeZoneIew).TimeZoneIregex(timeZoneIregex).TimeZoneIsw(timeZoneIsw).TimeZoneN(timeZoneN).TimeZoneNic(timeZoneNic).TimeZoneNie(timeZoneNie).TimeZoneNiew(timeZoneNiew).TimeZoneNisw(timeZoneNisw).TimeZoneRegex(timeZoneRegex).UpdatedByRequest(updatedByRequest).Execute()





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
	asn := []string{"Inner_example"} // []string | AS (ID) (optional)
	asnN := []string{"Inner_example"} // []string | AS (ID) (optional)
	asnId := []int32{int32(123)} // []int32 | AS (ID) (optional)
	asnIdN := []int32{int32(123)} // []int32 | AS (ID) (optional)
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
	facility := []string{"Inner_example"} // []string |  (optional)
	facilityEmpty := true // bool |  (optional)
	facilityIc := []string{"Inner_example"} // []string |  (optional)
	facilityIe := []string{"Inner_example"} // []string |  (optional)
	facilityIew := []string{"Inner_example"} // []string |  (optional)
	facilityIregex := []string{"Inner_example"} // []string |  (optional)
	facilityIsw := []string{"Inner_example"} // []string |  (optional)
	facilityN := []string{"Inner_example"} // []string |  (optional)
	facilityNic := []string{"Inner_example"} // []string |  (optional)
	facilityNie := []string{"Inner_example"} // []string |  (optional)
	facilityNiew := []string{"Inner_example"} // []string |  (optional)
	facilityNisw := []string{"Inner_example"} // []string |  (optional)
	facilityRegex := []string{"Inner_example"} // []string |  (optional)
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
	latitude := []float64{float64(123)} // []float64 |  (optional)
	latitudeEmpty := true // bool |  (optional)
	latitudeGt := []float64{float64(123)} // []float64 |  (optional)
	latitudeGte := []float64{float64(123)} // []float64 |  (optional)
	latitudeLt := []float64{float64(123)} // []float64 |  (optional)
	latitudeLte := []float64{float64(123)} // []float64 |  (optional)
	latitudeN := []float64{float64(123)} // []float64 |  (optional)
	limit := int32(56) // int32 | Number of results to return per page. (optional)
	longitude := []float64{float64(123)} // []float64 |  (optional)
	longitudeEmpty := true // bool |  (optional)
	longitudeGt := []float64{float64(123)} // []float64 |  (optional)
	longitudeGte := []float64{float64(123)} // []float64 |  (optional)
	longitudeLt := []float64{float64(123)} // []float64 |  (optional)
	longitudeLte := []float64{float64(123)} // []float64 |  (optional)
	longitudeN := []float64{float64(123)} // []float64 |  (optional)
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
	ownerGroup := []string{"Inner_example"} // []string | Owner Group (name) (optional)
	ownerGroupN := []string{"Inner_example"} // []string | Owner Group (name) (optional)
	ownerGroupId := []int32{int32(123)} // []int32 | Owner Group (ID) (optional)
	ownerGroupIdN := []int32{int32(123)} // []int32 | Owner Group (ID) (optional)
	ownerId := []*int32{int32(123)} // []*int32 | Owner (ID) (optional)
	ownerIdN := []*int32{int32(123)} // []*int32 | Owner (ID) (optional)
	q := "q_example" // string | Search (optional)
	region := []string{"Inner_example"} // []string |  (optional)
	regionN := []string{"Inner_example"} // []string |  (optional)
	regionId := []string{"Inner_example"} // []string |  (optional)
	regionIdN := []string{"Inner_example"} // []string |  (optional)
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
	status := []string{"Inner_example"} // []string |  (optional)
	statusEmpty := true // bool |  (optional)
	statusIc := []string{"Inner_example"} // []string |  (optional)
	statusIe := []string{"Inner_example"} // []string |  (optional)
	statusIew := []string{"Inner_example"} // []string |  (optional)
	statusIregex := []string{"Inner_example"} // []string |  (optional)
	statusIsw := []string{"Inner_example"} // []string |  (optional)
	statusN := []string{"Inner_example"} // []string |  (optional)
	statusNic := []string{"Inner_example"} // []string |  (optional)
	statusNie := []string{"Inner_example"} // []string |  (optional)
	statusNiew := []string{"Inner_example"} // []string |  (optional)
	statusNisw := []string{"Inner_example"} // []string |  (optional)
	statusRegex := []string{"Inner_example"} // []string |  (optional)
	tag := []string{"Inner_example"} // []string |  (optional)
	tagN := []string{"Inner_example"} // []string |  (optional)
	tagId := []string{"Inner_example"} // []string |  (optional)
	tagIdN := []string{"Inner_example"} // []string |  (optional)
	tenant := []string{"Inner_example"} // []string | Tenant (slug) (optional)
	tenantN := []string{"Inner_example"} // []string | Tenant (slug) (optional)
	tenantGroup := []string{"Inner_example"} // []string |  (optional)
	tenantGroupN := []string{"Inner_example"} // []string |  (optional)
	tenantGroupId := []string{"Inner_example"} // []string |  (optional)
	tenantGroupIdN := []string{"Inner_example"} // []string |  (optional)
	tenantId := []*int32{int32(123)} // []*int32 | Tenant (ID) (optional)
	tenantIdN := []*int32{int32(123)} // []*int32 | Tenant (ID) (optional)
	timeZone := []string{"Inner_example"} // []string |  (optional)
	timeZoneIc := []string{"Inner_example"} // []string |  (optional)
	timeZoneIe := []string{"Inner_example"} // []string |  (optional)
	timeZoneIew := []string{"Inner_example"} // []string |  (optional)
	timeZoneIregex := []string{"Inner_example"} // []string |  (optional)
	timeZoneIsw := []string{"Inner_example"} // []string |  (optional)
	timeZoneN := []string{"Inner_example"} // []string |  (optional)
	timeZoneNic := []string{"Inner_example"} // []string |  (optional)
	timeZoneNie := []string{"Inner_example"} // []string |  (optional)
	timeZoneNiew := []string{"Inner_example"} // []string |  (optional)
	timeZoneNisw := []string{"Inner_example"} // []string |  (optional)
	timeZoneRegex := []string{"Inner_example"} // []string |  (optional)
	updatedByRequest := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DcimAPI.DcimSitesList(context.Background()).Asn(asn).AsnN(asnN).AsnId(asnId).AsnIdN(asnIdN).Contact(contact).ContactN(contactN).ContactGroup(contactGroup).ContactGroupN(contactGroupN).ContactRole(contactRole).ContactRoleN(contactRoleN).Created(created).CreatedEmpty(createdEmpty).CreatedGt(createdGt).CreatedGte(createdGte).CreatedLt(createdLt).CreatedLte(createdLte).CreatedN(createdN).CreatedByRequest(createdByRequest).Description(description).DescriptionEmpty(descriptionEmpty).DescriptionIc(descriptionIc).DescriptionIe(descriptionIe).DescriptionIew(descriptionIew).DescriptionIregex(descriptionIregex).DescriptionIsw(descriptionIsw).DescriptionN(descriptionN).DescriptionNic(descriptionNic).DescriptionNie(descriptionNie).DescriptionNiew(descriptionNiew).DescriptionNisw(descriptionNisw).DescriptionRegex(descriptionRegex).Facility(facility).FacilityEmpty(facilityEmpty).FacilityIc(facilityIc).FacilityIe(facilityIe).FacilityIew(facilityIew).FacilityIregex(facilityIregex).FacilityIsw(facilityIsw).FacilityN(facilityN).FacilityNic(facilityNic).FacilityNie(facilityNie).FacilityNiew(facilityNiew).FacilityNisw(facilityNisw).FacilityRegex(facilityRegex).Group(group).GroupN(groupN).GroupId(groupId).GroupIdN(groupIdN).Id(id).IdEmpty(idEmpty).IdGt(idGt).IdGte(idGte).IdLt(idLt).IdLte(idLte).IdN(idN).LastUpdated(lastUpdated).LastUpdatedEmpty(lastUpdatedEmpty).LastUpdatedGt(lastUpdatedGt).LastUpdatedGte(lastUpdatedGte).LastUpdatedLt(lastUpdatedLt).LastUpdatedLte(lastUpdatedLte).LastUpdatedN(lastUpdatedN).Latitude(latitude).LatitudeEmpty(latitudeEmpty).LatitudeGt(latitudeGt).LatitudeGte(latitudeGte).LatitudeLt(latitudeLt).LatitudeLte(latitudeLte).LatitudeN(latitudeN).Limit(limit).Longitude(longitude).LongitudeEmpty(longitudeEmpty).LongitudeGt(longitudeGt).LongitudeGte(longitudeGte).LongitudeLt(longitudeLt).LongitudeLte(longitudeLte).LongitudeN(longitudeN).ModifiedByRequest(modifiedByRequest).Name(name).NameEmpty(nameEmpty).NameIc(nameIc).NameIe(nameIe).NameIew(nameIew).NameIregex(nameIregex).NameIsw(nameIsw).NameN(nameN).NameNic(nameNic).NameNie(nameNie).NameNiew(nameNiew).NameNisw(nameNisw).NameRegex(nameRegex).Offset(offset).Ordering(ordering).Owner(owner).OwnerN(ownerN).OwnerGroup(ownerGroup).OwnerGroupN(ownerGroupN).OwnerGroupId(ownerGroupId).OwnerGroupIdN(ownerGroupIdN).OwnerId(ownerId).OwnerIdN(ownerIdN).Q(q).Region(region).RegionN(regionN).RegionId(regionId).RegionIdN(regionIdN).Slug(slug).SlugEmpty(slugEmpty).SlugIc(slugIc).SlugIe(slugIe).SlugIew(slugIew).SlugIregex(slugIregex).SlugIsw(slugIsw).SlugN(slugN).SlugNic(slugNic).SlugNie(slugNie).SlugNiew(slugNiew).SlugNisw(slugNisw).SlugRegex(slugRegex).Status(status).StatusEmpty(statusEmpty).StatusIc(statusIc).StatusIe(statusIe).StatusIew(statusIew).StatusIregex(statusIregex).StatusIsw(statusIsw).StatusN(statusN).StatusNic(statusNic).StatusNie(statusNie).StatusNiew(statusNiew).StatusNisw(statusNisw).StatusRegex(statusRegex).Tag(tag).TagN(tagN).TagId(tagId).TagIdN(tagIdN).Tenant(tenant).TenantN(tenantN).TenantGroup(tenantGroup).TenantGroupN(tenantGroupN).TenantGroupId(tenantGroupId).TenantGroupIdN(tenantGroupIdN).TenantId(tenantId).TenantIdN(tenantIdN).TimeZone(timeZone).TimeZoneIc(timeZoneIc).TimeZoneIe(timeZoneIe).TimeZoneIew(timeZoneIew).TimeZoneIregex(timeZoneIregex).TimeZoneIsw(timeZoneIsw).TimeZoneN(timeZoneN).TimeZoneNic(timeZoneNic).TimeZoneNie(timeZoneNie).TimeZoneNiew(timeZoneNiew).TimeZoneNisw(timeZoneNisw).TimeZoneRegex(timeZoneRegex).UpdatedByRequest(updatedByRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimSitesList``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DcimSitesList`: PaginatedSiteList
	fmt.Fprintf(os.Stdout, "Response from `DcimAPI.DcimSitesList`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDcimSitesListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asn** | **[]string** | AS (ID) | 
 **asnN** | **[]string** | AS (ID) | 
 **asnId** | **[]int32** | AS (ID) | 
 **asnIdN** | **[]int32** | AS (ID) | 
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
 **facility** | **[]string** |  | 
 **facilityEmpty** | **bool** |  | 
 **facilityIc** | **[]string** |  | 
 **facilityIe** | **[]string** |  | 
 **facilityIew** | **[]string** |  | 
 **facilityIregex** | **[]string** |  | 
 **facilityIsw** | **[]string** |  | 
 **facilityN** | **[]string** |  | 
 **facilityNic** | **[]string** |  | 
 **facilityNie** | **[]string** |  | 
 **facilityNiew** | **[]string** |  | 
 **facilityNisw** | **[]string** |  | 
 **facilityRegex** | **[]string** |  | 
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
 **latitude** | **[]float64** |  | 
 **latitudeEmpty** | **bool** |  | 
 **latitudeGt** | **[]float64** |  | 
 **latitudeGte** | **[]float64** |  | 
 **latitudeLt** | **[]float64** |  | 
 **latitudeLte** | **[]float64** |  | 
 **latitudeN** | **[]float64** |  | 
 **limit** | **int32** | Number of results to return per page. | 
 **longitude** | **[]float64** |  | 
 **longitudeEmpty** | **bool** |  | 
 **longitudeGt** | **[]float64** |  | 
 **longitudeGte** | **[]float64** |  | 
 **longitudeLt** | **[]float64** |  | 
 **longitudeLte** | **[]float64** |  | 
 **longitudeN** | **[]float64** |  | 
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
 **ownerGroup** | **[]string** | Owner Group (name) | 
 **ownerGroupN** | **[]string** | Owner Group (name) | 
 **ownerGroupId** | **[]int32** | Owner Group (ID) | 
 **ownerGroupIdN** | **[]int32** | Owner Group (ID) | 
 **ownerId** | **[]int32** | Owner (ID) | 
 **ownerIdN** | **[]int32** | Owner (ID) | 
 **q** | **string** | Search | 
 **region** | **[]string** |  | 
 **regionN** | **[]string** |  | 
 **regionId** | **[]string** |  | 
 **regionIdN** | **[]string** |  | 
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
 **status** | **[]string** |  | 
 **statusEmpty** | **bool** |  | 
 **statusIc** | **[]string** |  | 
 **statusIe** | **[]string** |  | 
 **statusIew** | **[]string** |  | 
 **statusIregex** | **[]string** |  | 
 **statusIsw** | **[]string** |  | 
 **statusN** | **[]string** |  | 
 **statusNic** | **[]string** |  | 
 **statusNie** | **[]string** |  | 
 **statusNiew** | **[]string** |  | 
 **statusNisw** | **[]string** |  | 
 **statusRegex** | **[]string** |  | 
 **tag** | **[]string** |  | 
 **tagN** | **[]string** |  | 
 **tagId** | **[]string** |  | 
 **tagIdN** | **[]string** |  | 
 **tenant** | **[]string** | Tenant (slug) | 
 **tenantN** | **[]string** | Tenant (slug) | 
 **tenantGroup** | **[]string** |  | 
 **tenantGroupN** | **[]string** |  | 
 **tenantGroupId** | **[]string** |  | 
 **tenantGroupIdN** | **[]string** |  | 
 **tenantId** | **[]int32** | Tenant (ID) | 
 **tenantIdN** | **[]int32** | Tenant (ID) | 
 **timeZone** | **[]string** |  | 
 **timeZoneIc** | **[]string** |  | 
 **timeZoneIe** | **[]string** |  | 
 **timeZoneIew** | **[]string** |  | 
 **timeZoneIregex** | **[]string** |  | 
 **timeZoneIsw** | **[]string** |  | 
 **timeZoneN** | **[]string** |  | 
 **timeZoneNic** | **[]string** |  | 
 **timeZoneNie** | **[]string** |  | 
 **timeZoneNiew** | **[]string** |  | 
 **timeZoneNisw** | **[]string** |  | 
 **timeZoneRegex** | **[]string** |  | 
 **updatedByRequest** | **string** |  | 

### Return type

[**PaginatedSiteList**](PaginatedSiteList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DcimSitesPartialUpdate

> Site DcimSitesPartialUpdate(ctx, id).PatchedWritableSiteRequest(patchedWritableSiteRequest).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this site.
	patchedWritableSiteRequest := *openapiclient.NewPatchedWritableSiteRequest() // PatchedWritableSiteRequest |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DcimAPI.DcimSitesPartialUpdate(context.Background(), id).PatchedWritableSiteRequest(patchedWritableSiteRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimSitesPartialUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DcimSitesPartialUpdate`: Site
	fmt.Fprintf(os.Stdout, "Response from `DcimAPI.DcimSitesPartialUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this site. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDcimSitesPartialUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **patchedWritableSiteRequest** | [**PatchedWritableSiteRequest**](PatchedWritableSiteRequest.md) |  | 

### Return type

[**Site**](Site.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DcimSitesRetrieve

> Site DcimSitesRetrieve(ctx, id).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this site.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DcimAPI.DcimSitesRetrieve(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimSitesRetrieve``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DcimSitesRetrieve`: Site
	fmt.Fprintf(os.Stdout, "Response from `DcimAPI.DcimSitesRetrieve`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this site. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDcimSitesRetrieveRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**Site**](Site.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DcimSitesUpdate

> Site DcimSitesUpdate(ctx, id).WritableSiteRequest(writableSiteRequest).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this site.
	writableSiteRequest := *openapiclient.NewWritableSiteRequest("Name_example", "Slug_example") // WritableSiteRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DcimAPI.DcimSitesUpdate(context.Background(), id).WritableSiteRequest(writableSiteRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DcimAPI.DcimSitesUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DcimSitesUpdate`: Site
	fmt.Fprintf(os.Stdout, "Response from `DcimAPI.DcimSitesUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this site. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDcimSitesUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **writableSiteRequest** | [**WritableSiteRequest**](WritableSiteRequest.md) |  | 

### Return type

[**Site**](Site.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

