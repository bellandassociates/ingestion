# -*- Coding: utf-8 -*-
"""
test/conftest.py
Configs and fixtures for pytest
"""

import io
import openpyxl as xl
import os
from pathlib import Path
import psycopg
import pytest

DB_CONN_ERR_INCORRECT_TARGET_DB = """You might be trying to run tests against a
production database. Please check the target and try again."""

@pytest.fixture(scope="session")
def prep_incoming_directory():
    """
    Ensures that the watched directory actually exists before tests run, and
    provides the path handle in an OS independent way.
    """
    path = Path("/data")
    assert path.exists(), f"{path} does not exist in the container. Please" \
        " ensure that the container is correctly configured."
    return path

@pytest.fixture(scope="session")
def purge_test_database():
    """
    Purge the ephemeral test database to make sure the database is in a blank
    slate state for the test.
    """
    db_user = os.environ["DB_USER"]
    db_password = os.environ["DB_PASS"]
    host = os.environ["HOSTNAME"]
    db_type = os.environ["DB_TYPE"]
    assert db_type.lower() == "test", DB_CONN_ERR_INCORRECT_TARGET_DB
    admin_conn = psycopg.connect(
        f"postgresql://{db_user}:{db_password}@{host}:5432/postgres",
        autocommit=True,
    )
    with admin_conn.cursor() as cursor:
        cursor.execute("""
            SELECT dbname
            FROM pg_database
            WHERE datistemplate = false
                AND dbname NOT IN ('postgres');
        """)
        dbs = [row[0] for row in cur.fetchall()]
        for db in dbs:
            cursor.execute(f"""
                SELECT pg_terminate_backend(pid)
                FROM pg_stat_activity
                WHERE datname = %s
                    AND pid <> pg_backend_pid();
            """,
            (db,)
            )
            cursor.execute(f"DROP DATABASE IF EXISTS {db}")

@pytest.fixture
def dummy_workbook():
    wb = xl.Workbook()
    wb.create_sheet("page1")
    wb.create_sheet("page2")
    contents = [
        ["row1", "val1a", "val1b"],
        ["row2", "val2a", "val2b"],
        ["row3", "val3a", "val3b"],
        ["row4", "val4a", "val4b"],
        [],
        ["col1", "col2", "col3", "col4"],
        ["val1a", "val2a", "val3a", "val4a"],
        ["val1b", "val2b", "val3b", "val4b"],
        ["val1c", "val2c", "val3c", "val4c"],
        ["val1d", "val2d", "val3d", "val4d"],
    ]
    for ws in wb:
        ws.append(contents)
    stream = io.BytesIO()
    wb.save(stream)
    stream.seek(0)
    return stream

# EOF
