from MyFunctions import title


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


def table(n):
    title('VALUE BREAKDOWN', 40)
    print(f"""{'Analyzed value:':30}{money(n):10}
{'Double price:':30}{double(n, True):10}
{'Half price:':30}{half(n, True):10}
{'40 % increase:':30}{increase(n, 40, True):10}
{'30% discount:':30}{discount(n, 30, True)}""")
