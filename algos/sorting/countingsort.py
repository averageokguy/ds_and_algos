def countingsort(arr):
    # minimize temporary array size. also handles arrays
    # with negative values
    offset = min(arr)
    # needed to determine size of temporary array
    max_val = max(arr)
    # temp array to keep track of count of each number.
    # notice we only need an array with size of the range
    # of the input + 1
    count = [0] * (max_val - offset + 1)
    for val in arr:
        count[val - offset]+=1
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    res = [None] * len(arr)
    for val in arr:
        # decrement count array. then, use that value as
        # the idx to be updated in res[]
        count[val - offset]-=1
        idx = count[val - offset]
        res[idx] = val
    return res

if __name__ == "__main__":
    arr = [4,2,5,7,12,4,2,6,11,-1]
    print(countingsort(arr))