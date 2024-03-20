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


class PayloadAccountModification(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_data': 'AccountData',
        'email': 'str',
        'lastname': 'str',
        'name': 'str',
        'notifications': 'AccountNotifications',
        'phone': 'str',
        'profile_image': 'str',
        'settings': 'AccountSettings'
    }

    attribute_map = {
        'account_data': 'account_data',
        'email': 'email',
        'lastname': 'lastname',
        'name': 'name',
        'notifications': 'notifications',
        'phone': 'phone',
        'profile_image': 'profile_image',
        'settings': 'settings'
    }

    def __init__(self, account_data=None, email=None, lastname=None, name=None, notifications=None, phone=None, profile_image=None, settings=None):  # noqa: E501
        """PayloadAccountModification - a model defined in Swagger

        :param AccountData account_data:
        :param str email: Account email address
        :param str lastname: Your last name
        :param str name: Your first name
        :param AccountNotifications notifications:
        :param str phone: Your account phone number
        :param str profile_image: Profile image path
        :param AccountSettings settings:
        """  # noqa: E501
        self._account_data = None
        self._email = None
        self._lastname = None
        self._name = None
        self._notifications = None
        self._phone = None
        self._profile_image = None
        self._settings = None
        self.discriminator = None
        if account_data is not None:
            self.account_data = account_data
        if email is not None:
            self.email = email
        if lastname is not None:
            self.lastname = lastname
        if name is not None:
            self.name = name
        if notifications is not None:
            self.notifications = notifications
        if phone is not None:
            self.phone = phone
        if profile_image is not None:
            self.profile_image = profile_image
        if settings is not None:
            self.settings = settings

    @property
    def account_data(self):
        """Gets the account_data of this PayloadAccountModification.  # noqa: E501


        :return: The account_data of this PayloadAccountModification.  # noqa: E501
        :rtype: AccountData
        """
        return self._account_data

    @account_data.setter
    def account_data(self, account_data):
        """Sets the account_data of this PayloadAccountModification.


        :param account_data: The account_data of this PayloadAccountModification.  # noqa: E501
        :type: AccountData
        """

        self._account_data = account_data

    @property
    def email(self):
        """Gets the email of this PayloadAccountModification.  # noqa: E501

        Account email address  # noqa: E501

        :return: The email of this PayloadAccountModification.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PayloadAccountModification.

        Account email address  # noqa: E501

        :param email: The email of this PayloadAccountModification.  # noqa: E501
        :type: str
        """
        if email and not re.search(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$', email):  # noqa: E501
            raise ValueError(r"Invalid value for `email`, must be a follow pattern or equal to `/^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$/`")  # noqa: E501

        self._email = email

    @property
    def lastname(self):
        """Gets the lastname of this PayloadAccountModification.  # noqa: E501

        Your last name  # noqa: E501

        :return: The lastname of this PayloadAccountModification.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this PayloadAccountModification.

        Your last name  # noqa: E501

        :param lastname: The lastname of this PayloadAccountModification.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def name(self):
        """Gets the name of this PayloadAccountModification.  # noqa: E501

        Your first name  # noqa: E501

        :return: The name of this PayloadAccountModification.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PayloadAccountModification.

        Your first name  # noqa: E501

        :param name: The name of this PayloadAccountModification.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notifications(self):
        """Gets the notifications of this PayloadAccountModification.  # noqa: E501


        :return: The notifications of this PayloadAccountModification.  # noqa: E501
        :rtype: AccountNotifications
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this PayloadAccountModification.


        :param notifications: The notifications of this PayloadAccountModification.  # noqa: E501
        :type: AccountNotifications
        """

        self._notifications = notifications

    @property
    def phone(self):
        """Gets the phone of this PayloadAccountModification.  # noqa: E501

        Your account phone number  # noqa: E501

        :return: The phone of this PayloadAccountModification.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this PayloadAccountModification.

        Your account phone number  # noqa: E501

        :param phone: The phone of this PayloadAccountModification.  # noqa: E501
        :type: str
        """
        if phone and not re.search(r'^[+]?[0-9]{8,}$', phone):  # noqa: E501
            raise ValueError(r"Invalid value for `phone`, must be a follow pattern or equal to `/^[+]?[0-9]{8,}$/`")  # noqa: E501

        self._phone = phone

    @property
    def profile_image(self):
        """Gets the profile_image of this PayloadAccountModification.  # noqa: E501

        Profile image path  # noqa: E501

        :return: The profile_image of this PayloadAccountModification.  # noqa: E501
        :rtype: str
        """
        return self._profile_image

    @profile_image.setter
    def profile_image(self, profile_image):
        """Sets the profile_image of this PayloadAccountModification.

        Profile image path  # noqa: E501

        :param profile_image: The profile_image of this PayloadAccountModification.  # noqa: E501
        :type: str
        """

        self._profile_image = profile_image

    @property
    def settings(self):
        """Gets the settings of this PayloadAccountModification.  # noqa: E501


        :return: The settings of this PayloadAccountModification.  # noqa: E501
        :rtype: AccountSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this PayloadAccountModification.


        :param settings: The settings of this PayloadAccountModification.  # noqa: E501
        :type: AccountSettings
        """

        self._settings = settings

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
        if issubclass(PayloadAccountModification, dict):
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
        if not isinstance(other, PayloadAccountModification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

