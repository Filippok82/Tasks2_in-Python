# Задача 13 При заданном целом числе n посчитайте n + nn + nnn.

# n=int(input('Введите n: '))

# print(n+n**2+n**3)


def solve(n):
    n1 = n
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    print(n1 + n2 + n3)

solve(2)