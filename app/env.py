from os import getenv

from dotenv import load_dotenv


load_dotenv()


class Env:
    """Environment variables loaded on api startup."""
    SQL_IMPL = getenv('SQL_IMPL')
    SQL_SERVICE = getenv('SQL_SERVICE')
    SQL_USER = getenv('POSTGRES_USER')
    SQL_PASSWORD = getenv('POSTGRES_PASSWORD')
    SQL_DB = getenv('POSTGRES_DB')

    DOCUMENT_IMPL = getenv('DOCUMENT_IMPL')
    DOCUMENT_DB = getenv('DOCUMENT_DB')
    DOCUMENT_HOST = getenv('DOCUMENT_HOST')
    DOCUMENT_PORT = int(getenv('DOCUMENT_PORT'))

    CACHE_HOST = getenv('CACHE_HOST')
    CACHE_PORT = getenv('CACHE_PORT')
    CACHE_SESSION_SECRET_KEY = getenv('CACHE_SESSION_SECRET_KEY')
    CACHE_TOKEN_EXPIRATION_MINUTES = int(getenv('CACHE_TOKEN_EXPIRATION_MINUTES'))
