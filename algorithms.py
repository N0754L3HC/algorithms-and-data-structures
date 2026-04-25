"""
Algorithms & Data Structures
=============================
Implementations of core CS concepts from the OCR A-Level specification:

  Sorting:        Bubble Sort, Insertion Sort, Merge Sort, Quick Sort
  Searching:      Linear Search, Binary Search
  Data Structures: Stack, Queue, Binary Search Tree

Each algorithm prints a step-by-step trace so you can follow the logic.

Run:  python algorithms.py
"""

# ═══════════════════════════════════════════════════════════════
#  SORTING ALGORITHMS
# ═══════════════════════════════════════════════════════════════

def bubble_sort(arr: list, trace: bool = True) -> tuple[list, int]:
    """
    Bubble Sort — O(n²) time, O(1) space
    Repeatedly swaps adjacent elements that are in the wrong order.
    """
    a = arr.copy()
    comparisons = 0
    n = len(a)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if trace:
            print(f"  Pass {i+1}: {a}")
        if not swapped:
            if trace:
                print(f"  Early exit — array sorted after {i+1} passes")
            break

    return a, comparisons


def insertion_sort(arr: list, trace: bool = True) -> tuple[list, int]:
    """
    Insertion Sort — O(n²) time, O(1) space
    Builds a sorted sublist by inserting each element into its correct position.
    """
    a = arr.copy()
    comparisons = 0

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            comparisons += 1
            a[j + 1] = a[j]
            j -= 1
        comparisons += 1  # final comparison that exits the loop
        a[j + 1] = key
        if trace:
            print(f"  Insert {key} → {a}")

    return a, comparisons


