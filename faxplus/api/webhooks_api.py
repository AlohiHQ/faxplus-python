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


class WebhooksApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_webhook(self, body=None, **kwargs):  # noqa: E501
        """Register new webhook  # noqa: E501

        Register a new webhook which will be called on a specific event. See the WebhookCallback model  # noqa: E501
        >>> result = WebhooksApi().create_webhook(body, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = WebhooksApi().create_webhook(body, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param Webhook body: Request to create new webhook
        :return: WebhookId
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WebhookId | ApplyResult[WebhookId]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_webhook_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_webhook_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_webhook_with_http_info(self, body=None, **kwargs):  # noqa: E501
        """Register new webhook  # noqa: E501

        The difference between this method and `create_webhook` is that this method may return not only the data,
        but also HTTP status and headers.

        Register a new webhook which will be called on a specific event. See the WebhookCallback model  # noqa: E501
        >>> result = WebhooksApi().create_webhook_with_http_info(body, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = WebhooksApi().create_webhook_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param Webhook body: Request to create new webhook
        :return: WebhookId
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WebhookId | tuple[WebhookId, int, HTTPHeaderDict] | ApplyResult[WebhookId] | ApplyResult[tuple[WebhookId, int, HTTPHeaderDict]]
        """

        collection_formats = {}

        path_params = {}

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
            '/hooks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebhookId',  # noqa: E501
            auth_settings=auth_settings,
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_webhook(self, hook_id, **kwargs):  # noqa: E501
        """Delete webhook  # noqa: E501

        Delete a webhook by its ID  # noqa: E501
        >>> result = WebhooksApi().delete_webhook(hook_id, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = WebhooksApi().delete_webhook(hook_id, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str hook_id: ID of the webhook to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None | ApplyResult[None]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_webhook_with_http_info(hook_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_webhook_with_http_info(hook_id, **kwargs)  # noqa: E501
            return data

    def delete_webhook_with_http_info(self, hook_id, **kwargs):  # noqa: E501
        """Delete webhook  # noqa: E501

        The difference between this method and `delete_webhook` is that this method may return not only the data,
        but also HTTP status and headers.

        Delete a webhook by its ID  # noqa: E501
        >>> result = WebhooksApi().delete_webhook_with_http_info(hook_id, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = WebhooksApi().delete_webhook_with_http_info(hook_id, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str hook_id: ID of the webhook to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None | tuple[None, int, HTTPHeaderDict] | ApplyResult[None] | ApplyResult[tuple[None, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'hook_id' is set
        if hook_id is None:
            raise ValueError("Missing the required parameter `hook_id` when calling `delete_webhook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if hook_id is not None:
            path_params['hook_id'] = hook_id  # noqa: E501

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
            '/hooks/{hook_id}', 'DELETE',
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

    def get_webhooks(self, event, **kwargs):  # noqa: E501
        """List user webhooks  # noqa: E501

        Returns a list of currently registered webhooks for the requested **event**  # noqa: E501
        >>> result = WebhooksApi().get_webhooks(event, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = WebhooksApi().get_webhooks(event, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param WebhookEventType event: (required)
        :return: WebhookList
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WebhookList | ApplyResult[WebhookList]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_webhooks_with_http_info(event, **kwargs)  # noqa: E501
        else:
            (data) = self.get_webhooks_with_http_info(event, **kwargs)  # noqa: E501
            return data

    def get_webhooks_with_http_info(self, event, **kwargs):  # noqa: E501
        """List user webhooks  # noqa: E501

        The difference between this method and `get_webhooks` is that this method may return not only the data,
        but also HTTP status and headers.

        Returns a list of currently registered webhooks for the requested **event**  # noqa: E501
        >>> result = WebhooksApi().get_webhooks_with_http_info(event, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = WebhooksApi().get_webhooks_with_http_info(event, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param WebhookEventType event: (required)
        :return: WebhookList
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WebhookList | tuple[WebhookList, int, HTTPHeaderDict] | ApplyResult[WebhookList] | ApplyResult[tuple[WebhookList, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'event' is set
        if event is None:
            raise ValueError("Missing the required parameter `event` when calling `get_webhooks`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if event is not None:
            query_params.append(('event', event))  # noqa: E501

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
            '/hooks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebhookList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats=collection_formats)
