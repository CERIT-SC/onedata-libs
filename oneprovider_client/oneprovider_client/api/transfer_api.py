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


class TransferApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_transfer(self, tid, **kwargs):  # noqa: E501
        """Cancel specific transfer  # noqa: E501

        Cancels a scheduled or active transfer. Returns 400 in case the transfer is already completed, canceled or failed.  This operation requires `space_cancel_replication` privilege in case of canceling replication, `space_cancel_eviction` privilege in case of canceling eviction and both of them when canceling migration.  However, canceling your own transfers does not require any privileges.  ***Example cURL requests***  **Cancel specific transfer** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/transfers/$TRANSFER_ID\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_transfer(tid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tid: Transfer Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_transfer_with_http_info(tid, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_transfer_with_http_info(tid, **kwargs)  # noqa: E501
            return data

    def cancel_transfer_with_http_info(self, tid, **kwargs):  # noqa: E501
        """Cancel specific transfer  # noqa: E501

        Cancels a scheduled or active transfer. Returns 400 in case the transfer is already completed, canceled or failed.  This operation requires `space_cancel_replication` privilege in case of canceling replication, `space_cancel_eviction` privilege in case of canceling eviction and both of them when canceling migration.  However, canceling your own transfers does not require any privileges.  ***Example cURL requests***  **Cancel specific transfer** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/transfers/$TRANSFER_ID\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_transfer_with_http_info(tid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tid: Transfer Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_transfer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tid' is set
        if ('tid' not in params or
                params['tid'] is None):
            raise ValueError("Missing the required parameter `tid` when calling `cancel_transfer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tid' in params:
            path_params['tid'] = params['tid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/transfers/{tid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_transfer(self, body, **kwargs):  # noqa: E501
        """Create transfer  # noqa: E501

        Creates transfer, which is a process of data movement between providers. This operation is asynchronous and it can take a long time depending on the size of the data to move.  The following types of transfer are supported: - `replication` - process of copying data to achieve a complete replica in provider   specified as `replicatingProviderId`. The data will be copied   from one or more providers in the space that hold replicas   or some fragments. This operation requires   `space_schedule_replication` privilege. - `eviction` - process of removing replica(s) from provider specified in `evictingProviderId`.   Eviction is safe - will succeed only if there is at least one   complete replica (accumulated) on other providers in the space.   This operation requires `space_schedule_eviction` privilege. - `migration` - `replication` followed by `eviction`. This operation requires both   `space_schedule_replication` and `space_schedule_eviction` privileges.  Each transfer applies to one or more files/directories, depending on chosen `dataSourceType`:   - file - a single chosen file or directory   - view - all files that are returned as a result of querying chosen view  In case of a directory, the transfer applies to all its subfiles and subdirectories (recursively).  ***Example cURL requests***  **Create file replication** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/transfers\" \\ -H \"Content-Type: application/json\" -d '{     \"type\": \"replication\",     \"replicatingProviderId\": \"'$PROVIDER_ID'\",     \"dataSourceType\": \"file\",     \"fileId\": \"'$FILE_ID'\" }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_transfer(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TransferCreateRequest body: Transfer properties. (required)
        :return: InlineResponse2012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_transfer_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_transfer_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_transfer_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create transfer  # noqa: E501

        Creates transfer, which is a process of data movement between providers. This operation is asynchronous and it can take a long time depending on the size of the data to move.  The following types of transfer are supported: - `replication` - process of copying data to achieve a complete replica in provider   specified as `replicatingProviderId`. The data will be copied   from one or more providers in the space that hold replicas   or some fragments. This operation requires   `space_schedule_replication` privilege. - `eviction` - process of removing replica(s) from provider specified in `evictingProviderId`.   Eviction is safe - will succeed only if there is at least one   complete replica (accumulated) on other providers in the space.   This operation requires `space_schedule_eviction` privilege. - `migration` - `replication` followed by `eviction`. This operation requires both   `space_schedule_replication` and `space_schedule_eviction` privileges.  Each transfer applies to one or more files/directories, depending on chosen `dataSourceType`:   - file - a single chosen file or directory   - view - all files that are returned as a result of querying chosen view  In case of a directory, the transfer applies to all its subfiles and subdirectories (recursively).  ***Example cURL requests***  **Create file replication** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/transfers\" \\ -H \"Content-Type: application/json\" -d '{     \"type\": \"replication\",     \"replicatingProviderId\": \"'$PROVIDER_ID'\",     \"dataSourceType\": \"file\",     \"fileId\": \"'$FILE_ID'\" }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_transfer_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TransferCreateRequest body: Transfer properties. (required)
        :return: InlineResponse2012
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
                    " to method create_transfer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_transfer`")  # noqa: E501

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
            '/transfers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_transfers(self, sid, **kwargs):  # noqa: E501
        """Get all space transfers  # noqa: E501

        Returns the list of all transfer IDs in a space with given state. The list is broken down into pages, each with length less or equal to the limit parameter. If the nextPageToken in the response has non-null value, there are more transfers to list - provide the token in the page_token parameter in the following request.  This operation requires `space_view_transfers` privilege.  ***Example cURL requests***  **List at most 3 ongoing transfers starting from page id 757136151113c2f** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/transfers?state=ongoing&limit=3&page_token=757136151113c2f\"  {     \"transfers\": [         \"2727a9fe5f5df6b43a8033386d2990e8ch5df6\",         \"4bd9b58f6387622bf07f7388945e4fc4ch8762\",         \"579a785181331e618b26980166b6ba2fch331e\"     ],     \"nextPageToken\": \"8471726779817b3a\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_transfers(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id in which to list transfers.  (required)
        :param str state: Specifies the state of transfers to list. The default is \"ongoing\". 
        :param int limit: Allows to limit the number of returned transfers. 
        :param str page_token: Allows to start the listing from a certain point, identified by the page token. 
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_transfers_with_http_info(sid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_all_transfers_with_http_info(sid, **kwargs)  # noqa: E501
            return data

    def get_all_transfers_with_http_info(self, sid, **kwargs):  # noqa: E501
        """Get all space transfers  # noqa: E501

        Returns the list of all transfer IDs in a space with given state. The list is broken down into pages, each with length less or equal to the limit parameter. If the nextPageToken in the response has non-null value, there are more transfers to list - provide the token in the page_token parameter in the following request.  This operation requires `space_view_transfers` privilege.  ***Example cURL requests***  **List at most 3 ongoing transfers starting from page id 757136151113c2f** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/transfers?state=ongoing&limit=3&page_token=757136151113c2f\"  {     \"transfers\": [         \"2727a9fe5f5df6b43a8033386d2990e8ch5df6\",         \"4bd9b58f6387622bf07f7388945e4fc4ch8762\",         \"579a785181331e618b26980166b6ba2fch331e\"     ],     \"nextPageToken\": \"8471726779817b3a\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_transfers_with_http_info(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id in which to list transfers.  (required)
        :param str state: Specifies the state of transfers to list. The default is \"ongoing\". 
        :param int limit: Allows to limit the number of returned transfers. 
        :param str page_token: Allows to start the listing from a certain point, identified by the page token. 
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sid', 'state', 'limit', 'page_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_transfers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `get_all_transfers`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sid' in params:
            path_params['sid'] = params['sid']  # noqa: E501

        query_params = []
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'page_token' in params:
            query_params.append(('page_token', params['page_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/spaces/{sid}/transfers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_transfer_status(self, tid, **kwargs):  # noqa: E501
        """Get transfer status  # noqa: E501

        Returns status of specific transfer.  This operation requires `space_view_transfers` privilege.  ***Example cURL requests***  **Get status of specific transfer** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/transfers/$TRANSFER_ID\"  {     \"type\": \"replication\",     \"userId\": \"admin\",     \"rerunId\": null,     \"effectiveJobTransferId\": $TRANSFER_ID,     \"spaceId\": \"6ec1a5413b6f4e2b01a5c85a8fd797e2\",     \"dataSourceType\": \"file\",     \"fileId\": \"00000000005CF4706775696423745F772D67686431633765446F4D76546D6F2D67575F3361737A7670486B477A7936587734507265584A7723394A4F355F5F396E4C31623031594576776E667431723230677767776C6B497031394E445F6E3868677873\",     \"filePath\": \"/space/tmp\",     \"transferStatus\": \"completed\",     \"effectiveJobStatus\": \"completed\",     \"replicationStatus\": \"completed\",     \"evictionStatus\": \"skipped\",     \"replicatingProviderId\": \"HICATChd8wzbFmB6qfGby9VN7MfdXgI1qC4pULGVm8Q\",     \"evictingProviderId\": null,     \"callback\": null,     \"filesToProcess\": 1,     \"filesProcessed\": 1,     \"filesReplicated\": 1,     \"filesEvicted\": 0,     \"filesFailed\": 0,     \"bytesReplicated\": 10485760000,     \"scheduleTime\": 1504688800,     \"startTime\": 15046888765,     \"finishTime\": 1504688814,     \"lastUpdate\": 1504988814,     \"minHist\": {         \"ASDxicvuisodr78w979879wer\": [419430400, 1153433600, 1258291200, 1468006400, 1048576000, 1048576000, 1048576000, 1153433600, 629145600, 1258291200, 0, 0, 0, 0, 0, 0, 0, 0, 0]     },     \"hrHist\": {         \"ASDxicvuisodr78w979879wer\": [10485760000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     },     \"dyHist\": {         \"ASDxicvuisodr78w979879wer\": [10485760000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     },     \"mthHist\": {         \"ASDxicvuisodr78w979879wer\": [10485760000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     } } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transfer_status(tid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tid: Transfer Id. (required)
        :return: TransferStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_transfer_status_with_http_info(tid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_transfer_status_with_http_info(tid, **kwargs)  # noqa: E501
            return data

    def get_transfer_status_with_http_info(self, tid, **kwargs):  # noqa: E501
        """Get transfer status  # noqa: E501

        Returns status of specific transfer.  This operation requires `space_view_transfers` privilege.  ***Example cURL requests***  **Get status of specific transfer** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/transfers/$TRANSFER_ID\"  {     \"type\": \"replication\",     \"userId\": \"admin\",     \"rerunId\": null,     \"effectiveJobTransferId\": $TRANSFER_ID,     \"spaceId\": \"6ec1a5413b6f4e2b01a5c85a8fd797e2\",     \"dataSourceType\": \"file\",     \"fileId\": \"00000000005CF4706775696423745F772D67686431633765446F4D76546D6F2D67575F3361737A7670486B477A7936587734507265584A7723394A4F355F5F396E4C31623031594576776E667431723230677767776C6B497031394E445F6E3868677873\",     \"filePath\": \"/space/tmp\",     \"transferStatus\": \"completed\",     \"effectiveJobStatus\": \"completed\",     \"replicationStatus\": \"completed\",     \"evictionStatus\": \"skipped\",     \"replicatingProviderId\": \"HICATChd8wzbFmB6qfGby9VN7MfdXgI1qC4pULGVm8Q\",     \"evictingProviderId\": null,     \"callback\": null,     \"filesToProcess\": 1,     \"filesProcessed\": 1,     \"filesReplicated\": 1,     \"filesEvicted\": 0,     \"filesFailed\": 0,     \"bytesReplicated\": 10485760000,     \"scheduleTime\": 1504688800,     \"startTime\": 15046888765,     \"finishTime\": 1504688814,     \"lastUpdate\": 1504988814,     \"minHist\": {         \"ASDxicvuisodr78w979879wer\": [419430400, 1153433600, 1258291200, 1468006400, 1048576000, 1048576000, 1048576000, 1153433600, 629145600, 1258291200, 0, 0, 0, 0, 0, 0, 0, 0, 0]     },     \"hrHist\": {         \"ASDxicvuisodr78w979879wer\": [10485760000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     },     \"dyHist\": {         \"ASDxicvuisodr78w979879wer\": [10485760000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     },     \"mthHist\": {         \"ASDxicvuisodr78w979879wer\": [10485760000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     } } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transfer_status_with_http_info(tid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tid: Transfer Id. (required)
        :return: TransferStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transfer_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tid' is set
        if ('tid' not in params or
                params['tid'] is None):
            raise ValueError("Missing the required parameter `tid` when calling `get_transfer_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tid' in params:
            path_params['tid'] = params['tid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/transfers/{tid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransferStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rerun_transfer(self, tid, **kwargs):  # noqa: E501
        """Rerun ended transfer  # noqa: E501

        Reruns ended transfer by creating a new, identical transfer.  This operation requires:   * `space_schedule_replication` when rerunning replication   * `space_schedule_eviction` when rerunning eviction   * `space_schedule_replication` and `space_schedule_eviction` when rerunning migration  Additionally, rerunning transfers using views requires `space_query_views` privilege.  ***Example cURL requests***  **Rerun finished transfer** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/transfers/$TRANSFER_ID/rerun\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rerun_transfer(tid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tid: Transfer Id. (required)
        :return: InlineResponse2013
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rerun_transfer_with_http_info(tid, **kwargs)  # noqa: E501
        else:
            (data) = self.rerun_transfer_with_http_info(tid, **kwargs)  # noqa: E501
            return data

    def rerun_transfer_with_http_info(self, tid, **kwargs):  # noqa: E501
        """Rerun ended transfer  # noqa: E501

        Reruns ended transfer by creating a new, identical transfer.  This operation requires:   * `space_schedule_replication` when rerunning replication   * `space_schedule_eviction` when rerunning eviction   * `space_schedule_replication` and `space_schedule_eviction` when rerunning migration  Additionally, rerunning transfers using views requires `space_query_views` privilege.  ***Example cURL requests***  **Rerun finished transfer** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/transfers/$TRANSFER_ID/rerun\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rerun_transfer_with_http_info(tid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tid: Transfer Id. (required)
        :return: InlineResponse2013
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rerun_transfer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tid' is set
        if ('tid' not in params or
                params['tid'] is None):
            raise ValueError("Missing the required parameter `tid` when calling `rerun_transfer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tid' in params:
            path_params['tid'] = params['tid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/transfers/{tid}/rerun', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2013',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
