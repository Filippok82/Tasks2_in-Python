# 24.В заданном списке вещественных чисел найдите разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19


from random import uniform

def real_numbers(n):
    a= [round(uniform(1,10), 2) for i in range(n)] 
    print(a)
    b = [round(x - int(x), 2) for x in a]
    print(b)
    return round(max(b) - min(b),2)


print(real_numbers(5))