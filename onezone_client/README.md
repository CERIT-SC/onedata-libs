# onezone_client
# Overview 
This is the RESTful API definition of Onezone component of Onedata data management system [onedata.org](http://onedata.org).  
> This API is defined using [Swagger](http://swagger.io/), the JSON specification can be used to automatically generate client libraries - [swagger.json](../../../swagger/onezone/swagger.json).  

This API allows control and configuration of local Onezone service deployment, in particular management of users, groups, spaces, shares, providers, handle services, handles and clusters.

## Authentication and authorization 
To be able to use this API, the REST client must authenticate with the Onezone service and posses required authorization, which is determined based on client's privileges and relations in the system.  
There are essentially three types of REST clients depending on the authentication:

* **users** - can authenticate using an access token or basic credentials   (only for users originating from Onezone's onepanel). Examples:  
```bash  
curl -H \"x-auth-token: $TOKEN\" [...]  
curl -H \"authorization: Bearer $TOKEN\" [...]  
curl -u \"username:password\" [...]  
curl -H \"macaroon: $TOKEN\" [...]  # DEPRECATED  
```  
> `$TOKEN` can ba a Onedata access token, obtained via Onezone GUI or API, in the form   `MDAxNWxvY2F00aW9...`. If authority delegation for given IdP is enabled,   it is possible to provide an access token from the IdP, which must be prefixed   properly (depending on the configuration), e.g.: `github/GST5aasdA...`.  

* **Oneproviders** - can authenticate using the provider root token,   which was assigned during registration in Onezone. It can be found in   `/etc/op_worker/provider_root_token.txt`. It is used just like a user   access token, for example:  
```bash  
curl -H \"x-auth-token: $TOKEN\" [...]  
curl -H \"authorization: Bearer $TOKEN\" [...]  
curl -H \"macaroon: $TOKEN\" [...]   # DEPRECATED   
```  

> Please mind that the provider root token is highly confidential and must   be kept secret (similarly to a private RSA key).  

* **anonymous** - there is a small subset of operations that do not require     any authentication and are publicly available (look for information about     public availability in the endpoint descriptions).  The authorization of the client is determined based on existing relations and privileges in the system. In most cases, the rules below can be roughly applied:

  * users and providers can access and modify their own data
  * users can perform operations in groups, spaces, handle services, handles     and clusters depending on their privileges in subject entity - the required     privileges are listed in the description of each operation   
  * users can be given special admin privileges (fine-grained) that allow to     access and modify all entities in the system - see certain operations for     details.  

* Authentication and Authorization errors have the following meaning:  
  * HTTP 401 UNAUTHORIZED - the client could not be authenticated  
  * HTTP 403 FORBIDDEN - the client was authenticated, but is not permitted to     perform the action  

## Effective users and effective groups and spaces 
Onedata supports creation of arbitrary nested group and space membership tree structures. In order to determine if a given user belongs to the group directly or indirectly by belonging to a subgroup of a group, separate API calls are provided for getting information about group users (direct group members) and effective users (indirect group members).  

## API structure 
The API is divided into several categories, corresponding to entities in Onedata:  
**Space management** The space management operations of this API provide means for accessing information about spaces and their management.  
**Share management** The share management operations of this API provide means for accessing information about shares and their management.  
**Group management** The group management operations allow creation of user groups, assigning their authorization rights, adding and removing users from groups.  
**User management** The user management methods allow creation of users, managing their authorization credentials as well as space and group membership.  
**Provider management** Provider specific calls allow getting global information about the spaces managed by the provider, and some administrative operations which can be used for monitoring or accounting.  
**Handle service management** The handle service management operations of this API provide means for accessing information about handle services and their management.  
**Handle API** Onezone provides extensive support for integration with Handle system registration services, including support for DOI and PID identifier assignment services. The API provides methods for adding new Handle services to the system, managing which users can use which registration services and complete API for registering identifiers to users' data sets which are made public.  
**Cluster management** Operations for managing Onezone / Oneprovider clusters and their members - users and groups that can access the Onepanel interfaces (REST or GUI) of a cluster.  

## Using the API Onezone
API is quite complex and thus it might be difficult to quickly figure out how to perform specific action, however the following guidelines might be useful:  
* Operations performed by a regular users on their resources are grouped under     `/user` path (**USER** group in the menu)  
* Operations performed by administrators of specific resources (e.g. groups,     spaces, shares) start with specific resource (e.g. `/groups`)   
* By default the operations which list resource membership     (e.g. `/spaces/SPACE_ID/groups/`) will list explicit resource membership.     To get list of effective resource membership (i.e. including indirect     membership), special paths are provided     (e.g. `/spaces/SPACE_ID/effective_groups/`)  

Furthermore, we have prepared a command-line client environment based on Docker which gives easy access to each of Onedata services via command-line clients, with pre-configured shell with full help on the APIs and autocomplete for operations and attributes.
```
docker run -it onedata/rest-cli:21.02.3 
```  
Below you can find some tutorials which show how to use this API in practice:  
* [User oriented tutorial](https://onedata.org/#/home/documentation/doc/using_onedata/using_onedata_from_cli.html)   
* [Administrator oriented tutorial](https://onedata.org/#/home/documentation/doc/administering_onedata/administering_onedata_from_cli.html)   

## Examples  
**Generate new authentication token** 
```bash
curl -u user:password -X POST -H 'Content-type: application/json' -d '{}' \\ https://$ONEZONE_HOST/api/v3/onezone/user/client_tokens 
```  
**Get user details** 
```bash 
curl -H 'X-Auth-Token: $TOKEN' -X GET \\ https://$ONEZONE_HOST/api/v3/onezone/user 
```  
**Get user details using an access token from github** 
```bash
curl -H 'X-Auth-Token: github/ijaAVWq3j9234jA9gPoR9agFja89t9UiPf8tiueSdx' -X GET \\ https://$ONEZONE_HOST/api/v3/onezone/user 
``` 
> Note that GitHub IdP must be properly configured for the example to work: 
> * authority delegation must be enabled 
> * tokenPrefix must be set to \"github/\" 
> > You can learn more in > [the documentation](https://onedata.org/#/home/documentation/doc/administering_onedata/openid_saml_configuration/openid_saml_configuration_19_02[authority-delegation].html). 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 21.02.3
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [https://onedata.org/#/home/support](https://onedata.org/#/home/support)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import onezone_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import onezone_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import onezone_client
from onezone_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
uid = 'uid_example' # str | User Id.
body = onezone_client.UsersUidBody5() # UsersUidBody5 |  (optional)

try:
    # Add user to cluster
    api_instance.add_cluster_user(id, uid, body=body)
except ApiException as e:
    print("Exception when calling ClusterApi->add_cluster_user: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
gid = 'gid_example' # str | Group Id.
body = onezone_client.GroupsGidBody4() # GroupsGidBody4 |  (optional)

try:
    # Add group to cluster
    api_instance.add_group_to_cluster(id, gid, body=body)
except ApiException as e:
    print("Exception when calling ClusterApi->add_group_to_cluster: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
body = onezone_client.GroupCreateRequest() # GroupCreateRequest | Group properties.
id = 'id_example' # str | Cluster Id.

try:
    # Create group in cluster
    api_instance.create_cluster_group(body, id)
except ApiException as e:
    print("Exception when calling ClusterApi->create_cluster_group: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.

try:
    # Create cluster invite token for group
    api_response = api_instance.create_cluster_group_invite_token(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->create_cluster_group_invite_token: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.

try:
    # Create cluster user invite token
    api_response = api_instance.create_cluster_user_invite_token(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->create_cluster_user_invite_token: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.

try:
    # Get cluster details
    api_response = api_instance.get_cluster(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
gid = 'gid_example' # str | Group Id.

try:
    # Get cluster's effective group details
    api_response = api_instance.get_cluster_effective_group(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_effective_group: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
uid = 'uid_example' # str | User Id.

try:
    # Get cluster's effective user details
    api_response = api_instance.get_cluster_effective_user(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_effective_user: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
gid = 'gid_example' # str | Group Id.

try:
    # Get cluster group details
    api_response = api_instance.get_cluster_group(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_group: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
uid = 'uid_example' # str | User Id.

try:
    # Get cluster's user details
    api_response = api_instance.get_cluster_user(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_user: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
gid = 'gid_example' # str | Group Id.

try:
    # Get effective group's cluster membership intermediaries
    api_response = api_instance.get_effective_group_cluster_membership_intermediaries(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_effective_group_cluster_membership_intermediaries: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
uid = 'uid_example' # str | User Id.

try:
    # Get effective user's cluster membership intermediaries
    api_response = api_instance.get_effective_user_cluster_membership_intermediaries(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_effective_user_cluster_membership_intermediaries: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.

try:
    # List cluster's effective groups
    api_response = api_instance.list_cluster_effective_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_cluster_effective_groups: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.

try:
    # List cluster's effective users
    api_response = api_instance.list_cluster_effective_users(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_cluster_effective_users: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.

try:
    # List cluster's groups
    api_response = api_instance.list_cluster_groups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_cluster_groups: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))

try:
    # List all cluster privileges
    api_response = api_instance.list_cluster_privileges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_cluster_privileges: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.

try:
    # List cluster's users
    api_response = api_instance.list_cluster_users(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_cluster_users: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
gid = 'gid_example' # str | Group Id.

try:
    # List effective group's cluster privileges
    api_response = api_instance.list_effective_group_cluster_privileges(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_effective_group_cluster_privileges: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
uid = 'uid_example' # str | User Id.

try:
    # List effective user's cluster privileges
    api_response = api_instance.list_effective_user_cluster_privileges(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_effective_user_cluster_privileges: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
gid = 'gid_example' # str | Group Id.

try:
    # List group's cluster privileges
    api_response = api_instance.list_group_cluster_privileges(id, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_group_cluster_privileges: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
uid = 'uid_example' # str | User Id.

try:
    # List user's cluster privileges
    api_response = api_instance.list_user_cluster_privileges(id, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_user_cluster_privileges: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
body = onezone_client.ClusterUpdateRequest() # ClusterUpdateRequest | Cluster data.
id = 'id_example' # str | Cluster Id.

try:
    # Modify cluster details
    api_instance.modify_cluster(body, id)
except ApiException as e:
    print("Exception when calling ClusterApi->modify_cluster: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))

try:
    # List all clusters
    api_response = api_instance.oz_clusters_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->oz_clusters_list: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
gid = 'gid_example' # str | Group Id.

try:
    # Remove group from cluster
    api_instance.remove_cluster_group(id, gid)
except ApiException as e:
    print("Exception when calling ClusterApi->remove_cluster_group: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
id = 'id_example' # str | Cluster Id.
uid = 'uid_example' # str | User Id.

try:
    # Remove user from cluster
    api_instance.remove_cluster_user(id, uid)
except ApiException as e:
    print("Exception when calling ClusterApi->remove_cluster_user: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
body = onezone_client.ClusterPrivilegesUpdate() # ClusterPrivilegesUpdate | Cluster privileges update request.
id = 'id_example' # str | Cluster Id.
gid = 'gid_example' # str | Group Id.

try:
    # Update group's privileges in a cluster
    api_instance.update_group_cluster_privileges(body, id, gid)
except ApiException as e:
    print("Exception when calling ClusterApi->update_group_cluster_privileges: %s\n" % e)

# Configure API key authorization: api_key1
configuration = onezone_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: api_key2
configuration = onezone_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: basic
configuration = onezone_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = onezone_client.ClusterApi(onezone_client.ApiClient(configuration))
body = onezone_client.ClusterPrivilegesUpdate() # ClusterPrivilegesUpdate | Cluster privileges update request.
id = 'id_example' # str | Cluster Id.
uid = 'uid_example' # str | User Id.

try:
    # Update user's cluster privileges
    api_instance.update_user_cluster_privileges(body, id, uid)
except ApiException as e:
    print("Exception when calling ClusterApi->update_user_cluster_privileges: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */api/v3/onezone*

| Class              | Method                                                                                                                                      | HTTP request                                                    | Description                                                            |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------------------------------------------------------|
| *ClusterApi*       | [**add_cluster_user**](docs/ClusterApi.md#add_cluster_user)                                                                                 | **PUT** /clusters/{id}/users/{uid}                              | Add user to cluster                                                    |
| *ClusterApi*       | [**add_group_to_cluster**](docs/ClusterApi.md#add_group_to_cluster)                                                                         | **PUT** /clusters/{id}/groups/{gid}                             | Add group to cluster                                                   |
| *ClusterApi*       | [**create_cluster_group**](docs/ClusterApi.md#create_cluster_group)                                                                         | **POST** /clusters/{id}/groups                                  | Create group in cluster                                                |
| *ClusterApi*       | [**create_cluster_group_invite_token**](docs/ClusterApi.md#create_cluster_group_invite_token)                                               | **POST** /clusters/{id}/groups/token                            | Create cluster invite token for group                                  |
| *ClusterApi*       | [**create_cluster_user_invite_token**](docs/ClusterApi.md#create_cluster_user_invite_token)                                                 | **POST** /clusters/{id}/users/token                             | Create cluster user invite token                                       |
| *ClusterApi*       | [**get_cluster**](docs/ClusterApi.md#get_cluster)                                                                                           | **GET** /clusters/{id}                                          | Get cluster details                                                    |
| *ClusterApi*       | [**get_cluster_effective_group**](docs/ClusterApi.md#get_cluster_effective_group)                                                           | **GET** /clusters/{id}/effective_groups/{gid}                   | Get cluster&#x27;s effective group details                             |
| *ClusterApi*       | [**get_cluster_effective_user**](docs/ClusterApi.md#get_cluster_effective_user)                                                             | **GET** /clusters/{id}/effective_users/{uid}                    | Get cluster&#x27;s effective user details                              |
| *ClusterApi*       | [**get_cluster_group**](docs/ClusterApi.md#get_cluster_group)                                                                               | **GET** /clusters/{id}/groups/{gid}                             | Get cluster group details                                              |
| *ClusterApi*       | [**get_cluster_user**](docs/ClusterApi.md#get_cluster_user)                                                                                 | **GET** /clusters/{id}/users/{uid}                              | Get cluster&#x27;s user details                                        |
| *ClusterApi*       | [**get_effective_group_cluster_membership_intermediaries**](docs/ClusterApi.md#get_effective_group_cluster_membership_intermediaries)       | **GET** /clusters/{id}/effective_groups/{gid}/membership        | Get effective group&#x27;s cluster membership intermediaries           |
| *ClusterApi*       | [**get_effective_user_cluster_membership_intermediaries**](docs/ClusterApi.md#get_effective_user_cluster_membership_intermediaries)         | **GET** /clusters/{id}/effective_users/{uid}/membership         | Get effective user&#x27;s cluster membership intermediaries            |
| *ClusterApi*       | [**list_cluster_effective_groups**](docs/ClusterApi.md#list_cluster_effective_groups)                                                       | **GET** /clusters/{id}/effective_groups                         | List cluster&#x27;s effective groups                                   |
| *ClusterApi*       | [**list_cluster_effective_users**](docs/ClusterApi.md#list_cluster_effective_users)                                                         | **GET** /clusters/{id}/effective_users                          | List cluster&#x27;s effective users                                    |
| *ClusterApi*       | [**list_cluster_groups**](docs/ClusterApi.md#list_cluster_groups)                                                                           | **GET** /clusters/{id}/groups                                   | List cluster&#x27;s groups                                             |
| *ClusterApi*       | [**list_cluster_privileges**](docs/ClusterApi.md#list_cluster_privileges)                                                                   | **GET** /clusters/privileges                                    | List all cluster privileges                                            |
| *ClusterApi*       | [**list_cluster_users**](docs/ClusterApi.md#list_cluster_users)                                                                             | **GET** /clusters/{id}/users                                    | List cluster&#x27;s users                                              |
| *ClusterApi*       | [**list_effective_group_cluster_privileges**](docs/ClusterApi.md#list_effective_group_cluster_privileges)                                   | **GET** /clusters/{id}/effective_groups/{gid}/privileges        | List effective group&#x27;s cluster privileges                         |
| *ClusterApi*       | [**list_effective_user_cluster_privileges**](docs/ClusterApi.md#list_effective_user_cluster_privileges)                                     | **GET** /clusters/{id}/effective_users/{uid}/privileges         | List effective user&#x27;s cluster privileges                          |
| *ClusterApi*       | [**list_group_cluster_privileges**](docs/ClusterApi.md#list_group_cluster_privileges)                                                       | **GET** /clusters/{id}/groups/{gid}/privileges                  | List group&#x27;s cluster privileges                                   |
| *ClusterApi*       | [**list_user_cluster_privileges**](docs/ClusterApi.md#list_user_cluster_privileges)                                                         | **GET** /clusters/{id}/users/{uid}/privileges                   | List user&#x27;s cluster privileges                                    |
| *ClusterApi*       | [**modify_cluster**](docs/ClusterApi.md#modify_cluster)                                                                                     | **PATCH** /clusters/{id}                                        | Modify cluster details                                                 |
| *ClusterApi*       | [**oz_clusters_list**](docs/ClusterApi.md#oz_clusters_list)                                                                                 | **GET** /clusters                                               | List all clusters                                                      |
| *ClusterApi*       | [**remove_cluster_group**](docs/ClusterApi.md#remove_cluster_group)                                                                         | **DELETE** /clusters/{id}/groups/{gid}                          | Remove group from cluster                                              |
| *ClusterApi*       | [**remove_cluster_user**](docs/ClusterApi.md#remove_cluster_user)                                                                           | **DELETE** /clusters/{id}/users/{uid}                           | Remove user from cluster                                               |
| *ClusterApi*       | [**update_group_cluster_privileges**](docs/ClusterApi.md#update_group_cluster_privileges)                                                   | **PATCH** /clusters/{id}/groups/{gid}/privileges                | Update group&#x27;s privileges in a cluster                            |
| *ClusterApi*       | [**update_user_cluster_privileges**](docs/ClusterApi.md#update_user_cluster_privileges)                                                     | **PATCH** /clusters/{id}/users/{uid}/privileges                 | Update user&#x27;s cluster privileges                                  |
| *GroupApi*         | [**add_child_group**](docs/GroupApi.md#add_child_group)                                                                                     | **PUT** /groups/{id}/children/{cid}                             | Add child group                                                        |
| *GroupApi*         | [**add_group_handle_service**](docs/GroupApi.md#add_group_handle_service)                                                                   | **POST** /groups/{id}/handle_services                           | Create a new handle service for given group.                           |
| *GroupApi*         | [**add_group_user**](docs/GroupApi.md#add_group_user)                                                                                       | **PUT** /groups/{id}/users/{uid}                                | Add user to group                                                      |
| *GroupApi*         | [**create_child_group**](docs/GroupApi.md#create_child_group)                                                                               | **POST** /groups/{id}/children                                  | Create child group                                                     |
| *GroupApi*         | [**create_child_group_token**](docs/GroupApi.md#create_child_group_token)                                                                   | **POST** /groups/{id}/children/token                            | Create child group invitation token                                    |
| *GroupApi*         | [**create_group**](docs/GroupApi.md#create_group)                                                                                           | **POST** /groups                                                | Create new group                                                       |
| *GroupApi*         | [**create_group_handle**](docs/GroupApi.md#create_group_handle)                                                                             | **POST** /groups/{id}/handles                                   | Create a new handle for given group                                    |
| *GroupApi*         | [**create_harvester_for_group**](docs/GroupApi.md#create_harvester_for_group)                                                               | **POST** /groups/{id}/harvesters                                | Create a new harvester for given group                                 |
| *GroupApi*         | [**create_parent_group**](docs/GroupApi.md#create_parent_group)                                                                             | **POST** /groups/{id}/parents                                   | Create a new parent group for given group                              |
| *GroupApi*         | [**create_space_for_group**](docs/GroupApi.md#create_space_for_group)                                                                       | **POST** /groups/{id}/spaces                                    | Create a new space for given group                                     |
| *GroupApi*         | [**create_user_group_invite_token**](docs/GroupApi.md#create_user_group_invite_token)                                                       | **POST** /groups/{id}/users/token                               | Create user invite token for group                                     |
| *GroupApi*         | [**get_child_group**](docs/GroupApi.md#get_child_group)                                                                                     | **GET** /groups/{id}/children/{cid}                             | Get child group details                                                |
| *GroupApi*         | [**get_effective_child_group**](docs/GroupApi.md#get_effective_child_group)                                                                 | **GET** /groups/{id}/effective_children/{cid}                   | Get effective child group details                                      |
| *GroupApi*         | [**get_effective_child_group_membership_intermediaries**](docs/GroupApi.md#get_effective_child_group_membership_intermediaries)             | **GET** /groups/{id}/effective_children/{cid}/membership        | Get effective child&#x27;s group membership intermediaries             |
| *GroupApi*         | [**get_effective_children_groups**](docs/GroupApi.md#get_effective_children_groups)                                                         | **GET** /groups/{id}/effective_children                         | Get effective child groups                                             |
| *GroupApi*         | [**get_effective_group_handle**](docs/GroupApi.md#get_effective_group_handle)                                                               | **GET** /groups/{id}/effective_handles/{hid}                    | Get effective group handle details                                     |
| *GroupApi*         | [**get_effective_group_harvester**](docs/GroupApi.md#get_effective_group_harvester)                                                         | **GET** /groups/{id}/effective_harvesters/{hid}                 | Get effective group harvester details                                  |
| *GroupApi*         | [**get_effective_group_space**](docs/GroupApi.md#get_effective_group_space)                                                                 | **GET** /groups/{id}/effective_spaces/{sid}                     | Get effective group space details                                      |
| *GroupApi*         | [**get_effective_group_user**](docs/GroupApi.md#get_effective_group_user)                                                                   | **GET** /groups/{id}/effective_users/{uid}                      | Get effective group user details                                       |
| *GroupApi*         | [**get_effective_parent_group**](docs/GroupApi.md#get_effective_parent_group)                                                               | **GET** /groups/{id}/effective_parents/{pid}                    | Get effective parent group details                                     |
| *GroupApi*         | [**get_effective_user_group_membership_intermediaries**](docs/GroupApi.md#get_effective_user_group_membership_intermediaries)               | **GET** /groups/{id}/effective_users/{uid}/membership           | Get effective user&#x27;s group membership intermediaries              |
| *GroupApi*         | [**get_group**](docs/GroupApi.md#get_group)                                                                                                 | **GET** /groups/{id}                                            | Get group details                                                      |
| *GroupApi*         | [**get_group_cluster**](docs/GroupApi.md#get_group_cluster)                                                                                 | **GET** /groups/{id}/clusters/{cid}                             | Get group&#x27;s cluster details                                       |
| *GroupApi*         | [**get_group_effective_cluster**](docs/GroupApi.md#get_group_effective_cluster)                                                             | **GET** /groups/{id}/effective_clusters/{cid}                   | Get group&#x27;s effective cluster details                             |
| *GroupApi*         | [**get_group_effective_handle_service**](docs/GroupApi.md#get_group_effective_handle_service)                                               | **GET** /groups/{id}/effective_handle_services/{hsid}           | Get effective group handle service details                             |
| *GroupApi*         | [**get_group_effective_provider**](docs/GroupApi.md#get_group_effective_provider)                                                           | **GET** /groups/{id}/effective_providers/{pid}                  | Get group&#x27;s effective provider details                            |
| *GroupApi*         | [**get_group_handle**](docs/GroupApi.md#get_group_handle)                                                                                   | **GET** /groups/{id}/handles/{hid}                              | Get group handle details                                               |
| *GroupApi*         | [**get_group_handle_service**](docs/GroupApi.md#get_group_handle_service)                                                                   | **GET** /groups/{id}/handle_services/{hsid}                     | Get group handle service details                                       |
| *GroupApi*         | [**get_group_harvester**](docs/GroupApi.md#get_group_harvester)                                                                             | **GET** /groups/{id}/harvesters/{hid}                           | Get group&#x27;s harvester details                                     |
| *GroupApi*         | [**get_group_space**](docs/GroupApi.md#get_group_space)                                                                                     | **GET** /groups/{id}/spaces/{sid}                               | Get group&#x27;s space details                                         |
| *GroupApi*         | [**get_group_spaces_in_effective_provider**](docs/GroupApi.md#get_group_spaces_in_effective_provider)                                       | **GET** /groups/{id}/effective_providers/{pid}/spaces           | Get group&#x27;s spaces that are supported by given effective provider |
| *GroupApi*         | [**get_group_user**](docs/GroupApi.md#get_group_user)                                                                                       | **GET** /groups/{id}/users/{uid}                                | Get group user details                                                 |
| *GroupApi*         | [**get_parent_group**](docs/GroupApi.md#get_parent_group)                                                                                   | **GET** /groups/{id}/parents/{pid}                              | Get parent group details                                               |
| *GroupApi*         | [**group_join_cluster**](docs/GroupApi.md#group_join_cluster)                                                                               | **POST** /groups/{id}/clusters/join                             | Join group to a cluster                                                |
| *GroupApi*         | [**group_join_harvester**](docs/GroupApi.md#group_join_harvester)                                                                           | **POST** /groups/{id}/harvesters/join                           | Join harvester by group                                                |
| *GroupApi*         | [**group_join_space**](docs/GroupApi.md#group_join_space)                                                                                   | **POST** /groups/{id}/spaces/join                               | Join space by group                                                    |
| *GroupApi*         | [**group_leave_cluster**](docs/GroupApi.md#group_leave_cluster)                                                                             | **DELETE** /groups/{id}/clusters/{cid}                          | Leave cluster                                                          |
| *GroupApi*         | [**group_leave_handle**](docs/GroupApi.md#group_leave_handle)                                                                               | **DELETE** /groups/{id}/handles/{hid}                           | Group leave handle                                                     |
| *GroupApi*         | [**group_leave_handle_service**](docs/GroupApi.md#group_leave_handle_service)                                                               | **DELETE** /groups/{id}/handle_services/{hsid}                  | Group leave handle service                                             |
| *GroupApi*         | [**join_parent_group**](docs/GroupApi.md#join_parent_group)                                                                                 | **POST** /groups/{id}/parents/join                              | Join parent group                                                      |
| *GroupApi*         | [**leave_parent_group**](docs/GroupApi.md#leave_parent_group)                                                                               | **DELETE** /groups/{id}/parents/{pid}                           | Leave parent group                                                     |
| *GroupApi*         | [**list_child_group_privileges**](docs/GroupApi.md#list_child_group_privileges)                                                             | **GET** /groups/{id}/children/{cid}/privileges                  | List child&#x27;s group privileges                                     |
| *GroupApi*         | [**list_child_groups**](docs/GroupApi.md#list_child_groups)                                                                                 | **GET** /groups/{id}/children                                   | Get child groups                                                       |
| *GroupApi*         | [**list_effective_child_group_privileges**](docs/GroupApi.md#list_effective_child_group_privileges)                                         | **GET** /groups/{id}/effective_children/{cid}/privileges        | List effective child&#x27;s group privileges                           |
| *GroupApi*         | [**list_effective_group_handle_services**](docs/GroupApi.md#list_effective_group_handle_services)                                           | **GET** /groups/{id}/effective_handle_services                  | List effective group handle services                                   |
| *GroupApi*         | [**list_effective_group_handles**](docs/GroupApi.md#list_effective_group_handles)                                                           | **GET** /groups/{id}/effective_handles                          | List effective group handles                                           |
| *GroupApi*         | [**list_effective_group_harvesters**](docs/GroupApi.md#list_effective_group_harvesters)                                                     | **GET** /groups/{id}/effective_harvesters                       | List effective group&#x27;s harvesters                                 |
| *GroupApi*         | [**list_effective_group_providers**](docs/GroupApi.md#list_effective_group_providers)                                                       | **GET** /groups/{id}/effective_providers                        | List effective group&#x27;s providers                                  |
| *GroupApi*         | [**list_effective_group_spaces**](docs/GroupApi.md#list_effective_group_spaces)                                                             | **GET** /groups/{id}/effective_spaces                           | List effective group&#x27;s spaces                                     |
| *GroupApi*         | [**list_effective_group_users**](docs/GroupApi.md#list_effective_group_users)                                                               | **GET** /groups/{id}/effective_users                            | List effective group users                                             |
| *GroupApi*         | [**list_effective_parent_groups**](docs/GroupApi.md#list_effective_parent_groups)                                                           | **GET** /groups/{id}/effective_parents                          | List effective parent groups                                           |
| *GroupApi*         | [**list_effective_user_group_privileges**](docs/GroupApi.md#list_effective_user_group_privileges)                                           | **GET** /groups/{id}/effective_users/{uid}/privileges           | List effective user&#x27;s group privileges                            |
| *GroupApi*         | [**list_group_admin_privileges**](docs/GroupApi.md#list_group_admin_privileges)                                                             | **GET** /groups/{id}/privileges                                 | List group&#x27;s admin privileges                                     |
| *GroupApi*         | [**list_group_clusters**](docs/GroupApi.md#list_group_clusters)                                                                             | **GET** /groups/{id}/clusters                                   | List group&#x27;s clusters                                             |
| *GroupApi*         | [**list_group_effective_admin_privileges**](docs/GroupApi.md#list_group_effective_admin_privileges)                                         | **GET** /groups/{id}/effective_privileges                       | List group&#x27;s effective admin privileges                           |
| *GroupApi*         | [**list_group_effective_clusters**](docs/GroupApi.md#list_group_effective_clusters)                                                         | **GET** /groups/{id}/effective_clusters                         | List group&#x27;s effective clusters                                   |
| *GroupApi*         | [**list_group_handle_services**](docs/GroupApi.md#list_group_handle_services)                                                               | **GET** /groups/{id}/handle_services                            | List group handle services                                             |
| *GroupApi*         | [**list_group_handles**](docs/GroupApi.md#list_group_handles)                                                                               | **GET** /groups/{id}/handles                                    | List group handles                                                     |
| *GroupApi*         | [**list_group_harvesters**](docs/GroupApi.md#list_group_harvesters)                                                                         | **GET** /groups/{id}/harvesters                                 | List group&#x27;s harvesters                                           |
| *GroupApi*         | [**list_group_privileges**](docs/GroupApi.md#list_group_privileges)                                                                         | **GET** /groups/privileges                                      | List all group privileges                                              |
| *GroupApi*         | [**list_group_spaces**](docs/GroupApi.md#list_group_spaces)                                                                                 | **GET** /groups/{id}/spaces                                     | List group&#x27;s spaces                                               |
| *GroupApi*         | [**list_group_users**](docs/GroupApi.md#list_group_users)                                                                                   | **GET** /groups/{id}/users                                      | List group users                                                       |
| *GroupApi*         | [**list_groups**](docs/GroupApi.md#list_groups)                                                                                             | **GET** /groups                                                 | List all groups                                                        |
| *GroupApi*         | [**list_parent_groups**](docs/GroupApi.md#list_parent_groups)                                                                               | **GET** /groups/{id}/parents                                    | List parent groups                                                     |
| *GroupApi*         | [**list_user_group_privileges**](docs/GroupApi.md#list_user_group_privileges)                                                               | **GET** /groups/{id}/users/{uid}/privileges                     | List user&#x27;s group privileges                                      |
| *GroupApi*         | [**modify_group**](docs/GroupApi.md#modify_group)                                                                                           | **PATCH** /groups/{id}                                          | Modify group details                                                   |
| *GroupApi*         | [**remove_child_group**](docs/GroupApi.md#remove_child_group)                                                                               | **DELETE** /groups/{id}/children/{cid}                          | Remove child group                                                     |
| *GroupApi*         | [**remove_group**](docs/GroupApi.md#remove_group)                                                                                           | **DELETE** /groups/{id}                                         | Remove group                                                           |
| *GroupApi*         | [**remove_group_admin_privileges**](docs/GroupApi.md#remove_group_admin_privileges)                                                         | **DELETE** /groups/{id}/privileges                              | Remove group&#x27;s admin privileges                                   |
| *GroupApi*         | [**remove_group_from_harvester**](docs/GroupApi.md#remove_group_from_harvester)                                                             | **DELETE** /groups/{id}/harvesters/{hid}                        | Remove group from harvester                                            |
| *GroupApi*         | [**remove_group_from_space**](docs/GroupApi.md#remove_group_from_space)                                                                     | **DELETE** /groups/{id}/spaces/{sid}                            | Remove group from space                                                |
| *GroupApi*         | [**remove_group_user**](docs/GroupApi.md#remove_group_user)                                                                                 | **DELETE** /groups/{id}/users/{uid}                             | Remove user from group                                                 |
| *GroupApi*         | [**update_child_group_privileges**](docs/GroupApi.md#update_child_group_privileges)                                                         | **PATCH** /groups/{id}/children/{cid}/privileges                | Update child&#x27;s group privileges                                   |
| *GroupApi*         | [**update_group_admin_privileges**](docs/GroupApi.md#update_group_admin_privileges)                                                         | **PATCH** /groups/{id}/privileges                               | Update group&#x27;s admin privileges                                   |
| *GroupApi*         | [**update_user_group_privileges**](docs/GroupApi.md#update_user_group_privileges)                                                           | **PATCH** /groups/{id}/users/{uid}/privileges                   | Update user&#x27;s group privileges                                    |
| *HandleApi*        | [**add_handle_group**](docs/HandleApi.md#add_handle_group)                                                                                  | **PUT** /handles/{id}/groups/{gid}                              | Add handle group                                                       |
| *HandleApi*        | [**add_handle_user**](docs/HandleApi.md#add_handle_user)                                                                                    | **PUT** /handles/{id}/users/{uid}                               | Add handle user                                                        |
| *HandleApi*        | [**get_effective_handle_group**](docs/HandleApi.md#get_effective_handle_group)                                                              | **GET** /handles/{id}/effective_groups/{gid}                    | Get effective handle group                                             |
| *HandleApi*        | [**get_effective_handle_user**](docs/HandleApi.md#get_effective_handle_user)                                                                | **GET** /handles/{id}/effective_users/{uid}                     | Get effective handle user                                              |
| *HandleApi*        | [**get_handle**](docs/HandleApi.md#get_handle)                                                                                              | **GET** /handles/{id}                                           | Get handle                                                             |
| *HandleApi*        | [**get_handle_group**](docs/HandleApi.md#get_handle_group)                                                                                  | **GET** /handles/{id}/groups/{gid}                              | Get handle group                                                       |
| *HandleApi*        | [**get_handle_user**](docs/HandleApi.md#get_handle_user)                                                                                    | **GET** /handles/{id}/users/{uid}                               | Get handle user                                                        |
| *HandleApi*        | [**get_public_handle_details**](docs/HandleApi.md#get_public_handle_details)                                                                | **GET** /handles/{id}/public                                    | Get public handle details                                              |
| *HandleApi*        | [**handle_service_register_handle**](docs/HandleApi.md#handle_service_register_handle)                                                      | **POST** /handles                                               | Register handle                                                        |
| *HandleApi*        | [**handle_update**](docs/HandleApi.md#handle_update)                                                                                        | **PATCH** /handles/{id}                                         | Modify handle                                                          |
| *HandleApi*        | [**list_effective_group_handle_privileges**](docs/HandleApi.md#list_effective_group_handle_privileges)                                      | **GET** /handles/{id}/effective_groups/{gid}/privileges         | List effective group&#x27;s handle privileges                          |
| *HandleApi*        | [**list_effective_handle_groups**](docs/HandleApi.md#list_effective_handle_groups)                                                          | **GET** /handles/{id}/effective_groups                          | Get effective handle groups                                            |
| *HandleApi*        | [**list_effective_handle_users**](docs/HandleApi.md#list_effective_handle_users)                                                            | **GET** /handles/{id}/effective_users                           | List effective handle users                                            |
| *HandleApi*        | [**list_effective_user_handle_privileges**](docs/HandleApi.md#list_effective_user_handle_privileges)                                        | **GET** /handles/{id}/effective_users/{uid}/privileges          | List effective user&#x27;s handle privileges                           |
| *HandleApi*        | [**list_group_handle_privileges**](docs/HandleApi.md#list_group_handle_privileges)                                                          | **GET** /handles/{id}/groups/{gid}/privileges                   | List group&#x27;s handle privileges                                    |
| *HandleApi*        | [**list_handle_groups**](docs/HandleApi.md#list_handle_groups)                                                                              | **GET** /handles/{id}/groups                                    | List handle groups                                                     |
| *HandleApi*        | [**list_handle_privileges**](docs/HandleApi.md#list_handle_privileges)                                                                      | **GET** /handles/privileges                                     | List all handle privileges                                             |
| *HandleApi*        | [**list_handle_users**](docs/HandleApi.md#list_handle_users)                                                                                | **GET** /handles/{id}/users                                     | List handle users                                                      |
| *HandleApi*        | [**list_handles**](docs/HandleApi.md#list_handles)                                                                                          | **GET** /handles                                                | List handles                                                           |
| *HandleApi*        | [**list_user_handle_privileges**](docs/HandleApi.md#list_user_handle_privileges)                                                            | **GET** /handles/{id}/users/{uid}/privileges                    | List user handle privileges                                            |
| *HandleApi*        | [**remove_handle**](docs/HandleApi.md#remove_handle)                                                                                        | **DELETE** /handles/{id}                                        | Unregister handle                                                      |
| *HandleApi*        | [**remove_handle_group**](docs/HandleApi.md#remove_handle_group)                                                                            | **DELETE** /handles/{id}/groups/{gid}                           | Remove handle group                                                    |
| *HandleApi*        | [**remove_handle_user**](docs/HandleApi.md#remove_handle_user)                                                                              | **DELETE** /handles/{id}/users/{uid}                            | Remove handle user                                                     |
| *HandleApi*        | [**update_group_handle_privileges**](docs/HandleApi.md#update_group_handle_privileges)                                                      | **PATCH** /handles/{id}/groups/{gid}/privileges                 | Update handle groups privileges                                        |
| *HandleApi*        | [**update_handle_user_privileges**](docs/HandleApi.md#update_handle_user_privileges)                                                        | **PATCH** /handles/{id}/users/{uid}/privileges                  | Update user handle privileges                                          |
| *HandleServiceApi* | [**add_handle_service**](docs/HandleServiceApi.md#add_handle_service)                                                                       | **POST** /handle_services                                       | Add handle service                                                     |
| *HandleServiceApi* | [**add_handle_service_group**](docs/HandleServiceApi.md#add_handle_service_group)                                                           | **PUT** /handle_services/{id}/groups/{gid}                      | Add handle service group                                               |
| *HandleServiceApi* | [**add_handle_service_user**](docs/HandleServiceApi.md#add_handle_service_user)                                                             | **PUT** /handle_services/{id}/users/{uid}                       | Add handle service user                                                |
| *HandleServiceApi* | [**get_effective_handle_service_group**](docs/HandleServiceApi.md#get_effective_handle_service_group)                                       | **GET** /handle_services/{id}/effective_groups/{gid}            | Get effective handle service group                                     |
| *HandleServiceApi* | [**get_effective_handle_service_user**](docs/HandleServiceApi.md#get_effective_handle_service_user)                                         | **GET** /handle_services/{id}/effective_users/{uid}             | Get effective handle service user                                      |
| *HandleServiceApi* | [**get_handle_service**](docs/HandleServiceApi.md#get_handle_service)                                                                       | **GET** /handle_services/{id}                                   | Get handle service                                                     |
| *HandleServiceApi* | [**get_handle_service_group**](docs/HandleServiceApi.md#get_handle_service_group)                                                           | **GET** /handle_services/{id}/groups/{gid}                      | Get handle service group details                                       |
| *HandleServiceApi* | [**get_handle_service_handle**](docs/HandleServiceApi.md#get_handle_service_handle)                                                         | **GET** /handle_services/{id}/handles/{hid}                     | Get handle from handle service                                         |
| *HandleServiceApi* | [**get_handle_service_user**](docs/HandleServiceApi.md#get_handle_service_user)                                                             | **GET** /handle_services/{id}/users/{uid}                       | Get handle service user                                                |
| *HandleServiceApi* | [**handle_service_update**](docs/HandleServiceApi.md#handle_service_update)                                                                 | **PATCH** /handle_services/{id}                                 | Modify handle service                                                  |
| *HandleServiceApi* | [**list_effective_group_handle_service_privileges**](docs/HandleServiceApi.md#list_effective_group_handle_service_privileges)               | **GET** /handle_services/{id}/effective_groups/{gid}/privileges | List effective group&#x27;s handle service privileges                  |
| *HandleServiceApi* | [**list_effective_handle_service_groups**](docs/HandleServiceApi.md#list_effective_handle_service_groups)                                   | **GET** /handle_services/{id}/effective_groups                  | List effective handle service groups                                   |
| *HandleServiceApi* | [**list_effective_handle_service_users**](docs/HandleServiceApi.md#list_effective_handle_service_users)                                     | **GET** /handle_services/{id}/effective_users                   | Get effective handle service users                                     |
| *HandleServiceApi* | [**list_effective_user_handle_service_privileges**](docs/HandleServiceApi.md#list_effective_user_handle_service_privileges)                 | **GET** /handle_services/{id}/effective_users/{uid}/privileges  | List effective user&#x27;s handle service privileges                   |
| *HandleServiceApi* | [**list_group_handle_service_privileges**](docs/HandleServiceApi.md#list_group_handle_service_privileges)                                   | **GET** /handle_services/{id}/groups/{gid}/privileges           | List group&#x27;s handle service privileges                            |
| *HandleServiceApi* | [**list_handle_service_groups**](docs/HandleServiceApi.md#list_handle_service_groups)                                                       | **GET** /handle_services/{id}/groups                            | List handle service groups                                             |
| *HandleServiceApi* | [**list_handle_service_privileges**](docs/HandleServiceApi.md#list_handle_service_privileges)                                               | **GET** /handle_services/privileges                             | List all handle service privileges                                     |
| *HandleServiceApi* | [**list_handle_service_users**](docs/HandleServiceApi.md#list_handle_service_users)                                                         | **GET** /handle_services/{id}/users                             | Get handle service users                                               |
| *HandleServiceApi* | [**list_handle_services**](docs/HandleServiceApi.md#list_handle_services)                                                                   | **GET** /handle_services                                        | List handle services                                                   |
| *HandleServiceApi* | [**list_handleservice_handles**](docs/HandleServiceApi.md#list_handleservice_handles)                                                       | **GET** /handle_services/{id}/handles                           | List handle service handles                                            |
| *HandleServiceApi* | [**list_user_handle_service_privileges**](docs/HandleServiceApi.md#list_user_handle_service_privileges)                                     | **GET** /handle_services/{id}/users/{uid}/privileges            | List user&#x27;s handle service privileges                             |
| *HandleServiceApi* | [**remove_handle_service**](docs/HandleServiceApi.md#remove_handle_service)                                                                 | **DELETE** /handle_services/{id}                                | Unregister handle service                                              |
| *HandleServiceApi* | [**remove_handle_service_group**](docs/HandleServiceApi.md#remove_handle_service_group)                                                     | **DELETE** /handle_services/{id}/groups/{gid}                   | Remove handle service group                                            |
| *HandleServiceApi* | [**remove_handle_service_user**](docs/HandleServiceApi.md#remove_handle_service_user)                                                       | **DELETE** /handle_services/{id}/users/{uid}                    | Remove handle service user                                             |
| *HandleServiceApi* | [**update_group_handle_service_privileges**](docs/HandleServiceApi.md#update_group_handle_service_privileges)                               | **PATCH** /handle_services/{id}/users/{uid}/privileges          | Update user&#x27;s handle service privileges                           |
| *HandleServiceApi* | [**update_group_handle_service_privileges_0**](docs/HandleServiceApi.md#update_group_handle_service_privileges_0)                           | **PATCH** /handle_services/{id}/groups/{gid}/privileges         | Update group&#x27;s handle service privileges                          |
| *HarvesterApi*     | [**add_group_to_harvester**](docs/HarvesterApi.md#add_group_to_harvester)                                                                   | **PUT** /harvesters/{id}/groups/{gid}                           | Add group to harvester                                                 |
| *HarvesterApi*     | [**add_harvester_user**](docs/HarvesterApi.md#add_harvester_user)                                                                           | **PUT** /harvesters/{id}/users/{uid}                            | Add user to harvester                                                  |
| *HarvesterApi*     | [**add_space_to_harvester**](docs/HarvesterApi.md#add_space_to_harvester)                                                                   | **PUT** /harvesters/{id}/spaces/{sid}                           | Add space to harvester                                                 |
| *HarvesterApi*     | [**create_harvester**](docs/HarvesterApi.md#create_harvester)                                                                               | **POST** /harvesters                                            | Create new harvester                                                   |
| *HarvesterApi*     | [**create_harvester_group**](docs/HarvesterApi.md#create_harvester_group)                                                                   | **POST** /harvesters/{id}/groups                                | Create group in harvester                                              |
| *HarvesterApi*     | [**create_harvester_group_token**](docs/HarvesterApi.md#create_harvester_group_token)                                                       | **POST** /harvesters/{id}/groups/token                          | Create harvester invite token for group                                |
| *HarvesterApi*     | [**create_harvester_index**](docs/HarvesterApi.md#create_harvester_index)                                                                   | **POST** /harvesters/{id}/indices                               | Create new index in harvester                                          |
| *HarvesterApi*     | [**create_harvester_invite_space_token**](docs/HarvesterApi.md#create_harvester_invite_space_token)                                         | **POST** /harvesters/{id}/spaces/token                          | Create harvester invite token for space                                |
| *HarvesterApi*     | [**create_harvester_user_invite_token**](docs/HarvesterApi.md#create_harvester_user_invite_token)                                           | **POST** /harvesters/{id}/users/token                           | Create harvester user invite token                                     |
| *HarvesterApi*     | [**get_effective_group_harvester_membership_intermediaries**](docs/HarvesterApi.md#get_effective_group_harvester_membership_intermediaries) | **GET** /harvesters/{id}/effective_groups/{gid}/membership      | Get effective group&#x27;s harvester membership intermediaries         |
| *HarvesterApi*     | [**get_effective_harvester_group**](docs/HarvesterApi.md#get_effective_harvester_group)                                                     | **GET** /harvesters/{id}/effective_groups/{gid}                 | Get effective harvester group details                                  |
| *HarvesterApi*     | [**get_effective_harvester_user**](docs/HarvesterApi.md#get_effective_harvester_user)                                                       | **GET** /harvesters/{id}/effective_users/{uid}                  | Get effective harvester user details                                   |
| *HarvesterApi*     | [**get_effective_user_harvester_membership_intermediaries**](docs/HarvesterApi.md#get_effective_user_harvester_membership_intermediaries)   | **GET** /harvesters/{id}/effective_users/{uid}/membership       | Get effective user&#x27;s harvester membership intermediaries          |
| *HarvesterApi*     | [**get_harvester**](docs/HarvesterApi.md#get_harvester)                                                                                     | **GET** /harvesters/{id}                                        | Get harvester details                                                  |
| *HarvesterApi*     | [**get_harvester_config**](docs/HarvesterApi.md#get_harvester_config)                                                                       | **GET** /harvesters/{id}/gui_plugin_config                      | Get harvester configuration                                            |
| *HarvesterApi*     | [**get_harvester_group**](docs/HarvesterApi.md#get_harvester_group)                                                                         | **GET** /harvesters/{id}/groups/{gid}                           | Get harvester&#x27;s group details                                     |
| *HarvesterApi*     | [**get_harvester_index**](docs/HarvesterApi.md#get_harvester_index)                                                                         | **GET** /harvesters/{id}/indices/{idx}                          | Get harvester index details                                            |
| *HarvesterApi*     | [**get_harvester_index_stats**](docs/HarvesterApi.md#get_harvester_index_stats)                                                             | **GET** /harvesters/{id}/indices/{idx}/stats                    | Get harvester index stats                                              |
| *HarvesterApi*     | [**get_harvester_space**](docs/HarvesterApi.md#get_harvester_space)                                                                         | **GET** /harvesters/{id}/spaces/{sid}                           | Get harvester space details                                            |
| *HarvesterApi*     | [**get_harvester_user**](docs/HarvesterApi.md#get_harvester_user)                                                                           | **GET** /harvesters/{id}/users/{uid}                            | Get harvester user details                                             |
| *HarvesterApi*     | [**harvester_join_space**](docs/HarvesterApi.md#harvester_join_space)                                                                       | **POST** /harvesters/{id}/spaces/join                           | Join harvester to a space                                              |
| *HarvesterApi*     | [**list_effective_group_harvester_privileges**](docs/HarvesterApi.md#list_effective_group_harvester_privileges)                             | **GET** /harvesters/{id}/effective_groups/{gid}/privileges      | List effective group&#x27;s harvester privileges                       |
| *HarvesterApi*     | [**list_effective_harvester_groups**](docs/HarvesterApi.md#list_effective_harvester_groups)                                                 | **GET** /harvesters/{id}/effective_groups                       | List effective harvester groups                                        |
| *HarvesterApi*     | [**list_effective_harvester_users**](docs/HarvesterApi.md#list_effective_harvester_users)                                                   | **GET** /harvesters/{id}/effective_users                        | List effective harvester users                                         |
| *HarvesterApi*     | [**list_effective_user_harvester_privileges**](docs/HarvesterApi.md#list_effective_user_harvester_privileges)                               | **GET** /harvesters/{id}/effective_users/{uid}/privileges       | List effective user&#x27;s harvester privileges                        |
| *HarvesterApi*     | [**list_group_harvester_privileges**](docs/HarvesterApi.md#list_group_harvester_privileges)                                                 | **GET** /harvesters/{id}/groups/{gid}/privileges                | List group&#x27;s harvester privileges                                 |
| *HarvesterApi*     | [**list_harvester_groups**](docs/HarvesterApi.md#list_harvester_groups)                                                                     | **GET** /harvesters/{id}/groups                                 | List harvester groups                                                  |
| *HarvesterApi*     | [**list_harvester_indices**](docs/HarvesterApi.md#list_harvester_indices)                                                                   | **GET** /harvesters/{id}/indices                                | List harvester indices                                                 |
| *HarvesterApi*     | [**list_harvester_privileges**](docs/HarvesterApi.md#list_harvester_privileges)                                                             | **GET** /harvesters/privileges                                  | List all harvester privileges                                          |
| *HarvesterApi*     | [**list_harvester_spaces**](docs/HarvesterApi.md#list_harvester_spaces)                                                                     | **GET** /harvesters/{id}/spaces                                 | List harvester spaces                                                  |
| *HarvesterApi*     | [**list_harvester_users**](docs/HarvesterApi.md#list_harvester_users)                                                                       | **GET** /harvesters/{id}/users                                  | List harvester users                                                   |
| *HarvesterApi*     | [**list_user_harvester_privileges**](docs/HarvesterApi.md#list_user_harvester_privileges)                                                   | **GET** /harvesters/{id}/users/{uid}/privileges                 | List user&#x27;s harvester privileges                                  |
| *HarvesterApi*     | [**modify_harvester**](docs/HarvesterApi.md#modify_harvester)                                                                               | **PATCH** /harvesters/{id}                                      | Modify harvester details                                               |
| *HarvesterApi*     | [**modify_harvester_config**](docs/HarvesterApi.md#modify_harvester_config)                                                                 | **PATCH** /harvesters/{id}/gui_plugin_config                    | Modify harvester configuration                                         |
| *HarvesterApi*     | [**modify_harvester_index**](docs/HarvesterApi.md#modify_harvester_index)                                                                   | **PATCH** /harvesters/{id}/indices/{idx}                        | Modify harvester index                                                 |
| *HarvesterApi*     | [**oz_harvesters_list**](docs/HarvesterApi.md#oz_harvesters_list)                                                                           | **GET** /harvesters                                             | List all harvesters                                                    |
| *HarvesterApi*     | [**query_harvester_index**](docs/HarvesterApi.md#query_harvester_index)                                                                     | **POST** /harvesters/{id}/indices/{idx}/query                   | Query harvester index                                                  |
| *HarvesterApi*     | [**remove_harvested_index_metadata**](docs/HarvesterApi.md#remove_harvested_index_metadata)                                                 | **DELETE** /harvesters/{id}/indices/{idx}/metadata              | Remove harvested index metadata                                        |
| *HarvesterApi*     | [**remove_harvested_metadata**](docs/HarvesterApi.md#remove_harvested_metadata)                                                             | **DELETE** /harvesters/{id}/metadata                            | Remove harvested metadata                                              |
| *HarvesterApi*     | [**remove_harvester**](docs/HarvesterApi.md#remove_harvester)                                                                               | **DELETE** /harvesters/{id}                                     | Remove harvester                                                       |
| *HarvesterApi*     | [**remove_harvester_group**](docs/HarvesterApi.md#remove_harvester_group)                                                                   | **DELETE** /harvesters/{id}/groups/{gid}                        | Remove group from harvester                                            |
| *HarvesterApi*     | [**remove_harvester_index**](docs/HarvesterApi.md#remove_harvester_index)                                                                   | **DELETE** /harvesters/{id}/indices/{idx}                       | Remove harvester index                                                 |
| *HarvesterApi*     | [**remove_harvester_space**](docs/HarvesterApi.md#remove_harvester_space)                                                                   | **DELETE** /harvesters/{id}/spaces/{sid}                        | Remove harvester space                                                 |
| *HarvesterApi*     | [**remove_harvester_user**](docs/HarvesterApi.md#remove_harvester_user)                                                                     | **DELETE** /harvesters/{id}/users/{uid}                         | Remove user from harvester                                             |
| *HarvesterApi*     | [**update_group_harvester_privileges**](docs/HarvesterApi.md#update_group_harvester_privileges)                                             | **PATCH** /harvesters/{id}/groups/{gid}/privileges              | Update group privileges to harvester                                   |
| *HarvesterApi*     | [**update_user_harvester_privileges**](docs/HarvesterApi.md#update_user_harvester_privileges)                                               | **PATCH** /harvesters/{id}/users/{uid}/privileges               | Update user&#x27;s harvester privileges                                |
| *ProviderApi*      | [**check_current_time**](docs/ProviderApi.md#check_current_time)                                                                            | **GET** /provider/public/get_current_time                       | Show current clock time                                                |
| *ProviderApi*      | [**check_my_ip**](docs/ProviderApi.md#check_my_ip)                                                                                          | **GET** /provider/public/check_my_ip                            | Show client IP address                                                 |
| *ProviderApi*      | [**get_current_provider_details**](docs/ProviderApi.md#get_current_provider_details)                                                        | **GET** /provider                                               | Get current provider details                                           |
| *ProviderApi*      | [**get_current_provider_domain_config**](docs/ProviderApi.md#get_current_provider_domain_config)                                            | **GET** /provider/domain_config                                 | Get current provider&#x27;s domain config                              |
| *ProviderApi*      | [**get_effective_group_provider_membership_intermediaries**](docs/ProviderApi.md#get_effective_group_provider_membership_intermediaries)    | **GET** /providers/{id}/effective_groups/{gid}/membership       | Get effective group&#x27;s provider membership intermediaries          |
| *ProviderApi*      | [**get_effective_provider_group**](docs/ProviderApi.md#get_effective_provider_group)                                                        | **GET** /providers/{id}/effective_groups/{gid}                  | Get group of provider                                                  |
| *ProviderApi*      | [**get_effective_provider_user**](docs/ProviderApi.md#get_effective_provider_user)                                                          | **GET** /providers/{id}/effective_users/{uid}                   | Get effective user of provider                                         |
| *ProviderApi*      | [**get_effective_user_provider_membership_intermediaries**](docs/ProviderApi.md#get_effective_user_provider_membership_intermediaries)      | **GET** /providers/{id}/effective_users/{uid}/membership        | Get effective user&#x27;s provider membership intermediaries           |
| *ProviderApi*      | [**get_provider_details**](docs/ProviderApi.md#get_provider_details)                                                                        | **GET** /providers/{id}                                         | Get provider details                                                   |
| *ProviderApi*      | [**get_provider_domain_config**](docs/ProviderApi.md#get_provider_domain_config)                                                            | **GET** /providers/{id}/domain_config                           | Get provider&#x27;s domain config                                      |
| *ProviderApi*      | [**get_provider_space**](docs/ProviderApi.md#get_provider_space)                                                                            | **GET** /providers/{id}/spaces/{sid}                            | Get space supported by provider                                        |
| *ProviderApi*      | [**get_supported_space**](docs/ProviderApi.md#get_supported_space)                                                                          | **GET** /provider/spaces/{sid}                                  | Get space details by provider                                          |
| *ProviderApi*      | [**list_current_provider_supported_spaces**](docs/ProviderApi.md#list_current_provider_supported_spaces)                                    | **GET** /provider/spaces                                        | List current provider&#x27;s supported spaces                          |
| *ProviderApi*      | [**list_effective_provider_groups**](docs/ProviderApi.md#list_effective_provider_groups)                                                    | **GET** /providers/{id}/effective_groups                        | List effective groups of provider                                      |
| *ProviderApi*      | [**list_effective_provider_users**](docs/ProviderApi.md#list_effective_provider_users)                                                      | **GET** /providers/{id}/effective_users                         | List effective users of provider                                       |
| *ProviderApi*      | [**list_provider_supported_spaces**](docs/ProviderApi.md#list_provider_supported_spaces)                                                    | **GET** /providers/{id}/spaces                                  | List provider&#x27;s supported spaces                                  |
| *ProviderApi*      | [**map_idp_group**](docs/ProviderApi.md#map_idp_group)                                                                                      | **POST** /provider/public/map_idp_group                         | Map IdP group to Onezone group                                         |
| *ProviderApi*      | [**map_idp_user**](docs/ProviderApi.md#map_idp_user)                                                                                        | **POST** /provider/public/map_idp_user                          | Map IdP user to Onezone user                                           |
| *ProviderApi*      | [**modify_provider**](docs/ProviderApi.md#modify_provider)                                                                                  | **PATCH** /provider                                             | Modify provider details                                                |
| *ProviderApi*      | [**modify_supported_space**](docs/ProviderApi.md#modify_supported_space)                                                                    | **PATCH** /provider/spaces/{sid}                                | Modify supported space                                                 |
| *ProviderApi*      | [**oz_providers_list**](docs/ProviderApi.md#oz_providers_list)                                                                              | **GET** /providers                                              | List providers                                                         |
| *ProviderApi*      | [**register_provider**](docs/ProviderApi.md#register_provider)                                                                              | **POST** /providers                                             | Register provider                                                      |
| *ProviderApi*      | [**remove_provider**](docs/ProviderApi.md#remove_provider)                                                                                  | **DELETE** /providers/{id}                                      | Remove provider                                                        |
| *ProviderApi*      | [**remove_space_support**](docs/ProviderApi.md#remove_space_support)                                                                        | **DELETE** /provider/spaces/{sid}                               | Remove space support                                                   |
| *ProviderApi*      | [**unregister_provider**](docs/ProviderApi.md#unregister_provider)                                                                          | **DELETE** /provider                                            | Unregister provider                                                    |
| *ProviderApi*      | [**verify_provider_identity**](docs/ProviderApi.md#verify_provider_identity)                                                                | **POST** /provider/public/verify_provider_identity              | Verify the identity of given provider                                  |
| *ShareApi*         | [**get_public_share_details**](docs/ShareApi.md#get_public_share_details)                                                                   | **GET** /shares/{id}/public                                     | Get public share details                                               |
| *ShareApi*         | [**get_share**](docs/ShareApi.md#get_share)                                                                                                 | **GET** /shares/{id}                                            | Get share details                                                      |
| *ShareApi*         | [**get_shared_data**](docs/ShareApi.md#get_shared_data)                                                                                     | **GET** /shares/data/{file_id}/{subpath}                        | Get shared file or directory data                                      |
| *ShareApi*         | [**list_shares**](docs/ShareApi.md#list_shares)                                                                                             | **GET** /shares                                                 | List all shares                                                        |
| *ShareApi*         | [**modify_share**](docs/ShareApi.md#modify_share)                                                                                           | **PATCH** /shares/{id}                                          | Modify share details                                                   |
| *SpaceApi*         | [**add_group_to_space**](docs/SpaceApi.md#add_group_to_space)                                                                               | **PUT** /spaces/{id}/groups/{gid}                               | Add group to space                                                     |
| *SpaceApi*         | [**add_space_owner**](docs/SpaceApi.md#add_space_owner)                                                                                     | **PUT** /spaces/{id}/owners/{uid}                               | Add space owner                                                        |
| *SpaceApi*         | [**add_space_user**](docs/SpaceApi.md#add_space_user)                                                                                       | **PUT** /spaces/{id}/users/{uid}                                | Add user to space                                                      |
| *SpaceApi*         | [**cease_support_by_provider**](docs/SpaceApi.md#cease_support_by_provider)                                                                 | **DELETE** /spaces/{id}/providers/{pid}                         | Ceases space support by provider                                       |
| *SpaceApi*         | [**create_space**](docs/SpaceApi.md#create_space)                                                                                           | **POST** /spaces                                                | Create new space                                                       |
| *SpaceApi*         | [**create_space_group**](docs/SpaceApi.md#create_space_group)                                                                               | **POST** /spaces/{id}/groups                                    | Create group in space                                                  |
| *SpaceApi*         | [**create_space_group_token**](docs/SpaceApi.md#create_space_group_token)                                                                   | **POST** /spaces/{id}/groups/token                              | Create space invite token for group                                    |
| *SpaceApi*         | [**create_space_support_token**](docs/SpaceApi.md#create_space_support_token)                                                               | **POST** /spaces/{id}/providers/token                           | Create space support token                                             |
| *SpaceApi*         | [**create_space_user_invite_token**](docs/SpaceApi.md#create_space_user_invite_token)                                                       | **POST** /spaces/{id}/users/token                               | Create space user invite token                                         |
| *SpaceApi*         | [**get_effective_group_space_membership_intermediaries**](docs/SpaceApi.md#get_effective_group_space_membership_intermediaries)             | **GET** /spaces/{id}/effective_groups/{gid}/membership          | Get effective group&#x27;s space membership intermediaries             |
| *SpaceApi*         | [**get_effective_space_group**](docs/SpaceApi.md#get_effective_space_group)                                                                 | **GET** /spaces/{id}/effective_groups/{gid}                     | Get effective space group details                                      |
| *SpaceApi*         | [**get_effective_space_user**](docs/SpaceApi.md#get_effective_space_user)                                                                   | **GET** /spaces/{id}/effective_users/{uid}                      | Get effective space user details                                       |
| *SpaceApi*         | [**get_effective_user_space_membership_intermediaries**](docs/SpaceApi.md#get_effective_user_space_membership_intermediaries)               | **GET** /spaces/{id}/effective_users/{uid}/membership           | Get effective user&#x27;s space membership intermediaries              |
| *SpaceApi*         | [**get_membership_requester_info**](docs/SpaceApi.md#get_membership_requester_info)                                                         | **GET** /spaces/marketplace/{id}/request/{rid}/requester_info   | Get membership requester info                                          |
| *SpaceApi*         | [**get_space**](docs/SpaceApi.md#get_space)                                                                                                 | **GET** /spaces/{id}                                            | Get space details                                                      |
| *SpaceApi*         | [**get_space_data_in_marketplace**](docs/SpaceApi.md#get_space_data_in_marketplace)                                                         | **GET** /spaces/marketplace/{id}                                | Get space details in the Marketplace                                   |
| *SpaceApi*         | [**get_space_group**](docs/SpaceApi.md#get_space_group)                                                                                     | **GET** /spaces/{id}/groups/{gid}                               | Get space&#x27;s group details                                         |
| *SpaceApi*         | [**get_space_harvester**](docs/SpaceApi.md#get_space_harvester)                                                                             | **GET** /spaces/{id}/harvesters/{hid}                           | Get harvester details                                                  |
| *SpaceApi*         | [**get_space_provider**](docs/SpaceApi.md#get_space_provider)                                                                               | **GET** /spaces/{id}/providers/{pid}                            | Get space provider details                                             |
| *SpaceApi*         | [**get_space_share**](docs/SpaceApi.md#get_space_share)                                                                                     | **GET** /spaces/{id}/shares/{sid}                               | Get space share                                                        |
| *SpaceApi*         | [**get_space_user**](docs/SpaceApi.md#get_space_user)                                                                                       | **GET** /spaces/{id}/users/{uid}                                | Get space user details                                                 |
| *SpaceApi*         | [**list_effective_group_space_privileges**](docs/SpaceApi.md#list_effective_group_space_privileges)                                         | **GET** /spaces/{id}/effective_groups/{gid}/privileges          | List effective group&#x27;s space privileges                           |
| *SpaceApi*         | [**list_effective_space_groups**](docs/SpaceApi.md#list_effective_space_groups)                                                             | **GET** /spaces/{id}/effective_groups                           | List effective space groups                                            |
| *SpaceApi*         | [**list_effective_space_users**](docs/SpaceApi.md#list_effective_space_users)                                                               | **GET** /spaces/{id}/effective_users                            | List effective space users                                             |
| *SpaceApi*         | [**list_effective_user_space_privileges**](docs/SpaceApi.md#list_effective_user_space_privileges)                                           | **GET** /spaces/{id}/effective_users/{uid}/privileges           | List effective user&#x27;s space privileges                            |
| *SpaceApi*         | [**list_group_space_privileges**](docs/SpaceApi.md#list_group_space_privileges)                                                             | **GET** /spaces/{id}/groups/{gid}/privileges                    | List group&#x27;s space privileges                                     |
| *SpaceApi*         | [**list_marketplace**](docs/SpaceApi.md#list_marketplace)                                                                                   | **POST** /spaces/marketplace/list                               | List the Space Marketplace                                             |
| *SpaceApi*         | [**list_space_groups**](docs/SpaceApi.md#list_space_groups)                                                                                 | **GET** /spaces/{id}/groups                                     | List space groups                                                      |
| *SpaceApi*         | [**list_space_harvesters**](docs/SpaceApi.md#list_space_harvesters)                                                                         | **GET** /spaces/{id}/harvesters                                 | List space harvesters                                                  |
| *SpaceApi*         | [**list_space_owners**](docs/SpaceApi.md#list_space_owners)                                                                                 | **GET** /spaces/{id}/owners                                     | List space owners                                                      |
| *SpaceApi*         | [**list_space_privileges**](docs/SpaceApi.md#list_space_privileges)                                                                         | **GET** /spaces/privileges                                      | List all space privileges                                              |
| *SpaceApi*         | [**list_space_providers**](docs/SpaceApi.md#list_space_providers)                                                                           | **GET** /spaces/{id}/providers                                  | List space providers                                                   |
| *SpaceApi*         | [**list_space_shares**](docs/SpaceApi.md#list_space_shares)                                                                                 | **GET** /spaces/{id}/shares                                     | List space shares                                                      |
| *SpaceApi*         | [**list_space_users**](docs/SpaceApi.md#list_space_users)                                                                                   | **GET** /spaces/{id}/users                                      | List space users                                                       |
| *SpaceApi*         | [**list_spaces**](docs/SpaceApi.md#list_spaces)                                                                                             | **GET** /spaces                                                 | List all spaces                                                        |
| *SpaceApi*         | [**list_user_space_privileges**](docs/SpaceApi.md#list_user_space_privileges)                                                               | **GET** /spaces/{id}/users/{uid}/privileges                     | List user&#x27;s space privileges                                      |
| *SpaceApi*         | [**modify_space**](docs/SpaceApi.md#modify_space)                                                                                           | **PATCH** /spaces/{id}                                          | Modify space details                                                   |
| *SpaceApi*         | [**remove_space**](docs/SpaceApi.md#remove_space)                                                                                           | **DELETE** /spaces/{id}                                         | Remove space                                                           |
| *SpaceApi*         | [**remove_space_from_harvester**](docs/SpaceApi.md#remove_space_from_harvester)                                                             | **DELETE** /spaces/{id}/harvesters/{hid}                        | Remove space from harvester.                                           |
| *SpaceApi*         | [**remove_space_group**](docs/SpaceApi.md#remove_space_group)                                                                               | **DELETE** /spaces/{id}/groups/{gid}                            | Remove group from space                                                |
| *SpaceApi*         | [**remove_space_owner**](docs/SpaceApi.md#remove_space_owner)                                                                               | **DELETE** /spaces/{id}/owners/{uid}                            | Remove space owner                                                     |
| *SpaceApi*         | [**remove_space_user**](docs/SpaceApi.md#remove_space_user)                                                                                 | **DELETE** /spaces/{id}/users/{uid}                             | Remove user from space                                                 |
| *SpaceApi*         | [**request_space_membership**](docs/SpaceApi.md#request_space_membership)                                                                   | **POST** /spaces/marketplace/{id}/request                       | Request space membership via Marketplace                               |
| *SpaceApi*         | [**resolve_space_membership_request**](docs/SpaceApi.md#resolve_space_membership_request)                                                   | **POST** /spaces/marketplace/{id}/request/{rid}/resolve         | Resolve space membership request                                       |
| *SpaceApi*         | [**space_join_harvester**](docs/SpaceApi.md#space_join_harvester)                                                                           | **POST** /spaces/{id}/harvesters/join                           | Join space to a harvester                                              |
| *SpaceApi*         | [**update_group_space_privileges**](docs/SpaceApi.md#update_group_space_privileges)                                                         | **PATCH** /spaces/{id}/groups/{gid}/privileges                  | Update group privileges to space                                       |
| *SpaceApi*         | [**update_support_parameters_of_provider**](docs/SpaceApi.md#update_support_parameters_of_provider)                                         | **PATCH** /spaces/{id}/providers/{pid}/support_parameters       | Update space support parameters of provider                            |
| *SpaceApi*         | [**update_user_space_privileges**](docs/SpaceApi.md#update_user_space_privileges)                                                           | **PATCH** /spaces/{id}/users/{uid}/privileges                   | Update user&#x27;s space privileges                                    |
| *TokenApi*         | [**confine_token**](docs/TokenApi.md#confine_token)                                                                                         | **POST** /tokens/confine                                        | Confine a token                                                        |
| *TokenApi*         | [**create_named_token_for_current_provider**](docs/TokenApi.md#create_named_token_for_current_provider)                                     | **POST** /provider/tokens/named                                 | Create named token for current provider                                |
| *TokenApi*         | [**create_named_token_for_current_user**](docs/TokenApi.md#create_named_token_for_current_user)                                             | **POST** /user/tokens/named                                     | Create named token for current user                                    |
| *TokenApi*         | [**create_named_token_for_provider**](docs/TokenApi.md#create_named_token_for_provider)                                                     | **POST** /providers/{id}/tokens/named                           | Create named token for a provider                                      |
| *TokenApi*         | [**create_named_token_for_user**](docs/TokenApi.md#create_named_token_for_user)                                                             | **POST** /users/{id}/tokens/named                               | Create named token for a user                                          |
| *TokenApi*         | [**create_temporary_token_for_current_provider**](docs/TokenApi.md#create_temporary_token_for_current_provider)                             | **POST** /provider/tokens/temporary                             | Create temporary token for current provider                            |
| *TokenApi*         | [**create_temporary_token_for_current_user**](docs/TokenApi.md#create_temporary_token_for_current_user)                                     | **POST** /user/tokens/temporary                                 | Create temporary token for current user                                |
| *TokenApi*         | [**create_temporary_token_for_provider**](docs/TokenApi.md#create_temporary_token_for_provider)                                             | **POST** /providers/{id}/tokens/temporary                       | Create temporary token for a provider                                  |
| *TokenApi*         | [**create_temporary_token_for_user**](docs/TokenApi.md#create_temporary_token_for_user)                                                     | **POST** /users/{id}/tokens/temporary                           | Create temporary token for a user                                      |
| *TokenApi*         | [**delete_named_token**](docs/TokenApi.md#delete_named_token)                                                                               | **DELETE** /tokens/named/{id}                                   | Delete named token                                                     |
| *TokenApi*         | [**delete_named_tokens_of_current_provider**](docs/TokenApi.md#delete_named_tokens_of_current_provider)                                     | **DELETE** /provider/tokens/named                               | Delete named tokens of current provider                                |
| *TokenApi*         | [**delete_named_tokens_of_current_user**](docs/TokenApi.md#delete_named_tokens_of_current_user)                                             | **DELETE** /user/tokens/named                                   | Delete named tokens of current user                                    |
| *TokenApi*         | [**delete_named_tokens_of_provider**](docs/TokenApi.md#delete_named_tokens_of_provider)                                                     | **DELETE** /providers/{id}/tokens/named                         | Delete named tokens of a provider                                      |
| *TokenApi*         | [**delete_named_tokens_of_user**](docs/TokenApi.md#delete_named_tokens_of_user)                                                             | **DELETE** /users/{id}/tokens/named                             | Delete named tokens of a user                                          |
| *TokenApi*         | [**examine_token**](docs/TokenApi.md#examine_token)                                                                                         | **POST** /tokens/examine                                        | Examine a token                                                        |
| *TokenApi*         | [**get_named_token**](docs/TokenApi.md#get_named_token)                                                                                     | **GET** /tokens/named/{id}                                      | Get named token                                                        |
| *TokenApi*         | [**get_named_token_of_current_provider_by_name**](docs/TokenApi.md#get_named_token_of_current_provider_by_name)                             | **GET** /provider/tokens/named/name/{name}                      | Get named token of current provider by name                            |
| *TokenApi*         | [**get_named_token_of_current_user_by_name**](docs/TokenApi.md#get_named_token_of_current_user_by_name)                                     | **GET** /user/tokens/named/name/{name}                          | Get named token of current user by name                                |
| *TokenApi*         | [**get_named_token_of_provider_by_name**](docs/TokenApi.md#get_named_token_of_provider_by_name)                                             | **GET** /providers/{id}/tokens/named/name/{name}                | Get named token of a provider by name                                  |
| *TokenApi*         | [**get_named_token_of_user_by_name**](docs/TokenApi.md#get_named_token_of_user_by_name)                                                     | **GET** /users/{id}/tokens/named/name/{name}                    | Get named token of a user by name                                      |
| *TokenApi*         | [**get_named_token_status**](docs/TokenApi.md#get_named_token_status)                                                                       | **GET** /tokens/named/{id}/status                               | Get named token status                                                 |
| *TokenApi*         | [**get_temporary_token_generation_of_current_provider**](docs/TokenApi.md#get_temporary_token_generation_of_current_provider)               | **GET** /provider/tokens/temporary                              | Get temporary token generation of current provider                     |
| *TokenApi*         | [**get_temporary_token_generation_of_current_user**](docs/TokenApi.md#get_temporary_token_generation_of_current_user)                       | **GET** /user/tokens/temporary                                  | Get temporary token generation of current user                         |
| *TokenApi*         | [**get_temporary_token_generation_of_provider**](docs/TokenApi.md#get_temporary_token_generation_of_provider)                               | **GET** /providers/{id}/tokens/temporary                        | Get temporary token generation of a provider                           |
| *TokenApi*         | [**get_temporary_token_generation_of_user**](docs/TokenApi.md#get_temporary_token_generation_of_user)                                       | **GET** /users/{id}/tokens/temporary                            | Get temporary token generation of a user                               |
| *TokenApi*         | [**list_all_named_tokens**](docs/TokenApi.md#list_all_named_tokens)                                                                         | **GET** /tokens/named                                           | List all named tokens                                                  |
| *TokenApi*         | [**list_named_tokens_of_current_provider**](docs/TokenApi.md#list_named_tokens_of_current_provider)                                         | **GET** /provider/tokens/named                                  | List named tokens of current provider                                  |
| *TokenApi*         | [**list_named_tokens_of_current_user**](docs/TokenApi.md#list_named_tokens_of_current_user)                                                 | **GET** /user/tokens/named                                      | List named tokens of current user                                      |
| *TokenApi*         | [**list_named_tokens_of_provider**](docs/TokenApi.md#list_named_tokens_of_provider)                                                         | **GET** /providers/{id}/tokens/named                            | List named tokens of a provider                                        |
| *TokenApi*         | [**list_named_tokens_of_user**](docs/TokenApi.md#list_named_tokens_of_user)                                                                 | **GET** /users/{id}/tokens/named                                | List named tokens of a user                                            |
| *TokenApi*         | [**modify_named_token**](docs/TokenApi.md#modify_named_token)                                                                               | **PATCH** /tokens/named/{id}                                    | Modify named token                                                     |
| *TokenApi*         | [**revoke_all_temporary_tokens_of_current_provider**](docs/TokenApi.md#revoke_all_temporary_tokens_of_current_provider)                     | **DELETE** /provider/tokens/temporary                           | Revoke all temporary tokens of current provider                        |
| *TokenApi*         | [**revoke_all_temporary_tokens_of_current_user**](docs/TokenApi.md#revoke_all_temporary_tokens_of_current_user)                             | **DELETE** /user/tokens/temporary                               | Revoke all temporary tokens of current user                            |
| *TokenApi*         | [**revoke_all_temporary_tokens_of_provider**](docs/TokenApi.md#revoke_all_temporary_tokens_of_provider)                                     | **DELETE** /providers/{id}/tokens/temporary                     | Revoke all temporary tokens of a provider                              |
| *TokenApi*         | [**revoke_all_temporary_tokens_of_user**](docs/TokenApi.md#revoke_all_temporary_tokens_of_user)                                             | **DELETE** /users/{id}/tokens/temporary                         | Revoke all temporary tokens of a user                                  |
| *TokenApi*         | [**verify_access_token**](docs/TokenApi.md#verify_access_token)                                                                             | **POST** /tokens/verify_access_token                            | Verify an access token                                                 |
| *TokenApi*         | [**verify_identity_token**](docs/TokenApi.md#verify_identity_token)                                                                         | **POST** /tokens/verify_identity_token                          | Verify an identity token                                               |
| *TokenApi*         | [**verify_invite_token**](docs/TokenApi.md#verify_invite_token)                                                                             | **POST** /tokens/verify_invite_token                            | Verify an invite token                                                 |
| *UserApi*          | [**acquire_idp_access_token**](docs/UserApi.md#acquire_idp_access_token)                                                                    | **POST** /user/idp_access_token/{idp}                           | Acquire IdP access token                                               |
| *UserApi*          | [**add_user_handle_service**](docs/UserApi.md#add_user_handle_service)                                                                      | **POST** /user/handle_services                                  | Create a new handle service for the current user                       |
| *UserApi*          | [**change_user_basic_auth_settings**](docs/UserApi.md#change_user_basic_auth_settings)                                                      | **PATCH** /users/{id}/basic_auth                                | Change user&#x27;s basic auth settings                                 |
| *UserApi*          | [**change_user_password**](docs/UserApi.md#change_user_password)                                                                            | **PATCH** /user/password                                        | Change user&#x27;s password                                            |
| *UserApi*          | [**create_client_token**](docs/UserApi.md#create_client_token)                                                                              | **POST** /user/client_tokens                                    | Generate user access token                                             |
| *UserApi*          | [**create_provider_registration_token_for_current_user**](docs/UserApi.md#create_provider_registration_token_for_current_user)              | **POST** /user/clusters/provider_registration_token             | Create provider registration token for current user                    |
| *UserApi*          | [**create_provider_registration_token_for_user**](docs/UserApi.md#create_provider_registration_token_for_user)                              | **POST** /users/{id}/clusters/provider_registration_token       | Create provider registration token for a user                          |
| *UserApi*          | [**create_user**](docs/UserApi.md#create_user)                                                                                              | **POST** /users                                                 | Create new user                                                        |
| *UserApi*          | [**create_user_group**](docs/UserApi.md#create_user_group)                                                                                  | **POST** /user/groups                                           | Create a new group for the current user                                |
| *UserApi*          | [**create_user_handle**](docs/UserApi.md#create_user_handle)                                                                                | **POST** /user/handles                                          | Create a new handle for the current user                               |
| *UserApi*          | [**create_user_harvester**](docs/UserApi.md#create_user_harvester)                                                                          | **POST** /user/harvesters                                       | Create a new harvester for the current user                            |
| *UserApi*          | [**create_user_space**](docs/UserApi.md#create_user_space)                                                                                  | **POST** /user/spaces                                           | Create a new space for the current user                                |
| *UserApi*          | [**get_current_user**](docs/UserApi.md#get_current_user)                                                                                    | **GET** /user                                                   | Get current user details                                               |
| *UserApi*          | [**get_effective_user_harvester**](docs/UserApi.md#get_effective_user_harvester)                                                            | **GET** /user/effective_harvesters/{hid}                        | Get effective harvester details                                        |
| *UserApi*          | [**get_effective_user_space**](docs/UserApi.md#get_effective_user_space)                                                                    | **GET** /user/effective_spaces/{sid}                            | Get effective space details                                            |
| *UserApi*          | [**get_space_membership_requests**](docs/UserApi.md#get_space_membership_requests)                                                          | **GET** /user/space_membership_requests                         | Get summary of space membership requests                               |
| *UserApi*          | [**get_user**](docs/UserApi.md#get_user)                                                                                                    | **GET** /users/{id}                                             | Get user details                                                       |
| *UserApi*          | [**get_user_cluster**](docs/UserApi.md#get_user_cluster)                                                                                    | **GET** /user/clusters/{cid}                                    | Get user&#x27;s cluster details                                        |
| *UserApi*          | [**get_user_effective_cluster**](docs/UserApi.md#get_user_effective_cluster)                                                                | **GET** /user/effective_clusters/{cid}                          | Get user&#x27;s effective cluster details                              |
| *UserApi*          | [**get_user_effective_group**](docs/UserApi.md#get_user_effective_group)                                                                    | **GET** /user/effective_groups/{gid}                            | Get effective group details                                            |
| *UserApi*          | [**get_user_effective_handle**](docs/UserApi.md#get_user_effective_handle)                                                                  | **GET** /user/effective_handles/{hid}                           | Get effective handle details                                           |
| *UserApi*          | [**get_user_effective_handle_service**](docs/UserApi.md#get_user_effective_handle_service)                                                  | **GET** /user/effective_handle_services/{hsid}                  | Get effective handle service details                                   |
| *UserApi*          | [**get_user_effective_provider**](docs/UserApi.md#get_user_effective_provider)                                                              | **GET** /user/effective_providers/{pid}                         | Get user&#x27;s effective provider details                             |
| *UserApi*          | [**get_user_group**](docs/UserApi.md#get_user_group)                                                                                        | **GET** /user/groups/{gid}                                      | Get group details                                                      |
| *UserApi*          | [**get_user_handle**](docs/UserApi.md#get_user_handle)                                                                                      | **GET** /user/handles/{hid}                                     | Get handle details                                                     |
| *UserApi*          | [**get_user_handle_service**](docs/UserApi.md#get_user_handle_service)                                                                      | **GET** /user/handle_services/{hsid}                            | Get user handle service details                                        |
| *UserApi*          | [**get_user_harvester**](docs/UserApi.md#get_user_harvester)                                                                                | **GET** /user/harvesters/{hid}                                  | Get harvester details                                                  |
| *UserApi*          | [**get_user_space**](docs/UserApi.md#get_user_space)                                                                                        | **GET** /user/spaces/{sid}                                      | Get space details                                                      |
| *UserApi*          | [**get_user_space_alias**](docs/UserApi.md#get_user_space_alias)                                                                            | **GET** /user/spaces/{sid}/alias                                | Get user space alias                                                   |
| *UserApi*          | [**get_user_spaces_in_effective_provider**](docs/UserApi.md#get_user_spaces_in_effective_provider)                                          | **GET** /user/effective_providers/{pid}/spaces                  | Get user&#x27;s spaces that are supported by given effective provider  |
| *UserApi*          | [**join_group**](docs/UserApi.md#join_group)                                                                                                | **POST** /user/groups/join                                      | Join group                                                             |
| *UserApi*          | [**join_harvester**](docs/UserApi.md#join_harvester)                                                                                        | **POST** /user/harvesters/join                                  | Join harvester                                                         |
| *UserApi*          | [**join_space**](docs/UserApi.md#join_space)                                                                                                | **POST** /user/spaces/join                                      | Join space                                                             |
| *UserApi*          | [**leave_group**](docs/UserApi.md#leave_group)                                                                                              | **DELETE** /user/groups/{gid}                                   | Leave group                                                            |
| *UserApi*          | [**leave_handle_service**](docs/UserApi.md#leave_handle_service)                                                                            | **DELETE** /user/handle_services/{hsid}                         | Leave handle service                                                   |
| *UserApi*          | [**leave_space**](docs/UserApi.md#leave_space)                                                                                              | **DELETE** /user/spaces/{sid}                                   | Leave space                                                            |
| *UserApi*          | [**list_client_tokens**](docs/UserApi.md#list_client_tokens)                                                                                | **GET** /user/client_tokens                                     | List user access tokens                                                |
| *UserApi*          | [**list_current_user_admin_privileges**](docs/UserApi.md#list_current_user_admin_privileges)                                                | **GET** /user/privileges                                        | List current user privileges                                           |
| *UserApi*          | [**list_current_user_effective_admin_privileges**](docs/UserApi.md#list_current_user_effective_admin_privileges)                            | **GET** /user/effective_privileges                              | List current user effective privileges                                 |
| *UserApi*          | [**list_effective_user_groups**](docs/UserApi.md#list_effective_user_groups)                                                                | **GET** /user/effective_groups                                  | List effective user groups                                             |
| *UserApi*          | [**list_effective_user_harvesters**](docs/UserApi.md#list_effective_user_harvesters)                                                        | **GET** /user/effective_harvesters                              | List effective user harvesters                                         |
| *UserApi*          | [**list_effective_user_providers**](docs/UserApi.md#list_effective_user_providers)                                                          | **GET** /user/effective_providers                               | List user effective providers                                          |
| *UserApi*          | [**list_effective_user_spaces**](docs/UserApi.md#list_effective_user_spaces)                                                                | **GET** /user/effective_spaces                                  | List effective user spaces                                             |
| *UserApi*          | [**list_user_admin_privileges**](docs/UserApi.md#list_user_admin_privileges)                                                                | **GET** /users/{id}/privileges                                  | List user admin privileges                                             |
| *UserApi*          | [**list_user_clusters**](docs/UserApi.md#list_user_clusters)                                                                                | **GET** /user/clusters                                          | List user&#x27;s clusters                                              |
| *UserApi*          | [**list_user_effective_admin_privileges**](docs/UserApi.md#list_user_effective_admin_privileges)                                            | **GET** /users/{id}/effective_privileges                        | List user&#x27;s effective admin privileges                            |
| *UserApi*          | [**list_user_effective_clusters**](docs/UserApi.md#list_user_effective_clusters)                                                            | **GET** /user/effective_clusters                                | List user&#x27;s effective clusters                                    |
| *UserApi*          | [**list_user_effective_handle_services**](docs/UserApi.md#list_user_effective_handle_services)                                              | **GET** /user/effective_handle_services                         | List user effective handle services                                    |
| *UserApi*          | [**list_user_effective_handles**](docs/UserApi.md#list_user_effective_handles)                                                              | **GET** /user/effective_handles                                 | Get user effective handles                                             |
| *UserApi*          | [**list_user_groups**](docs/UserApi.md#list_user_groups)                                                                                    | **GET** /user/groups                                            | List user groups                                                       |
| *UserApi*          | [**list_user_handle_services**](docs/UserApi.md#list_user_handle_services)                                                                  | **GET** /user/handle_services                                   | List user handle services                                              |
| *UserApi*          | [**list_user_handles**](docs/UserApi.md#list_user_handles)                                                                                  | **GET** /user/handles                                           | List user handles                                                      |
| *UserApi*          | [**list_user_harvesters**](docs/UserApi.md#list_user_harvesters)                                                                            | **GET** /user/harvesters                                        | List user harvesters                                                   |
| *UserApi*          | [**list_user_spaces**](docs/UserApi.md#list_user_spaces)                                                                                    | **GET** /user/spaces                                            | List user spaces                                                       |
| *UserApi*          | [**modify_current_user**](docs/UserApi.md#modify_current_user)                                                                              | **PATCH** /user                                                 | Modify current user                                                    |
| *UserApi*          | [**oz_users_list**](docs/UserApi.md#oz_users_list)                                                                                          | **GET** /users                                                  | List all users                                                         |
| *UserApi*          | [**remove_client_token**](docs/UserApi.md#remove_client_token)                                                                              | **DELETE** /user/client_tokens/{tid}                            | Delete access token                                                    |
| *UserApi*          | [**remove_current_user**](docs/UserApi.md#remove_current_user)                                                                              | **DELETE** /user                                                | Remove current user                                                    |
| *UserApi*          | [**remove_current_user_admin_privileges**](docs/UserApi.md#remove_current_user_admin_privileges)                                            | **DELETE** /user/privileges                                     | Remove current user&#x27;s admin privileges                            |
| *UserApi*          | [**remove_user**](docs/UserApi.md#remove_user)                                                                                              | **DELETE** /users/{id}                                          | Remove user                                                            |
| *UserApi*          | [**remove_user_admin_privileges**](docs/UserApi.md#remove_user_admin_privileges)                                                            | **DELETE** /users/{id}/privileges                               | Remove user&#x27;s admin privileges                                    |
| *UserApi*          | [**remove_user_handle**](docs/UserApi.md#remove_user_handle)                                                                                | **DELETE** /user/handles/{hid}                                  | Leave handle                                                           |
| *UserApi*          | [**remove_user_space_alias**](docs/UserApi.md#remove_user_space_alias)                                                                      | **DELETE** /user/spaces/{sid}/alias                             | Remove space alias                                                     |
| *UserApi*          | [**set_user_space_alias**](docs/UserApi.md#set_user_space_alias)                                                                            | **PUT** /user/spaces/{sid}/alias                                | Set user space alias                                                   |
| *UserApi*          | [**toggle_user_access_block**](docs/UserApi.md#toggle_user_access_block)                                                                    | **PATCH** /users/{id}/access_block                              | Block or unblock user access                                           |
| *UserApi*          | [**update_current_user_admin_privileges**](docs/UserApi.md#update_current_user_admin_privileges)                                            | **PATCH** /user/privileges                                      | Update current user&#x27;s admin privileges                            |
| *UserApi*          | [**update_user_admin_privileges**](docs/UserApi.md#update_user_admin_privileges)                                                            | **PATCH** /users/{id}/privileges                                | Update user&#x27;s admin privileges                                    |
| *UserApi*          | [**user_join_cluster**](docs/UserApi.md#user_join_cluster)                                                                                  | **POST** /user/clusters/join                                    | Join cluster                                                           |
| *UserApi*          | [**user_leave_cluster**](docs/UserApi.md#user_leave_cluster)                                                                                | **DELETE** /user/clusters/{cid}                                 | Leave cluster                                                          |
| *UserApi*          | [**user_leave_harvester**](docs/UserApi.md#user_leave_harvester)                                                                            | **DELETE** /user/harvesters/{hid}                               | Leave harvester                                                        |
| *ZoneApi*          | [**get_configuration**](docs/ZoneApi.md#get_configuration)                                                                                  | **GET** /configuration                                          | Returns public configuration of Onezone service.                       |
| *ZoneApi*          | [**health**](docs/ZoneApi.md#health)                                                                                                        | **GET** /health                                                 | Check cluster health                                                   |
| *ZoneApi*          | [**list_privileges**](docs/ZoneApi.md#list_privileges)                                                                                      | **GET** /privileges                                             | List all admin privileges.                                             |
| *ZoneApi*          | [**test_image**](docs/ZoneApi.md#test_image)                                                                                                | **GET** /test_image                                             | Get test image.                                                        |

## Documentation For Models

 - [AdminPrivileges](docs/AdminPrivileges.md)
 - [AdminPrivilegesUpdate](docs/AdminPrivilegesUpdate.md)
 - [Api](docs/Api.md)
 - [Asn](docs/Asn.md)
 - [Caveat](docs/Caveat.md)
 - [ChildrenCidBody](docs/ChildrenCidBody.md)
 - [ClientToken](docs/ClientToken.md)
 - [ClientTokens](docs/ClientTokens.md)
 - [Cluster](docs/Cluster.md)
 - [ClusterInviteToken](docs/ClusterInviteToken.md)
 - [ClusterManagerPrivileges](docs/ClusterManagerPrivileges.md)
 - [ClusterMemberPrivileges](docs/ClusterMemberPrivileges.md)
 - [ClusterPrivileges](docs/ClusterPrivileges.md)
 - [ClusterPrivilegesUpdate](docs/ClusterPrivilegesUpdate.md)
 - [ClusterUpdateRequest](docs/ClusterUpdateRequest.md)
 - [Clusters](docs/Clusters.md)
 - [Configuration](docs/Configuration.md)
 - [ConfigurationSupportedIdPs](docs/ConfigurationSupportedIdPs.md)
 - [Consumer](docs/Consumer.md)
 - [DOIServiceProperties](docs/DOIServiceProperties.md)
 - [DOIServicePropertiesUpdate](docs/DOIServicePropertiesUpdate.md)
 - [DataObjectid](docs/DataObjectid.md)
 - [DataPath](docs/DataPath.md)
 - [DataReadonly](docs/DataReadonly.md)
 - [Error](docs/Error.md)
 - [ErrorError](docs/ErrorError.md)
 - [ExaminedToken](docs/ExaminedToken.md)
 - [GeoCountry](docs/GeoCountry.md)
 - [GeoRegion](docs/GeoRegion.md)
 - [Group](docs/Group.md)
 - [GroupCreateRequest](docs/GroupCreateRequest.md)
 - [GroupInviteToken](docs/GroupInviteToken.md)
 - [GroupJoinCluster](docs/GroupJoinCluster.md)
 - [GroupJoinGroup](docs/GroupJoinGroup.md)
 - [GroupJoinHarvester](docs/GroupJoinHarvester.md)
 - [GroupJoinSpace](docs/GroupJoinSpace.md)
 - [GroupManagerPrivileges](docs/GroupManagerPrivileges.md)
 - [GroupMemberPrivileges](docs/GroupMemberPrivileges.md)
 - [GroupPrivileges](docs/GroupPrivileges.md)
 - [GroupPrivilegesUpdate](docs/GroupPrivilegesUpdate.md)
 - [GroupUpdateRequest](docs/GroupUpdateRequest.md)
 - [Groups](docs/Groups.md)
 - [GroupsGidBody](docs/GroupsGidBody.md)
 - [GroupsGidBody1](docs/GroupsGidBody1.md)
 - [GroupsGidBody2](docs/GroupsGidBody2.md)
 - [GroupsGidBody3](docs/GroupsGidBody3.md)
 - [GroupsGidBody4](docs/GroupsGidBody4.md)
 - [Handle](docs/Handle.md)
 - [HandleMemberPrivileges](docs/HandleMemberPrivileges.md)
 - [HandlePrivileges](docs/HandlePrivileges.md)
 - [HandlePrivilegesUpdate](docs/HandlePrivilegesUpdate.md)
 - [HandleRegistrationRequest](docs/HandleRegistrationRequest.md)
 - [HandleService](docs/HandleService.md)
 - [HandleServiceCreateRequest](docs/HandleServiceCreateRequest.md)
 - [HandleServiceMemberPrivileges](docs/HandleServiceMemberPrivileges.md)
 - [HandleServicePrivileges](docs/HandleServicePrivileges.md)
 - [HandleServicePrivilegesUpdate](docs/HandleServicePrivilegesUpdate.md)
 - [HandleServiceProperties](docs/HandleServiceProperties.md)
 - [HandleServicePropertiesUpdate](docs/HandleServicePropertiesUpdate.md)
 - [HandleServiceUpdate](docs/HandleServiceUpdate.md)
 - [HandleServices](docs/HandleServices.md)
 - [Handles](docs/Handles.md)
 - [HandlesIdBody](docs/HandlesIdBody.md)
 - [Harvester](docs/Harvester.md)
 - [HarvesterCreateRequest](docs/HarvesterCreateRequest.md)
 - [HarvesterGuiPluginConfig](docs/HarvesterGuiPluginConfig.md)
 - [HarvesterIndex](docs/HarvesterIndex.md)
 - [HarvesterIndexCreateRequest](docs/HarvesterIndexCreateRequest.md)
 - [HarvesterIndexStatsDetails](docs/HarvesterIndexStatsDetails.md)
 - [HarvesterIndexStatsDetailsSpaceId](docs/HarvesterIndexStatsDetailsSpaceId.md)
 - [HarvesterIndexStatsDetailsSpaceIdProviderId](docs/HarvesterIndexStatsDetailsSpaceIdProviderId.md)
 - [HarvesterIndices](docs/HarvesterIndices.md)
 - [HarvesterInviteToken](docs/HarvesterInviteToken.md)
 - [HarvesterJoinSpace](docs/HarvesterJoinSpace.md)
 - [HarvesterManagerPrivileges](docs/HarvesterManagerPrivileges.md)
 - [HarvesterMemberPrivileges](docs/HarvesterMemberPrivileges.md)
 - [HarvesterPrivileges](docs/HarvesterPrivileges.md)
 - [HarvesterPrivilegesUpdate](docs/HarvesterPrivilegesUpdate.md)
 - [HarvesterQuery](docs/HarvesterQuery.md)
 - [HarvesterQueryResponse](docs/HarvesterQueryResponse.md)
 - [HarvesterUpdateRequest](docs/HarvesterUpdateRequest.md)
 - [Harvesters](docs/Harvesters.md)
 - [IdPAccessToken](docs/IdPAccessToken.md)
 - [IdRequestBody](docs/IdRequestBody.md)
 - [IdSpacesBody](docs/IdSpacesBody.md)
 - [IndicesIdxBody](docs/IndicesIdxBody.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse20014](docs/InlineResponse20014.md)
 - [InlineResponse20015](docs/InlineResponse20015.md)
 - [InlineResponse20016](docs/InlineResponse20016.md)
 - [InlineResponse20017](docs/InlineResponse20017.md)
 - [InlineResponse20018](docs/InlineResponse20018.md)
 - [InlineResponse20019](docs/InlineResponse20019.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse20020](docs/InlineResponse20020.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2007Spaces](docs/InlineResponse2007Spaces.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [Interface](docs/Interface.md)
 - [InviteToken](docs/InviteToken.md)
 - [InviteTokenPropertyPrivileges](docs/InviteTokenPropertyPrivileges.md)
 - [InviteTokenPropertyUsageLimit](docs/InviteTokenPropertyUsageLimit.md)
 - [Ip](docs/Ip.md)
 - [LinkedAccount](docs/LinkedAccount.md)
 - [MarketplaceListBody](docs/MarketplaceListBody.md)
 - [MembershipIntermediaries](docs/MembershipIntermediaries.md)
 - [MembershipIntermediariesIntermediaries](docs/MembershipIntermediariesIntermediaries.md)
 - [NamedToken](docs/NamedToken.md)
 - [NamedTokenCreateRequest](docs/NamedTokenCreateRequest.md)
 - [NamedTokenCreateResponse](docs/NamedTokenCreateResponse.md)
 - [NamedTokenStatus](docs/NamedTokenStatus.md)
 - [NamedTokenUpdateRequest](docs/NamedTokenUpdateRequest.md)
 - [PIDServiceProperties](docs/PIDServiceProperties.md)
 - [PIDServicePropertiesUpdate](docs/PIDServicePropertiesUpdate.md)
 - [ProviderDetails](docs/ProviderDetails.md)
 - [ProviderDomainConfig](docs/ProviderDomainConfig.md)
 - [ProviderRegistrationRequest](docs/ProviderRegistrationRequest.md)
 - [ProviderRegistrationResponse](docs/ProviderRegistrationResponse.md)
 - [ProviderRegistrationToken](docs/ProviderRegistrationToken.md)
 - [ProviderSyncProgress](docs/ProviderSyncProgress.md)
 - [ProviderSyncProgressAdditionalProperties](docs/ProviderSyncProgressAdditionalProperties.md)
 - [ProviderUpdateRequest](docs/ProviderUpdateRequest.md)
 - [Providers](docs/Providers.md)
 - [PublicMapIdpGroupBody](docs/PublicMapIdpGroupBody.md)
 - [PublicMapIdpUserBody](docs/PublicMapIdpUserBody.md)
 - [PublicVerifyProviderIdentityBody](docs/PublicVerifyProviderIdentityBody.md)
 - [RegisterOneprovider](docs/RegisterOneprovider.md)
 - [RidResolveBody](docs/RidResolveBody.md)
 - [SerializedToken](docs/SerializedToken.md)
 - [Service](docs/Service.md)
 - [Share](docs/Share.md)
 - [Shares](docs/Shares.md)
 - [SharesIdBody](docs/SharesIdBody.md)
 - [Space](docs/Space.md)
 - [SpaceAdvertisedInMarketplace](docs/SpaceAdvertisedInMarketplace.md)
 - [SpaceAlias](docs/SpaceAlias.md)
 - [SpaceCreateRequest](docs/SpaceCreateRequest.md)
 - [SpaceDescription](docs/SpaceDescription.md)
 - [SpaceInviteToken](docs/SpaceInviteToken.md)
 - [SpaceJoinHarvester](docs/SpaceJoinHarvester.md)
 - [SpaceManagerPrivileges](docs/SpaceManagerPrivileges.md)
 - [SpaceMarketplaceContactEmail](docs/SpaceMarketplaceContactEmail.md)
 - [SpaceMarketplaceData](docs/SpaceMarketplaceData.md)
 - [SpaceMemberPrivileges](docs/SpaceMemberPrivileges.md)
 - [SpaceMembershipRequest](docs/SpaceMembershipRequest.md)
 - [SpaceMembershipRequesterInfo](docs/SpaceMembershipRequesterInfo.md)
 - [SpaceMembershipRequests](docs/SpaceMembershipRequests.md)
 - [SpaceOrganizationName](docs/SpaceOrganizationName.md)
 - [SpacePrivileges](docs/SpacePrivileges.md)
 - [SpacePrivilegesUpdate](docs/SpacePrivilegesUpdate.md)
 - [SpaceStats](docs/SpaceStats.md)
 - [SpaceSupportToken](docs/SpaceSupportToken.md)
 - [SpaceTags](docs/SpaceTags.md)
 - [Spaces](docs/Spaces.md)
 - [SpacesBody](docs/SpacesBody.md)
 - [SpacesIdBody](docs/SpacesIdBody.md)
 - [Subject](docs/Subject.md)
 - [SupportParameters](docs/SupportParameters.md)
 - [SupportSpace](docs/SupportSpace.md)
 - [SupportStageDetails](docs/SupportStageDetails.md)
 - [TemporaryTokenCreateRequest](docs/TemporaryTokenCreateRequest.md)
 - [TemporaryTokenGeneration](docs/TemporaryTokenGeneration.md)
 - [Time](docs/Time.md)
 - [Timestamp](docs/Timestamp.md)
 - [TokenPropertyCaveats](docs/TokenPropertyCaveats.md)
 - [TokenPropertyCustomMetadata](docs/TokenPropertyCustomMetadata.md)
 - [TokenPropertyId](docs/TokenPropertyId.md)
 - [TokenPropertyMetadata](docs/TokenPropertyMetadata.md)
 - [TokenPropertyName](docs/TokenPropertyName.md)
 - [TokenPropertyOnezoneDomain](docs/TokenPropertyOnezoneDomain.md)
 - [TokenPropertyPersistence](docs/TokenPropertyPersistence.md)
 - [TokenPropertyRevoked](docs/TokenPropertyRevoked.md)
 - [TokenPropertySubject](docs/TokenPropertySubject.md)
 - [TokenPropertyTokenType](docs/TokenPropertyTokenType.md)
 - [Tokens](docs/Tokens.md)
 - [TokensConfineBody](docs/TokensConfineBody.md)
 - [TokensExamineBody](docs/TokensExamineBody.md)
 - [User](docs/User.md)
 - [UserAccessBlockUpdate](docs/UserAccessBlockUpdate.md)
 - [UserBasicAuthSettingsUpdate](docs/UserBasicAuthSettingsUpdate.md)
 - [UserCreateRequest](docs/UserCreateRequest.md)
 - [UserJoinCluster](docs/UserJoinCluster.md)
 - [UserJoinGroup](docs/UserJoinGroup.md)
 - [UserJoinHarvester](docs/UserJoinHarvester.md)
 - [UserJoinSpace](docs/UserJoinSpace.md)
 - [UserPasswordUpdate](docs/UserPasswordUpdate.md)
 - [UserProtectedInfo](docs/UserProtectedInfo.md)
 - [UserUpdateRequest](docs/UserUpdateRequest.md)
 - [Users](docs/Users.md)
 - [UsersUidBody](docs/UsersUidBody.md)
 - [UsersUidBody1](docs/UsersUidBody1.md)
 - [UsersUidBody2](docs/UsersUidBody2.md)
 - [UsersUidBody3](docs/UsersUidBody3.md)
 - [UsersUidBody4](docs/UsersUidBody4.md)
 - [UsersUidBody5](docs/UsersUidBody5.md)
 - [VerifyAccessTokenRequest](docs/VerifyAccessTokenRequest.md)
 - [VerifyIdentityTokenRequest](docs/VerifyIdentityTokenRequest.md)
 - [VerifyInviteTokenRequest](docs/VerifyInviteTokenRequest.md)
 - [VerifyTokenResponse](docs/VerifyTokenResponse.md)
 - [VersionInfo](docs/VersionInfo.md)
 - [ViewerPrivileges](docs/ViewerPrivileges.md)

## Documentation For Authorization


## api_key1

- **Type**: API key
- **API key parameter name**: X-Auth-Token
- **Location**: HTTP header

## api_key2

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

## basic

- **Type**: HTTP basic authentication


## Author

info@onedata.org
