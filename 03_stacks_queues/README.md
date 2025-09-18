# Stacks & Queues - Topic 3

This directory contains implementations and exercises for stack and queue data structures, following the [W3Schools DSA Tutorial](https://www.w3schools.com/dsa/index.php).

## Learning Objectives

By the end of this topic, you will be able to:
- Understand stack and queue fundamentals
- Implement both data structures using arrays and linked lists
- Apply stacks and queues to solve real-world problems
- Understand LIFO vs FIFO principles
- Analyze time and space complexity

## Topics Covered

### Part 1: Stack Implementation 🚧 (IN PROGRESS)
- [ ] Stack using Python list
- [ ] Stack using linked list
- [ ] Basic operations (push, pop, peek, isEmpty)
- [ ] Stack applications

### Part 2: Queue Implementation
- [ ] Queue using Python list
- [ ] Queue using linked list
- [ ] Basic operations (enqueue, dequeue, peek, isEmpty)
- [ ] Queue applications

### Part 3: Advanced Variations
- [ ] Circular queue
- [ ] Priority queue
- [ ] Deque (double-ended queue)
- [ ] Stack and queue combinations

### Part 4: Real-World Applications
- [ ] Expression evaluation
- [ ] Function call stack simulation
- [ ] BFS and DFS algorithms
- [ ] Undo/redo functionality

## 🎯 YOUR TASK: Complete Part 1 - Stack Implementation

### **What You Need to Do:**

1. **Create the stack implementation file** (`03_stacks_queues/stack.py`)
2. **Write comprehensive tests** (`03_stacks_queues/tests/test_stack.py`)
3. **Test your implementation**
4. **Commit and push to your branch**

### **Step-by-Step Instructions:**

#### **Step 1: Create the Stack File**
Create `03_stacks_queues/stack.py` with these components:

**Required Class:**
- `Stack` class using Python list

**Required Methods:**
- `__init__()` - Initialize empty stack
- `is_empty()` - Check if stack is empty
- `push(item)` - Add item to top of stack
- `pop()` - Remove and return top item
- `peek()` - Return top item without removing
- `size()` - Return number of items
- `display()` - Print stack contents

**Key Requirements:**
- Handle empty stack errors properly
- Include docstrings with time/space complexity
- Follow LIFO (Last In, First Out) principle

#### **Step 2: Write Tests**
Create `03_stacks_queues/tests/test_stack.py` with test cases for:
- Normal operations (push, pop, peek)
- Edge cases (empty stack operations)
- Error handling (pop from empty stack)

#### **Step 3: Test Your Code**
```bash
# Run your stack implementation
python 03_stacks_queues/stack.py

# Run your tests
python -m pytest 03_stacks_queues/tests/test_stack.py -v
```

#### **Step 4: Commit and Push**
```bash
git checkout -b topic-3-stacks-queues-stack
git add .
git commit -m "feat: implement stack data structure

- Add Stack class with all basic operations
- Implement push, pop, peek, isEmpty methods
- Add comprehensive test cases
- Handle empty stack error conditions"

git push origin topic-3-stacks-queues-stack
```

### **Success Criteria:**
- ✅ All methods work correctly
- ✅ Tests pass (including edge cases)
- ✅ Proper error handling for empty stack
- ✅ Docstrings include complexity analysis
- ✅ Ready for PR creation

## Time Complexity Reference

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Push | O(1) | O(1) |
| Pop | O(1) | O(1) |
| Peek | O(1) | O(1) |
| isEmpty | O(1) | O(1) |
| Size | O(1) | O(1) |

## Learning Resources

- [W3Schools DSA Stacks](https://www.w3schools.com/dsa/dsa_intro_stacks.php)
- [W3Schools DSA Queues](https://www.w3schools.com/dsa/dsa_intro_queues.php)
