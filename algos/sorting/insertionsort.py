# mentality - through each iteration, want to put the smallest
# item at index i
def insertionsort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr

if __name__ == "__main__":
    arr = [5,96,3,7,420,1,3,0,69]
    print(insertionsort(arr))