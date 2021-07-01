# coding: utf-8

"""
    FAX.PLUS REST API

    Visit https://apidoc.fax.plus for more information.

    © Alohi SA (Geneva, Switzerland)

    https://www.alohi.com
    Contact: info@fax.plus
"""

import pprint
import re  # noqa: F401

import six
from faxplus.models import *


class WebhookCallbackData(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'pages': 'float'
    }

    attribute_map = {
        'id': 'id',
        'pages': 'pages'
    }

    def __init__(self, id=None, pages=None):  # noqa: E501
        """WebhookCallbackData - a model defined in Swagger

        :param str id: Fax ID
        :param float pages:
        """  # noqa: E501
        self._id = None
        self._pages = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if pages is not None:
            self.pages = pages

    @property
    def id(self):
        """Gets the id of this WebhookCallbackData.  # noqa: E501

        Fax ID  # noqa: E501

        :return: The id of this WebhookCallbackData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookCallbackData.

        Fax ID  # noqa: E501

        :param id: The id of this WebhookCallbackData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def pages(self):
        """Gets the pages of this WebhookCallbackData.  # noqa: E501


        :return: The pages of this WebhookCallbackData.  # noqa: E501
        :rtype: float
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this WebhookCallbackData.


        :param pages: The pages of this WebhookCallbackData.  # noqa: E501
        :type: float
        """

        self._pages = pages

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
        if issubclass(WebhookCallbackData, dict):
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
        if not isinstance(other, WebhookCallbackData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

