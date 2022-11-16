from random import randint


def get_unique_list_numbers() -> list[int]:
    sp = []
    while len(sp) < 15:
        num = randint(-10,10)
        sp.append(num if num not in sp)
    return sp


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))