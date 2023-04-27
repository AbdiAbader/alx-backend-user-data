#!/usr/bin/env python3
""" task 0 - filter_datum
filter_datum should return the log message obfuscated:
Arguments:
    fields: a list of strings representing all fields to obfuscate"""

import re
from typing import List
import logging


PII_FIELDS = ('name', 'email', 'password', 'ssn', 'phone')


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ filter_datum """
    for field in fields:
        message = re.sub(field + f".*?{separator}",
                         field + "=" + redaction + separator, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """constructor"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format method"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger():
    "get logger"
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)

    return logger
