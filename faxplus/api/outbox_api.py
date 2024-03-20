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


class OutboxApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_outbox_fax(self, user_id, outbox_fax_id, **kwargs):  # noqa: E501
        """Delete an outgoing fax  # noqa: E501

        Delete an outgoing fax that is being scheduled for sending  # noqa: E501
        >>> result = OutboxApi().delete_outbox_fax(user_id, outbox_fax_id, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = OutboxApi().delete_outbox_fax(user_id, outbox_fax_id, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param str outbox_fax_id: ID of the outgoing fax to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None | ApplyResult[None]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_outbox_fax_with_http_info(user_id, outbox_fax_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_outbox_fax_with_http_info(user_id, outbox_fax_id, **kwargs)  # noqa: E501
            return data

    def delete_outbox_fax_with_http_info(self, user_id, outbox_fax_id, **kwargs):  # noqa: E501
        """Delete an outgoing fax  # noqa: E501

        The difference between this method and `delete_outbox_fax` is that this method may return not only the data,
        but also HTTP status and headers.

        Delete an outgoing fax that is being scheduled for sending  # noqa: E501
        >>> result = OutboxApi().delete_outbox_fax_with_http_info(user_id, outbox_fax_id, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = OutboxApi().delete_outbox_fax_with_http_info(user_id, outbox_fax_id, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param str outbox_fax_id: ID of the outgoing fax to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None | tuple[None, int, HTTPHeaderDict] | ApplyResult[None] | ApplyResult[tuple[None, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'user_id' is set
        if user_id is None:
            raise ValueError("Missing the required parameter `user_id` when calling `delete_outbox_fax`")  # noqa: E501
        # verify the required parameter 'outbox_fax_id' is set
        if outbox_fax_id is None:
            raise ValueError("Missing the required parameter `outbox_fax_id` when calling `delete_outbox_fax`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if user_id is not None:
            path_params['user_id'] = user_id  # noqa: E501
        if outbox_fax_id is not None:
            path_params['outbox_fax_id'] = outbox_fax_id  # noqa: E501

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
            '/accounts/{user_id}/outbox/{outbox_fax_id}', 'DELETE',
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

    def get_outbox_fax(self, user_id, outbox_fax_id, **kwargs):  # noqa: E501
        """List outgoing faxes  # noqa: E501

        Get a list of faxes currently scheduled for sending  # noqa: E501
        >>> result = OutboxApi().get_outbox_fax(user_id, outbox_fax_id, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = OutboxApi().get_outbox_fax(user_id, outbox_fax_id, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param str outbox_fax_id: ID of the outgoing fax to get (required)
        :return: Outbox
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Outbox | ApplyResult[Outbox]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_outbox_fax_with_http_info(user_id, outbox_fax_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_outbox_fax_with_http_info(user_id, outbox_fax_id, **kwargs)  # noqa: E501
            return data

    def get_outbox_fax_with_http_info(self, user_id, outbox_fax_id, **kwargs):  # noqa: E501
        """List outgoing faxes  # noqa: E501

        The difference between this method and `get_outbox_fax` is that this method may return not only the data,
        but also HTTP status and headers.

        Get a list of faxes currently scheduled for sending  # noqa: E501
        >>> result = OutboxApi().get_outbox_fax_with_http_info(user_id, outbox_fax_id, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = OutboxApi().get_outbox_fax_with_http_info(user_id, outbox_fax_id, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param str outbox_fax_id: ID of the outgoing fax to get (required)
        :return: Outbox
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Outbox | tuple[Outbox, int, HTTPHeaderDict] | ApplyResult[Outbox] | ApplyResult[tuple[Outbox, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'user_id' is set
        if user_id is None:
            raise ValueError("Missing the required parameter `user_id` when calling `get_outbox_fax`")  # noqa: E501
        # verify the required parameter 'outbox_fax_id' is set
        if outbox_fax_id is None:
            raise ValueError("Missing the required parameter `outbox_fax_id` when calling `get_outbox_fax`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if user_id is not None:
            path_params['user_id'] = user_id  # noqa: E501
        if outbox_fax_id is not None:
            path_params['outbox_fax_id'] = outbox_fax_id  # noqa: E501

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
            '/accounts/{user_id}/outbox/{outbox_fax_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Outbox',  # noqa: E501
            auth_settings=auth_settings,
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_outbox_faxes(self, user_id, **kwargs):  # noqa: E501
        """List faxes in the outbox  # noqa: E501

        Get a list of the faxes in the outbox which were not yet sent  # noqa: E501
        >>> result = OutboxApi().list_outbox_faxes(user_id, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = OutboxApi().list_outbox_faxes(user_id, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :return: OutboxList
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: OutboxList | ApplyResult[OutboxList]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_outbox_faxes_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_outbox_faxes_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def list_outbox_faxes_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """List faxes in the outbox  # noqa: E501

        The difference between this method and `list_outbox_faxes` is that this method may return not only the data,
        but also HTTP status and headers.

        Get a list of the faxes in the outbox which were not yet sent  # noqa: E501
        >>> result = OutboxApi().list_outbox_faxes_with_http_info(user_id, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = OutboxApi().list_outbox_faxes_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :return: OutboxList
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: OutboxList | tuple[OutboxList, int, HTTPHeaderDict] | ApplyResult[OutboxList] | ApplyResult[tuple[OutboxList, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'user_id' is set
        if user_id is None:
            raise ValueError("Missing the required parameter `user_id` when calling `list_outbox_faxes`")  # noqa: E501

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
            '/accounts/{user_id}/outbox', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OutboxList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_fax(self, user_id, body=None, **kwargs):  # noqa: E501
        """Send a fax  # noqa: E501

        Send a fax to one or more destinations. For corporate members without a fax number assigned set the 'from' parameter to 'no_number'  # noqa: E501
        >>> result = OutboxApi().send_fax(user_id, body, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = OutboxApi().send_fax(user_id, body, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param PayloadOutbox body: Request to send new outbound fax
        :return: SendFaxResponse
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SendFaxResponse | ApplyResult[SendFaxResponse]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.send_fax_with_http_info(user_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.send_fax_with_http_info(user_id, body, **kwargs)  # noqa: E501
            return data

    def send_fax_with_http_info(self, user_id, body=None, **kwargs):  # noqa: E501
        """Send a fax  # noqa: E501

        The difference between this method and `send_fax` is that this method may return not only the data,
        but also HTTP status and headers.

        Send a fax to one or more destinations. For corporate members without a fax number assigned set the 'from' parameter to 'no_number'  # noqa: E501
        >>> result = OutboxApi().send_fax_with_http_info(user_id, body, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = OutboxApi().send_fax_with_http_info(user_id, body, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param PayloadOutbox body: Request to send new outbound fax
        :return: SendFaxResponse
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SendFaxResponse | tuple[SendFaxResponse, int, HTTPHeaderDict] | ApplyResult[SendFaxResponse] | ApplyResult[tuple[SendFaxResponse, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'user_id' is set
        if user_id is None:
            raise ValueError("Missing the required parameter `user_id` when calling `send_fax`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if user_id is not None:
            path_params['user_id'] = user_id  # noqa: E501

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
            '/accounts/{user_id}/outbox', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SendFaxResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_outbox_fax(self, user_id, outbox_fax_id, body=None, **kwargs):  # noqa: E501
        """Modify an outgoing fax  # noqa: E501

        Modify an outgoing fax that is being scheduled for sending  # noqa: E501
        >>> result = OutboxApi().update_outbox_fax(user_id, outbox_fax_id, body, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = OutboxApi().update_outbox_fax(user_id, outbox_fax_id, body, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param str outbox_fax_id: ID of the outgoing fax to update (required)
        :param PayloadOutboxModification body: Request object for making changes in an outbox object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None | ApplyResult[None]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_outbox_fax_with_http_info(user_id, outbox_fax_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_outbox_fax_with_http_info(user_id, outbox_fax_id, body, **kwargs)  # noqa: E501
            return data

    def update_outbox_fax_with_http_info(self, user_id, outbox_fax_id, body=None, **kwargs):  # noqa: E501
        """Modify an outgoing fax  # noqa: E501

        The difference between this method and `update_outbox_fax` is that this method may return not only the data,
        but also HTTP status and headers.

        Modify an outgoing fax that is being scheduled for sending  # noqa: E501
        >>> result = OutboxApi().update_outbox_fax_with_http_info(user_id, outbox_fax_id, body, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = OutboxApi().update_outbox_fax_with_http_info(user_id, outbox_fax_id, body, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: self or user id of a corporate member (required)
        :param str outbox_fax_id: ID of the outgoing fax to update (required)
        :param PayloadOutboxModification body: Request object for making changes in an outbox object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None | tuple[None, int, HTTPHeaderDict] | ApplyResult[None] | ApplyResult[tuple[None, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'user_id' is set
        if user_id is None:
            raise ValueError("Missing the required parameter `user_id` when calling `update_outbox_fax`")  # noqa: E501
        # verify the required parameter 'outbox_fax_id' is set
        if outbox_fax_id is None:
            raise ValueError("Missing the required parameter `outbox_fax_id` when calling `update_outbox_fax`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if user_id is not None:
            path_params['user_id'] = user_id  # noqa: E501
        if outbox_fax_id is not None:
            path_params['outbox_fax_id'] = outbox_fax_id  # noqa: E501

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
            '/accounts/{user_id}/outbox/{outbox_fax_id}', 'PUT',
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
