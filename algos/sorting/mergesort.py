def mergesort(arr):
    # base case - if length is 1, already sorted
    if len(arr) == 1:
        return arr
    # split in half via middle_idx
    middle_idx = len(arr) // 2
    # recursively get left and right sorted halves
    left = mergesort(arr[:middle_idx])
    right = mergesort(arr[middle_idx:])
    # sort the two halves
    res = sort(left,right)
    return res

def sort(left,right):
    res,l_idx,r_idx = [],0,0
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            res.append(left[l_idx])
            l_idx+=1
        else:
            res.append(right[r_idx])
            r_idx+=1
    l_idx < len(left) and res.extend(left[l_idx:])
    r_idx < len(right) and res.extend(right[r_idx:])
    return res

if __name__ == "__main__":
    arr = [5,96,3,7,420,1,3,0,69]
    sorted_array = mergesort(arr)
    print(sorted_array)