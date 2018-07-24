import json
import logging

import urllib3
from requests import Session


class Icinga2APIClient(object):
    """
    Main Class to implement the Icinga2 API Client
    """

    URLCHOICES = {
        "host": "/v1/objects/hosts",
        "hostgroups": "/v1/objects/hostgroups",
        "service": "/v1/objects/services",
        "servicegroups": "/v1/objects/servicegroups",
        "notification": "/v1/objects/notifications",
        "downtime": "/v1/objects/downtimes",
        "users": "/v1/objects/users",
        "usergroups": "/v1/objects/usergroups"
    }

    def __init__(self):
        """
        Initialize all needed Variables
        """

        self.log = logging.getLogger('Icinga2API.client')
        self.connection = Session()
        self.connection.headers.update({'Accept': 'application/json'})
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def setconfig(self, username=None, password=None, url=None):
        if url is not None:
            self.baseurl = url
        else:
            raise ValueError("No URL set")

        self.connection.auth = (username, password)

    def get_Data(self, url):
        """
        Get Data from icinga2
        """
        try:
            ret = self.connection.get(self.baseurl + url, verify=False)
            ret.raise_for_status()
            return json.loads(ret.text)
        except Exception as e:
            self.log.error(e)
            raise

    def delete_Data(self, url):
        """
        Delete Data from icinga2
        """

        try:
            ret = self.connection.delete(self.baseurl + url, verify=False)
            ret.raise_for_status()
            return json.loads(ret.text)
        except Exception as e:
            self.log.error(e)
            raise

    def put_Data(self, url, data):
        """
        Put Data into Icinga2 via the API

        :param url: type of uri to attach to url
        :param data: Data Dictionary that is used to add values to Icinga2
        """
        try:
            ret = self.connection.put(self.baseurl + url, data=json.dumps(data), verify=False)
            self.log.debug(ret.text)
            ret.raise_for_status()
            return json.loads(ret.text)
        except Exception as e:
            self.log.error(e)
            raise

    def post_Data(self, uri, data):
        """
        POST method
        :param uri: uri to attach to url
        :param data: Data Dictionary that is used to query the Icinga2API
        """
        try:
            ret = self.connection.post(self.baseurl + uri, headers={'X-HTTP-Method-Override': 'GET'},
                                       data=json.dumps(data), verify=False)
            ret.raise_for_status()
            return json.loads(ret.text)
        except Exception as e:
            self.log.error(e)
            raise
