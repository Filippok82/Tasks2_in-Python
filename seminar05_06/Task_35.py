# 35.В файле находится N натуральных чисел, записанных через пробел.
#  Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

with open('task35.txt','w') as file:
     file.write('55 56 57 58 60 61 62 63 64')

def coll_elemen(path):
    nums_list = open(path, 'r') 
    new_num=nums_list.read()+' '
    new_num = list(map(int,new_num.split()))
    nums_list.close()
    return new_num
    




def search_num(new_num):
    for i in range(len(new_num)-1):
        if new_num[i+1] - new_num[i] > 1:
            return 'не хватает {}'.format(new_num[i] + 1)


path='task35.txt'
new_num=coll_elemen(path)
print(coll_elemen(path))
print(search_num(new_num))



