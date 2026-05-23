# -*- Coding: utf-8 -*-
"""
test/conftest.py
Configs and fixtures for pytest
"""

import io
import openpyxl as xl
import pytest

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
