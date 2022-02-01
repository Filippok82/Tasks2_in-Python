# 16.	Задать список из n чисел последовательности (1+〖1/n)〗^n и вывести на экран их сумму

from random import randint
n = randint(3, 6)
print(f'n={n}')


def sequence_numbers(n):      
        b=0
        for x in range(1,n+1):
            a = (1+(1/x)) ** x 
            print(a)
            b+=a  
        return f'сумма: {b}'
      
print(sequence_numbers(n))


