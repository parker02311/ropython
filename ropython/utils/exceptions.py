class RoPythonError(Exception):
    pass

class HttpUnauthorized(RoPythonError):
    def __init__(self):
        super().__init__("The application is not authorized to peform that action.")

class HttpUnknown(RoPythonError):
    def __init__(self):
        super().__init__("Roblox could not find the requested action.")

class HttpInternal(RoPythonError):
    def __init__(self):
        super().__init__("Roblox reported a internal server error.")

class HttpUnknownError(RoPythonError):
    def __init__(self, status_code):
        super().__init__(f"Server got a unknown HTTP error. {status_code}")