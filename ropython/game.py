from .utils.request import Request


class DeveloperProducts:
    """
    Developer product class
    """

    def __init__(self, UniverseId: int):
        """
        Initializes developer product class

        Attributes:
            UniverseId: The ID of the game you are reading/changing
        """
        self.UniverseId = UniverseId

    async def Create(self, Name: str, Description: str, Price: int):
        """
        Create's a developer product in the game specified when initiating the class.

        Attributes:
            Name: The name of the developer product
            Description: The description of the developer product
            Price: The price of the developer product
        """
        pass
