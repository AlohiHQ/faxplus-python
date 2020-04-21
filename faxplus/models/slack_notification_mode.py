# coding: utf-8

"""
    FAX.PLUS REST API

    OpenAPI spec version: 1.2.0
    Contact: info@fax.plus
"""

from enum import Enum


class SlackNotificationMode(str, Enum):

    WITH_ATTACHMENT = "with_attachment",
    NO_ATTACHMENT = "no_attachment",
    OFF = "off"

    def __str__(self):
        return str(self.value)
