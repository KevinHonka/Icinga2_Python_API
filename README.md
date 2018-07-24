[![Build Status](https://travis-ci.org/KevinHonka/Icinga2_Python_API.svg?branch=master)](https://travis-ci.org/KevinHonka/Icinga2_Python_API) [![PyPI version](https://badge.fury.io/py/icinga2.svg)](https://badge.fury.io/py/icinga2)

[Sonarcloud](https://sonarcloud.io/dashboard?id=Icinga2API)

# Icinga2_Python_API

An enhanced Python API  to communicate with Icinga2

To use it simply import the package like this:

```python
import icinga2_api

icinga2api = icinga2_api.Icinga2API(username = "example", password = "examplepw", url = "http://exampleicinga.de", debug = False)
```

These parameter do the following:
- username of the Icinga2 API-User to access the API
- password the password of the Icinga2 API-User to access the API
- url to Icinga2, do not add `/v1/objects/host` or similar, the API will do it for you.
- debug is either True or False, this determines if the debug output via the logger is enabled and is only here for development use.

To see which functions are supported and how they work, head to here:
[documentation](docs/index.md)
