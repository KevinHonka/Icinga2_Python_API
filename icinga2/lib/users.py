import logging
from pprint import pformat


class Users():
    """
    Class that contains all informations about Users and corresponding funtions
    """

    def __init__(self, config=None, client=None):
        """
        Initialize the Object with a given set of configurations.
        """
        self.client = client
        if config:
            self.config = config

        self.log = logging.getLogger('Icinga2API.user')

        self.filter = 'users'

    def add(self, data=None):
        """
        Adding a User with a given set of Attributes and/or Templates

        :rtype:
        :param data: Provides the needed variables to create a user.
        Example:
        data = {
            "attrs": {
                "user_name": "Max Mustermann",
                "display_name": "MaxMann"
                "groups": ['GroupA', 'GroupB']
            }
        }
        """

        def validate_data(data):
            """
            Returns an empty list, if everything checks out
            """
            needed_vars=["user_name","display_name","email"]
            missing_keys = []

            for need in needed_vars:
                if not need in data:
                    missing_keys.append(need)

            return missing_keys

        if not data:
            raise ValueError("Data not set")
        else:
            ret = validate_data(data)

        if not ret is True:
            return ret

        self.log.debug("Adding user with the following data: {}".format(pformat(data)))
        return self.client.put_Data(self.client.URLCHOICES[self.filter] + "/" + data['attrs']['user_name'], data)


    def delete(self, name=None):
        """
        Delete a User based on the user_name

        :param name: Username of the User that is to be deleted
        """
        if not name:
            raise ValueError("name not set")
        else:
            self.log.debug("Deleting User with name: {}".format(name))
            self.client.delete_Data(self.client.URLCHOICES[self.filter] + "/" + name)

    def list(self, name=None):
        """
        Method to list all users or only a select one
        Returns a list of all Users

        :param name: can be used to only list one User, if not set it will retrieve all Users
        """
        if name is not None:
            user_filter = {
                "attrs": ["__name"],
                "filter": "user.__name == name",
                "filter_vars": {
                    "name": name
                }
            }
        else:
            user_filter = {
                "attrs": ["name"]
            }

        self.log.debug("Listing all Users that match: {}".format(pformat(user_filter)))
        ret = self.client.post_Data(self.client.URLCHOICES[self.filter], user_filter)

        return_list = []

        for attrs in ret['results']:
            return_list.append(attrs['name'])

        self.log.debug("Finished list of all matches: {}".format(pformat(return_list)))
        return return_list


    def exists(self, name=None):
        """
        Method to check if a single User exists

        :param name: Is needed to check if the User exists, will throw a Value Exception when not set
        """
        if name:
            result = self.list(name=name)

            if not result:
                return False
            else:
                return True
        else:
            raise ValueError("Username was not set")

    def objects(self, attrs=None, _filter=None, joins=None):
        """
        returns User objects that fit the filter and joins

        :attrs List: List of Attributes that are returned
        :_filter List: List of filters to be applied
        :joins List:
        """

        payload = {}

        if attrs:
            payload['attrs'] = attrs
        else:
            payload['attrs'] = ['__name', 'display_name', 'email', 'vars', 'groups']

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
