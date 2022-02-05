# 29.	Найти НОК двух чисел

x=int(input('Введите число m:'))  #Принимаем два числа и записываем их в отдельные переменные.
y=int(input('Введите число n:'))




def lcm(x, y):
    
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


print( lcm(x, y))