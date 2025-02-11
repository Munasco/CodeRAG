# config.py

from dotenv import load_dotenv
import os


# Slack and OpenAI API credent

# Load environment variables from .env file
load_dotenv()

# Access environment variables
SNOWFLAKE_ACCOUNT = os.getenv("account")
SNOWFLAKE_USER = os.getenv("user")
SNOWFLAKE_PASSWORD = os.getenv("password")
SNOWFLAKE_ROLE = os.getenv("role")
SNOWFLAKE_DATABASE = os.getenv("database")
SNOWFLAKE_SCHEMA = os.getenv("schema")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MISTRAL_API_URL = os.getenv("MISTRAL_API_URL")
