# 18.	Реализовать алгоритм перемешивания списка. 

from random import *

arr=[i for i in range(10)]
print (arr)

def mixing (x):
    for i in range(len(x)-1):
        index=randint(i+1,len(x)-1)
        x[i],x[index]=x[index],x[i]
    return x
print(mixing(arr))