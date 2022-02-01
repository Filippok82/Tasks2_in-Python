# 19.	Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел
# Xn+1=(A*Xn+B)%M

# a = 2
# b = 3
# c = 10
# x = 1
# m = 10
# for i in range(c):
#     x = (a*x+b) % m
#     print(x)


import datetime


def arr_ran(n):
    return datetime.datetime.now().microsecond % 10
print(arr_ran(10))


