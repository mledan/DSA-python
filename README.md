# DSA Python Learning Repository

A comprehensive learning repository for Data Structures and Algorithms in Python, following the [W3Schools DSA Tutorial](https://www.w3schools.com/dsa/index.php).

## 🎯 Learning Objectives

This repository is designed to help you master:
- **Data Structures**: Arrays, Linked Lists, Stacks, Queues, Hash Tables, Trees, Graphs
- **Algorithms**: Sorting, Searching, Graph Traversal, Shortest Path, Dynamic Programming
- **Time Complexity**: Understanding Big O notation and algorithm efficiency
- **Problem Solving**: Applying DSA concepts to real-world problems

## 📚 Repository Structure

```
DSA-python/
├── 01_arrays/                 # Array operations and sorting algorithms
├── 02_linked_lists/          # Linked list implementations
├── 03_stacks_queues/         # Stack and queue data structures
├── 04_hash_tables/           # Hash tables, sets, and maps
├── 05_trees/                 # Binary trees, BST, AVL trees
├── 06_graphs/                # Graph representations and traversal
├── 07_shortest_path/         # Dijkstra's, Bellman-Ford algorithms
├── 08_minimum_spanning_tree/ # Prim's and Kruskal's algorithms
├── 09_maximum_flow/          # Ford-Fulkerson, Edmonds-Karp
├── 10_time_complexity/       # Big O analysis and examples
├── 11_advanced_algorithms/   # Dynamic programming, greedy algorithms
├── 12_exercises/             # Practice problems and solutions
├── tests/                    # Unit tests for all implementations
├── utils/                    # Utility functions and helpers
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone <your-repo-url>
   cd DSA-python
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run tests** to verify everything is working:
   ```bash
   pytest tests/
   ```

## 📖 Learning Path

### Phase 1: Fundamentals (Weeks 1-2)
- [ ] **Arrays**: Basic operations, sorting algorithms
- [ ] **Linked Lists**: Singly, doubly, and circular linked lists
- [ ] **Stacks & Queues**: Implementation and applications

### Phase 2: Intermediate (Weeks 3-4)
- [ ] **Hash Tables**: Hash sets, hash maps, collision handling
- [ ] **Trees**: Binary trees, BST, tree traversals
- [ ] **Graphs**: Representation, BFS, DFS

### Phase 3: Advanced (Weeks 5-6)
- [ ] **Shortest Path**: Dijkstra's, Bellman-Ford
- [ ] **Minimum Spanning Tree**: Prim's, Kruskal's
- [ ] **Time Complexity**: Big O analysis

### Phase 4: Expert (Weeks 7-8)
- [ ] **Advanced Algorithms**: Dynamic programming, greedy algorithms
- [ ] **Problem Solving**: LeetCode-style problems
- [ ] **System Design**: Applying DSA to real systems

## 🧪 Testing

Each module includes comprehensive test cases. Run tests using:

```bash
# Run all tests
pytest

# Run tests for specific module
pytest tests/test_basic_arrays.py

# Run with coverage
pytest --cov=.
```

## 📊 Performance Analysis

Use the included performance utilities to analyze algorithm efficiency:

```python
from utils.performance_timer import time_function, compare_algorithms

@time_function
def my_algorithm(data):
    # Your algorithm here
    pass
```

## 🎯 Practice Exercises

Each topic includes:
- **Theory**: Conceptual understanding
- **Implementation**: Working code examples
- **Exercises**: Practice problems with solutions
- **Tests**: Unit tests to verify correctness

## 📚 Additional Resources

- [W3Schools DSA Tutorial](https://www.w3schools.com/dsa/index.php) - Primary learning resource
- [LeetCode](https://leetcode.com/) - Practice problems
- [GeeksforGeeks](https://www.geeksforgeeks.org/) - Additional explanations
- [Big O Cheat Sheet](https://www.bigocheatsheet.com/) - Time complexity reference

## 🤝 Contributing

This is a personal learning repository, but feel free to:
- Add more examples
- Improve existing implementations
- Add more test cases
- Suggest better algorithms

## 📝 Progress Tracking

Use this checklist to track your learning progress:

- [ ] Arrays and Sorting Algorithms
- [ ] Linked Lists
- [ ] Stacks and Queues
- [ ] Hash Tables
- [ ] Trees and Binary Search Trees
- [ ] Graph Algorithms
- [ ] Shortest Path Algorithms
- [ ] Minimum Spanning Tree
- [ ] Time Complexity Analysis
- [ ] Advanced Algorithms

## 🏆 Goals

By the end of this learning journey, you should be able to:
1. Implement all major data structures from scratch
2. Analyze time and space complexity of algorithms
3. Solve coding interview problems efficiently
4. Choose appropriate data structures for different problems
5. Optimize algorithms for better performance

---

**Happy Learning! 🚀**

*Remember: The key to mastering DSA is consistent practice and understanding the underlying principles.* 
