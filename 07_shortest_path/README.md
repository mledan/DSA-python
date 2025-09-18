# Shortest Path - Topic 7

This directory contains implementations and exercises for shortest path algorithms, following the [W3Schools DSA Tutorial](https://www.w3schools.com/dsa/index.php).

## Learning Objectives

By the end of this topic, you will be able to:
- Understand shortest path problem fundamentals
- Implement Dijkstra's algorithm
- Implement Bellman-Ford algorithm
- Compare different shortest path algorithms
- Apply shortest path algorithms to real-world problems

## Topics Covered

### Part 1: Dijkstra's Algorithm 🚧 (IN PROGRESS)
- [ ] Graph with weighted edges
- [ ] Priority queue implementation
- [ ] Dijkstra's algorithm implementation
- [ ] Path reconstruction

### Part 2: Bellman-Ford Algorithm
- [ ] Negative weight handling
- [ ] Bellman-Ford implementation
- [ ] Negative cycle detection
- [ ] Algorithm comparison

### Part 3: Advanced Shortest Path
- [ ] A* algorithm
- [ ] Floyd-Warshall algorithm
- [ ] Bidirectional search
- [ ] Performance optimization

### Part 4: Real-World Applications
- [ ] GPS navigation systems
- [ ] Network routing
- [ ] Game pathfinding
- [ ] Social network analysis

## 🎯 YOUR TASK: Complete Part 1 - Dijkstra's Algorithm

### **What You Need to Do:**

1. **Create the shortest path file** (`07_shortest_path/dijkstra.py`)
2. **Write comprehensive tests** (`07_shortest_path/tests/test_dijkstra.py`)
3. **Test your implementation**
4. **Commit and push to your branch**

### **Step-by-Step Instructions:**

#### **Step 1: Create the Dijkstra File**
Create `07_shortest_path/dijkstra.py` with these components:

**Required Classes:**
- `WeightedGraph` class with edge weights
- `PriorityQueue` class for Dijkstra's algorithm

**Required Methods:**
- `__init__()` - Initialize weighted graph
- `add_vertex(vertex)` - Add vertex to graph
- `add_edge(vertex1, vertex2, weight)` - Add weighted edge
- `dijkstra(start_vertex)` - Find shortest paths from start
- `get_shortest_path(start, end)` - Get path between two vertices
- `get_shortest_distance(start, end)` - Get distance between vertices

**Key Requirements:**
- Use priority queue for efficient implementation
- Handle disconnected graphs
- Include docstrings with time/space complexity
- Return both distances and paths

#### **Step 2: Write Tests**
Create `07_shortest_path/tests/test_dijkstra.py` with test cases for:
- Normal shortest path calculations
- Edge cases (single vertex, disconnected graph)
- Path reconstruction

#### **Step 3: Test Your Code**
```bash
# Run your Dijkstra implementation
python 07_shortest_path/dijkstra.py

# Run your tests
python -m pytest 07_shortest_path/tests/test_dijkstra.py -v
```

#### **Step 4: Commit and Push**
```bash
git checkout -b topic-7-shortest-path-dijkstra
git add .
git commit -m "feat: implement Dijkstra's shortest path algorithm

- Add WeightedGraph class with edge weights
- Implement Dijkstra's algorithm with priority queue
- Add path reconstruction functionality
- Handle disconnected graphs"

git push origin topic-7-shortest-path-dijkstra
```

### **Success Criteria:**
- ✅ Algorithm finds correct shortest paths
- ✅ Tests pass (including edge cases)
- ✅ Proper path reconstruction
- ✅ Docstrings include complexity analysis
- ✅ Ready for PR creation

## Time Complexity Reference

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Dijkstra's | O((V + E) log V) | O(V) |
| Bellman-Ford | O(VE) | O(V) |
| Floyd-Warshall | O(V³) | O(V²) |

## Learning Resources

- [W3Schools DSA Shortest Path](https://www.w3schools.com/dsa/dsa_intro_shortestpath.php)
- [W3Schools Dijkstra's Algorithm](https://www.w3schools.com/dsa/dsa_intro_dijkstra.php)
- [W3Schools Bellman-Ford](https://www.w3schools.com/dsa/dsa_intro_bellmanford.php)
