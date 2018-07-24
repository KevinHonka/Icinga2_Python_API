class constants():
    username = "root"
    password = "icinga"
    url = "https://localhost:5665"

    TestHost_data = {
        "templates": ["generic-host"],
        "attrs": {
            "name": "test.localdomain",
            "address": "192.168.1.1",
            "check_command": "hostalive",
            "vars.os": "Linux"
        }
    }

    TestService_name = "TestService"

    Test_Hostgroup = {
        "name": "HostGroupA",
        "attrs": {
            "display_name": "Host Test GroupA"
        }
    }

    Test_Servicegroup = {
        "name": "ServiceGroupA",
        "attrs": {
            "display_name": "Service Test GroupA"
        }
    }

    Test_Usergroup = {
        "name": "UserGroupA",
        "attrs": {
            "display_name": "Service Test GroupA"
        }
    }

    TestService_data = {
        "templates": ["generic-service"],
        "attrs": {
            "check_command": "ping4",
            "check_interval": 10,
            "retry_interval": 30
        }
    }
