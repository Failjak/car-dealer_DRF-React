from apps.api.errors import BaseError


def error_response_handler_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BaseError as e:
            if hasattr(e, 'details') and hasattr(e, 'message'):
                raise BaseError(details=e.details, message=e.message)
            elif hasattr(e, 'details'):
                raise BaseError(details=e.details)
            elif hasattr(e, 'message'):
                raise BaseError(message=e.message)
    return wrapper
