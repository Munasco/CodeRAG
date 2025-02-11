# mock_ingest.py
import os
import snowflake.connector
from config import (
    SNOWFLAKE_USER,
    SNOWFLAKE_PASSWORD,
    SNOWFLAKE_ACCOUNT,
    SNOWFLAKE_WAREHOUSE,
    SNOWFLAKE_DATABASE,
    SNOWFLAKE_SCHEMA,
)
import logging

logging.basicConfig(level=logging.INFO)


def get_snowflake_connection():
    return snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA,
    )


def create_table_if_not_exists():
    conn = get_snowflake_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS slack_error_logs (
            id NUMBER AUTOINCREMENT,
            timestamp STRING,
            message_text STRING
        )
    """
    )
    conn.commit()
    cursor.close()
    conn.close()


def ingest_errors_from_file(file_path="mock_slack.txt"):
    create_table_if_not_exists()
    if not os.path.exists(file_path):
        logging.error(f"File {file_path} not found.")
        return

    conn = get_snowflake_connection()
    cursor = conn.cursor()

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:  # Skip empty lines
                # A very basic parsing of the log line; adjust as needed.
                # Assume format: [timestamp] LEVEL: message
                try:
                    parts = line.split("] ", 1)
                    timestamp = parts[0].lstrip("[")
                    message_text = parts[1] if len(parts) > 1 else line
                    cursor.execute(
                        """
                        INSERT INTO slack_error_logs (timestamp, message_text)
                        VALUES (%s, %s)
                    """,
                        (timestamp, message_text),
                    )
                except Exception as e:
                    logging.error(f"Error parsing line: {line} | {e}")
    conn.commit()
    cursor.close()
    conn.close()
    logging.info("Ingestion complete.")


if __name__ == "__main__":
    ingest_errors_from_file()
