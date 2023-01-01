def sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[i]):
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp

    return arr

print(sort([23, 14, 5, 3, 26, 2]))
