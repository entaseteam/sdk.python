"""Exceptions for Entase SDK"""


class BaseError(Exception):
    """Base exception for all Entase SDK errors"""
    def __init__(self, message: str, code: int = 1):
        self.message = message
        self.code = code
        super().__init__(self.message)

    def __str__(self):
        return f"{self.__class__.__name__}: [{self.code}]: {self.message}"


class APIError(BaseError):
    """Raised when API returns an error response"""
    pass


class RequestError(BaseError):
    """Raised when HTTP request fails"""
    pass


class CURLError(BaseError):
    """Raised when network request fails"""
    pass 