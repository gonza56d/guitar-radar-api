from datetime import datetime, timedelta
from time import time
from uuid import UUID

import bcrypt
import jwt

from app.env import Env


def hash_password(password):
    """Generate a salt and hash the password using bcrypt."""
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')


def generate_auth_token(user_id: UUID) -> str:
    jwt_token_payload = {
        'user_id': str(user_id),
        'exp': int(time()) + 3600,
        'exp_datetime_utc': (datetime.utcnow() + timedelta(minutes=3600)).isoformat()
    }
    return jwt.encode(jwt_token_payload, Env.CACHE_SESSION_SECRET_KEY, algorithm='HS256')
