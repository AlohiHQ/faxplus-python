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


class AccountNotificationsPushSettings(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'low_credit': 'bool',
        'new_feature': 'bool',
        'receive_fax': 'bool',
        'send_fax': 'bool',
        'voicemail': 'bool'
    }

    attribute_map = {
        'low_credit': 'low_credit',
        'new_feature': 'new_feature',
        'receive_fax': 'receive_fax',
        'send_fax': 'send_fax',
        'voicemail': 'voicemail'
    }

    def __init__(self, low_credit=None, new_feature=None, receive_fax=None, send_fax=None, voicemail=None):  # noqa: E501
        """AccountNotificationsPushSettings - a model defined in Swagger

        :param bool low_credit: Set to true if you want to receive notifications when your balance is low (required)
        :param bool new_feature: Set to true if you want to receive notifications about our new features (required)
        :param bool receive_fax: Set to true if you want to receive notifications about receiving faxes (required)
        :param bool send_fax: Set to true if you want to receive notifications when your fax is being send (required)
        :param bool voicemail: Set to true if you want to receive new voicemail notifications (required)
        """  # noqa: E501
        self._low_credit = None
        self._new_feature = None
        self._receive_fax = None
        self._send_fax = None
        self._voicemail = None
        self.discriminator = None
        self.low_credit = low_credit
        self.new_feature = new_feature
        self.receive_fax = receive_fax
        self.send_fax = send_fax
        self.voicemail = voicemail

    @property
    def low_credit(self):
        """Gets the low_credit of this AccountNotificationsPushSettings.  # noqa: E501

        Set to true if you want to receive notifications when your balance is low  # noqa: E501

        :return: The low_credit of this AccountNotificationsPushSettings.  # noqa: E501
        :rtype: bool
        """
        return self._low_credit

    @low_credit.setter
    def low_credit(self, low_credit):
        """Sets the low_credit of this AccountNotificationsPushSettings.

        Set to true if you want to receive notifications when your balance is low  # noqa: E501

        :param low_credit: The low_credit of this AccountNotificationsPushSettings.  # noqa: E501
        :type: bool
        """
        if low_credit is None:
            raise ValueError("Invalid value for `low_credit`, must not be `None`")  # noqa: E501

        self._low_credit = low_credit

    @property
    def new_feature(self):
        """Gets the new_feature of this AccountNotificationsPushSettings.  # noqa: E501

        Set to true if you want to receive notifications about our new features  # noqa: E501

        :return: The new_feature of this AccountNotificationsPushSettings.  # noqa: E501
        :rtype: bool
        """
        return self._new_feature

    @new_feature.setter
    def new_feature(self, new_feature):
        """Sets the new_feature of this AccountNotificationsPushSettings.

        Set to true if you want to receive notifications about our new features  # noqa: E501

        :param new_feature: The new_feature of this AccountNotificationsPushSettings.  # noqa: E501
        :type: bool
        """
        if new_feature is None:
            raise ValueError("Invalid value for `new_feature`, must not be `None`")  # noqa: E501

        self._new_feature = new_feature

    @property
    def receive_fax(self):
        """Gets the receive_fax of this AccountNotificationsPushSettings.  # noqa: E501

        Set to true if you want to receive notifications about receiving faxes  # noqa: E501

        :return: The receive_fax of this AccountNotificationsPushSettings.  # noqa: E501
        :rtype: bool
        """
        return self._receive_fax

    @receive_fax.setter
    def receive_fax(self, receive_fax):
        """Sets the receive_fax of this AccountNotificationsPushSettings.

        Set to true if you want to receive notifications about receiving faxes  # noqa: E501

        :param receive_fax: The receive_fax of this AccountNotificationsPushSettings.  # noqa: E501
        :type: bool
        """
        if receive_fax is None:
            raise ValueError("Invalid value for `receive_fax`, must not be `None`")  # noqa: E501

        self._receive_fax = receive_fax

    @property
    def send_fax(self):
        """Gets the send_fax of this AccountNotificationsPushSettings.  # noqa: E501

        Set to true if you want to receive notifications when your fax is being send  # noqa: E501

        :return: The send_fax of this AccountNotificationsPushSettings.  # noqa: E501
        :rtype: bool
        """
        return self._send_fax

    @send_fax.setter
    def send_fax(self, send_fax):
        """Sets the send_fax of this AccountNotificationsPushSettings.

        Set to true if you want to receive notifications when your fax is being send  # noqa: E501

        :param send_fax: The send_fax of this AccountNotificationsPushSettings.  # noqa: E501
        :type: bool
        """
        if send_fax is None:
            raise ValueError("Invalid value for `send_fax`, must not be `None`")  # noqa: E501

        self._send_fax = send_fax

    @property
    def voicemail(self):
        """Gets the voicemail of this AccountNotificationsPushSettings.  # noqa: E501

        Set to true if you want to receive new voicemail notifications  # noqa: E501

        :return: The voicemail of this AccountNotificationsPushSettings.  # noqa: E501
        :rtype: bool
        """
        return self._voicemail

    @voicemail.setter
    def voicemail(self, voicemail):
        """Sets the voicemail of this AccountNotificationsPushSettings.

        Set to true if you want to receive new voicemail notifications  # noqa: E501

        :param voicemail: The voicemail of this AccountNotificationsPushSettings.  # noqa: E501
        :type: bool
        """
        if voicemail is None:
            raise ValueError("Invalid value for `voicemail`, must not be `None`")  # noqa: E501

        self._voicemail = voicemail

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
        if issubclass(AccountNotificationsPushSettings, dict):
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
        if not isinstance(other, AccountNotificationsPushSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

