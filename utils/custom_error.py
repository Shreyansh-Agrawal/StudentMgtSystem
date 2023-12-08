class LoginError(Exception):
    '''
    Exception raised when login attempts exhausted
    '''
    def __init__(self, message):
        super().__init__(f"{message}")
        