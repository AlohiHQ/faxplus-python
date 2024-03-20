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


class AccountNotifications(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'black_list': 'AccountNotificationsBlacklist',
        'settings': 'AccountNotificationsSettings'
    }

    attribute_map = {
        'black_list': 'black_list',
        'settings': 'settings'
    }

    def __init__(self, black_list=None, settings=None):  # noqa: E501
        """AccountNotifications - a model defined in Swagger

        :param AccountNotificationsBlacklist black_list:
        :param AccountNotificationsSettings settings: (required)
        """  # noqa: E501
        self._black_list = None
        self._settings = None
        self.discriminator = None
        if black_list is not None:
            self.black_list = black_list
        self.settings = settings

    @property
    def black_list(self):
        """Gets the black_list of this AccountNotifications.  # noqa: E501


        :return: The black_list of this AccountNotifications.  # noqa: E501
        :rtype: AccountNotificationsBlacklist
        """
        return self._black_list

    @black_list.setter
    def black_list(self, black_list):
        """Sets the black_list of this AccountNotifications.


        :param black_list: The black_list of this AccountNotifications.  # noqa: E501
        :type: AccountNotificationsBlacklist
        """

        self._black_list = black_list

    @property
    def settings(self):
        """Gets the settings of this AccountNotifications.  # noqa: E501


        :return: The settings of this AccountNotifications.  # noqa: E501
        :rtype: AccountNotificationsSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this AccountNotifications.


        :param settings: The settings of this AccountNotifications.  # noqa: E501
        :type: AccountNotificationsSettings
        """
        if settings is None:
            raise ValueError("Invalid value for `settings`, must not be `None`")  # noqa: E501

        self._settings = settings

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
        if issubclass(AccountNotifications, dict):
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
        if not isinstance(other, AccountNotifications):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

