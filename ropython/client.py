import requests

class Client:
    """
    Client
    """

    def __init__(self, apikey: str = None, proxies: list = None):
        """
        Create's the client
        
        Attributes:
            apikey: The API key that should be used for sending requests
            proxies: The proxies of which to send from. This is not required.
        """
        self.proxies = proxies or {}
        self.session = requests.Session()
        self.session.headers["x-api-key"] = apikey