"""use this as the basis of any new decorators that need to be written"""

from functools import wraps

def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        #1. Code to execute BEFORE calling the decorated function
        #2. call the decorate function as required, returning its
        #   results if needed.
            return func(*args, **kwargs)
        #3. Code to execute INSTEAD of calling the decorated function.
    return wrapper

            
