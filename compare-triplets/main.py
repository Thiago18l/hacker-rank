def compareTriplets(array_alice: list, array_bob: list):
    alice_points = 0
    bob_points = 0

    for i in range(len(array_alice)):
        if array_alice[i] > array_bob[i]:
            alice_points += 1
        elif array_alice[i] < array_bob[i]:
            bob_points += 1

    print(alice_points, bob_points)


compareTriplets([5, 6, 7], [3, 6, 10])
