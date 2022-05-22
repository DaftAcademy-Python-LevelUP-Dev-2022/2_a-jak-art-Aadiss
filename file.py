from contextlib import redirect_stderr
from functools import wraps


def greeter(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "Aloha " + result.title()
    return wrapper


def sums_of_str_elements_are_equal(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result = result.split(" ")
        sum1 = sum([int(x) for x in result[0] if x != "-"])
        sum2 = sum([int(x) for x in result[1] if x != "-"])
        if result[0][0] == "-": sum1 *= -1
        if result[1][0] == "-": sum2 *= -1
        
        if sum1 == sum2:
            return f"{sum1} == {sum2}"
        else:
            return f"{sum1} != {sum2}"
    return wrapper


def format_output(*required_keys):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            current_dict = func(*args, **kwargs)
            formatted_args = [arg for arg in required_keys]
            result_dict = {}
            try:
                for key in formatted_args:
                    splitted = key.split("__")
                    if len(splitted) > 1:
                        temp_value = ""
                        for item in splitted:
                            temp_value += current_dict[item]
                            temp_value += " "
                        result_dict[key] = temp_value.strip()
                    else:
                        if current_dict[splitted[0]] == '':
                            result_dict[splitted[0]] = 'Empty value'
                        else:    
                            result_dict[splitted[0]] = current_dict[splitted[0]]
                return result_dict
            except KeyError:
                raise ValueError
        return wrapper
    return actual_decorator


def add_method_to_instance(klass):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            return func()
        
        setattr(klass, func.__name__, wrapper)
        return wrapper
    return actual_decorator
