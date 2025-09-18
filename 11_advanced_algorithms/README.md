# Advanced Algorithms - Topic 11

This directory contains implementations and exercises for advanced algorithmic techniques, following the [W3Schools DSA Tutorial](https://www.w3schools.com/dsa/index.php).

## Learning Objectives

By the end of this topic, you will be able to:
- Understand dynamic programming concepts
- Implement greedy algorithms
- Apply memoization and tabulation
- Solve complex optimization problems
- Understand algorithm design patterns

## Topics Covered

### Part 1: Dynamic Programming 🚧 (IN PROGRESS)
- [ ] Dynamic programming fundamentals
- [ ] Memoization technique
- [ ] Tabulation technique
- [ ] Classic DP problems

### Part 2: Greedy Algorithms
- [ ] Greedy algorithm principles
- [ ] Activity selection problem
- [ ] Huffman coding
- [ ] Minimum spanning tree (greedy approach)

### Part 3: Advanced DP Problems
- [ ] 0/1 Knapsack problem
- [ ] Longest common subsequence
- [ ] Edit distance
- [ ] Coin change problem

### Part 4: Algorithm Design Patterns
- [ ] Divide and conquer
- [ ] Backtracking
- [ ] Branch and bound
- [ ] Approximation algorithms

## 🎯 YOUR TASK: Complete Part 1 - Dynamic Programming

### **What You Need to Do:**

1. **Create the DP file** (`11_advanced_algorithms/dynamic_programming.py`)
2. **Write comprehensive tests** (`11_advanced_algorithms/tests/test_dp.py`)
3. **Test your implementation**
4. **Commit and push to your branch**

### **Step-by-Step Instructions:**

#### **Step 1: Create the Dynamic Programming File**
Create `11_advanced_algorithms/dynamic_programming.py` with these components:

**Required Functions:**
- `fibonacci_memoization(n)` - Fibonacci with memoization
- `fibonacci_tabulation(n)` - Fibonacci with tabulation
- `longest_common_subsequence(str1, str2)` - LCS problem
- `edit_distance(str1, str2)` - Edit distance problem
- `coin_change(coins, amount)` - Coin change problem

**Required Classes:**
- `DynamicProgramming` class for DP utilities

**Key Requirements:**
- Implement both memoization and tabulation
- Include docstrings with complexity analysis
- Handle edge cases properly
- Show time/space tradeoffs

#### **Step 2: Write Tests**
Create `11_advanced_algorithms/tests/test_dp.py` with test cases for:
- Normal DP problem solutions
- Edge cases (empty inputs, boundary values)
- Performance comparisons

#### **Step 3: Test Your Code**
```bash
# Run your DP implementation
python 11_advanced_algorithms/dynamic_programming.py

# Run your tests
python -m pytest 11_advanced_algorithms/tests/test_dp.py -v
```

#### **Step 4: Commit and Push**
```bash
git checkout -b topic-11-advanced-algorithms-dp
git add .
git commit -m "feat: implement dynamic programming algorithms

- Add memoization and tabulation techniques
- Implement classic DP problems (Fibonacci, LCS, Edit Distance)
- Add coin change problem solution
- Include performance comparisons"

git push origin topic-11-advanced-algorithms-dp
```

### **Success Criteria:**
- ✅ All DP algorithms work correctly
- ✅ Tests pass (including edge cases)
- ✅ Proper memoization and tabulation implementation
- ✅ Docstrings include complexity analysis
- ✅ Ready for PR creation

## Time Complexity Reference

| Problem | Naive | Memoization | Tabulation |
|---------|-------|-------------|------------|
| Fibonacci | O(2ⁿ) | O(n) | O(n) |
| LCS | O(2ⁿ) | O(mn) | O(mn) |
| Edit Distance | O(3ⁿ) | O(mn) | O(mn) |
| Coin Change | O(amountⁿ) | O(amount × coins) | O(amount × coins) |

## Learning Resources

- [W3Schools DSA Dynamic Programming](https://www.w3schools.com/dsa/dsa_intro_dynamicprogramming.php)
- [W3Schools DSA Greedy Algorithms](https://www.w3schools.com/dsa/dsa_intro_greedyalgorithms.php)
- [W3Schools DSA Memoization](https://www.w3schools.com/dsa/dsa_intro_memoization.php)
- [W3Schools DSA Tabulation](https://www.w3schools.com/dsa/dsa_intro_tabulation.php)
- [W3Schools DSA 0/1 Knapsack](https://www.w3schools.com/dsa/dsa_intro_knapsack.php)
- [W3Schools DSA Huffman Coding](https://www.w3schools.com/dsa/dsa_intro_huffmancoding.php)
- [W3Schools DSA Traveling Salesman](https://www.w3schools.com/dsa/dsa_intro_travelingsalesman.php)
