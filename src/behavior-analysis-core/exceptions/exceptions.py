class Error(Exception):
    """Base class for other exceptions"""
    pass


class InvalidParameters(Error):
    """Raised when the input value is invalid"""
    pass
