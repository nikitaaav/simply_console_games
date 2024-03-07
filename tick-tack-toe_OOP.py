from termcolor import colored


class Board:
    def __init__(self, win_length, size):
        self.win_length = win_length
        self.size = size
        self.board = [[Item() for i in range(self.size)] for _ in range(self.size)]
        self.step = 0
    def output(self):
        xo = [colored(str(i), 'red') for i in range(self.size)]
        xo = xo[::-1]
        xo.append(colored('XO', 'red'))
        xo = xo[::-1]
        print(*xo, sep=colored(' | ', 'yellow'), end='')
        print(colored(' |', 'yellow'))
        print(colored('-' * (self.size * 5), 'yellow'))
        for i in range(self.size):
            m = self.board[i]
            print(colored(str(i), 'red'), end=colored('  | ', 'yellow'))
            print(*m, sep=colored(' | ', 'yellow'), end='')
            print(colored(' |', 'yellow'))
        print(f'Ход: {self.step}')
    def check(self):
        for m in self.board:
            s = ''
            for i in m:
                s += str(i)
            if 'X'*self.win_length in s:
                return 'X'
            elif 'O'*self.win_length in s:
                return 'O'
        for i in range(len(self.board)):
            s = ''
            for y in range(len(self.board)):
                s += str(self.board[y][i])
            if 'X'*self.win_length in s:
                return 'X'
            elif 'O'*self.win_length in s:
                return 'O'
        for i in range(1, len(self.board) + 1):
            x, y = 0, i - 1
            m = ''
            for _ in range(i):
                m += str(self.board[y][x])
                x += 1
                y -= 1
            if len(m) >= self.win_length:
                if 'X'*self.win_length in m:
                    return 'X'
                elif 'O'*self.win_length in m:
                    return 'O'
            x, y = 0, i - 1
            m1 = ''
            for _ in range(len(self.board) + 1 - i):
                m1 += str(self.board[y][x])
                x += 1
                y += 1
            if len(m1) >= self.win_length:
                if 'X'*self.win_length in m1:
                    return 'X'
                elif 'O'*self.win_length in m1:
                    return 'O'
        for i in range(1, len(self.board)):
            x, y = i, 0
            m = ''
            for _ in range(len(self.board) - i):
                m += str(self.board[y][x])
                y += 1
                x += 1
            if len(m) >= self.win_length:
                if 'X'*self.win_length in m:
                    return 'X'
                elif 'O'*self.win_length in m:
                    return 'O'
        for i in range(1, len(self.board)):
            x, y = i, len(self.board) - 1
            m = ''
            for _ in range(len(self.board) - i):
                m += str(self.board[y][x])
                y -= 1
                x += 1
            if len(m) >= self.win_length:
                if 'X'*self.win_length in m:
                    return 'X'
                elif 'O'*self.win_length in m:
                    return 'O'
        k = 1
        for i in self.board:
            for j in i:
                if str(j) == '.':
                    return 'continue'
        else:
            return 'no'

class Item:
    def __init__(self, symb='.'):
        self.symb = symb
    def change(self, new_symb):
        self.symb = new_symb
    def can_change(self):
        if self.symb == '.':
            return True
        else:
            return False
    def __str__(self):
        return self.symb

class Game:
    def __init__(self) -> None:
        pass
    def start_game(self):
        size = int(input('Введите длину стороны квадратного поля: '))
        win_length = int(input('Введите количество фигур в ряд для победы: '))
        desk = Board(win_length, size)
        desk.output()
        while True:
            while True:
                y, x = map(int, input('Ход первого игрока: ').split())
                if desk.board[y][x].can_change():
                    desk.board[y][x].change('X')
                    desk.step += 1
                    break
                else:
                    print(colored('Неправильный ход!!!', 'light_red'))
                    continue
            desk.output()
            if desk.check() in ('X', 'O', 'no'):
                if desk.check() == 'X':
                    print('Первый игрок победил!')
                else:
                    print('Ничья!')
                break
            while True:
                y, x = map(int, input('Ход второго игрока: ').split())
                if desk.board[y][x].can_change():
                    desk.board[y][x].change('O')
                    desk.step += 1
                    break
                else:
                    print(colored('Неправильный ход!!!', 'light_red'))
                    continue
            desk.output()
            if desk.check() in ('X', 'O', 'no'):
                if desk.check() == 'X':
                    print('Второй игрок победил!')
                else:
                    print('Ничья!')
                break

while True:
    new_game = Game()
    new_game.start_game()
    go = input('Хотите сыграть еще раз? (+ или -):')
    if go == '+':
        continue
    else:
        break 
