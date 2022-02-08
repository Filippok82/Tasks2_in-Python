# 33. Задана натуральная степень k.
#  Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x²
# a*x^k+b*x+c=0


#__________________с вычислением квадратного корня______

# import math
# from random import randint


# k = 2

# numbers = []
# for i in range(3):
#     numbers.append(randint(0, 100))
# print(numbers)

# a = numbers[0]
# b = numbers[1]
# c = numbers[2]


# with open('task33.txt', 'w') as file_data:
#     file_data.write(
#         f'{a} * x ^ {k} + {b} * x + {c} = 0 ')


# D = ((b ** 2) - 4 * a * c)  # формула дискриминанта
# print(f'дискриминант равен {D}')

# x = - b + math.sqrt(D) / (2 * a)  # Нахождение квадратного корня

# print(x)


#_________________________________________________________________

k=3
step_k=[]
def degree_selection(k):
   
    for i in range(1,k+1):
        step_k.append(i)
    return step_k
   
print(degree_selection(k))


from random import randint

numbers=[]
def select_coefficient(k):
    for i in range(0,k+1):
        numbers.append(randint(0, 100))
    return numbers
print(select_coefficient(k))



def polinom(step_k,numbers):
    return f'{numbers[0]}*x**{step_k[2]}+{numbers[1]}*x**{step_k[1]}+{numbers[2]}*x+{numbers[3]} = 0'

print(polinom(step_k, numbers))


with open('task33.txt', 'w') as file_data:
     file_data.write(polinom(step_k,numbers))


