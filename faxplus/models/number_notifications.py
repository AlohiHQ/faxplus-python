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


class NumberNotifications(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'email': 'bool',
        'push_notification': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'email': 'email',
        'push_notification': 'push_notification',
        'type': 'type'
    }

    def __init__(self, email=None, push_notification=None, type=None):  # noqa: E501
        """NumberNotifications - a model defined in Swagger

        :param bool email:
        :param bool push_notification:
        :param str type:
        """  # noqa: E501
        self._email = None
        self._push_notification = None
        self._type = None
        self.discriminator = None
        if email is not None:
            self.email = email
        if push_notification is not None:
            self.push_notification = push_notification
        if type is not None:
            self.type = type

    @property
    def email(self):
        """Gets the email of this NumberNotifications.  # noqa: E501


        :return: The email of this NumberNotifications.  # noqa: E501
        :rtype: bool
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this NumberNotifications.


        :param email: The email of this NumberNotifications.  # noqa: E501
        :type: bool
        """

        self._email = email

    @property
    def push_notification(self):
        """Gets the push_notification of this NumberNotifications.  # noqa: E501


        :return: The push_notification of this NumberNotifications.  # noqa: E501
        :rtype: bool
        """
        return self._push_notification

    @push_notification.setter
    def push_notification(self, push_notification):
        """Sets the push_notification of this NumberNotifications.


        :param push_notification: The push_notification of this NumberNotifications.  # noqa: E501
        :type: bool
        """

        self._push_notification = push_notification

    @property
    def type(self):
        """Gets the type of this NumberNotifications.  # noqa: E501


        :return: The type of this NumberNotifications.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NumberNotifications.


        :param type: The type of this NumberNotifications.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(NumberNotifications, dict):
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
        if not isinstance(other, NumberNotifications):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

