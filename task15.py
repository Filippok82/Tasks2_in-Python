# Задача 15 Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.
a=set([3,7,9,55,77,99,12])
b=set([3,5,8,99,44,66])
print (a-b)
print(b-a) # наоборот