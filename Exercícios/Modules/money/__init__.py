def half(n, flag=False):
    s = n / 2
    if flag:
        return money(s)
    else:
        return s


def double(n, flag=False):
    s = n * 2
    if flag:
        return money(s)
    else:
        return s


def increase(n, i=0, flag=False):
    s = n * (1 + (i / 100))
    if flag:
        return money(s)
    else:
        return s


def discount(n, d=0, flag=False):
    s = n * (1 - (d / 100))
    if flag:
        return money(s)
    else:
        return s


def money(n):
    return f'US${n:.2f}'
