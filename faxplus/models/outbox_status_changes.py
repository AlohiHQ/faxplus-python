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


class OutboxStatusChanges(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'at': 'str',
        'status': 'OutboxStatus'
    }

    attribute_map = {
        'at': 'at',
        'status': 'status'
    }

    def __init__(self, at=None, status=None):  # noqa: E501
        """OutboxStatusChanges - a model defined in Swagger

        :param str at: Date and time at which status changed. Format: *YYYY-MM-DD HH:mm:ss* (required)
        :param OutboxStatus status: (required)
        """  # noqa: E501
        self._at = None
        self._status = None
        self.discriminator = None
        self.at = at
        self.status = status

    @property
    def at(self):
        """Gets the at of this OutboxStatusChanges.  # noqa: E501

        Date and time at which status changed. Format: *YYYY-MM-DD HH:mm:ss*  # noqa: E501

        :return: The at of this OutboxStatusChanges.  # noqa: E501
        :rtype: str
        """
        return self._at

    @at.setter
    def at(self, at):
        """Sets the at of this OutboxStatusChanges.

        Date and time at which status changed. Format: *YYYY-MM-DD HH:mm:ss*  # noqa: E501

        :param at: The at of this OutboxStatusChanges.  # noqa: E501
        :type: str
        """
        if at is None:
            raise ValueError("Invalid value for `at`, must not be `None`")  # noqa: E501
        if at and not re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}', at):  # noqa: E501
            raise ValueError(r"Invalid value for `at`, must be a follow pattern or equal to `/^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}/`")  # noqa: E501

        self._at = at

    @property
    def status(self):
        """Gets the status of this OutboxStatusChanges.  # noqa: E501


        :return: The status of this OutboxStatusChanges.  # noqa: E501
        :rtype: OutboxStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OutboxStatusChanges.


        :param status: The status of this OutboxStatusChanges.  # noqa: E501
        :type: OutboxStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if issubclass(OutboxStatusChanges, dict):
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
        if not isinstance(other, OutboxStatusChanges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

