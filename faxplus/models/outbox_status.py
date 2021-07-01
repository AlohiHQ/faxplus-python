# coding: utf-8

"""
    FAX.PLUS REST API

    Visit https://apidoc.fax.plus for more information.

    © Alohi SA (Geneva, Switzerland)

    https://www.alohi.com
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
