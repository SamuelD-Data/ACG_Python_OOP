# importing datetime for benchmarking (e.g., datetime.now()) 
from datetime import datetime

# creating benchmark class
# using datetime to record time before func is ran and 
# the time when it is complete, then substracting to 
# calculate how long it took to finish running
def benchmark(func=None, *, file_name=None):
    def decorator_func(func):
        def wrapped_func(*args, **kwargs):
            start_time = datetime.now()
            result = func(*args, **kwargs)
            end_time = datetime.now()
            duration = round((end_time - start_time).total_seconds(), 2)

            message = f"benchmark: {func.__name__} duration: {duration}"

            if file_name:
                with open(file_name, "a") as f:
                    f.write(message + "\n")
            else:
                print(message)

            return result

        return wrapped_func

    if func:
        return decorator_func(func)
    else:
        return decorator_func

# creating log class which takes optional function (func = None...)
# and keyword argument (file_name = none)
def log(func=None, *, file_name=None):
# creating decorator which handles the function
    def decorator_func(func):

        def wrapped_func(*args, **kwargs):
            result = func(*args, **kwargs)

            message = f"running: {func.__name__} args: {args} kwargs: {kwargs}"

# creating IF statement that appends ("a" argument in open(...)) message followed
# by a line break and prints the message otherwise 
            if file_name:
                with open(file_name, "a") as f:
                    f.write(message + "\n")
            else:
                print(message)

            return result

        return wrapped_func

# if function is provided, return result of passing func to decorator_func 
# otherwise return decorator_func
    if func:
        return decorator_func(func)
    else:
        return decorator_func
