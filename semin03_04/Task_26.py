# 26. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.

# Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


# F−n = (−1)˄n+1*Fn.
#________________________________________________________

# Фибоначчи рекурсией______________________________________


# def fibonacci(n):
#     if n in (1, 2):

#         return 1

#     return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(10))


# Фибоначчи циклом________________________________________


# fib1 = fib2 = 1


# n = int(input())


# print(fib1, fib2, end=' ')


# for i in range(2, n):

#     fib1, fib2 = fib2, fib1 + fib2

#     print(fib2, end=' ')


# lambda________________________________________________

# def fibonacci(n):


#     fib_list = [0, 1]


#     list(map(lambda _: fib_list.append(sum(fib_list[-2:])),range(2, n)))


#     return fib_list[:n]


# print(fibonacci(11))


# НЕГАФИБОНАЧЧИ-__________________

n = int(input('Введите n:'))
num1  = 1
num2 = -1
res=[]
ser=[]
res.append(num1)
res.append(num2)
for i in range(2, n+1):
    num1, num2 = num2, num1 - num2
    res.append(num2)
    ser=res[::-1]
print(ser)

num3=1
num4=1
res1=[]
res1.append(0)
res1.append(num3)
res1.append(num4)
i=0
for i in range(2,n+1):
    num3, num4 = num4, num3 + num4
    res1.append(num4)
print(res1)
res2=ser+res1
print(res2, '\n')


