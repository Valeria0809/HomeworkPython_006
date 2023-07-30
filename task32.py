# Задача 32. Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

list_1 = [random.randint(-50, 50) for i in range(random.randint(10,20))]
print(*list_1)
maxi=int(input("Введите максимальное значение: "))
mini=int(input("Введите минимальное значение: "))
list_2 = []

if maxi>=mini:
   for i in range(len(list_1)):
      if maxi >= list_1[i] and mini <= list_1[i]:
          list_2.append(i)
   print("Кол-во:",len(list_2))
   print("Индексы:",list_2)