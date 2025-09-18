# Arrays - Topic 1

This directory contains implementations and exercises for array-based data structures and algorithms, following the [W3Schools DSA Tutorial](https://www.w3schools.com/dsa/index.php).

## Learning Objectives

By the end of this topic, you will be able to:
- Understand array fundamentals and operations
- Implement basic array algorithms (min, max, sum, average)
- Analyze time and space complexity of array operations
- Apply arrays to solve simple problems

## Topics Covered

### Part 1: Basic Array Operations 🚧 (IN PROGRESS)
- [ ] Array creation and initialization
- [ ] Finding minimum and maximum values
- [ ] Calculating sum and average
- [ ] Basic array traversal

### Part 2: Sorting Algorithms (Coming Next)
- [ ] Bubble Sort
- [ ] Selection Sort  
- [ ] Insertion Sort
- [ ] Quick Sort
- [ ] Merge Sort

### Part 3: Searching Algorithms
- [ ] Linear Search
- [ ] Binary Search
- [ ] Search optimization techniques

### Part 4: Advanced Array Problems
- [ ] Two-pointer technique
- [ ] Sliding window problems
- [ ] Array manipulation challenges

## 🎯 YOUR TASK: Complete Part 1 - Basic Array Operations

### **What You Need to Do:**

1. **Create the basic operations file** (`01_arrays/basic_operations.py`)
2. **Write comprehensive tests** (`01_arrays/tests/test_basic_operations.py`)
3. **Test your implementation**
4. **Commit and push to your branch**

### **Step-by-Step Instructions:**

#### **Step 1: Create the Basic Operations File**
Create `01_arrays/basic_operations.py` with these functions:

**Required Functions:**
- `create_sample_array()` - Returns `[7, 12, 9, 4, 11]` (W3Schools example)
- `find_minimum(arr)` - Find smallest value in array
- `find_maximum(arr)` - Find largest value in array  
- `calculate_sum(arr)` - Sum all elements
- `calculate_average(arr)` - Average of all elements
- `count_elements(arr, target)` - Count occurrences of target
- `reverse_array(arr)` - Reverse array in-place
- `display_array(arr, title)` - Pretty print array

**Key Requirements:**
- Include docstrings with time/space complexity
- Handle edge cases (empty arrays, single elements)
- Follow the W3Schools example exactly for `find_minimum`

#### **Step 2: Write Tests**
Create `01_arrays/tests/test_basic_operations.py` with test cases for:
- Normal cases (your sample array)
- Edge cases (empty array, single element)
- Boundary cases (negative numbers, duplicates)

#### **Step 3: Test Your Code**
```bash
# Run your basic operations
python 01_arrays/basic_operations.py

# Run your tests
python -m pytest 01_arrays/tests/test_basic_operations.py -v
```

#### **Step 4: Commit and Push**
```bash
git add .
git commit -m "feat: implement basic array operations

- Add find_minimum, find_maximum functions
- Add calculate_sum, calculate_average functions  
- Add count_elements, reverse_array functions
- Include comprehensive test cases
- Follow W3Schools DSA tutorial examples"

git push origin topic-1-arrays-basic-operations
```

### **Success Criteria:**
- ✅ All functions work correctly
- ✅ Tests pass (including edge cases)
- ✅ Code follows Python best practices
- ✅ Docstrings include complexity analysis
- ✅ Ready for PR creation

## Files Structure

```
01_arrays/
├── README.md                    # This file
├── basic_operations.py          # Part 1: Basic array operations
├── sorting_algorithms.py        # Part 2: All sorting algorithms
├── searching_algorithms.py      # Part 3: Search algorithms
├── advanced_problems.py         # Part 4: Complex array problems
├── exercises.py                 # Practice exercises
└── tests/
    ├── test_basic_operations.py
    ├── test_sorting.py
    ├── test_searching.py
    └── test_advanced.py
```

## Time Complexity Reference

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Access | O(1) | O(1) |
| Search | O(n) | O(1) |
| Insertion | O(n) | O(1) |
| Deletion | O(n) | O(1) |
| Min/Max | O(n) | O(1) |
| Sum/Average | O(n) | O(1) |

## Learning Resources

- [W3Schools DSA Arrays](https://www.w3schools.com/dsa/dsa_intro_arrays.php)
- [W3Schools Sorting Algorithms](https://www.w3schools.com/dsa/dsa_intro_sorting.php)
- [W3Schools Linear Search](https://www.w3schools.com/dsa/dsa_intro_linearsearch.php)
- [W3Schools Binary Search](https://www.w3schools.com/dsa/dsa_intro_binarysearch.php)
