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


class OutboxCoverPage(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name_to': 'str',
        'name_from': 'str',
        'subject': 'str',
        'flags': 'list[CoverPageFlags]',
        'message': 'str'
    }

    attribute_map = {
        'name_to': 'name_to',
        'name_from': 'name_from',
        'subject': 'subject',
        'flags': 'flags',
        'message': 'message'
    }

    def __init__(self, name_to=None, name_from=None, subject=None, flags=None, message=None):  # noqa: E501
        """OutboxCoverPage - a model defined in Swagger

        :param str name_to: TO field on the cover page (required)
        :param str name_from: FROM field on the cover page (required)
        :param str subject: SUBJECT field on the cover page (required)
        :param list[CoverPageFlags] flags: Cover page flags
        :param str message: MESSAGE field on the cover page
        """  # noqa: E501
        self._name_to = None
        self._name_from = None
        self._subject = None
        self._flags = None
        self._message = None
        self.discriminator = None
        self.name_to = name_to
        self.name_from = name_from
        self.subject = subject
        if flags is not None:
            self.flags = flags
        if message is not None:
            self.message = message

    @property
    def name_to(self):
        """Gets the name_to of this OutboxCoverPage.  # noqa: E501

        TO field on the cover page  # noqa: E501

        :return: The name_to of this OutboxCoverPage.  # noqa: E501
        :rtype: str
        """
        return self._name_to

    @name_to.setter
    def name_to(self, name_to):
        """Sets the name_to of this OutboxCoverPage.

        TO field on the cover page  # noqa: E501

        :param name_to: The name_to of this OutboxCoverPage.  # noqa: E501
        :type: str
        """
        if name_to is None:
            raise ValueError("Invalid value for `name_to`, must not be `None`")  # noqa: E501

        self._name_to = name_to

    @property
    def name_from(self):
        """Gets the name_from of this OutboxCoverPage.  # noqa: E501

        FROM field on the cover page  # noqa: E501

        :return: The name_from of this OutboxCoverPage.  # noqa: E501
        :rtype: str
        """
        return self._name_from

    @name_from.setter
    def name_from(self, name_from):
        """Sets the name_from of this OutboxCoverPage.

        FROM field on the cover page  # noqa: E501

        :param name_from: The name_from of this OutboxCoverPage.  # noqa: E501
        :type: str
        """
        if name_from is None:
            raise ValueError("Invalid value for `name_from`, must not be `None`")  # noqa: E501

        self._name_from = name_from

    @property
    def subject(self):
        """Gets the subject of this OutboxCoverPage.  # noqa: E501

        SUBJECT field on the cover page  # noqa: E501

        :return: The subject of this OutboxCoverPage.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this OutboxCoverPage.

        SUBJECT field on the cover page  # noqa: E501

        :param subject: The subject of this OutboxCoverPage.  # noqa: E501
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def flags(self):
        """Gets the flags of this OutboxCoverPage.  # noqa: E501

        Cover page flags  # noqa: E501

        :return: The flags of this OutboxCoverPage.  # noqa: E501
        :rtype: list[CoverPageFlags]
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """Sets the flags of this OutboxCoverPage.

        Cover page flags  # noqa: E501

        :param flags: The flags of this OutboxCoverPage.  # noqa: E501
        :type: list[CoverPageFlags]
        """

        self._flags = flags

    @property
    def message(self):
        """Gets the message of this OutboxCoverPage.  # noqa: E501

        MESSAGE field on the cover page  # noqa: E501

        :return: The message of this OutboxCoverPage.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this OutboxCoverPage.

        MESSAGE field on the cover page  # noqa: E501

        :param message: The message of this OutboxCoverPage.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if issubclass(OutboxCoverPage, dict):
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
        if not isinstance(other, OutboxCoverPage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

