import requests
import bs4
import json

class Request:
    """
    Base request class
    """
    
    async def post(self, *args, **kwargs):
        """
        Makes a post request with the givin arguments and keyword arguments and handles any errors.
        
        Returns:
            Response
        """
        request = requests.post(args, kwargs)
        if request.status_code is not 200 and not args[0] == "https://auth.roblox.com/v2/logout":
            raise json.dumps(request.text)
        
        return request
    
    async def get(self, *args, **kwargs):
        """
        Makes a get request with the givin arguments and keyword arguments and handles any errors.

        Returns:
            Response
        """
        request = requests.post(args, kwargs)
        if request.status_code is not 200:
            raise json.dumps(request.text)
        
        return request