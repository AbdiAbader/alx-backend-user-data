#!/usr/bin/env python3
""" task 0 """

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """ filter_datum """
    for field in fields:
        message = re.sub(field + f".*?{separator}", field + "=" + redaction, message)
    return message
