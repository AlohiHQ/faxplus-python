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


class File(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'fax_file': 'str'
    }

    attribute_map = {
        'fax_file': 'fax_file'
    }

    def __init__(self, fax_file=None):  # noqa: E501
        """File - a model defined in Swagger

        :param str fax_file: Path to file to upload (required)
        """  # noqa: E501
        self._fax_file = None
        self.discriminator = None
        self.fax_file = fax_file

    @property
    def fax_file(self):
        """Gets the fax_file of this File.  # noqa: E501

        Path to file to upload  # noqa: E501

        :return: The fax_file of this File.  # noqa: E501
        :rtype: str
        """
        return self._fax_file

    @fax_file.setter
    def fax_file(self, fax_file):
        """Sets the fax_file of this File.

        Path to file to upload  # noqa: E501

        :param fax_file: The fax_file of this File.  # noqa: E501
        :type: str
        """
        if fax_file is None:
            raise ValueError("Invalid value for `fax_file`, must not be `None`")  # noqa: E501

        self._fax_file = fax_file

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
        if issubclass(File, dict):
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
        if not isinstance(other, File):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

