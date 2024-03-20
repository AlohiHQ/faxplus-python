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


class FaxesApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_fax(self, user_id, fax_id, **kwargs):  # noqa: E501
        """Delete a fax  # noqa: E501

        Delete a specific fax record by providing its id  # noqa: E501
        >>> result = FaxesApi().delete_fax(user_id, fax_id, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FaxesApi().delete_fax(user_id, fax_id, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param str fax_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None | ApplyResult[None]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_fax_with_http_info(user_id, fax_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_fax_with_http_info(user_id, fax_id, **kwargs)  # noqa: E501
            return data

    def delete_fax_with_http_info(self, user_id, fax_id, **kwargs):  # noqa: E501
        """Delete a fax  # noqa: E501

        The difference between this method and `delete_fax` is that this method may return not only the data,
        but also HTTP status and headers.

        Delete a specific fax record by providing its id  # noqa: E501
        >>> result = FaxesApi().delete_fax_with_http_info(user_id, fax_id, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FaxesApi().delete_fax_with_http_info(user_id, fax_id, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param str fax_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None | tuple[None, int, HTTPHeaderDict] | ApplyResult[None] | ApplyResult[tuple[None, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'user_id' is set
        if user_id is None:
            raise ValueError("Missing the required parameter `user_id` when calling `delete_fax`")  # noqa: E501
        # verify the required parameter 'fax_id' is set
        if fax_id is None:
            raise ValueError("Missing the required parameter `fax_id` when calling `delete_fax`")  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2', 'PAT']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{user_id}/faxes/{fax_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fax(self, user_id, fax_id, **kwargs):  # noqa: E501
        """Get a fax record  # noqa: E501

        Get a specific fax record details like duration, pages etc.  # noqa: E501
        >>> result = FaxesApi().get_fax(user_id, fax_id, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FaxesApi().get_fax(user_id, fax_id, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param str fax_id: (required)
        :return: Fax
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Fax | ApplyResult[Fax]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_fax_with_http_info(user_id, fax_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_fax_with_http_info(user_id, fax_id, **kwargs)  # noqa: E501
            return data

    def get_fax_with_http_info(self, user_id, fax_id, **kwargs):  # noqa: E501
        """Get a fax record  # noqa: E501

        The difference between this method and `get_fax` is that this method may return not only the data,
        but also HTTP status and headers.

        Get a specific fax record details like duration, pages etc.  # noqa: E501
        >>> result = FaxesApi().get_fax_with_http_info(user_id, fax_id, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FaxesApi().get_fax_with_http_info(user_id, fax_id, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param str fax_id: (required)
        :return: Fax
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Fax | tuple[Fax, int, HTTPHeaderDict] | ApplyResult[Fax] | ApplyResult[tuple[Fax, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'user_id' is set
        if user_id is None:
            raise ValueError("Missing the required parameter `user_id` when calling `get_fax`")  # noqa: E501
        # verify the required parameter 'fax_id' is set
        if fax_id is None:
            raise ValueError("Missing the required parameter `fax_id` when calling `get_fax`")  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2', 'PAT']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{user_id}/faxes/{fax_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Fax',  # noqa: E501
            auth_settings=auth_settings,
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_faxes(self, user_id, category=None, after=None, before=None, limit=None, **kwargs):  # noqa: E501
        """List fax records  # noqa: E501

        Get your own or your subordinate's faxes list  # noqa: E501
        >>> result = FaxesApi().list_faxes(user_id, category, after, before, limit, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FaxesApi().list_faxes(user_id, category, after, before, limit, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param FaxCategory category: Category parameter. Valid values: **inbox**, **sent**, **spam**
        :param str after: Start date to get records from that date. Format: *YYYY-MM-DD HH:mm:ss*
        :param str before: End date to get records before that date. Format: *YYYY-MM-DD HH:mm:ss*
        :param int limit: Limit of fax records you want to get per request
        :return: FaxList
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FaxList | ApplyResult[FaxList]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_faxes_with_http_info(user_id, category, after, before, limit, **kwargs)  # noqa: E501
        else:
            (data) = self.list_faxes_with_http_info(user_id, category, after, before, limit, **kwargs)  # noqa: E501
            return data

    def list_faxes_with_http_info(self, user_id, category=None, after=None, before=None, limit=None, **kwargs):  # noqa: E501
        """List fax records  # noqa: E501

        The difference between this method and `list_faxes` is that this method may return not only the data,
        but also HTTP status and headers.

        Get your own or your subordinate's faxes list  # noqa: E501
        >>> result = FaxesApi().list_faxes_with_http_info(user_id, category, after, before, limit, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FaxesApi().list_faxes_with_http_info(user_id, category, after, before, limit, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param FaxCategory category: Category parameter. Valid values: **inbox**, **sent**, **spam**
        :param str after: Start date to get records from that date. Format: *YYYY-MM-DD HH:mm:ss*
        :param str before: End date to get records before that date. Format: *YYYY-MM-DD HH:mm:ss*
        :param int limit: Limit of fax records you want to get per request
        :return: FaxList
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FaxList | tuple[FaxList, int, HTTPHeaderDict] | ApplyResult[FaxList] | ApplyResult[tuple[FaxList, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'user_id' is set
        if user_id is None:
            raise ValueError("Missing the required parameter `user_id` when calling `list_faxes`")  # noqa: E501

        if after is not None and not re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}', after):  # noqa: E501
            raise ValueError("Invalid value for parameter `after` when calling `list_faxes`, must conform to the pattern `/^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}/`")  # noqa: E501
        if before is not None and not re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}', before):  # noqa: E501
            raise ValueError("Invalid value for parameter `before` when calling `list_faxes`, must conform to the pattern `/^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}/`")  # noqa: E501
        if limit is not None and limit > 50:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_faxes`, must be a value less than or equal to `50`")  # noqa: E501
        if limit is not None and limit < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_faxes`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if user_id is not None:
            path_params['user_id'] = user_id  # noqa: E501

        query_params = []
        if category is not None:
            query_params.append(('category', category))  # noqa: E501
        if after is not None:
            query_params.append(('after', after))  # noqa: E501
        if before is not None:
            query_params.append(('before', before))  # noqa: E501
        if limit is not None:
            query_params.append(('limit', limit))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2', 'PAT']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{user_id}/faxes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FaxList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_fax(self, user_id, fax_id, body=None, **kwargs):  # noqa: E501
        """Modify fax record  # noqa: E501

        You can modify a fax record's comment or mark it as read  # noqa: E501
        >>> result = FaxesApi().update_fax(user_id, fax_id, body, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FaxesApi().update_fax(user_id, fax_id, body, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param str fax_id: (required)
        :param PayloadFaxModification body: Request object for making changes in a fax object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None | ApplyResult[None]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_fax_with_http_info(user_id, fax_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_fax_with_http_info(user_id, fax_id, body, **kwargs)  # noqa: E501
            return data

    def update_fax_with_http_info(self, user_id, fax_id, body=None, **kwargs):  # noqa: E501
        """Modify fax record  # noqa: E501

        The difference between this method and `update_fax` is that this method may return not only the data,
        but also HTTP status and headers.

        You can modify a fax record's comment or mark it as read  # noqa: E501
        >>> result = FaxesApi().update_fax_with_http_info(user_id, fax_id, body, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FaxesApi().update_fax_with_http_info(user_id, fax_id, body, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param str fax_id: (required)
        :param PayloadFaxModification body: Request object for making changes in a fax object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None | tuple[None, int, HTTPHeaderDict] | ApplyResult[None] | ApplyResult[tuple[None, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'user_id' is set
        if user_id is None:
            raise ValueError("Missing the required parameter `user_id` when calling `update_fax`")  # noqa: E501
        # verify the required parameter 'fax_id' is set
        if fax_id is None:
            raise ValueError("Missing the required parameter `fax_id` when calling `update_fax`")  # noqa: E501

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
        if body is not None:
            body_params = body
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2', 'PAT']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{user_id}/faxes/{fax_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats=collection_formats)
