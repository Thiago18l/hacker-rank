def diagonalDifference(arr: list):
    n = len(arr)  # Número de linhas e colunas
    primary_sum = 0
    secondary_sum = 0
    for i in range(n):
        primary_sum += arr[i][i]
        secondary_sum += arr[i][n - 1 - i]
    return abs(primary_sum - secondary_sum)


matrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
diff = diagonalDifference(matrix)
print(diff)
