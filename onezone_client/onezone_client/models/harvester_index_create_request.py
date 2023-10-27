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

class HarvesterIndexCreateRequest(object):
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
        'name': 'str',
        'gui_plugin_name': 'str',
        'schema': 'str',
        'include_metadata': 'list[str]',
        'include_file_details': 'list[str]',
        'include_rejection_reason': 'bool',
        'retry_on_rejection': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'gui_plugin_name': 'guiPluginName',
        'schema': 'schema',
        'include_metadata': 'includeMetadata',
        'include_file_details': 'includeFileDetails',
        'include_rejection_reason': 'includeRejectionReason',
        'retry_on_rejection': 'retryOnRejection'
    }

    def __init__(self, name=None, gui_plugin_name=None, schema=None, include_metadata=None, include_file_details=None, include_rejection_reason=None, retry_on_rejection=None):  # noqa: E501
        """HarvesterIndexCreateRequest - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._gui_plugin_name = None
        self._schema = None
        self._include_metadata = None
        self._include_file_details = None
        self._include_rejection_reason = None
        self._retry_on_rejection = None
        self.discriminator = None
        self.name = name
        if gui_plugin_name is not None:
            self.gui_plugin_name = gui_plugin_name
        if schema is not None:
            self.schema = schema
        if include_metadata is not None:
            self.include_metadata = include_metadata
        if include_file_details is not None:
            self.include_file_details = include_file_details
        if include_rejection_reason is not None:
            self.include_rejection_reason = include_rejection_reason
        if retry_on_rejection is not None:
            self.retry_on_rejection = retry_on_rejection

    @property
    def name(self):
        """Gets the name of this HarvesterIndexCreateRequest.  # noqa: E501

        The name of the index.  # noqa: E501

        :return: The name of this HarvesterIndexCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HarvesterIndexCreateRequest.

        The name of the index.  # noqa: E501

        :param name: The name of this HarvesterIndexCreateRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def gui_plugin_name(self):
        """Gets the gui_plugin_name of this HarvesterIndexCreateRequest.  # noqa: E501

        Mapping of index name to one recognized by gui plugin. Allows to specify this index to be used by GUI plugin to produce search results. Recognized gui index names are listed in gui plugin manifest.  # noqa: E501

        :return: The gui_plugin_name of this HarvesterIndexCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._gui_plugin_name

    @gui_plugin_name.setter
    def gui_plugin_name(self, gui_plugin_name):
        """Sets the gui_plugin_name of this HarvesterIndexCreateRequest.

        Mapping of index name to one recognized by gui plugin. Allows to specify this index to be used by GUI plugin to produce search results. Recognized gui index names are listed in gui plugin manifest.  # noqa: E501

        :param gui_plugin_name: The gui_plugin_name of this HarvesterIndexCreateRequest.  # noqa: E501
        :type: str
        """

        self._gui_plugin_name = gui_plugin_name

    @property
    def schema(self):
        """Gets the schema of this HarvesterIndexCreateRequest.  # noqa: E501

        Schema of the index provided as string (e.g. encoded JSON).  # noqa: E501

        :return: The schema of this HarvesterIndexCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this HarvesterIndexCreateRequest.

        Schema of the index provided as string (e.g. encoded JSON).  # noqa: E501

        :param schema: The schema of this HarvesterIndexCreateRequest.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def include_metadata(self):
        """Gets the include_metadata of this HarvesterIndexCreateRequest.  # noqa: E501

        Specifies what types of file metadata should be harvested in this index. At least one type must be given.  # noqa: E501

        :return: The include_metadata of this HarvesterIndexCreateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._include_metadata

    @include_metadata.setter
    def include_metadata(self, include_metadata):
        """Sets the include_metadata of this HarvesterIndexCreateRequest.

        Specifies what types of file metadata should be harvested in this index. At least one type must be given.  # noqa: E501

        :param include_metadata: The include_metadata of this HarvesterIndexCreateRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["json", "xattrs", "rdf"]  # noqa: E501
        if not set(include_metadata).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `include_metadata` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(include_metadata) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._include_metadata = include_metadata

    @property
    def include_file_details(self):
        """Gets the include_file_details of this HarvesterIndexCreateRequest.  # noqa: E501

        Specifies what file details should be harvested alongside the metadata. Enabling `metadataExistenceFlags` will add boolean flags saying whether the file has any metadata of certain type. The `fileName` field may be utilized by the GUI plugin to improve the browsing experience.  # noqa: E501

        :return: The include_file_details of this HarvesterIndexCreateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._include_file_details

    @include_file_details.setter
    def include_file_details(self, include_file_details):
        """Sets the include_file_details of this HarvesterIndexCreateRequest.

        Specifies what file details should be harvested alongside the metadata. Enabling `metadataExistenceFlags` will add boolean flags saying whether the file has any metadata of certain type. The `fileName` field may be utilized by the GUI plugin to improve the browsing experience.  # noqa: E501

        :param include_file_details: The include_file_details of this HarvesterIndexCreateRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["fileName", "spaceId", "metadataExistenceFlags"]  # noqa: E501
        if not set(include_file_details).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `include_file_details` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(include_file_details) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._include_file_details = include_file_details

    @property
    def include_rejection_reason(self):
        """Gets the include_rejection_reason of this HarvesterIndexCreateRequest.  # noqa: E501

        If enabled, all harvesting errors (e.g. when the index rejects a payload due to non-matching schema) are stored as text in the index, which may be useful for later analysis.  # noqa: E501

        :return: The include_rejection_reason of this HarvesterIndexCreateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_rejection_reason

    @include_rejection_reason.setter
    def include_rejection_reason(self, include_rejection_reason):
        """Sets the include_rejection_reason of this HarvesterIndexCreateRequest.

        If enabled, all harvesting errors (e.g. when the index rejects a payload due to non-matching schema) are stored as text in the index, which may be useful for later analysis.  # noqa: E501

        :param include_rejection_reason: The include_rejection_reason of this HarvesterIndexCreateRequest.  # noqa: E501
        :type: bool
        """

        self._include_rejection_reason = include_rejection_reason

    @property
    def retry_on_rejection(self):
        """Gets the retry_on_rejection of this HarvesterIndexCreateRequest.  # noqa: E501

        If enabled, all payloads rejected by the harvesting backend will be automatically analysed for offending data (e.g. fields that do not match the schema), pruned and submitted again. This might slow down the harvesting process and cause nonconformant metadata to be lost.  # noqa: E501

        :return: The retry_on_rejection of this HarvesterIndexCreateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._retry_on_rejection

    @retry_on_rejection.setter
    def retry_on_rejection(self, retry_on_rejection):
        """Sets the retry_on_rejection of this HarvesterIndexCreateRequest.

        If enabled, all payloads rejected by the harvesting backend will be automatically analysed for offending data (e.g. fields that do not match the schema), pruned and submitted again. This might slow down the harvesting process and cause nonconformant metadata to be lost.  # noqa: E501

        :param retry_on_rejection: The retry_on_rejection of this HarvesterIndexCreateRequest.  # noqa: E501
        :type: bool
        """

        self._retry_on_rejection = retry_on_rejection

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
        if issubclass(HarvesterIndexCreateRequest, dict):
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
        if not isinstance(other, HarvesterIndexCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
