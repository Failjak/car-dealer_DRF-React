
class OfferError(Exception):
    def __init__(self, offer=None, message=''):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return 'Error message: ' + self.message