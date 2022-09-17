from MyFunctions import title


def factorial(n, show=False):
    """
    →Prints the factorial for the given integer number.
    :param n: Integer value for calculation.
    :param show: (optional) Input True to show calculation.
    :return: n factorial.
    """
    if show is True:
        print(f'{n} x ', end='')
    for i in range(n-1, 0, -1):
        n *= i
        if show is True:
            if i > 1:
                print(f'{i}', end=' x ')
            else:
                print(f'{i}', end=' = ')
    return n


title('FACTORIAL CREATOR', 30)
print(factorial(5, show=True))
help(factorial)
