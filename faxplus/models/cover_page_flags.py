# coding: utf-8

"""
    Fax.Plus REST API

    Visit https://apidoc.fax.plus for more information.

    © Alohi SA (Geneva, Switzerland)

    https://www.alohi.com
    Contact: info@fax.plus
"""

from enum import Enum


class CoverPageFlags(str, Enum):
    """
    Allowed flags for the cover page
    """
    URGENT = "urgent",
    FOR_REVIEW = "for_review",
    PLEASE_REPLY = "please_reply",
    CONFIDENTIAL = "confidential"

    def __str__(self):
        return str(self.value)
