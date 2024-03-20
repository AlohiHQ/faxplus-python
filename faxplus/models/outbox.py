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


class Outbox(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'comment': 'OutboxComment',
        'contact_name': 'str',
        'designated_src': 'str',
        'extra_info': 'object',
        'file_changes': 'list[OutboxFileChanges]',
        'files': 'list[str]',
        'id': 'str',
        'initiated_from': 'OutboxInitiatedFrom',
        'ip': 'str',
        'last_updated_status_time': 'str',
        'options': 'OutboxOptions',
        'page_count': 'int',
        'retry': 'RetryOptions',
        'send_time': 'str',
        'should_enhance': 'bool',
        'src': 'str',
        'status': 'OutboxStatus',
        'status_changes': 'list[OutboxStatusChanges]',
        'submit_time': 'str',
        'to': 'list[str]',
        'uid': 'str',
        'cover_page': 'OutboxCoverPage'
    }

    attribute_map = {
        'comment': 'comment',
        'contact_name': 'contact_name',
        'designated_src': 'designated_src',
        'extra_info': 'extra_info',
        'file_changes': 'file_changes',
        'files': 'files',
        'id': 'id',
        'initiated_from': 'initiated_from',
        'ip': 'ip',
        'last_updated_status_time': 'last_updated_status_time',
        'options': 'options',
        'page_count': 'page_count',
        'retry': 'retry',
        'send_time': 'send_time',
        'should_enhance': 'should_enhance',
        'src': 'src',
        'status': 'status',
        'status_changes': 'status_changes',
        'submit_time': 'submit_time',
        'to': 'to',
        'uid': 'uid',
        'cover_page': 'cover_page'
    }

    def __init__(self, comment=None, contact_name=None, designated_src=None, extra_info=None, file_changes=None, files=None, id=None, initiated_from=None, ip=None, last_updated_status_time=None, options=None, page_count=None, retry=None, send_time=None, should_enhance=None, src=None, status=None, status_changes=None, submit_time=None, to=None, uid=None, cover_page=None):  # noqa: E501
        """Outbox - a model defined in Swagger

        :param OutboxComment comment:
        :param str contact_name:
        :param str designated_src:
        :param object extra_info:
        :param list[OutboxFileChanges] file_changes:
        :param list[str] files: Files to send
        :param str id: Fax ID (required)
        :param OutboxInitiatedFrom initiated_from:
        :param str ip: IP address from which the send request originated
        :param str last_updated_status_time: Time and date when the send request status was last updated. Format: *YYYY-MM-DD HH:mm:ss*
        :param OutboxOptions options:
        :param int page_count: Number of fax pages
        :param RetryOptions retry:
        :param str send_time:
        :param bool should_enhance:
        :param str src:
        :param OutboxStatus status: (required)
        :param list[OutboxStatusChanges] status_changes:
        :param str submit_time: Date and time when the fax was submitted for sending
        :param list[str] to:
        :param str uid: User ID (required)
        :param OutboxCoverPage cover_page:
        """  # noqa: E501
        self._comment = None
        self._contact_name = None
        self._designated_src = None
        self._extra_info = None
        self._file_changes = None
        self._files = None
        self._id = None
        self._initiated_from = None
        self._ip = None
        self._last_updated_status_time = None
        self._options = None
        self._page_count = None
        self._retry = None
        self._send_time = None
        self._should_enhance = None
        self._src = None
        self._status = None
        self._status_changes = None
        self._submit_time = None
        self._to = None
        self._uid = None
        self._cover_page = None
        self.discriminator = None
        if comment is not None:
            self.comment = comment
        if contact_name is not None:
            self.contact_name = contact_name
        if designated_src is not None:
            self.designated_src = designated_src
        if extra_info is not None:
            self.extra_info = extra_info
        if file_changes is not None:
            self.file_changes = file_changes
        if files is not None:
            self.files = files
        self.id = id
        if initiated_from is not None:
            self.initiated_from = initiated_from
        if ip is not None:
            self.ip = ip
        if last_updated_status_time is not None:
            self.last_updated_status_time = last_updated_status_time
        if options is not None:
            self.options = options
        if page_count is not None:
            self.page_count = page_count
        if retry is not None:
            self.retry = retry
        if send_time is not None:
            self.send_time = send_time
        if should_enhance is not None:
            self.should_enhance = should_enhance
        if src is not None:
            self.src = src
        self.status = status
        if status_changes is not None:
            self.status_changes = status_changes
        if submit_time is not None:
            self.submit_time = submit_time
        if to is not None:
            self.to = to
        self.uid = uid
        if cover_page is not None:
            self.cover_page = cover_page

    @property
    def comment(self):
        """Gets the comment of this Outbox.  # noqa: E501


        :return: The comment of this Outbox.  # noqa: E501
        :rtype: OutboxComment
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Outbox.


        :param comment: The comment of this Outbox.  # noqa: E501
        :type: OutboxComment
        """

        self._comment = comment

    @property
    def contact_name(self):
        """Gets the contact_name of this Outbox.  # noqa: E501


        :return: The contact_name of this Outbox.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this Outbox.


        :param contact_name: The contact_name of this Outbox.  # noqa: E501
        :type: str
        """

        self._contact_name = contact_name

    @property
    def designated_src(self):
        """Gets the designated_src of this Outbox.  # noqa: E501


        :return: The designated_src of this Outbox.  # noqa: E501
        :rtype: str
        """
        return self._designated_src

    @designated_src.setter
    def designated_src(self, designated_src):
        """Sets the designated_src of this Outbox.


        :param designated_src: The designated_src of this Outbox.  # noqa: E501
        :type: str
        """

        self._designated_src = designated_src

    @property
    def extra_info(self):
        """Gets the extra_info of this Outbox.  # noqa: E501


        :return: The extra_info of this Outbox.  # noqa: E501
        :rtype: object
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        """Sets the extra_info of this Outbox.


        :param extra_info: The extra_info of this Outbox.  # noqa: E501
        :type: object
        """

        self._extra_info = extra_info

    @property
    def file_changes(self):
        """Gets the file_changes of this Outbox.  # noqa: E501


        :return: The file_changes of this Outbox.  # noqa: E501
        :rtype: list[OutboxFileChanges]
        """
        return self._file_changes

    @file_changes.setter
    def file_changes(self, file_changes):
        """Sets the file_changes of this Outbox.


        :param file_changes: The file_changes of this Outbox.  # noqa: E501
        :type: list[OutboxFileChanges]
        """

        self._file_changes = file_changes

    @property
    def files(self):
        """Gets the files of this Outbox.  # noqa: E501

        Files to send  # noqa: E501

        :return: The files of this Outbox.  # noqa: E501
        :rtype: list[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Outbox.

        Files to send  # noqa: E501

        :param files: The files of this Outbox.  # noqa: E501
        :type: list[str]
        """

        self._files = files

    @property
    def id(self):
        """Gets the id of this Outbox.  # noqa: E501

        Fax ID  # noqa: E501

        :return: The id of this Outbox.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Outbox.

        Fax ID  # noqa: E501

        :param id: The id of this Outbox.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def initiated_from(self):
        """Gets the initiated_from of this Outbox.  # noqa: E501


        :return: The initiated_from of this Outbox.  # noqa: E501
        :rtype: OutboxInitiatedFrom
        """
        return self._initiated_from

    @initiated_from.setter
    def initiated_from(self, initiated_from):
        """Sets the initiated_from of this Outbox.


        :param initiated_from: The initiated_from of this Outbox.  # noqa: E501
        :type: OutboxInitiatedFrom
        """

        self._initiated_from = initiated_from

    @property
    def ip(self):
        """Gets the ip of this Outbox.  # noqa: E501

        IP address from which the send request originated  # noqa: E501

        :return: The ip of this Outbox.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Outbox.

        IP address from which the send request originated  # noqa: E501

        :param ip: The ip of this Outbox.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def last_updated_status_time(self):
        """Gets the last_updated_status_time of this Outbox.  # noqa: E501

        Time and date when the send request status was last updated. Format: *YYYY-MM-DD HH:mm:ss*  # noqa: E501

        :return: The last_updated_status_time of this Outbox.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_status_time

    @last_updated_status_time.setter
    def last_updated_status_time(self, last_updated_status_time):
        """Sets the last_updated_status_time of this Outbox.

        Time and date when the send request status was last updated. Format: *YYYY-MM-DD HH:mm:ss*  # noqa: E501

        :param last_updated_status_time: The last_updated_status_time of this Outbox.  # noqa: E501
        :type: str
        """
        if last_updated_status_time and not re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}', last_updated_status_time):  # noqa: E501
            raise ValueError(r"Invalid value for `last_updated_status_time`, must be a follow pattern or equal to `/^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}/`")  # noqa: E501

        self._last_updated_status_time = last_updated_status_time

    @property
    def options(self):
        """Gets the options of this Outbox.  # noqa: E501


        :return: The options of this Outbox.  # noqa: E501
        :rtype: OutboxOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this Outbox.


        :param options: The options of this Outbox.  # noqa: E501
        :type: OutboxOptions
        """

        self._options = options

    @property
    def page_count(self):
        """Gets the page_count of this Outbox.  # noqa: E501

        Number of fax pages  # noqa: E501

        :return: The page_count of this Outbox.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this Outbox.

        Number of fax pages  # noqa: E501

        :param page_count: The page_count of this Outbox.  # noqa: E501
        :type: int
        """
        if page_count is not None and page_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `page_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._page_count = page_count

    @property
    def retry(self):
        """Gets the retry of this Outbox.  # noqa: E501


        :return: The retry of this Outbox.  # noqa: E501
        :rtype: RetryOptions
        """
        return self._retry

    @retry.setter
    def retry(self, retry):
        """Sets the retry of this Outbox.


        :param retry: The retry of this Outbox.  # noqa: E501
        :type: RetryOptions
        """

        self._retry = retry

    @property
    def send_time(self):
        """Gets the send_time of this Outbox.  # noqa: E501


        :return: The send_time of this Outbox.  # noqa: E501
        :rtype: str
        """
        return self._send_time

    @send_time.setter
    def send_time(self, send_time):
        """Sets the send_time of this Outbox.


        :param send_time: The send_time of this Outbox.  # noqa: E501
        :type: str
        """

        self._send_time = send_time

    @property
    def should_enhance(self):
        """Gets the should_enhance of this Outbox.  # noqa: E501


        :return: The should_enhance of this Outbox.  # noqa: E501
        :rtype: bool
        """
        return self._should_enhance

    @should_enhance.setter
    def should_enhance(self, should_enhance):
        """Sets the should_enhance of this Outbox.


        :param should_enhance: The should_enhance of this Outbox.  # noqa: E501
        :type: bool
        """

        self._should_enhance = should_enhance

    @property
    def src(self):
        """Gets the src of this Outbox.  # noqa: E501


        :return: The src of this Outbox.  # noqa: E501
        :rtype: str
        """
        return self._src

    @src.setter
    def src(self, src):
        """Sets the src of this Outbox.


        :param src: The src of this Outbox.  # noqa: E501
        :type: str
        """

        self._src = src

    @property
    def status(self):
        """Gets the status of this Outbox.  # noqa: E501


        :return: The status of this Outbox.  # noqa: E501
        :rtype: OutboxStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Outbox.


        :param status: The status of this Outbox.  # noqa: E501
        :type: OutboxStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def status_changes(self):
        """Gets the status_changes of this Outbox.  # noqa: E501


        :return: The status_changes of this Outbox.  # noqa: E501
        :rtype: list[OutboxStatusChanges]
        """
        return self._status_changes

    @status_changes.setter
    def status_changes(self, status_changes):
        """Sets the status_changes of this Outbox.


        :param status_changes: The status_changes of this Outbox.  # noqa: E501
        :type: list[OutboxStatusChanges]
        """

        self._status_changes = status_changes

    @property
    def submit_time(self):
        """Gets the submit_time of this Outbox.  # noqa: E501

        Date and time when the fax was submitted for sending  # noqa: E501

        :return: The submit_time of this Outbox.  # noqa: E501
        :rtype: str
        """
        return self._submit_time

    @submit_time.setter
    def submit_time(self, submit_time):
        """Sets the submit_time of this Outbox.

        Date and time when the fax was submitted for sending  # noqa: E501

        :param submit_time: The submit_time of this Outbox.  # noqa: E501
        :type: str
        """

        self._submit_time = submit_time

    @property
    def to(self):
        """Gets the to of this Outbox.  # noqa: E501


        :return: The to of this Outbox.  # noqa: E501
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this Outbox.


        :param to: The to of this Outbox.  # noqa: E501
        :type: list[str]
        """

        self._to = to

    @property
    def uid(self):
        """Gets the uid of this Outbox.  # noqa: E501

        User ID  # noqa: E501

        :return: The uid of this Outbox.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this Outbox.

        User ID  # noqa: E501

        :param uid: The uid of this Outbox.  # noqa: E501
        :type: str
        """
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

    @property
    def cover_page(self):
        """Gets the cover_page of this Outbox.  # noqa: E501


        :return: The cover_page of this Outbox.  # noqa: E501
        :rtype: OutboxCoverPage
        """
        return self._cover_page

    @cover_page.setter
    def cover_page(self, cover_page):
        """Sets the cover_page of this Outbox.


        :param cover_page: The cover_page of this Outbox.  # noqa: E501
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
        if issubclass(Outbox, dict):
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
        if not isinstance(other, Outbox):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

