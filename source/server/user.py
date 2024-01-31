
class user_api:

    def __init__(self, return_string):
        self.return_string = return_string

    def get_hello_api(self):
        """
        Returns the hello API string.
        """
        return self.return_string