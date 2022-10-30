def get_count_char(str_):
    str_=str_.lower()
    str_new = []
    count = 0
    dic={}
    for char in str_:
        if char.isalpha():
            str_new.append(char)
    for char in str_new:
        if char.isalpha():
            dic[char] = dic.setdefault(char,count) + 1
    return dic
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
dic_per = get_count_char(main_str)
def procent_count_char(dic_):
    dic_1 ={}
    length = len(main_str)
    for char in dic_:
        i = dic_.get(char)
        i_percent = i/length*100
        dic_1[i] = dic_1.setdefault(char,i_percent)
    return dic_1
print (procent_count_char(dic_per))
