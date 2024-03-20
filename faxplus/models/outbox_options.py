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


class OutboxOptions(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'enhancement': 'bool',
        'retry': 'RetryOptions'
    }

    attribute_map = {
        'enhancement': 'enhancement',
        'retry': 'retry'
    }

    def __init__(self, enhancement=True, retry=None):  # noqa: E501
        """OutboxOptions - a model defined in Swagger

        :param bool enhancement: Text enhancement. Set to True to optimize fax file for text.
        :param RetryOptions retry:
        """  # noqa: E501
        self._enhancement = None
        self._retry = None
        self.discriminator = None
        if enhancement is not None:
            self.enhancement = enhancement
        if retry is not None:
            self.retry = retry

    @property
    def enhancement(self):
        """Gets the enhancement of this OutboxOptions.  # noqa: E501

        Text enhancement. Set to True to optimize fax file for text.  # noqa: E501

        :return: The enhancement of this OutboxOptions.  # noqa: E501
        :rtype: bool
        """
        return self._enhancement

    @enhancement.setter
    def enhancement(self, enhancement):
        """Sets the enhancement of this OutboxOptions.

        Text enhancement. Set to True to optimize fax file for text.  # noqa: E501

        :param enhancement: The enhancement of this OutboxOptions.  # noqa: E501
        :type: bool
        """

        self._enhancement = enhancement

    @property
    def retry(self):
        """Gets the retry of this OutboxOptions.  # noqa: E501


        :return: The retry of this OutboxOptions.  # noqa: E501
        :rtype: RetryOptions
        """
        return self._retry

    @retry.setter
    def retry(self, retry):
        """Sets the retry of this OutboxOptions.


        :param retry: The retry of this OutboxOptions.  # noqa: E501
        :type: RetryOptions
        """

        self._retry = retry

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
        if issubclass(OutboxOptions, dict):
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
        if not isinstance(other, OutboxOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

