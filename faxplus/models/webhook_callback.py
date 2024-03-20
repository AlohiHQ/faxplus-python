# coding: utf-8

"""
    Fax.Plus REST API

    Visit https://apidoc.fax.plus for more information.

    © Alohi SA (Geneva, Switzerland)

    https://www.alohi.com
    Contact: info@fax.plus
"""

import pprint
import re  # noqa: F401

import six
from faxplus.models import *


class WebhookCallback(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'hook': 'WebhookCallbackHook',
        'data': 'WebhookCallbackData'
    }

    attribute_map = {
        'hook': 'hook',
        'data': 'data'
    }

    def __init__(self, hook=None, data=None):  # noqa: E501
        """WebhookCallback - a model defined in Swagger

        :param WebhookCallbackHook hook:
        :param WebhookCallbackData data:
        """  # noqa: E501
        self._hook = None
        self._data = None
        self.discriminator = None
        if hook is not None:
            self.hook = hook
        if data is not None:
            self.data = data

    @property
    def hook(self):
        """Gets the hook of this WebhookCallback.  # noqa: E501


        :return: The hook of this WebhookCallback.  # noqa: E501
        :rtype: WebhookCallbackHook
        """
        return self._hook

    @hook.setter
    def hook(self, hook):
        """Sets the hook of this WebhookCallback.


        :param hook: The hook of this WebhookCallback.  # noqa: E501
        :type: WebhookCallbackHook
        """

        self._hook = hook

    @property
    def data(self):
        """Gets the data of this WebhookCallback.  # noqa: E501


        :return: The data of this WebhookCallback.  # noqa: E501
        :rtype: WebhookCallbackData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this WebhookCallback.


        :param data: The data of this WebhookCallback.  # noqa: E501
        :type: WebhookCallbackData
        """

        self._data = data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(WebhookCallback, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WebhookCallback):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

