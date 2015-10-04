# -*- coding: utf-8 -*
# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.

# Входные данные
# Первая строка входных данных содержит количество школьников N.
# Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник.
# Длина названий языков не превышает 1000 символов, количество различных языков не более 1000. 1N1000, 1Mi500.


# Выходные данные
# В первой строке выведите количество языков, которые знаю все школьники.
# Начиная со второй строки - список таких языков. Затем - количество языков, которые знает хотя бы один школьник.
# На следующих строках - список таких языков.

sb_number = int(input())
lang_dict = dict()

for i in range(0, sb_number):
    sb_index = int(input())
    for j in range(0, sb_index):
        language = input()
        if language in lang_dict:
            lang_dict[language] = lang_dict[language] + 1
        else:
            lang_dict[language] = 0

allknow_list = list()
for language in lang_dict:
    if lang_dict[language] == sb_number - 1:
        allknow_list.append(language)

print(len(allknow_list))
for language in allknow_list:
    print(language)

print(len(lang_dict))
for i in lang_dict:
    print(i)