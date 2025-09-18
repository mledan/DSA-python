# Minimum Spanning Tree - Topic 8

This directory contains implementations and exercises for minimum spanning tree algorithms, following the [W3Schools DSA Tutorial](https://www.w3schools.com/dsa/index.php).

## Learning Objectives

By the end of this topic, you will be able to:
- Understand minimum spanning tree concepts
- Implement Prim's algorithm
- Implement Kruskal's algorithm
- Compare different MST algorithms
- Apply MST algorithms to network design problems

## Topics Covered

### Part 1: Prim's Algorithm 🚧 (IN PROGRESS)
- [ ] MST problem understanding
- [ ] Prim's algorithm implementation
- [ ] Priority queue usage
- [ ] MST construction

### Part 2: Kruskal's Algorithm
- [ ] Union-Find data structure
- [ ] Kruskal's algorithm implementation
- [ ] Edge sorting and selection
- [ ] Cycle detection

### Part 3: Algorithm Comparison
- [ ] Time complexity analysis
- [ ] Space complexity comparison
- [ ] Use case scenarios
- [ ] Performance testing

### Part 4: Real-World Applications
- [ ] Network design
- [ ] Circuit design
- [ ] Clustering algorithms
- [ ] Image segmentation

## 🎯 YOUR TASK: Complete Part 1 - Prim's Algorithm

### **What You Need to Do:**

1. **Create the MST file** (`08_minimum_spanning_tree/prims.py`)
2. **Write comprehensive tests** (`08_minimum_spanning_tree/tests/test_prims.py`)
3. **Test your implementation**
4. **Commit and push to your branch**

### **Step-by-Step Instructions:**

#### **Step 1: Create the Prim's Algorithm File**
Create `08_minimum_spanning_tree/prims.py` with these components:

**Required Classes:**
- `WeightedGraph` class for MST input
- `MST` class for result storage

**Required Methods:**
- `__init__()` - Initialize weighted graph
- `add_vertex(vertex)` - Add vertex to graph
- `add_edge(vertex1, vertex2, weight)` - Add weighted edge
- `prims_algorithm(start_vertex)` - Find MST using Prim's algorithm
- `get_mst_edges()` - Get all edges in MST
- `get_mst_weight()` - Get total weight of MST
- `display_mst()` - Print MST structure

**Key Requirements:**
- Use priority queue for efficient implementation
- Handle disconnected graphs
- Include docstrings with time/space complexity
- Return both edges and total weight

#### **Step 2: Write Tests**
Create `08_minimum_spanning_tree/tests/test_prims.py` with test cases for:
- Normal MST calculations
- Edge cases (single vertex, disconnected graph)
- Weight verification

#### **Step 3: Test Your Code**
```bash
# Run your Prim's algorithm implementation
python 08_minimum_spanning_tree/prims.py

# Run your tests
python -m pytest 08_minimum_spanning_tree/tests/test_prims.py -v
```

#### **Step 4: Commit and Push**
```bash
git checkout -b topic-8-mst-prims
git add .
git commit -m "feat: implement Prim's minimum spanning tree algorithm

- Add WeightedGraph class for MST input
- Implement Prim's algorithm with priority queue
- Add MST weight calculation
- Handle disconnected graphs"

git push origin topic-8-mst-prims
```

### **Success Criteria:**
- ✅ Algorithm finds correct MST
- ✅ Tests pass (including edge cases)
- ✅ Proper weight calculation
- ✅ Docstrings include complexity analysis
- ✅ Ready for PR creation

## Time Complexity Reference

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Prim's | O((V + E) log V) | O(V) |
| Kruskal's | O(E log E) | O(V) |

## Learning Resources

- [W3Schools Minimum Spanning Tree](https://www.w3schools.com/dsa/dsa_intro_mst.php)
- [W3Schools Prim's Algorithm](https://www.w3schools.com/dsa/dsa_intro_prims.php)
- [W3Schools Kruskal's Algorithm](https://www.w3schools.com/dsa/dsa_intro_kruskal.php)
