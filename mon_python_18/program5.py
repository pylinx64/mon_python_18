import random

# коробка для лотереи
case = ['XBOX', 'Дом в Запорожье', '1000 $', 'iphone 9', 'кирпич']

# коробка для кол-во попыток
money = 1000

while True:
    input()
    # проверка: если денег = 0, то останавливаем игру
    if money < 0:
        print('Денег нет')
        break
    
    # рандомно выбирает предмет из списка
    win_box = random.choice(case)
    print('Ваша награда: ')
    print(win_box)
    
    # уменьшаем кол-во попыток
    money = money - 600
    print(money)
    
