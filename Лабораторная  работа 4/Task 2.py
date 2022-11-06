
def get_count_char(str_):
    str_ = str_.lower()
    str_new ="".join(char for char in str_ if char.isalpha())
    count = 0
    dic = {}
    for char in str_new:
            dic[char] = dic.setdefault(char, count) + 1
    return dic

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))

dic_checking = get_count_char(main_str)

def procent_count(str_):
    dic_1 = {}
    str_ = str_.lower()
    str_new = "".join(char for char in str_ if char.isalpha())
    len_ = len(str_new)
    for char in dic_checking:
        i = dic_checking.get(char)
        i_percent = round(i/len_*100,2)
        dic_1[char] = dic_1.setdefault(char, i_percent)
    return dic_1


print(procent_count(main_str))