# -*- Coding: utf-8 -*-
"""
test_excel.py
Unit test for app/excel.py
"""

def test_excel_parser_load_workbook():
    """
    Test ExcelParser's read method
    """
    from app.excel import ExcelParser
    assert hasattr(ExcelParser, "read")
    assert callable(ExcelParser, "read")

def test_excel_parser_parse():
    """
    Test ExcelParser's parse method
    """
    from app.excel import ExcelParser
    assert hasattr(ExcelParser, "parse")
    assert callable(ExcelParser, "parse")

def test_find_blocks():
    """
    Test ExcelParser's find_blocks method
    """
    from app.excel import ExcelParser
    assert hasattr(ExcelParser, "find_blocks")
    assert callable(ExcelParser, "find_blocks")

# EOF
