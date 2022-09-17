def half(n):
    s = n / 2
    return s


def double(n):
    s = n * 2
    return s


def increase(n, i=0):
    s = n * (1 + (i / 100))
    return s


def discount(n, d=0):
    s = n * (1 - (d / 100))
    return s


def money(n):
    return f'US${n:.2f}'
