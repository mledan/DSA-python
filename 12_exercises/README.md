# Exercises - Topic 12

This directory contains practice exercises and coding challenges to reinforce your DSA knowledge, following the [W3Schools DSA Tutorial](https://www.w3schools.com/dsa/index.php).

## Learning Objectives

By the end of this topic, you will be able to:
- Apply DSA concepts to solve real-world problems
- Practice coding interview questions
- Implement complex algorithms from scratch
- Optimize solutions for better performance
- Build confidence in problem-solving

## Topics Covered

### Part 1: Array Exercises 🚧 (IN PROGRESS)
- [ ] Two Sum problem
- [ ] Maximum Subarray (Kadane's Algorithm)
- [ ] Rotate Array
- [ ] Product of Array Except Self

### Part 2: Linked List Exercises
- [ ] Reverse Linked List
- [ ] Merge Two Sorted Lists
- [ ] Detect Cycle in Linked List
- [ ] Remove Nth Node From End

### Part 3: Tree and Graph Exercises
- [ ] Binary Tree Level Order Traversal
- [ ] Validate Binary Search Tree
- [ ] Course Schedule (Topological Sort)
- [ ] Number of Islands

### Part 4: Dynamic Programming Exercises
- [ ] Climbing Stairs
- [ ] House Robber
- [ ] Longest Increasing Subsequence
- [ ] Word Break

## 🎯 YOUR TASK: Complete Part 1 - Array Exercises

### **What You Need to Do:**

1. **Create the exercises file** (`12_exercises/array_exercises.py`)
2. **Write comprehensive tests** (`12_exercises/tests/test_array_exercises.py`)
3. **Test your implementation**
4. **Commit and push to your branch**

### **Step-by-Step Instructions:**

#### **Step 1: Create the Array Exercises File**
Create `12_exercises/array_exercises.py` with these components:

**Required Functions:**
- `two_sum(nums, target)` - Find two numbers that add up to target
- `max_subarray(nums)` - Find maximum sum of contiguous subarray
- `rotate_array(nums, k)` - Rotate array to the right by k steps
- `product_except_self(nums)` - Return array where each element is product of all others

**Key Requirements:**
- Include docstrings with complexity analysis
- Handle edge cases properly
- Optimize for time and space complexity
- Follow coding interview best practices

#### **Step 2: Write Tests**
Create `12_exercises/tests/test_array_exercises.py` with test cases for:
- Normal problem solutions
- Edge cases (empty arrays, single elements)
- Performance verification

#### **Step 3: Test Your Code**
```bash
# Run your exercises
python 12_exercises/array_exercises.py

# Run your tests
python -m pytest 12_exercises/tests/test_array_exercises.py -v
```

#### **Step 4: Commit and Push**
```bash
git checkout -b topic-12-exercises-arrays
git add .
git commit -m "feat: implement array coding exercises

- Add Two Sum problem solution
- Implement Maximum Subarray (Kadane's Algorithm)
- Add Rotate Array solution
- Implement Product of Array Except Self"

git push origin topic-12-exercises-arrays
```

### **Success Criteria:**
- ✅ All exercises solved correctly
- ✅ Tests pass (including edge cases)
- ✅ Optimal time and space complexity
- ✅ Clean, readable code
- ✅ Ready for PR creation

## Exercise Difficulty Levels

| Level | Description | Examples |
|-------|-------------|----------|
| Easy | Basic DSA concepts | Two Sum, Valid Parentheses |
| Medium | Multiple concepts combined | 3Sum, Longest Substring |
| Hard | Complex algorithms | Median of Two Sorted Arrays |

## Learning Resources

- [W3Schools DSA Examples](https://www.w3schools.com/dsa/dsa_intro_examples.php)
- [W3Schools DSA Exercises](https://www.w3schools.com/dsa/dsa_intro_exercises.php)
- [LeetCode](https://leetcode.com/) - Practice problems
- [HackerRank](https://www.hackerrank.com/) - Coding challenges
