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


class Number(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'acquired_date': 'str',
        'assigned_to': 'list[str]',
        'expiration_date': 'str',
        'id': 'str',
        'is_canceled': 'bool',
        'notifications': 'list[NumberNotifications]',
        'number': 'str',
        'owner_id': 'str',
        'status': 'NumberStatus'
    }

    attribute_map = {
        'acquired_date': 'acquired_date',
        'assigned_to': 'assigned_to',
        'expiration_date': 'expiration_date',
        'id': 'id',
        'is_canceled': 'is_canceled',
        'notifications': 'notifications',
        'number': 'number',
        'owner_id': 'owner_id',
        'status': 'status'
    }

    def __init__(self, acquired_date=None, assigned_to=None, expiration_date=None, id=None, is_canceled=None, notifications=None, number=None, owner_id=None, status=None):  # noqa: E501
        """Number - a model defined in Swagger

        :param str acquired_date: Date and time at which the number was acquired (required)
        :param list[str] assigned_to: IDs of the user to whom this number is assigned (required)
        :param str expiration_date: Number expiration date, might be blank
        :param str id: Number ID (required)
        :param bool is_canceled: True if number is canceled but not yet deleted
        :param list[NumberNotifications] notifications:
        :param str number: Fax number (required)
        :param str owner_id: Number owner ID (required)
        :param NumberStatus status: (required)
        """  # noqa: E501
        self._acquired_date = None
        self._assigned_to = None
        self._expiration_date = None
        self._id = None
        self._is_canceled = None
        self._notifications = None
        self._number = None
        self._owner_id = None
        self._status = None
        self.discriminator = None
        self.acquired_date = acquired_date
        self.assigned_to = assigned_to
        if expiration_date is not None:
            self.expiration_date = expiration_date
        self.id = id
        if is_canceled is not None:
            self.is_canceled = is_canceled
        if notifications is not None:
            self.notifications = notifications
        self.number = number
        self.owner_id = owner_id
        self.status = status

    @property
    def acquired_date(self):
        """Gets the acquired_date of this Number.  # noqa: E501

        Date and time at which the number was acquired  # noqa: E501

        :return: The acquired_date of this Number.  # noqa: E501
        :rtype: str
        """
        return self._acquired_date

    @acquired_date.setter
    def acquired_date(self, acquired_date):
        """Sets the acquired_date of this Number.

        Date and time at which the number was acquired  # noqa: E501

        :param acquired_date: The acquired_date of this Number.  # noqa: E501
        :type: str
        """
        if acquired_date is None:
            raise ValueError("Invalid value for `acquired_date`, must not be `None`")  # noqa: E501

        self._acquired_date = acquired_date

    @property
    def assigned_to(self):
        """Gets the assigned_to of this Number.  # noqa: E501

        IDs of the user to whom this number is assigned  # noqa: E501

        :return: The assigned_to of this Number.  # noqa: E501
        :rtype: list[str]
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to):
        """Sets the assigned_to of this Number.

        IDs of the user to whom this number is assigned  # noqa: E501

        :param assigned_to: The assigned_to of this Number.  # noqa: E501
        :type: list[str]
        """
        if assigned_to is None:
            raise ValueError("Invalid value for `assigned_to`, must not be `None`")  # noqa: E501

        self._assigned_to = assigned_to

    @property
    def expiration_date(self):
        """Gets the expiration_date of this Number.  # noqa: E501

        Number expiration date, might be blank  # noqa: E501

        :return: The expiration_date of this Number.  # noqa: E501
        :rtype: str
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this Number.

        Number expiration date, might be blank  # noqa: E501

        :param expiration_date: The expiration_date of this Number.  # noqa: E501
        :type: str
        """

        self._expiration_date = expiration_date

    @property
    def id(self):
        """Gets the id of this Number.  # noqa: E501

        Number ID  # noqa: E501

        :return: The id of this Number.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Number.

        Number ID  # noqa: E501

        :param id: The id of this Number.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_canceled(self):
        """Gets the is_canceled of this Number.  # noqa: E501

        True if number is canceled but not yet deleted  # noqa: E501

        :return: The is_canceled of this Number.  # noqa: E501
        :rtype: bool
        """
        return self._is_canceled

    @is_canceled.setter
    def is_canceled(self, is_canceled):
        """Sets the is_canceled of this Number.

        True if number is canceled but not yet deleted  # noqa: E501

        :param is_canceled: The is_canceled of this Number.  # noqa: E501
        :type: bool
        """

        self._is_canceled = is_canceled

    @property
    def notifications(self):
        """Gets the notifications of this Number.  # noqa: E501


        :return: The notifications of this Number.  # noqa: E501
        :rtype: list[NumberNotifications]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this Number.


        :param notifications: The notifications of this Number.  # noqa: E501
        :type: list[NumberNotifications]
        """

        self._notifications = notifications

    @property
    def number(self):
        """Gets the number of this Number.  # noqa: E501

        Fax number  # noqa: E501

        :return: The number of this Number.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Number.

        Fax number  # noqa: E501

        :param number: The number of this Number.  # noqa: E501
        :type: str
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501
        if number and not re.search(r'^[+][0-9]{8,}$', number):  # noqa: E501
            raise ValueError(r"Invalid value for `number`, must be a follow pattern or equal to `/^[+][0-9]{8,}$/`")  # noqa: E501

        self._number = number

    @property
    def owner_id(self):
        """Gets the owner_id of this Number.  # noqa: E501

        Number owner ID  # noqa: E501

        :return: The owner_id of this Number.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this Number.

        Number owner ID  # noqa: E501

        :param owner_id: The owner_id of this Number.  # noqa: E501
        :type: str
        """
        if owner_id is None:
            raise ValueError("Invalid value for `owner_id`, must not be `None`")  # noqa: E501

        self._owner_id = owner_id

    @property
    def status(self):
        """Gets the status of this Number.  # noqa: E501


        :return: The status of this Number.  # noqa: E501
        :rtype: NumberStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Number.


        :param status: The status of this Number.  # noqa: E501
        :type: NumberStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if issubclass(Number, dict):
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
        if not isinstance(other, Number):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

