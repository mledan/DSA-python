# Trees - Topic 5

This directory contains implementations and exercises for tree data structures, following the [W3Schools DSA Tutorial](https://www.w3schools.com/dsa/index.php).

## Learning Objectives

By the end of this topic, you will be able to:
- Understand tree fundamentals and terminology
- Implement binary trees and binary search trees
- Perform tree traversals (pre-order, in-order, post-order)
- Understand balanced trees (AVL trees)
- Apply trees to solve hierarchical problems

## Topics Covered

### Part 1: Binary Tree Basics 🚧 (IN PROGRESS)
- [ ] Tree node implementation
- [ ] Binary tree structure
- [ ] Tree traversal algorithms
- [ ] Tree height and depth

### Part 2: Binary Search Trees
- [ ] BST insertion and deletion
- [ ] BST search operations
- [ ] BST validation
- [ ] BST applications

### Part 3: Tree Traversals
- [ ] Pre-order traversal
- [ ] In-order traversal
- [ ] Post-order traversal
- [ ] Level-order traversal (BFS)

### Part 4: Balanced Trees
- [ ] AVL tree implementation
- [ ] Tree rotation operations
- [ ] Balance factor calculation
- [ ] Self-balancing properties

## 🎯 YOUR TASK: Complete Part 1 - Binary Tree Basics

### **What You Need to Do:**

1. **Create the binary tree file** (`05_trees/binary_tree.py`)
2. **Write comprehensive tests** (`05_trees/tests/test_binary_tree.py`)
3. **Test your implementation**
4. **Commit and push to your branch**

### **Step-by-Step Instructions:**

#### **Step 1: Create the Binary Tree File**
Create `05_trees/binary_tree.py` with these components:

**Required Classes:**
- `TreeNode` class with data, left, right attributes
- `BinaryTree` class with root pointer

**Required Methods:**
- `__init__()` - Initialize empty tree
- `insert(data)` - Insert new node
- `search(data)` - Find node with given data
- `height()` - Calculate tree height
- `size()` - Count total nodes
- `is_empty()` - Check if tree is empty
- `display()` - Print tree structure

**Key Requirements:**
- Handle empty tree operations
- Include docstrings with time/space complexity
- Implement basic tree operations

#### **Step 2: Write Tests**
Create `05_trees/tests/test_binary_tree.py` with test cases for:
- Normal operations (insert, search)
- Edge cases (empty tree, single node)
- Tree properties (height, size)

#### **Step 3: Test Your Code**
```bash
# Run your binary tree implementation
python 05_trees/binary_tree.py

# Run your tests
python -m pytest 05_trees/tests/test_binary_tree.py -v
```

#### **Step 4: Commit and Push**
```bash
git checkout -b topic-5-trees-binary-basic
git add .
git commit -m "feat: implement basic binary tree

- Add TreeNode and BinaryTree classes
- Implement insert, search, height, size methods
- Add comprehensive test cases
- Handle empty tree operations"

git push origin topic-5-trees-binary-basic
```

### **Success Criteria:**
- ✅ All methods work correctly
- ✅ Tests pass (including edge cases)
- ✅ Proper tree structure maintenance
- ✅ Docstrings include complexity analysis
- ✅ Ready for PR creation

## Time Complexity Reference

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Insert | O(log n) | O(log n) |
| Search | O(log n) | O(log n) |
| Delete | O(log n) | O(log n) |
| Traversal | O(n) | O(h) |

## Learning Resources

- [W3Schools DSA Trees](https://www.w3schools.com/dsa/dsa_intro_trees.php)
- [W3Schools DSA Binary Trees](https://www.w3schools.com/dsa/dsa_intro_binarytrees.php)
- [W3Schools DSA Tree Traversals](https://www.w3schools.com/dsa/dsa_intro_treetraversal.php)
- [W3Schools DSA Binary Search Trees](https://www.w3schools.com/dsa/dsa_intro_binarysearchtrees.php)
