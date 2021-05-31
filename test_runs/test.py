from live_coder import snoop


def my_method(a, b):
    a *= b
    c = 33
    b + c
    return a + b


@snoop
def test_my_method():
    my_method(2, 4)


test_my_method()
