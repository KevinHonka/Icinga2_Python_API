[7bf95750]: https://github.com/Icinga/icingaweb2/blob/master/modules/monitoring/library/Monitoring/Backend/Ido/Query/ServicestatusQuery.php "Origin of the severity calculation"

# Host Object

## Requirements
None

## Parameters

HOST_STATUS => contains a mapping of DOWN, CRITICAL, UNKNOWN to their numerical representations

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
    "name": "test.localdomain"
    "template": [ "generic-host" ],
    "attrs": {
        "name": "testserver1",
        "address": "127.0.0.1",
        "check_command": "hostalive"
    }
}

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.hosts.add(data)
```

It returns a dictionary with the HTTP Returncode and other data that icinga2 provides.


### delete

Parameters:
- name

Example:
```python
from icinga2 import Icinga2API

name = "test.localdomain"

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.hosts.delete(name)
```

It returns a dictionary with the HTTP Returncode and other data that icinga2 provides.

### list

Parameters:
- name

Example:
```python
from icinga2 import Icinga2API

name = "test.localdomain"

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.hosts.list()
```
Returns a list of all hostnames

```python
api.hosts.list(name)
```
returns a list of all hostnames that match the name

### exists

Parameters:
- name

Example:
```python
from icinga2 import Icinga2API

name = "test.localdomain"

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.hosts.exists(name)
```
Returns true or false depending on the hosts existence

### objects

Parameters:
- attrs
- _filter
- joins

Example:
```python
from icinga2 import Icinga2API

attrs = ['name', 'state', 'last_check']
_filter = ['host.name == test.localdomain', 'service.name == ping4']
joins = ['service.name']


api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.hosts.objects(attrs=attrs, _filter=_filter, joins=joins)
```
Returns a list of all object, with their attributes, matching the _\_filter_, with addition of the field defined in _joins_

### problem_count

Parameters:
- None

Example:
```python
from icinga2 import Icinga2API

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.hosts.problem_count()
```
Returns the count of all Hosts, that have a problem and are neither acknowledged nor in a downtime.

### problem_count

Parameters:
- None

Example:
```python
from icinga2 import Icinga2API

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.hosts.problem_list()
```
Returns a dictionary where the hostnames are keys and contain their severity as a value


### severity
**WARNING: Internal method, do not use**

This method is used by _problem_list_ to accurately calculate the severity. Calculation is derived from [Origin][7bf95750]

Parameters:
- attrs

Example:
```python
host_problems[host['name']] = self.host_severity(host['attrs'])
```
