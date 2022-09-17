def scores(*n, sit=False):
    """
    → Function for analyzing scores and averages of a student.
    :param n: One or more of a student's scores.
    :param sit: (optional) Show if the student has generally GOOD, AVERAGE or BAD scores.
    :return: A dictionary with various informations pertaining the presented scores.
    """
    avg = sum(n) / len(n)
    dc = {'total': len(n), 'highest': (max(n)), 'lowest': min(n), 'average': f'{avg:.1f}'}
    if sit is True:
        if avg < 5:
            dc['situation'] = 'BAD'
        elif 5 <= avg < 7:
            dc['situation'] = 'AVERAGE'
        else:
            dc['situation'] = 'GOOD'
    return dc


resp = scores(3, 6, 7, 9, sit=True)
print(resp)
help(scores)
