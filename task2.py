from threading import Thread
from time import sleep

"""
########## first example #############
@function_timer_deco(5)
def sum(a, b):
    return a + b

print('result', sum(1, 2))

########## second example #############
@function_timer_deco(5)
def sum(a, b):
    sleep(30)
    return a + b

print('result', sum(1, 2))
"""


def start_error_timer(seconds_count, result, fn_name):
    sleep(seconds_count)
    result['error'] = TimeoutError(
        'Times up! Function "{}" did not return a result after {} seconds'.format(fn_name, seconds_count))


def get_main_fn_value(fn, result):
    def inner(*args, **kwargs):
        try:
            result['value'] = fn(*args, **kwargs)
        except Exception as e:
            result['error'] = e
    return inner


def function_timer_deco(seconds_count):
    def wrapper(fn):
        def inner(*args, **kwargs):
            result = {'value': None,
                      'error': None}
            timer_thread = Thread(target=start_error_timer, args=(
                seconds_count, result, fn.__name__), daemon=True)
            main_fn_thread = Thread(target=get_main_fn_value(fn, result), args=args,
                                    kwargs=kwargs, daemon=True)

            timer_thread.start()
            main_fn_thread.start()

            while True:
                value = result['value']
                error = result['error']
                if error:
                    raise error
                elif value:
                    return result['value']

        return inner
    return wrapper
