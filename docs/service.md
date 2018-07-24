[7bf95750]: https://github.com/Icinga/icingaweb2/blob/master/modules/monitoring/library/Monitoring/Backend/Ido/Query/ServicestatusQuery.php "Origin of the severity calculation"

# Service Object

## Requirements
None

## Parameters

SERVICE_STATUS => contains a mapping of OK, WARNING, CRITICAL, UNKNOWN to their numerical representations

## Functions

### Constructor
The constructor sets the client object, as well as a logger for debugging and a filter for determining which URI the client should use.

### add

Parameters:
- data
- servicename
- hostname

Example:
```python
from icinga2 import Icinga2API

hostname = "test.localdomain"

servicename = "pingv4"

data = {
    "templates": [ "generic-service" ],
    "attrs": {
        "check_command": "ping4",
        "check_interval": 10,
        "retry_interval": 30
    }
}

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.services.add(servicename=servicename, hostname=hostname, data)
```

It returns a dictionary with the HTTP Returncode and other data that icinga2 provides.


### delete

Parameters:
- name

Example:
```python
from icinga2 import Icinga2API

hostname = "test.localdomain"

servicename = "pingv4"

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.services.delete(hostname, servicename)
```

It returns a dictionary with the HTTP Returncode and other data that icinga2 provides.

### list

Parameters:
- name

Example:
```python
from icinga2 import Icinga2API

hostname = "test.localdomain"
servicename = "pingv4"

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.services.list()
```
Returns a list of all services

```python
api.services.list(servicename=servicename)
```
Returns a dictionary of with a list of all services by that name, key is their hostname

```python
api.services.list(hostname=hostname)
```
returns a list of all services for this hostname

### exists

Parameters:
- name

Example:
```python
from icinga2 import Icinga2API

name = "test.localdomain"

servicename = "pingv4"

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.services.exists(servicename=servicename)
```
Returns true or false depending on the service existing

```python
api.hosts.exists(hostname=hostname, servicename=servicename)
```
Returns true or false depending on the service existing for that host

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
joins = ['host.name']


api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.services.objects(attrs=attrs, _filter=_filter, joins=joins)
```
Returns a list of all object, with their attributes, matching the _\_filter_, with addition of the field defined in _joins_

### unhandled_list

Parameters:
- None

Example:
```python
from icinga2 import Icinga2API

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.services.unhandled_list()
```
Returns a list of all unhandled service problems

### problem_count

Parameters:
- None

Example:
```python
from icinga2 import Icinga2API

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.services.problem_count()
```
Returns the count of all services, that have a problem and are neither acknowledged nor in a downtime.

### problem_handled_count

Parameters:
- None

Example:
```python
from icinga2 import Icinga2API

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.services.problem_count()
```
Returns the count of all services, that have a problem and are either acknowledged nor in a downtime.

### warning_count

Parameters:
- None

Example:
```python
from icinga2 import Icinga2API

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.services.warning_count()
```
Returns the count of all services, that are in status warning

### warning_handled_count

Parameters:
- None

Example:
```python
from icinga2 import Icinga2API

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.services.warning_handled_count()
```
Returns the count of all services, that are in state warning and either acknowledged or in a downtime

### critical_count

Parameters:
- None

Example:
```python
from icinga2 import Icinga2API

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.services.critical_count()
```
Returns the count of all services, that are in status critical

### critical_handled_count

Parameters:
- None

Example:
```python
from icinga2 import Icinga2API

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.services.critical_handled_count()
```
Returns the count of all services, that are in state critical and either acknowledged or in a downtime

### unknown_count

Parameters:
- None

Example:
```python
from icinga2 import Icinga2API

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.services.unknown_count()
```
Returns the count of all services, that are in state unknown

### unknown_handled_count

Parameters:
- None

Example:
```python
from icinga2 import Icinga2API

api = Icinga2API(username="root", password="icinga2", url="https://localhost:5665")
api.services.unknown_handled_count()
```
Returns the count of all services, that are in state unknown and either acknowledged or in a downtime
