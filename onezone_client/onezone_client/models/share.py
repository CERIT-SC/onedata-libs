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

class Share(object):
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
        'share_id': 'str',
        'name': 'str',
        'description': 'str',
        'public_url': 'str',
        'public_rest_url': 'str',
        'space_id': 'str',
        'root_file_id': 'str',
        'file_type': 'str',
        'handle_id': 'str',
        'creator': 'Subject',
        'creation_time': 'Timestamp'
    }

    attribute_map = {
        'share_id': 'shareId',
        'name': 'name',
        'description': 'description',
        'public_url': 'publicUrl',
        'public_rest_url': 'publicRestUrl',
        'space_id': 'spaceId',
        'root_file_id': 'rootFileId',
        'file_type': 'fileType',
        'handle_id': 'handleId',
        'creator': 'creator',
        'creation_time': 'creationTime'
    }

    def __init__(self, share_id=None, name=None, description=None, public_url=None, public_rest_url=None, space_id=None, root_file_id=None, file_type=None, handle_id=None, creator=None, creation_time=None):  # noqa: E501
        """Share - a model defined in Swagger"""  # noqa: E501
        self._share_id = None
        self._name = None
        self._description = None
        self._public_url = None
        self._public_rest_url = None
        self._space_id = None
        self._root_file_id = None
        self._file_type = None
        self._handle_id = None
        self._creator = None
        self._creation_time = None
        self.discriminator = None
        self.share_id = share_id
        self.name = name
        self.description = description
        self.public_url = public_url
        self.public_rest_url = public_rest_url
        if space_id is not None:
            self.space_id = space_id
        self.root_file_id = root_file_id
        self.file_type = file_type
        self.handle_id = handle_id
        if creator is not None:
            self.creator = creator
        self.creation_time = creation_time

    @property
    def share_id(self):
        """Gets the share_id of this Share.  # noqa: E501

        Share Id.  # noqa: E501

        :return: The share_id of this Share.  # noqa: E501
        :rtype: str
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        """Sets the share_id of this Share.

        Share Id.  # noqa: E501

        :param share_id: The share_id of this Share.  # noqa: E501
        :type: str
        """
        if share_id is None:
            raise ValueError("Invalid value for `share_id`, must not be `None`")  # noqa: E501

        self._share_id = share_id

    @property
    def name(self):
        """Gets the name of this Share.  # noqa: E501

        The name of the share.  # noqa: E501

        :return: The name of this Share.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Share.

        The name of the share.  # noqa: E501

        :param name: The name of this Share.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Share.  # noqa: E501

        Description of the share contents, interpreted as markdown format when displayed in GUI.  # noqa: E501

        :return: The description of this Share.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Share.

        Description of the share contents, interpreted as markdown format when displayed in GUI.  # noqa: E501

        :param description: The description of this Share.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def public_url(self):
        """Gets the public_url of this Share.  # noqa: E501

        Publicly accessible link that can be used to view the contents of the share in a web browser. Anyone with the link will be able to access the share browser, without any authentication.   # noqa: E501

        :return: The public_url of this Share.  # noqa: E501
        :rtype: str
        """
        return self._public_url

    @public_url.setter
    def public_url(self, public_url):
        """Sets the public_url of this Share.

        Publicly accessible link that can be used to view the contents of the share in a web browser. Anyone with the link will be able to access the share browser, without any authentication.   # noqa: E501

        :param public_url: The public_url of this Share.  # noqa: E501
        :type: str
        """
        if public_url is None:
            raise ValueError("Invalid value for `public_url`, must not be `None`")  # noqa: E501

        self._public_url = public_url

    @property
    def public_rest_url(self):
        """Gets the public_rest_url of this Share.  # noqa: E501

        URL to the publicly accessible REST endpoint, which can be used to programmatically access the share information and data. The endpoint does not require any authentication.   # noqa: E501

        :return: The public_rest_url of this Share.  # noqa: E501
        :rtype: str
        """
        return self._public_rest_url

    @public_rest_url.setter
    def public_rest_url(self, public_rest_url):
        """Sets the public_rest_url of this Share.

        URL to the publicly accessible REST endpoint, which can be used to programmatically access the share information and data. The endpoint does not require any authentication.   # noqa: E501

        :param public_rest_url: The public_rest_url of this Share.  # noqa: E501
        :type: str
        """
        if public_rest_url is None:
            raise ValueError("Invalid value for `public_rest_url`, must not be `None`")  # noqa: E501

        self._public_rest_url = public_rest_url

    @property
    def space_id(self):
        """Gets the space_id of this Share.  # noqa: E501

        The Id of the space in which the share was created. *Not included in public share details.*   # noqa: E501

        :return: The space_id of this Share.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this Share.

        The Id of the space in which the share was created. *Not included in public share details.*   # noqa: E501

        :param space_id: The space_id of this Share.  # noqa: E501
        :type: str
        """

        self._space_id = space_id

    @property
    def root_file_id(self):
        """Gets the root_file_id of this Share.  # noqa: E501

        Public Id of shared file or directory, allowing read access to its contents without authentication.  # noqa: E501

        :return: The root_file_id of this Share.  # noqa: E501
        :rtype: str
        """
        return self._root_file_id

    @root_file_id.setter
    def root_file_id(self, root_file_id):
        """Sets the root_file_id of this Share.

        Public Id of shared file or directory, allowing read access to its contents without authentication.  # noqa: E501

        :param root_file_id: The root_file_id of this Share.  # noqa: E501
        :type: str
        """
        if root_file_id is None:
            raise ValueError("Invalid value for `root_file_id`, must not be `None`")  # noqa: E501

        self._root_file_id = root_file_id

    @property
    def file_type(self):
        """Gets the file_type of this Share.  # noqa: E501

        Denotes the type of the shared element (file or directory)  # noqa: E501

        :return: The file_type of this Share.  # noqa: E501
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this Share.

        Denotes the type of the shared element (file or directory)  # noqa: E501

        :param file_type: The file_type of this Share.  # noqa: E501
        :type: str
        """
        if file_type is None:
            raise ValueError("Invalid value for `file_type`, must not be `None`")  # noqa: E501
        allowed_values = ["file", "dir"]  # noqa: E501
        if file_type not in allowed_values:
            raise ValueError(
                "Invalid value for `file_type` ({0}), must be one of {1}"  # noqa: E501
                .format(file_type, allowed_values)
            )

        self._file_type = file_type

    @property
    def handle_id(self):
        """Gets the handle_id of this Share.  # noqa: E501

        The Id of open data Handle (e.g. DOI or PID) assigned to this share or null.  # noqa: E501

        :return: The handle_id of this Share.  # noqa: E501
        :rtype: str
        """
        return self._handle_id

    @handle_id.setter
    def handle_id(self, handle_id):
        """Sets the handle_id of this Share.

        The Id of open data Handle (e.g. DOI or PID) assigned to this share or null.  # noqa: E501

        :param handle_id: The handle_id of this Share.  # noqa: E501
        :type: str
        """
        if handle_id is None:
            raise ValueError("Invalid value for `handle_id`, must not be `None`")  # noqa: E501

        self._handle_id = handle_id

    @property
    def creator(self):
        """Gets the creator of this Share.  # noqa: E501


        :return: The creator of this Share.  # noqa: E501
        :rtype: Subject
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this Share.


        :param creator: The creator of this Share.  # noqa: E501
        :type: Subject
        """

        self._creator = creator

    @property
    def creation_time(self):
        """Gets the creation_time of this Share.  # noqa: E501


        :return: The creation_time of this Share.  # noqa: E501
        :rtype: Timestamp
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this Share.


        :param creation_time: The creation_time of this Share.  # noqa: E501
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
        if issubclass(Share, dict):
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
        if not isinstance(other, Share):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
