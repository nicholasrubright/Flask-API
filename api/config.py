import os
from dotenv import load_dotenv
from src.utils import get_connection_str

load_dotenv()

class Config:
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_USERNAME = os.getenv("POSTGRES_USERNAME")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

    if POSTGRES_HOST != None and POSTGRES_DB != None and POSTGRES_USERNAME != None and POSTGRES_PASSWORD != None:
        SQLALCHEMY_DATABASE_URI = get_connection_str(POSTGRES_HOST, POSTGRES_DB, POSTGRES_USERNAME, POSTGRES_PASSWORD)
    else:
        SQLALCHEMY_DATABASE_URI = ""