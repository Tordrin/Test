'''a = 0
while True:
    print('hello' + str(a))
    a += 1
    if a == 15:
        break
print('end')


while True:
    name = input('Name: ')
    if 'А' in name:
        print('Ура')
        break
    else:
        print('нет буквы А в имени')


spis = []
slov = {}
kortesh = (12,'foot')

friends = 'max,vlad,yaroslav,ilya,nikita,aleksey'
birthday = (12,'cake',friends)

print('у меня сегодня ДР '+"мне секгодня "+str(birthday[0])+' лет.' + " На столе будет "+birthday[1]+' ко мне придут '+  str(birthday[2]))

pokupki = [[2,4,3242],
           [58,90,655],
           [67,55,45]]
print(pokupki[1][2])

bestiariy = {"edinorog":'лошадь с одним рогом,пукает радугой',
             'garpy':'огромная ворона с телом женщины',
             "kraken":'гиганский спрут, ел корабли'}

print(bestiariy['garpy'])

foo = [1,2,3,4,5,6,7,8,9]
for x in range(10):
    print(x*9)'''

import random

name = input('Ваше имя: ')
print(f"Привет, {name} ,я хочу сыграть с тобой в игру!")

vopros = 1
while vopros == 1:
    print('Я загадал число от 1 до 100. Отгадаешь?')
    print('У тебя 10 попыток.')
    num = random.randint(1,100)
    popitki = 0
    life = 10
    while True:
        if life > 0:
            cash = life*100
            otvet = int(input('ваше число: '))
            #читы
            if otvet == 666 or otvet == 999:
                print('Псс парень, я загадал ' + str(num))
            if otvet == 123:
                print('Я загадал ' + str(num))
            if otvet == 0:
                exit()
            #ответы
            if num > otvet:
                print("число больше вашего")
                life -=1
                popitki +=1
            elif num < otvet:
                print("число меньше вашего")
                life -=1
                popitki +=1
            else:
                print('Ты справился, '+ str(name) + ', отгадал число всего за ' + str(popitki) + ' попытки(ок)\nТвой выйгрыш ' + str(cash))
                vopros = int(input('Еще разок? (1)да (0)нет'))
                break
        else:
            print('Попытки закончились, салага.')
            vopros = int(input('Еще разок? (1)да (0)нет'))
            break

input()