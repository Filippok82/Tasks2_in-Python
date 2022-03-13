# Задача 8 Напишите проверку на то, является ли строка палиндромом. 
# Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.

my_str=str(input('Ввведите строку для проверки: '))

# def polindrom (my_str):
#     if my_str[0]==my_str[4] and my_str[1]==my_str[3]:
#         return 'строка является полиндромом'
#     else:
#         return 'строка  не является полиндромом'

# print (polindrom(my_str))


# def is_palindrome(my_str):
#     return my_str == ''.join(reversed(my_str))
# print(is_palindrome(my_str))



def is_palindrome(my_str):
    return my_str == my_str[::-1]

print(is_palindrome(my_str))