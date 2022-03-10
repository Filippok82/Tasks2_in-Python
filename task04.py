# Задача 4 Напишите программу для слияния нескольких словарей в один.

# a={1:'dog',2:'cat',3:'mouse', 4:'pig'}
# b={5:'fox',6:'fish'}
# c={}
# c={**a,**b}
# print(c)

#________________________________________

a = {1:'peanut', 2:'butter', 3:'jelly', 4:'time'}
b = {5:'fish', 6:'chips'}        

c=dict()
for i in (a,b):
    c.update(i)
print(c)
