def fun1(x, y, z):
    if x == 1:
        return fun2(y, y=z)
    elif x == 2:
        return x + y + z
    elif x == 3:
        return fun2(y=9, z=x + y)
    else:
        return 17


def fun2(x=7, y=9, z=11):
    if x == 2:
        return x + y + z
    elif x == 7:
        return x * y * z
    else:
        return 42


print(fun2)
print(fun1(1, 2, 3))
