# -*- Coding: utf-8 -*-
"""
Unit test for /app/ingestion.py
"""

def test_ingestion_instantiation():
    from ingestion import IngestionEngine
    from excel import ExcelParser
    ig = IngestionEngine(ExcelParser())
    assert isinstance(ig.parser, ExcelParser)

# EOF
