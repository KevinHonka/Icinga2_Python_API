class Downtime():
    """
    Class that contains all informations about downtimes and corresponding funtions
    """

    def __init__(self, config=None, client=None):
        """
        Initialize the Object with a given set of configurations.
        """

        self.client = client

        if config:
            self.config = config

    def add(self, userdata=None):
        """
        To be filled
        :rtype:
        """
        pass

    def list(self, username=None):
        """
        To be filled
        """
        pass
