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


class AccountNotificationsEmailSettingsAttachments(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'confirmation_page': 'bool',
        'receive_fax': 'bool',
        'send_fax': 'bool'
    }

    attribute_map = {
        'confirmation_page': 'confirmation_page',
        'receive_fax': 'receive_fax',
        'send_fax': 'send_fax'
    }

    def __init__(self, confirmation_page=None, receive_fax=None, send_fax=None):  # noqa: E501
        """AccountNotificationsEmailSettingsAttachments - a model defined in Swagger

        :param bool confirmation_page:
        :param bool receive_fax: Set to true if you want to receive new faxes as notification attachments (required)
        :param bool send_fax: Set to true if you want to receive your sent fax as an attachment to the notification (required)
        """  # noqa: E501
        self._confirmation_page = None
        self._receive_fax = None
        self._send_fax = None
        self.discriminator = None
        if confirmation_page is not None:
            self.confirmation_page = confirmation_page
        self.receive_fax = receive_fax
        self.send_fax = send_fax

    @property
    def confirmation_page(self):
        """Gets the confirmation_page of this AccountNotificationsEmailSettingsAttachments.  # noqa: E501


        :return: The confirmation_page of this AccountNotificationsEmailSettingsAttachments.  # noqa: E501
        :rtype: bool
        """
        return self._confirmation_page

    @confirmation_page.setter
    def confirmation_page(self, confirmation_page):
        """Sets the confirmation_page of this AccountNotificationsEmailSettingsAttachments.


        :param confirmation_page: The confirmation_page of this AccountNotificationsEmailSettingsAttachments.  # noqa: E501
        :type: bool
        """

        self._confirmation_page = confirmation_page

    @property
    def receive_fax(self):
        """Gets the receive_fax of this AccountNotificationsEmailSettingsAttachments.  # noqa: E501

        Set to true if you want to receive new faxes as notification attachments  # noqa: E501

        :return: The receive_fax of this AccountNotificationsEmailSettingsAttachments.  # noqa: E501
        :rtype: bool
        """
        return self._receive_fax

    @receive_fax.setter
    def receive_fax(self, receive_fax):
        """Sets the receive_fax of this AccountNotificationsEmailSettingsAttachments.

        Set to true if you want to receive new faxes as notification attachments  # noqa: E501

        :param receive_fax: The receive_fax of this AccountNotificationsEmailSettingsAttachments.  # noqa: E501
        :type: bool
        """
        if receive_fax is None:
            raise ValueError("Invalid value for `receive_fax`, must not be `None`")  # noqa: E501

        self._receive_fax = receive_fax

    @property
    def send_fax(self):
        """Gets the send_fax of this AccountNotificationsEmailSettingsAttachments.  # noqa: E501

        Set to true if you want to receive your sent fax as an attachment to the notification  # noqa: E501

        :return: The send_fax of this AccountNotificationsEmailSettingsAttachments.  # noqa: E501
        :rtype: bool
        """
        return self._send_fax

    @send_fax.setter
    def send_fax(self, send_fax):
        """Sets the send_fax of this AccountNotificationsEmailSettingsAttachments.

        Set to true if you want to receive your sent fax as an attachment to the notification  # noqa: E501

        :param send_fax: The send_fax of this AccountNotificationsEmailSettingsAttachments.  # noqa: E501
        :type: bool
        """
        if send_fax is None:
            raise ValueError("Invalid value for `send_fax`, must not be `None`")  # noqa: E501

        self._send_fax = send_fax

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
        if issubclass(AccountNotificationsEmailSettingsAttachments, dict):
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
        if not isinstance(other, AccountNotificationsEmailSettingsAttachments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

