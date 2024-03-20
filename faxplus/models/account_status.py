# coding: utf-8

"""
    Fax.Plus REST API

    Visit https://apidoc.fax.plus for more information.

    © Alohi SA (Geneva, Switzerland)

    https://www.alohi.com
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
