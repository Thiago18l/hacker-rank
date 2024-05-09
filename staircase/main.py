def staircase(n: int) -> None:
    for stairs in range(1, n + 1):
        print(" " * (n - stairs) + "#" * stairs)


staircase(3)
