import bs4
import requests
import re

class Client:
    """
    Client
    """
    def __init__(self, cookie=None):
        """
        Create's the client
        :param cookie: A full Roblox cookie to login with
        """
        self.cookie = cookie

    async def get_token(self):
        """
        Get's a x-csrf-token from Roblox which is required for all requests.
        """
        # This doesn't acutally log you out since we aren't passing in a token
        request = requests.post("https://auth.roblox.com/v2/logout", cookies={".ROBLOSECURITY": self.cookie})
        if request.headers["x-csrf-token"]:
            self.token = request.headers["x-csrf-token"]
            return request.headers["x-csrf-token"]
        
        return None
    
    async def create_product(self, gameId: int, name: str, description: str, price: int):
        """
        Creates a developer product
        :param gameId: the ID of the game you are creating the product for
        :param name: The name of the product
        :param description: The description of the product
        :param price: The price of the product
        """
        if self.token == None:
            await self.get_token()
        
        request = requests.post(
            "https://www.roblox.com/places/developerproducts/add",
            data={
                "universeId": gameId,
                "name": name,
                "description": descrpition,
                "priceInRobux": price,
            },
            cookies={".ROBLOSECURITY": self.cookie},
            headers={"x-csrf-token": self.token},
        )
        if request.status_code == 200:
            return re.find(
                r"\d",
                bs4.BeautifulSoup(request.text, "html.parser").find(id="DeveloperProductStatus")
            )

        return None