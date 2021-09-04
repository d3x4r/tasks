"""
1.) Реализуйте класс, который выводит название метода пользователю при его обращении к этому методу:
> obj = SomeClass()
> >>> obj.foo()
> foo
> >>> obj.mothefucker()
> mothefucker
> >>> obj.hop_hey_la_la_ley()
> hop_hey_la_la_ley
> >>> obj.cerber_one_love()
> cerber_one_love

example
obj = SomeClass()
obj.foo()
obj.mothefucker()
obj.hop_hey_la_la_ley()
obj.cerber_one_love()

"""

from task2 import function_timer_deco
from time import sleep


class SomeClass():
    def __getattribute__(self, name):
        attr = super().__getattribute__(name)
        if (callable(attr)):
            print(attr.__name__)
            return attr
        return attr

    def foo(self):
        pass

    def mothefucker(self):
        pass

    def hop_hey_la_la_ley(self):
        pass

    def cerber_one_love(self):
        pass


"""
2.) Реализуйте функцию factory, которая создает классы динамически
> >>> for clazz in ["OneClass", "TwoClass", "ThreeClass"]:
        factory(clazz)

"""


def factory(name, base_class_names=(), attributes={}): return type(
    name, base_class_names, attributes)

"""
3.) В классе Class появилась еще одна функция foo(self, args), И возможно появится еще 100 функций. Реализовать аналог декорирования ограничения времени выполнения с использованием метаклассов (или чего то еще :) )

example
class Class(metaclass=metaclass_with_timer):

    def bar(self):
        sleep(7)

x = Class()
x.bar()
> >>> TimeoutError: Times up! Function "bar" did not return a result after 4 seconds
"""


def metaclass_with_timer(class_name, base_class_names, attributes):
    attributes_with_timer_methods = {}

    for name, attribute in attributes.items():
        if hasattr(attribute, '__call__'):
            attributes_with_timer_methods[name] = function_timer_deco(
                attribute)
        else:
            attributes_with_timer_methods[name] = attribute

    return type(class_name, base_class_names, attributes_with_timer_methods)
