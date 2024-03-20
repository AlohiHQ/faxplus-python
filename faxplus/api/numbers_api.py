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


class NumbersApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_number(self, user_id, number, **kwargs):  # noqa: E501
        """Get number information  # noqa: E501

        Get information about a single purchased/assigned fax number  # noqa: E501
        >>> result = NumbersApi().get_number(user_id, number, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = NumbersApi().get_number(user_id, number, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: ID of the number owner (required)
        :param str number: Fax number to get information about (required)
        :return: Number
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Number | ApplyResult[Number]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_number_with_http_info(user_id, number, **kwargs)  # noqa: E501
        else:
            (data) = self.get_number_with_http_info(user_id, number, **kwargs)  # noqa: E501
            return data

    def get_number_with_http_info(self, user_id, number, **kwargs):  # noqa: E501
        """Get number information  # noqa: E501

        The difference between this method and `get_number` is that this method may return not only the data,
        but also HTTP status and headers.

        Get information about a single purchased/assigned fax number  # noqa: E501
        >>> result = NumbersApi().get_number_with_http_info(user_id, number, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = NumbersApi().get_number_with_http_info(user_id, number, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: ID of the number owner (required)
        :param str number: Fax number to get information about (required)
        :return: Number
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Number | tuple[Number, int, HTTPHeaderDict] | ApplyResult[Number] | ApplyResult[tuple[Number, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'user_id' is set
        if user_id is None:
            raise ValueError("Missing the required parameter `user_id` when calling `get_number`")  # noqa: E501
        # verify the required parameter 'number' is set
        if number is None:
            raise ValueError("Missing the required parameter `number` when calling `get_number`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if user_id is not None:
            path_params['user_id'] = user_id  # noqa: E501
        if number is not None:
            path_params['number'] = number  # noqa: E501

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
            '/accounts/{user_id}/numbers/{number}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Number',  # noqa: E501
            auth_settings=auth_settings,
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_numbers(self, user_id, **kwargs):  # noqa: E501
        """List phone numbers  # noqa: E501

        List your purchased/assigned phone numbers. For corporate members all assigned numbers will be returned, while for the corporate admin, all purchased numbers  # noqa: E501
        >>> result = NumbersApi().list_numbers(user_id, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = NumbersApi().list_numbers(user_id, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: ID of the user to get numbers for (required)
        :return: NumberList
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NumberList | ApplyResult[NumberList]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_numbers_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_numbers_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def list_numbers_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """List phone numbers  # noqa: E501

        The difference between this method and `list_numbers` is that this method may return not only the data,
        but also HTTP status and headers.

        List your purchased/assigned phone numbers. For corporate members all assigned numbers will be returned, while for the corporate admin, all purchased numbers  # noqa: E501
        >>> result = NumbersApi().list_numbers_with_http_info(user_id, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = NumbersApi().list_numbers_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: ID of the user to get numbers for (required)
        :return: NumberList
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NumberList | tuple[NumberList, int, HTTPHeaderDict] | ApplyResult[NumberList] | ApplyResult[tuple[NumberList, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'user_id' is set
        if user_id is None:
            raise ValueError("Missing the required parameter `user_id` when calling `list_numbers`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if user_id is not None:
            path_params['user_id'] = user_id  # noqa: E501

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
            '/accounts/{user_id}/numbers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NumberList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats=collection_formats)

    def revoke_number(self, user_id, number, **kwargs):  # noqa: E501
        """Revoke number  # noqa: E501

        Revoke fax number from a corporate member. To revoke your own number use self as a user_id  # noqa: E501
        >>> result = NumbersApi().revoke_number(user_id, number, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = NumbersApi().revoke_number(user_id, number, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: ID of the user to revoke the number from. Number can not be removed from the admin (required)
        :param str number: Fax number to remove members from (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None | ApplyResult[None]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.revoke_number_with_http_info(user_id, number, **kwargs)  # noqa: E501
        else:
            (data) = self.revoke_number_with_http_info(user_id, number, **kwargs)  # noqa: E501
            return data

    def revoke_number_with_http_info(self, user_id, number, **kwargs):  # noqa: E501
        """Revoke number  # noqa: E501

        The difference between this method and `revoke_number` is that this method may return not only the data,
        but also HTTP status and headers.

        Revoke fax number from a corporate member. To revoke your own number use self as a user_id  # noqa: E501
        >>> result = NumbersApi().revoke_number_with_http_info(user_id, number, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = NumbersApi().revoke_number_with_http_info(user_id, number, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: ID of the user to revoke the number from. Number can not be removed from the admin (required)
        :param str number: Fax number to remove members from (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None | tuple[None, int, HTTPHeaderDict] | ApplyResult[None] | ApplyResult[tuple[None, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'user_id' is set
        if user_id is None:
            raise ValueError("Missing the required parameter `user_id` when calling `revoke_number`")  # noqa: E501
        # verify the required parameter 'number' is set
        if number is None:
            raise ValueError("Missing the required parameter `number` when calling `revoke_number`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if user_id is not None:
            path_params['user_id'] = user_id  # noqa: E501
        if number is not None:
            path_params['number'] = number  # noqa: E501

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
            '/accounts/{user_id}/numbers/{number}', 'DELETE',
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

    def update_number(self, user_id, number, body=None, **kwargs):  # noqa: E501
        """Assign number  # noqa: E501

        Assign fax number to a corporate member  # noqa: E501
        >>> result = NumbersApi().update_number(user_id, number, body, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = NumbersApi().update_number(user_id, number, body, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: ID of the number owner (required)
        :param str number: Fax number to update (required)
        :param PayloadNumberModification body: Request object for making changes in number object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None | ApplyResult[None]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_number_with_http_info(user_id, number, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_number_with_http_info(user_id, number, body, **kwargs)  # noqa: E501
            return data

    def update_number_with_http_info(self, user_id, number, body=None, **kwargs):  # noqa: E501
        """Assign number  # noqa: E501

        The difference between this method and `update_number` is that this method may return not only the data,
        but also HTTP status and headers.

        Assign fax number to a corporate member  # noqa: E501
        >>> result = NumbersApi().update_number_with_http_info(user_id, number, body, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = NumbersApi().update_number_with_http_info(user_id, number, body, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: ID of the number owner (required)
        :param str number: Fax number to update (required)
        :param PayloadNumberModification body: Request object for making changes in number object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None | tuple[None, int, HTTPHeaderDict] | ApplyResult[None] | ApplyResult[tuple[None, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'user_id' is set
        if user_id is None:
            raise ValueError("Missing the required parameter `user_id` when calling `update_number`")  # noqa: E501
        # verify the required parameter 'number' is set
        if number is None:
            raise ValueError("Missing the required parameter `number` when calling `update_number`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if user_id is not None:
            path_params['user_id'] = user_id  # noqa: E501
        if number is not None:
            path_params['number'] = number  # noqa: E501

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
            '/accounts/{user_id}/numbers/{number}', 'PUT',
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
