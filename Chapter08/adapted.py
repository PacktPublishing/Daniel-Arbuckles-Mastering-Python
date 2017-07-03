from functools import wraps

def adapted(func):
    @wraps(func)
    def wrapper(**kwargs):
        final_args = {}

        for name, value in kwargs.items():
            adapt = func.__annotations__.get(name)
            if adapt is not None:
                final_args[name] = adapt(value)
            else:
                final_args[name] = value

        result = func(**final_args)

        adapt = func.__annotations__.get('return')
        if adapt is not None:
            return adapt(result)
        return result

    return wrapper

@adapted
def foo(a : int, b : repr) -> str:
    return a
