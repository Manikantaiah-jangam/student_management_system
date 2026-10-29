
import os

import mysql.connector
from dotenv import load_dotenv

# Load settings from the local .env file
load_dotenv()


def get_connection():
    """Create and return a MySQL database connection."""
    password = os.getenv("DB_PASSWORD")

    if not password:
        raise ValueError(
            "DB_PASSWORD is missing. Check your local .env file."
        )

    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=password,
        database=os.getenv("DB_NAME", "college"),
        port=int(os.getenv("DB_PORT", "3306"))
    )
