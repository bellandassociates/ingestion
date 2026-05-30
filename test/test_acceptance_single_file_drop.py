# -*- coding: utf-8 -*-
"""
test/test_acceptance_single_file_drop.py
Performs acceptance test for the case where user drops a single data file to
the watched directory.
"""

# Built-in module imports
from datetime import date

def test_single_file_dropoff_with_user_schema(
    launch_ingestion_engine,
    write_schema_to,
    write_test_file_to,
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
    workbook_file = INCOMING_PATH / "sample_data.xlsx"
    schema_file = SCHEMA_PATH / "schema.json"

    write_schema_to(
        schema_file,
        schema={
            "database": "sample_data",
            "sheets": {
                "Ships": {
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
                },
                "Legos": {
                    "tables": {
                        "lego_header": {
                            "orientation": "v",
                            "columns": {
                                "Set Types": "string",
                                "Total price": "decimal"
                            },
                        },
                        "lego": {
                            "orientation": "h",
                            "columns": {
                                "Set number": "int",
                                "Set name": "string",
                                "Price": "decimal",
                                "Pieces": "int",
                            },
                        },
                    },
                },
            },
        }
    )

    write_test_file_to(
        workbook_file,
        sheets={
            "Ships": [
                ["name", "completed", "length_m", "sunk"],
                ["Titanic", date(1912,4,2), 269.1, True],
                ["Endurance", date(1912,12,17), 44, True],
                ["Emma Maersk", date(2006,5,18), 398, False],
            ],
            "Legos": [
                ["Set Types", "Ships"],
                ["Total price", 679.99+269.99+149.99],
                [],
                ["Set number", "Set Name", "Price", "Pieces"],
                [10294, "Titanic", 679.99, 9090],
                [10335, "Endurance", 269.99, 3011],
                [40955, "Ane Maersk", 149.99, 1516],
            ]
        },
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

def test_single_file_dropoff_with_automated_schema():
    """
    Workflow:
    1. User drops a file to the watched directory.
    2. Process ingests and commits the data to database, using schema and types
       inferred from data.
    3. A detailed log file documenting the process and actual schema is
       generated for user to review.
    """
    launch_ingestion_engine()
    write_test_file_to(INCOMING_PATH)
    assert database_exists(expected_db_name)
    assert tables_exist(expected_table_names)
    for table, (expected_column_names, expected_column_types) \
            in database.items():
        assert columns_exist(table, expected_column_names)
        for column, dtype in (expected_column_names, expected_column_types):
            assert column_istype(table, column, dtype)

# EOF
