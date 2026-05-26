# Data ingestion application

This repository contains the code to run a data ingestion engine.

## Workflow

Entrypoint `ingestion/app.py` launches an event loop that waits for a trigger to start `IngestionEngine`.
Depending on the trigger type, appropriate dependency injection to `IngestionEngine` instance helps to
parse different data input.

`IngestionEngine`'s main function is to read, clean up, and commit incoming files to a database.
Depending on the type of input, it can work in one of three modalities:

1. Single file read - a single file is given, and `IngestionEngine` extracts data from the file and commits
to the databse.
2. Multiple file read - a collection of files is given, and `IngestionEngine` parses the organizational
structures of the files and folders, extracts data from each files, and commit the data to the database with
appropriate relations between the files.
3. zip file read - a collection of files, compressed in a `.zip` file, is extracted and parsed as outlined in 2.

When `IngestionEngine` parses the files, it can either guess the schema, or use a user-supplied schema. The user
supplied schema can be supplied either with a `schema.conf` file along with the data files or with a web UI dialog.

Once all the data files are ingested, a log file is created. The log file contains a detailed manifest of the data,
formats applied to the data, and any warnings or issues raised.
