# coding: utf-8

"""
    Onepanel

    # Overview  This is the RESTful API definition of **Onepanel** component of Onedata data management system [onedata.org](http://onedata.org).  > This API is defined using [Swagger](http://swagger.io/), the JSON specification can be used to automatically generate client libraries -   [swagger.json](../../../swagger/onepanel/swagger.json).  This API allows control and configuration of local Onedata deployment, in particular full control over the **Onezone** and **Oneprovider** services and their distribution and monitoring on the local resources.  The API is grouped into 3 categories of operations:   * **Onepanel** - for common operations   * **Oneprovider** - for Oneprovider specific administrative operations   * **Onezone** - for Onezone specific administrative operations  Each of these components is composed of the following services:   * **Worker services** - these are available under `/zone/workers` and     `/provider/workers` paths,   * **Databases services** - each Onedata component stores it's metadata in a     Couchbase backend, which can be distributed on any number of nodes, these     are available under `/zone/databases` and `/provider/databases` paths,   * **Cluster manager services** - this is a service which controls other     deployed processes in one site, these are availables under these are     available under `/zone/managers` and `/provider/managers` paths.  **Onezone** and **Oneprovider** components are composed of 3 types of services: **managers**, **databases** and **workers**.  Using this API each of these components can be deployed, configured, started and stopped on a specified host in the local site, in the context of either **Onezone** or **Oneprovider** service.  All paths listed in this documentation are relative to the base Onepanel REST API which is `/api/v3/onepanel`, so complete URL for a request to Onepanel service is:  ``` http://HOSTNAME:PORT/api/v3/onepanel/... ```  ## Authentication  ### Token authentication  The recommended, safest way of authenticating requests to Onepanel API is using the **Onedata access tokens**. The token should be present in `X-Auth-Token` or `Authorization: Bearer` header. See [Onezone documentation](/#/home/api/latest/onezone?anchor=section/Overview/Authentication-and-authorization) for detailed explanation of the token concepts.  Curl examples: ```bash curl -H \"X-Auth-Token: $TOKEN\" [...] curl -H \"Authorization: Bearer $TOKEN\" [...] curl -H \"Macaroon: $TOKEN\" [...]   # DEPRECATED ```   ### Passphrase authentication  The token authentication dependes on the Onezone service. In special cases - during Onezone deployment or its outage - it is necessary to use the local **emergency passphrase**.  The passphrase should be provided in a Basic authentication header with username `onepanel`. For curl users this means ```bash curl -u onepanel:TheEmergencyPassphrase ```  The passphrase can also be sent without any username, as the whole content of base64-encoded string in Basic authorization header, e.g. ```bash curl -H \"Authorization: Basic $(echo -n TheEmergencyPassphrase | base64)\" ```  The passphrase is set during deployment. It can be changed in the Onepanel GUI or with an API request: ```bash curl -X PUT 'https://$PANEL_HOST:9443/api/v3/onepanel/emergency_passphrase' \\ -u onepanel:TheEmergencyPassphrase -H 'Content-Type: application/json' \\ -d '{\"currentPassphrase\": \"TheEmergencyPassphrase\", \"newPassphrase\": \"TheNewPassphrase\"}' ```  ## API structure  The Onepanel API is structured to reflect that it can either be used to control **Onezone** or **Oneprovider** deployment, each Onedata component deployment has a separate Onepanel instance. In order to make the API calls explicit, **Onezone** or **Oneprovider** specific requests have different paths, i.e.:   * Onezone specific operations start with `/api/v3/onepanel/zone/`   * Oneprovider specific operations start with `/api/v3/onepanel/provider/`   * Common operations paths include `/api/v3/onepanel/users`,     `/api/v3/onepanel/hosts` and `/api/v3/onepanel/tasks`  The overall configuration of each component can be controlled by updating `/api/v3/onepanel/zone/configuration` and `/api/v3/onepanel/provider/configuration` resources.  ## Examples  Below are some example requests to Onepanel using cURL:  **Add storage resource to provider** ```bash curl -X POST -u onepanel:Passphrase1 -k -vvv -H \"content-type: application/json\" \\ -d '{\"NFS\": {\"type\": \"posix\", \"mountPoint\": \"/mnt/vfs\"}}' \\ https://172.17.0.4:9443/api/v3/onepanel/provider/storages ```  **Add a new Onezone worker** ```bash curl -X POST -u onepanel:Passphrase1 -k -vvv -H \"content-type: application/json\" \\ -d '{\"hosts\": [\"node1.p1.1.dev\"]}' \\ https://172.17.0.4:9443/api/v3/onepanel/zone/workers ```   # noqa: E501

    OpenAPI spec version: 21.02.3
    Contact: info@onedata.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from onepanel_client.api_client import ApiClient


class AutoCleaningApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_auto_cleaning(self, id, **kwargs):  # noqa: E501
        """Cancel space auto-cleaning  # noqa: E501

        Cancel current run of auto-cleaning mechanism for given space.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_auto_cleaning(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Id of a space. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_auto_cleaning_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_auto_cleaning_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def cancel_auto_cleaning_with_http_info(self, id, **kwargs):  # noqa: E501
        """Cancel space auto-cleaning  # noqa: E501

        Cancel current run of auto-cleaning mechanism for given space.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_auto_cleaning_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Id of a space. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_auto_cleaning" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `cancel_auto_cleaning`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/provider/spaces/{id}/auto-cleaning/cancel', 'POST',
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

    def configure_space_auto_cleaning(self, body, id, **kwargs):  # noqa: E501
        """Configure space auto-cleaning mechanism  # noqa: E501

        Configures space auto-cleaning mechanism in the space.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.configure_space_auto_cleaning(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SpaceAutoCleaningConfiguration body: New configuration of space auto-cleaning mechanism.
 (required)
        :param str id: The Id of a space. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.configure_space_auto_cleaning_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.configure_space_auto_cleaning_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def configure_space_auto_cleaning_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Configure space auto-cleaning mechanism  # noqa: E501

        Configures space auto-cleaning mechanism in the space.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.configure_space_auto_cleaning_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SpaceAutoCleaningConfiguration body: New configuration of space auto-cleaning mechanism.
 (required)
        :param str id: The Id of a space. (required)
        :return: None
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
                    " to method configure_space_auto_cleaning" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `configure_space_auto_cleaning`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `configure_space_auto_cleaning`")  # noqa: E501

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
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/provider/spaces/{id}/auto-cleaning/configuration', 'PATCH',
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

    def get_provider_space_auto_cleaning_report(self, id, report_id, **kwargs):  # noqa: E501
        """Get the report from a space auto-cleaning run  # noqa: E501

        Returns the details of a specific auto-cleaning run.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_provider_space_auto_cleaning_report(id, report_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Id of a space. (required)
        :param str report_id: The Id of an auto-cleaning report. (required)
        :return: SpaceAutoCleaningReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_provider_space_auto_cleaning_report_with_http_info(id, report_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_provider_space_auto_cleaning_report_with_http_info(id, report_id, **kwargs)  # noqa: E501
            return data

    def get_provider_space_auto_cleaning_report_with_http_info(self, id, report_id, **kwargs):  # noqa: E501
        """Get the report from a space auto-cleaning run  # noqa: E501

        Returns the details of a specific auto-cleaning run.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_provider_space_auto_cleaning_report_with_http_info(id, report_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Id of a space. (required)
        :param str report_id: The Id of an auto-cleaning report. (required)
        :return: SpaceAutoCleaningReport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'report_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_provider_space_auto_cleaning_report" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_provider_space_auto_cleaning_report`")  # noqa: E501
        # verify the required parameter 'report_id' is set
        if ('report_id' not in params or
                params['report_id'] is None):
            raise ValueError("Missing the required parameter `report_id` when calling `get_provider_space_auto_cleaning_report`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'report_id' in params:
            path_params['report_id'] = params['report_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/provider/spaces/{id}/auto-cleaning/reports/{report_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SpaceAutoCleaningReport',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_provider_space_auto_cleaning_reports(self, id, **kwargs):  # noqa: E501
        """Get Ids of of the space auto-cleaning reports  # noqa: E501

        Returns the list of Ids of space auto-cleaning reports. The list is sorted descending by start time of an auto-cleaning run (the newest report is first).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_provider_space_auto_cleaning_reports(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Id of a space. (required)
        :param int offset: Allows to skip N first report Ids.
        :param int limit: Allows to limit the number of returned report Ids up to N last reports. By default, all report Ids will be returned. 
        :param str index: Allows to list the report Ids starting from the specific report. 
        :return: SpaceAutoCleaningReports
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_provider_space_auto_cleaning_reports_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_provider_space_auto_cleaning_reports_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_provider_space_auto_cleaning_reports_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Ids of of the space auto-cleaning reports  # noqa: E501

        Returns the list of Ids of space auto-cleaning reports. The list is sorted descending by start time of an auto-cleaning run (the newest report is first).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_provider_space_auto_cleaning_reports_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Id of a space. (required)
        :param int offset: Allows to skip N first report Ids.
        :param int limit: Allows to limit the number of returned report Ids up to N last reports. By default, all report Ids will be returned. 
        :param str index: Allows to list the report Ids starting from the specific report. 
        :return: SpaceAutoCleaningReports
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'offset', 'limit', 'index']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_provider_space_auto_cleaning_reports" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_provider_space_auto_cleaning_reports`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'index' in params:
            query_params.append(('index', params['index']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/provider/spaces/{id}/auto-cleaning/reports', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SpaceAutoCleaningReports',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_provider_space_auto_cleaning_status(self, id, **kwargs):  # noqa: E501
        """Get status of space auto-cleaning mechanism  # noqa: E501

        Returns status of current process of auto-cleaning for the space.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_provider_space_auto_cleaning_status(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Id of a space. (required)
        :return: SpaceAutoCleaningStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_provider_space_auto_cleaning_status_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_provider_space_auto_cleaning_status_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_provider_space_auto_cleaning_status_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get status of space auto-cleaning mechanism  # noqa: E501

        Returns status of current process of auto-cleaning for the space.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_provider_space_auto_cleaning_status_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Id of a space. (required)
        :return: SpaceAutoCleaningStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_provider_space_auto_cleaning_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_provider_space_auto_cleaning_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/provider/spaces/{id}/auto-cleaning/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SpaceAutoCleaningStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_space_auto_cleaning_configuration(self, id, **kwargs):  # noqa: E501
        """Get space auto-cleaning configuration  # noqa: E501

        Returns configuration of auto-cleaning mechanism in the space specified by space Id in the path.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_auto_cleaning_configuration(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Id of a space of which auto-cleaning configuration should be returned. (required)
        :return: SpaceAutoCleaningConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_space_auto_cleaning_configuration_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_space_auto_cleaning_configuration_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_space_auto_cleaning_configuration_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get space auto-cleaning configuration  # noqa: E501

        Returns configuration of auto-cleaning mechanism in the space specified by space Id in the path.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_space_auto_cleaning_configuration_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Id of a space of which auto-cleaning configuration should be returned. (required)
        :return: SpaceAutoCleaningConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_space_auto_cleaning_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_space_auto_cleaning_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/provider/spaces/{id}/auto-cleaning/configuration', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SpaceAutoCleaningConfiguration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def trigger_auto_cleaning(self, id, **kwargs):  # noqa: E501
        """Trigger space auto-cleaning  # noqa: E501

        Trigger one run of auto-cleaning mechanism for given space.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trigger_auto_cleaning(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Id of a space. (required)
        :return: InlineResponse202
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.trigger_auto_cleaning_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.trigger_auto_cleaning_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def trigger_auto_cleaning_with_http_info(self, id, **kwargs):  # noqa: E501
        """Trigger space auto-cleaning  # noqa: E501

        Trigger one run of auto-cleaning mechanism for given space.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trigger_auto_cleaning_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Id of a space. (required)
        :return: InlineResponse202
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trigger_auto_cleaning" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `trigger_auto_cleaning`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key1', 'api_key2', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/provider/spaces/{id}/auto-cleaning/start', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse202',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
