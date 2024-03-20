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


class MemberDetail(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'quota': 'int',
        'role': 'str'
    }

    attribute_map = {
        'quota': 'quota',
        'role': 'role'
    }

    def __init__(self, quota=None, role=None):  # noqa: E501
        """MemberDetail - a model defined in Swagger

        :param int quota: Quota of member (number of pages member can send per month)
        :param str role: Role of member in your company
        """  # noqa: E501
        self._quota = None
        self._role = None
        self.discriminator = None
        if quota is not None:
            self.quota = quota
        if role is not None:
            self.role = role

    @property
    def quota(self):
        """Gets the quota of this MemberDetail.  # noqa: E501

        Quota of member (number of pages member can send per month)  # noqa: E501

        :return: The quota of this MemberDetail.  # noqa: E501
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this MemberDetail.

        Quota of member (number of pages member can send per month)  # noqa: E501

        :param quota: The quota of this MemberDetail.  # noqa: E501
        :type: int
        """
        if quota is not None and quota < 0:  # noqa: E501
            raise ValueError("Invalid value for `quota`, must be a value greater than or equal to `0`")  # noqa: E501

        self._quota = quota

    @property
    def role(self):
        """Gets the role of this MemberDetail.  # noqa: E501

        Role of member in your company  # noqa: E501

        :return: The role of this MemberDetail.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this MemberDetail.

        Role of member in your company  # noqa: E501

        :param role: The role of this MemberDetail.  # noqa: E501
        :type: str
        """

        self._role = role

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
        if issubclass(MemberDetail, dict):
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
        if not isinstance(other, MemberDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

