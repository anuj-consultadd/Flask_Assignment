import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "mysql+pymysql://anuj:Anuj%4011234@localhost/library_db"
    )  # Ensure pymysql is used
    SQLALCHEMY_TRACK_MODIFICATIONS = False
