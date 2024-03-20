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


class OutboxInitiatedFrom(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'from_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'from_id': 'from_id',
        'type': 'type'
    }

    def __init__(self, from_id=None, type=None):  # noqa: E501
        """OutboxInitiatedFrom - a model defined in Swagger

        :param str from_id:
        :param str type:
        """  # noqa: E501
        self._from_id = None
        self._type = None
        self.discriminator = None
        if from_id is not None:
            self.from_id = from_id
        if type is not None:
            self.type = type

    @property
    def from_id(self):
        """Gets the from_id of this OutboxInitiatedFrom.  # noqa: E501


        :return: The from_id of this OutboxInitiatedFrom.  # noqa: E501
        :rtype: str
        """
        return self._from_id

    @from_id.setter
    def from_id(self, from_id):
        """Sets the from_id of this OutboxInitiatedFrom.


        :param from_id: The from_id of this OutboxInitiatedFrom.  # noqa: E501
        :type: str
        """

        self._from_id = from_id

    @property
    def type(self):
        """Gets the type of this OutboxInitiatedFrom.  # noqa: E501


        :return: The type of this OutboxInitiatedFrom.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OutboxInitiatedFrom.


        :param type: The type of this OutboxInitiatedFrom.  # noqa: E501
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
        if issubclass(OutboxInitiatedFrom, dict):
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
        if not isinstance(other, OutboxInitiatedFrom):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

