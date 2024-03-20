# coding: utf-8

"""
    Fax.Plus REST API

    Visit https://apidoc.fax.plus for more information.

    © Alohi SA (Geneva, Switzerland)

    https://www.alohi.com
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
