# 29.	Найти НОК двух чисел

m=int(input('Введите число m:'))  #Принимаем два числа и записываем их в отдельные переменные.
n=int(input('Введите число n:'))


# Способ №1

# def nok(m, n):
    
#     if m > n:  
#        number = m
#     else:                # определяем какое число больше
#        number = n
#     while(True):
#         if number % m == 0 and number % n == 0: # проверяем, делится ли без остатка число number 
#                                                      # на оба данных нам числа одновременно.
           
#            nok = number # если делится, то функция прекращает свою работу и выводит это число, которое и будет НОК.
#            break
       
#         else:
#            number += 1  # Если нет, то опять вызывается эта рекурсивная функция, в 
#                          # которой значение переменной еще раз увеличивается на величину наибольшего из данных в задаче чисел.
#                          #И так будет повторяться, пока не выполнится условие делимости без остатка на оба числа.
#     return number


# print(nok (m, n))



# Способ №2________________________________________________________________________

import math

print(math.lcm(m,n))