MIN_INT = -2**31
MAX_INT = 2**31-1

def reverse(x: int) -> int:
    x_str = str(x)
    if x_str[0] == "-":
        neg = True
        x_str = x_str[1:]
    else:
        neg = False
    x_str_rev = x_str[::-1]
    x_rev = int(x_str_rev)
    if neg:
        x_rev = - x_rev
    if x_rev < MIN_INT or x_rev > MAX_INT:
        return 0
    return x_rev
