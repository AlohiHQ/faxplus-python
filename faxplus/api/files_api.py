# coding: utf-8

"""
    Fax.Plus REST API

    Visit https://apidoc.fax.plus for more information.

    © Alohi SA (Geneva, Switzerland)

    https://www.alohi.com
    Contact: info@fax.plus
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from faxplus.api_client import ApiClient
from faxplus.models import *
from multiprocessing.pool import ApplyResult
from urllib3._collections import HTTPHeaderDict


class FilesApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_fax_report(self, user_id, fax_id, **kwargs):  # noqa: E501
        """Get fax confirmation report  # noqa: E501

        Retrieve fax confirmation report  # noqa: E501
        >>> result = FilesApi().get_fax_report(user_id, fax_id, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FilesApi().get_fax_report(user_id, fax_id, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param str fax_id: ID of the fax which you want to download (required)
        :return: Binary
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Binary | ApplyResult[Binary]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_fax_report_with_http_info(user_id, fax_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_fax_report_with_http_info(user_id, fax_id, **kwargs)  # noqa: E501
            return data

    def get_fax_report_with_http_info(self, user_id, fax_id, **kwargs):  # noqa: E501
        """Get fax confirmation report  # noqa: E501

        The difference between this method and `get_fax_report` is that this method may return not only the data,
        but also HTTP status and headers.

        Retrieve fax confirmation report  # noqa: E501
        >>> result = FilesApi().get_fax_report_with_http_info(user_id, fax_id, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FilesApi().get_fax_report_with_http_info(user_id, fax_id, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param str fax_id: ID of the fax which you want to download (required)
        :return: Binary
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Binary | tuple[Binary, int, HTTPHeaderDict] | ApplyResult[Binary] | ApplyResult[tuple[Binary, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'user_id' is set
        if user_id is None:
            raise ValueError("Missing the required parameter `user_id` when calling `get_fax_report`")  # noqa: E501
        # verify the required parameter 'fax_id' is set
        if fax_id is None:
            raise ValueError("Missing the required parameter `fax_id` when calling `get_fax_report`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if user_id is not None:
            path_params['user_id'] = user_id  # noqa: E501
        if fax_id is not None:
            path_params['fax_id'] = fax_id  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/pdf', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2', 'PAT']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{user_id}/report/{fax_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Binary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_file(self, user_id, fax_id, format=None, **kwargs):  # noqa: E501
        """Download fax file  # noqa: E501

        Download sent or received fax file  # noqa: E501
        >>> result = FilesApi().get_file(user_id, fax_id, format, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FilesApi().get_file(user_id, fax_id, format, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param str fax_id: ID of the fax which you want to download (required)
        :param FileType format: This parameter overrides the Accept header
        :return: Binary
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Binary | ApplyResult[Binary]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_file_with_http_info(user_id, fax_id, format, **kwargs)  # noqa: E501
        else:
            (data) = self.get_file_with_http_info(user_id, fax_id, format, **kwargs)  # noqa: E501
            return data

    def get_file_with_http_info(self, user_id, fax_id, format=None, **kwargs):  # noqa: E501
        """Download fax file  # noqa: E501

        The difference between this method and `get_file` is that this method may return not only the data,
        but also HTTP status and headers.

        Download sent or received fax file  # noqa: E501
        >>> result = FilesApi().get_file_with_http_info(user_id, fax_id, format, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FilesApi().get_file_with_http_info(user_id, fax_id, format, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param str fax_id: ID of the fax which you want to download (required)
        :param FileType format: This parameter overrides the Accept header
        :return: Binary
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Binary | tuple[Binary, int, HTTPHeaderDict] | ApplyResult[Binary] | ApplyResult[tuple[Binary, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'user_id' is set
        if user_id is None:
            raise ValueError("Missing the required parameter `user_id` when calling `get_file`")  # noqa: E501
        # verify the required parameter 'fax_id' is set
        if fax_id is None:
            raise ValueError("Missing the required parameter `fax_id` when calling `get_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if user_id is not None:
            path_params['user_id'] = user_id  # noqa: E501
        if fax_id is not None:
            path_params['fax_id'] = fax_id  # noqa: E501

        query_params = []
        if format is not None:
            query_params.append(('format', format))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/pdf', 'image/tiff', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2', 'PAT']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{user_id}/files/{fax_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Binary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats=collection_formats)

    def upload_file(self, user_id, fax_file=None, format=None, **kwargs):  # noqa: E501
        """Upload a file  # noqa: E501

        Before sending a fax you need to upload your files using this API. In order to upload your fax file, you have to send a `multipart/form-data` request with your file. Set the `name` to `fax_file`, `filename` to your file's name with extension, and the Content-Type to the file's MIME type. In most cases, the `filename` directive will be automatically added by your library of choice. If the upload was successful you would receive a `file_path` which you can use to send your fax.  # noqa: E501
        >>> result = FilesApi().upload_file(user_id, fax_file, format, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FilesApi().upload_file(user_id, fax_file, format, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param str fax_file:
        :param FileType format: Can be 'pdf' or 'tiff'
        :return: FilePath
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FilePath | ApplyResult[FilePath]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upload_file_with_http_info(user_id, fax_file, format, **kwargs)  # noqa: E501
        else:
            (data) = self.upload_file_with_http_info(user_id, fax_file, format, **kwargs)  # noqa: E501
            return data

    def upload_file_with_http_info(self, user_id, fax_file=None, format=None, **kwargs):  # noqa: E501
        """Upload a file  # noqa: E501

        The difference between this method and `upload_file` is that this method may return not only the data,
        but also HTTP status and headers.

        Before sending a fax you need to upload your files using this API. In order to upload your fax file, you have to send a `multipart/form-data` request with your file. Set the `name` to `fax_file`, `filename` to your file's name with extension, and the Content-Type to the file's MIME type. In most cases, the `filename` directive will be automatically added by your library of choice. If the upload was successful you would receive a `file_path` which you can use to send your fax.  # noqa: E501
        >>> result = FilesApi().upload_file_with_http_info(user_id, fax_file, format, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FilesApi().upload_file_with_http_info(user_id, fax_file, format, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param str fax_file:
        :param FileType format: Can be 'pdf' or 'tiff'
        :return: FilePath
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FilePath | tuple[FilePath, int, HTTPHeaderDict] | ApplyResult[FilePath] | ApplyResult[tuple[FilePath, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'user_id' is set
        if user_id is None:
            raise ValueError("Missing the required parameter `user_id` when calling `upload_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if user_id is not None:
            path_params['user_id'] = user_id  # noqa: E501

        query_params = []
        if format is not None:
            query_params.append(('format', format))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if fax_file is not None:
            local_var_files['fax_file'] = fax_file  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2', 'PAT']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{user_id}/files', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilePath',  # noqa: E501
            auth_settings=auth_settings,
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats=collection_formats)
