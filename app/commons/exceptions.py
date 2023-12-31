from typing import Any, Dict, Optional

from fastapi import status, HTTPException


class DuplicatedError(HTTPException):
    def __init__(
        self, detail: Any = None, headers: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(status.HTTP_400_BAD_REQUEST, detail, headers)


class AuthError(HTTPException):
    def __init__(
        self, detail: Any = None, headers: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(status.HTTP_401_UNAUTHORIZED, detail, headers)


class NotFoundError(HTTPException):
    def __init__(
        self, detail: Any = None, headers: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(status.HTTP_404_NOT_FOUND, detail, headers=headers)


class ValidationError(HTTPException):
    def __init__(
        self, detail: Any = None, headers: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail,
            headers,
        )


class ForbiddenError(HTTPException):
    def __init__(
        self, detail: Any = None, headers: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(
            status.HTTP_403_FORBIDDEN,
            detail,
            headers,
        )


class BadRequestError(HTTPException):
    def __init__(
        self, detail: Any = None, headers: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(
            status.HTTP_400_BAD_REQUEST,
            detail,
            headers,
        )


class InternalServerError(HTTPException):
    def __init__(
        self, detail: Any = None, headers: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail,
            headers,
        )


class ServiceUnavailableError(HTTPException):
    def __init__(
        self, detail: Any = None, headers: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(
            status.HTTP_503_SERVICE_UNAVAILABLE,
            detail,
            headers,
        )
