# use case - longest monotonically increasing subsequence
# high level - partition into buckets. decide on bucket
#              by variation of binary search. you want it
#              to go in the index where the current val is
#              less than whatever's currently in that
#              "bucket" but more than what's in the bucket
#              at index - 1. if larger than
#              bucket[len(bucket)-1], append to bucket

def patiencesort(arr):
    # if we want to actually recreate the subsequence,
    # need to keep track of the preceding value at that
    # given point in time - prev_map
    buckets,prev_map = [],{}
    for val in arr:
        _place_in_bucket(val,buckets,prev_map)
    res = []
    start = buckets[len(buckets)-1]
    while start:
        res.append(start)
        start = prev_map[start]
    res.reverse()
    for val in res:
        print(val, "=>", end=" ")
    return buckets

def _place_in_bucket(val, buckets, prev_map):
    if not buckets:
        buckets.append(val)
        prev_map[val] = None
        return
    # variation of binary search
    l,r = 0,len(buckets)-1
    while l <= r:
        m = l + (r-l)//2
        if buckets[m] == val:
            return
        if m-1 >= 0 and val < buckets[m] and val > buckets[m-1]:
            buckets[m] = val
            prev_map[val] = buckets[m-1]
            return
        if val < buckets[m]:
            r = m-1
        else:
            l = m+1
    # if l == 0, we know the value has to be smaller than
    # buckets[0]. thus, we replace and return
    if l == 0:
        buckets[l] = val
        prev_map[val] = None
        return
    # val is larger than largest currently in buckets
    buckets.append(val)
    prev_map[val] = buckets[len(buckets)-2]

if __name__ == "__main__":
    arr = [2,1,2,5,3,69,420,12,8,2,7]
    print(patiencesort(arr))