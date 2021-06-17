from live_coder import snoop


def d():
    xx = 1 + 'a'
    return xx


def c():
    return d()


def b():
    try:
        aa = c()
    except TypeError:
        aa = 3
    bb = aa + 8
    return bb


@snoop
def a():
    b = '''

    a
    test

    '''
    print(b())


a()
