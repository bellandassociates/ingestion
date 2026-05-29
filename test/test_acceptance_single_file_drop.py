# -*- coding: utf-8 -*-
"""
test/test_acceptance_single_file_drop.py
Performs acceptance test for the case where user drops a single data file to
the watched directory.
"""

def test_single_file_dropoff_with_user_schema():
    """
    Workflow:
    1. User creates a schema file to define the expected structure of the data.
    2. User drops a file to the watched directory.
    3. Process ingests and commits the data to database, with schema and types
       as dictated by the schema file.
    4. A detailed log file documenting the process and actual schema is
       generated for user to review.
    """

def test_single_file_dropoff_with_automated_schema():
    """
    Workflow:
    1. User drops a file to the watched directory.
    2. Process ingests and commits the data to database, using schema and types
       inferred from data.
    3. A detailed log file documenting the process and actual schema is
       generated for user to review.
    """

# EOF
