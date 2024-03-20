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


class OutboxComment(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'tags': 'list[str]',
        'text': 'str'
    }

    attribute_map = {
        'tags': 'tags',
        'text': 'text'
    }

    def __init__(self, tags=None, text=''):  # noqa: E501
        """OutboxComment - a model defined in Swagger

        :param list[str] tags:
        :param str text:
        """  # noqa: E501
        self._tags = None
        self._text = None
        self.discriminator = None
        if tags is not None:
            self.tags = tags
        if text is not None:
            self.text = text

    @property
    def tags(self):
        """Gets the tags of this OutboxComment.  # noqa: E501


        :return: The tags of this OutboxComment.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this OutboxComment.


        :param tags: The tags of this OutboxComment.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def text(self):
        """Gets the text of this OutboxComment.  # noqa: E501


        :return: The text of this OutboxComment.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this OutboxComment.


        :param text: The text of this OutboxComment.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if issubclass(OutboxComment, dict):
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
        if not isinstance(other, OutboxComment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

