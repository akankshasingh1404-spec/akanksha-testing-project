"""
Reads test data from JSON files for data-driven testing.
"""
import json
import os


class DataReader:
    """Loads test data from JSON for data-driven test execution."""

    @staticmethod
    def read_json(file_path: str) -> dict:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Test data file not found: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
