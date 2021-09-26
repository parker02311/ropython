from .utils.request import Request
from .utils.session import session_cookie


class Client:
    """
    Client
    """

    def __init__(self, cookie: int = None):
        """
        Create's the client
        Attributes:
            cookie: The Roblox cookie in it's entirety
        """
        self.cookie = cookie
        session_cookie = cookie

    async def get_token(self):
        """
        Get's a x-csrf-token from Roblox which is required for all requests.
        """
        # This doesn't acutally log you out since we aren't passing in a token
        r = Request.post(
            "https://auth.roblox.com/v2/logout", cookies={".ROBLOSECURITY": self.cookie}
        )
        if r.headers["x-csrf-token"]:
            self.token = r.headers["x-csrf-token"]
            return r.headers["x-csrf-token"]

        return None
