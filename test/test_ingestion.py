# -*- Coding: utf-8 -*-
"""
Unit test for /app/ingestion.py
"""

def test_ingestion_instantiation():
    from app.ingestion import IngestionEngine
    from app.excel import ExcelParser
    ig = IngestionEngine(ExcelParser())
    assert isinstance(ig.parser, ExcelParser)

# EOF
