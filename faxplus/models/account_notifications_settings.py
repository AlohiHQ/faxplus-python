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


class AccountNotificationsSettings(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'email': 'AccountNotificationsEmailSettings',
        'language': 'AccountNotificationsLanguage',
        'push_notifications': 'AccountNotificationsPushSettings',
        'slack': 'AccountNotificationsSlackSettings',
        'sms': 'AccountNotificationsSmsSettings'
    }

    attribute_map = {
        'email': 'email',
        'language': 'language',
        'push_notifications': 'push_notifications',
        'slack': 'slack',
        'sms': 'sms'
    }

    def __init__(self, email=None, language=None, push_notifications=None, slack=None, sms=None):  # noqa: E501
        """AccountNotificationsSettings - a model defined in Swagger

        :param AccountNotificationsEmailSettings email: (required)
        :param AccountNotificationsLanguage language:
        :param AccountNotificationsPushSettings push_notifications: (required)
        :param AccountNotificationsSlackSettings slack:
        :param AccountNotificationsSmsSettings sms: (required)
        """  # noqa: E501
        self._email = None
        self._language = None
        self._push_notifications = None
        self._slack = None
        self._sms = None
        self.discriminator = None
        self.email = email
        if language is not None:
            self.language = language
        self.push_notifications = push_notifications
        if slack is not None:
            self.slack = slack
        self.sms = sms

    @property
    def email(self):
        """Gets the email of this AccountNotificationsSettings.  # noqa: E501


        :return: The email of this AccountNotificationsSettings.  # noqa: E501
        :rtype: AccountNotificationsEmailSettings
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AccountNotificationsSettings.


        :param email: The email of this AccountNotificationsSettings.  # noqa: E501
        :type: AccountNotificationsEmailSettings
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def language(self):
        """Gets the language of this AccountNotificationsSettings.  # noqa: E501


        :return: The language of this AccountNotificationsSettings.  # noqa: E501
        :rtype: AccountNotificationsLanguage
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this AccountNotificationsSettings.


        :param language: The language of this AccountNotificationsSettings.  # noqa: E501
        :type: AccountNotificationsLanguage
        """

        self._language = language

    @property
    def push_notifications(self):
        """Gets the push_notifications of this AccountNotificationsSettings.  # noqa: E501


        :return: The push_notifications of this AccountNotificationsSettings.  # noqa: E501
        :rtype: AccountNotificationsPushSettings
        """
        return self._push_notifications

    @push_notifications.setter
    def push_notifications(self, push_notifications):
        """Sets the push_notifications of this AccountNotificationsSettings.


        :param push_notifications: The push_notifications of this AccountNotificationsSettings.  # noqa: E501
        :type: AccountNotificationsPushSettings
        """
        if push_notifications is None:
            raise ValueError("Invalid value for `push_notifications`, must not be `None`")  # noqa: E501

        self._push_notifications = push_notifications

    @property
    def slack(self):
        """Gets the slack of this AccountNotificationsSettings.  # noqa: E501


        :return: The slack of this AccountNotificationsSettings.  # noqa: E501
        :rtype: AccountNotificationsSlackSettings
        """
        return self._slack

    @slack.setter
    def slack(self, slack):
        """Sets the slack of this AccountNotificationsSettings.


        :param slack: The slack of this AccountNotificationsSettings.  # noqa: E501
        :type: AccountNotificationsSlackSettings
        """

        self._slack = slack

    @property
    def sms(self):
        """Gets the sms of this AccountNotificationsSettings.  # noqa: E501


        :return: The sms of this AccountNotificationsSettings.  # noqa: E501
        :rtype: AccountNotificationsSmsSettings
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this AccountNotificationsSettings.


        :param sms: The sms of this AccountNotificationsSettings.  # noqa: E501
        :type: AccountNotificationsSmsSettings
        """
        if sms is None:
            raise ValueError("Invalid value for `sms`, must not be `None`")  # noqa: E501

        self._sms = sms

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
        if issubclass(AccountNotificationsSettings, dict):
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
        if not isinstance(other, AccountNotificationsSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

