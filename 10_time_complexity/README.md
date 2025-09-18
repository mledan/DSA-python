# Time Complexity - Topic 10

This directory contains implementations and exercises for understanding time complexity analysis, following the [W3Schools DSA Tutorial](https://www.w3schools.com/dsa/index.php).

## Learning Objectives

By the end of this topic, you will be able to:
- Understand Big O notation and complexity analysis
- Analyze time complexity of different algorithms
- Compare algorithm performance
- Understand space-time tradeoffs
- Apply complexity analysis to algorithm selection

## Topics Covered

### Part 1: Big O Notation Basics 🚧 (IN PROGRESS)
- [ ] Big O notation explanation
- [ ] Common complexity classes
- [ ] Best, average, and worst case analysis
- [ ] Complexity comparison examples

### Part 2: Sorting Algorithm Analysis
- [ ] Bubble sort complexity
- [ ] Selection sort complexity
- [ ] Insertion sort complexity
- [ ] Quick sort complexity
- [ ] Merge sort complexity

### Part 3: Searching Algorithm Analysis
- [ ] Linear search complexity
- [ ] Binary search complexity
- [ ] Hash table operations
- [ ] Tree operations

### Part 4: Advanced Complexity Analysis
- [ ] Space complexity analysis
- [ ] Amortized analysis
- [ ] Recursive algorithm analysis
- [ ] Dynamic programming complexity

## 🎯 YOUR TASK: Complete Part 1 - Big O Notation Basics

### **What You Need to Do:**

1. **Create the complexity analysis file** (`10_time_complexity/big_o_analysis.py`)
2. **Write comprehensive examples** (`10_time_complexity/examples.py`)
3. **Create performance tests** (`10_time_complexity/performance_tests.py`)
4. **Commit and push to your branch**

### **Step-by-Step Instructions:**

#### **Step 1: Create the Big O Analysis File**
Create `10_time_complexity/big_o_analysis.py` with these components:

**Required Functions:**
- `constant_time_example(n)` - O(1) example
- `linear_time_example(n)` - O(n) example
- `quadratic_time_example(n)` - O(n²) example
- `logarithmic_time_example(n)` - O(log n) example
- `exponential_time_example(n)` - O(2ⁿ) example

**Required Classes:**
- `ComplexityAnalyzer` class for performance testing

**Key Requirements:**
- Include docstrings with complexity analysis
- Provide clear examples for each complexity class
- Include timing measurements
- Explain the mathematical reasoning

#### **Step 2: Create Examples File**
Create `10_time_complexity/examples.py` with:
- Real-world algorithm examples
- Complexity comparison charts
- Performance visualization

#### **Step 3: Create Performance Tests**
Create `10_time_complexity/performance_tests.py` with:
- Timing different input sizes
- Complexity verification
- Performance comparison

#### **Step 4: Test Your Code**
```bash
# Run your complexity analysis
python 10_time_complexity/big_o_analysis.py

# Run your examples
python 10_time_complexity/examples.py

# Run performance tests
python 10_time_complexity/performance_tests.py
```

#### **Step 5: Commit and Push**
```bash
git checkout -b topic-10-time-complexity-big-o
git add .
git commit -m "feat: implement Big O notation analysis

- Add examples for all major complexity classes
- Implement performance testing framework
- Add complexity comparison tools
- Include real-world algorithm examples"

git push origin topic-10-time-complexity-big-o
```

### **Success Criteria:**
- ✅ All complexity examples work correctly
- ✅ Performance tests demonstrate expected behavior
- ✅ Clear explanations of complexity analysis
- ✅ Ready for PR creation

## Complexity Classes Reference

| Complexity | Notation | Example | Description |
|------------|----------|---------|-------------|
| Constant | O(1) | Array access | Time doesn't depend on input size |
| Logarithmic | O(log n) | Binary search | Time grows logarithmically |
| Linear | O(n) | Linear search | Time grows linearly with input |
| Linearithmic | O(n log n) | Merge sort | Time grows as n times log n |
| Quadratic | O(n²) | Bubble sort | Time grows quadratically |
| Exponential | O(2ⁿ) | Recursive Fibonacci | Time grows exponentially |

## Learning Resources

- [W3Schools Time Complexity](https://www.w3schools.com/dsa/dsa_intro_timecomplexity.php)
- [W3Schools Bubble Sort Complexity](https://www.w3schools.com/dsa/dsa_intro_timecomplexity_bubblesort.php)
- [W3Schools Selection Sort Complexity](https://www.w3schools.com/dsa/dsa_intro_timecomplexity_selectionsort.php)
- [W3Schools Insertion Sort Complexity](https://www.w3schools.com/dsa/dsa_intro_timecomplexity_insertionsort.php)
- [W3Schools Quick Sort Complexity](https://www.w3schools.com/dsa/dsa_intro_timecomplexity_quicksort.php)
- [W3Schools Counting Sort Complexity](https://www.w3schools.com/dsa/dsa_intro_timecomplexity_countingsort.php)
- [W3Schools Radix Sort Complexity](https://www.w3schools.com/dsa/dsa_intro_timecomplexity_radixsort.php)
- [W3Schools Merge Sort Complexity](https://www.w3schools.com/dsa/dsa_intro_timecomplexity_mergesort.php)
- [W3Schools Linear Search Complexity](https://www.w3schools.com/dsa/dsa_intro_timecomplexity_linearsearch.php)
- [W3Schools Binary Search Complexity](https://www.w3schools.com/dsa/dsa_intro_timecomplexity_binarysearch.php)
