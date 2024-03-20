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


class AccountsApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_accounts(self, **kwargs):  # noqa: E501
        """List corporate members  # noqa: E501

        Get account information of all non-admin members of your corporate account. Only the admin account can send a request to this endpoint which returns the accounts of all members  # noqa: E501
        >>> result = AccountsApi().get_accounts()

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = AccountsApi().get_accounts(async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :return: AccountList
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AccountList | ApplyResult[AccountList]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_accounts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_accounts_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_accounts_with_http_info(self, **kwargs):  # noqa: E501
        """List corporate members  # noqa: E501

        The difference between this method and `get_accounts` is that this method may return not only the data,
        but also HTTP status and headers.

        Get account information of all non-admin members of your corporate account. Only the admin account can send a request to this endpoint which returns the accounts of all members  # noqa: E501
        >>> result = AccountsApi().get_accounts_with_http_info()

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = AccountsApi().get_accounts_with_http_info(async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :return: AccountList
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AccountList | tuple[AccountList, int, HTTPHeaderDict] | ApplyResult[AccountList] | ApplyResult[tuple[AccountList, int, HTTPHeaderDict]]
        """

        collection_formats = {}

        path_params = {}

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
            '/accounts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_member_details(self, member_user_id, **kwargs):  # noqa: E501
        """Get member details  # noqa: E501

        Get corporate member's role and faxing quota  # noqa: E501
        >>> result = AccountsApi().get_member_details(member_user_id, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = AccountsApi().get_member_details(member_user_id, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str member_user_id: Member user ID (required)
        :return: MemberDetail
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MemberDetail | ApplyResult[MemberDetail]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_member_details_with_http_info(member_user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_member_details_with_http_info(member_user_id, **kwargs)  # noqa: E501
            return data

    def get_member_details_with_http_info(self, member_user_id, **kwargs):  # noqa: E501
        """Get member details  # noqa: E501

        The difference between this method and `get_member_details` is that this method may return not only the data,
        but also HTTP status and headers.

        Get corporate member's role and faxing quota  # noqa: E501
        >>> result = AccountsApi().get_member_details_with_http_info(member_user_id, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = AccountsApi().get_member_details_with_http_info(member_user_id, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str member_user_id: Member user ID (required)
        :return: MemberDetail
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MemberDetail | tuple[MemberDetail, int, HTTPHeaderDict] | ApplyResult[MemberDetail] | ApplyResult[tuple[MemberDetail, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'member_user_id' is set
        if member_user_id is None:
            raise ValueError("Missing the required parameter `member_user_id` when calling `get_member_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if member_user_id is not None:
            path_params['member_user_id'] = member_user_id  # noqa: E501

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
            '/accounts/self/member-details/{member_user_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MemberDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user(self, user_id, **kwargs):  # noqa: E501
        """Get account information  # noqa: E501

        Get information about an account. For members user_id can only be self. For admin it can be either self, or a user_id of any corporate member  # noqa: E501
        >>> result = AccountsApi().get_user(user_id, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = AccountsApi().get_user(user_id, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: User ID to get information about. For your own account use **'self'** (required)
        :return: Account
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Account | ApplyResult[Account]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def get_user_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Get account information  # noqa: E501

        The difference between this method and `get_user` is that this method may return not only the data,
        but also HTTP status and headers.

        Get information about an account. For members user_id can only be self. For admin it can be either self, or a user_id of any corporate member  # noqa: E501
        >>> result = AccountsApi().get_user_with_http_info(user_id, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = AccountsApi().get_user_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: User ID to get information about. For your own account use **'self'** (required)
        :return: Account
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Account | tuple[Account, int, HTTPHeaderDict] | ApplyResult[Account] | ApplyResult[tuple[Account, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'user_id' is set
        if user_id is None:
            raise ValueError("Missing the required parameter `user_id` when calling `get_user`")  # noqa: E501

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
            '/accounts/{user_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Account',  # noqa: E501
            auth_settings=auth_settings,
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_member_details(self, member_user_id, body=None, **kwargs):  # noqa: E501
        """Modify member details  # noqa: E501

        Update corporate member's role and faxing quota  # noqa: E501
        >>> result = AccountsApi().update_member_details(member_user_id, body, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = AccountsApi().update_member_details(member_user_id, body, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str member_user_id: Member user ID (required)
        :param MemberDetail body: Request object for making changes in member details
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None | ApplyResult[None]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_member_details_with_http_info(member_user_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_member_details_with_http_info(member_user_id, body, **kwargs)  # noqa: E501
            return data

    def update_member_details_with_http_info(self, member_user_id, body=None, **kwargs):  # noqa: E501
        """Modify member details  # noqa: E501

        The difference between this method and `update_member_details` is that this method may return not only the data,
        but also HTTP status and headers.

        Update corporate member's role and faxing quota  # noqa: E501
        >>> result = AccountsApi().update_member_details_with_http_info(member_user_id, body, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = AccountsApi().update_member_details_with_http_info(member_user_id, body, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str member_user_id: Member user ID (required)
        :param MemberDetail body: Request object for making changes in member details
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None | tuple[None, int, HTTPHeaderDict] | ApplyResult[None] | ApplyResult[tuple[None, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'member_user_id' is set
        if member_user_id is None:
            raise ValueError("Missing the required parameter `member_user_id` when calling `update_member_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if member_user_id is not None:
            path_params['member_user_id'] = member_user_id  # noqa: E501

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
            '/accounts/self/member-details/{member_user_id}', 'PUT',
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

    def update_user(self, user_id, body=None, **kwargs):  # noqa: E501
        """Modify account information  # noqa: E501

        Modify personal information of your own account or your corporate member's account. user_id can be either self, or a subordinate's user_id  # noqa: E501
        >>> result = AccountsApi().update_user(user_id, body, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = AccountsApi().update_user(user_id, body, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: User ID to get information about. For your own account use **'self'** (required)
        :param PayloadAccountModification body: Request object for making changes in account
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None | ApplyResult[None]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_user_with_http_info(user_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_user_with_http_info(user_id, body, **kwargs)  # noqa: E501
            return data

    def update_user_with_http_info(self, user_id, body=None, **kwargs):  # noqa: E501
        """Modify account information  # noqa: E501

        The difference between this method and `update_user` is that this method may return not only the data,
        but also HTTP status and headers.

        Modify personal information of your own account or your corporate member's account. user_id can be either self, or a subordinate's user_id  # noqa: E501
        >>> result = AccountsApi().update_user_with_http_info(user_id, body, )

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = AccountsApi().update_user_with_http_info(user_id, body, async_req=True)
        >>> result = thread.get()

        :keyword async_req bool: Run the request asynchronously
        :param str user_id: User ID to get information about. For your own account use **'self'** (required)
        :param PayloadAccountModification body: Request object for making changes in account
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None | tuple[None, int, HTTPHeaderDict] | ApplyResult[None] | ApplyResult[tuple[None, int, HTTPHeaderDict]]
        """
        # verify the required parameter 'user_id' is set
        if user_id is None:
            raise ValueError("Missing the required parameter `user_id` when calling `update_user`")  # noqa: E501

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
            '/accounts/{user_id}', 'PUT',
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
