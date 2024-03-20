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


class OutboxFileChanges(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'at': 'str',
        'files': 'list[OutboxFiles]'
    }

    attribute_map = {
        'at': 'at',
        'files': 'files'
    }

    def __init__(self, at=None, files=None):  # noqa: E501
        """OutboxFileChanges - a model defined in Swagger

        :param str at:
        :param list[OutboxFiles] files:
        """  # noqa: E501
        self._at = None
        self._files = None
        self.discriminator = None
        if at is not None:
            self.at = at
        if files is not None:
            self.files = files

    @property
    def at(self):
        """Gets the at of this OutboxFileChanges.  # noqa: E501


        :return: The at of this OutboxFileChanges.  # noqa: E501
        :rtype: str
        """
        return self._at

    @at.setter
    def at(self, at):
        """Sets the at of this OutboxFileChanges.


        :param at: The at of this OutboxFileChanges.  # noqa: E501
        :type: str
        """

        self._at = at

    @property
    def files(self):
        """Gets the files of this OutboxFileChanges.  # noqa: E501


        :return: The files of this OutboxFileChanges.  # noqa: E501
        :rtype: list[OutboxFiles]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this OutboxFileChanges.


        :param files: The files of this OutboxFileChanges.  # noqa: E501
        :type: list[OutboxFiles]
        """

        self._files = files

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
        if issubclass(OutboxFileChanges, dict):
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
        if not isinstance(other, OutboxFileChanges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

