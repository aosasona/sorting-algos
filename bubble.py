"""
This compares the next array element (moving forward)
"""
def sort(arr: list[int]):
    length = len(arr)

    for i in range(length):
        for j in range(0, length - i - 1):
            if(arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

print(sort([23,62,90,6,1]))
