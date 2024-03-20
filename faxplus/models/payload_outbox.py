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


class PayloadOutbox(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'from_number': 'str',
        'to': 'list[str]',
        'files': 'list[str]',
        'comment': 'OutboxComment',
        'options': 'OutboxOptions',
        'send_time': 'str',
        'return_ids': 'bool',
        'cover_page': 'OutboxCoverPage'
    }

    attribute_map = {
        'from_number': 'from',
        'to': 'to',
        'files': 'files',
        'comment': 'comment',
        'options': 'options',
        'send_time': 'send_time',
        'return_ids': 'return_ids',
        'cover_page': 'cover_page'
    }

    def __init__(self, from_number=None, to=None, files=None, comment=None, options=None, send_time=None, return_ids=False, cover_page=None):  # noqa: E501
        """PayloadOutbox - a model defined in Swagger

        :param str from_number: Number to use for sending the fax (required)
        :param list[str] to: List of fax destination numbers (required)
        :param list[str] files: List of file names to send. Files should be uploaded beforehand. (required)
        :param OutboxComment comment:
        :param OutboxOptions options:
        :param str send_time: Date when to send the fax. Format: **YYYY-MM-DD HH:mm:ss +HHMM**
        :param bool return_ids: Return scheduled fax IDs to use for tracking and with webhooks
        :param OutboxCoverPage cover_page:
        """  # noqa: E501
        self._from_number = None
        self._to = None
        self._files = None
        self._comment = None
        self._options = None
        self._send_time = None
        self._return_ids = None
        self._cover_page = None
        self.discriminator = None
        self.from_number = from_number
        self.to = to
        self.files = files
        if comment is not None:
            self.comment = comment
        if options is not None:
            self.options = options
        if send_time is not None:
            self.send_time = send_time
        if return_ids is not None:
            self.return_ids = return_ids
        if cover_page is not None:
            self.cover_page = cover_page

    @property
    def from_number(self):
        """Gets the from_number of this PayloadOutbox.  # noqa: E501

        Number to use for sending the fax  # noqa: E501

        :return: The from_number of this PayloadOutbox.  # noqa: E501
        :rtype: str
        """
        return self._from_number

    @from_number.setter
    def from_number(self, from_number):
        """Sets the from_number of this PayloadOutbox.

        Number to use for sending the fax  # noqa: E501

        :param from_number: The from_number of this PayloadOutbox.  # noqa: E501
        :type: str
        """
        if from_number is None:
            raise ValueError("Invalid value for `from_number`, must not be `None`")  # noqa: E501
        if from_number and not re.search(r'^([+][0-9]{8,}([*]{0,10}[0-9]+)?)|(no_number)|(NO_NUMBER)$', from_number):  # noqa: E501
            raise ValueError(r"Invalid value for `from_number`, must be a follow pattern or equal to `/^([+][0-9]{8,}([*]{0,10}[0-9]+)?)|(no_number)|(NO_NUMBER)$/`")  # noqa: E501

        self._from_number = from_number

    @property
    def to(self):
        """Gets the to of this PayloadOutbox.  # noqa: E501

        List of fax destination numbers  # noqa: E501

        :return: The to of this PayloadOutbox.  # noqa: E501
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this PayloadOutbox.

        List of fax destination numbers  # noqa: E501

        :param to: The to of this PayloadOutbox.  # noqa: E501
        :type: list[str]
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def files(self):
        """Gets the files of this PayloadOutbox.  # noqa: E501

        List of file names to send. Files should be uploaded beforehand.  # noqa: E501

        :return: The files of this PayloadOutbox.  # noqa: E501
        :rtype: list[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this PayloadOutbox.

        List of file names to send. Files should be uploaded beforehand.  # noqa: E501

        :param files: The files of this PayloadOutbox.  # noqa: E501
        :type: list[str]
        """
        if files is None:
            raise ValueError("Invalid value for `files`, must not be `None`")  # noqa: E501

        self._files = files

    @property
    def comment(self):
        """Gets the comment of this PayloadOutbox.  # noqa: E501


        :return: The comment of this PayloadOutbox.  # noqa: E501
        :rtype: OutboxComment
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this PayloadOutbox.


        :param comment: The comment of this PayloadOutbox.  # noqa: E501
        :type: OutboxComment
        """

        self._comment = comment

    @property
    def options(self):
        """Gets the options of this PayloadOutbox.  # noqa: E501


        :return: The options of this PayloadOutbox.  # noqa: E501
        :rtype: OutboxOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this PayloadOutbox.


        :param options: The options of this PayloadOutbox.  # noqa: E501
        :type: OutboxOptions
        """

        self._options = options

    @property
    def send_time(self):
        """Gets the send_time of this PayloadOutbox.  # noqa: E501

        Date when to send the fax. Format: **YYYY-MM-DD HH:mm:ss +HHMM**  # noqa: E501

        :return: The send_time of this PayloadOutbox.  # noqa: E501
        :rtype: str
        """
        return self._send_time

    @send_time.setter
    def send_time(self, send_time):
        """Sets the send_time of this PayloadOutbox.

        Date when to send the fax. Format: **YYYY-MM-DD HH:mm:ss +HHMM**  # noqa: E501

        :param send_time: The send_time of this PayloadOutbox.  # noqa: E501
        :type: str
        """
        if send_time and not re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} [+][0-9]{4}', send_time):  # noqa: E501
            raise ValueError(r"Invalid value for `send_time`, must be a follow pattern or equal to `/^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} [+][0-9]{4}/`")  # noqa: E501

        self._send_time = send_time

    @property
    def return_ids(self):
        """Gets the return_ids of this PayloadOutbox.  # noqa: E501

        Return scheduled fax IDs to use for tracking and with webhooks  # noqa: E501

        :return: The return_ids of this PayloadOutbox.  # noqa: E501
        :rtype: bool
        """
        return self._return_ids

    @return_ids.setter
    def return_ids(self, return_ids):
        """Sets the return_ids of this PayloadOutbox.

        Return scheduled fax IDs to use for tracking and with webhooks  # noqa: E501

        :param return_ids: The return_ids of this PayloadOutbox.  # noqa: E501
        :type: bool
        """

        self._return_ids = return_ids

    @property
    def cover_page(self):
        """Gets the cover_page of this PayloadOutbox.  # noqa: E501


        :return: The cover_page of this PayloadOutbox.  # noqa: E501
        :rtype: OutboxCoverPage
        """
        return self._cover_page

    @cover_page.setter
    def cover_page(self, cover_page):
        """Sets the cover_page of this PayloadOutbox.


        :param cover_page: The cover_page of this PayloadOutbox.  # noqa: E501
        :type: OutboxCoverPage
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
        if issubclass(PayloadOutbox, dict):
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
        if not isinstance(other, PayloadOutbox):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

