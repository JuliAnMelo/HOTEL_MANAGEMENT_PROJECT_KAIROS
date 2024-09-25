class IntInputError(Exception):
    def __init__(self, message):
        super().__init__(message)
        #this handles the menus' unexistent options  