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
        'uid': 'str',
        'pages': 'float',
        'from_number': 'str',
        'to_number': 'str',
        'start_time': 'str',
        'file': 'str',
        'file_name': 'str',
        'cost': 'float',
        'status': 'FaxStatus'
    }

    attribute_map = {
        'id': 'id',
        'uid': 'uid',
        'pages': 'pages',
        'from_number': 'from_number',
        'to_number': 'to_number',
        'start_time': 'start_time',
        'file': 'file',
        'file_name': 'file_name',
        'cost': 'cost',
        'status': 'status'
    }

    def __init__(self, id=None, uid=None, pages=None, from_number=None, to_number=None, start_time=None, file=None, file_name=None, cost=None, status=None):  # noqa: E501
        """WebhookCallbackData - a model defined in Swagger

        :param str id: Fax session ID. Note that this ID might be different from the one returned by the listFaxes handle, as this ID refers to the faxing session as a whole, with retries included. Both IDs can be used with the API getFile handle
        :param str uid: Sender user ID
        :param float pages: Number of pages in the fax
        :param str from_number: Sender number. Might be a user ID for faxes sent from free accounts
        :param str to_number: Fax destination number. Might be a user ID for faxes sent from free accounts
        :param str start_time: Time at which faxing session started. Format: YYYY-MM-DD HH:mm:ss
        :param str file: File ID
        :param str file_name: Human-readable file name
        :param float cost: Fax cost (in pages)
        :param FaxStatus status:
        """  # noqa: E501
        self._id = None
        self._uid = None
        self._pages = None
        self._from_number = None
        self._to_number = None
        self._start_time = None
        self._file = None
        self._file_name = None
        self._cost = None
        self._status = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if uid is not None:
            self.uid = uid
        if pages is not None:
            self.pages = pages
        if from_number is not None:
            self.from_number = from_number
        if to_number is not None:
            self.to_number = to_number
        if start_time is not None:
            self.start_time = start_time
        if file is not None:
            self.file = file
        if file_name is not None:
            self.file_name = file_name
        if cost is not None:
            self.cost = cost
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this WebhookCallbackData.  # noqa: E501

        Fax session ID. Note that this ID might be different from the one returned by the listFaxes handle, as this ID refers to the faxing session as a whole, with retries included. Both IDs can be used with the API getFile handle  # noqa: E501

        :return: The id of this WebhookCallbackData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookCallbackData.

        Fax session ID. Note that this ID might be different from the one returned by the listFaxes handle, as this ID refers to the faxing session as a whole, with retries included. Both IDs can be used with the API getFile handle  # noqa: E501

        :param id: The id of this WebhookCallbackData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def uid(self):
        """Gets the uid of this WebhookCallbackData.  # noqa: E501

        Sender user ID  # noqa: E501

        :return: The uid of this WebhookCallbackData.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this WebhookCallbackData.

        Sender user ID  # noqa: E501

        :param uid: The uid of this WebhookCallbackData.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def pages(self):
        """Gets the pages of this WebhookCallbackData.  # noqa: E501

        Number of pages in the fax  # noqa: E501

        :return: The pages of this WebhookCallbackData.  # noqa: E501
        :rtype: float
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this WebhookCallbackData.

        Number of pages in the fax  # noqa: E501

        :param pages: The pages of this WebhookCallbackData.  # noqa: E501
        :type: float
        """

        self._pages = pages

    @property
    def from_number(self):
        """Gets the from_number of this WebhookCallbackData.  # noqa: E501

        Sender number. Might be a user ID for faxes sent from free accounts  # noqa: E501

        :return: The from_number of this WebhookCallbackData.  # noqa: E501
        :rtype: str
        """
        return self._from_number

    @from_number.setter
    def from_number(self, from_number):
        """Sets the from_number of this WebhookCallbackData.

        Sender number. Might be a user ID for faxes sent from free accounts  # noqa: E501

        :param from_number: The from_number of this WebhookCallbackData.  # noqa: E501
        :type: str
        """

        self._from_number = from_number

    @property
    def to_number(self):
        """Gets the to_number of this WebhookCallbackData.  # noqa: E501

        Fax destination number. Might be a user ID for faxes sent from free accounts  # noqa: E501

        :return: The to_number of this WebhookCallbackData.  # noqa: E501
        :rtype: str
        """
        return self._to_number

    @to_number.setter
    def to_number(self, to_number):
        """Sets the to_number of this WebhookCallbackData.

        Fax destination number. Might be a user ID for faxes sent from free accounts  # noqa: E501

        :param to_number: The to_number of this WebhookCallbackData.  # noqa: E501
        :type: str
        """

        self._to_number = to_number

    @property
    def start_time(self):
        """Gets the start_time of this WebhookCallbackData.  # noqa: E501

        Time at which faxing session started. Format: YYYY-MM-DD HH:mm:ss  # noqa: E501

        :return: The start_time of this WebhookCallbackData.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this WebhookCallbackData.

        Time at which faxing session started. Format: YYYY-MM-DD HH:mm:ss  # noqa: E501

        :param start_time: The start_time of this WebhookCallbackData.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def file(self):
        """Gets the file of this WebhookCallbackData.  # noqa: E501

        File ID  # noqa: E501

        :return: The file of this WebhookCallbackData.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this WebhookCallbackData.

        File ID  # noqa: E501

        :param file: The file of this WebhookCallbackData.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def file_name(self):
        """Gets the file_name of this WebhookCallbackData.  # noqa: E501

        Human-readable file name  # noqa: E501

        :return: The file_name of this WebhookCallbackData.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this WebhookCallbackData.

        Human-readable file name  # noqa: E501

        :param file_name: The file_name of this WebhookCallbackData.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def cost(self):
        """Gets the cost of this WebhookCallbackData.  # noqa: E501

        Fax cost (in pages)  # noqa: E501

        :return: The cost of this WebhookCallbackData.  # noqa: E501
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this WebhookCallbackData.

        Fax cost (in pages)  # noqa: E501

        :param cost: The cost of this WebhookCallbackData.  # noqa: E501
        :type: float
        """

        self._cost = cost

    @property
    def status(self):
        """Gets the status of this WebhookCallbackData.  # noqa: E501


        :return: The status of this WebhookCallbackData.  # noqa: E501
        :rtype: FaxStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WebhookCallbackData.


        :param status: The status of this WebhookCallbackData.  # noqa: E501
        :type: FaxStatus
        """

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