def merge_sort(arr: list, depth: int = 0, trace: bool = True) -> list:
    """
    Merge Sort — O(n log n) time, O(n) space
    Divide and conquer: split in half, sort each half, merge.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left  = merge_sort(arr[:mid],  depth + 1, trace)
    right = merge_sort(arr[mid:],  depth + 1, trace)
    merged = _merge(left, right)

    if trace:
        indent = "  " * depth
        print(f"{indent}merge({left}, {right}) → {merged}")

    return merged


def _merge(left: list, right: list) -> list:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]);  i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr: list, low: int = None, high: int = None, trace: bool = True) -> list:
    """
    Quick Sort — O(n log n) average, O(n²) worst, O(log n) space
    Partitions around a pivot so all smaller items are left, larger right.
    """
    if low is None:
        arr = arr.copy()
        low, high = 0, len(arr) - 1

    if low < high:
        pivot_idx = _partition(arr, low, high)
        if trace:
            print(f"  pivot={arr[pivot_idx]}  →  {arr}")
        quick_sort(arr, low, pivot_idx - 1, trace)
        quick_sort(arr, pivot_idx + 1, high, trace)

    return arr


def _partition(arr: list, low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# ═══════════════════════════════════════════════════════════════
#  SEARCHING ALGORITHMS
# ═══════════════════════════════════════════════════════════════

def linear_search(arr: list, target, trace: bool = True) -> int:
    """
    Linear Search — O(n) time
    Checks each element one by one from left to right.
    """
    for i, val in enumerate(arr):
        if trace:
            print(f"  Check index {i}: {val} {'== TARGET' if val == target else ''}")
        if val == target:
            return i
    return -1


def binary_search(arr: list, target, trace: bool = True) -> int:
    """
    Binary Search — O(log n) time, requires sorted input
    Repeatedly halves the search space by comparing against the midpoint.
    """
    lo, hi = 0, len(arr) - 1
    step = 0

    while lo <= hi:
        mid = (lo + hi) // 2
        step += 1
        if trace:
            view = arr[lo:hi+1]
            print(f"  Step {step}: lo={lo} hi={hi} mid={mid} arr[mid]={arr[mid]}", end="")
        if arr[mid] == target:
            if trace:
                print(f"  ← FOUND")
            return mid
        elif arr[mid] < target:
            lo = mid + 1
            if trace:
                print(f"  → go right")
        else:
            hi = mid - 1
            if trace:
                print(f"  → go left")

    return -1


# ═══════════════════════════════════════════════════════════════
#  DATA STRUCTURES — STACK
# ═══════════════════════════════════════════════════════════════

class Stack:
    """
    LIFO stack backed by a Python list.
    Supports push, pop, peek, size, and display.
    """
    def __init__(self, max_size: int = None):
        self._data = []
        self._max = max_size

    def push(self, item) -> bool:
        if self._max and len(self._data) >= self._max:
            print(f"  Stack overflow — max size {self._max} reached")
            return False
        self._data.append(item)
        print(f"  push({item})  →  {self}")
        return True

    def pop(self):
        if self.is_empty():
            print("  Stack underflow — cannot pop from empty stack")
            return None
        item = self._data.pop()
        print(f"  pop()  →  {item}  |  stack: {self}")
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def __str__(self):
        return f"[{' | '.join(str(x) for x in self._data)}]  ← top"


# ═══════════════════════════════════════════════════════════════
#  DATA STRUCTURES — QUEUE
# ═══════════════════════════════════════════════════════════════

class Queue:
    """
    FIFO queue backed by a Python list.
    Supports enqueue, dequeue, peek, size, and display.
    """
    def __init__(self, max_size: int = None):
        self._data = []
        self._max = max_size

    def enqueue(self, item) -> bool:
        if self._max and len(self._data) >= self._max:
            print(f"  Queue full — max size {self._max} reached")
            return False
        self._data.append(item)
        print(f"  enqueue({item})  →  {self}")
        return True

    def dequeue(self):
        if self.is_empty():
            print("  Queue empty — cannot dequeue")
            return None
        item = self._data.pop(0)
        print(f"  dequeue()  →  {item}  |  queue: {self}")
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def __str__(self):
        return f"front → [{' | '.join(str(x) for x in self._data)}] ← rear"


# ═══════════════════════════════════════════════════════════════
#  DATA STRUCTURES — BINARY SEARCH TREE
# ═══════════════════════════════════════════════════════════════

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree:
    """
    Binary Search Tree with insert, search, and three traversal orders.
    - In-order  (left → root → right) → sorted output
    - Pre-order (root → left → right) → copy/serialise
    - Post-order(left → right → root) → delete/free
    """
    def __init__(self):
        self.root = None

    def insert(self, value) -> None:
        if self.root is None:
            self.root = BSTNode(value)
            print(f"  insert({value})  →  root")
        else:
            self._insert(self.root, value, "root")

    def _insert(self, node: BSTNode, value, path: str) -> None:
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
                print(f"  insert({value})  →  left of {node.value}  [{path} → left]")
            else:
                self._insert(node.left, value, path + " → left")
        elif value > node.value:
            if node.right is None:
                node.right = BSTNode(value)
                print(f"  insert({value})  →  right of {node.value}  [{path} → right]")
            else:
                self._insert(node.right, value, path + " → right")
        else:
            print(f"  insert({value})  →  duplicate, ignored")

    def search(self, value) -> bool:
        node = self.root
        steps = 0
        while node:
            steps += 1
            if value == node.value:
                print(f"  search({value})  →  FOUND in {steps} steps")
                return True
            elif value < node.value:
                print(f"  search({value})  →  go left  (current: {node.value})")
                node = node.left
            else:
                print(f"  search({value})  →  go right (current: {node.value})")
                node = node.right
        print(f"  search({value})  →  NOT FOUND")
        return False

    def inorder(self) -> list:
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

    def preorder(self) -> list:
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.value)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self) -> list:
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.value)

    def height(self) -> int:
        return self._height(self.root)

    def _height(self, node) -> int:
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))


# ═══════════════════════════════════════════════════════════════
#  DEMO RUNNER
# ═══════════════════════════════════════════════════════════════

DIVIDER = "─" * 55

def run_sorting_demo():
    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"\n  Input: {data}")

    print(f"\n{DIVIDER}")
    print("  BUBBLE SORT")
    print(DIVIDER)
    sorted_arr, comps = bubble_sort(data)
    print(f"  Result: {sorted_arr}  ({comps} comparisons)")

    print(f"\n{DIVIDER}")
    print("  INSERTION SORT")
    print(DIVIDER)
    sorted_arr, comps = insertion_sort(data)
    print(f"  Result: {sorted_arr}  ({comps} comparisons)")

    print(f"\n{DIVIDER}")
    print("  MERGE SORT")
    print(DIVIDER)
    sorted_arr = merge_sort(data)
    print(f"  Result: {sorted_arr}")

    print(f"\n{DIVIDER}")
    print("  QUICK SORT")
    print(DIVIDER)
    sorted_arr = quick_sort(data)
    print(f"  Result: {sorted_arr}")


def run_searching_demo():
    data = [11, 12, 22, 25, 34, 64, 90]  # sorted for binary search
    target = 25
    print(f"\n  Array: {data}  |  Target: {target}")

    print(f"\n{DIVIDER}")
    print("  LINEAR SEARCH")
    print(DIVIDER)
    idx = linear_search(data, target)
    print(f"  Found at index: {idx}")

    print(f"\n{DIVIDER}")
    print("  BINARY SEARCH")
    print(DIVIDER)
    idx = binary_search(data, target)
    print(f"  Found at index: {idx}")


def run_stack_demo():
    print(f"\n{DIVIDER}")
    print("  STACK (LIFO — Last In First Out)")
    print(DIVIDER)
    s = Stack(max_size=5)
    for val in [10, 20, 30, 40]:
        s.push(val)
    s.peek() and print(f"  peek()  →  {s.peek()}")
    s.pop()
    s.pop()
    print(f"  Size: {s.size()}")


def run_queue_demo():
    print(f"\n{DIVIDER}")
    print("  QUEUE (FIFO — First In First Out)")
    print(DIVIDER)
    q = Queue(max_size=5)
    for val in ["Alice", "Bob", "Charlie", "Diana"]:
        q.enqueue(val)
    q.dequeue()
    q.dequeue()
    print(f"  Front of queue: {q.peek()}")


def run_bst_demo():
    print(f"\n{DIVIDER}")
    print("  BINARY SEARCH TREE")
    print(DIVIDER)
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    print("  Inserting:", values)
    for v in values:
        bst.insert(v)

    print(f"\n  In-order   (sorted): {bst.inorder()}")
    print(f"  Pre-order  (root first): {bst.preorder()}")
    print(f"  Post-order (root last): {bst.postorder()}")
    print(f"  Height: {bst.height()}")

    print()
    bst.search(40)
    bst.search(55)


def main():
    print("=" * 55)
    print("  ALGORITHMS & DATA STRUCTURES")
    print("=" * 55)

    while True:
        print("\n  1. Sorting algorithms (Bubble, Insertion, Merge, Quick)")
        print("  2. Searching algorithms (Linear, Binary)")
        print("  3. Stack demo")
        print("  4. Queue demo")
        print("  5. Binary Search Tree demo")
        print("  6. Run all demos")
        print("  Q. Quit")
        choice = input("\n  Select: ").strip().upper()

        if choice == "1":
            run_sorting_demo()
        elif choice == "2":
            run_searching_demo()
        elif choice == "3":
            run_stack_demo()
        elif choice == "4":
            run_queue_demo()
        elif choice == "5":
            run_bst_demo()
        elif choice == "6":
            run_sorting_demo()
            run_searching_demo()
            run_stack_demo()
            run_queue_demo()
            run_bst_demo()
        elif choice == "Q":
            break
        else:
            print("  Invalid option.")


if __name__ == "__main__":
    main()
