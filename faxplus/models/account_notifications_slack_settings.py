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


class AccountNotificationsSlackSettings(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'receive_fax': 'SlackNotificationMode',
        'send_fax': 'SlackNotificationMode',
        'target_channel': 'str'
    }

    attribute_map = {
        'receive_fax': 'receive_fax',
        'send_fax': 'send_fax',
        'target_channel': 'target_channel'
    }

    def __init__(self, receive_fax=None, send_fax=None, target_channel=None):  # noqa: E501
        """AccountNotificationsSlackSettings - a model defined in Swagger

        :param SlackNotificationMode receive_fax: (required)
        :param SlackNotificationMode send_fax: (required)
        :param str target_channel: Channel to send notifications (required)
        """  # noqa: E501
        self._receive_fax = None
        self._send_fax = None
        self._target_channel = None
        self.discriminator = None
        self.receive_fax = receive_fax
        self.send_fax = send_fax
        self.target_channel = target_channel

    @property
    def receive_fax(self):
        """Gets the receive_fax of this AccountNotificationsSlackSettings.  # noqa: E501


        :return: The receive_fax of this AccountNotificationsSlackSettings.  # noqa: E501
        :rtype: SlackNotificationMode
        """
        return self._receive_fax

    @receive_fax.setter
    def receive_fax(self, receive_fax):
        """Sets the receive_fax of this AccountNotificationsSlackSettings.


        :param receive_fax: The receive_fax of this AccountNotificationsSlackSettings.  # noqa: E501
        :type: SlackNotificationMode
        """
        if receive_fax is None:
            raise ValueError("Invalid value for `receive_fax`, must not be `None`")  # noqa: E501

        self._receive_fax = receive_fax

    @property
    def send_fax(self):
        """Gets the send_fax of this AccountNotificationsSlackSettings.  # noqa: E501


        :return: The send_fax of this AccountNotificationsSlackSettings.  # noqa: E501
        :rtype: SlackNotificationMode
        """
        return self._send_fax

    @send_fax.setter
    def send_fax(self, send_fax):
        """Sets the send_fax of this AccountNotificationsSlackSettings.


        :param send_fax: The send_fax of this AccountNotificationsSlackSettings.  # noqa: E501
        :type: SlackNotificationMode
        """
        if send_fax is None:
            raise ValueError("Invalid value for `send_fax`, must not be `None`")  # noqa: E501

        self._send_fax = send_fax

    @property
    def target_channel(self):
        """Gets the target_channel of this AccountNotificationsSlackSettings.  # noqa: E501

        Channel to send notifications  # noqa: E501

        :return: The target_channel of this AccountNotificationsSlackSettings.  # noqa: E501
        :rtype: str
        """
        return self._target_channel

    @target_channel.setter
    def target_channel(self, target_channel):
        """Sets the target_channel of this AccountNotificationsSlackSettings.

        Channel to send notifications  # noqa: E501

        :param target_channel: The target_channel of this AccountNotificationsSlackSettings.  # noqa: E501
        :type: str
        """
        if target_channel is None:
            raise ValueError("Invalid value for `target_channel`, must not be `None`")  # noqa: E501

        self._target_channel = target_channel

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
        if issubclass(AccountNotificationsSlackSettings, dict):
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
        if not isinstance(other, AccountNotificationsSlackSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

