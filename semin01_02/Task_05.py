# 5.	Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

def check_the_number(n):
    if n%5==0 and n%10==0 or n%15==0 and n%30!=0:
        return True
    else: 
        return False
print (check_the_number(76))