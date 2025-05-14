To get to data in a csv file as though it were an SQL table use:

`q`

Execute SQL-like queries on CSV and TSV files. More information: https://harelba.github.io/q.

Query a CSV file by specifying the delimiter as ',':
q [-d|--delimiter] ',' "SELECT * from path/to/file"

Query a TSV file:
q [-t|--tab-delimited] "SELECT * from path/to/file"

Query file with header row:
q [-d|--delimiter] delimiter [-H|--skip-header] "SELECT * from path/to/file"

Read data from stdin; '-' in the query represents the data from stdin:
output | q "select * from -"

Join two files (aliased as f1 and f2 in the example) on column c1, a common column:
q "SELECT * FROM path/to/file f1 JOIN path/to/other_file f2 ON (f1.c1 = f2.c1)"

Format output using an output delimiter with an output header line (Note: Command will output column names based on the input file header or the column aliases overridden in the query):
q [-D|--output-delimiter] delimiter [-O|--output-header] "SELECT column as alias from path/to/file"

## Install

$ sudo apt install python3-q-text-as-data
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
python3-q-text-as-data is already the newest version (3.1.6-3).

## Schema

<command> ::= q [ <flags> ] <sql-query>

<sql-query> ::= "SELECT <select-list> FROM <table-spec> [ WHERE <condition> ] [ GROUP BY <expr> ] [ ORDER BY <expr> ] [ LIMIT <n> ]"

<table-spec> ::=
    <filename> |
    "-" |  # stdin
    <sqlite-file>:::<table-name> |
    <cache-file>.qsql

<filename> ::= <path> [ .gz ]  # supports gzip compression

<cache-file> ::= <filename>.qsql

<sqlite-file> ::= <path>  # auto-detetected SQLite DB (1 or many tables)

<select-list> ::= * | <column-ref> [ , <column-ref> ]*

<column-ref> ::= c<N> | <header-name> | <alias>

<flags> ::= [ -H ] [ -d <delimiter> | -t | -p ] [ -C <caching-mode> ] 
            [ -e <encoding> ] [ -E <encoding> ] [ -O ] [ -b ] [ -S <save-db> ]
            ... other optional flags ...

<H> ::= --skip-header

<delimiter> ::= "," | "\t" | "|" | <any-char>

<t> ::= --tab-delimited

<p> ::= --pipe-delimited

<caching-mode> ::= none | read | readwrite

<encoding> ::= utf-8 | utf-8-sig | iso-8859-1 | ... 

<O> ::= --output-header

<b> ::= --beautify

<S> ::= --save-db-to-disk <filename>

<supported-input-types> ::=
    CSV |
    TSV |
    Custom-delimited text |
    GZipped versions |
    Stdin |
    SQLite databases (.sqlite, any extension) |
    Auto-generated .qsql cache files

<output-options> ::=
    -D <delimiter> |
    -T |
    -P |
    -W <quoting-mode> |
    -E <encoding> |
    -O |
    -b

<data-analysis> ::=
    Column type detection |
    Schema analysis (-A) |
    Encoding handling |
    Header parsing |
    Aggregation, filtering, joins

<join-support> ::=
    INNER JOIN |
    LEFT JOIN |
    ON condition |
    Table aliases supported

<subquery-support> ::=
    Subqueries in WHERE clause only

<limitations> ::=
    No CTEs |
    No FROM subqueries |
    No spaces in filenames |
    Max ~500 tables per query |
    Limited to ~10 attached SQLite DBs without memory load
```

## Examples


