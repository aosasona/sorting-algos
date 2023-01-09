def sort(arr):
    for i in range(len(arr) - 1):
        minimum_pos = i

        for j in range(i + 1, len(arr)):
            if(arr[j] < arr[minimum_pos]):
                minimum_pos = j

        arr[i], arr[minimum_pos] = arr[minimum_pos], arr[i]
    
    return arr


print(sort([23, 14, 5, 3, 26, 2]))
