class InputError(Exception):
    def __init__(self, message):
        return f"Input Error. {message}"