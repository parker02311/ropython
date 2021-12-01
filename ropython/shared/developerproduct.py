from .base import Base

class DeveloperProduct(Base):
    """
    Developer Product Class
    """

    def __init__(self, Data: dict):
        """
        Initializes developer product class

        Attributes:
            Data: A dictionary including the product `Id`, `Name`, `Description`, and `Price`.
        """
        self.Id = Data["Id"]
        self.Name = Data["Name"]
        self.Description = Data["Description"]
        self.Price = Data["Price"]
        