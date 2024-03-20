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


class AccountNotificationsBlacklist(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'uids': 'list[str]'
    }

    attribute_map = {
        'uids': 'uids'
    }

    def __init__(self, uids=None):  # noqa: E501
        """AccountNotificationsBlacklist - a model defined in Swagger

        :param list[str] uids: (required)
        """  # noqa: E501
        self._uids = None
        self.discriminator = None
        self.uids = uids

    @property
    def uids(self):
        """Gets the uids of this AccountNotificationsBlacklist.  # noqa: E501


        :return: The uids of this AccountNotificationsBlacklist.  # noqa: E501
        :rtype: list[str]
        """
        return self._uids

    @uids.setter
    def uids(self, uids):
        """Sets the uids of this AccountNotificationsBlacklist.


        :param uids: The uids of this AccountNotificationsBlacklist.  # noqa: E501
        :type: list[str]
        """
        if uids is None:
            raise ValueError("Invalid value for `uids`, must not be `None`")  # noqa: E501

        self._uids = uids

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
        if issubclass(AccountNotificationsBlacklist, dict):
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
        if not isinstance(other, AccountNotificationsBlacklist):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

