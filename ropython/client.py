from .game import Game
from typing import Optional
import requests


class Client:
    """
    Client
    """

    def __init__(self, cookie: int = None, proxies: list = None):
        """
        Create's the client
        Attributes:
            cookie: The Roblox cookie in it's entirety
            proxies: The proxies of which to send from. This is not required.
        """
        self.proxise = proxies or {}
        self.session = requests.Session()
        self.session.cookies[".ROBLOSECURITY"] = cookie
        self.session.headers["x-csrf-token"] = get_token() or None

    def get_token(self) -> Optional[str]:
        """
        Get's a x-csrf-token from Roblox which is required for all requests.
        """
        # This doesn't acutally log you out since we aren't passing in a token
        r = self.session.post(
            "https://auth.roblox.com/v2/logout", cookies={".ROBLOSECURITY": self.cookie}
        )
        if r.headers["x-csrf-token"]:
            self.token = r.headers["x-csrf-token"]
            return r.headers["x-csrf-token"]
    
    async def get_game(self, UniverseId: int) -> Game:
        """
        Get a game object which is required to do anything with games.
        Attributes:
            UniverseId: The ID of the game to get
        """
        return Game(UniverseId)
