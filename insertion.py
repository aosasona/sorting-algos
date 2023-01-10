"""
In a summary, this compares the previous element with the current one, it walks backwards on each iteration
"""
def sort(arr: list[int]):
    length = len(arr)
    for i in range(1, length):
        j = i - 1
        while arr[j+1] < arr[j] and j >= 0:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1

    return arr

print(sort([100, 3, 76, 34, 19]))
