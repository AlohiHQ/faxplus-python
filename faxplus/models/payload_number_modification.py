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


class PayloadNumberModification(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'assigned_to': 'str'
    }

    attribute_map = {
        'assigned_to': 'assigned_to'
    }

    def __init__(self, assigned_to=None):  # noqa: E501
        """PayloadNumberModification - a model defined in Swagger

        :param str assigned_to: User ID of the account to assign number to (required)
        """  # noqa: E501
        self._assigned_to = None
        self.discriminator = None
        self.assigned_to = assigned_to

    @property
    def assigned_to(self):
        """Gets the assigned_to of this PayloadNumberModification.  # noqa: E501

        User ID of the account to assign number to  # noqa: E501

        :return: The assigned_to of this PayloadNumberModification.  # noqa: E501
        :rtype: str
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to):
        """Sets the assigned_to of this PayloadNumberModification.

        User ID of the account to assign number to  # noqa: E501

        :param assigned_to: The assigned_to of this PayloadNumberModification.  # noqa: E501
        :type: str
        """
        if assigned_to is None:
            raise ValueError("Invalid value for `assigned_to`, must not be `None`")  # noqa: E501

        self._assigned_to = assigned_to

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
        if issubclass(PayloadNumberModification, dict):
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
        if not isinstance(other, PayloadNumberModification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

