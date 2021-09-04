from threading import Thread
from time import sleep
import time

"""
########## first example #############
@function_timer_deco
def sum(a, b):
    return a + b

print('result', sum(1, 2))

########## second example #############
@function_timer_deco
def sum(a, b):
    sleep(30)
    return a + b

print('result', sum(1, 2))
"""


def function_timer_deco(fn):
    def inner(*args, **kwargs):
        TIMER_VALUE = 4
        results = []

        def get_main_fn_value():
            try:
                results.append(fn(*args, **kwargs))
            except BaseException as e:
                results.append(e)

        tr = Thread(target=get_main_fn_value, daemon=True)
        tr.start()
        tr.join(timeout=TIMER_VALUE)

        results.append(TimeoutError(
            f'Times up! Function "{fn.__name__}" did not return a result after {TIMER_VALUE} seconds'))

        result, *_ = results

        if isinstance(result, BaseException):
            raise result
        return result

    return inner
