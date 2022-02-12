# 36.	Дан список чисел. Выделить среди них числа, удовлетворяющие условию: следующее больше предыдущего. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

num=[1, 5, 2, 3, 4, 6, 1, 7]
new_num=[]
def order_min_newt(num):
    for i in range(len(num) - 1):
        n = num[i]
        i += 1
        m = num[i]
        if n < m:
            new_num.append(n)
    return new_num
print(order_min_newt(num))

