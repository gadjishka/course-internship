from math import sqrt

def count_find_num(primesL, limit):
    prod = 1
    count = 0
    max_int = 0
    for i in range(len(primesL)):
        prod *= primesL[i]
    for x in range(prod, limit + 1):
        tmp = set()
        x_2 = x
        for i in range(2, int(sqrt(x) + 1)):
            while x % i == 0:
                tmp.add(int(i))
                x /= i
        if x != 1:
            tmp.add(int(x))
        if tmp == set(primesL):
            count += 1
            if x_2 > max_int:
                max_int = x_2
    return [count, max_int] if count > 0 else []

primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []

