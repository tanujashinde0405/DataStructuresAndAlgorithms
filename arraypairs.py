# Log all pairs of array


def logallpairsofarray(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            print(arr[i], arr[j])


arr = [1, 2, 3, 4, 5]
logallpairsofarray(arr)
