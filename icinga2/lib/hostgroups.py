import logging
from pprint import pformat


class Hostgroups():
    """
    Class that contains all informations about Hostgroups and corresponding funtions
    """

    def __init__(self, config=None, client=None):
        """
        Initialize the Object with a given set of configurations.
        """
        self.client = client
        if config:
            self.config = config

        self.log = logging.getLogger('Icinga2API.hostgroups')

        self.filter = 'hostgroups'

    def add(self, data=None):
        """
        Adding a Hostgroup with a given set of Attributes and/or Templates

        :rtype:
        :param data: Provides the needed variables to create a Hostgroup.
        Example:
        data = {
            "name": "GroupA",
            "attrs": {
                "name": "GroupA",
                "groups": ["GroupB", "GroupC"]
            }
        }
        """

        def validate_data(data):
            """
            Returns an empty list, if everything checks out
            """
            needed_vars = ["name"]
            missing_keys = []

            for need in needed_vars:
                if not need in data:
                    missing_keys.append(need)

            return missing_keys

        if not data:
            raise ValueError("Data not set")
        else:
            ret = validate_data(data)

        if ret:
            return ret

        payload = {}
        payload["attrs"] = data["attrs"]

        self.log.debug("Adding {} with the following data: {}".format(self.__class__, pformat(data)))
        return self.client.put_Data(self.client.URLCHOICES[self.filter] + "/" + data['name'], payload)


    def delete(self, name=None):
        """
        Delete a Hostgroup based on the name

        :param name: Name of the Hostgroup that is to be deleted
        """
        if not name:
            raise ValueError("Username not set")
        else:
            self.log.debug("Deleting {} with name: {}".format(self.__class__, name))
            return self.client.delete_Data(self.client.URLCHOICES[self.filter] + "/" + name)

    def list(self, name=None):
        """
        Method to list all Hostgroups or only a select one

        :param name: can be used to only list one Hostgroups, if not set it will retrieve all Hostgroups
        """
        if name:
            group_filter = {
                "attrs": ["name"],
                "filter": "name == name",
                "filter_vars": {
                    "name": name
                }
            }
        else:
            group_filter = {
                "attrs": ["name"]
            }

        self.log.debug("Listing all {} that match: {}".format(self.__class__, pformat(group_filter)))
        ret = self.client.post_Data(self.client.URLCHOICES[self.filter], group_filter)

        return_list = []

        for attrs in ret['results']:
            return_list.append(attrs['name'])

        self.log.debug("Finished list of all matches: {}".format(pformat(return_list)))
        return return_list


    def exists(self, name=None):
        """
        Method to check if a single Hostgroup exists

        :param name: Is needed to check if the Hostgroup exists, will throw a Value Exception when not set
        """
        if name:
            result = self.list(name=name)

            if not result:
                return False
            else:
                return True
        else:
            raise ValueError("Name was not set")

    def objects(self, attrs=None, _filter=None, joins=None):
        """
        returns Hostgroup objects that fit the filter and joins

        :attrs List: List of Attributes that are returned
        :_filter List: List of filters to be applied
        :joins List:
        """

        payload = {}

        if attrs:
            payload['attrs'] = attrs
        else:
            payload['attrs'] = ['__name', 'display_name']

        self.log.debug("Attrs set to: {}".format(pformat(payload['attrs'])))

        if _filter:
            payload['filter'] = _filter
            self.log.debug("Filter set to: {}".format(pformat(payload['filter'])))

        if joins:
            payload['joins'] = joins
            self.log.debug("Joins set to: {}".format(pformat(payload['joins'])))

        self.log.debug("Payload: {}".format(pformat(payload)))

        result = self.client.post_Data(self.client.URLCHOICES[self.filter], payload)

        self.log.debug("Result: {}".format(result))

        return result['results']
