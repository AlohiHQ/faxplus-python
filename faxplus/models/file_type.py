# coding: utf-8

"""
    FAX.PLUS REST API

    OpenAPI spec version: 1.2.0
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
