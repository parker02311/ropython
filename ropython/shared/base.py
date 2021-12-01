class Base:
    """
    This defines the base class that everything inherits except the client.
    """

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} id={self.Id}>"
    
    def __int__(self) -> int:
        return self.Id