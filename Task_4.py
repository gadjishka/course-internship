from itertools import combinations

def bananas(s) -> set:
    result = set()
    tmp = list(combinations(range(len(s)), 6))
    ban = tuple('banana')
    for _ in tmp:
        f = True
        for i in range(len(_)):
            if(s[_[i]] != ban[i]):
                f = False
                break
        if f:
            ans = ''
            for i in range(len(s)):
                if i in _:
                    ans += s[i]
                else:
                    ans += '-'
            result.add(ans)
    return result

assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}

'''print(bananas("banana"))
print(bananas("bbananana"))
print(bananas("bananaaa"))
print(bananas("bananana"))'''