# Algorithms & Data Structures

**Step-by-step traces of sorting, searching, and fundamental data structures — implemented from scratch in Python.**

---

## What Is This?

A runnable, interactive reference implementation of the core algorithms and data structures from the OCR A-Level Computer Science specification (Section 2.3). Every algorithm prints a step-by-step trace so you can follow exactly what's happening at each stage.

---

## How to Run

```bash
python algorithms.py
```

No dependencies — Python standard library only.

---

## What's Included

### Sorting

| Algorithm | Time (avg) | Time (worst) | Space | Notes |
|---|---|---|---|---|
| Bubble Sort | O(n²) | O(n²) | O(1) | Early-exit optimisation included |
| Insertion Sort | O(n²) | O(n²) | O(1) | Efficient on nearly-sorted data |
| Merge Sort | O(n log n) | O(n log n) | O(n) | Divide and conquer, stable |
| Quick Sort | O(n log n) | O(n²) | O(log n) | In-place partitioning |

Each sort prints its intermediate states so you can watch it work:
```
Bubble Sort — Input: [64, 34, 25, 12, 22, 11, 90]
  Pass 1: [34, 25, 12, 22, 11, 64, 90]
  Pass 2: [25, 12, 22, 11, 34, 64, 90]
  ...
```

### Searching

| Algorithm | Time | Requirement |
|---|---|---|
| Linear Search | O(n) | Unsorted or sorted |
| Binary Search | O(log n) | **Sorted input required** |

Binary search prints each midpoint comparison, showing the halving of the search space.

### Data Structures

#### Stack (LIFO)
```
push(10) → [10] ← top
push(20) → [10 | 20] ← top
pop()    → 20   | [10] ← top
```
Supports: `push`, `pop`, `peek`, `is_empty`, `size`, optional max capacity with overflow detection.

#### Queue (FIFO)
```
enqueue(Alice)  → front → [Alice] ← rear
enqueue(Bob)    → front → [Alice | Bob] ← rear
dequeue()       → Alice | front → [Bob] ← rear
```
Supports: `enqueue`, `dequeue`, `peek`, `is_empty`, `size`, optional max capacity.

#### Binary Search Tree
Traces every insert and search with the path taken through the tree:
```
insert(50) → root
insert(30) → left of 50
insert(70) → right of 50
insert(20) → left of 50 → left
```
Supports:
- `insert` — with duplicate detection
- `search` — with step count
- `inorder` — returns sorted output
- `preorder` / `postorder` — all three traversal orders
- `height` — tree height

---

## Example Output — Binary Search Tree

```
Values inserted: [50, 30, 70, 20, 40, 60, 80]

In-order   (sorted):    [20, 30, 40, 50, 60, 70, 80]
Pre-order  (root first): [50, 30, 20, 40, 70, 60, 80]
Post-order (root last):  [20, 40, 30, 60, 80, 70, 50]
Height: 3

search(40) → go left (current: 50) → go right (current: 30) → FOUND in 3 steps
search(55) → go right (current: 50) → go left (current: 70) → NOT FOUND
```

---

## What This Demonstrates

- **Algorithm design** — implementation of all major sorting and searching algorithms
- **Time and space complexity analysis** — comparison table with Big O notation
- **Data structures** — Stack, Queue, BST with clean OOP design
- **Recursion** — merge sort, quick sort, BST insert/search/traversal all use recursion
- **Tracing** — every function prints its working, not just the result
- **Python OOP** — `Stack`, `Queue`, `BinarySearchTree`, `BSTNode` classes with encapsulation

---

*Python 3.9+. No external dependencies. Covers OCR H446 Section 2.3 — Algorithms.*
