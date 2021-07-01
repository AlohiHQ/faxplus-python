# coding: utf-8

"""
    FAX.PLUS REST API

    Visit https://apidoc.fax.plus for more information.

    © Alohi SA (Geneva, Switzerland)

    https://www.alohi.com
    Contact: info@fax.plus
"""

from enum import Enum


class WebhookEventType(str, Enum):
    """
    Webhook event type
    """
    FAX_RECEIVED = "fax_received"

    def __str__(self):
        return str(self.value)
