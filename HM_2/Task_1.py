from itertools import permutations
from math import sqrt

def func(arr):
    arr.append(arr[0])
    tmp = [i for i in list(permutations(arr)) if i[0] == i[len(i)-1] == arr[0]]
    max_ = 1000000
    iter = 0
    for i in range(len(tmp)):
        tmp_2 = 0
        for j in range(0, len(tmp[i]) - 1):
            tmp_2 += sqrt((tmp[i][j+1][0] - tmp[i][j][0])**2 + (tmp[i][j+1][1] - tmp[i][j][1])**2)
        if tmp_2 < max_:
            max_ = tmp_2
            iter = i
    tmp_2 = 0
    iter = tmp[iter]
    print(iter[0], end='')
    for i in range(0, len(iter) - 1):
        tmp_2 += sqrt((iter[i + 1][0] - iter[i][0]) ** 2 + (iter[i + 1][1] - iter[i][1]) ** 2)
        print(' ->', iter[i+1], f'[{tmp_2}]', end='')
    print(' = ', tmp_2)

Postal_office = (0, 2)
st_Griboyedov = (2, 5)
baker_st = (5, 2)
st_Bolshaya_Sadovaya = (6, 6)
evergreen_alley = (8, 3)
func([Postal_office, st_Griboyedov, baker_st, st_Bolshaya_Sadovaya, evergreen_alley])
