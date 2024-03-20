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


class Fax(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'comment': 'str',
        'cost': 'int',
        'cost_details': 'FaxCostDetails',
        'description': 'str',
        'direction': 'FaxDirection',
        'duration': 'int',
        'file': 'str',
        'file_name': 'str',
        'from_number': 'str',
        'header': 'str',
        'id': 'str',
        'is_read': 'bool',
        'is_spam': 'bool',
        'last_update': 'str',
        'max_retry': 'int',
        'owner_id': 'str',
        'pages': 'int',
        'retry_delay': 'int',
        'scheduled_time': 'str',
        'start_time': 'str',
        'status': 'FaxStatus',
        'submit_time': 'str',
        'to': 'str',
        'cover_page': 'FaxCoverPage'
    }

    attribute_map = {
        'comment': 'comment',
        'cost': 'cost',
        'cost_details': 'cost_details',
        'description': 'description',
        'direction': 'direction',
        'duration': 'duration',
        'file': 'file',
        'file_name': 'file_name',
        'from_number': 'from',
        'header': 'header',
        'id': 'id',
        'is_read': 'is_read',
        'is_spam': 'is_spam',
        'last_update': 'last_update',
        'max_retry': 'max_retry',
        'owner_id': 'owner_id',
        'pages': 'pages',
        'retry_delay': 'retry_delay',
        'scheduled_time': 'scheduled_time',
        'start_time': 'start_time',
        'status': 'status',
        'submit_time': 'submit_time',
        'to': 'to',
        'cover_page': 'cover_page'
    }

    def __init__(self, comment=None, cost=None, cost_details=None, description=None, direction=None, duration=None, file=None, file_name=None, from_number=None, header=None, id=None, is_read=None, is_spam=None, last_update=None, max_retry=None, owner_id=None, pages=None, retry_delay=None, scheduled_time=None, start_time=None, status=None, submit_time=None, to=None, cover_page=None):  # noqa: E501
        """Fax - a model defined in Swagger

        :param str comment: Free-form comment (required)
        :param int cost: Fax cost in the user currency
        :param FaxCostDetails cost_details: (required)
        :param str description:
        :param FaxDirection direction:
        :param int duration:
        :param str file: Fax file ID for the getFile handle
        :param str file_name: Human-readable file name
        :param str from_number: Sender number. Might be a userId for faxes sent or received with free accounts
        :param str header:
        :param str id: Fax ID (required)
        :param bool is_read:
        :param bool is_spam: True if the fax is marked as spam
        :param str last_update:
        :param int max_retry: Maximum number of retries
        :param str owner_id: User ID of the fax owner (required)
        :param int pages: Number of pages in the fax (required)
        :param int retry_delay: Delay between two retries
        :param str scheduled_time:
        :param str start_time: Time at which faxing session started. Format: YYYY-MM-DD HH:mm:ss
        :param FaxStatus status: (required)
        :param str submit_time: Time when the fax was submitted for sending. For outgoing faxes only
        :param str to: Fax destination number. Might be a userId for faxes sent or received with free accounts
        :param FaxCoverPage cover_page:
        """  # noqa: E501
        self._comment = None
        self._cost = None
        self._cost_details = None
        self._description = None
        self._direction = None
        self._duration = None
        self._file = None
        self._file_name = None
        self._from_number = None
        self._header = None
        self._id = None
        self._is_read = None
        self._is_spam = None
        self._last_update = None
        self._max_retry = None
        self._owner_id = None
        self._pages = None
        self._retry_delay = None
        self._scheduled_time = None
        self._start_time = None
        self._status = None
        self._submit_time = None
        self._to = None
        self._cover_page = None
        self.discriminator = None
        self.comment = comment
        if cost is not None:
            self.cost = cost
        self.cost_details = cost_details
        if description is not None:
            self.description = description
        if direction is not None:
            self.direction = direction
        if duration is not None:
            self.duration = duration
        if file is not None:
            self.file = file
        if file_name is not None:
            self.file_name = file_name
        if from_number is not None:
            self.from_number = from_number
        if header is not None:
            self.header = header
        self.id = id
        if is_read is not None:
            self.is_read = is_read
        if is_spam is not None:
            self.is_spam = is_spam
        if last_update is not None:
            self.last_update = last_update
        if max_retry is not None:
            self.max_retry = max_retry
        self.owner_id = owner_id
        self.pages = pages
        if retry_delay is not None:
            self.retry_delay = retry_delay
        if scheduled_time is not None:
            self.scheduled_time = scheduled_time
        if start_time is not None:
            self.start_time = start_time
        self.status = status
        if submit_time is not None:
            self.submit_time = submit_time
        if to is not None:
            self.to = to
        if cover_page is not None:
            self.cover_page = cover_page

    @property
    def comment(self):
        """Gets the comment of this Fax.  # noqa: E501

        Free-form comment  # noqa: E501

        :return: The comment of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Fax.

        Free-form comment  # noqa: E501

        :param comment: The comment of this Fax.  # noqa: E501
        :type: str
        """
        if comment is None:
            raise ValueError("Invalid value for `comment`, must not be `None`")  # noqa: E501

        self._comment = comment

    @property
    def cost(self):
        """Gets the cost of this Fax.  # noqa: E501

        Fax cost in the user currency  # noqa: E501

        :return: The cost of this Fax.  # noqa: E501
        :rtype: int
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this Fax.

        Fax cost in the user currency  # noqa: E501

        :param cost: The cost of this Fax.  # noqa: E501
        :type: int
        """
        if cost is not None and cost < 0:  # noqa: E501
            raise ValueError("Invalid value for `cost`, must be a value greater than or equal to `0`")  # noqa: E501

        self._cost = cost

    @property
    def cost_details(self):
        """Gets the cost_details of this Fax.  # noqa: E501


        :return: The cost_details of this Fax.  # noqa: E501
        :rtype: FaxCostDetails
        """
        return self._cost_details

    @cost_details.setter
    def cost_details(self, cost_details):
        """Sets the cost_details of this Fax.


        :param cost_details: The cost_details of this Fax.  # noqa: E501
        :type: FaxCostDetails
        """
        if cost_details is None:
            raise ValueError("Invalid value for `cost_details`, must not be `None`")  # noqa: E501

        self._cost_details = cost_details

    @property
    def description(self):
        """Gets the description of this Fax.  # noqa: E501


        :return: The description of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Fax.


        :param description: The description of this Fax.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def direction(self):
        """Gets the direction of this Fax.  # noqa: E501


        :return: The direction of this Fax.  # noqa: E501
        :rtype: FaxDirection
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this Fax.


        :param direction: The direction of this Fax.  # noqa: E501
        :type: FaxDirection
        """

        self._direction = direction

    @property
    def duration(self):
        """Gets the duration of this Fax.  # noqa: E501


        :return: The duration of this Fax.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Fax.


        :param duration: The duration of this Fax.  # noqa: E501
        :type: int
        """
        if duration is not None and duration < 0:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value greater than or equal to `0`")  # noqa: E501

        self._duration = duration

    @property
    def file(self):
        """Gets the file of this Fax.  # noqa: E501

        Fax file ID for the getFile handle  # noqa: E501

        :return: The file of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this Fax.

        Fax file ID for the getFile handle  # noqa: E501

        :param file: The file of this Fax.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def file_name(self):
        """Gets the file_name of this Fax.  # noqa: E501

        Human-readable file name  # noqa: E501

        :return: The file_name of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this Fax.

        Human-readable file name  # noqa: E501

        :param file_name: The file_name of this Fax.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def from_number(self):
        """Gets the from_number of this Fax.  # noqa: E501

        Sender number. Might be a userId for faxes sent or received with free accounts  # noqa: E501

        :return: The from_number of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._from_number

    @from_number.setter
    def from_number(self, from_number):
        """Sets the from_number of this Fax.

        Sender number. Might be a userId for faxes sent or received with free accounts  # noqa: E501

        :param from_number: The from_number of this Fax.  # noqa: E501
        :type: str
        """

        self._from_number = from_number

    @property
    def header(self):
        """Gets the header of this Fax.  # noqa: E501


        :return: The header of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this Fax.


        :param header: The header of this Fax.  # noqa: E501
        :type: str
        """

        self._header = header

    @property
    def id(self):
        """Gets the id of this Fax.  # noqa: E501

        Fax ID  # noqa: E501

        :return: The id of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Fax.

        Fax ID  # noqa: E501

        :param id: The id of this Fax.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_read(self):
        """Gets the is_read of this Fax.  # noqa: E501


        :return: The is_read of this Fax.  # noqa: E501
        :rtype: bool
        """
        return self._is_read

    @is_read.setter
    def is_read(self, is_read):
        """Sets the is_read of this Fax.


        :param is_read: The is_read of this Fax.  # noqa: E501
        :type: bool
        """

        self._is_read = is_read

    @property
    def is_spam(self):
        """Gets the is_spam of this Fax.  # noqa: E501

        True if the fax is marked as spam  # noqa: E501

        :return: The is_spam of this Fax.  # noqa: E501
        :rtype: bool
        """
        return self._is_spam

    @is_spam.setter
    def is_spam(self, is_spam):
        """Sets the is_spam of this Fax.

        True if the fax is marked as spam  # noqa: E501

        :param is_spam: The is_spam of this Fax.  # noqa: E501
        :type: bool
        """

        self._is_spam = is_spam

    @property
    def last_update(self):
        """Gets the last_update of this Fax.  # noqa: E501


        :return: The last_update of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this Fax.


        :param last_update: The last_update of this Fax.  # noqa: E501
        :type: str
        """

        self._last_update = last_update

    @property
    def max_retry(self):
        """Gets the max_retry of this Fax.  # noqa: E501

        Maximum number of retries  # noqa: E501

        :return: The max_retry of this Fax.  # noqa: E501
        :rtype: int
        """
        return self._max_retry

    @max_retry.setter
    def max_retry(self, max_retry):
        """Sets the max_retry of this Fax.

        Maximum number of retries  # noqa: E501

        :param max_retry: The max_retry of this Fax.  # noqa: E501
        :type: int
        """
        if max_retry is not None and max_retry > 3:  # noqa: E501
            raise ValueError("Invalid value for `max_retry`, must be a value less than or equal to `3`")  # noqa: E501
        if max_retry is not None and max_retry < 0:  # noqa: E501
            raise ValueError("Invalid value for `max_retry`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_retry = max_retry

    @property
    def owner_id(self):
        """Gets the owner_id of this Fax.  # noqa: E501

        User ID of the fax owner  # noqa: E501

        :return: The owner_id of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this Fax.

        User ID of the fax owner  # noqa: E501

        :param owner_id: The owner_id of this Fax.  # noqa: E501
        :type: str
        """
        if owner_id is None:
            raise ValueError("Invalid value for `owner_id`, must not be `None`")  # noqa: E501

        self._owner_id = owner_id

    @property
    def pages(self):
        """Gets the pages of this Fax.  # noqa: E501

        Number of pages in the fax  # noqa: E501

        :return: The pages of this Fax.  # noqa: E501
        :rtype: int
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this Fax.

        Number of pages in the fax  # noqa: E501

        :param pages: The pages of this Fax.  # noqa: E501
        :type: int
        """
        if pages is None:
            raise ValueError("Invalid value for `pages`, must not be `None`")  # noqa: E501
        if pages is not None and pages < 0:  # noqa: E501
            raise ValueError("Invalid value for `pages`, must be a value greater than or equal to `0`")  # noqa: E501

        self._pages = pages

    @property
    def retry_delay(self):
        """Gets the retry_delay of this Fax.  # noqa: E501

        Delay between two retries  # noqa: E501

        :return: The retry_delay of this Fax.  # noqa: E501
        :rtype: int
        """
        return self._retry_delay

    @retry_delay.setter
    def retry_delay(self, retry_delay):
        """Sets the retry_delay of this Fax.

        Delay between two retries  # noqa: E501

        :param retry_delay: The retry_delay of this Fax.  # noqa: E501
        :type: int
        """
        if retry_delay is not None and retry_delay > 30:  # noqa: E501
            raise ValueError("Invalid value for `retry_delay`, must be a value less than or equal to `30`")  # noqa: E501
        if retry_delay is not None and retry_delay < 0:  # noqa: E501
            raise ValueError("Invalid value for `retry_delay`, must be a value greater than or equal to `0`")  # noqa: E501

        self._retry_delay = retry_delay

    @property
    def scheduled_time(self):
        """Gets the scheduled_time of this Fax.  # noqa: E501


        :return: The scheduled_time of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._scheduled_time

    @scheduled_time.setter
    def scheduled_time(self, scheduled_time):
        """Sets the scheduled_time of this Fax.


        :param scheduled_time: The scheduled_time of this Fax.  # noqa: E501
        :type: str
        """

        self._scheduled_time = scheduled_time

    @property
    def start_time(self):
        """Gets the start_time of this Fax.  # noqa: E501

        Time at which faxing session started. Format: YYYY-MM-DD HH:mm:ss  # noqa: E501

        :return: The start_time of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Fax.

        Time at which faxing session started. Format: YYYY-MM-DD HH:mm:ss  # noqa: E501

        :param start_time: The start_time of this Fax.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this Fax.  # noqa: E501


        :return: The status of this Fax.  # noqa: E501
        :rtype: FaxStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Fax.


        :param status: The status of this Fax.  # noqa: E501
        :type: FaxStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def submit_time(self):
        """Gets the submit_time of this Fax.  # noqa: E501

        Time when the fax was submitted for sending. For outgoing faxes only  # noqa: E501

        :return: The submit_time of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._submit_time

    @submit_time.setter
    def submit_time(self, submit_time):
        """Sets the submit_time of this Fax.

        Time when the fax was submitted for sending. For outgoing faxes only  # noqa: E501

        :param submit_time: The submit_time of this Fax.  # noqa: E501
        :type: str
        """

        self._submit_time = submit_time

    @property
    def to(self):
        """Gets the to of this Fax.  # noqa: E501

        Fax destination number. Might be a userId for faxes sent or received with free accounts  # noqa: E501

        :return: The to of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this Fax.

        Fax destination number. Might be a userId for faxes sent or received with free accounts  # noqa: E501

        :param to: The to of this Fax.  # noqa: E501
        :type: str
        """

        self._to = to

    @property
    def cover_page(self):
        """Gets the cover_page of this Fax.  # noqa: E501


        :return: The cover_page of this Fax.  # noqa: E501
        :rtype: FaxCoverPage
        """
        return self._cover_page

    @cover_page.setter
    def cover_page(self, cover_page):
        """Sets the cover_page of this Fax.


        :param cover_page: The cover_page of this Fax.  # noqa: E501
        :type: FaxCoverPage
        """

        self._cover_page = cover_page

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
        if issubclass(Fax, dict):
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
        if not isinstance(other, Fax):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

