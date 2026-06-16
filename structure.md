ingestion/
│
├── app/
│   ├── \_\_init\_\_.py
│   ├── ingestion/
│   │   ├── \_\_init\_\_.py
│   │   └── observer.py
│   │
│   ├── parsers/
│   │   ├── \_\_init\_\_.py
│   │   ├── config\_parser.py
│   │   ├── base\_parser.py
│   │   ├── csv\_parser.py
│   │   └── xlsx\_parser.py
│   │
│   ├── transformers/
│   │   ├── \_\_init\_\_.py
│   │   └── schema\_builder.py
│   │
│   ├── db/
│   │   ├── \_\_init\_\_.py
│   │   ├── connection.py
│   │   ├── schema.py
│   │   └── writer.py
│   │
│   ├── services/
│   │   ├── \_\_init\_\_.py
│   │   ├── ingestion.py
│   │   └── pipeline\_orchestrator.py
│   │
│   ├── logging/
│   │   └── \_\_init\_\_.py
│   │
│   ├── errors/
│   │   ├── \_\_init\_\_.py
│   │   └── exceptions.py
│   └── main.py
│ 
├── tests/
│   ├── conftest.py
│   ├── test\_acceptance\_single\_xlsx\_file\_drop.py
│   ├── test\_acceptance\_single\_csv\_files\_drop.py
│   └── teststrategy.md
