from . import client
class Notification():
    """
    Class that contains all informations about Services and corresponding funtions
    """

    def __init__(self, config=None, client=None):
        """
        Initialize the Object with a given set of configurations.
        """
        if config:
            self.config = config

    def enable_for_host(self, arg):
        """
        To be filled
        """
        pass

    def disable_for_host(self, arg):
        """
        To be filled
        """
        pass

    def enable_for_service(self, arg):
        """
        To be filled
        """
        pass

    def disable_for_service(self, arg):
        """
        To be filled
        """
        pass

    def enable_for_hostgroup(self, arg):
        """
        To be filled
        """
        pass

    def disable_for_hostgroup(self, arg):
        """
        To be filled
        """
        pass

    def list(self, servicename=None):
        """
        To be filled
        """
        pass
