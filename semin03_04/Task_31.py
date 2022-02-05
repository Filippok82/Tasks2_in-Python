# 31.	Составить список простых множителей натурального числа N


n = int(input('введите n:'))


a=[]
for i in range(2,n + 1):
    if n % i == 0:           
        for j in range(2,(i//2 + 1)):
            if(i % j == 0): 
                break
        else:
            a.append(i)
print(a)


