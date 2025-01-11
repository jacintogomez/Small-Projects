class Person:

    def __init__(self):
        self.name='Jacinto'

    def printname(self):
        print(f'Hi, my name is {self.name}')


def with_base(baseclass):
    def decorator(func):
        def wrapper(*args,**kwargs):
            instance=baseclass()
            return func(instance,*args,**kwargs)
        return wrapper
    return decorator

@with_base(Person)
def who_am_i(instance):
    instance.printname()

who_am_i()