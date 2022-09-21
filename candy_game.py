from random import randint as rnd
dificult = None
can_take = None
gm_pl = None
players = ''

print('Игра в конфетки!')
print('Выбор варианта игры\n1: против ПК\n2: Вдвоем')

gm_pl = int(input('Номер варианта? : '))
while True and (gm_pl > 2 or gm_pl < 1):
    gm_pl = int(input('неверный ввод исправьте: '))

players = [input(f"Введите ник {i+1}-го игрока : ") for i in range(gm_pl)]

if gm_pl==1:
    players.append("PC")
    dificult = input('Выберите сложность:\n"новичек" "профи"\nВаш выбор: ')
    print(f'Если решка то первым ходит - {players[gm_pl-1]}, \n'
          f'Если орел то PC\n')
else:
    print(f'Если решка то первым ходит - {players[gm_pl - 2]}, \n'
          f'Если орел то {players[gm_pl - 1]}')


candy= int(input(f'Введите сколько конфет хотите разыграть?: \nВаш выбор= '))
if candy <= 7:
    print('У вас нечего делить:)\nКонец Игры!')
    quit()
elif 7 < candy < 30:
    can_take = rnd(4, candy//3)
else:
    can_take = candy * 2//100 + rnd(5, 11)


print(f'Правила игры:\nСложность !!! {dificult} !!!\nЗа один ход можно забрать не более чем {can_take} конфет.\n'
      'Все конфеты оппонента достаются сделавшему последний ход.')


def coin():
    if rnd(1, 100) % 2 == 0:
        print(f'\n<<<Орел>>>\n')
        return 1
    else:
        print(f"\n<<<Решка>>>\n")
        return 0


start = coin()


while candy > 0:
    for player in players:
        print(f'Игрок {player} ваш выбор\n'
              f' <<  {candy}  >> конфет осталось')
        if player == 'PC':
            if dificult != 'профи':
                chose = rnd(1, candy % can_take)
            else:
                if candy / can_take >= 1 and candy % can_take >= 2:
                    chose = candy % can_take - 1
                elif candy / can_take >= 1 and 0 <= candy % can_take < 2:
                    chose = can_take - rnd(1, can_take-1)
                else:
                    if candy % can_take > 0:
                        chose = rnd(1, candy % can_take + 1)
                    else:
                        chose = candy
            print(f'  PC choice  <<  {chose}  >>  ')
        else:
            chose = int(input(f'Сколько конфет берете? : '))
        if 1 <= chose <= can_take:
            pass
        else:
            while True and (chose < 1 or chose > can_take):
                chose = int(input('!!!вы вышли за рамки правил,\n'
                                  'так сколько забираете? : '))
        candy -= chose
        if candy == 0 and candy >= 0:
            print(f'    <<<  Winner - {player}  >>>')