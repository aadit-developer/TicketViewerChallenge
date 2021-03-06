# TicketViewerChallenge

## Installation:
Install requirements.txt
```bash
pip install -r requirements.txt
```

## Libraries to be imported:
``` python
import requests
import unittest
import json
```

## Credentials:
Credentials have already been added in the ticketsViewer.py file

## Run:
``` bash
python ticketsViewer.py
```

## Modules:
1. test.py contains all the test-cases written using Unittest package that check the correctness and working\
code.
2. ticketsViewer.py contains all the operations that need to be done on the API in order to view all tickets or single ticket data with proper pagination integration.
3. test_data folder contains dummy test data which can be used to
compare the output of the test-cases and verify its working.

## Error Handling:
It handles two errors in total:
1. It checks for error or failure while calling zendesk API to fetch required data.
2. It also handles error or failure while performing pagination.

## Testing:
Four tests have been performed:\
1. whether the data at ID=1 is correct or not
2. whether the full API data is correct or not
3. paging for first page
4. paging for last page

## User Interface:
Python's CLI has been used.
