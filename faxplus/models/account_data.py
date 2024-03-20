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


class AccountData(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'company_logo': 'str',
        'company_name': 'str',
        'deactivation_reason': 'str',
        'default_file_type': 'FileType',
        'role': 'str',
        'save_history': 'bool'
    }

    attribute_map = {
        'company_logo': 'company_logo',
        'company_name': 'company_name',
        'deactivation_reason': 'deactivation_reason',
        'default_file_type': 'default_file_type',
        'role': 'role',
        'save_history': 'save_history'
    }

    def __init__(self, company_logo=None, company_name=None, deactivation_reason=None, default_file_type=None, role=None, save_history=None):  # noqa: E501
        """AccountData - a model defined in Swagger

        :param str company_logo: File name of your company logo
        :param str company_name: Your company name in case you are a corporate admin
        :param str deactivation_reason:
        :param FileType default_file_type:
        :param str role: Role of the account in the company
        :param bool save_history: Save fax CDRs in inbox status
        """  # noqa: E501
        self._company_logo = None
        self._company_name = None
        self._deactivation_reason = None
        self._default_file_type = None
        self._role = None
        self._save_history = None
        self.discriminator = None
        if company_logo is not None:
            self.company_logo = company_logo
        if company_name is not None:
            self.company_name = company_name
        if deactivation_reason is not None:
            self.deactivation_reason = deactivation_reason
        if default_file_type is not None:
            self.default_file_type = default_file_type
        if role is not None:
            self.role = role
        if save_history is not None:
            self.save_history = save_history

    @property
    def company_logo(self):
        """Gets the company_logo of this AccountData.  # noqa: E501

        File name of your company logo  # noqa: E501

        :return: The company_logo of this AccountData.  # noqa: E501
        :rtype: str
        """
        return self._company_logo

    @company_logo.setter
    def company_logo(self, company_logo):
        """Sets the company_logo of this AccountData.

        File name of your company logo  # noqa: E501

        :param company_logo: The company_logo of this AccountData.  # noqa: E501
        :type: str
        """

        self._company_logo = company_logo

    @property
    def company_name(self):
        """Gets the company_name of this AccountData.  # noqa: E501

        Your company name in case you are a corporate admin  # noqa: E501

        :return: The company_name of this AccountData.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this AccountData.

        Your company name in case you are a corporate admin  # noqa: E501

        :param company_name: The company_name of this AccountData.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def deactivation_reason(self):
        """Gets the deactivation_reason of this AccountData.  # noqa: E501


        :return: The deactivation_reason of this AccountData.  # noqa: E501
        :rtype: str
        """
        return self._deactivation_reason

    @deactivation_reason.setter
    def deactivation_reason(self, deactivation_reason):
        """Sets the deactivation_reason of this AccountData.


        :param deactivation_reason: The deactivation_reason of this AccountData.  # noqa: E501
        :type: str
        """

        self._deactivation_reason = deactivation_reason

    @property
    def default_file_type(self):
        """Gets the default_file_type of this AccountData.  # noqa: E501


        :return: The default_file_type of this AccountData.  # noqa: E501
        :rtype: FileType
        """
        return self._default_file_type

    @default_file_type.setter
    def default_file_type(self, default_file_type):
        """Sets the default_file_type of this AccountData.


        :param default_file_type: The default_file_type of this AccountData.  # noqa: E501
        :type: FileType
        """

        self._default_file_type = default_file_type

    @property
    def role(self):
        """Gets the role of this AccountData.  # noqa: E501

        Role of the account in the company  # noqa: E501

        :return: The role of this AccountData.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this AccountData.

        Role of the account in the company  # noqa: E501

        :param role: The role of this AccountData.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def save_history(self):
        """Gets the save_history of this AccountData.  # noqa: E501

        Save fax CDRs in inbox status  # noqa: E501

        :return: The save_history of this AccountData.  # noqa: E501
        :rtype: bool
        """
        return self._save_history

    @save_history.setter
    def save_history(self, save_history):
        """Sets the save_history of this AccountData.

        Save fax CDRs in inbox status  # noqa: E501

        :param save_history: The save_history of this AccountData.  # noqa: E501
        :type: bool
        """

        self._save_history = save_history

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
        if issubclass(AccountData, dict):
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
        if not isinstance(other, AccountData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

