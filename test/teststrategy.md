# Test strategy

## Does my code work?
Tests to write:
- Acceptance tests: Dropping one or more files off to the designated folder and
  triggers the data parsing process
- When data is a single document or data file, the contents are correctly
  parsed into data tables
- When data is many files and folders, the directory tree as well as the
  contents of each data file are correctly parsed into data tables
- When data is one or more .zip files, the .zip files are replaced with the
  extracted contents, and then the contents are parsed as above
- Acceptance tests: Automatic data schema and attribute datatype inference to
  correctly parse the data
- Acceptance tests: User-supplied data schema and attribute datatype to
  correctly parse the data
- Acceptance tests: Database is initialized with correct schema and data is
  copied over to the database
- Unit tests: Happy path
  - on launch, a persistent process is launched with a connection handle to the
    database
  - persistent process awaits for event triggers
  - when files are dropped off, an event trigger is generated
  - when event trigger is generated, the data parsing process is triggered
  - data parsing process checks if the file is a .zip file, and if so, extracts
    the contents and replaces the .zip file with the extracted contents
  - data parsing process notes directory structure to see nontrivial relations
    between files
  - data parsing process reads the filetype and correctly triggers the correct
    file read function
  - data parsing process checks for user-supplied schema
  - file read function reads ALL contents of the files and turns the contents
    into any number of tables as approrpiate, using either user-supplied schema
    or a heuristic engine to guess the schema and datatypes of the file
    contents.
  - data parsing process initializes the database with correct schema
  - data parsing process copies over the data to the database
  - data parsing process triggers logging functions at every step of the
    process for data provenance
- Unit tests: Edge cases
  - Empty files
  - files with only whitespace
  - files with only delimiters
  - files with only headers and no data
  - files with only data and no headers
  - files with missing values
  - files with extra values
  - files with inconsistent number of values across rows
  - files with non-standard delimiters
  - files with non-standard encodings
  - files with non-standard table structures
  - files with non-standard data types
  - irrelevant files in the same directory as the data files
  - files with no headers

## Is the code secure?
Tests to write:
- Security tests: When reading file/files, attempts at code injection or
  other malicious behaviors are correctly handled
- Security tests: When using user-supplied data schema, attempts at code
  injection and other malicious behaviors are correctly handled
- Security tests: Connection to the database is secure and does not allow
  unauthorized access, nor does it happen with inappropriate access rights
- Security tests: Any attempts at SQL injection and other malicious payloads
  are scanned and stripped before being sent to the database
