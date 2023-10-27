# coding: utf-8

"""
    Onezone

    # Overview This is the RESTful API definition of Onezone component of Onedata data management system [onedata.org](http://onedata.org).  > This API is defined using [Swagger](http://swagger.io/), the JSON specification can be used to automatically generate client libraries - [swagger.json](../../../swagger/onezone/swagger.json).  This API allows control and configuration of local Onezone service deployment, in particular management of users, groups, spaces, shares, providers, handle services, handles and clusters.  ## Authentication and authorization To be able to use this API, the REST client must authenticate with the Onezone service and posses required authorization, which is determined based on client's privileges and relations in the system.  There are essentially three types of REST clients depending on the authentication:   * **users** - can authenticate using an access token or basic credentials   (only for users originating from Onezone's onepanel). Examples:   ```bash   curl -H \"x-auth-token: $TOKEN\" [...]   curl -H \"authorization: Bearer $TOKEN\" [...]   curl -u \"username:password\" [...]   curl -H \"macaroon: $TOKEN\" [...]   # DEPRECATED   ```   > `$TOKEN` can ba a Onedata access token, obtained via Onezone GUI or API, in the form   `MDAxNWxvY2F00aW9...`. If authority delegation for given IdP is enabled,   it is possible to provide an access token from the IdP, which must be prefixed   properly (depending on the configuration), e.g.: `github/GST5aasdA...`.    * **Oneproviders** - can authenticate using the provider root token,   which was assigned during registration in Onezone. It can be found in   `/etc/op_worker/provider_root_token.txt`. It is used just like a user   access token, for example:   ```bash   curl -H \"x-auth-token: $TOKEN\" [...]   curl -H \"authorization: Bearer $TOKEN\" [...]   curl -H \"macaroon: $TOKEN\" [...]   # DEPRECATED   ```   > Please mind that the provider root token is highly confidential and must   be kept secret (similarly to a private RSA key).    * **anonymous** - there is a small subset of operations that do not require     any authentication and are publicly available (look for information about     public availability in the endpoint descriptions).  The authorization of the client is determined based on existing relations and privileges in the system. In most cases, the rules below can be roughly applied:   * users and providers can access and modify their own data   * users can perform operations in groups, spaces, handle services, handles     and clusters depending on their privileges in subject entity - the required     privileges are listed in the description of each operation   * users can be given special admin privileges (fine-grained) that allow to     access and modify all entities in the system - see certain operations for     details.  Authentication and Authorization errors have the following meaning:   * HTTP 401 UNAUTHORIZED - the client could not be authenticated   * HTTP 403 FORBIDDEN - the client was authenticated, but is not permitted to     perform the action  ## Effective users and effective groups and spaces Onedata supports creation of arbitrary nested group and space membership tree structures. In order to determine if a given user belongs to the group directly or indirectly by belonging to a subgroup of a group, separate API calls are provided for getting information about group users (direct group members) and effective users (indirect group members).  ## API structure The API is divided into several categories, corresponding to entities in Onedata:  **Space management** The space management operations of this API provide means for accessing information about spaces and their management.  **Share management** The share management operations of this API provide means for accessing information about shares and their management.  **Group management** The group management operations allow creation of user groups, assigning their authorization rights, adding and removing users from groups.  **User management** The user management methods allow creation of users, managing their authorization credentials as well as space and group membership.  **Provider management** Provider specific calls allow getting global information about the spaces managed by the provider, and some administrative operations which can be used for monitoring or accounting.  **Handle service management** The handle service management operations of this API provide means for accessing information about handle services and their management.  **Handle API** Onezone provides extensive support for integration with Handle system registration services, including support for DOI and PID identifier assignment services. The API provides methods for adding new Handle services to the system, managing which users can use which registration services and complete API for registering identifiers to users' data sets which are made public.  **Cluster management** Operations for managing Onezone / Oneprovider clusters and their members - users and groups that can access the Onepanel interfaces (REST or GUI) of a cluster.   ## Using the API Onezone API is quite complex and thus it might be difficult to quickly figure out how to perform specific action, however the following guidelines might be useful:   * Operations performed by a regular users on their resources are grouped under     `/user` path (**USER** group in the menu)   * Operations performed by administrators of specific resources (e.g. groups,     spaces, shares) start with specific resource (e.g. `/groups`)   * By default the operations which list resource membership     (e.g. `/spaces/SPACE_ID/groups/`) will list explicit resource membership.     To get list of effective resource membership (i.e. including indirect     membership), special paths are provided     (e.g. `/spaces/SPACE_ID/effective_groups/`)  Furthermore, we have prepared a command-line client environment based on Docker which gives easy access to each of Onedata services via command-line clients, with pre-configured shell with full help on the APIs and autocomplete for operations and attributes.  ``` docker run -it onedata/rest-cli:21.02.3 ```  Below you can find some tutorials which show how to use this API in practice:   * [User oriented tutorial](https://onedata.org/#/home/documentation/doc/using_onedata/using_onedata_from_cli.html)   * [Administrator oriented tutorial](https://onedata.org/#/home/documentation/doc/administering_onedata/administering_onedata_from_cli.html)   ## Examples  **Generate new authentication token** ```bash curl -u user:password -X POST -H 'Content-type: application/json' -d '{}' \\ https://$ONEZONE_HOST/api/v3/onezone/user/client_tokens ```  **Get user details** ```bash curl -H 'X-Auth-Token: $TOKEN' -X GET \\ https://$ONEZONE_HOST/api/v3/onezone/user ```  **Get user details using an access token from github** ```bash curl -H 'X-Auth-Token: github/ijaAVWq3j9234jA9gPoR9agFja89t9UiPf8tiueSdx' -X GET \\ https://$ONEZONE_HOST/api/v3/onezone/user ``` > Note that GitHub IdP must be properly configured for the example to work: > * authority delegation must be enabled > * tokenPrefix must be set to \"github/\" > > You can learn more in > [the documentation](https://onedata.org/#/home/documentation/doc/administering_onedata/openid_saml_configuration/openid_saml_configuration_19_02[authority-delegation].html).   # noqa: E501

    OpenAPI spec version: 21.02.3
    Contact: info@onedata.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Handle(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'handle_id': 'str',
        'public_handle': 'str',
        'handle_service_id': 'str',
        'resource_type': 'str',
        'resource_id': 'str',
        'metadata': 'str',
        'timestamp': 'str',
        'creator': 'Subject',
        'creation_time': 'Timestamp'
    }

    attribute_map = {
        'handle_id': 'handleId',
        'public_handle': 'publicHandle',
        'handle_service_id': 'handleServiceId',
        'resource_type': 'resourceType',
        'resource_id': 'resourceId',
        'metadata': 'metadata',
        'timestamp': 'timestamp',
        'creator': 'creator',
        'creation_time': 'creationTime'
    }

    def __init__(self, handle_id=None, public_handle=None, handle_service_id=None, resource_type=None, resource_id=None, metadata=None, timestamp=None, creator=None, creation_time=None):  # noqa: E501
        """Handle - a model defined in Swagger"""  # noqa: E501
        self._handle_id = None
        self._public_handle = None
        self._handle_service_id = None
        self._resource_type = None
        self._resource_id = None
        self._metadata = None
        self._timestamp = None
        self._creator = None
        self._creation_time = None
        self.discriminator = None
        self.handle_id = handle_id
        self.public_handle = public_handle
        if handle_service_id is not None:
            self.handle_service_id = handle_service_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.metadata = metadata
        self.timestamp = timestamp
        if creator is not None:
            self.creator = creator
        self.creation_time = creation_time

    @property
    def handle_id(self):
        """Gets the handle_id of this Handle.  # noqa: E501

        Unique Id of the handle in Onedata.  # noqa: E501

        :return: The handle_id of this Handle.  # noqa: E501
        :rtype: str
        """
        return self._handle_id

    @handle_id.setter
    def handle_id(self, handle_id):
        """Sets the handle_id of this Handle.

        Unique Id of the handle in Onedata.  # noqa: E501

        :param handle_id: The handle_id of this Handle.  # noqa: E501
        :type: str
        """
        if handle_id is None:
            raise ValueError("Invalid value for `handle_id`, must not be `None`")  # noqa: E501

        self._handle_id = handle_id

    @property
    def public_handle(self):
        """Gets the public_handle of this Handle.  # noqa: E501

        Unique Id of the handle as registered in the handle service. Depending on the handle service, can be an Id (DOI: 10.5072/w95Zlng) or an URL (PID: http://hdl.handle.net/21.T15999/TgAl7s0).   # noqa: E501

        :return: The public_handle of this Handle.  # noqa: E501
        :rtype: str
        """
        return self._public_handle

    @public_handle.setter
    def public_handle(self, public_handle):
        """Sets the public_handle of this Handle.

        Unique Id of the handle as registered in the handle service. Depending on the handle service, can be an Id (DOI: 10.5072/w95Zlng) or an URL (PID: http://hdl.handle.net/21.T15999/TgAl7s0).   # noqa: E501

        :param public_handle: The public_handle of this Handle.  # noqa: E501
        :type: str
        """
        if public_handle is None:
            raise ValueError("Invalid value for `public_handle`, must not be `None`")  # noqa: E501

        self._public_handle = public_handle

    @property
    def handle_service_id(self):
        """Gets the handle_service_id of this Handle.  # noqa: E501

        Id of the service where the handle was registered. *Not included in public handle details.*   # noqa: E501

        :return: The handle_service_id of this Handle.  # noqa: E501
        :rtype: str
        """
        return self._handle_service_id

    @handle_service_id.setter
    def handle_service_id(self, handle_service_id):
        """Sets the handle_service_id of this Handle.

        Id of the service where the handle was registered. *Not included in public handle details.*   # noqa: E501

        :param handle_service_id: The handle_service_id of this Handle.  # noqa: E501
        :type: str
        """

        self._handle_service_id = handle_service_id

    @property
    def resource_type(self):
        """Gets the resource_type of this Handle.  # noqa: E501

        The type of resource to be registered.  # noqa: E501

        :return: The resource_type of this Handle.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Handle.

        The type of resource to be registered.  # noqa: E501

        :param resource_type: The resource_type of this Handle.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Share"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def resource_id(self):
        """Gets the resource_id of this Handle.  # noqa: E501

        The Id of the resource, corresponding to resourceType (currently, always a share Id).  # noqa: E501

        :return: The resource_id of this Handle.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this Handle.

        The Id of the resource, corresponding to resourceType (currently, always a share Id).  # noqa: E501

        :param resource_id: The resource_id of this Handle.  # noqa: E501
        :type: str
        """
        if resource_id is None:
            raise ValueError("Invalid value for `resource_id`, must not be `None`")  # noqa: E501

        self._resource_id = resource_id

    @property
    def metadata(self):
        """Gets the metadata of this Handle.  # noqa: E501

        Dublin Core metadata for the resource encoded in XML.  # noqa: E501

        :return: The metadata of this Handle.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Handle.

        Dublin Core metadata for the resource encoded in XML.  # noqa: E501

        :param metadata: The metadata of this Handle.  # noqa: E501
        :type: str
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def timestamp(self):
        """Gets the timestamp of this Handle.  # noqa: E501

        Timestamp of the last Handle modification.  # noqa: E501

        :return: The timestamp of this Handle.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Handle.

        Timestamp of the last Handle modification.  # noqa: E501

        :param timestamp: The timestamp of this Handle.  # noqa: E501
        :type: str
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def creator(self):
        """Gets the creator of this Handle.  # noqa: E501


        :return: The creator of this Handle.  # noqa: E501
        :rtype: Subject
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this Handle.


        :param creator: The creator of this Handle.  # noqa: E501
        :type: Subject
        """

        self._creator = creator

    @property
    def creation_time(self):
        """Gets the creation_time of this Handle.  # noqa: E501


        :return: The creation_time of this Handle.  # noqa: E501
        :rtype: Timestamp
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this Handle.


        :param creation_time: The creation_time of this Handle.  # noqa: E501
        :type: Timestamp
        """
        if creation_time is None:
            raise ValueError("Invalid value for `creation_time`, must not be `None`")  # noqa: E501

        self._creation_time = creation_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Handle, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Handle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
