def maximum(arr: list) -> int:
    maximum_index = 0
    maximum = arr[0]
    for i in range(len(arr)):
        if arr[i] > maximum:
            maximum_index = i
            maximum = arr[i]
    return maximum, maximum_index


num, index = maximum([8, 10, 23, 12, 5])
print(num, index)
