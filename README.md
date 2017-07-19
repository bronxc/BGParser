# BGParser
BGParser is a best guess parser used to parse multi-line data. The tool is useful when data is provided in key/value pairs over multiple lines and has distinguishable starts to each new record.

Example data:

```
Record: 1
Name: Alice
Age: 19

Record: 2
Name: Bob
Age: 26
```

We could use BGParser to pull the data into csv format that looks as follows:

```
1,Alice,19
2,Bob,26
```

## Usage

```
Usage: bgparser.py [options]

Options:
  -h, --help            Show help message
  -f FILE, --file=FILE  File name to parser
  -s SEP, --sep=SEP     Separator used to identify key/value pairs.
  --fields=FIELDS       Fields to be displayed after parser (comma separated)
  --new-record=NEW_RECORD
                        Regular Expression to identify the start of a new
                        record
```
