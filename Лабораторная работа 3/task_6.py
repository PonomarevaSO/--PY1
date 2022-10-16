list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
index_maximum = 0
max_znach = list_numbers[0]
for index, value in enumerate(list_numbers):
    if value > max_znach:
        max_znach =value
        index_maximum = index
list_numbers[index_maximum], list_numbers[-1] = list_numbers[-1], list_numbers[index_maximum]

print(list_numbers)