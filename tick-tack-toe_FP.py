from termcolor import colored

def game():
    length = int(input('Введите длину стороны квадратного поля: '))
    win_length = int(input('Введите количество фигур в ряд для победы: '))
    step = 0
    area = [['.' for i in range(length)] for j in range(length)]
    xo = [colored(str(i), 'red') for i in range(length)]
    xo = xo[::-1]
    xo.append(colored('XO', 'red'))
    xo = xo[::-1]
    yo = [colored(str(i), 'red') for i in range(length)]
    output(xo, yo, area, length, step)
    while True:
        y1, x1 = map(int, input('Ход первого игрока: ').split())
        step += 1
        area = change(area, x1, y1, 1)
        output(xo, yo, area, length, step)
        if check(win_length, area) in ('X', 'O', 'no'):
            winner(win_length, area)
            break
        y2, x2 = map(int, input('Ход второго игрока: ').split())
        step += 1
        area = change(area, x2, y2, 2)
        output(xo, yo, area, length, step)
        if check(win_length, area) in ('X', 'O', 'no'):
            winner(win_length, area)
            break

def winner(win_length, area):
    if check(win_length, area) == 'X':
        print('Первый игрок победил!')
    elif check(win_length, area) == 'O':
        print('Второй игрок победил!')
    else:
        print('Ничья!')
def cicle():
    try:
        k = 1
        while True:
            game()
            if k == 1:
                question = 'Хотите сыграть в крестики нолики? (+ или -): '
            else:
                question = 'Хотите сыграть еще раз? (+ или -): '
            respawn = input(question)
            if respawn == '+':
                k = 0
                continue
            else:
                break
    except:
        print('Извините, какая-то ошибка! Перезапустите игру')
def output(xo, yo, area, length, step):
    print(*xo, sep=colored(' | ', 'yellow'), end='')
    print(colored(' |', 'yellow'))
    print(colored('-' * (length * 5), 'yellow'))
    for i in range(length):
        m = area[i]
        print(colored(str(i), 'red'), end=colored('  | ', 'yellow'))
        print(*m, sep=colored(' | ', 'yellow'), end='')
        print(colored(' |', 'yellow'))
    print(f'Ход: {step}')
def check(win_length, area):
    try:
        for m in area:
            s = ''
            for i in m:
                s += i
            if 'X'*win_length in s:
                return 'X'
            elif 'O'*win_length in s:
                return 'O'
        for i in range(len(area)):
            s = ''
            for y in range(len(area)):
                s += area[y][i]
            if 'X'*win_length in s:
                return 'X'
            elif 'O'*win_length in s:
                return 'O'
        if check_di(win_length, area) in ('X', 'O'):
            return check_di(win_length, area)
        elif no_win(area):
            return 'no'
        else:
            return 'pass'
    except:
        print('error')
def check_di(win_length, area):
    for i in range(1, len(area) + 1):
        x, y = 0, i - 1
        m = ''
        for _ in range(i):
            m += area[y][x]
            x += 1
            y -= 1
        if len(m) >= win_length:
            if 'X'*win_length in m:
                return 'X'
            elif 'O'*win_length in m:
                return 'O'
        x, y = 0, i - 1
        m1 = ''
        for _ in range(len(area) + 1 - i):
            m1 += area[y][x]
            x += 1
            y += 1
        if len(m1) >= win_length:
            if 'X'*win_length in m1:
                return 'X'
            elif 'O'*win_length in m1:
                return 'O'
    for i in range(1, len(area)):
        x, y = i, 0
        m = ''
        for _ in range(len(area) - i):
            m += area[y][x]
            y += 1
            x += 1
        if len(m) >= win_length:
            if 'X'*win_length in m:
                return 'X'
            elif 'O'*win_length in m:
                return 'O'
    for i in range(1, len(area)):
        x, y = i, len(area) - 1
        m = ''
        for _ in range(len(area) - i):
            m += area[y][x]
            y -= 1
            x += 1
        if len(m) >= win_length:
            if 'X'*win_length in m:
                return 'X'
            elif 'O'*win_length in m:
                return 'O'
    return 'no'
        
    

def no_win(area):
    k = 1
    for i in area:
        for j in i:
            if j == '.':
                return False
    else:
        return True
def change(area, x, y, player):
    if player == 1:
        area[y][x] = 'X'
    else:
        area[y][x] = 'O'
    return area

cicle()      
    
    
    