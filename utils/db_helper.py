"""
Database validation helper — demonstrates SQL validation layer
matching the HM Land Registry experience on resume.

This is a template using sqlite3 (no external DB needed for demo).
In production, swap to psycopg2 / pymysql / pyodbc for Postgres/MySQL/MSSQL.
"""
import sqlite3
from utils.logger import get_logger

logger = get_logger(__name__)


class DBHelper:
    """Lightweight SQL helper for data validation in tests."""

    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        logger.info(f"Connected to DB: {db_path}")

    def execute_query(self, query: str, params: tuple = ()):
        """Run a SELECT query and return all results."""
        logger.info(f"Executing query: {query}")
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def execute_update(self, query: str, params: tuple = ()):
        """Run an INSERT/UPDATE/DELETE."""
        self.cursor.execute(query, params)
        self.conn.commit()

    def validate_record_exists(self, table: str, column: str, value) -> bool:
        """Returns True if a record exists matching the column/value criteria."""
        query = f"SELECT COUNT(*) FROM {table} WHERE {column} = ?"
        result = self.execute_query(query, (value,))
        return result[0][0] > 0

    def close(self):
        self.conn.close()
        logger.info("DB connection closed")
