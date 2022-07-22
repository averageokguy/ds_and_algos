from math import ceil

class StandardHeap:
    def __init__(self, arr=[]) -> None:
        self._heapify(arr)

    def push(self, val):
        idx = len(self.heap)
        self.heap.append(val)
        self._bubble_up(idx)

    def pop(self):
        if not self.heap:
            return None
        swap_idx = len(self.heap) - 1
        self.heap[0],self.heap[swap_idx] = self.heap[swap_idx],self.heap[0]
        res = self.heap.pop()
        self.heap and self._bubble_down(self.heap[0], 0)
        return res

    def peek(self):
        return self.heap[0]

    def _heapify(self, arr):
        if not arr:
            return []
        self.heap = [None] * len(arr)
        for idx in range(len(arr) - 1, -1, -1):
            self._bubble_down(arr[idx], idx)

    def _bubble_up(self, idx):
        if idx == 0 or self.heap[idx] > self.heap[ceil(idx / 2) - 1]:
            return
        self.heap[idx],self.heap[ceil(idx / 2) - 1] = self.heap[ceil(idx / 2) - 1],self.heap[idx]
        self._bubble_up(ceil(idx / 2) - 1)

    def _bubble_down(self, val, idx):
        if len(self.heap) <= 2*idx + 1:
            self.heap[idx] = val
            return
        left = self.heap[2*idx + 1]
        right = self.heap[2*idx + 2] if 2*idx + 2 < len(self.heap) else float("inf")
        self.heap[idx] = val
        if val > min(left,right):
            if left < right:
                self.heap[idx],self.heap[2*idx+1] = self.heap[2*idx+1],self.heap[idx]
                self._bubble_down(val, 2*idx+1)
            else:
                self.heap[idx],self.heap[2*idx+2] = self.heap[2*idx+2],self.heap[idx]
                self._bubble_down(val, 2*idx+2)

if __name__ == "__main__":
    my_heap = StandardHeap([2,5,69,12,0,-420])
    while my_heap.heap:
        print(my_heap.pop())