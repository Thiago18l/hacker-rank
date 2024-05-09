def minMaxSum(arr: list):
    total_sum = sum(arr)
    min_value = arr[0]
    max_value = arr[0]

    for num in arr[1:]:
        min_value = min(min_value, num)
        max_value = max(max_value, num)

    min_sum = total_sum - max_value
    max_sum = total_sum - min_value
    print(min_sum, max_sum)


minMaxSum([1, 3, 5, 7, 9])
