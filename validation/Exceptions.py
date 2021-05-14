
class BioTooLong(Exception):
    """Exception raised for errors in the input salary.
       Attributes:
           length -- length of the bio
           message -- explanation of the error
       """

    def __init__(self, length, max_length, message="Bio is too long"):
        self.length = length
        self.message = message
        self.max_length = max_length
        super().__init__(self.message)

    def __len__(self):
        return self.length

class NoInput(Exception):
    """Exception raised for a missing input value.
       Attributes:
           suggested_default -- suggested default for the missing input
           message -- explanation of the error
       """
    def __init__(self, suggested_default, message="An input is missing"):
        self.suggested_default = suggested_default
        self.message = message
        super().__init__(self.message)