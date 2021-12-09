from bs4 import BeautifulSoup
from .shared.base import Base
from .shared.developerproduct import DeveloperProduct
import requests
import re

class Experience(Base):
    """
    Experience class
    """

    def __init__(self, UniverseId: int):
        """
        Initializes experience product class

        Attributes:
            UniverseId: The ID of the experience you are reading/changing
        """
        self.Id = UniverseId

    async def create_developer_product(self, Name: str, Description: str, Price: int) -> DeveloperProduct:
        """
        Create's a developer product in the experience specified when initiating the class.

        Attributes:
            Name: The name of the developer product
            Description: The description of the developer product
            Price: The price of the developer product
        """
        response = requests.session.post(
            "https://www.roblox.com/places/developerproducts/add",
            data = {
                "universeId": self.Id,
                "name": Name,
                "priceInRobux": Price,
                "description": Description
            },
        )

        id = re.findall(
            r"\d",
            BeautifulSoup(r.text, "html.parser").find(id="DeveloperProductStatus")
        )

        return DeveloperProduct(Data={
            "Id": id,
            "Name": Name,
            "Description": Description,
            "Price": Price,
        })