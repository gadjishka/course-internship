from random import randint


def Pole(arr):
    for i in range(10):
        print("______", end="")
    print("_")
    for i in range(10):
        print('| ', end='')
        for j in range(10):
            if type(arr[i][j]) == int:
                print("%3d" % arr[i][j], end=' | ')
            else:
                print(f" {arr[i][j]} ", end=' | ')
        print()
        for j in range(10):
            print("|-----", end="")
        print("|")
    EX(arr)


def Man_Move(arr):
    print("Select field number: ", end=' ')
    move = int(input())
    while move not in [i for i in range(100)] or (arr[move // 10][move % 10] in ['X', 'O']):
        print("Please select another: ", end=' ')
        move = int(input())
    arr[move // 10][move % 10] = 'X'


def CP_Move(arr):
    while True:
        a = randint(0, 9)
        b = randint(0, 9)
        if arr[a][b] not in ['X', 'O']:
            arr[a][b] = 'O'
            break


def EX(arr):
    f = False
    for i in range(10):
        if not f:
            for j in range(10):
                if arr[i][j] not in ['X', 'O']:
                    f = True
                    break
        else:
            break
    if not f:
        print('Draw!!')
        exit()
    Ex_col_row(arr, 'X')
    Ex_col_row(arr, 'O')
    Ex_diag(arr, 'X')
    Ex_diag(arr, 'O')
    Ex_invert_diag(arr, 'X')
    Ex_invert_diag(arr, 'O')


def Ex_col_row(arr, symbl):
    f_1 = False
    flag_1 = -1
    f_2 = False
    flag_2 = -1
    for row in arr:
        if row.count(symbl) >= 5:
            for i in range(len(row)):
                if row[i] == symbl and not f_1:
                    f_1 = True
                    flag_1 = i
                elif row[i] == symbl and f_1:
                    if i - flag_1 == 4:
                        if symbl == 'X':
                            print("You lose!!!")
                        else:
                            print('CP lose!!')
                        exit()
                else:
                    f_1 = False
                    flag_1 = -1
    for i in range(10):
        for j in range(10):
            if arr[j][i] == symbl and not f_2:
                f_2 = True
                flag_2 = j
            elif arr[j][i] == symbl and f_2:
                if j - flag_2 == 4:
                    if symbl == 'X':
                        print("You lose!!!")
                    else:
                        print('CP lose!!')
                    exit()
            else:
                f_2 = False
                flag_2 = -1


def Ex_diag(arr, symbl):
    for j in range(5):
        f = False
        flag = -1
        h = j
        for i in range(10 - j):
            if arr[i][h] == symbl and not f:
                f = True
                flag = i
            elif arr[i][h] == symbl and f:
                if i - flag == 4:
                    if symbl == 'X':
                        print("You lose!!!")
                    else:
                        print('CP lose!!')
                    exit()
            else:
                f = False
                flag = -1
            h += 1
    for j in range(5):
        f = False
        flag = -1
        h = j
        for i in range(10 - j):
            if arr[h][i] == symbl and not f:
                f = True
                flag = i
            elif arr[h][i] == symbl and f:
                if i - flag == 4:
                    if symbl == 'X':
                        print("You lose!!!")
                    else:
                        print('CP lose!!')
                    exit()
            else:
                f = False
                flag = -1
            h += 1


def Ex_invert_diag(arr, symbl):
    for j in range(9, 3, -1):
        f = False
        flag = -1
        h = j
        for i in range(j):
            if arr[i][h] == symbl and not f:
                f = True
                flag = i
            elif arr[i][h] == symbl and f:
                if i - flag == 4:
                    if symbl == 'X':
                        print("You lose!!!")
                    else:
                        print('CP lose!!')
                    exit()
            else:
                f = False
                flag = -1
            h -= 1
    for j in range(1, 6):
        f = False
        flag = -1
        h = j
        for i in range(9, j - 1, -1):
            if arr[h][i] == symbl and not f:
                f = True
                flag = i
            elif arr[h][i] == symbl and f:
                if abs(i - flag) == 4:
                    if symbl == 'X':
                        print("You lose!!!")
                    else:
                        print('CP lose!!')
                    exit()
            else:
                f = False
                flag = -1
            h += 1


array = [[j for j in range(i - 10, i)] for i in range(10, 101, 10)]

while True:
    Pole(array)
    CP_Move(array)
    Man_Move(array)
