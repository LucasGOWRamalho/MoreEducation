from jose import JWTError, jwt
from datetime import datetime, timedelta
from .config import settings
from .exceptions import GazeBaseException

class AuthError(GazeBaseException):
    """Authentication related errors"""

class TokenHandler:
    SECRET_KEY = settings.SECRET_KEY
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    @classmethod
    def create_access_token(cls, data: dict):
        expires_delta = timedelta(minutes=cls.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, cls.SECRET_KEY, algorithm=cls.ALGORITHM)

    @classmethod
    def verify_token(cls, token: str):
        try:
            payload = jwt.decode(token, cls.SECRET_KEY, algorithms=[cls.ALGORITHM])
            return payload
        except JWTError:
            raise AuthError("Could not validate credentials")