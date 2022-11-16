from random import sample
from string import digits, ascii_letters


def get_random_password(n = 8) -> str:
    return "".join(sample(digits + ascii_letters,n))


print(get_random_password())