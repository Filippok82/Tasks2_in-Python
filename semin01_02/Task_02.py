# 2.  Найти максимальное из пяти чисел


#import sys

# num=[input('Введите пять чисел:')]  # с помощью функции max

# def number_search(num):
#     return max(num)

# print (number_search(num))



# matrix = [33,48,29,83,77]
# matrix.sort()
# print (matrix)                # с помощью сортирки от меньшего к большему (sort)  и удаления последнего числа с помощью pop 

# max = matrix.pop()
# print (max)



list = []
for i in range(5):   
  list.append(int(input('введите число ')))
max = list[i]
for i in range(5):    
    if list[i] > max:     
        max = list[i]
print(max)

