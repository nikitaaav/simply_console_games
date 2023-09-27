# Gem Puzzle or Game of Fifteen
import random

def correct_test(area):
    messes = 0
    m = []
    for i in area:
        for j in i:
            if (j != '  ') and (j != ' '):
                m.append(int(j))
    for i in range(len(m)):
        element = m[i]
        for j in range(i+1, len(m)):
            if m[j] < element:
                messes += 1
    if messes % 2 == 0:
        return True
    else:
        return False
def tegeg(number):
    if len(number) == 1:
            number = ' ' + number
    return number
def test(number, area):
    g = 0
    for i in range(4):
        for j in range(4):
            if area[i][j] == number:
                g = 1
                break
        if g == 1:
            break
    if g == 1:
        return True
    else:
        return False


z = input('Press Enter to start the game!')

# game area generation
area = [[0, 0, 0, 0] for i in range(4)]
m = ['  ', ' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10', '11', '12', '13', '14', '15']
result = [' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10', '11', '12', '13', '14', '15', '  ']
random.shuffle(m)

while not correct_test(m):
    random.shuffle(m)

k = 0
steps = 0

for i in range(4):
    for j in range(4):
        area[i][j] = m[k]
        k += 1



while True:
    # print area
    print(' __________________________')
    print('')
    print('|  ' + area[0][0] + '  |  '+ area[0][1] + '  |  ' + area[0][2] + '  | ' + area[0][3] + '  |')
    print(' __________________________')
    print('')
    print('|  ' + area[1][0] + '  |  '+ area[1][1] + '  |  ' + area[1][2] + '  | ' + area[1][3] + '  |')
    print(' __________________________')
    print('')
    print('|  ' + area[2][0] + '  |  '+ area[2][1] + '  |  ' + area[2][2] + '  | ' + area[2][3] + '  |')
    print(' __________________________')
    print('')
    print('|  ' + area[3][0] + '  |  '+ area[3][1] + '  |  ' + area[3][2] + '  | ' + area[3][3] + '  |')
    print(' __________________________')
    print('')
    number = tegeg(input('Enter the number you want to move to an empty space: '))
    if not (test(number, area)):
        print('Error! There is no such number in the deck. Enter the number again')
        print('')
        continue
    else:
        k = 1
        gtg = 1
        for i in range(4):
            for j in range(4):
                if number == area[i][j]:
                    if (0 <= i+1 <= 3) and (area[i+1][j] == '  '):
                        area[i][j], area[i+1][j] = area[i+1][j], area[i][j]
                        gtg = 0
                        break
                    elif (0 <= i-1 <= 3) and (area[i-1][j] == '  '):
                        area[i][j], area[i-1][j] = area[i-1][j], area[i][j]
                        gtg = 0
                        break
                    elif (0 <= j+1 <= 3) and (area[i][j+1] == '  '):
                        area[i][j], area[i][j+1] = area[i][j+1], area[i][j]
                        gtg = 0
                        break
                    elif (0 <= j-1 <= 3) and (area[i][j-1] == '  '):
                        area[i][j], area[i][j-1] = area[i][j-1], area[i][j]
                        gtg = 0
                        break
                    else:
                        print('Error! This number cannot be shifted!')
                        print('')
                        k = 0   
            if gtg == 0:
                break                
        if k == 0:
            continue
        else:
            steps += 1
            tst = 1
            delta = 0
            for i in range(4):
                for j in range(4):
                    if area[i][j] != result[delta]:
                        tst = 0
                        break
                    delta += 1
                if tst == 0:
                    break
            if tst == 1:
                break

print(' __________________________')
print('')
print('|  ' + area[0][0] + '  |  '+ area[0][1] + '  |  ' + area[0][2] + '  | ' + area[0][3] + '  |')
print(' __________________________')
print('')
print('|  ' + area[1][0] + '  |  '+ area[1][1] + '  |  ' + area[1][2] + '  | ' + area[1][3] + '  |')
print(' __________________________')
print('')
print('|  ' + area[2][0] + '  |  '+ area[2][1] + '  |  ' + area[2][2] + '  | ' + area[2][3] + '  |')
print(' __________________________')
print('')
print('|  ' + area[3][0] + '  |  '+ area[3][1] + '  |  ' + area[3][2] + '  | ' + area[3][3] + '  |')
print(' __________________________')
print('')
print('')
print("Congratulations!!! You've won!")
print('You have done {} steps'.format(steps))

