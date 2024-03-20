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


class PayloadFaxModification(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'comment': 'str',
        'is_read': 'bool'
    }

    attribute_map = {
        'comment': 'comment',
        'is_read': 'is_read'
    }

    def __init__(self, comment=None, is_read=None):  # noqa: E501
        """PayloadFaxModification - a model defined in Swagger

        :param str comment: (required)
        :param bool is_read: (required)
        """  # noqa: E501
        self._comment = None
        self._is_read = None
        self.discriminator = None
        self.comment = comment
        self.is_read = is_read

    @property
    def comment(self):
        """Gets the comment of this PayloadFaxModification.  # noqa: E501


        :return: The comment of this PayloadFaxModification.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this PayloadFaxModification.


        :param comment: The comment of this PayloadFaxModification.  # noqa: E501
        :type: str
        """
        if comment is None:
            raise ValueError("Invalid value for `comment`, must not be `None`")  # noqa: E501

        self._comment = comment

    @property
    def is_read(self):
        """Gets the is_read of this PayloadFaxModification.  # noqa: E501


        :return: The is_read of this PayloadFaxModification.  # noqa: E501
        :rtype: bool
        """
        return self._is_read

    @is_read.setter
    def is_read(self, is_read):
        """Sets the is_read of this PayloadFaxModification.


        :param is_read: The is_read of this PayloadFaxModification.  # noqa: E501
        :type: bool
        """
        if is_read is None:
            raise ValueError("Invalid value for `is_read`, must not be `None`")  # noqa: E501

        self._is_read = is_read

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
        if issubclass(PayloadFaxModification, dict):
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
        if not isinstance(other, PayloadFaxModification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

