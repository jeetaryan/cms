# config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    # Secret key for session management and security
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable to suppress warning and improve performance

