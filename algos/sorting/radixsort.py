from math import log, ceil

def radixsort(arr):
    # need max_val to determine max_digits possible
    max_val = max(arr)
    max_digits = ceil(log(max_val,10))
    for place in range(max_digits):
        # bucket for each digit 0-9
        buckets = [[] for n in range(10)]
        for val in arr:
            # reduce val to the relevant digit. handwrite
            # e.g. try to get tens place of 420
            # 420 // 10**1 == 42
            # 42 % 10 = 2
            bucket_idx = (val // 10**place) % 10
            buckets[bucket_idx].append(val)
        # reset array in order to recreate from buckets
        arr = []
        for bucket in buckets:
            arr+=bucket
    return arr

if __name__ == "__main__":
    arr = [5,96,3,112,156,212,254,342,256,299,301,7,420,1,3,0,69]
    print(radixsort(arr))