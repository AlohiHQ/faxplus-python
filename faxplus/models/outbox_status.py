# coding: utf-8

"""
    FAX.PLUS REST API

    OpenAPI spec version: 1.2.0
    Contact: info@fax.plus
"""

from enum import Enum


class OutboxStatus(str, Enum):
    """
    Outbound fax status
    """
    SUBMITTED = "submitted",
    CONVERTING = "converting",
    SCHEDULED_FOR_SENDING = "scheduled_for_sending",
    SENDING = "sending"

    def __str__(self):
        return str(self.value)
