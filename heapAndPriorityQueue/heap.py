"""
Class heap implements the data structure heap.

Heap is a complete binary tree where each node satisfies heap property:
1. Complete binary tree is binary tree with following property:
    - each level, except possibly last one is filled.
    - each node is as far left as possible

2. Heap property is the property of a node with:
    - (For max heap): Key at each node in max heap is greater
    than the key at child nodes. And the key at the root node
    is the largest among all nodes.
    - (For min heap): Key at each node in min heap is less than
     the key at the child nodes. And the key at the root
    node is the smallest among all nodes

Repersentation:
1. Tree based
2. Array based : Heaps are usually implemented  with arrays,
 as follows:
    - Each element in array represents a node in a heap
    - The parent/child relationship is defined by implicity
     by the elements indices in the array.
    - If we are storing one element at index i in array Arr,
    the parent will be stored at index i/2(unless its a root,
    as root has no parent)and can be accessed by Arr[i/2], its
     left child can be access by Arr[2*i] and right child
    can be accessed by Arr[2*i+1].
    - Index of root will be 1 in an array.
"""


class Heap:
    def __init__(self, heap_array=[]):
        self.arr = heap_array

    def print_heap(self):
        print(self.arr)


class MaxHeap(Heap):
    def __init__(self, heap_array=[]):
        super().__init__(heap_array)

    def max_heapify(self, current_index, size_of_heap):
        left = 2 * current_index  # left child
        right = 2 * current_index + 1  # right child

        largest = current_index
        if left <= size_of_heap and self.arr[current_index] < self.arr[left]:
            largest = left

        if right <= size_of_heap and self.arr[largest] < self.arr[right]:
            largest = right

        if largest != current_index:
            self.arr[current_index], self.arr[largest] = (
                self.arr[largest],
                self.arr[current_index],
            )
            self.max_heapify(largest, size_of_heap)

    def build_max_heap(self):
        for i in range(len(self.arr), -1, -1):
            self.max_heapify(i, len(self.arr) - 1)

    def peek(self):
        if len(self.arr) == 0:
            return None

        return self.arr[0]

    def pop_max(self):
        if len(self.arr) == 0:
            return None
        maximum_value = self.arr[0]
        self.arr.pop(0)
        self.build_max_heap()
        return maximum_value

    def insert(self, elm):
        if len(self.arr) == 0:
            self.arr.append(elm)
        else:
            self.arr.append(elm)
            self.build_max_heap()

    def delete(self, elm):
        i = 0
        for i in range(0, len(self.arr)):
            if self.arr[i] == elm:
                break

        # element to be deleted is found
        # replace right most left node element
        # with found element and delete last element
        # heapify
        self.arr[i], self.arr[len(self.arr) - 1] = (
            self.arr[len(self.arr) - 1],
            self.arr[i],
        )
        self.arr.pop()
        self.build_max_heap()


class MinHeap(Heap):
    def __init__(self, heap_array=[]):
        super().__init__(heap_array)

    def min_heapify(self, current_index, size_of_heap):
        left = 2 * current_index
        right = 2 * current_index + 1

        smallest = current_index
        if left <= size_of_heap and self.arr[current_index] > self.arr[left]:
            smallest = left

        if right <= size_of_heap and self.arr[smallest] > self.arr[right]:
            smallest = right

        if smallest != current_index:
            self.arr[current_index], self.arr[smallest] = (
                self.arr[smallest],
                self.arr[current_index],
            )
            self.min_heapify(smallest, size_of_heap)

    def build_min_heap(self):
        for i in range(len(self.arr) - 1, -1, -1):
            self.min_heapify(i, len(self.arr) - 1)

    def peek(self):
        if len(self.arr) == 0:
            return None
        return self.arr[0]

    def pop_min(self):
        if len(self.arr) == 0:
            return None

        min_elm = self.arr[0]
        self.arr.pop(0)
        self.build_min_heap()
        return min_elm

    def insert(self, elm):
        if len(self.arr) == 0:
            self.arr.append(elm)
        else:
            self.arr.append(elm)
            self.build_min_heap()

    def delete(self, elm):
        i = 0
        for i in range(0, len(self.arr)):
            if self.arr[i] == elm:
                break

        self.arr[i], self.arr[len(self.arr) - 1] = (
            self.arr[len(self.arr) - 1],
            self.arr[i],
        )
        self.arr.pop()
        self.build_min_heap()


if __name__ == "__main__":
    max_heap = MaxHeap([200, 4, 5, 1, 6, 7, 3, 2])
    print("before")
    max_heap.print_heap()

    max_heap.build_max_heap()
    print("after")
    max_heap.print_heap()

    print(max_heap.peek())
    # h.pop_max()

    print(max_heap.peek())

    max_heap.insert(300)
    max_heap.print_heap()
    print(max_heap.peek())

    max_heap.delete(300)
    max_heap.print_heap()
    print(max_heap.peek())
    print(max_heap.pop_max())
    print(max_heap.peek())

    min_heap = MinHeap([200, 4, 5, 1, 6, 7, 3, 2])
    print("before min heap", min_heap.print_heap())
    min_heap.build_min_heap()
    print("after building min heap", min_heap.print_heap())
    print(min_heap.peek())
    min_heap.pop_min()

    print(min_heap.print_heap())
    print(min_heap.peek())

    min_heap.insert(0)
    print(min_heap.print_heap())
    print(min_heap.peek())

    min_heap.delete(0)
    print(min_heap.print_heap())
    print(min_heap.peek())
