# -*- coding: utf-8 -*-
"""
test/test_acceptance_single_file_drop.py
Performs acceptance test for the case where user drops a single data file to
the watched directory.
"""

# Built-in module imports
from datetime import date

def test_single_csv_file_dropoff_with_user_schema(
    launch_ingestion_engine,
    write_schema_to,
    write_test_csv_file_to,
    database_exists,
    tables_exist,
    db,
    INCOMING_PATH,
    SCHEMA_PATH
):
    """
    Workflow:
    1. User creates a schema file to define the expected structure of the data.
    2. User drops a file to the watched directory.
    3. Process ingests and commits the data to database, with schema and types
       as dictated by the schema file.
    4. A detailed log file documenting the process and actual schema is
       generated for user to review.
    """
    launch_ingestion_engine()
    csv_file = INCOMING_PATH / "sample_data.csv"
    schema_file = SCHEMA_PATH / "schema.json"

    write_schema_to(
        schema_file,
        schema={
            "database": "sample_data",
            "tables": {
                "ships": {
                    "orientation": "h",
                    "columns": {
                        "name": "string",
                        "completed": "date",
                        "length_m": "float",
                        "sunk": "boolean",
                    },
                },
            },
        }
    )

    write_test_csv_file_to(
        csv_file,
        data=[
            ["name", "completed", "length_m", "sunk"],
            ["Titanic", date(1912,4,2), 269.1, True],
            ["Endurance", date(1912,12,17), 44, True],
            ["Emma Maersk", date(2006,5,18), 398, False],
        ],
    )
    assert database_exists("sample_data")
    assert tables_exist(["ships"])
    assert db.columns_match(
        table="ships",
        expected_columns=["id", "name", "completed", "length_m", "sunk"],
        expected_types=["int", "string", "date", "float", "boolean"],
    )

def test_single_csv_file_dropoff_with_automated_schema(
    launch_ingestion_engine,
    write_test_csv_file_to,
    database_exists,
    tables_exist,
    db,
    INCOMING_PATH
):
    """
    Workflow:
    1. User drops a file to the watched directory.
    2. Process ingests and commits the data to database, using schema and types
       inferred from data.
    3. A detailed log file documenting the process and actual schema is
       generated for user to review.
    """
    launch_ingestion_engine()
    csv_file = INCOMING_PATH / "sample_data.csv"

    write_test_csv_file_to(
        csv_file,
        data=[
            ["name", "completed", "length_m", "sunk"],
            ["Titanic", date(1912,4,2), 269.1, True],
            ["Endurance", date(1912,12,17), 44, True],
            ["Emma Maersk", date(2006,5,18), 398, False],
        ],
    )
    assert database_exists("sample_data")
    assert tables_exist(["ships", "lego_header", "lego"])
    assert db.columns_match(
        table="ships",
        expected_columns=["id", "name", "completed", "length_m", "sunk"],
        expected_types=["int", "string", "date", "float", "boolean"],
    )
    assert db.columns_match(
        table="lego_header",
        expected_columns=["set_types", "total_price"],
        expected_types=["string", "decimal"],
    )
    assert db.columns_match(
        table="lego",
        expected_columns=["set_number", "set_name", "price", "pieces"],
        expected_types=["int", "string", "decimal", "int"],
    )

# EOF
