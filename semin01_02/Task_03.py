# 3.	Вывести на экран числа от -N до N

# n = int(input('Введите число n: '))
# def elemets(n):
#     for i in range(-n, n+1):
#         print(f'{i}')
#     return i
# print(elemets(n))

n = int(input('Введите число n: '))
def elements(n):
    a = [i for i in range(-n, n + 1)]
    return a
print(elements(n))