from time import sleep

from live_coder import snoop


def my_method(a, b):
    a *= b
    c = 33
    print(44+c)
    b + c
    return a + b


@snoop
def test_my_method():
    print('test_my_method')
    sleep(10)
    my_method(2, 4)


print('test')
test_my_method()
