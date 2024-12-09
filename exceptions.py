"""Sendsay API exception classes"""

class SendsayAPIError(Exception):
    """Base class to represent API errors"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "%s: %s" % (self.value[0].get('id', ''), self.value[0].get('explain', ''))


class SendsayAPIErrorSessionExpired(SendsayAPIError):
    """Session Expired API Error exception class"""
    pass