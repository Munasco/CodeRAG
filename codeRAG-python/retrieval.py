# retrieval.py
from snowflake.snowpark import Session
from config import (
    SNOWFLAKE_ACCOUNT,
    SNOWFLAKE_USER,
    SNOWFLAKE_PASSWORD,
    SNOWFLAKE_WAREHOUSE,
    SNOWFLAKE_DATABASE,
    SNOWFLAKE_SCHEMA,
)


def get_snowflake_session():
    connection_parameters = {
        "account": SNOWFLAKE_ACCOUNT,
        "user": SNOWFLAKE_USER,
        "password": SNOWFLAKE_PASSWORD,
        "warehouse": SNOWFLAKE_WAREHOUSE,
        "database": SNOWFLAKE_DATABASE,
        "schema": SNOWFLAKE_SCHEMA,
    }
    return Session.builder.configs(connection_parameters).create()


def cortex_search(query_text, limit=5):
    session = get_snowflake_session()

    # Access the Cortex Search Service
    # Adjust the following lines based on your actual service name and structure
    database = session.catalog.get_database("cortex_search_db")
    schema = database.schemas["services"]
    # Replace 'error_log_search_service' with your actual Cortex Search Service name
    cortex_service = schema.cortex_search_services["error_log_search_service"]

    # Perform a search query using the Cortex Search Service
    response = cortex_service.search(
        query=query_text,
        columns=["message_text", "timestamp"],
        filter={},  # Add filter conditions if needed
        limit=limit,
    )

    session.close()
    return response
