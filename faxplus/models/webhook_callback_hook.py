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


class WebhookCallbackHook(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'event': 'str',
        'event_time': 'str',
        'target': 'str'
    }

    attribute_map = {
        'id': 'id',
        'event': 'event',
        'event_time': 'event_time',
        'target': 'target'
    }

    def __init__(self, id=None, event=None, event_time=None, target=None):  # noqa: E501
        """WebhookCallbackHook - a model defined in Swagger

        :param str id: Fax ID
        :param str event: Event type
        :param str event_time: Time of the event. Format: YYYY-MM-DD HH:mm:ss
        :param str target: Configured URL target for this webhook
        """  # noqa: E501
        self._id = None
        self._event = None
        self._event_time = None
        self._target = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if event is not None:
            self.event = event
        if event_time is not None:
            self.event_time = event_time
        if target is not None:
            self.target = target

    @property
    def id(self):
        """Gets the id of this WebhookCallbackHook.  # noqa: E501

        Fax ID  # noqa: E501

        :return: The id of this WebhookCallbackHook.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookCallbackHook.

        Fax ID  # noqa: E501

        :param id: The id of this WebhookCallbackHook.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def event(self):
        """Gets the event of this WebhookCallbackHook.  # noqa: E501

        Event type  # noqa: E501

        :return: The event of this WebhookCallbackHook.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this WebhookCallbackHook.

        Event type  # noqa: E501

        :param event: The event of this WebhookCallbackHook.  # noqa: E501
        :type: str
        """
        allowed_values = ["fax_sent", "fax_received"]  # noqa: E501
        if event not in allowed_values:
            raise ValueError(
                "Invalid value for `event` ({0}), must be one of {1}"  # noqa: E501
                .format(event, allowed_values)
            )

        self._event = event

    @property
    def event_time(self):
        """Gets the event_time of this WebhookCallbackHook.  # noqa: E501

        Time of the event. Format: YYYY-MM-DD HH:mm:ss  # noqa: E501

        :return: The event_time of this WebhookCallbackHook.  # noqa: E501
        :rtype: str
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """Sets the event_time of this WebhookCallbackHook.

        Time of the event. Format: YYYY-MM-DD HH:mm:ss  # noqa: E501

        :param event_time: The event_time of this WebhookCallbackHook.  # noqa: E501
        :type: str
        """

        self._event_time = event_time

    @property
    def target(self):
        """Gets the target of this WebhookCallbackHook.  # noqa: E501

        Configured URL target for this webhook  # noqa: E501

        :return: The target of this WebhookCallbackHook.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this WebhookCallbackHook.

        Configured URL target for this webhook  # noqa: E501

        :param target: The target of this WebhookCallbackHook.  # noqa: E501
        :type: str
        """

        self._target = target

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
        if issubclass(WebhookCallbackHook, dict):
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
        if not isinstance(other, WebhookCallbackHook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

