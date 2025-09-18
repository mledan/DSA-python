# Maximum Flow - Topic 9

This directory contains implementations and exercises for maximum flow algorithms, following the [W3Schools DSA Tutorial](https://www.w3schools.com/dsa/index.php).

## Learning Objectives

By the end of this topic, you will be able to:
- Understand maximum flow problem fundamentals
- Implement Ford-Fulkerson algorithm
- Implement Edmonds-Karp algorithm
- Understand residual graphs and augmenting paths
- Apply maximum flow to network optimization problems

## Topics Covered

### Part 1: Ford-Fulkerson Algorithm 🚧 (IN PROGRESS)
- [ ] Flow network representation
- [ ] Residual graph concept
- [ ] Augmenting path finding
- [ ] Maximum flow calculation

### Part 2: Edmonds-Karp Algorithm
- [ ] BFS-based path finding
- [ ] Improved time complexity
- [ ] Implementation comparison
- [ ] Performance analysis

### Part 3: Advanced Flow Algorithms
- [ ] Push-relabel algorithm
- [ ] Dinic's algorithm
- [ ] Min-cost max-flow
- [ ] Bipartite matching

### Part 4: Real-World Applications
- [ ] Network capacity planning
- [ ] Transportation optimization
- [ ] Image segmentation
- [ ] Social network analysis

## 🎯 YOUR TASK: Complete Part 1 - Ford-Fulkerson Algorithm

### **What You Need to Do:**

1. **Create the maximum flow file** (`09_maximum_flow/ford_fulkerson.py`)
2. **Write comprehensive tests** (`09_maximum_flow/tests/test_ford_fulkerson.py`)
3. **Test your implementation**
4. **Commit and push to your branch**

### **Step-by-Step Instructions:**

#### **Step 1: Create the Ford-Fulkerson File**
Create `09_maximum_flow/ford_fulkerson.py` with these components:

**Required Classes:**
- `FlowNetwork` class with capacities
- `ResidualGraph` class for augmenting paths

**Required Methods:**
- `__init__()` - Initialize flow network
- `add_vertex(vertex)` - Add vertex to network
- `add_edge(vertex1, vertex2, capacity)` - Add edge with capacity
- `ford_fulkerson(source, sink)` - Find maximum flow
- `get_max_flow()` - Get maximum flow value
- `get_flow_edges()` - Get all edges with flow
- `display_flow()` - Print flow network

**Key Requirements:**
- Implement residual graph correctly
- Find augmenting paths using DFS
- Handle network constraints
- Include docstrings with time/space complexity

#### **Step 2: Write Tests**
Create `09_maximum_flow/tests/test_ford_fulkerson.py` with test cases for:
- Normal maximum flow calculations
- Edge cases (single path, multiple paths)
- Flow verification

#### **Step 3: Test Your Code**
```bash
# Run your Ford-Fulkerson implementation
python 09_maximum_flow/ford_fulkerson.py

# Run your tests
python -m pytest 09_maximum_flow/tests/test_ford_fulkerson.py -v
```

#### **Step 4: Commit and Push**
```bash
git checkout -b topic-9-maximum-flow-ford-fulkerson
git add .
git commit -m "feat: implement Ford-Fulkerson maximum flow algorithm

- Add FlowNetwork class with capacity constraints
- Implement Ford-Fulkerson algorithm with residual graph
- Add augmenting path finding
- Handle network flow optimization"

git push origin topic-9-maximum-flow-ford-fulkerson
```

### **Success Criteria:**
- ✅ Algorithm finds correct maximum flow
- ✅ Tests pass (including edge cases)
- ✅ Proper residual graph implementation
- ✅ Docstrings include complexity analysis
- ✅ Ready for PR creation

## Time Complexity Reference

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Ford-Fulkerson | O(E × max_flow) | O(V + E) |
| Edmonds-Karp | O(VE²) | O(V + E) |
| Push-Relabel | O(V²E) | O(V + E) |

## Learning Resources

- [W3Schools DSA Maximum Flow](https://www.w3schools.com/dsa/dsa_intro_maximumflow.php)
- [W3Schools Ford-Fulkerson](https://www.w3schools.com/dsa/dsa_intro_fordfulkerson.php)
- [W3Schools Edmonds-Karp](https://www.w3schools.com/dsa/dsa_intro_edmondskarp.php)
