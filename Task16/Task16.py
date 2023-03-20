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