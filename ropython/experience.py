from bs4 import BeautifulSoup
from .shared.base import Base

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

    async def create_developer_product(self, Name: str, Description: str, Price: int):
        """
        Create's a developer product in the experience specified when initiating the class.

        Attributes:
            Name: The name of the developer product
            Description: The description of the developer product
            Price: The price of the developer product
        """
        pass