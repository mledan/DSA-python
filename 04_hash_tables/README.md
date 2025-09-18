# Hash Tables - Topic 4

This directory contains implementations and exercises for hash table data structures, following the [W3Schools DSA Tutorial](https://www.w3schools.com/dsa/index.php).

## Learning Objectives

By the end of this topic, you will be able to:
- Understand hash table fundamentals and hash functions
- Implement hash tables with collision handling
- Create hash sets and hash maps
- Analyze hash table performance
- Apply hash tables to solve problems efficiently

## Topics Covered

### Part 1: Hash Table Basics 🚧 (IN PROGRESS)
- [ ] Hash function implementation
- [ ] Basic hash table structure
- [ ] Collision handling (chaining)
- [ ] Load factor and resizing

### Part 2: Hash Set Implementation
- [ ] Set operations (add, remove, contains)
- [ ] Union, intersection, difference
- [ ] Set applications

### Part 3: Hash Map Implementation
- [ ] Key-value pair storage
- [ ] Map operations (put, get, remove)
- [ ] Iteration and key management

### Part 4: Advanced Hash Techniques
- [ ] Open addressing (linear probing)
- [ ] Double hashing
- [ ] Consistent hashing
- [ ] Hash table optimization

## 🎯 YOUR TASK: Complete Part 1 - Hash Table Basics

### **What You Need to Do:**

1. **Create the hash table file** (`04_hash_tables/hash_table.py`)
2. **Write comprehensive tests** (`04_hash_tables/tests/test_hash_table.py`)
3. **Test your implementation**
4. **Commit and push to your branch**

### **Step-by-Step Instructions:**

#### **Step 1: Create the Hash Table File**
Create `04_hash_tables/hash_table.py` with these components:

**Required Classes:**
- `HashTable` class with collision handling

**Required Methods:**
- `__init__(capacity)` - Initialize hash table with given capacity
- `_hash(key)` - Hash function to convert key to index
- `put(key, value)` - Insert key-value pair
- `get(key)` - Retrieve value by key
- `remove(key)` - Delete key-value pair
- `contains(key)` - Check if key exists
- `size()` - Return number of elements
- `display()` - Print all key-value pairs

**Key Requirements:**
- Use chaining for collision resolution
- Handle key not found errors
- Include docstrings with time/space complexity
- Implement a simple hash function

#### **Step 2: Write Tests**
Create `04_hash_tables/tests/test_hash_table.py` with test cases for:
- Normal operations (put, get, remove)
- Collision handling
- Edge cases (empty table, key not found)

#### **Step 3: Test Your Code**
```bash
# Run your hash table implementation
python 04_hash_tables/hash_table.py

# Run your tests
python -m pytest 04_hash_tables/tests/test_hash_table.py -v
```

#### **Step 4: Commit and Push**
```bash
git checkout -b topic-4-hash-tables-basic
git add .
git commit -m "feat: implement basic hash table

- Add HashTable class with collision handling
- Implement put, get, remove, contains methods
- Add comprehensive test cases
- Handle collision resolution with chaining"

git push origin topic-4-hash-tables-basic
```

### **Success Criteria:**
- ✅ All methods work correctly
- ✅ Tests pass (including collision cases)
- ✅ Proper error handling for missing keys
- ✅ Docstrings include complexity analysis
- ✅ Ready for PR creation

## Time Complexity Reference

| Operation | Average Case | Worst Case | Space Complexity |
|-----------|-------------|------------|------------------|
| Insert | O(1) | O(n) | O(n) |
| Search | O(1) | O(n) | O(1) |
| Delete | O(1) | O(n) | O(1) |

## Learning Resources

- [W3Schools DSA Hash Tables](https://www.w3schools.com/dsa/dsa_intro_hashtables.php)
- [W3Schools DSA Hash Sets](https://www.w3schools.com/dsa/dsa_intro_hashsets.php)
- [W3Schools DSA Hash Maps](https://www.w3schools.com/dsa/dsa_intro_hashmaps.php)
