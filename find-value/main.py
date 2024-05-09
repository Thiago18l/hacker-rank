def find(arr: list, num: int) -> int:
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return num


print(f"index: {find([3, 1, 3, 4], 4)}")
