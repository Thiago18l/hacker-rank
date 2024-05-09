def tallest(n: list) -> int:
    max_value = n[0]
    for num in n[1:]:
        if num > max_value:
            max_value = num
    return max_value


# Poderia ser usando max()
def birthdayCandles(candles: list):
    taller = tallest(candles)
    counter = 0
    for i in candles:
        if i == taller:
            counter += 1

    print(counter)


birthdayCandles([3, 2, 1, 3])
