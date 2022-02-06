# 28.	Найти корни квадратного уравнения Ax² + Bx + C = 0
	#Математикой
	#Используя дополнительные библиотеки*

# def quadratic_equation(a,b,c):  # Решение математикой
#     # d=b**2-4*a*c
#     x1=-(b+((b**2-4*a*c)**0.5))/2*a
#     x2=-(b-((b**2-4*a*c)**0.5))/2*a

#     return x1,x2
# print (quadratic_equation(1, -5, 6))


import math

a = int(input('введи коэфициент a:'))
b = int(input('введи коэфициент b:'))
c = int(input('введи коэфициент с:'))


def formula(a,b,c):
    D = ((b ** 2) - 4 * a * c)# формула дискриминанта
    print(f'дискриминат равен {D}')#  нахождение дискриминанта
   
    x1 =( -b - math.sqrt(D)) / (2 * a) # Нахождение квадратных корней
    x2 = (-b + math.sqrt(D)) / (2 * a) 
    
    return x1,x2

print(formula(a, b, c))
