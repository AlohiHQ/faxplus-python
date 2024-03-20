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


class AccountSettings(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'caller_id_name': 'str',
        'options': 'object',
        'send_fax': 'AccountSettingsSendFax',
        'should_enhance': 'bool'
    }

    attribute_map = {
        'caller_id_name': 'caller_id_name',
        'options': 'options',
        'send_fax': 'send_fax',
        'should_enhance': 'should_enhance'
    }

    def __init__(self, caller_id_name=None, options=None, send_fax=None, should_enhance=None):  # noqa: E501
        """AccountSettings - a model defined in Swagger

        :param str caller_id_name: Account caller id name
        :param object options:
        :param AccountSettingsSendFax send_fax:
        :param bool should_enhance:
        """  # noqa: E501
        self._caller_id_name = None
        self._options = None
        self._send_fax = None
        self._should_enhance = None
        self.discriminator = None
        if caller_id_name is not None:
            self.caller_id_name = caller_id_name
        if options is not None:
            self.options = options
        if send_fax is not None:
            self.send_fax = send_fax
        if should_enhance is not None:
            self.should_enhance = should_enhance

    @property
    def caller_id_name(self):
        """Gets the caller_id_name of this AccountSettings.  # noqa: E501

        Account caller id name  # noqa: E501

        :return: The caller_id_name of this AccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._caller_id_name

    @caller_id_name.setter
    def caller_id_name(self, caller_id_name):
        """Sets the caller_id_name of this AccountSettings.

        Account caller id name  # noqa: E501

        :param caller_id_name: The caller_id_name of this AccountSettings.  # noqa: E501
        :type: str
        """

        self._caller_id_name = caller_id_name

    @property
    def options(self):
        """Gets the options of this AccountSettings.  # noqa: E501


        :return: The options of this AccountSettings.  # noqa: E501
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this AccountSettings.


        :param options: The options of this AccountSettings.  # noqa: E501
        :type: object
        """

        self._options = options

    @property
    def send_fax(self):
        """Gets the send_fax of this AccountSettings.  # noqa: E501


        :return: The send_fax of this AccountSettings.  # noqa: E501
        :rtype: AccountSettingsSendFax
        """
        return self._send_fax

    @send_fax.setter
    def send_fax(self, send_fax):
        """Sets the send_fax of this AccountSettings.


        :param send_fax: The send_fax of this AccountSettings.  # noqa: E501
        :type: AccountSettingsSendFax
        """

        self._send_fax = send_fax

    @property
    def should_enhance(self):
        """Gets the should_enhance of this AccountSettings.  # noqa: E501


        :return: The should_enhance of this AccountSettings.  # noqa: E501
        :rtype: bool
        """
        return self._should_enhance

    @should_enhance.setter
    def should_enhance(self, should_enhance):
        """Sets the should_enhance of this AccountSettings.


        :param should_enhance: The should_enhance of this AccountSettings.  # noqa: E501
        :type: bool
        """

        self._should_enhance = should_enhance

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
        if issubclass(AccountSettings, dict):
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
        if not isinstance(other, AccountSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

