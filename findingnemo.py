import time


def finding_nemo(arr):
    t1 = time.time()
    print(t1)
    for i in range(0, len(arr)):
        if arr[i] == 'nemo':
            print("found nemo")
            break
    t2 = time.time()
    print(t2)
    print("time taken by findingnemo function is : ", (t2 - t1))


arr = ['tanu', 'dory', 'clown', 'nemo', 'rachel']
finding_nemo(arr)
