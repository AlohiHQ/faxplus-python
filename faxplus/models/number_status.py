# coding: utf-8

"""
    Fax.Plus REST API

    Visit https://apidoc.fax.plus for more information.

    © Alohi SA (Geneva, Switzerland)

    https://www.alohi.com
    Contact: info@fax.plus
"""

from enum import Enum


class NumberStatus(str, Enum):
    """
    Status of your fax number e.g. active, inactive.
    """
    WAITING_VERIFICATION = "waiting_verification",
    ACTIVE = "active"

    def __str__(self):
        return str(self.value)
