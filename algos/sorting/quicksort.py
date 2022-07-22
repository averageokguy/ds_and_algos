# reference video - 

def quicksort(arr):
    # base case - return empty array if array is already empty
    if len(arr) == 0:
        return []
    # base case - return array if len == 1 => already sorted
    if len(arr) == 1:
        return arr
    # define first value in array as pivot
    p = arr[0]
    l = 1
    # iterate through remainder of array
    for r in range(1,len(arr)):
        # swap arr[l] and arr[r] when arr[p] < p => we want all
        # values smaller than pivot to be as far left in the
        # array as they can be
        if arr[r] < p:
            arr[l],arr[r] = arr[r],arr[l]
            l+=1
    # swap pivot and arr[l-1] => 1 - l-1 is the boundary of all
    # values smaller than pivot
    arr[0],arr[l-1] = arr[l-1],arr[0]
    # recursively sort left and right subarrays
    left = quicksort(arr[:l-1])
    right = quicksort(arr[l:])
    # ez smoosh via python
    return left + [p] + right

if __name__ == "__main__":
    arr = [5,96,3,7,420,1,3,0,69]
    sorted_array = quicksort(arr)
    print(sorted_array)