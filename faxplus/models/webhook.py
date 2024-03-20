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


class Webhook(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'target': 'str',
        'event': 'WebhookEventType'
    }

    attribute_map = {
        'id': 'id',
        'target': 'target',
        'event': 'event'
    }

    def __init__(self, id=None, target=None, event=None):  # noqa: E501
        """Webhook - a model defined in Swagger

        :param str id: Webhook ID
        :param str target: Webhook target URL (required)
        :param WebhookEventType event: (required)
        """  # noqa: E501
        self._id = None
        self._target = None
        self._event = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.target = target
        self.event = event

    @property
    def id(self):
        """Gets the id of this Webhook.  # noqa: E501

        Webhook ID  # noqa: E501

        :return: The id of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Webhook.

        Webhook ID  # noqa: E501

        :param id: The id of this Webhook.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def target(self):
        """Gets the target of this Webhook.  # noqa: E501

        Webhook target URL  # noqa: E501

        :return: The target of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this Webhook.

        Webhook target URL  # noqa: E501

        :param target: The target of this Webhook.  # noqa: E501
        :type: str
        """
        if target is None:
            raise ValueError("Invalid value for `target`, must not be `None`")  # noqa: E501

        self._target = target

    @property
    def event(self):
        """Gets the event of this Webhook.  # noqa: E501


        :return: The event of this Webhook.  # noqa: E501
        :rtype: WebhookEventType
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this Webhook.


        :param event: The event of this Webhook.  # noqa: E501
        :type: WebhookEventType
        """
        if event is None:
            raise ValueError("Invalid value for `event`, must not be `None`")  # noqa: E501

        self._event = event

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
        if issubclass(Webhook, dict):
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
        if not isinstance(other, Webhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

