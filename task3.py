from functools import wraps

""" example
@UpdateResult('!')
def sum(a, b, c):
    return a + b + c
print(sum(1, 2 ,3))
"""

class UpdateResult:
    def __init__(self, dec_arg):
        self.dec_arg = dec_arg

    def __call__(self, fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            resulf_fn = fn(*args, **kwargs)
            return f'{resulf_fn}{self.dec_arg}'
        return wrapper
