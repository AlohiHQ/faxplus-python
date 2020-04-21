# coding: utf-8

"""
    FAX.PLUS REST API

    OpenAPI spec version: 1.2.0
    Contact: info@fax.plus
"""

from enum import Enum


class FaxCategory(str, Enum):

    INBOX = "inbox",
    SENT = "sent",
    SPAM = "spam"

    def __str__(self):
        return str(self.value)
