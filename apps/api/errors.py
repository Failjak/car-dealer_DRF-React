class BaseError(Exception):
    def __init__(self, *args, **kwargs):

        if len(args):
            arg = args[0]
            if isinstance(arg, str):
                self.message = arg
            elif isinstance(arg, dict):
                self.details = arg

        if 'details' in kwargs:
            self.details = kwargs.get('details')

        if 'message' in kwargs:
            self.message = kwargs.get('message')

    @property
    def formatted_message(self):
        return self.details
