from live_coder import snoop


def d():
    xx = 1 + 'a'
    return xx


def c():
    return d()


def b():
    print('1\n1')
    try:
        print(2)
        aa = c()
    except TypeError:
        aa = 3
    bb = aa + 8
    return bb


def e():
    return 3


@snoop
def a():
    aa = e()
    bb = '''

    a
    test

    '''
    print(b())


a()
