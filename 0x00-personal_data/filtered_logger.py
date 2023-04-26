#!/usr/bin/env python3
""" task 0 """

import re


def filter_datum(fields, redaction, message, separator):
    """ filter_datum """
    for field in fields:
        message = re.sub(field + f".*?{separator}",
                         field + "=" + redaction, message)
    return message
