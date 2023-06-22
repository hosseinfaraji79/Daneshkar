def fact(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def round_func(item: (int, float), digit: int) -> (int, float):
    item2 = (item // (10 ** -digit)) * (10 ** -digit)
    if (item - item2) * (10 ** (digit + 1)) > 5:
        item2 += (10 ** -digit)
    return item2


def neper_func(num: int, poww: (int, float)) -> (int, float):
    res = 0
    for i in range(int(num)):
        res += (poww **i) / (fact(i))
    return round_func(res, 3)

print(neper_func(100, 6))