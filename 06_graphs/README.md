# Graphs - Topic 6

This directory contains implementations and exercises for graph data structures, following the [W3Schools DSA Tutorial](https://www.w3schools.com/dsa/index.php).

## Learning Objectives

By the end of this topic, you will be able to:
- Understand graph fundamentals and representations
- Implement graph traversal algorithms (BFS, DFS)
- Detect cycles in graphs
- Understand directed vs undirected graphs
- Apply graphs to solve network problems

## Topics Covered

### Part 1: Graph Representation 🚧 (IN PROGRESS)
- [ ] Adjacency list implementation
- [ ] Adjacency matrix implementation
- [ ] Graph node and edge classes
- [ ] Graph construction methods

### Part 2: Graph Traversal
- [ ] Depth-First Search (DFS)
- [ ] Breadth-First Search (BFS)
- [ ] Traversal applications
- [ ] Path finding algorithms

### Part 3: Cycle Detection
- [ ] DFS-based cycle detection
- [ ] Union-Find algorithm
- [ ] Topological sorting
- [ ] Graph connectivity

### Part 4: Graph Applications
- [ ] Shortest path problems
- [ ] Minimum spanning tree
- [ ] Network flow algorithms
- [ ] Social network analysis

## 🎯 YOUR TASK: Complete Part 1 - Graph Representation

### **What You Need to Do:**

1. **Create the graph file** (`06_graphs/graph.py`)
2. **Write comprehensive tests** (`06_graphs/tests/test_graph.py`)
3. **Test your implementation**
4. **Commit and push to your branch**

### **Step-by-Step Instructions:**

#### **Step 1: Create the Graph File**
Create `06_graphs/graph.py` with these components:

**Required Classes:**
- `GraphNode` class with data and neighbors
- `Graph` class with adjacency list

**Required Methods:**
- `__init__()` - Initialize empty graph
- `add_node(data)` - Add new node to graph
- `add_edge(node1, node2)` - Add edge between nodes
- `remove_node(data)` - Remove node and its edges
- `remove_edge(node1, node2)` - Remove edge between nodes
- `get_neighbors(data)` - Get all neighbors of a node
- `has_edge(node1, node2)` - Check if edge exists
- `display()` - Print graph structure

**Key Requirements:**
- Support both directed and undirected graphs
- Handle duplicate nodes and edges
- Include docstrings with time/space complexity
- Implement adjacency list representation

#### **Step 2: Write Tests**
Create `06_graphs/tests/test_graph.py` with test cases for:
- Normal operations (add/remove nodes and edges)
- Edge cases (empty graph, single node)
- Graph properties (neighbors, edge existence)

#### **Step 3: Test Your Code**
```bash
# Run your graph implementation
python 06_graphs/graph.py

# Run your tests
python -m pytest 06_graphs/tests/test_graph.py -v
```

#### **Step 4: Commit and Push**
```bash
git checkout -b topic-6-graphs-representation
git add .
git commit -m "feat: implement graph data structure

- Add GraphNode and Graph classes
- Implement adjacency list representation
- Add node and edge operations
- Support directed and undirected graphs"

git push origin topic-6-graphs-representation
```

### **Success Criteria:**
- ✅ All methods work correctly
- ✅ Tests pass (including edge cases)
- ✅ Proper graph structure maintenance
- ✅ Docstrings include complexity analysis
- ✅ Ready for PR creation

## Time Complexity Reference

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Add Node | O(1) | O(1) |
| Add Edge | O(1) | O(1) |
| Remove Node | O(V + E) | O(1) |
| Remove Edge | O(1) | O(1) |
| Get Neighbors | O(1) | O(1) |
| DFS | O(V + E) | O(V) |
| BFS | O(V + E) | O(V) |

## Learning Resources

- [W3Schools DSA Graphs](https://www.w3schools.com/dsa/dsa_intro_graphs.php)
- [W3Schools Graph Implementation](https://www.w3schools.com/dsa/dsa_intro_graphs_implementation.php)
- [W3Schools Graph Traversal](https://www.w3schools.com/dsa/dsa_intro_graphs_traversal.php)
- [W3Schools Cycle Detection](https://www.w3schools.com/dsa/dsa_intro_graphs_cycles.php)
