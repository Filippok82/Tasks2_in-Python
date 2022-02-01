# 15.	Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]


def pow_numbers (n):
    x=1
    arr=[]
    for i in range(1,n+1):
        x=i*x
        arr.append(x)
    return arr
print(pow_numbers(6))
