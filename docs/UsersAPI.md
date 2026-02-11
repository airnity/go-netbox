# \UsersAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**UsersGroupsBulkDestroy**](UsersAPI.md#UsersGroupsBulkDestroy) | **Delete** /api/users/groups/ | 
[**UsersGroupsBulkPartialUpdate**](UsersAPI.md#UsersGroupsBulkPartialUpdate) | **Patch** /api/users/groups/ | 
[**UsersGroupsBulkUpdate**](UsersAPI.md#UsersGroupsBulkUpdate) | **Put** /api/users/groups/ | 
[**UsersGroupsCreate**](UsersAPI.md#UsersGroupsCreate) | **Post** /api/users/groups/ | 
[**UsersGroupsDestroy**](UsersAPI.md#UsersGroupsDestroy) | **Delete** /api/users/groups/{id}/ | 
[**UsersGroupsList**](UsersAPI.md#UsersGroupsList) | **Get** /api/users/groups/ | 
[**UsersGroupsPartialUpdate**](UsersAPI.md#UsersGroupsPartialUpdate) | **Patch** /api/users/groups/{id}/ | 
[**UsersGroupsRetrieve**](UsersAPI.md#UsersGroupsRetrieve) | **Get** /api/users/groups/{id}/ | 
[**UsersGroupsUpdate**](UsersAPI.md#UsersGroupsUpdate) | **Put** /api/users/groups/{id}/ | 
[**UsersPermissionsBulkPartialUpdate**](UsersAPI.md#UsersPermissionsBulkPartialUpdate) | **Patch** /api/users/permissions/ | 
[**UsersPermissionsBulkUpdate**](UsersAPI.md#UsersPermissionsBulkUpdate) | **Put** /api/users/permissions/ | 
[**UsersPermissionsCreate**](UsersAPI.md#UsersPermissionsCreate) | **Post** /api/users/permissions/ | 
[**UsersPermissionsPartialUpdate**](UsersAPI.md#UsersPermissionsPartialUpdate) | **Patch** /api/users/permissions/{id}/ | 
[**UsersPermissionsRetrieve**](UsersAPI.md#UsersPermissionsRetrieve) | **Get** /api/users/permissions/{id}/ | 
[**UsersPermissionsUpdate**](UsersAPI.md#UsersPermissionsUpdate) | **Put** /api/users/permissions/{id}/ | 



## UsersGroupsBulkDestroy

> UsersGroupsBulkDestroy(ctx).GroupRequest(groupRequest).Execute()





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
	groupRequest := []openapiclient.GroupRequest{*openapiclient.NewGroupRequest("Name_example")} // []GroupRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.UsersAPI.UsersGroupsBulkDestroy(context.Background()).GroupRequest(groupRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersAPI.UsersGroupsBulkDestroy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUsersGroupsBulkDestroyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupRequest** | [**[]GroupRequest**](GroupRequest.md) |  | 

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


## UsersGroupsBulkPartialUpdate

> []Group UsersGroupsBulkPartialUpdate(ctx).GroupRequest(groupRequest).Execute()





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
	groupRequest := []openapiclient.GroupRequest{*openapiclient.NewGroupRequest("Name_example")} // []GroupRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UsersAPI.UsersGroupsBulkPartialUpdate(context.Background()).GroupRequest(groupRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersAPI.UsersGroupsBulkPartialUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UsersGroupsBulkPartialUpdate`: []Group
	fmt.Fprintf(os.Stdout, "Response from `UsersAPI.UsersGroupsBulkPartialUpdate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUsersGroupsBulkPartialUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupRequest** | [**[]GroupRequest**](GroupRequest.md) |  | 

### Return type

[**[]Group**](Group.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UsersGroupsBulkUpdate

> []Group UsersGroupsBulkUpdate(ctx).GroupRequest(groupRequest).Execute()





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
	groupRequest := []openapiclient.GroupRequest{*openapiclient.NewGroupRequest("Name_example")} // []GroupRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UsersAPI.UsersGroupsBulkUpdate(context.Background()).GroupRequest(groupRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersAPI.UsersGroupsBulkUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UsersGroupsBulkUpdate`: []Group
	fmt.Fprintf(os.Stdout, "Response from `UsersAPI.UsersGroupsBulkUpdate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUsersGroupsBulkUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupRequest** | [**[]GroupRequest**](GroupRequest.md) |  | 

### Return type

[**[]Group**](Group.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UsersGroupsCreate

> Group UsersGroupsCreate(ctx).UsersGroupsCreateRequest(usersGroupsCreateRequest).Execute()





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
	usersGroupsCreateRequest := openapiclient.users_groups_create_request{GroupRequest: openapiclient.NewGroupRequest("Name_example")} // UsersGroupsCreateRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UsersAPI.UsersGroupsCreate(context.Background()).UsersGroupsCreateRequest(usersGroupsCreateRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersAPI.UsersGroupsCreate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UsersGroupsCreate`: Group
	fmt.Fprintf(os.Stdout, "Response from `UsersAPI.UsersGroupsCreate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUsersGroupsCreateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usersGroupsCreateRequest** | [**UsersGroupsCreateRequest**](UsersGroupsCreateRequest.md) |  | 

### Return type

[**Group**](Group.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UsersGroupsDestroy

> UsersGroupsDestroy(ctx, id).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this group.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.UsersAPI.UsersGroupsDestroy(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersAPI.UsersGroupsDestroy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this group. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUsersGroupsDestroyRequest struct via the builder pattern


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


## UsersGroupsList

> PaginatedGroupList UsersGroupsList(ctx).Description(description).DescriptionEmpty(descriptionEmpty).DescriptionIc(descriptionIc).DescriptionIe(descriptionIe).DescriptionIew(descriptionIew).DescriptionIregex(descriptionIregex).DescriptionIsw(descriptionIsw).DescriptionN(descriptionN).DescriptionNic(descriptionNic).DescriptionNie(descriptionNie).DescriptionNiew(descriptionNiew).DescriptionNisw(descriptionNisw).DescriptionRegex(descriptionRegex).Id(id).IdEmpty(idEmpty).IdGt(idGt).IdGte(idGte).IdLt(idLt).IdLte(idLte).IdN(idN).Limit(limit).Name(name).NameEmpty(nameEmpty).NameIc(nameIc).NameIe(nameIe).NameIew(nameIew).NameIregex(nameIregex).NameIsw(nameIsw).NameN(nameN).NameNic(nameNic).NameNie(nameNie).NameNiew(nameNiew).NameNisw(nameNisw).NameRegex(nameRegex).NotificationGroupId(notificationGroupId).NotificationGroupIdN(notificationGroupIdN).Offset(offset).Ordering(ordering).Owner(owner).OwnerN(ownerN).OwnerId(ownerId).OwnerIdN(ownerIdN).PermissionId(permissionId).PermissionIdN(permissionIdN).Q(q).UserId(userId).UserIdN(userIdN).Execute()





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
	limit := int32(56) // int32 | Number of results to return per page. (optional)
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
	notificationGroupId := []int32{int32(123)} // []int32 | Notification group (ID) (optional)
	notificationGroupIdN := []int32{int32(123)} // []int32 | Notification group (ID) (optional)
	offset := int32(56) // int32 | The initial index from which to return the results. (optional)
	ordering := "ordering_example" // string | Which field to use when ordering the results. (optional)
	owner := []string{"Inner_example"} // []string | Owner (name) (optional)
	ownerN := []string{"Inner_example"} // []string | Owner (name) (optional)
	ownerId := []int32{int32(123)} // []int32 | Owner (ID) (optional)
	ownerIdN := []int32{int32(123)} // []int32 | Owner (ID) (optional)
	permissionId := []int32{int32(123)} // []int32 | Permission (ID) (optional)
	permissionIdN := []int32{int32(123)} // []int32 | Permission (ID) (optional)
	q := "q_example" // string | Search (optional)
	userId := []int32{int32(123)} // []int32 | User (ID) (optional)
	userIdN := []int32{int32(123)} // []int32 | User (ID) (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UsersAPI.UsersGroupsList(context.Background()).Description(description).DescriptionEmpty(descriptionEmpty).DescriptionIc(descriptionIc).DescriptionIe(descriptionIe).DescriptionIew(descriptionIew).DescriptionIregex(descriptionIregex).DescriptionIsw(descriptionIsw).DescriptionN(descriptionN).DescriptionNic(descriptionNic).DescriptionNie(descriptionNie).DescriptionNiew(descriptionNiew).DescriptionNisw(descriptionNisw).DescriptionRegex(descriptionRegex).Id(id).IdEmpty(idEmpty).IdGt(idGt).IdGte(idGte).IdLt(idLt).IdLte(idLte).IdN(idN).Limit(limit).Name(name).NameEmpty(nameEmpty).NameIc(nameIc).NameIe(nameIe).NameIew(nameIew).NameIregex(nameIregex).NameIsw(nameIsw).NameN(nameN).NameNic(nameNic).NameNie(nameNie).NameNiew(nameNiew).NameNisw(nameNisw).NameRegex(nameRegex).NotificationGroupId(notificationGroupId).NotificationGroupIdN(notificationGroupIdN).Offset(offset).Ordering(ordering).Owner(owner).OwnerN(ownerN).OwnerId(ownerId).OwnerIdN(ownerIdN).PermissionId(permissionId).PermissionIdN(permissionIdN).Q(q).UserId(userId).UserIdN(userIdN).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersAPI.UsersGroupsList``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UsersGroupsList`: PaginatedGroupList
	fmt.Fprintf(os.Stdout, "Response from `UsersAPI.UsersGroupsList`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUsersGroupsListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
 **limit** | **int32** | Number of results to return per page. | 
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
 **notificationGroupId** | **[]int32** | Notification group (ID) | 
 **notificationGroupIdN** | **[]int32** | Notification group (ID) | 
 **offset** | **int32** | The initial index from which to return the results. | 
 **ordering** | **string** | Which field to use when ordering the results. | 
 **owner** | **[]string** | Owner (name) | 
 **ownerN** | **[]string** | Owner (name) | 
 **ownerId** | **[]int32** | Owner (ID) | 
 **ownerIdN** | **[]int32** | Owner (ID) | 
 **permissionId** | **[]int32** | Permission (ID) | 
 **permissionIdN** | **[]int32** | Permission (ID) | 
 **q** | **string** | Search | 
 **userId** | **[]int32** | User (ID) | 
 **userIdN** | **[]int32** | User (ID) | 

### Return type

[**PaginatedGroupList**](PaginatedGroupList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UsersGroupsPartialUpdate

> Group UsersGroupsPartialUpdate(ctx, id).PatchedGroupRequest(patchedGroupRequest).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this group.
	patchedGroupRequest := *openapiclient.NewPatchedGroupRequest() // PatchedGroupRequest |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UsersAPI.UsersGroupsPartialUpdate(context.Background(), id).PatchedGroupRequest(patchedGroupRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersAPI.UsersGroupsPartialUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UsersGroupsPartialUpdate`: Group
	fmt.Fprintf(os.Stdout, "Response from `UsersAPI.UsersGroupsPartialUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this group. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUsersGroupsPartialUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **patchedGroupRequest** | [**PatchedGroupRequest**](PatchedGroupRequest.md) |  | 

### Return type

[**Group**](Group.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UsersGroupsRetrieve

> Group UsersGroupsRetrieve(ctx, id).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this group.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UsersAPI.UsersGroupsRetrieve(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersAPI.UsersGroupsRetrieve``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UsersGroupsRetrieve`: Group
	fmt.Fprintf(os.Stdout, "Response from `UsersAPI.UsersGroupsRetrieve`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this group. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUsersGroupsRetrieveRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**Group**](Group.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UsersGroupsUpdate

> Group UsersGroupsUpdate(ctx, id).GroupRequest(groupRequest).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this group.
	groupRequest := *openapiclient.NewGroupRequest("Name_example") // GroupRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UsersAPI.UsersGroupsUpdate(context.Background(), id).GroupRequest(groupRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersAPI.UsersGroupsUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UsersGroupsUpdate`: Group
	fmt.Fprintf(os.Stdout, "Response from `UsersAPI.UsersGroupsUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this group. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUsersGroupsUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **groupRequest** | [**GroupRequest**](GroupRequest.md) |  | 

### Return type

[**Group**](Group.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UsersPermissionsBulkPartialUpdate

> []ObjectPermission UsersPermissionsBulkPartialUpdate(ctx).ObjectPermissionRequest(objectPermissionRequest).Execute()





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
	objectPermissionRequest := []openapiclient.ObjectPermissionRequest{*openapiclient.NewObjectPermissionRequest("Name_example", []string{"ObjectTypes_example"}, []string{"Actions_example"})} // []ObjectPermissionRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UsersAPI.UsersPermissionsBulkPartialUpdate(context.Background()).ObjectPermissionRequest(objectPermissionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersAPI.UsersPermissionsBulkPartialUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UsersPermissionsBulkPartialUpdate`: []ObjectPermission
	fmt.Fprintf(os.Stdout, "Response from `UsersAPI.UsersPermissionsBulkPartialUpdate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUsersPermissionsBulkPartialUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **objectPermissionRequest** | [**[]ObjectPermissionRequest**](ObjectPermissionRequest.md) |  | 

### Return type

[**[]ObjectPermission**](ObjectPermission.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UsersPermissionsBulkUpdate

> []ObjectPermission UsersPermissionsBulkUpdate(ctx).ObjectPermissionRequest(objectPermissionRequest).Execute()





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
	objectPermissionRequest := []openapiclient.ObjectPermissionRequest{*openapiclient.NewObjectPermissionRequest("Name_example", []string{"ObjectTypes_example"}, []string{"Actions_example"})} // []ObjectPermissionRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UsersAPI.UsersPermissionsBulkUpdate(context.Background()).ObjectPermissionRequest(objectPermissionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersAPI.UsersPermissionsBulkUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UsersPermissionsBulkUpdate`: []ObjectPermission
	fmt.Fprintf(os.Stdout, "Response from `UsersAPI.UsersPermissionsBulkUpdate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUsersPermissionsBulkUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **objectPermissionRequest** | [**[]ObjectPermissionRequest**](ObjectPermissionRequest.md) |  | 

### Return type

[**[]ObjectPermission**](ObjectPermission.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UsersPermissionsCreate

> ObjectPermission UsersPermissionsCreate(ctx).UsersPermissionsCreateRequest(usersPermissionsCreateRequest).Execute()





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
	usersPermissionsCreateRequest := openapiclient.users_permissions_create_request{ObjectPermissionRequest: openapiclient.NewObjectPermissionRequest("Name_example", []string{"ObjectTypes_example"}, []string{"Actions_example"})} // UsersPermissionsCreateRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UsersAPI.UsersPermissionsCreate(context.Background()).UsersPermissionsCreateRequest(usersPermissionsCreateRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersAPI.UsersPermissionsCreate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UsersPermissionsCreate`: ObjectPermission
	fmt.Fprintf(os.Stdout, "Response from `UsersAPI.UsersPermissionsCreate`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUsersPermissionsCreateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usersPermissionsCreateRequest** | [**UsersPermissionsCreateRequest**](UsersPermissionsCreateRequest.md) |  | 

### Return type

[**ObjectPermission**](ObjectPermission.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UsersPermissionsPartialUpdate

> ObjectPermission UsersPermissionsPartialUpdate(ctx, id).PatchedObjectPermissionRequest(patchedObjectPermissionRequest).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this permission.
	patchedObjectPermissionRequest := *openapiclient.NewPatchedObjectPermissionRequest() // PatchedObjectPermissionRequest |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UsersAPI.UsersPermissionsPartialUpdate(context.Background(), id).PatchedObjectPermissionRequest(patchedObjectPermissionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersAPI.UsersPermissionsPartialUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UsersPermissionsPartialUpdate`: ObjectPermission
	fmt.Fprintf(os.Stdout, "Response from `UsersAPI.UsersPermissionsPartialUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this permission. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUsersPermissionsPartialUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **patchedObjectPermissionRequest** | [**PatchedObjectPermissionRequest**](PatchedObjectPermissionRequest.md) |  | 

### Return type

[**ObjectPermission**](ObjectPermission.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UsersPermissionsRetrieve

> ObjectPermission UsersPermissionsRetrieve(ctx, id).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this permission.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UsersAPI.UsersPermissionsRetrieve(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersAPI.UsersPermissionsRetrieve``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UsersPermissionsRetrieve`: ObjectPermission
	fmt.Fprintf(os.Stdout, "Response from `UsersAPI.UsersPermissionsRetrieve`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this permission. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUsersPermissionsRetrieveRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ObjectPermission**](ObjectPermission.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UsersPermissionsUpdate

> ObjectPermission UsersPermissionsUpdate(ctx, id).ObjectPermissionRequest(objectPermissionRequest).Execute()





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
	id := int32(56) // int32 | A unique integer value identifying this permission.
	objectPermissionRequest := *openapiclient.NewObjectPermissionRequest("Name_example", []string{"ObjectTypes_example"}, []string{"Actions_example"}) // ObjectPermissionRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UsersAPI.UsersPermissionsUpdate(context.Background(), id).ObjectPermissionRequest(objectPermissionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersAPI.UsersPermissionsUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UsersPermissionsUpdate`: ObjectPermission
	fmt.Fprintf(os.Stdout, "Response from `UsersAPI.UsersPermissionsUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | A unique integer value identifying this permission. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUsersPermissionsUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **objectPermissionRequest** | [**ObjectPermissionRequest**](ObjectPermissionRequest.md) |  | 

### Return type

[**ObjectPermission**](ObjectPermission.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

