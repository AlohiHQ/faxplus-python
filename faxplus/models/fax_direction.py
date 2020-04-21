# coding: utf-8

"""
    FAX.PLUS REST API

    OpenAPI spec version: 1.2.0
    Contact: info@fax.plus
"""

from enum import Enum


class FaxDirection(str, Enum):
    """
    Fax direction
    """
    OUTGOING = "outgoing",
    INCOMING = "incoming"

    def __str__(self):
        return str(self.value)
