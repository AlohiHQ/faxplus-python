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


class FaxCostDetails(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'multiplier': 'float',
        'notification_cost': 'float'
    }

    attribute_map = {
        'multiplier': 'multiplier',
        'notification_cost': 'notification_cost'
    }

    def __init__(self, multiplier=None, notification_cost=None):  # noqa: E501
        """FaxCostDetails - a model defined in Swagger

        :param float multiplier:
        :param float notification_cost:
        """  # noqa: E501
        self._multiplier = None
        self._notification_cost = None
        self.discriminator = None
        if multiplier is not None:
            self.multiplier = multiplier
        if notification_cost is not None:
            self.notification_cost = notification_cost

    @property
    def multiplier(self):
        """Gets the multiplier of this FaxCostDetails.  # noqa: E501


        :return: The multiplier of this FaxCostDetails.  # noqa: E501
        :rtype: float
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, multiplier):
        """Sets the multiplier of this FaxCostDetails.


        :param multiplier: The multiplier of this FaxCostDetails.  # noqa: E501
        :type: float
        """

        self._multiplier = multiplier

    @property
    def notification_cost(self):
        """Gets the notification_cost of this FaxCostDetails.  # noqa: E501


        :return: The notification_cost of this FaxCostDetails.  # noqa: E501
        :rtype: float
        """
        return self._notification_cost

    @notification_cost.setter
    def notification_cost(self, notification_cost):
        """Sets the notification_cost of this FaxCostDetails.


        :param notification_cost: The notification_cost of this FaxCostDetails.  # noqa: E501
        :type: float
        """

        self._notification_cost = notification_cost

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
        if issubclass(FaxCostDetails, dict):
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
        if not isinstance(other, FaxCostDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

