# User Object

## Requirements
None

## Parameters

None

## Functions

### Constructor
The constructor sets the client object, as well as a logger for debugging and a filter for determining which URI the client should use.

### add

Parameters:
- data

Example:
```python
from icinga2 import Icinga2API

data = {
    "attrs": {
        "user_name": "Max Mustermann",
        "display_name": "MaxMann"
        "groups": ['GroupA', 'GroupB']
    }
}

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.users.add(data)
```

It returns a dictionary with the HTTP Returncode and other data that icinga2 provides.


### delete

Parameters:
- name

Example:
```python
from icinga2 import Icinga2API

name = "Max Mustermann"

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.users.delete(name)
```

It returns a dictionary with the HTTP Returncode and other data that icinga2 provides.

### list

Parameters:
- name

Example:
```python
from icinga2 import Icinga2API

name = "Max Mustermann"

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.users.list()
```
Returns a list of all hostnames

```python
api.users.list(name)
```
returns a list of all usernames that match the name

### exists

Parameters:
- name

Example:
```python
from icinga2 import Icinga2API

name = "Max Mustermann"

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.users.exists(name)
```
Returns true or false depending on the users existence

### objects

Parameters:
- attrs
- _filter
- joins

Example:
```python
from icinga2 import Icinga2API

attrs = ['__name', 'display_name', 'email']
_filter = ['__name == Max Mustermann']
joins = ['']


api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.users.objects(attrs=attrs, _filter=_filter, joins=joins)
```
Returns a list of all object, with their attributes, matching the _\_filter_, with addition of the field defined in _joins_
