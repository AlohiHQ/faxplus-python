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


class RetryOptions(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'count': 'int',
        'delay': 'int'
    }

    attribute_map = {
        'count': 'count',
        'delay': 'delay'
    }

    def __init__(self, count=None, delay=None):  # noqa: E501
        """RetryOptions - a model defined in Swagger

        :param int count: Number of tries to send the fax
        :param int delay: Delay in seconds between two retries
        """  # noqa: E501
        self._count = None
        self._delay = None
        self.discriminator = None
        if count is not None:
            self.count = count
        if delay is not None:
            self.delay = delay

    @property
    def count(self):
        """Gets the count of this RetryOptions.  # noqa: E501

        Number of tries to send the fax  # noqa: E501

        :return: The count of this RetryOptions.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this RetryOptions.

        Number of tries to send the fax  # noqa: E501

        :param count: The count of this RetryOptions.  # noqa: E501
        :type: int
        """
        if count is not None and count > 3:  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value less than or equal to `3`")  # noqa: E501
        if count is not None and count < 0:  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._count = count

    @property
    def delay(self):
        """Gets the delay of this RetryOptions.  # noqa: E501

        Delay in seconds between two retries  # noqa: E501

        :return: The delay of this RetryOptions.  # noqa: E501
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this RetryOptions.

        Delay in seconds between two retries  # noqa: E501

        :param delay: The delay of this RetryOptions.  # noqa: E501
        :type: int
        """
        if delay is not None and delay > 30:  # noqa: E501
            raise ValueError("Invalid value for `delay`, must be a value less than or equal to `30`")  # noqa: E501
        if delay is not None and delay < 0:  # noqa: E501
            raise ValueError("Invalid value for `delay`, must be a value greater than or equal to `0`")  # noqa: E501

        self._delay = delay

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
        if issubclass(RetryOptions, dict):
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
        if not isinstance(other, RetryOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

