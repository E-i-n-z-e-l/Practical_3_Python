# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X. 
# Попробуйте использовать метод count(), а также решите задачу с помощью своего алгоритма (без count). 
# Замерьте время работы двух алгоритмов и сравните, подумайте, почему оно отличается.

# Пример:
#  1 2 3 4 5
#      3
#     -> 1

new_list = []
elements_list = int(input('Введите сколько будет элементов в списке '))
element_count = 1
for _ in range(elements_list):                                                
    new_list.append(int(input(f'Введите элемент {element_count}: ')))
    element_count = element_count + 1
print(new_list)

import time

need_element = int(input('Введите искомое число в списке: '))
count = 0
start = time.perf_counter()
for i in range(elements_list):
    if new_list[i] == need_element:
        count = count + 1
end = time.perf_counter()
first_time = end - start
print(f'Элементов со значением {need_element} в списке встречается {count} раз')




array_string = ''
for i in new_list:
    array_string = array_string + str(i)
print(array_string)
new_need_element = input('Введите искомое число в списке: ')
start = time.perf_counter()
first_count = array_string.count(new_need_element)
end = time.perf_counter()
second_time = end - start
print(f'Элементов со значением {need_element} в списке встречается {first_count} раз')

print(second_time / first_time)


# Метод "count" строчный, скорее всего из-за этого он не быстрый.




# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример:

# 1 2 3 4 5
#     6
#  -> 5



new_list = []
elements_list = int(input('Введите сколько будет элементов в списке '))
element_count = 1
for _ in range(elements_list):                                                
    new_list.append(int(input(f'Введите элемент {element_count}: ')))
    element_count = element_count + 1
print(new_list)

need_number = int(input('Какое число вы ищите? '))
while need_number < 0:
    print('Введите положительное число, так как список состоит из положительных чисел ')
    need_number = int(input('Какое число вы ищите? '))

for i in range(elements_list):
    if new_list[i] == need_number:
        print(f'Число {need_number} есть в списке ')

max_element = 0
for i in range(elements_list) :
    if max_element < new_list[i]:
        max_element = new_list[i]

if need_number > max_element:
    print(f'Самое близкое число к искомому числу "{need_number}" это число "{max_element}"')

min_elements = 0
for i in range(elements_list):
    if min_elements > new_list[i]:
        min_elements = new_list[i]

if need_number < min_elements:
    print(f'Самое близкое число к искомому числу "{need_number}" это число "{min_elements}"')


for i in range(elements_list):
    if need_number < new_list[i]:
    
        if new_list[i] - need_number > new_list[i - 1] - need_number:
            print(f'Самое близкое число к искомому числу {need_number} это число {new_list[i - 1]}')
            break
        else:
            print(f'Самое близкое число к искомому числу {need_number} это число {new_list[i]}')
            break


# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков. 
# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Пример:
# ноутбук - 12
import re
word = input('Введите слово ')

dct = {'[AEIOULNSTR]' : '1', '[DG]' : '2', '[BCMP]' : '3', '[FHVWY]' : '4', '[K]' : '5', '[JX]' : '8', '[QZ]' : '10', '[АВЕИНОРСТ]' : '1', '[ДКЛМПУ]' : '2', '[БГЁЬЯ]' : '3', '[ЙЫ]' : '4', '[ЖЗХЦЧ]' : '5', '[ШЭЮ]' : '8', '[ФЩЪ]' : '10'}

for i in dct:
    word = re.sub(i, dct[i], word)
print(sum(map(int, word)))