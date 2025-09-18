# Linked Lists - Topic 2

This directory contains implementations and exercises for linked list data structures, following the [W3Schools DSA Tutorial](https://www.w3schools.com/dsa/index.php).

## Learning Objectives

By the end of this topic, you will be able to:
- Understand linked list fundamentals and memory representation
- Implement singly, doubly, and circular linked lists
- Perform all basic operations (insert, delete, search, traverse)
- Compare linked lists vs arrays
- Apply linked lists to solve problems

## Topics Covered

### Part 1: Singly Linked Lists 🚧 (IN PROGRESS)
- [ ] Node class implementation
- [ ] Basic operations (insert, delete, search)
- [ ] Traversal and display
- [ ] Size and empty checks

### Part 2: Doubly Linked Lists
- [ ] Node with previous pointer
- [ ] Bidirectional traversal
- [ ] Insert/delete operations
- [ ] Advantages over singly linked lists

### Part 3: Circular Linked Lists
- [ ] Circular structure implementation
- [ ] Special traversal considerations
- [ ] Insert/delete at any position
- [ ] Applications and use cases

### Part 4: Advanced Operations
- [ ] Merge two linked lists
- [ ] Detect cycles
- [ ] Reverse linked list
- [ ] Find middle element

## 🎯 YOUR TASK: Complete Part 1 - Singly Linked Lists

### **What You Need to Do:**

1. **Create the singly linked list file** (`02_linked_lists/singly_linked_list.py`)
2. **Write comprehensive tests** (`02_linked_lists/tests/test_singly_linked_list.py`)
3. **Test your implementation**
4. **Commit and push to your branch**

### **Step-by-Step Instructions:**

#### **Step 1: Create the Singly Linked List File**
Create `02_linked_lists/singly_linked_list.py` with these components:

**Required Classes:**
- `Node` class with `data` and `next` attributes
- `SinglyLinkedList` class with head pointer

**Required Methods:**
- `__init__()` - Initialize empty list
- `is_empty()` - Check if list is empty
- `get_size()` - Return number of nodes
- `prepend(data)` - Add node at beginning
- `append(data)` - Add node at end
- `insert_at(index, data)` - Insert at specific position
- `delete_first()` - Remove first node
- `delete_last()` - Remove last node
- `delete_at(index)` - Remove at specific position
- `search(data)` - Find node with given data
- `display()` - Print all elements
- `reverse()` - Reverse the linked list

**Key Requirements:**
- Handle edge cases (empty list, single node, invalid indices)
- Include docstrings with time/space complexity
- Use proper error handling for invalid operations

#### **Step 2: Write Tests**
Create `02_linked_lists/tests/test_singly_linked_list.py` with test cases for:
- Normal operations (insert, delete, search)
- Edge cases (empty list, single node)
- Error cases (invalid indices, operations on empty list)

#### **Step 3: Test Your Code**
```bash
# Run your linked list implementation
python 02_linked_lists/singly_linked_list.py

# Run your tests
python -m pytest 02_linked_lists/tests/test_singly_linked_list.py -v
```

#### **Step 4: Commit and Push**
```bash
git checkout -b topic-2-linked-lists-singly
git add .
git commit -m "feat: implement singly linked list

- Add Node and SinglyLinkedList classes
- Implement all basic operations (insert, delete, search)
- Add comprehensive test cases
- Handle edge cases and error conditions"

git push origin topic-2-linked-lists-singly
```

### **Success Criteria:**
- ✅ All methods work correctly
- ✅ Tests pass (including edge cases)
- ✅ Proper error handling for invalid operations
- ✅ Docstrings include complexity analysis
- ✅ Ready for PR creation

## Time Complexity Reference

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Access | O(n) | O(1) |
| Search | O(n) | O(1) |
| Insertion (beginning) | O(1) | O(1) |
| Insertion (end) | O(n) | O(1) |
| Insertion (middle) | O(n) | O(1) |
| Deletion (beginning) | O(1) | O(1) |
| Deletion (end) | O(n) | O(1) |
| Deletion (middle) | O(n) | O(1) |

## Learning Resources

- [W3Schools DSA Linked Lists](https://www.w3schools.com/dsa/dsa_intro_linkedlists.php)
- [W3Schools Linked Lists in Memory](https://www.w3schools.com/dsa/dsa_intro_linkedlists_memory.php)
- [W3Schools Linked List Types](https://www.w3schools.com/dsa/dsa_intro_linkedlists_types.php)
- [W3Schools Linked List Operations](https://www.w3schools.com/dsa/dsa_intro_linkedlists_operations.php)
