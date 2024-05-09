def fact(num: int):
    return (lambda num: 1 if num == 0 else num * fact(num - 1))(num)


print(fact(4))
