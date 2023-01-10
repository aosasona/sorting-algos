"""
This is another divide-and-conquer algo
It picks a pivot and compares every other value to it
- The ones smaller than the pivot are placed in a sublist and the same is done for bigger ones
This is done recursively until the array contains 1 or no element

-- EFFECTIVE FOR VERY LARGE LISTS with O(n log n) efficiency in the best case scenario
"""
def sort(arr: list[int]):
    length = len(arr)
    if length <= 1: 
        return arr
    else:
        pivot = arr.pop()

    greater_arr = []
    lesser_arr = []

    for element in arr:
        if element > pivot:
            greater_arr.append(element)
        else:
            lesser_arr.append(element)

    return sort(lesser_arr) + [pivot] + sort(greater_arr)

print(sort([20, 29, 12, 3, 90, 65, 3, 83, 42]))
