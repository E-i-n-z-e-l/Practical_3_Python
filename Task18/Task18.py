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

