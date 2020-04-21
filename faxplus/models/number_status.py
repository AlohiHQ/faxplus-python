# coding: utf-8

"""
    FAX.PLUS REST API

    OpenAPI spec version: 1.2.0
    Contact: info@fax.plus
"""

from enum import Enum


class NumberStatus(str, Enum):
    """
    Status of your fax phone number e.g. active, inactive.
    """
    WAITING_VERIFICATION = "waiting_verification",
    ACTIVE = "active"

    def __str__(self):
        return str(self.value)
