# coding: utf-8

"""
    Fax.Plus REST API

    Visit https://apidoc.fax.plus for more information.

    © Alohi SA (Geneva, Switzerland)

    https://www.alohi.com
    Contact: info@fax.plus
"""

from enum import Enum


class FaxCategory(str, Enum):

    INBOX = "inbox",
    SENT = "sent",
    SPAM = "spam"

    def __str__(self):
        return str(self.value)
