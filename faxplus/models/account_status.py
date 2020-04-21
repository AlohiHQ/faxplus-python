# coding: utf-8

"""
    FAX.PLUS REST API

    OpenAPI spec version: 1.2.0
    Contact: info@fax.plus
"""

from enum import Enum


class AccountStatus(str, Enum):
    """
    Your account status which could be active, inactive etc
    """
    ACTIVE = "active",
    UNVERIFIED_PHONE = "unverified_phone",
    SUSPENDED = "suspended",
    DISABLED = "disabled",
    INACTIVE = "inactive",
    DELETED = "deleted",
    CORPORATE_DELETED = "corporate_deleted",
    WAITING_FOR_SIGNUP = "waiting_for_signup"

    def __str__(self):
        return str(self.value)
