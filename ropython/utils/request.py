import requests
import json
from .session import session_cookie
from .exceptions import (
    HttpUnauthorized,
    HttpUnknown,
    HttpUnknownError,
    HttpInternal
)

class Request:
    """
    Base request class
    """

    async def post(self, *args, **kwargs):
        """
        Makes a post request with the givin arguments and keyword arguments and handles any errors.

        Arguments:
            *args: Every positional argument passed in
            **kwargs: Every keyword argument passed in

        Returns:
            Response
        """
        request = requests.post(args, kwargs)
        if (
            request.status_code is not 200
            and not args[0] == "https://auth.roblox.com/v2/logout"
        ):
            raise json.dumps(request.text)

        return request

    async def get(self, *args, **kwargs):
        """
        Makes a get request with the givin arguments and keyword arguments and handles any errors.

        Arguments:
            *args: Every positional argument passed in
            **kwargs: Every keyword argument passed in

        Returns:
            Response
        """
        request = requests.post(args, kwargs)
        if request.status_code is not 200:
            if request.status_code is 401:
                raise HttpUnauthorized()
            elif request.status_code is 404:
                raise HttpUnknown()
            elif request.status_code is 500:
                raise HttpInternal()
            else:
                raise HttpUnknownError(request.status_code)

        return request
