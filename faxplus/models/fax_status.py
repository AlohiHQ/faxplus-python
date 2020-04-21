# coding: utf-8

"""
    FAX.PLUS REST API

    OpenAPI spec version: 1.2.0
    Contact: info@fax.plus
"""

from enum import Enum


class FaxStatus(str, Enum):
    """
    Fax status
    """
    SUCCESS = "success",
    PARTIALLY_SENT = "partially_sent",
    PARTIALLY_RECEIVED = "partially_received",
    INSUFFICIENT_CREDIT = "insufficient_credit",
    FAILED = "failed",
    FAILED_INTERNAL_PROCESS_ERROR = "failed_internal_process_error",
    FAILED_SEPARATE_FILE_PAGES_ISSUE = "failed_separate_file_pages_issue",
    FAILED_RENDER_HEADER_ISSUE = "failed_render_header_issue",
    FAILED_INVALID_NUMBER_FORMAT = "failed_invalid_number_format",
    FAILED_MIMETYPE_NOT_SUPPORTED = "failed_mimetype_not_supported",
    FAILED_DESTINATION_NOT_SUPPORTED = "failed_destination_not_supported",
    FAILED_TO_SEND = "failed_to_send",
    FAILED_NORMAL_TEMPORARY_FAILURE = "failed_normal_temporary_failure",
    FAILED_UNKNOWN_CONVERTER_ISSUE = "failed_unknown_converter_issue",
    FAILED_NORMAL_CLEARING = "failed_normal_clearing",
    FAILED_CONVERT_TO_TIFF_ISSUE = "failed_convert_to_tiff_issue",
    FAILED_FS_49 = "failed_fs_49"

    def __str__(self):
        return str(self.value)
