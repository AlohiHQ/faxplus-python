# coding: utf-8

"""
    FAX.PLUS REST API

    OpenAPI spec version: 1.2.0
    Contact: info@fax.plus
"""

from enum import Enum


class AccountType(str, Enum):
    """
    Account type which could be corporate_admin, individual, etc
    """
    CORPORATE_ADMIN = "corporate_admin",
    INDIVIDUAL = "individual",
    CORPORATE_MEMBER = "corporate_member"

    def __str__(self):
        return str(self.value)
