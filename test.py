from time import sleep
from random import randint

from live_coder import snoop


def my_method(a, b):
    a *= b
    c = randint(2, 5)
    b + c
    return a + b


@snoop
def test_my_method():
    my_method(2, 4)


print('test')
test_my_method()
