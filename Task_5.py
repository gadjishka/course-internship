from itertools import combinations_with_replacement
from functools import reduce

def count_find_num(primesL, limit):
    ans = set()
    len_p = len(primesL)
    for i in range(len_p, 100):
        f = False
        tmp = combinations_with_replacement(primesL, i)
        for _ in tmp:
            if set(_) == set(primesL):
                mat_a = reduce(lambda x, y: x * y, _)
                if mat_a <= limit:
                    f = True
                    ans.add(mat_a)
        if not (f):
            break
    return [len(ans), max(ans)] if len(ans) > 0 else []
