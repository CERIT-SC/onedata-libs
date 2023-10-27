# coding: utf-8

"""
    Oneprovider

    # Overview  This is the RESTful API definition of Oneprovider component of Onedata data management system [onedata.org](http://onedata.org).  > This API is defined using [Swagger](http://swagger.io/), the JSON specification can be used to automatically generate > client libraries - [swagger.json](../../../swagger/oneprovider/swagger.json).  All paths below are relative to a common Oneprovider basepath which is `/api/v3/oneprovider`, thus a complete example query for 'mode' file attributes would be: ``` https://ONEPROVIDER_HOSTNAME/api/v3/oneprovider/data/$FILE_ID?attribute=mode ``` Please note that currently the default port for Oneprovider instances is `443`.  In addition to REST API, Oneprovider also provides support for [CDMI](http://onedata.org/#/home/documentation/doc/advanced/cdmi.html) protocol.   ## Authentication To use the APIs, the REST client must authenticate with the Oneprovider service and present a proof of authorization to perform a specific operation. This is done using access tokens, which can be generated using the Onedata GUI or Onezone's REST API.  The token is passed in the request header like this: ``` X-Auth-Token: MIIFrzCCA5egAwIBAgIBEzANBgkqhkiG9w0BAQUFADBcMQswCQYDVQQGEwJQTDET... ```  The authorization to perform a specific operation depends on the authenticated user's privileges in the corresponding space, file level permissions (posix, ACL) and caveats (restrictions) inscribed in the provided access token.   ## Data management basics The Onedata system organizes all user data into logical containers called spaces. <!--- TODO VFS-7218 uncomment when the new docs are deployed --> <!--- For more information, please refer to the [documentation](https://onedata.org/#/home/documentation). -->  Files and directories in Onedata can be globally identified using unique File Ids or logical paths. Whenever possible, it is recommended to use File Ids, due to better performance and no need for escaping or encoding.  ### File path All logical paths in Onedata use the slash (`/`) delimiter and must start with a space name: ```lang-none /CMS 1/file.txt /MyExperiment/directory/subdirectory/image.jpg ```  When referencing files by path in the REST API, make sure to urlencode the path in the URL: ```bash {...}/CMS%201/file.txt ```  ### File Id  File Id is a unique, global identifier associated with a file or directory and can be used universally in the REST and CDMI APIs. There are several ways to find out the File Id of given file or directory: <!---  @TODO VFS-7218 remove redundant information and provide a link to the new docs -->  **Web GUI** - click on Information in the file/directory context menu and look for File Id.  **REST API** - use the File Id resolution endpoint. Below example returns the File Id of `/CMS 1/file.txt`, where `CMS 1` is the space name:  ```bash curl -H \"X-Auth-Token: ${ACCESS_TOKEN}\" \\ -X POST \"https://${ONEPROVIDER_DOMAIN}/api/v3/oneprovider/lookup-file-id/CMS%201/file.txt\" {     \"fileId\": \"094576776E667431723230677767776C6B497031394E445F6E3868677873...\" } ```  ### Space Id  Space Id is a unique, global identifier associated with a space and can be used universally in the REST APIs. In order to find out the Space Id:  **Web GUI** - click on Information in the file/directory context menu and look for Space Id.  **REST API** - use the [Get all user spaces](#operation/get_all_spaces) endpoint.  The Space Id can be used interchangeably with the space root directory's File Id in the path-based enpoints.  **Remove specific file relative to the space root** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_ID/path/dir1/file.txt\" # is equivalent to curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$SPACE_ROOT_FILE_ID/path/dir1/file.txt\" ``` **Remove specific file relative to any parent directory** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$PARENT_FILE_ID/path/dir1/file.txt\" ```   ## API structure  The API is divided into the following sections:  ### Space management These methods provide means for getting basic information about spaces directly from the Oneprovider service, but also allows to define database views.  ### File access and management The API provides capabilities for:   - browsing files in spaces and directories,   - creating and deleting files as well as updating their content   - querying for file attributes, such as 'mode' file permissions and updating them,   - managing custom file metadata (xattrs, JSON, RDF),   - manual registration of files for imported storages.  More information can be found [here](#section/Overview/Data-management-basics).  ### Replica and QoS management These methods allow viewing file replica distribution, requesting file replication (transfers) between Oneproviders, viewing ongoing and historical transfers data, as well as managing QoS requirements that trigger automatic replication according to the QoS rules.  ### Share management Offers methods for creating, modyfying and deleting shares. Shares are files or directories that were made publicly available, so that they can be viewed by everyone through a public URL.  ### Dataset & archive management API for managing datasets - designated files or directories that are used to facilitate building collections of data meaningful for the users with additional features, such as write protection and archivisation mechanisms.  ### Automation Basic API for scheduling and viewing workflow executions.  ### Monitoring The API provides means for subscribing (through HTTP long-polling technique) for file related events such as reads, writes or deletes which are returned as complete file metadata records with sequence numbers representing their current version.  ### Service information Publicly available, basic configuration of the Oneprovider service.  Detailed examples of API usage are available in the documentation of each operation.   # noqa: E501

    OpenAPI spec version: 21.02.3
    Contact: info@onedata.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from oneprovider_client.api_client import ApiClient


class MiscellaneousApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_directory_size_stats(self, body, id, **kwargs):  # noqa: E501
        """Get directory size statistics  # noqa: E501

        Retrieves historical size statistics over time for a directory. The response includes only the information pertaining to the queried provider; in order to collect globally-complete statistics, all providers supporting the space must be queried. There may be discrepancies in statistics such as logical size of data, which stem from synchronization delays between providers.  Size statistics over time are available only for directories. They are collected hierarchically i.e. for a  certain directory, its statistics are a sum of statistics for the directory (regarding its direct children), and the statistics from all its subdirectories. Additionally, size statistics for the space directory encompass relevant information from archives.  **This endpoint requires the size statistics to be enabled for the containing space on the queried provider.** Otherwise, an adequate error will be returned.  Two request modes are supported:    * `layout` - returns information about the structure of stats collection,  i.e. the names of the available time series and metrics within them   * `slice` - returns a slice of statistics as a collection of slices of  requested time series and metrics  The following time series are available for each directory:   * `total_size` - the total logical size of file data contained in the directory,  i.e. the sum of logical byte sizes of all regular files.   * `storage_use_$STORAGE_ID` - storage size used to store the physical data of the contained files for given `$STORAGE_ID`. Only the storage backends owned by the queried providers are returned.   * `reg_file_and_link_count` - the count of regular files, hardlinks,  and symbolic links contained in the directory.   * `dir_count` - the count of directories contained in the directory.   * `file_errors_count` - the count of error occurrences when the statistics  mechanisms were not able to gather size information about a certain file.   * `dir_errors_count` - like above, for directories.  If the values of `file_errors_count` or `dir_errors_count` are not zero, the statistics may not be accurate.  The following metrics are available for each time series: `day`, `hour`, `minute`, `month`.  ***Example cURL requests***  **Get the layout of directory size statistics**     ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$DIR_ID/dir_size_stats\" \\ -H \"Content-Type: application/json\" -d '{     \"mode\": \"layout\"   }'  {     \"layout\": {         \"total_size\": [             \"day\",             \"hour\",             \"minute\",             \"month\"         ],         \"storage_use_7ab46e96fdb27a2694493c2c5bd7491dch8f55\": [...],         \"reg_file_and_link_count\": [...],         \"file_errors_count\": [...],         \"dir_errors_count\": [...],         \"dir_count\": [...]     } } ```  **Get a slice of directory size statistics**     ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$DIR_ID/dir_size_stats\" \\ -H \"Content-Type: application/json\" -d '{     \"mode\": \"slice\",     \"extendedInfo\": true,     \"layout\": {         \"total_size\": [             \"minute\"         ],         \"storage_use_7ab46e96fdb27a2694493c2c5bd7491dch8f55\": [             \"minute\"         ]     },     \"startTimestamp\": 1687513285,     \"stopTimestamp\": 1687499802,     \"windowLimit\": 31 }'  {     \"slice\": {         \"total_size\": {             \"minute\": [                 {                     \"value\": 883365,                     \"timestamp\": 1687513260,                     \"lastMeasurementTimestamp\": 1687513287,                     \"firstMeasurementTimestamp\": 1687513287                 },                 ...             ]         },         \"storage_use_7ab46e96fdb27a2694493c2c5bd7491dch8f55\": {             \"minute\": [                 {                     \"value\": 56280,                     \"timestamp\": 1687513260,                     \"lastMeasurementTimestamp\": 1687513287,                     \"firstMeasurementTimestamp\": 1687513287                 },                 ...             ]         }     } }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_directory_size_stats(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DirSizeStatsQuery body: Query body. (required)
        :param str id: Directory Id  (required)
        :return: DirSizeStatsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_directory_size_stats_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_directory_size_stats_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def get_directory_size_stats_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Get directory size statistics  # noqa: E501

        Retrieves historical size statistics over time for a directory. The response includes only the information pertaining to the queried provider; in order to collect globally-complete statistics, all providers supporting the space must be queried. There may be discrepancies in statistics such as logical size of data, which stem from synchronization delays between providers.  Size statistics over time are available only for directories. They are collected hierarchically i.e. for a  certain directory, its statistics are a sum of statistics for the directory (regarding its direct children), and the statistics from all its subdirectories. Additionally, size statistics for the space directory encompass relevant information from archives.  **This endpoint requires the size statistics to be enabled for the containing space on the queried provider.** Otherwise, an adequate error will be returned.  Two request modes are supported:    * `layout` - returns information about the structure of stats collection,  i.e. the names of the available time series and metrics within them   * `slice` - returns a slice of statistics as a collection of slices of  requested time series and metrics  The following time series are available for each directory:   * `total_size` - the total logical size of file data contained in the directory,  i.e. the sum of logical byte sizes of all regular files.   * `storage_use_$STORAGE_ID` - storage size used to store the physical data of the contained files for given `$STORAGE_ID`. Only the storage backends owned by the queried providers are returned.   * `reg_file_and_link_count` - the count of regular files, hardlinks,  and symbolic links contained in the directory.   * `dir_count` - the count of directories contained in the directory.   * `file_errors_count` - the count of error occurrences when the statistics  mechanisms were not able to gather size information about a certain file.   * `dir_errors_count` - like above, for directories.  If the values of `file_errors_count` or `dir_errors_count` are not zero, the statistics may not be accurate.  The following metrics are available for each time series: `day`, `hour`, `minute`, `month`.  ***Example cURL requests***  **Get the layout of directory size statistics**     ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$DIR_ID/dir_size_stats\" \\ -H \"Content-Type: application/json\" -d '{     \"mode\": \"layout\"   }'  {     \"layout\": {         \"total_size\": [             \"day\",             \"hour\",             \"minute\",             \"month\"         ],         \"storage_use_7ab46e96fdb27a2694493c2c5bd7491dch8f55\": [...],         \"reg_file_and_link_count\": [...],         \"file_errors_count\": [...],         \"dir_errors_count\": [...],         \"dir_count\": [...]     } } ```  **Get a slice of directory size statistics**     ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/data/$DIR_ID/dir_size_stats\" \\ -H \"Content-Type: application/json\" -d '{     \"mode\": \"slice\",     \"extendedInfo\": true,     \"layout\": {         \"total_size\": [             \"minute\"         ],         \"storage_use_7ab46e96fdb27a2694493c2c5bd7491dch8f55\": [             \"minute\"         ]     },     \"startTimestamp\": 1687513285,     \"stopTimestamp\": 1687499802,     \"windowLimit\": 31 }'  {     \"slice\": {         \"total_size\": {             \"minute\": [                 {                     \"value\": 883365,                     \"timestamp\": 1687513260,                     \"lastMeasurementTimestamp\": 1687513287,                     \"firstMeasurementTimestamp\": 1687513287                 },                 ...             ]         },         \"storage_use_7ab46e96fdb27a2694493c2c5bd7491dch8f55\": {             \"minute\": [                 {                     \"value\": 56280,                     \"timestamp\": 1687513260,                     \"lastMeasurementTimestamp\": 1687513287,                     \"firstMeasurementTimestamp\": 1687513287                 },                 ...             ]         }     } }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_directory_size_stats_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DirSizeStatsQuery body: Query body. (required)
        :param str id: Directory Id  (required)
        :return: DirSizeStatsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_directory_size_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `get_directory_size_stats`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_directory_size_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}/dir_size_stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirSizeStatsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def register_file(self, body, **kwargs):  # noqa: E501
        """Register file  # noqa: E501

        Registers a file located on an `imported storage`. This operation is available only in spaces supported with `imported storages` with `manual import mode` enabled. In such setup, the files existing on the storage are not automatically visible in the space and must be registered manually by the space users - [learn more](https://onedata.org/#/home/documentation/stable/doc/using_onedata/file-registration.html).  The operation creates the necessary metadata for the file and registers its physical location on the storage in Onedata, which makes the file visible and accessible within the space. The metadata can be provided explicitly by the registering user, or an automatic detection will be performed (although not all storage backends support the required `stat` operation or equivalent - in such case some metadata must be provided for the operation to succeed).  The registration of the same file can be repeated, which updates the previous metadata with the new information. In most cases, the metadata is overwritten with new values, with exception of xattrs - previous values are merged with new ones.  This operation requires:   * space_register_file privilege  ***Example cURL requests***  **Register file** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/data/register\" \\ -H 'Content-Type: application/json' -d \"@./file_spec.json\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register_file(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FileRegistrationRequest body: Specification of a file to be registered. (required)
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.register_file_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.register_file_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def register_file_with_http_info(self, body, **kwargs):  # noqa: E501
        """Register file  # noqa: E501

        Registers a file located on an `imported storage`. This operation is available only in spaces supported with `imported storages` with `manual import mode` enabled. In such setup, the files existing on the storage are not automatically visible in the space and must be registered manually by the space users - [learn more](https://onedata.org/#/home/documentation/stable/doc/using_onedata/file-registration.html).  The operation creates the necessary metadata for the file and registers its physical location on the storage in Onedata, which makes the file visible and accessible within the space. The metadata can be provided explicitly by the registering user, or an automatic detection will be performed (although not all storage backends support the required `stat` operation or equivalent - in such case some metadata must be provided for the operation to succeed).  The registration of the same file can be repeated, which updates the previous metadata with the new information. In most cases, the metadata is overwritten with new values, with exception of xattrs - previous values are merged with new ones.  This operation requires:   * space_register_file privilege  ***Example cURL requests***  **Register file** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/data/register\" \\ -H 'Content-Type: application/json' -d \"@./file_spec.json\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register_file_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FileRegistrationRequest body: Specification of a file to be registered. (required)
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method register_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `register_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/data/register', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2011',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
