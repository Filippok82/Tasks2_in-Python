# Задача 17 Сложите цифры целого числа.
n= int(input('Введите  число: '))
# a=n%10
# b=n%100//10
# print(a+b)   #Простое для двухзначного  



def sum_digits(n):
    digits = [int(d) for d in str(n)]
    return sum(digits)

print(sum_digits(n))