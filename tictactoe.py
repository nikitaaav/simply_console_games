print('Игра крестики - нолики. Для начала игры нажмите Enter!')
x = input()
s = 'C'
while s == 'C':
    print('----------------')
    print('| 7  | 8  | 9  |')
    print('----------------')
    print('| 4  | 5  | 6  |')
    print('----------------')
    print('| 1  | 2  | 3  |')
    print('----------------')
    l = 0
    print('Крестик - первый игрок. Нолик - второй игрок.')
    winner = "Ничья"
    hod = 1
    m = [' ']*9
    while (l < 9):
        x = int(input())
        if hod == 1:
            m[x-1] = '+'
            hod = 2
        else:
            m[x-1] = 'o'
            hod = 1

        print('-------------------')
        print('|  ' + str(m[6]) + '  |  '+ str(m[7]) + '  |  ' + str(m[8]) + '  |')
        print('-------------------')
        print('|  ' + str(m[3]) + '  |  '+ str(m[4]) + '  |  ' + str(m[5]) + '  |')
        print('-------------------')
        print('|  ' + str(m[0]) + '  |  '+ str(m[1]) + '  |  ' + str(m[2]) + '  |')
        print('-------------------')

        # Test players tactic
        if m[0] == m[1] == m[2]:
            if m[0] == '+':
                winner = 'Первый игрок побеждает'
                break
            elif m[0] == 'o':
                winner = 'Второй игрок побеждает'
                break
        elif m[3] == m[4] == m[5]:
            if m[3] == '+':
                winner = 'Первый игрок побеждает'
                break
            elif m[3] == 'o':
                winner = 'Второй игрок побеждает'
                break
        elif m[6] == m[7] == m[8]:
            if m[6] == '+':
                winner = 'Первый игрок побеждает'
                break
            elif m[6] == 'o':
                winner = 'Второй игрок побеждает'
                break
        elif m[6] == m[4] == m[2]:
            if m[2] == '+':
                winner = 'Первый игрок побеждает'
                break
            elif m[2] == 'o':
                winner = 'Второй игрок побеждает'
                break
        elif m[0] == m[4] == m[8]:
            if m[0] == '+':
                winner = 'Первый игрок побеждает'
                break
            elif m[0] == 'o':
                winner = 'Второй игрок побеждает'
                break
        elif m[0] == m[3] == m[6]:
            if m[0] == '+':
                winner = 'Первый игрок побеждает'
                break
            elif m[0] == 'o':
                winner = 'Второй игрок побеждает'
                break
        elif m[1] == m[4] == m[7]:
            if m[1] == '+':
                winner = 'Первый игрок побеждает'
                break
            elif m[1] == 'o':
                winner = 'Второй игрок побеждает'
                break
        elif m[2] == m[5] == m[8]:
            if m[2] == '+':
                winner = 'Первый игрок побеждает'
                break
            elif m[2] == 'o':
                winner = 'Второй игрок побеждает'
                break
        l += 1
    print(winner)
    s = input('Введите C, если хотите сыграть еще раз. Если хотите выйти из игры введите Q:  ')