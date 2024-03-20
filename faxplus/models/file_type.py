# coding: utf-8

"""
    Fax.Plus REST API

    Visit https://apidoc.fax.plus for more information.

    © Alohi SA (Geneva, Switzerland)

    https://www.alohi.com
    Contact: info@fax.plus
"""

from enum import Enum


class FileType(str, Enum):
    """
    File type
    """
    TIFF = "tiff",
    PDF = "pdf"

    def __str__(self):
        return str(self.value)
