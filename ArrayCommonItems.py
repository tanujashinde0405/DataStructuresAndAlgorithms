def returnifcommonitems(arr1, arr2):
    for i in range(0, len(arr1)):
        if arr1[i] in arr2:
            return True
    return False


arr1 = ['1', '2', '3', '4', '5']
arr2 = ['7', '6', '9']
print(returnifcommonitems(arr1, arr2))
