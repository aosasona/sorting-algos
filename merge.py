def sort(arr: list[int]):
    n = len(arr)
    if n > 1:

        # Get the middle point and split array into two chunks
        mid = n//2
        l_arr = arr[:mid]
        r_arr = arr[mid:]

        # recursively call this function on these new chunks until it cannot be split
        sort(l_arr)
        sort(r_arr)

        i = j = k = 0

        # compare each elements in each arrays
        while i < len(l_arr) and j < len(r_arr):
            if l_arr[i] < r_arr[j]:
                arr[k] = l_arr[i]
                i += 1
            else:
                arr[k] = r_arr[j]
                j += 1
            k += 1

        # pick the remaining elements and append them to the list
        while i < len(l_arr):
            arr[k] = l_arr[i]
            i += 1
            k += 1

        while j < len(r_arr):
            arr[k] = r_arr[j]
            j += 1 
            k += 1


    return arr



print(sort([56, 71, 2, 98, 12, 11, 5, 34, 1, 44, 88]))
