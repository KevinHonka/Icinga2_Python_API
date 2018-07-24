# Client object

## Requirements
- Requests
- urllib3
- logging
- json

## Parameter

URLCHOICES => a list of uris that are used to switch between the different objects that icinga2 provides

### Example

```python
"host": "/v1/objects/hosts",
.
.
.
"users": "/v1/objects/users",
```

## Functions

### Constructor
Does not take any parameters.</br>
Sets the default logger for debugging.</br>
Creates a Session object that is used as the single connection to Icinga2.</br>
Updates the Session Headers to include `'Accept': 'application/json'`</br>
Disables the urllib3 warning for self-signed certificates.


### setconfig

Parameters taken:
- username
- password
- url

Sets the baseurl as well as the username and Password needed for authentication.

### get_Data

**WARNING: This function is deprecated and will be removed in a later version**

Parameters taken:
- uri

Uses HTTP-GET to retrieve data from baseurl + uri.
Returns a dictionary that is parsed from json.

### delete_Data

Parameters taken:
- uri

Uses HTTP-DELETE to remove objects from icinga2
Returns a dictionary that is parsed from json.

### put_Data

Parameters taken:
- uri
- data

Uses HTTP-PUT to create new objects in Icinga2
Returns a dictionary that is parsed from json.

### post_Data

Parameters taken:
- uri
- data

Uses HTTP-PUT to create new objects in Icinga2
Returns a dictionary that is parsed from json.
