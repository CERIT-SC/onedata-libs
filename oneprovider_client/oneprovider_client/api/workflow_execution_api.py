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


class WorkflowExecutionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_workflow_execution(self, wid, **kwargs):  # noqa: E501
        """Cancel workflow execution  # noqa: E501

        Cancels scheduled, ongoing or suspended workflow execution.  This operation requires `space_schedule_atm_workflow_executions` when invoked by scheduling user, or `space_manage_atm_workflow_executions`  otherwise.  ***Example cURL requests***  **Cancel workflow execution** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID/cancel\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_workflow_execution(wid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wid: Workflow execution Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_workflow_execution_with_http_info(wid, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_workflow_execution_with_http_info(wid, **kwargs)  # noqa: E501
            return data

    def cancel_workflow_execution_with_http_info(self, wid, **kwargs):  # noqa: E501
        """Cancel workflow execution  # noqa: E501

        Cancels scheduled, ongoing or suspended workflow execution.  This operation requires `space_schedule_atm_workflow_executions` when invoked by scheduling user, or `space_manage_atm_workflow_executions`  otherwise.  ***Example cURL requests***  **Cancel workflow execution** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID/cancel\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_workflow_execution_with_http_info(wid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wid: Workflow execution Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_workflow_execution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'wid' is set
        if ('wid' not in params or
                params['wid'] is None):
            raise ValueError("Missing the required parameter `wid` when calling `cancel_workflow_execution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'wid' in params:
            path_params['wid'] = params['wid']  # noqa: E501

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
            '/automation/execution/workflows/{wid}/cancel', 'POST',
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

    def delete_workflow_execution(self, wid, **kwargs):  # noqa: E501
        """Delete workflow execution  # noqa: E501

        Deletes stopped workflow execution.  This operation requires `space_schedule_atm_workflow_executions` when invoked by scheduling user, or `space_manage_atm_workflow_executions`  otherwise.  ***Example cURL requests***  **Delete workflow execution details** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_workflow_execution(wid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wid: Workflow execution Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_workflow_execution_with_http_info(wid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_workflow_execution_with_http_info(wid, **kwargs)  # noqa: E501
            return data

    def delete_workflow_execution_with_http_info(self, wid, **kwargs):  # noqa: E501
        """Delete workflow execution  # noqa: E501

        Deletes stopped workflow execution.  This operation requires `space_schedule_atm_workflow_executions` when invoked by scheduling user, or `space_manage_atm_workflow_executions`  otherwise.  ***Example cURL requests***  **Delete workflow execution details** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X DELETE \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_workflow_execution_with_http_info(wid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wid: Workflow execution Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workflow_execution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'wid' is set
        if ('wid' not in params or
                params['wid'] is None):
            raise ValueError("Missing the required parameter `wid` when calling `delete_workflow_execution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'wid' in params:
            path_params['wid'] = params['wid']  # noqa: E501

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
            '/automation/execution/workflows/{wid}', 'DELETE',
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

    def force_continue_workflow_execution(self, wid, **kwargs):  # noqa: E501
        """Force continue workflow execution  # noqa: E501

        Forcefully proceeds with a failed execution, commencing from the subsequent  lane to the one that failed.  This operation requires `space_schedule_atm_workflow_executions` when invoked by scheduling user, or `space_manage_atm_workflow_executions`  otherwise.  ***Example cURL requests***  **Force continue workflow execution** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID/force_continue\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.force_continue_workflow_execution(wid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wid: Workflow execution Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.force_continue_workflow_execution_with_http_info(wid, **kwargs)  # noqa: E501
        else:
            (data) = self.force_continue_workflow_execution_with_http_info(wid, **kwargs)  # noqa: E501
            return data

    def force_continue_workflow_execution_with_http_info(self, wid, **kwargs):  # noqa: E501
        """Force continue workflow execution  # noqa: E501

        Forcefully proceeds with a failed execution, commencing from the subsequent  lane to the one that failed.  This operation requires `space_schedule_atm_workflow_executions` when invoked by scheduling user, or `space_manage_atm_workflow_executions`  otherwise.  ***Example cURL requests***  **Force continue workflow execution** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID/force_continue\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.force_continue_workflow_execution_with_http_info(wid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wid: Workflow execution Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method force_continue_workflow_execution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'wid' is set
        if ('wid' not in params or
                params['wid'] is None):
            raise ValueError("Missing the required parameter `wid` when calling `force_continue_workflow_execution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'wid' in params:
            path_params['wid'] = params['wid']  # noqa: E501

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
            '/automation/execution/workflows/{wid}/force_continue', 'POST',
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

    def get_workflow_execution_details(self, wid, **kwargs):  # noqa: E501
        """Get workflow execution details  # noqa: E501

        Returns the details of a specific workflow execution.  This operation requires `space_view_atm_workflow_executions` privilege and the requesting user must belong to the automation inventory containing the corresponding workflow schema definition.  ***Example cURL requests***  **Get workflow execution details** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID\"  {     \"atmWorkflowExecutionId\": \"11a53ed06d175c89bc3ed5be61f8217cch1890\",     \"atmWorkflowSchemaSnapshotId\": \"821711ad53ed06be61f175c89bc3ed5cch1890\",     \"name\": \"test execution\",     \"atmInventoryId\": \"2d180796daafcf15d586d29dd13dae48chd5fc\",     \"spaceId\": \"c17147cc3188408c26f522881282cb83ch9853\",     \"userId\": \"08c26cc228812c3188417147f582cb83ch9853\",     \"status\": \"enqueued\",     \"scheduleTime\": 1626107063,     \"startTime\": 0,     \"suspendTime\": 0,     \"finishTime\": 0,     \"lambdaSnapshotRegistry\": {         \"e412848d415329d81b7edd15c80b7740chf93f\": \"3946496fb29e3cf3faa96dbbd58d42d9ch9e3c\"     },     \"storeRegistry\": {         \"216a5de15ba9f8f3138168682c3da954212abf\": \"805392e2b84fb7e6ff5b31b4b7e70845ch1995\"     },     \"systemAuditLogStoreId\": \"1439ca4dee1a251483923f4535bca500e72f2a\",     \"lanes\": [         {             \"schemaId\": \"3a1a829f714a41b043c4ce67402d8c136f125f\",             \"runs\": [                 {                     \"runNumber\": 3,                     \"originRunNumber\": 1,                     \"runType\": \"retry\",                     \"status\": \"pending\",                     \"iteratedStoreId\": \"1b502545a3f9faa7f1e339f4aea793117be91d\",                     \"exceptionStoreId\": \"98c669ec69c0394a38391c0ab0117f67ch260d\",                     \"parallelBoxes\": [                         {                             \"taskRegistry\": {                                 \"d92b861a5edfb08b920e0e80f4670a87f48176\": \"1697f7c1f46e0e22bb426bead5a3cb47chda3d\"                             },                             \"schemaId\": \"0068146d662adc878f699bf82af08b9ddbd9ab\"                         }                     ],                     \"isRetriable\": false,                     \"isRerunable\": false                 },                 ...             ]         }     ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workflow_execution_details(wid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wid: Workflow execution Id. (required)
        :return: AtmWorkflowExecutionDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_workflow_execution_details_with_http_info(wid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_workflow_execution_details_with_http_info(wid, **kwargs)  # noqa: E501
            return data

    def get_workflow_execution_details_with_http_info(self, wid, **kwargs):  # noqa: E501
        """Get workflow execution details  # noqa: E501

        Returns the details of a specific workflow execution.  This operation requires `space_view_atm_workflow_executions` privilege and the requesting user must belong to the automation inventory containing the corresponding workflow schema definition.  ***Example cURL requests***  **Get workflow execution details** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID\"  {     \"atmWorkflowExecutionId\": \"11a53ed06d175c89bc3ed5be61f8217cch1890\",     \"atmWorkflowSchemaSnapshotId\": \"821711ad53ed06be61f175c89bc3ed5cch1890\",     \"name\": \"test execution\",     \"atmInventoryId\": \"2d180796daafcf15d586d29dd13dae48chd5fc\",     \"spaceId\": \"c17147cc3188408c26f522881282cb83ch9853\",     \"userId\": \"08c26cc228812c3188417147f582cb83ch9853\",     \"status\": \"enqueued\",     \"scheduleTime\": 1626107063,     \"startTime\": 0,     \"suspendTime\": 0,     \"finishTime\": 0,     \"lambdaSnapshotRegistry\": {         \"e412848d415329d81b7edd15c80b7740chf93f\": \"3946496fb29e3cf3faa96dbbd58d42d9ch9e3c\"     },     \"storeRegistry\": {         \"216a5de15ba9f8f3138168682c3da954212abf\": \"805392e2b84fb7e6ff5b31b4b7e70845ch1995\"     },     \"systemAuditLogStoreId\": \"1439ca4dee1a251483923f4535bca500e72f2a\",     \"lanes\": [         {             \"schemaId\": \"3a1a829f714a41b043c4ce67402d8c136f125f\",             \"runs\": [                 {                     \"runNumber\": 3,                     \"originRunNumber\": 1,                     \"runType\": \"retry\",                     \"status\": \"pending\",                     \"iteratedStoreId\": \"1b502545a3f9faa7f1e339f4aea793117be91d\",                     \"exceptionStoreId\": \"98c669ec69c0394a38391c0ab0117f67ch260d\",                     \"parallelBoxes\": [                         {                             \"taskRegistry\": {                                 \"d92b861a5edfb08b920e0e80f4670a87f48176\": \"1697f7c1f46e0e22bb426bead5a3cb47chda3d\"                             },                             \"schemaId\": \"0068146d662adc878f699bf82af08b9ddbd9ab\"                         }                     ],                     \"isRetriable\": false,                     \"isRerunable\": false                 },                 ...             ]         }     ] } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workflow_execution_details_with_http_info(wid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wid: Workflow execution Id. (required)
        :return: AtmWorkflowExecutionDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workflow_execution_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'wid' is set
        if ('wid' not in params or
                params['wid'] is None):
            raise ValueError("Missing the required parameter `wid` when calling `get_workflow_execution_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'wid' in params:
            path_params['wid'] = params['wid']  # noqa: E501

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
            '/automation/execution/workflows/{wid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AtmWorkflowExecutionDetails',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_workflow_executions(self, sid, **kwargs):  # noqa: E501
        """List workflow executions  # noqa: E501

        Returns the list of workflow execution Ids with given phase within a space. The list will include only workflow executions based on schemas from  inventories to which user has access.  This operation requires `space_view_atm_workflow_executions` privilege.  ***Example cURL requests***  **List at most 3 ongoing workflow executions starting from page id 757136151113c2f** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/automation/execution/workflows?phase=ongoing&limit=3&token=757136151113c2f\"  {     \"atmWorkflowExecutions\": [         \"2727a9fe5f5df6b43a8033386d2990e8ch5df6\",         \"4bd9b58f6387622bf07f7388945e4fc4ch8762\",         \"579a785181331e618b26980166b6ba2fch331e\"     ],     \"isLast\": false,     \"nextPageToken\": \"8471726779817b3a\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_workflow_executions(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id in which to list workflow executions.  (required)
        :param str phase: Specifies the phase of workflow executions to list.
        :param int limit: Allows specifying maximum number of entries that should be returned.  If there are more workflow executions, they can be retrieved using  `offset` or `token` query parameters. 
        :param int offset: Offset determining beginning of the list of workflow executions returned  in the response. Expressed in number of entries, further adjusts the  starting point of listing indicated by `token` parameter. The value can be negative, in such case entries preceding the starting  point will be returned. 
        :param str token: Determines the starting point for listing. The listing will start from  the next page (batch) of entries which follows the page previously  obtained along with the corresponding `nextPageToken`. 
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_workflow_executions_with_http_info(sid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_workflow_executions_with_http_info(sid, **kwargs)  # noqa: E501
            return data

    def list_workflow_executions_with_http_info(self, sid, **kwargs):  # noqa: E501
        """List workflow executions  # noqa: E501

        Returns the list of workflow execution Ids with given phase within a space. The list will include only workflow executions based on schemas from  inventories to which user has access.  This operation requires `space_view_atm_workflow_executions` privilege.  ***Example cURL requests***  **List at most 3 ongoing workflow executions starting from page id 757136151113c2f** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X GET \"https://$PROVIDER_HOST/api/v3/oneprovider/spaces/$SPACE_ID/automation/execution/workflows?phase=ongoing&limit=3&token=757136151113c2f\"  {     \"atmWorkflowExecutions\": [         \"2727a9fe5f5df6b43a8033386d2990e8ch5df6\",         \"4bd9b58f6387622bf07f7388945e4fc4ch8762\",         \"579a785181331e618b26980166b6ba2fch331e\"     ],     \"isLast\": false,     \"nextPageToken\": \"8471726779817b3a\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_workflow_executions_with_http_info(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: Space Id in which to list workflow executions.  (required)
        :param str phase: Specifies the phase of workflow executions to list.
        :param int limit: Allows specifying maximum number of entries that should be returned.  If there are more workflow executions, they can be retrieved using  `offset` or `token` query parameters. 
        :param int offset: Offset determining beginning of the list of workflow executions returned  in the response. Expressed in number of entries, further adjusts the  starting point of listing indicated by `token` parameter. The value can be negative, in such case entries preceding the starting  point will be returned. 
        :param str token: Determines the starting point for listing. The listing will start from  the next page (batch) of entries which follows the page previously  obtained along with the corresponding `nextPageToken`. 
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sid', 'phase', 'limit', 'offset', 'token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_workflow_executions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `list_workflow_executions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sid' in params:
            path_params['sid'] = params['sid']  # noqa: E501

        query_params = []
        if 'phase' in params:
            query_params.append(('phase', params['phase']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501

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
            '/spaces/{sid}/automation/execution/workflows', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pause_workflow_execution(self, wid, **kwargs):  # noqa: E501
        """Pause workflow execution  # noqa: E501

        Pauses scheduled or ongoing workflow execution.  This operation requires `space_schedule_atm_workflow_executions` when invoked by scheduling user, or `space_manage_atm_workflow_executions`  otherwise.  ***Example cURL requests***  **Pause workflow execution** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID/pause\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pause_workflow_execution(wid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wid: Workflow execution Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pause_workflow_execution_with_http_info(wid, **kwargs)  # noqa: E501
        else:
            (data) = self.pause_workflow_execution_with_http_info(wid, **kwargs)  # noqa: E501
            return data

    def pause_workflow_execution_with_http_info(self, wid, **kwargs):  # noqa: E501
        """Pause workflow execution  # noqa: E501

        Pauses scheduled or ongoing workflow execution.  This operation requires `space_schedule_atm_workflow_executions` when invoked by scheduling user, or `space_manage_atm_workflow_executions`  otherwise.  ***Example cURL requests***  **Pause workflow execution** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID/pause\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pause_workflow_execution_with_http_info(wid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wid: Workflow execution Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pause_workflow_execution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'wid' is set
        if ('wid' not in params or
                params['wid'] is None):
            raise ValueError("Missing the required parameter `wid` when calling `pause_workflow_execution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'wid' in params:
            path_params['wid'] = params['wid']  # noqa: E501

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
            '/automation/execution/workflows/{wid}/pause', 'POST',
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

    def rerun_workflow_execution(self, body, wid, **kwargs):  # noqa: E501
        """Rerun workflow execution  # noqa: E501

        Reruns stopped workflow execution starting from specified lane run.  This operation requires `space_schedule_atm_workflow_executions` when invoked by scheduling user, or `space_manage_atm_workflow_executions`  otherwise.  ***Example cURL requests***  **Rerun workflow execution** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID/rerun\" -H \"Content-Type: application/json\" -d '{     \"laneIndex\": 2,     \"laneRunNumber\": 3 }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rerun_workflow_execution(body, wid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WidRerunBody body: Lane run reference. (required)
        :param str wid: Workflow execution Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rerun_workflow_execution_with_http_info(body, wid, **kwargs)  # noqa: E501
        else:
            (data) = self.rerun_workflow_execution_with_http_info(body, wid, **kwargs)  # noqa: E501
            return data

    def rerun_workflow_execution_with_http_info(self, body, wid, **kwargs):  # noqa: E501
        """Rerun workflow execution  # noqa: E501

        Reruns stopped workflow execution starting from specified lane run.  This operation requires `space_schedule_atm_workflow_executions` when invoked by scheduling user, or `space_manage_atm_workflow_executions`  otherwise.  ***Example cURL requests***  **Rerun workflow execution** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID/rerun\" -H \"Content-Type: application/json\" -d '{     \"laneIndex\": 2,     \"laneRunNumber\": 3 }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rerun_workflow_execution_with_http_info(body, wid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WidRerunBody body: Lane run reference. (required)
        :param str wid: Workflow execution Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'wid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rerun_workflow_execution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `rerun_workflow_execution`")  # noqa: E501
        # verify the required parameter 'wid' is set
        if ('wid' not in params or
                params['wid'] is None):
            raise ValueError("Missing the required parameter `wid` when calling `rerun_workflow_execution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'wid' in params:
            path_params['wid'] = params['wid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/automation/execution/workflows/{wid}/rerun', 'POST',
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

    def resume_workflow_execution(self, wid, **kwargs):  # noqa: E501
        """Resume workflow execution  # noqa: E501

        Resumes suspended (either paused or interrupted) workflow execution.  This operation requires `space_schedule_atm_workflow_executions` when invoked by scheduling user, or `space_manage_atm_workflow_executions`  otherwise.  ***Example cURL requests***  **Resume workflow execution** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID/resume\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resume_workflow_execution(wid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wid: Workflow execution Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.resume_workflow_execution_with_http_info(wid, **kwargs)  # noqa: E501
        else:
            (data) = self.resume_workflow_execution_with_http_info(wid, **kwargs)  # noqa: E501
            return data

    def resume_workflow_execution_with_http_info(self, wid, **kwargs):  # noqa: E501
        """Resume workflow execution  # noqa: E501

        Resumes suspended (either paused or interrupted) workflow execution.  This operation requires `space_schedule_atm_workflow_executions` when invoked by scheduling user, or `space_manage_atm_workflow_executions`  otherwise.  ***Example cURL requests***  **Resume workflow execution** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID/resume\" ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resume_workflow_execution_with_http_info(wid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wid: Workflow execution Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resume_workflow_execution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'wid' is set
        if ('wid' not in params or
                params['wid'] is None):
            raise ValueError("Missing the required parameter `wid` when calling `resume_workflow_execution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'wid' in params:
            path_params['wid'] = params['wid']  # noqa: E501

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
            '/automation/execution/workflows/{wid}/resume', 'POST',
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

    def retry_workflow_execution(self, body, wid, **kwargs):  # noqa: E501
        """Retry workflow execution  # noqa: E501

        Retries failed workflow execution starting from specified lane run.  This operation requires `space_schedule_atm_workflow_executions` when invoked by scheduling user, or `space_manage_atm_workflow_executions`  otherwise.  ***Example cURL requests***  **Retry workflow execution** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID/retry\" -H \"Content-Type: application/json\" -d '{     \"laneIndex\": 2,     \"laneRunNumber\": 3 }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retry_workflow_execution(body, wid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WidRetryBody body: Lane run reference. (required)
        :param str wid: Workflow execution Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retry_workflow_execution_with_http_info(body, wid, **kwargs)  # noqa: E501
        else:
            (data) = self.retry_workflow_execution_with_http_info(body, wid, **kwargs)  # noqa: E501
            return data

    def retry_workflow_execution_with_http_info(self, body, wid, **kwargs):  # noqa: E501
        """Retry workflow execution  # noqa: E501

        Retries failed workflow execution starting from specified lane run.  This operation requires `space_schedule_atm_workflow_executions` when invoked by scheduling user, or `space_manage_atm_workflow_executions`  otherwise.  ***Example cURL requests***  **Retry workflow execution** ```bash curl -H \"X-Auth-Token: $TOKEN\" \\ -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows/$ATM_WORKFLOW_EXECUTION_ID/retry\" -H \"Content-Type: application/json\" -d '{     \"laneIndex\": 2,     \"laneRunNumber\": 3 }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retry_workflow_execution_with_http_info(body, wid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WidRetryBody body: Lane run reference. (required)
        :param str wid: Workflow execution Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'wid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retry_workflow_execution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `retry_workflow_execution`")  # noqa: E501
        # verify the required parameter 'wid' is set
        if ('wid' not in params or
                params['wid'] is None):
            raise ValueError("Missing the required parameter `wid` when calling `retry_workflow_execution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'wid' in params:
            path_params['wid'] = params['wid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2']  # noqa: E501

        return self.api_client.call_api(
            '/automation/execution/workflows/{wid}/retry', 'POST',
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

    def schedule_workflow_execution(self, body, **kwargs):  # noqa: E501
        """Schedule workflow execution  # noqa: E501

        Schedules a workflow execution based on specified workflow schema revision. The execution is asynchronous.  This operation requires `space_schedule_atm_workflow_executions` privilege and the requesting user must belong to the automation inventory containing the corresponding workflow schema definition.  ***Example cURL requests***  **Create workflow execution** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows\" \\ -H \"Content-Type: application/json\" -d '{     \"spaceId\": \"'$SPACE_ID'\",     \"atmWorkflowSchemaId\": \"'$ATM_WORKFLOW_SCHEMA_ID'\",     \"atmWorkflowSchemaRevisionNumber\": 3,     \"storeInitialContentOverlay\": {         \"de6d2e524459dd235f80aa8652a68879b5dbe9\": [             {                 \"file_id\": \"0000000000523261677569642330376134636136616638613431366334386338343366356338643562323662\"             }         ],         \"83cf895501eb11f9bc71e4b2b41a252e8561b5\": {             \"file_id\": \"000000000052A6E0677569642334653938663463616538386232366437366539636462393634633031653733\"         }     },     \"logLevel\": \"debug\",     \"callback\": \"https://my-server.example.com/execution-callback\" }'  {\"atmWorkflowExecutionId\": \"11a53ed06d175c89bc3ed5be61f8217cch1890\"} ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedule_workflow_execution(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AtmWorkflowExecutionScheduleRequest body: Workflow execution properties. (required)
        :return: InlineResponse2018
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.schedule_workflow_execution_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.schedule_workflow_execution_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def schedule_workflow_execution_with_http_info(self, body, **kwargs):  # noqa: E501
        """Schedule workflow execution  # noqa: E501

        Schedules a workflow execution based on specified workflow schema revision. The execution is asynchronous.  This operation requires `space_schedule_atm_workflow_executions` privilege and the requesting user must belong to the automation inventory containing the corresponding workflow schema definition.  ***Example cURL requests***  **Create workflow execution** ```bash curl -H \"X-Auth-Token: $TOKEN\" -X POST \"https://$PROVIDER_HOST/api/v3/oneprovider/automation/execution/workflows\" \\ -H \"Content-Type: application/json\" -d '{     \"spaceId\": \"'$SPACE_ID'\",     \"atmWorkflowSchemaId\": \"'$ATM_WORKFLOW_SCHEMA_ID'\",     \"atmWorkflowSchemaRevisionNumber\": 3,     \"storeInitialContentOverlay\": {         \"de6d2e524459dd235f80aa8652a68879b5dbe9\": [             {                 \"file_id\": \"0000000000523261677569642330376134636136616638613431366334386338343366356338643562323662\"             }         ],         \"83cf895501eb11f9bc71e4b2b41a252e8561b5\": {             \"file_id\": \"000000000052A6E0677569642334653938663463616538386232366437366539636462393634633031653733\"         }     },     \"logLevel\": \"debug\",     \"callback\": \"https://my-server.example.com/execution-callback\" }'  {\"atmWorkflowExecutionId\": \"11a53ed06d175c89bc3ed5be61f8217cch1890\"} ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedule_workflow_execution_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AtmWorkflowExecutionScheduleRequest body: Workflow execution properties. (required)
        :return: InlineResponse2018
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
                    " to method schedule_workflow_execution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `schedule_workflow_execution`")  # noqa: E501

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
            '/automation/execution/workflows', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2018',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
