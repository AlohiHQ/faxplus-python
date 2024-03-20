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


class Account(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_data': 'AccountData',
        'account_type': 'AccountType',
        'creation_date': 'str',
        'email': 'str',
        'last_password_modification_date': 'str',
        'lastname': 'str',
        'member_of': 'list[str]',
        'name': 'str',
        'notifications': 'AccountNotifications',
        'phone': 'str',
        'profile_image': 'str',
        'settings': 'AccountSettings',
        'status': 'AccountStatus',
        'uid': 'str'
    }

    attribute_map = {
        'account_data': 'account_data',
        'account_type': 'account_type',
        'creation_date': 'creation_date',
        'email': 'email',
        'last_password_modification_date': 'last_password_modification_date',
        'lastname': 'lastname',
        'member_of': 'member_of',
        'name': 'name',
        'notifications': 'notifications',
        'phone': 'phone',
        'profile_image': 'profile_image',
        'settings': 'settings',
        'status': 'status',
        'uid': 'uid'
    }

    def __init__(self, account_data=None, account_type=None, creation_date=None, email=None, last_password_modification_date=None, lastname=None, member_of=None, name=None, notifications=None, phone=None, profile_image=None, settings=None, status=None, uid=None):  # noqa: E501
        """Account - a model defined in Swagger

        :param AccountData account_data:
        :param AccountType account_type: (required)
        :param str creation_date: Creation date in UTC. Format: *YYYY-MM-DD HH:mm:ss* (required)
        :param str email: Account email address (required)
        :param str last_password_modification_date: The date on which you have changed your password
        :param str lastname: Your last name
        :param list[str] member_of: List of user ids that you are member of.
        :param str name: Your first name
        :param AccountNotifications notifications:
        :param str phone: Your account phone number
        :param str profile_image: Profile image path
        :param AccountSettings settings:
        :param AccountStatus status: (required)
        :param str uid: User ID of current user (required)
        """  # noqa: E501
        self._account_data = None
        self._account_type = None
        self._creation_date = None
        self._email = None
        self._last_password_modification_date = None
        self._lastname = None
        self._member_of = None
        self._name = None
        self._notifications = None
        self._phone = None
        self._profile_image = None
        self._settings = None
        self._status = None
        self._uid = None
        self.discriminator = None
        if account_data is not None:
            self.account_data = account_data
        self.account_type = account_type
        self.creation_date = creation_date
        self.email = email
        if last_password_modification_date is not None:
            self.last_password_modification_date = last_password_modification_date
        if lastname is not None:
            self.lastname = lastname
        if member_of is not None:
            self.member_of = member_of
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
        self.status = status
        self.uid = uid

    @property
    def account_data(self):
        """Gets the account_data of this Account.  # noqa: E501


        :return: The account_data of this Account.  # noqa: E501
        :rtype: AccountData
        """
        return self._account_data

    @account_data.setter
    def account_data(self, account_data):
        """Sets the account_data of this Account.


        :param account_data: The account_data of this Account.  # noqa: E501
        :type: AccountData
        """

        self._account_data = account_data

    @property
    def account_type(self):
        """Gets the account_type of this Account.  # noqa: E501


        :return: The account_type of this Account.  # noqa: E501
        :rtype: AccountType
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this Account.


        :param account_type: The account_type of this Account.  # noqa: E501
        :type: AccountType
        """
        if account_type is None:
            raise ValueError("Invalid value for `account_type`, must not be `None`")  # noqa: E501

        self._account_type = account_type

    @property
    def creation_date(self):
        """Gets the creation_date of this Account.  # noqa: E501

        Creation date in UTC. Format: *YYYY-MM-DD HH:mm:ss*  # noqa: E501

        :return: The creation_date of this Account.  # noqa: E501
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Account.

        Creation date in UTC. Format: *YYYY-MM-DD HH:mm:ss*  # noqa: E501

        :param creation_date: The creation_date of this Account.  # noqa: E501
        :type: str
        """
        if creation_date is None:
            raise ValueError("Invalid value for `creation_date`, must not be `None`")  # noqa: E501
        if creation_date and not re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}', creation_date):  # noqa: E501
            raise ValueError(r"Invalid value for `creation_date`, must be a follow pattern or equal to `/^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}/`")  # noqa: E501

        self._creation_date = creation_date

    @property
    def email(self):
        """Gets the email of this Account.  # noqa: E501

        Account email address  # noqa: E501

        :return: The email of this Account.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Account.

        Account email address  # noqa: E501

        :param email: The email of this Account.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if email and not re.search(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$', email):  # noqa: E501
            raise ValueError(r"Invalid value for `email`, must be a follow pattern or equal to `/^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$/`")  # noqa: E501

        self._email = email

    @property
    def last_password_modification_date(self):
        """Gets the last_password_modification_date of this Account.  # noqa: E501

        The date on which you have changed your password  # noqa: E501

        :return: The last_password_modification_date of this Account.  # noqa: E501
        :rtype: str
        """
        return self._last_password_modification_date

    @last_password_modification_date.setter
    def last_password_modification_date(self, last_password_modification_date):
        """Sets the last_password_modification_date of this Account.

        The date on which you have changed your password  # noqa: E501

        :param last_password_modification_date: The last_password_modification_date of this Account.  # noqa: E501
        :type: str
        """

        self._last_password_modification_date = last_password_modification_date

    @property
    def lastname(self):
        """Gets the lastname of this Account.  # noqa: E501

        Your last name  # noqa: E501

        :return: The lastname of this Account.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this Account.

        Your last name  # noqa: E501

        :param lastname: The lastname of this Account.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def member_of(self):
        """Gets the member_of of this Account.  # noqa: E501

        List of user ids that you are member of.  # noqa: E501

        :return: The member_of of this Account.  # noqa: E501
        :rtype: list[str]
        """
        return self._member_of

    @member_of.setter
    def member_of(self, member_of):
        """Sets the member_of of this Account.

        List of user ids that you are member of.  # noqa: E501

        :param member_of: The member_of of this Account.  # noqa: E501
        :type: list[str]
        """

        self._member_of = member_of

    @property
    def name(self):
        """Gets the name of this Account.  # noqa: E501

        Your first name  # noqa: E501

        :return: The name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Account.

        Your first name  # noqa: E501

        :param name: The name of this Account.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notifications(self):
        """Gets the notifications of this Account.  # noqa: E501


        :return: The notifications of this Account.  # noqa: E501
        :rtype: AccountNotifications
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this Account.


        :param notifications: The notifications of this Account.  # noqa: E501
        :type: AccountNotifications
        """

        self._notifications = notifications

    @property
    def phone(self):
        """Gets the phone of this Account.  # noqa: E501

        Your account phone number  # noqa: E501

        :return: The phone of this Account.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Account.

        Your account phone number  # noqa: E501

        :param phone: The phone of this Account.  # noqa: E501
        :type: str
        """
        if phone and not re.search(r'^[+]?[0-9]{8,}$', phone):  # noqa: E501
            raise ValueError(r"Invalid value for `phone`, must be a follow pattern or equal to `/^[+]?[0-9]{8,}$/`")  # noqa: E501

        self._phone = phone

    @property
    def profile_image(self):
        """Gets the profile_image of this Account.  # noqa: E501

        Profile image path  # noqa: E501

        :return: The profile_image of this Account.  # noqa: E501
        :rtype: str
        """
        return self._profile_image

    @profile_image.setter
    def profile_image(self, profile_image):
        """Sets the profile_image of this Account.

        Profile image path  # noqa: E501

        :param profile_image: The profile_image of this Account.  # noqa: E501
        :type: str
        """

        self._profile_image = profile_image

    @property
    def settings(self):
        """Gets the settings of this Account.  # noqa: E501


        :return: The settings of this Account.  # noqa: E501
        :rtype: AccountSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this Account.


        :param settings: The settings of this Account.  # noqa: E501
        :type: AccountSettings
        """

        self._settings = settings

    @property
    def status(self):
        """Gets the status of this Account.  # noqa: E501


        :return: The status of this Account.  # noqa: E501
        :rtype: AccountStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Account.


        :param status: The status of this Account.  # noqa: E501
        :type: AccountStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def uid(self):
        """Gets the uid of this Account.  # noqa: E501

        User ID of current user  # noqa: E501

        :return: The uid of this Account.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this Account.

        User ID of current user  # noqa: E501

        :param uid: The uid of this Account.  # noqa: E501
        :type: str
        """
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

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
        if issubclass(Account, dict):
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
        if not isinstance(other, Account):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

