# 39.	Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"

# sweets = 100
# max_sweets = 28
# player = 1


# def get_sweets(player):
#     while True:
#         sweets_count = int(input(f'сколько взять конфет {player}:'))
#         if sweets_count <= max_sweets:
#             return sweets_count


# while True:
#     print(f'сейчас конфет {sweets}')
#     sweets -= get_sweets(player)
#     if sweets == 0:
#         print(f'Победил игрок {player}')
#         break
#     player = 2 if player == 1 else 1


# _____________________против бота_____________________

from random import randint

sweets = 100
max_sweets = 28
player = 1


def get_sweets(player):
    while True:
        if player == 1:
            sweets_count = int(input(f'сколько взять конфет {player}:'))
        else:
            sweets_count = randint(1, sweets)
            print(f' бот взял: {sweets_count}')
        if sweets_count <= max_sweets:
            return sweets_count


while True:
    print(f'сейчас конфет {sweets}')
    sweets -= get_sweets(player)
    if sweets <= 0:
        if player==1:
            print(f'Победил игрок{player}')
            break
        elif player==2:
            print('Победил бот')
    player = 2 if player == 1 else 1
