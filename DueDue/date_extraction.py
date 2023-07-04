```python
import re
from dateutil.parser import parse

contract_dates = []

def is_date(string, fuzzy=False):
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False

def extract_dates(file_content):
    words = file_content.split()
    for word in words:
        if is_date(word):
            contract_dates.append(parse(word))

    return contract_dates
```