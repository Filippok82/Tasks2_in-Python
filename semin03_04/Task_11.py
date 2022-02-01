#11.	Для натурального N создать список : 1, ,-3, 9, -27, 81 и т.д.

n=int(input(('введите число n: ')))
def create_set(n):
    arr=[]
    for i in range(n):
        if i%2!=0:arr.append(-3**i)            
        else: arr.append(3**i)
    return arr
print(create_set(n))