from datetime import datetime


def vote(x):
    age = datetime.now().year - x
    if age < 16:
        return f'At age {age}, you are not allowed to vote.'
    elif 16 <= age < 18 or age >= 65:
        return f'At age {age}, you can choose whether to vote or not.'
    else:
        return f'At age {age}, you are obligated to vote.'


print(vote(int(input('Birth year: '))))
